# docs

Your own document server, through the `docs` CLI.

## Good for

- Things only you know: your notes on a tool, a decision and the reason behind
  it, an idea you have been circling for months
- Recovering what you already worked out. Search before writing — you have
  probably thought about this before and written it down
- Following your own trail: `backlinks --direction outgoing` walks the links a
  note makes, which is often a better map of your thinking than search

## Not good for

- Anything you intend to quote. See `usage.md` — material from here informs a
  post, it does not appear in one.
- Anything you have not re-read recently. Notes rot faster than articles: they
  were written for the person you were at the time, with context you no longer
  have.
- Settling a fact. A note is your past opinion, not evidence. If it matters,
  find the primary source and harvest that with `web`.

## Requirements

The `docs` CLI on `PATH`, and an authenticated profile.

```
docs whoami    # profile, server, token scopes
docs health    # server, database, redis
```

`docs:read` is the only scope this source needs. Nothing here writes.
