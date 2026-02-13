from __future__ import annotations

import pandas as pd
import pytest

from climate_index.global_index import compute_global_index


def test_compute_global_index_weighted_sum():
    silver_df = pd.DataFrame(
        {
            "date": ["2024-01-05", "2024-01-05", "2024-01-12", "2024-01-12"],
            "region_id": ["FR", "US", "FR", "US"],
            "temp_anom": [1.0, 0.0, 2.0, 0.0],
            "precip_anom": [0.0, 1.0, 0.0, 2.0],
        }
    )

    config = {
        "wheat": {
            "regions": [
                {"id": "FR", "weight": 0.6, "factors": {"temp_anom": 1.0, "precip_anom": 0.0}},
                {"id": "US", "weight": 0.4, "factors": {"temp_anom": 0.0, "precip_anom": 1.0}},
            ]
        }
    }

    out = compute_global_index(silver_df, "wheat", config)

    assert "global_risk_0_100" in out.columns
    assert "contrib_FR" in out.columns
    assert "contrib_US" in out.columns
    assert len(out) == 2

    for idx, row in out.iterrows():
        contrib_sum = row["contrib_FR"] + row["contrib_US"]
        assert row["global_risk_0_100"] == pytest.approx(contrib_sum)
