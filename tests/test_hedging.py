from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from hedging.advanced import recommend_hedge_from_arimax


def test_recommend_hedge_from_arimax_writes_output(tmp_path: Path):
    forecast_path = tmp_path / "wheat_forecast.json"
    risk_path = tmp_path / "wheat_global_index.json"

    pd.DataFrame(
        {
            "date": ["2024-01-05", "2024-01-12"],
            "price_forecast": [100.0, 103.0],
        }
    ).to_json(forecast_path, orient="records", indent=2)

    pd.DataFrame({"date": ["2024-01-12"], "global_risk_0_100": [82.0]}).to_json(
        risk_path, orient="records", indent=2
    )

    result = recommend_hedge_from_arimax(
        forecast_path=str(forecast_path),
        risk_index_path=str(risk_path),
        profile="balanced",
        role="importer",
        exposure=10000.0,
    )

    out_path = tmp_path / "wheat_hedge_rec.json"
    assert out_path.exists()
    assert 0.0 <= result["hedge_ratio"] <= 1.0
    assert result["instrument"] in {"long futures", "long call options", "short futures", "long put options"}

    persisted = json.loads(out_path.read_text())
    assert persisted["commodity"] == "wheat"
