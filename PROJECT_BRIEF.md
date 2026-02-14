# PROJECT_BRIEF

## Project
Hedging Engine is a research-oriented pipeline that links climate stress signals to commodity market dynamics and produces explainable hedge recommendations.

## Core Goal
Given a commodity (for example `wheat`), the system should:
1. Pull and align market, weather, and agricultural supply data.
2. Build a global climate risk index.
3. Fit an ARIMAX-style forecast with uncertainty bands.
4. Convert model output into a practical hedge recommendation.
5. Display outputs in a Streamlit dashboard.

## Current Status (Audit Snapshot)
The repository has strong conceptual modules (`ingestion`, `climate_index`, `market_models`, `hedging`, `interface`) and runnable CLI entrypoints. However, it is currently "prototype-ready" more than "internship/research-ready" due to documentation drift and reproducibility gaps.

## Internship/Research Readiness Priorities
- Keep a single, clear execution path (`python -m interface.cli ...`).
- Make the structure auditable for newcomers in less than 15 minutes.
- Ensure dependencies are minimal and intentional.
- Keep data contracts explicit (what files are read/written by each stage).
- Provide a concrete task backlog with small, reviewable milestones.

## Main Outputs
Generated artifacts (not committed):
- `data/silver/silver_data.csv`
- `data/gold/<commodity>_global_index.json`
- `data/gold/<commodity>_forecast.json`
- `data/gold/<commodity>_hedge_rec.json`
