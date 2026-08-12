# Writing protocol

An **item** is a topic that motivates one or more documents — a flat post, or a
tree of pages. It is not a tag: a tag groups finished writing, an item is the
reason that writing happens at all.

Everything about one item lives in one directory. Human and agent follow the
same protocol described here.

## Layout

```
writing/items/{YYYY-MM-DD}-{tag}/
  planning.md      what documents this item yields, and why
  state.md         where the item is now (front matter is authoritative)
  publish.md       metadata Hugo needs (front matter is authoritative)
  manner.md        voice and audience, then formatting and citation rules
  structure.md     section overrides, docs items only
  sources/         which sources to draw on, and the queries used
  references/      material actually harvested, one file per reference
  docs/{lang}/     successive drafts, never overwritten
  editing/{lang}/  editing passes; for a docs item, the shape of the subtree
```

The item id is `{YYYY-MM-DD}-{tag}`. The tag must match
`^[a-z0-9]+(-[a-z0-9]+)*$`, because it is also the default publish slug. A
same-day collision on the same tag takes a `-2` suffix.

For a `docs` item, `docs/{lang}/` mirrors the same tree as `editing/{lang}/`,
so a page's draft history sits where you would look for it:

```
docs/ko/setup-v1-20260811.md
docs/ko/templates/basics-v1-20260811.md
docs/ko/templates/basics-v2-20260812.md
```

This is a convention for your own benefit — nothing enforces or reads it.

> **Two different `docs/`.** An item's `docs/` holds versioned drafts. Hugo's
> `content/{lang}/docs/` holds the published tree that becomes the sidebar.
> They share a name and nothing else.

## Stages

`state.md` front matter carries a `stage` from this fixed set. Nothing enforces
the order — the vocabulary exists so items can be reported on, not to gate you.

| Stage | Done when |
|---|---|
| `planning` | `planning.md` and `manner.md` are filled in; the documents are named |
| `gathering` | `sources/` records which sources to use and the queries |
| `drafting` | at least one draft per declared language in `docs/{lang}/` |
| `editing` | a `posts` item has `editing/{lang}/final.md` for every declared language; a `docs` item has the subtree it wants published |
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
make new TAG=hugo-pipeline                    # Korean only
make new TAG=hugo-pipeline LANGS=ko,en        # both languages
make new TAG=hugo-pipeline TARGET=docs        # document tree
make new TAG=hugo-pipeline DATE=2026-08-10    # backdate the item
```

`TARGET` is `posts` or `docs`; see [Flat post or document tree](#flat-post-or-document-tree).
`DATE` sets the item's date, which is both the `{YYYY-MM-DD}` in the item id
and the `date` in `publish.md` — it defaults to today, and you want it when
you are scaffolding an item for something already written.

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

**6. Edit.** Work in `editing/{lang}/`. A `posts` item ends at a single
`editing/{lang}/final.md`, whose body publishes under front matter generated
from `publish.md`. A `docs` item ends with the subtree you want published,
each file carrying its own front matter.

**7. Set the metadata.** Fill in `publish.md`. The scaffold leaves `title`
blank for every declared language, and `publish.py` refuses to publish an item
with a blank title — so this step is not optional:

```yaml
title:
  ko: "Hugo 글쓰기 파이프라인"
  en: "A Writing Pipeline for Hugo"
