.PHONY: default serve new publish test

# LANG is a near-universal shell/locale environment variable (POSIX). GNU Make
# imports environment variables as makefile variables, so without this reset,
# an unset --lang on the command line (the documented default: publish every
# declared language) would silently pick up the shell's locale (e.g.
# "C.UTF-8") instead of being empty. This line makes the makefile's LANG
# start empty regardless of the inherited environment value, while
# `make new LANG=...` / `make publish LANG=...` on the command line still
# override it, per normal GNU Make precedence.
LANG :=

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
