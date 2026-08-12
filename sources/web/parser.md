# web — Parser

## Steps

1. Fetch the URL.
2. Take the main content region — `<article>`, `<main>`, or the densest text
   block. Ignore the rest of the page chrome.
3. Convert to markdown, keeping heading levels as they are.
4. Rewrite relative links and image sources to absolute, against the page URL.
   A relative link is useless once the page is a local file.
5. Decide the `type` — `documentation`, `article` or `paper` — using the rule
   in `format.md`. This is the one source where it is a judgment.
6. Prepend the front matter from `format.md`.

## Keep

Code blocks with their language tags, tables, headings, footnotes, and any
figure captions that carry meaning.

## Drop

Navigation, sidebars, ads, cookie banners, comment threads, social buttons,
"related posts" lists.

## Filename

- `{YYYYMMDD}` — the retrieval date, digits only
- `{domain}` — the registrable domain with dots as hyphens, `www.` stripped:
  `gohugo.io` → `gohugo-io`
- `{slug}` — the last meaningful path segment, lowercased, non-alphanumerics
  collapsed to single hyphens

`https://gohugo.io/hugo-modules/` retrieved on 2026-08-10 becomes
`20260810-gohugo-io-hugo-modules.md`.
