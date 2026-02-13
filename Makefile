PYTHON ?= python
COMMODITY ?= wheat
PROFILE ?= balanced
ROLE ?= importer
EXPOSURE ?= 10000

.PHONY: help setup ingest climate market hedge full report smoke

help:
	@echo "Targets: setup ingest climate market hedge full report smoke"
	@echo "Example: make full COMMODITY=wheat PROFILE=balanced ROLE=importer EXPOSURE=10000"

setup:
	$(PYTHON) -m pip install -r requirements.txt

ingest:
	$(PYTHON) -m interface.cli ingest --commodity $(COMMODITY)

climate:
	$(PYTHON) -m interface.cli climate-index --commodity $(COMMODITY)

market:
	$(PYTHON) -m interface.cli market-model --commodity $(COMMODITY)

hedge:
	$(PYTHON) -m interface.cli hedge --commodity $(COMMODITY) --profile $(PROFILE) --role $(ROLE) --exposure $(EXPOSURE)

full:
	$(PYTHON) -m interface.cli full-run --commodity $(COMMODITY) --profile $(PROFILE) --role $(ROLE) --exposure $(EXPOSURE)

report:
	$(PYTHON) -m interface.cli report --commodity $(COMMODITY)

smoke:
	$(PYTHON) scripts/smoke_check.py --commodity $(COMMODITY)
