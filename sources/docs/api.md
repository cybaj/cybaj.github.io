# docs — API

All read-only. This source never calls `new`, `append`, `tokens` or `webhooks`.

## Search

```
docs search <query> [--space <space>] [--limit <n>] --json
```

The text table shows only `slugId` and `title`. **Use `--json`** — the metadata
a reference needs is there and nowhere else:

```json
{
  "slugId": "Tl5fQtxcuy",
  "title": "hugo",
  "updatedAt": "2025-03-29T02:55:59.550Z",
  "space": { "slug": "dev" }
}
```

Search is not cursor-paginated; `--limit` is the only bound, and there is no
way to page further into the ranking.

## Get

```
docs read <slugId>
```

Prints **only the document body** to stdout — no title, no front matter, no
metadata — so redirection captures exactly the page. This is why harvesting is
two calls: `search --json` for the metadata, `read` for the body.

`--format` accepts `markdown` (default), `json`, `html`, `blocks`. Markdown is
what a reference wants; the `json` form is the editor's document tree, not
metadata.

To find neighbouring pages rather than one you already have:

```
docs backlinks <page> --direction outgoing   # what this note links to
docs backlinks <page> --direction incoming   # what links to it
```

## Re-checking

This section is an addition to the five-file contract, which asks only for
Search, Get and Rate limits. It is here because this source has no immutable
revision id, so how you detect drift is load-bearing rather than incidental —
see the locator note in `format.md`.

```
docs changes [--since <cursor>] [--space <space>]
```

A keyset delta feed, not a snapshot. The next cursor is written to **stderr**
as `next cursor: ...`, so capture it separately from the results.

A soft-deleted page stays in the feed with `changeType: "deleted"` rather than
vanishing — the server bumps its `updatedAt` on deletion. A harvested page that
later disappears is therefore detectable rather than silently stale.

## Rate limits

300 requests per minute; exceeding it exits `6`.

Exit codes worth handling: `3` authentication failed, `4` missing scope,
`5` forbidden **or** nonexistent — deliberately indistinguishable, so a page
missing from search does not tell you which — and `7` server unreachable.
