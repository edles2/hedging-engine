from __future__ import annotations

import sys

from scripts import smoke_check


def test_smoke_check_fails_when_outputs_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["smoke_check.py", "--commodity", "wheat"])

    rc = smoke_check.main()

    assert rc == 1
