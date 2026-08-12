# docs — API

All read-only. This source never calls `new`, `append`, `tokens` or `webhooks`.

## Search

```
docs search <query> [--space <space>] [--limit <n>] [--phase <name>] --json
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

**Search is lexical, and that has a real consequence.** A page is found by what
its title and body say, so a note filed under a topic without naming it will not
appear in a search for that topic — at any `--limit`. Use `children` below to
walk the topic's subtree instead; the two find different things and neither
subsumes the other.

`--phase` filters to one phase, but a search result carries no phase name and
the table has no PHASE column. If a hit's phase matters, read it separately
with `pages` or `children`.

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
docs children <page>                         # immediate sub-pages
docs children <page> --all                   # the whole subtree, depth-first
docs backlinks <page> --direction outgoing   # what this note links to
docs backlinks <page> --direction incoming   # what links to it
```

`children` lists structurally rather than lexically, which is why it finds what
search cannot. Its table carries `slugId`, `title`, `updatedAt` and `PHASE` —
`updatedAt` is what a reference's locator needs, so `children` can replace the
`search --json` call when you already know the parent.

`--all` and `--phase` are mutually exclusive and the CLI rejects the
combination rather than guessing: `--all` walks unfiltered, so a phase filter
applied only to the immediate children would silently miss matching pages
deeper in the tree. The same restriction applies to `pages`.

A page's lifecycle state is also readable here:

```
docs phases                # the phases actually in use
docs phase <page>          # read one; prints nothing if unset
```

A phase is a single named state — `scaffold`, `writing`, `completed`, or any
name you invent — and a page has at most one. Names are normalised server-side,
so "In Progress" is stored as `in-progress`; `none` is reserved as the filter
value meaning *no phase*. `docs phases` lists only phases some page carries, so
an empty result means the workspace is not using them yet, which is the case at
the time of writing.

Reading a phase is in scope. **Setting or clearing one is not** —
`docs phase <page> <name>` and `--clear` write to your workspace.

A phase is deliberately not recorded in a reference: it is a mutable state on
your side rather than a property of the document's content, so unlike
`updatedAt` it says nothing about whether the harvested text still stands.

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
