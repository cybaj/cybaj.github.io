# wiki — Parser

## Steps

1. Search for the term; take the exact `title` from the result.
2. Fetch `extracts|revisions|langlinks` for that title.
3. Note the `revid`. Build the reference's `url` as
   `https://{lang}.wikipedia.org/w/index.php?oldid={revid}`.
4. Convert the extract to markdown, keeping section headings at the level
   Wikipedia uses.
5. Prepend the front matter from `format.md`. `type` is always `encyclopedia`
   here — there is nothing to decide.
6. If `langlinks` returned a counterpart and you want it, repeat from step 2
   for that language — as a **separate** reference file, not an addition to
   this one.

## Keep

The lead section, the section headings, and the References or 각주 list. That
list is the reason to be here: it names what to read next.

Keep `[citation needed]` / `[출처 필요]` markers too. They tell you which claims
not to lean on, which is information you lose by tidying them away.

## Drop

Navigation boxes, infobox markup, edit links, coordinates, the category
footer, and image markup whose files you are not harvesting.

## Filename

The existing rule, unchanged — the language edition is already part of the
domain:

- `{YYYYMMDD}` — the retrieval date, digits only
- `{domain}` — `ko.wikipedia.org` → `ko-wikipedia-org`
- `{slug}` — the article title, lowercased, with letters and digits kept
  **including Hangul**, and every other character — spaces, punctuation,
  parenthesised disambiguators — collapsed to single hyphens

`기계 학습` from `ko.wikipedia.org` retrieved on 2026-08-12 becomes
`20260812-ko-wikipedia-org-기계-학습.md`, and its English counterpart becomes
`20260812-en-wikipedia-org-machine-learning.md`.
