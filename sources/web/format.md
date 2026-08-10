# web — Formats

## Request

A single absolute URL, `https://` preferred.

## Raw

An HTML document, occasionally markdown or plain text when the site serves it.

## Result

One normalized reference file:

    references/{YYYYMMDD}-{domain}-{slug}.md

```markdown
---
source: web
url: https://gohugo.io/hugo-modules/
retrieved: 2026-08-10
title: "Hugo Modules"
---

## Overview

Hugo Modules are the core building blocks...
```

## Metadata

| Field | Value |
|---|---|
| `source` | always `web` |
| `url` | the absolute URL fetched |
| `retrieved` | fetch date, `YYYY-MM-DD` |
| `title` | the page's `<h1>`, or its `<title>` if there is no `<h1>` |