```

Check `slug` and `date` while you are there. The slug defaults to the tag you
scaffolded with and becomes the post's URL. See [Publish metadata](#publish-metadata)
below for the full field list.

**8. Publish.**

```bash
make publish ITEM=2026-08-10-hugo-pipeline
```

For a `posts` item — the default — this writes
`content/{korean,english}/posts/{slug}.md` for every declared language; a
`docs` item writes a subtree instead, see
[Flat post or document tree](#flat-post-or-document-tree). Re-running
overwrites, so fixing a typo is edit-and-republish. Then commit and push; CI
builds and deploys to GitHub Pages.

`LANGS` publishes one language instead of all of them — that is how you ship
the Korean post while the English one is still being drafted:

```bash
make publish ITEM=2026-08-10-hugo-pipeline LANGS=ko
```

(`LANGS` takes a comma list for `new`, which creates a directory per language,
and a single language for `publish`, which publishes one at a time.)

`FORCE=1` overwrites content in `content/` that this pipeline does not own —
a hand-written post or section page, or one belonging to another item. It is
how you take a slug over, and it destroys what was there:

```bash
make publish ITEM=2026-08-10-hugo-pipeline FORCE=1
```

Renaming a `slug`, dropping a language, deleting a page from a `docs` item's
tree, or switching `target` all leave already-published files sitting in
`content/`, still deploying. Publishing warns about every such orphan by name;
the publish itself still succeeds, and deleting the old files is your call.

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

Generated files carry `item: {item-id}` in their front matter — every file,
including the section pages publishing generates for you. That marker is how
`publish.py` recognizes files it owns; it refuses to overwrite hand-written
content in `content/` unless given `--force` (`FORCE=1` through `make`), and
it checks every file it is about to write before it writes any of them.

## Flat post or document tree

`publish.md` chooses where an item lands:

```yaml
target: docs        # docs | posts   (default: posts)
```

| `target` | destination | shape |
|---|---|---|
| `posts` | `content/{lang}/posts/{slug}.md` | one flat, dated post |
| `docs` | `content/{lang}/docs/{slug}/**` | a subtree in the sidebar |

Omitting `target` means `posts`, so nothing written before this existed
behaves differently.

For a `docs` item, **the directories under `editing/{lang}/` are the tree**.
Add a file, get a page; add a directory *with a document in it*, get a section.
Nothing lists them anywhere — the files are the source of truth. An empty
directory is not a section, because the tree is derived from the `.md` files
found in it; naming one in `structure.md` is then an error.

```
editing/ko/                    →  content/korean/docs/hugo-guide/
  setup.md                          _index.md         ← generated
  templates/                        setup.md
    basics.md                       templates/
                                      _index.md       ← generated
                                      basics.md
```

Each document carries its own front matter — `title`, `weight`, and any
hugo-book flag. `publish.md` fills the gaps with item-wide `date`, `tags`,
`categories`, `author` and `draft`. The document wins where both set a field;
the `item:` marker is always the pipeline's.

A document with no `title` takes the first `# H1` in its body, and failing
that its filename, with a warning.

## Section pages

Section `_index.md` files are generated during publishing — you never have to
write one, and a directory without one still becomes a section. You *may* add
one to give a section landing copy; see the end of this section.

Their titles come from `structure.md`, which lists only the sections you want
to customise — not an inventory of the tree:

```yaml
---
sections:
  templates:
    title: {ko: "템플릿", en: "Templates"}
    weight: 20
    bookCollapseSection: true
---
```

Recognised fields are `title` and `weight`; anything else passes straight into
the generated front matter, so every hugo-book flag works — `bookCollapseSection`,
`bookHidden`, `bookFlatSection`, `bookToc`.

Section paths are relative to `editing/{lang}/`, and the **root section is the
empty key** — that is how you give the subtree's own landing page a weight or
a theme flag:

```yaml
---
sections:
  "":
    weight: 1
    bookCollapseSection: true
---
```

Titles resolve in order: the entry in `structure.md`, then the item title from
`publish.md` for the root section, then the directory's own name — and that
last case warns, because on a bilingual site an undeclared Korean section
would otherwise appear under an English directory name without saying so.

`structure.md` may be empty or absent. A section named there with no matching
directory is an error.

> **A section page with no body is not a link.** hugo-book renders such a
> section in the sidebar as plain text: correctly nested, correctly titled,
> and unclickable. A generated `_index.md` has no body unless you write one,
> so every section is like this by default — which is fine for a pure grouping
> heading, and wrong the moment a reader expects a landing page there.

Giving it a body is the fix: create `editing/{lang}/<path>/_index.md`. Its body
is used, and its front matter fills gaps beneath the resolved section metadata —
`structure.md` still decides the title, so a section is never named two ways.

## Languages

An item declares its own languages. `[ko]` is a perfectly good item — the
English side is simply never created. Adding `en` later means adding it to
`languages`, adding a `title.en`, and creating `docs/en/` and `editing/en/`.

## Preview

```bash
make serve
```

Runs `hugo server` with the hugo-book theme over the same `content/` CI
deploys, on http://localhost:1313. It is what `make` with no target does.

**Restart it after publishing into a section that did not exist before.** The
server watches the directories it found at startup, so the first `docs` item —
or any item that creates a new top-level section — appears on disk and in a
fresh `hugo` build but keeps 404ing in the browser until you restart. Editing a
page inside a section it already knows about reloads normally.

## Tests

```bash
make test
```

Runs `scripts/test_pipeline.py`, which scaffolds and publishes items end to end
in a temporary directory. It touches nothing under `writing/` or `content/`.
