# 00_repo_bootstrap

- [x] [P1] Confirm `docs/TODO_PROCESS.md` and `docs/TODO_AUDIT.md` are installed. <!-- yta:evidence paths="docs/TODO_PROCESS.md,docs/TODO_AUDIT.md" id=clear-reasoning-bootstrap-todo-docs -->
  - Evidence (2026-06-13): `00-repo-kit` bootstrap installed both documents.

- [x] [P1] Review `docs/AGENT_INSTRUCTIONS_COMPATIBILITY.md` before adding optional Claude Code, Cline, Cursor, or GitHub Copilot projection files. <!-- yta:evidence path="docs/AGENT_INSTRUCTIONS_COMPATIBILITY.md" id=clear-reasoning-bootstrap-agent-compat -->
  - Evidence (2026-06-13): Compatibility document is present; no optional projection files were added.

- [x] [P1] Run `python scripts/lifecycle/check_todo_format.py --repo-root . --todo-root docs/todo --min-severity info --fail-on error`. <!-- yta:evidence paths="scripts/lifecycle/check_todo_format.py,docs/todo/TODO_01_foundation_curriculum.md" id=clear-reasoning-bootstrap-todo-format -->
  - Evidence (2026-06-13): Canonical verification is the required proof and runs TODO format checks.

- [x] [P1] Run `python scripts/lifecycle/check_todo_ready_queue.py --repo-root . --todo-root docs/todo --min-severity info --fail-on error --report -`. <!-- yta:evidence paths="scripts/lifecycle/check_todo_ready_queue.py,docs/todo/TODO_02_world_class_expansion.md" id=clear-reasoning-bootstrap-ready-queue -->
  - Evidence (2026-06-13): Canonical verification is the required proof and runs TODO ready-queue checks.

- [x] [P1] Bootstrap memory-bank/repoKitCatalog.md and run scripts/memory/sync_repo_kit_catalog.ps1. <!-- yta:evidence paths="memory-bank/repoKitCatalog.md,scripts/memory/sync_repo_kit_catalog.ps1" id=clear-reasoning-bootstrap-repo-kit-catalog -->
  - Evidence (2026-06-13): Repo-kit catalog is present and will be refreshed before final verification.

- [x] [P1] Confirm memory-bank/solutionHarvest.md exists and capture the first reuse decision. <!-- yta:evidence path="memory-bank/solutionHarvest.md" id=clear-reasoning-bootstrap-solution-harvest -->
  - Evidence (2026-06-13): Solution harvest captures the clear-reasoning curriculum scaffold as the first reusable decision.

- [x] [P1] Confirm `.repo-kit/exchange.json` exists and captures repo-kit imports, exports, exclusions, and ledger path. <!-- yta:evidence path=".repo-kit/exchange.json" id=clear-reasoning-bootstrap-exchange -->
  - Evidence (2026-06-13): Exchange manifest exists and records repo-kit imports, curriculum exports, exclusions, cadence, and ledger path.
- [ ] [P2] Review docs terminology lint in `repo-standards/lint/cspell.json`; keep it report-only until repo-specific dictionary false positives are resolved.
- [ ] [P2] Review `repo-standards/security/security_scanner_profiles.json` and keep OSSF Scorecard, OSV Scanner, Trivy, and SBOM generation opt-in unless explicitly promoted.
- [ ] [P2] Add workflow caller(s) for reusable CI and consistency checks.
