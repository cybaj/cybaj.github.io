# docs — Usage

## Item-wide research

Search here first, before any public source. You have probably already thought
about this topic and written something down, and starting from your own notes
means the item builds on your thinking rather than restating someone else's.

Search across spaces rather than guessing which one holds it — the same topic
is often split across `dev`, `ml` and wherever you were working at the time.

Then follow the trail: `backlinks --direction outgoing` on a promising note
shows what you linked it to, which is usually a better map of your own thinking
than another search.

## Per-post research

The specific note behind one claim — the reason you chose a tool, the thing
that surprised you, the number you measured once. Harvest that page rather than
the whole cluster.

## Cautions

- **Unpublishable by default.** Everything here comes from your own document
  server. Treat it as material that informs a post but does not appear in one,
  until you consciously decide otherwise for a specific page. `references/` is
  gitignored, so the harvested material stays local — but what you type into a
  draft does not, and a published post is a deploy away from the public web.

- **Space names are organisation, not permission.** `public` is a space name,
  not a licence; `private` is not more sensitive than `dev`. Decide per page,
  by reading it, not by where it happens to live.

- **A note is not a source.** It is your own past opinion, written with context
  you no longer have. If a claim matters, find what convinced you at the time
  and harvest that with `web`.

- **Notes move without history.** The `@updatedAt` in the locator records which
  version you read, but the server keeps no revisions — a changed timestamp
  tells you the note moved, not what it used to say. Re-read before relying on
  anything load-bearing.

- **Missing is ambiguous.** Exit code `5` covers forbidden and nonexistent
  alike, deliberately. A page vanishing from search does not tell you whether
  it was deleted or whether your token stopped being allowed to see it.
