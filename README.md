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
  status: "Working paper"
  venue: "Series or journal"
  authors:
    - key: "mette_foged"
    - name: "Mikkel Stahlschmidt"
  summary: "Short description."
  links:
    - label: "Paper"
      type: "paper"
      url: "https://example.com/paper"
    - label: "Code"
      type: "code"
      url: "https://github.com/..."
```

Frequent co-authors can be defined once in `_data/coauthors.yml` and then reused with `key`.
For one-off collaborators, you can still write:

```yml
- name: "Co-author Name"
  url: "https://coauthor-site.example"
```

Supported link types are `paper`, `preregistration`, and `code`.

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

