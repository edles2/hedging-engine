# ARCHITECTURE

## Runtime Flow
1. **Ingestion** (`scripts/pull_all.py`)
   - Pulls weather, market, and agri data.
   - Writes CSVs under `data/silver/` and merged `data/silver/silver_data.csv`.
2. **Climate Index** (`climate_index/global_index.py` via `interface/cli.py`)
   - Reads silver merged data + `configs/commodities.yaml`.
   - Computes regional contributions and `global_risk_0_100`.
   - Writes `data/gold/<commodity>_global_index.json`.
3. **Market Model** (`market_models/arimax.py` via `interface/cli.py`)
   - Reads market prices + global climate index.
   - Builds weekly return model and 8-step forecast.
   - Writes `data/gold/<commodity>_forecast.json`.
4. **Hedging** (`hedging/advanced.py` via `interface/cli.py`)
   - Reads forecast + risk index.
   - Produces hedge ratio, instrument suggestion, and rationale.
   - Writes `data/gold/<commodity>_hedge_rec.json`.
5. **Interface** (`interface/streamlit_app.py`)
   - Reads gold outputs + market history.
   - Displays KPIs, forecasts, confidence bands, and recommendation details.

## Repository Layout
- `climate_index/`: regional/global climate score logic.
- `configs/`: commodity and region config.
- `hedging/`: business decision layer from model outputs.
- `ingestion/`: external data clients and contracts.
- `interface/`: CLI + Streamlit dashboard.
- `market_models/`: ARIMAX prep, fitting, forecasting.
- `scripts/`: operational scripts (mainly ingestion orchestrator).
- `utils/`: cache and documentation helpers.
- `visualization/`: plotting/report helpers.

## Data Contracts
- Ingestion produces **silver** tables.
- Modeling and hedging produce **gold** JSON artifacts.
- Dashboard consumes gold artifacts and optional market silver history.

## Key Audit Gaps Found
- README content drift (claims and examples mismatched with code reality).
- Dependency drift (`requirements.txt` overly broad with duplicates).
- Package hygiene issue (`utils/__init__.py` imports missing modules).
- Presence of temporary app artifact (`interface/_report_app_tmp.py`).
- Missing contributor-facing docs for architecture and staged tasks.
