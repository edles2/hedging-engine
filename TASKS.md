# TASKS

## Audit Findings
1. README is long but partially stale and not newcomer-efficient.
2. Reproducibility is weak due to bloated/duplicated dependencies.
3. Code layout has legacy/temporary artifacts that reduce clarity.
4. Data handling contracts exist implicitly in code, but are not clearly documented.

## 7-Commit Cleanup Plan
1. **Docs bootstrap**: add `PROJECT_BRIEF.md`, `ARCHITECTURE.md`, `TASKS.md`.
2. **Package hygiene**: fix `utils/__init__.py` import breakage.
3. **Layout cleanup**: remove temporary report app artifact.
4. **Reproducibility baseline**: slim `requirements.txt` + add `requirements-dev.txt`.
5. **Run ergonomics**: add `Makefile` with standard setup/run commands.
6. **Validation utility**: add smoke-check script for expected pipeline outputs.
7. **README overhaul**: concise quickstart + accurate module and data flow docs.

## Prioritized Backlog (Post-cleanup)
- Add sample fixture data for offline demo runs.
- Add contract tests for silver/gold schemas.
- Add CI job for lint + smoke checks.
- Add experiment tracking metadata for model runs.
