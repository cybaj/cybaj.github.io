# wiki — Formats

## Request

A language edition and a page title:

```
ko  기계 학습
en  Machine learning
```

The title must be the one Wikipedia uses, taken from a search result — not the
term as you would normally write it.

## Raw

JSON from the Action API: an `extracts` string, a `revisions` array carrying
`revid` and `timestamp`, and `langlinks` when a counterpart exists.

## Result

One normalized reference file:

    references/{YYYYMMDD}-{domain}-{slug}.md

```markdown
---
source: wiki
url: https://ko.wikipedia.org/w/index.php?oldid=39845983
retrieved: 2026-08-12
title: "기계 학습"
---

기계 학습(機械學習) 또는 머신 러닝은 …

## 개요

…

## 각주

1. …
```

## Metadata

| Field | Value |
|---|---|
| `source` | always `wiki` |
| `url` | **the permanent revision link**, `https://{lang}.wikipedia.org/w/index.php?oldid={revid}` — never the article URL |
| `retrieved` | fetch date, `YYYY-MM-DD` |
| `title` | the article title as Wikipedia spells it, including spacing |

The `url` is the one decision that matters here. An article URL shows whatever
the page says today; an `oldid` link shows the exact text you read, forever.
The contract defines `url` as "any locator", so pinning a revision needs no
extra field — and it makes this source's references verifiable in a way `web`'s
cannot be.
