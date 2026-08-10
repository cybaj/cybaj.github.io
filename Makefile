.PHONY: default serve new publish test

# LANG is also the POSIX locale variable, and GNU Make auto-imports the
# environment — so without this reset, a bare `make publish ITEM=...` would
# expand $(LANG) to the shell's locale and pass `--lang C.UTF-8`. Scoped to
# the two targets that read it, so `serve` still hands hugo the real locale.
# A command-line LANG=ko,en outranks a target-specific assignment and wins.
new publish: LANG :=

default: serve

serve:
	hugo server --minify --theme hugo-book

# make new TAG=hugo-pipeline [LANG=ko,en] [DATE=2026-08-10]
new:
	@test -n "$(TAG)" || { echo "usage: make new TAG=<tag> [LANG=ko,en] [DATE=YYYY-MM-DD]"; exit 1; }
	python3 scripts/new_item.py "$(TAG)" \
		$(if $(LANG),--lang "$(LANG)",) \
		$(if $(DATE),--date "$(DATE)",)

# make publish ITEM=2026-08-10-hugo-pipeline [LANG=ko] [FORCE=1]
publish:
	@test -n "$(ITEM)" || { echo "usage: make publish ITEM=<item-id> [LANG=ko] [FORCE=1]"; exit 1; }
	python3 scripts/publish.py "$(ITEM)" \
		$(if $(LANG),--lang "$(LANG)",) \
		$(if $(FORCE),--force,)

test:
	python3 scripts/test_pipeline.py
