# Academic Website

This site has been simplified to three editing workflows:

1. Update homepage news in `_data/news.yml`
2. Update publications and projects in `_data/research.yml`
3. Publish blog-style notes by adding Markdown files to `_posts/`

## Where to edit

### Homepage news

Add a new item to the top of `_data/news.yml`:

```yml
- date: 2026-03-18
  title: "Short headline"
  body: "One or two sentences of context."
  link:
    label: "Read more"
    url: "https://example.com"
```

### Research outputs

Add items under the relevant section in `_data/research.yml`:

```yml
- title: "Paper title"
  year: 2026
  status: "Working paper"          # shown as pill badge; omit if not needed
  venue: "Series or journal"
  series: "Working Paper No. 1"    # optional; appended after venue with " · "
  authors:
    - key: "mette_foged"           # lookup from _data/coauthors.yml
    - name: "Mikkel Stahlschmidt"  # inline name (no lookup)
  summary: "Abstract text. HTML like <i>italics</i> is allowed."
  bibtex: |
    @unpublished{key2026,
      author = {Last, First and Last, First},
      title  = {Paper Title},
      year   = {2026},
      note   = {Working Paper Series No. 1},
      doi    = {10.xxxxx/xxxxx},
      url    = {https://example.com}
    }
  links:
    - label: "Paper"
      type: "paper"
      url: "https://example.com/paper"
      primary: true                # highlighted as the canonical version
    - label: "Older version"
      type: "paper"
      url: "https://example.com/old"
```

#### Entry types (`@unpublished` vs `@article`)

Use `@unpublished` for working papers, pre-registrations, and anything not yet in a journal. Use `@article` for published journal articles (add `journal`, `volume`, `number`, `pages` fields).

#### Link types

| `type`             | Icon              |
|--------------------|-------------------|
| `paper`            | file icon         |
| `preregistration`  | clipboard icon    |
| `code`             | code icon         |
| *(other/omitted)*  | external link     |

#### Primary links

When an entry has multiple links, mark the canonical/newest version with `primary: true`. Non-primary links render with a muted outline style. If no link is marked primary, all links render with the default style.

#### Co-authors

Frequent co-authors are defined once in `_data/coauthors.yml` and reused with `key`:

```yml
mette_foged:
  name: "Mette Foged"
  url: "https://example.com"
```

For one-off collaborators, use inline `name` (and optional `url`).

### Notes and blog posts

Create a new file in `_posts/` using the pattern `YYYY-MM-DD-title.md`.

Example:

```md
---
title: "A short note title"
excerpt: "One-sentence summary for the notes page."
---

Write the post here.
```

There is also a starter draft in `_drafts/note-template.md`.

