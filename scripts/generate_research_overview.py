from __future__ import annotations

from datetime import date
from pathlib import Path
import re

from reportlab.lib.colors import Color, HexColor, black, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
import yaml


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "_data"
FILES_DIR = ROOT / "files"
INCLUDED_SECTION_TITLES = {
    "Journal articles",
    "Working papers and projects",
    "Non-academic work",
}

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 14 * mm
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)
ACCENT = HexColor("#C92A2A")
TEXT = HexColor("#212529")
MUTED = HexColor("#6C757D")
PAPER = HexColor("#FFF8F4")
BORDER = HexColor("#EAD7CF")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def author_name(author: dict, coauthors: dict) -> str:
    if "key" in author:
        person = coauthors.get(author["key"], {})
        return person.get("name", author["key"])
    return author.get("name", "")


def included_sections(research: dict) -> list[dict]:
    return [
        section
        for section in research.get("sections", [])
        if section.get("title") in INCLUDED_SECTION_TITLES
    ]


def truncate_text(text: str, font_name: str, font_size: float, max_width: float) -> str:
    text = " ".join(text.split())
    if stringWidth(text, font_name, font_size) <= max_width:
        return text

    ellipsis = "..."
    trimmed = text
    while trimmed and stringWidth(trimmed + ellipsis, font_name, font_size) > max_width:
        trimmed = trimmed[:-1]
    return (trimmed.rstrip() + ellipsis) if trimmed else ellipsis


def wrap_text(text: str, font_name: str, font_size: float, max_width: float, max_lines: int) -> list[str]:
    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if stringWidth(candidate, font_name, font_size) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
            if len(lines) == max_lines - 1:
                break

    if len(lines) < max_lines:
        remaining_words = words[len(" ".join(lines + [current]).split()):]
        if remaining_words:
            current = " ".join([current] + remaining_words)
        lines.append(current)

    if len(lines) > max_lines:
        lines = lines[:max_lines]

    if len(lines) == max_lines:
        lines[-1] = truncate_text(lines[-1], font_name, font_size, max_width)

    return lines


def first_sentence(text: str) -> str:
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)
    return parts[0].strip()


def one_line_summary(item: dict) -> str:
    if item.get("summary"):
        return truncate_text(first_sentence(item["summary"]), "Times-Roman", 8.4, CONTENT_WIDTH - 12)

    status = item.get("status")
    venue = item.get("venue")
    if status and venue:
        base = f"{status} project in {venue}."
    elif venue:
        base = f"Project listed under {venue}."
    else:
        base = "Research project listed on the website."
    return truncate_text(base, "Times-Roman", 8.4, CONTENT_WIDTH - 12)


def draw_lines(pdf: canvas.Canvas, lines: list[str], x: float, y: float, font_name: str, font_size: float, color, leading: float) -> float:
    pdf.setFont(font_name, font_size)
    pdf.setFillColor(color)
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def draw_entry(pdf: canvas.Canvas, x: float, y: float, item: dict, available_width: float) -> float:
    title_lines = wrap_text(item["title"], "Helvetica-Bold", 9.2, available_width, 2)
    summary_line = one_line_summary(item)

    y = draw_lines(pdf, title_lines, x, y, "Helvetica-Bold", 9.2, TEXT, 10.5)
    y = draw_lines(pdf, [summary_line], x + 6, y + 1, "Times-Roman", 8.4, MUTED, 9.6)
    return y - 3


def main() -> None:
    config = load_yaml(ROOT / "_config.yml")
    research = load_yaml(DATA_DIR / "research.yml")
    FILES_DIR.mkdir(exist_ok=True)

    pdf_path = FILES_DIR / "research-overview.pdf"
    pdf = canvas.Canvas(str(pdf_path), pagesize=A4)
    y = PAGE_HEIGHT - MARGIN
    author = config["author"]

    pdf.setTitle("Research Overview")
    pdf.setAuthor(author["name"])

    pdf.setFont("Helvetica", 9)
    pdf.setFillColor(MUTED)
    pdf.drawString(MARGIN, y, f"Generated {date.today().isoformat()}")
    y -= 15

    pdf.setFont("Helvetica-Bold", 22)
    pdf.setFillColor(ACCENT)
    pdf.drawString(MARGIN, y, author["name"])
    y -= 20

    bio_lines = wrap_text(author["bio"], "Times-Roman", 10.2, CONTENT_WIDTH, 3)
    y = draw_lines(pdf, bio_lines, MARGIN, y, "Times-Roman", 10.2, TEXT, 12)

    employer_lines = wrap_text(author["employer"], "Times-Roman", 10.2, CONTENT_WIDTH, 2)
    y = draw_lines(pdf, employer_lines, MARGIN, y + 1, "Times-Roman", 10.2, TEXT, 12)
    y -= 6

    pdf.setFont("Helvetica", 8.6)
    pdf.setFillColor(MUTED)
    pdf.drawString(MARGIN, y, f"Website: {config['url']}  |  Email: {author['email']}")
    y -= 10
    pdf.drawString(MARGIN, y, f"Google Scholar: {author['googlescholar']}")
    y -= 10
    pdf.drawString(MARGIN, y, f"ORCID: {author['orcid']}")
    y -= 16

    box_height = 34
    pdf.setStrokeColor(BORDER)
    pdf.setFillColor(PAPER)
    pdf.roundRect(MARGIN, y - box_height + 6, CONTENT_WIDTH, box_height, 10, stroke=1, fill=1)
    pdf.setFillColor(TEXT)
    pdf.setFont("Times-Roman", 9.2)
    pdf.drawString(MARGIN + 10, y - 7, "This one-page overview is intended for non-academic visitors who want a quick sense of my work.")
    pdf.drawString(MARGIN + 10, y - 19, "Main themes: migration and integration, survey methods, and applied policy evaluation.")
    y -= box_height + 6

    bottom_reserve = MARGIN + 34
    note_added = False

    for section in included_sections(research):
        if y <= bottom_reserve:
            break

        pdf.setFont("Helvetica-Bold", 11.2)
        pdf.setFillColor(ACCENT)
        pdf.drawString(MARGIN, y, section["title"])
        y -= 12

        items = section.get("items", [])
        if not items:
            pdf.setFont("Helvetica", 8.5)
            pdf.setFillColor(MUTED)
            pdf.drawString(MARGIN, y, "No items listed yet.")
            y -= 12
            continue

        for index, item in enumerate(items):
            estimated_height = 26
            if y - estimated_height <= bottom_reserve:
                pdf.setFont("Helvetica-Oblique", 8.2)
                pdf.setFillColor(MUTED)
                pdf.drawString(MARGIN, y, "Additional items are available on the website.")
                y -= 10
                note_added = True
                break
            y = draw_entry(pdf, MARGIN, y, item, CONTENT_WIDTH)

        if note_added:
            break

        y -= 6

    pdf.setStrokeColor(Color(0, 0, 0, alpha=0.12))
    pdf.line(MARGIN, MARGIN + 16, PAGE_WIDTH - MARGIN, MARGIN + 16)
    pdf.setFont("Helvetica", 8.2)
    pdf.setFillColor(MUTED)
    pdf.drawString(
        MARGIN,
        MARGIN + 4,
        "Disclaimer: This PDF is generated automatically by OpenAI Codex when the website is updated. I do not guarantee that the information is correct.",
    )

    pdf.showPage()
    pdf.save()

    if not pdf_path.exists():
        raise RuntimeError("PDF generation did not produce research-overview.pdf")


if __name__ == "__main__":
    main()
