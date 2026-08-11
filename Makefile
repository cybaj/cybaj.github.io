.PHONY: default serve new publish test

default: serve

serve:
	hugo server --minify --theme hugo-book

# LANGS names the languages for both targets: a comma list for `new`, which
# creates a directory per language, and a single language for `publish`, which
# publishes one at a time. (It is LANGS, not LANG, because Make auto-imports
# the environment and LANG is the POSIX locale variable.)

# make new TAG=hugo-pipeline [LANGS=ko,en] [DATE=2026-08-10] [TARGET=docs]
new:
	@test -n "$(TAG)" || { echo "usage: make new TAG=<tag> [LANGS=ko,en] [DATE=YYYY-MM-DD] [TARGET=docs]"; exit 1; }
	python3 scripts/new_item.py "$(TAG)" \
		$(if $(LANGS),--lang "$(LANGS)",) \
		$(if $(DATE),--date "$(DATE)",) \
		$(if $(TARGET),--target $(TARGET),)

# make publish ITEM=2026-08-10-hugo-pipeline [LANGS=ko] [FORCE=1]
publish:
	@test -n "$(ITEM)" || { echo "usage: make publish ITEM=<item-id> [LANGS=ko] [FORCE=1]"; exit 1; }
	python3 scripts/publish.py "$(ITEM)" \
		$(if $(LANGS),--lang "$(LANGS)",) \
		$(if $(filter-out 0 no false,$(FORCE)),--force,)

test:
	python3 scripts/test_pipeline.py
