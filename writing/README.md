# Writing protocol

An **item** is a topic that motivates one or more posts. It is not a tag: a tag
groups finished posts, an item is the reason several posts get written at all.

Everything about one item lives in one directory. Human and agent follow the
same protocol described here.

## Layout

```
writing/items/{YYYY-MM-DD}-{tag}/
  planning.md      what posts this item yields, and why
  state.md         where the item is now (front matter is authoritative)
  publish.md       metadata Hugo needs (front matter is authoritative)
  manner.md        voice and audience, then formatting and citation rules
  sources/         which sources to draw on, and the queries used
  references/      material actually harvested, one file per reference
  docs/{lang}/     successive drafts, never overwritten
  editing/{lang}/  editing passes, ending in final.md
```

The item id is `{YYYY-MM-DD}-{tag}`. The tag must match
`^[a-z0-9]+(-[a-z0-9]+)*$`, because it is also the default publish slug. A
same-day collision on the same tag takes a `-2` suffix.

## Stages

`state.md` front matter carries a `stage` from this fixed set. Nothing enforces
the order — the vocabulary exists so items can be reported on, not to gate you.

| Stage | Done when |
|---|---|
| `planning` | `planning.md` and `manner.md` are filled in; the posts are named |
| `gathering` | `sources/` records which sources to use and the queries |
| `drafting` | at least one draft per declared language in `docs/{lang}/` |
| `editing` | `editing/{lang}/final.md` exists for every declared language |
| `published` | `publish.py` has written into `content/` and it is committed |

Per-language progress is tracked separately, since languages advance at
different speeds:

```yaml
---
stage: drafting
languages:
  ko: drafting        # not-started | drafting | editing | done
  en: not-started
updated: 2026-08-10
---
```

Whoever advances the item updates `state.md`, human or agent.

## Walkthrough

**1. Create the item.**

```bash
make new TAG=hugo-pipeline              # Korean only
make new TAG=hugo-pipeline LANG=ko,en   # both languages
```

**2. Plan.** Fill in `planning.md` and `manner.md`. `manner.md` matters more
than it looks: it is what an agent reads to sound like you rather than generic.

**3. Gather.** Decide which sources to use and record them in `sources/`, with
the actual queries. See `sources/README.md` for what is available and how each
one works.

**4. Harvest.** Pull material into `references/`, one file per reference, in the
normalized shape every source produces:

```
references/{YYYYMMDD}-{domain}-{slug}.md
```

Drafting never cares where a reference came from — that is the whole point of
the source contract.

**5. Draft.** Write into `docs/{lang}/{slug}-v{N}-{YYYYMMDD}.md`. Each version is
a new file. Never overwrite a draft; the history of how a piece got there is
worth keeping.

**6. Edit.** Work in `editing/{lang}/`, ending at `editing/{lang}/final.md`.
`final.md` holds **body text only** — no front matter. `publish.md` is where
metadata lives, and `publish.py` generates the front matter from it.

**7. Publish.**

```bash
make publish ITEM=2026-08-10-hugo-pipeline
```

This writes `content/{korean,english}/posts/{slug}.md` for every declared
language. Re-running overwrites, so fixing a typo is edit-and-republish. Then
commit and push; CI builds and deploys to GitHub Pages.

## Publish metadata

`publish.md` front matter is the single source of truth for everything Hugo
needs:

```yaml
---
slug: hugo-pipeline
languages: [ko, en]
date: 2026-08-10
tags: [hugo, blogging]
title:
  ko: "Hugo 글쓰기 파이프라인"
  en: "A Writing Pipeline for Hugo"
---
```

Required: `slug`, `languages`, `date`, `title`. `title` needs a non-empty entry
for every declared language. Optional: `tags`, `categories`, `author`, `draft`.

Generated files carry `item: {item-id}` in their front matter. That marker is
how `publish.py` recognizes files it owns; it refuses to overwrite hand-written
content in `content/` unless given `--force`.

## Languages

An item declares its own languages. `[ko]` is a perfectly good item — the
English side is simply never created. Adding `en` later means adding it to
`languages`, adding a `title.en`, and creating `docs/en/` and `editing/en/`.
