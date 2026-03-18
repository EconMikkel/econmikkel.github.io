from __future__ import annotations

from datetime import date
from pathlib import Path
import subprocess

import yaml


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "_data"
FILES_DIR = ROOT / "files"
INCLUDED_SECTION_TITLES = {
    "Journal articles",
    "Working papers and projects",
    "Non-academic work",
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def author_name(author: dict, coauthors: dict) -> str:
    if "key" in author:
        person = coauthors.get(author["key"], {})
        return person.get("name", author["key"])
    return author.get("name", "")


def join_authors(authors: list[dict], coauthors: dict) -> str:
    return ", ".join(filter(None, (author_name(author, coauthors) for author in authors)))


def item_meta(item: dict, coauthors: dict) -> str:
    bits: list[str] = []
    authors = join_authors(item.get("authors", []), coauthors)
    if authors:
        bits.append(authors)
    if item.get("venue"):
        bits.append(item["venue"])
    if item.get("status"):
        bits.append(item["status"])
    return " | ".join(bits)


def render_items(items: list[dict], coauthors: dict) -> str:
    blocks: list[str] = []
    for item in items:
        blocks.append(
            "\n".join(
                [
                    rf"\textbf{{{tex_escape(item['title'])}}}\par",
                    rf"{{\footnotesize {tex_escape(item_meta(item, coauthors))}}}\par"
                    if item_meta(item, coauthors)
                    else "",
                    rf"{tex_escape(item.get('summary', ''))}\par" if item.get("summary") else "",
                    r"\vspace{0.6em}",
                ]
            )
        )
    return "\n".join(blocks)


def included_sections(research: dict) -> list[dict]:
    return [
        section
        for section in research.get("sections", [])
        if section.get("title") in INCLUDED_SECTION_TITLES
    ]


def build_tex() -> str:
    config = load_yaml(ROOT / "_config.yml")
    research = load_yaml(DATA_DIR / "research.yml")
    coauthors = load_yaml(DATA_DIR / "coauthors.yml")

    author = config["author"]
    today = date.today().isoformat()
    sections_tex: list[str] = []

    for section in included_sections(research):
        items = section.get("items", [])
        content = render_items(items, coauthors) if items else r"{\footnotesize No items listed yet.\par}"
        sections_tex.append(
            "\n".join(
                [
                    rf"{{\sffamily\bfseries\color{{accent}} {tex_escape(section['title'])}\par}}",
                    r"\vspace{0.35em}",
                    content,
                    r"\vspace{0.55em}",
                ]
            )
        )

    return rf"""
\documentclass[10pt]{{article}}
\usepackage[a4paper,margin=14mm]{{geometry}}
\usepackage{{xcolor}}
\usepackage{{fontspec}}
\setmainfont{{Georgia}}
\setsansfont{{Arial}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.35em}}
\definecolor{{accent}}{{HTML}}{{C92A2A}}

\begin{{document}}

{{\sffamily\footnotesize Generated {today}\par}}
{{\sffamily\bfseries\fontsize{{24}}{{26}}\selectfont\color{{accent}} {tex_escape(author['name'])}\par}}
{tex_escape(author['bio'])}\par
{tex_escape(author['employer'])}\par

{{\sffamily\footnotesize Website: {tex_escape(config['url'])} \hfill Email: {tex_escape(author['email'])}\par}}
{{\sffamily\footnotesize Google Scholar: {tex_escape(author['googlescholar'])}\par}}
{{\sffamily\footnotesize ORCID: {tex_escape(author['orcid'])}\par}}

\vspace{{0.5em}}
\fcolorbox{{accent!15}}{{accent!4}}{{%
  \parbox{{0.97\linewidth}}{{%
    This one-page overview is intended for non-academic visitors who want a quick sense of the themes, collaborators, and applied relevance of my work.\par
    \textbf{{Main themes:}} migration and integration, survey methods, and applied policy evaluation.
  }}%
}}

\vspace{{0.9em}}
{'\n'.join(sections_tex)}

\vfill
{{\sffamily\footnotesize\color{{black!65}} Disclaimer: This PDF is generated automatically by OpenAI Codex when the website is updated. I do not guarantee that the information is correct.\par}}

\end{{document}}
"""


def main() -> None:
    FILES_DIR.mkdir(exist_ok=True)
    tex_path = FILES_DIR / "research-overview.tex"
    pdf_path = FILES_DIR / "research-overview.pdf"
    tex_path.write_text(build_tex(), encoding="utf-8")

    subprocess.run(
        [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory",
            str(FILES_DIR),
            str(tex_path),
        ],
        check=True,
        cwd=ROOT,
    )

    if not pdf_path.exists():
        raise RuntimeError("PDF generation did not produce research-overview.pdf")


if __name__ == "__main__":
    main()
