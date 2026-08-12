# docs — Parser

## Steps

1. `docs search <query> --json`. Take `slugId`, `title`, `space.slug` and
   `updatedAt` from the match you want.
2. `docs read <slugId>` for the body. It arrives as markdown with nothing
   wrapped around it.
3. Assemble the locator: `docs://{space.slug}/{slugId}@{updatedAt}`.
4. Prepend the front matter from `format.md`. `type` is always `note` here —
   there is nothing to decide.

Two calls, not one — `read` carries no metadata and `search` carries no body.

## Keep

Everything. The body is already markdown written by you, with no navigation,
no advertising and no boilerplate to strip. This is the one source whose parser
is not mostly about discarding.

Keep the note's own headings even where they are terse or oddly capitalised
(`# 설 치`). They are how you organised the thought, and flattening them loses
that.

## Drop

Nothing.

If a note is too long to be useful as one reference, that is a signal to
harvest a narrower page rather than to trim this one. Look at what
`backlinks --direction outgoing` returns: the specific note you want is often
one link away.

## Filename

- `{YYYYMMDD}` — the retrieval date, digits only
- `docs` — literal, since there is no domain here
- `{space}` — the space slug, e.g. `dev`
- `{slugId}` — the page's slugId, verbatim

`hugo` from the `dev` space retrieved on 2026-08-12 becomes
`20260812-docs-dev-Tl5fQtxcuy.md`.

The slugId is used rather than a title slug on purpose. Note titles are short,
frequently duplicated (`hugo` and `hugo book` both exist), and often mixed
script — none of which makes a good unique filename. The slugId is unique,
stable, and the thing `docs read` actually takes.
