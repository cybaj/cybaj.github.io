# wiki — API

The MediaWiki Action API, at `https://{lang}.wikipedia.org/w/api.php`.
`formatversion=2` gives a flatter JSON shape and is used throughout.

## Search

Always search first. Do not guess the page title — Korean titles frequently
differ from how the term is normally written:

```
GET https://ko.wikipedia.org/w/api.php
    ?action=query&list=search&srsearch=기계학습&srlimit=3
    &format=json&formatversion=2
```

Searching `기계학습` returns the article actually titled `기계 학습`, with a
space. Take the `title` from the result and use it verbatim in the next call.

## Get

One call returns the text, the revision id, and the counterpart article in
another language:

```
GET https://ko.wikipedia.org/w/api.php
    ?action=query&prop=extracts|revisions|langlinks
    &titles=기계 학습&rvprop=ids|timestamp&lllang=en
    &explaintext=1&format=json&formatversion=2
```

- `extracts` — the article text. `explaintext=1` gives plain text;
  drop it for HTML if you would rather convert that.
- `revisions` with `rvprop=ids` — the `revid`. **This is the important one**;
  it is what the reference's `url` pins to.
- `langlinks` with `lllang=en` — the English counterpart's title, or nothing
  if no article exists there.

## Rate limits

No published hard limit for reads. Make requests serially rather than in
parallel, and harvest a page once into a reference file rather than re-fetching
while drafting.

Wikimedia asks API clients to send a descriptive `User-Agent` identifying the
tool and a way to make contact. Requests with a default or empty one may be
refused.
