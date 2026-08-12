# Sources

A **source** is somewhere material comes from: the web, a wiki, your own
filesystem, an LLM transcript. Each source documents itself in five files so
that harvesting from it is repeatable.

Whatever the source, it emits reference files in **one normalized shape**. That
is the entire point: drafting never has to care where material came from.

## Available sources

| Source | Use for |
|---|---|
| [`web/`](web/) | Any public URL — docs, articles, posts |
| [`wiki/`](wiki/) | Wikipedia — orientation, terminology, and a route to primary sources |

## The normalized reference

Every harvested reference is one markdown file, written into an item's
`references/` directory:

```
references/{YYYYMMDD}-{domain}-{slug}.md
```

```markdown
---
source: web
url: https://gohugo.io/hugo-modules/
retrieved: 2026-08-10
title: "Hugo Modules"
---

<extracted markdown>
```

- `source` — the source directory name, so a reference can be traced back
- `url` — any locator: a URL, a file path, a video id
- `retrieved` — when it was pulled, since sources change under you
- `title` — human-readable, used when citing

## Adding a source

Copy `TEMPLATE/` to `sources/{name}/` and fill in all five files:

| File | Answers |
|---|---|
| `README.md` | What is this source good for, and when is it the wrong choice? |
| `api.md` | How do you search it, and how do you get one item? |
| `format.md` | Request, raw, result, and metadata shapes |
| `parser.md` | How raw data becomes a normalized reference |
| `usage.md` | Item-wide research versus per-post research |

Then add a row to the table above. Adding a source is five markdown files and
nothing else — no code changes.
