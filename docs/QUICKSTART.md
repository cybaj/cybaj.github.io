# Quickstart

Getting this repository running, and knowing what lives where.

For *writing* — items, stages, publishing — see [`writing/README.md`](../writing/README.md).
That document is the protocol; this one is the workshop.

## What this is

A [Hugo](https://gohugo.io) site using the [hugo-book](https://github.com/alex-shpak/hugo-book)
theme, bilingual (Korean and English), deployed to GitHub Pages at
<https://cybaj.github.io/>.

On top of it sits an authoring pipeline. An **item** is a topic that motivates
one or more documents — it is not a tag. You scaffold an item, gather sources
into it, draft, edit, and publish; publishing copies finished work into Hugo's
`content/` with generated front matter. An item produces either one flat blog
post or a whole subtree in the sidebar.

Hugo knows nothing about any of this. `content/` is ordinary Hugo content that
you can hand-edit or delete freely.

## Setup

**1. The theme is a git submodule.** Clone or fresh checkout leaves it empty,
and Hugo then fails with confusing `found no layout file` warnings rather than
saying the theme is missing:

```bash
git submodule update --init --recursive
ls themes/hugo-book/layouts   # should list 404.html, _default, partials, ...
```

Each git worktree gets its own submodule working tree, so run this again in
any worktree you create.

**2. Hugo, extended, version 0.145.0.** Extended because the theme compiles
SCSS; pinned because `.github/workflows/hugo.yaml` pins the same version, and
a mismatch means "works locally, fails in CI".

```bash
CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@v0.145.0
```

That needs a C compiler and takes a few minutes. `go install` writes to
`$(go env GOPATH)/bin` — usually `~/go/bin`, which is often **not** on `PATH`
even when the Go toolchain is. Link it somewhere that is:

```bash
ln -sf ~/go/bin/hugo ~/.local/bin/hugo
hugo version   # must print v0.145.0+extended
```

The prebuilt `hugo_extended_0.145.0_linux-amd64.tar.gz` from the Hugo releases
page works too and is faster, if you would rather not build.

**3. PyYAML**, for `scripts/publish.py`:

```bash
python3 -c "import yaml; print(yaml.__version__)"
```

`scripts/new_item.py` deliberately does **not** need it, so scaffolding works
on a machine without PyYAML. Don't add an import that breaks that.

**4. Check it works:**

```bash
make test     # 95 tests
make serve    # http://localhost:1313
```

## Repository map

| Path | What it is |
|---|---|
| `content/{english,korean}/` | Hugo content. Written by `publish.py`; safe to hand-edit. |
| `writing/README.md` | **The authoring protocol.** Read this before writing. |
| `writing/TEMPLATES/` | Files seeded into each new item. |
| `writing/items/` | One directory per item — drafts, sources, references, metadata. |
| `sources/` | The source contract: how each source produces a normalized reference. |
| `scripts/` | `new_item.py`, `publish.py`, `hierarchy.py`, `frontmatter.py`, `test_pipeline.py`. |
| `themes/hugo-book/` | Theme, as a git submodule. |
| `docs/superpowers/` | Design history — specs and implementation plans. Local only, gitignored. |
| `archive/hugo/` | The original demo scaffold. Nothing builds from it. |
| `TODO/` | Original design notes, superseded by `docs/superpowers/specs/`. Local only, gitignored. |
| `public/`, `resources/_gen/` | Generated. Gitignored. |

## Daily commands

```bash
make serve                          # dev server on :1313, live reload
make test                           # the pipeline test suite

make new TAG=my-topic               # new item, Korean, flat post
  LANGS=ko,en                       #   both languages
  DATE=2026-08-10                   #   backdate it (default: today)
  TARGET=docs                       #   a document tree instead of a post

make publish ITEM=2026-08-12-my-topic
  LANGS=ko                          #   publish one language only
  FORCE=1                           #   overwrite content this pipeline
                                    #   does not own — destructive
```

The scripts also run directly, and `--root` lets you point them at another
tree, which is how the tests drive them:

```bash
python3 scripts/new_item.py --help
python3 scripts/publish.py --help
```

## Writing

Three sentences, then go read the real thing.

`make new` scaffolds an item under `writing/items/{date}-{tag}/`. You fill in
`planning.md` and `manner.md`, gather material into `references/`, draft in
`docs/{lang}/`, and finish in `editing/{lang}/`. `make publish` then writes it
into `content/` — one file for a `posts` item, or a mirrored subtree for a
`docs` item, where the directories under `editing/{lang}/` *are* the tree.

Everything else — the stage vocabulary, the `publish.md` fields, `structure.md`,
orphan warnings — is in [`writing/README.md`](../writing/README.md).

## Deployment

Pushing to `main` triggers `.github/workflows/hugo.yaml`, which builds with
Hugo 0.145.0 extended and deploys to GitHub Pages. **Nothing else deploys.**
Local commits, local merges, and pushes to other branches are all safe.

CI overrides `baseURL` at build time, so the value in `hugo.toml` only affects
local preview.

## Gotchas

**The submodule.** Covered above, but it is the single most likely reason a
fresh checkout won't build, and the error message doesn't say so.

**Hugo must be the extended build.** A plain build fails on the theme's SCSS.
`hugo version` must show `+extended`.

**`FORCE=1` destroys things.** It overwrites content in `content/` that the
pipeline does not own — a hand-written page, or one belonging to another item.
Without it, publish refuses and tells you why. That refusal is the safety net;
don't reach for `FORCE=1` to make an error go away without reading it first.

**Orphans are warnings, not errors.** Renaming a slug, dropping a language,
deleting a page from a tree, or switching `target` leaves the previously
published file in `content/`, still deploying. Publish names each one on
stderr and still exits 0 — deleting them is your call.

**`hugo.toml` still says `title = 'My New Hugo Site'`.** It shows in the
sidebar brand on every page. One line, whenever you want it.
