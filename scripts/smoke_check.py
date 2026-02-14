#!/usr/bin/env python3
"""Small smoke checks for expected pipeline outputs."""

from __future__ import annotations

import argparse
from pathlib import Path


EXPECTED = [
    Path("data/silver/silver_data.csv"),
    Path("data/silver/market/market_prices.csv"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate expected output artifacts exist.")
    parser.add_argument("--commodity", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    gold = [
        Path(f"data/gold/{args.commodity}_global_index.json"),
        Path(f"data/gold/{args.commodity}_forecast.json"),
        Path(f"data/gold/{args.commodity}_hedge_rec.json"),
    ]

    missing = [p for p in (EXPECTED + gold) if not p.exists()]
    if missing:
        print("[FAIL] Missing expected artifacts:")
        for path in missing:
            print(f"  - {path}")
        return 1

    print("[OK] All expected artifacts are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
