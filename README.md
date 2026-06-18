# Academic Website

A static Jekyll site styled as a New York Times–style editorial layout
(Newsreader + Libre Franklin, black-on-white, hairline/scotch rules). It has
three pages — **Home** (`/`), **Research** (`/research/`), **Notes** (`/notes/`) —
and three editing workflows:

1. Update homepage news in `_data/news.yml`
2. Update publications and projects in `_data/research.yml`
3. Publish blog-style notes by adding Markdown files to `_posts/`

You never edit HTML/CSS to add content — just the data files and posts below.

## Preview locally

```
bundle install                       # first time only
bundle exec jekyll serve --livereload
```

Then open <http://localhost:4000>. Edits to data files and posts reload
automatically; after editing `_sass/` or `_includes/`, hard-refresh the browser.

## Where to edit

### Homepage news (`_data/news.yml`)

Add a new item to the **top** of the list:

```yml
- date: 2026-03-18
  kicker: "Working Paper · In Press"   # optional small eyebrow above the headline
  title: "Short headline"
  body: "One or two sentences of context."
  link:                                # a single link …
    label: "Read more"
    url: "https://example.com"
  # … or several, using `links:` instead of `link:`
  # links:
  #   - label: "Venue A"
  #     url: "https://example.com/a"
  #   - label: "Venue B"
  #     url: "https://example.com/b"
```

The Home page shows the latest four items under "The Latest".

### Research outputs (`_data/research.yml`)

The file is a list of `sections`; add items under the relevant section's
`items:`. Sections with no items show their `empty_message` as an italic note.

```yml
- title: "Paper title"
  year: 2026
  status: "Working paper"          # shown in the metadata line, in accent colour
  venue: "Series or journal"
  series: "Working Paper No. 1"    # optional; appended after venue with " · "
  authors:
    - key: "mette_foged"           # lookup from _data/coauthors.yml
    - name: "Mikkel Stahlschmidt"  # inline name (no lookup) — your own name stays plain
  summary: "Abstract text. HTML like <i>italics</i> is allowed."
  bibtex: |
    @unpublished{key2026,
      author = {Last, First and Last, First},
      title  = {Paper Title},
      year   = {2026},
      url    = {https://example.com}
    }
  links:
    - label: "Working paper"
      url: "https://example.com/paper"
    - label: "RFBerlin version"
      url: "https://example.com/old"
      older: true                  # tucked under an "Older versions +" toggle
```

#### Two entry layouts (controlled by `summary`)

- **Has a `summary`** → full "working paper" layout: index number (`01`, `02`…),
  metadata line, author byline, **Read summary** and **BibTeX** toggles, and the
  version-links row.
- **No `summary`** → compact layout (used for older / RA work): metadata, title,
  byline, and links only. No abstract or BibTeX panel.

So: add a `summary` to give a paper the full treatment; leave it out for a short
entry.

#### Current vs. older version links

List every version under `links:`. The current/canonical versions show as
prominent accent links. Mark any superseded link with `older: true` and it moves
behind an **"Older versions +"** toggle, rendered de-emphasised. You can flag any
number of links this way. To add a published-version link later, just add another
entry to `links:` (leave `older` off so it shows as current).

> Note: the old `primary:` and `type:` fields are no longer used by the templates
> (arrows replaced the icons, and `older:` now controls emphasis). They're
> harmless if left in place, but you don't need them on new entries.

#### Co-authors (`_data/coauthors.yml`)

Frequent co-authors are defined once and reused with `key`. Their name becomes a
clickable link to their homepage; your own name (added inline with `name:`) stays
plain text.

```yml
mette_foged:
  name: "Mette Foged"
  url: "https://example.com"
```

For one-off collaborators, use an inline `name` (with an optional `url`).

### Notes and blog posts (`_posts/`)

Create a file named `YYYY-MM-DD-title.md`:

```md
---
title: "A short note title"
excerpt: "One-sentence summary shown in the notes list."
---

Write the post here.
```

When `_posts/` is empty the Notes page shows an empty-state block; once posts
exist they render as an editorial article list automatically.

## Tweaking the design

- **Accent colour:** change `--accent` in `_sass/layout/_custom.scss` (default
  editorial blue `#326891`; the design also suggests `#121212` or oxblood
  `#7a2e2e`).
- **Section headings, type, spacing, hairlines:** all live in
  `_sass/layout/_custom.scss` as CSS custom properties and component classes.
- **Masthead / nav / footer:** `_includes/masthead.html` and
  `_includes/footer.html`. The nav (`HOME · RESEARCH · NOTES`) sticks to the top
  when you scroll; the active page is detected from the URL.
- The expand/collapse and copy-to-clipboard behaviour is a few lines of inline
  vanilla JS in `_includes/research-entry.html` — no framework or build step.

Dark mode was removed as part of the editorial redesign; the site is
intentionally black-on-white.
