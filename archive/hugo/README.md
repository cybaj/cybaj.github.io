# Archived Hugo scaffold

Nothing here is built or served. It is kept for reference only.

## `content/`

The `hugo-book` demo pages that shipped with the theme — `docs/example/`,
`docs/shortcodes/`, `test.md`, and the original lorem-ipsum `_index.md`
landing pages, in both languages.

The shortcode pages are the reason this is archived rather than deleted:
they are working examples of `columns`, `hints`, `tabs`, `details`, `katex`
and `mermaid`, which are useful to copy from when writing real posts.

They are also recoverable upstream from
<https://github.com/alex-shpak/hugo-book/tree/master/exampleSite>.

## `public/`

One stale build output, committed before `public/` was gitignored. CI rebuilds
the site from source on every push and uploads its own artifact, so nothing
depends on these files.
