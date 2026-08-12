# docs — Formats

## Request

A `slugId`, or a query that yields one:

```
Tl5fQtxcuy
docs search hugo --json   →   slugId, title, updatedAt, space
```

## Raw

Two pieces, from two calls: a JSON metadata record from `search --json`, and
markdown on stdout from `read`.

## Result

One normalized reference file:

    references/{YYYYMMDD}-docs-{space}-{slugId}.md

````markdown
---
source: docs
type: note
url: docs://dev/Tl5fQtxcuy@2025-03-29T02:55:59.550Z
retrieved: 2026-08-12
title: "hugo"
---

# 설 치

```
brew install hugo
```

# CLI

https://gohugo.io/commands/
````

## Metadata

| Field | Value |
|---|---|
| `source` | always `docs` |
| `type` | always `note` — everything here is a personal note. A draft citing one renders the label (개인 노트 / personal note) so a reader can see the claim rests on private material they cannot check |
| `url` | `docs://{space}/{slugId}@{updatedAt}` — see below |
| `retrieved` | fetch date, `YYYY-MM-DD` |
| `title` | the page title from `search --json` |

### On the locator

`docs://{space}/{slugId}` addresses the page: `docs read {slugId}` retrieves it,
and the space records where it lived when harvested.

The `@{updatedAt}` suffix records **which version you read**. Be clear about
what that does and does not do: the server keeps no revision history, so this
cannot restore the text you saw. What it buys is a one-command drift check —
re-run `search --json` and compare the timestamps. Different means the note
moved under you, and the reference is describing something that no longer
exists in that form.

That is weaker than the `wiki` source's `?oldid=`, which genuinely retrieves the
exact revision. It is as much as this system allows, and recording it beats
guessing.
