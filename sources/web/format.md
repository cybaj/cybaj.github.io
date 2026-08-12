# web — Formats

## Request

A single absolute URL, `https://` preferred.

## Raw

An HTML document, occasionally markdown or plain text when the site serves it.

## Result

One normalized reference file:

    references/{YYYYMMDD}-{domain}-{slug}.md

```markdown
---
source: web
type: documentation
url: https://gohugo.io/hugo-modules/
retrieved: 2026-08-10
title: "Hugo Modules"
---

## Overview

Hugo Modules are the core building blocks...
```

## Metadata

| Field | Value |
|---|---|
| `source` | always `web` |
| `type` | one of `documentation`, `article`, `paper` — chosen per page, since a URL can be any of them. See below |
| `url` | the absolute URL fetched |
| `retrieved` | fetch date, `YYYY-MM-DD` |
| `title` | the page's `<h1>`, or its `<title>` if there is no `<h1>` |

### Choosing the type

This is the only source where `type` is a judgment rather than a constant, so
decide by what the page *is*, not where it is hosted:

- `documentation` — maintained by whoever made the thing it describes, and
  expected to change as the thing changes. Official docs, a reference manual,
  a specification.
- `article` — written once by an author with a byline, and not maintained
  afterwards. Blog posts, news, tutorials.
- `paper` — published through some form of review, with a stable identity such
  as a DOI or arXiv id.

The distinction that matters is whether the page is expected to change. A draft
citing `documentation` is citing a moving target; a `paper` will still say the
same thing next year. When a page sits between two of these, prefer the one
that sets the lower expectation of stability.
