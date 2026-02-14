# Hedging Engine

Climate-informed commodity hedging pipeline with four stages:
1. Ingestion of weather/market/agri signals
2. Global climate risk index construction
3. ARIMAX-style market forecasting
4. Hedge recommendation + Streamlit reporting

## Online quickstart (uses external APIs)

### 1) Create environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the full pipeline
```bash
python -m interface.cli full-run \
  --commodity wheat \
  --profile balanced \
  --role importer \
  --exposure 10000
```

Or with `make`:
```bash
make full COMMODITY=wheat PROFILE=balanced ROLE=importer EXPOSURE=10000
```

### 3) Validate artifacts
```bash
python scripts/smoke_check.py --commodity wheat
# or: make smoke COMMODITY=wheat
```

## Offline smoke test (no external APIs)

30-second smoke command:
```bash
python -m interface.cli --help && pytest -q
```

This checks that:
- the CLI entrypoint is importable and callable
- the local smoke tests pass without network calls

## Step-by-step online commands

```bash
python -m interface.cli ingest --commodity wheat
python -m interface.cli climate-index --commodity wheat
python -m interface.cli market-model --commodity wheat
python -m interface.cli hedge --commodity wheat --profile balanced --role importer --exposure 10000
python -m interface.cli report --commodity wheat
```

## Repository structure

- `scripts/pull_all.py`: ingestion orchestrator writing silver-layer CSVs
- `ingestion/`: data clients and quality contracts
- `climate_index/`: regional/global climate score logic
- `market_models/`: ARIMAX fitting and forecasting logic
- `hedging/`: recommendation engine from forecast + risk inputs
- `interface/cli.py`: main command-line entrypoint
- `interface/streamlit_app.py`: dashboard app
- `configs/commodities.yaml`: commodity/region weighting config
- `visualization/`: charting/report utilities
- `utils/`: cache and documentation helpers

## Data flow and artifacts

Pipeline outputs are generated locally (not committed):

- Silver layer:
  - `data/silver/weather/weather_anomalies.csv`
  - `data/silver/market/market_prices.csv`
  - `data/silver/agri/agri_supply.csv`
  - `data/silver/silver_data.csv`
- Gold layer:
  - `data/gold/<commodity>_global_index.json`
  - `data/gold/<commodity>_forecast.json`
  - `data/gold/<commodity>_hedge_rec.json`

## Reproducibility notes

- Runtime dependencies are intentionally minimal in `requirements.txt`.
- Optional notebook/testing tooling lives in `requirements-dev.txt`.
- Use `make` targets for consistent local runs (`make help`).

## Additional docs

- `PROJECT_BRIEF.md`: project framing and readiness goals
- `ARCHITECTURE.md`: module/data flow and contracts
- `TASKS.md`: prioritized cleanup backlog and commit plan

## License

MIT (`LICENSE`).
