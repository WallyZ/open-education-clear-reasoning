# Solution Harvest

## Metadata

- Last updated: 2026-06-13
- Wave ID: clear-reasoning-initial-scaffold-v1

## Candidate Reusable Solutions

- Candidate: clear-reasoning-curriculum-contract
  - Problem solved: Subject education repos need a public-safe way to expose course metadata, source boundaries, module maps, mastery bands, and capstone requirements without copying learner data or unlicensed source text.
  - Reusable assets: curriculum/clear_reasoning_program.json, schemas/clear_reasoning_program.schema.json, scripts/lifecycle/check_clear_reasoning_program.py
  - Reuse potential: high
  - Adopted this wave: yes; the initial repo uses the contract and changed-scope verifier.

- Candidate: great-works-source-boundary-pattern
  - Problem solved: Great-works education repos need to reference public-domain traditions while avoiding accidental inclusion of copyrighted translations or course assets.
  - Reusable assets: docs/SOURCE_CANON.md, docs/WORKFLOW.md
  - Reuse potential: high
  - Adopted this wave: yes; source text is reference-only until license-verified source packets exist.

## Promoted to Repo-Kit

- None in this wave. Candidate exports are recorded in `.repo-kit/exchange.json` for later review.

## Deferred / Not Reusable

- Learner submissions, private recordings, generated media, and copied source texts are intentionally excluded from this repo.

## Test Confirmation Notes

- Command(s) run: `python scripts\lifecycle\check_clear_reasoning_program.py --repo-root .`; `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`
- Expected outcome: curriculum docs, source boundaries, JSON contract, modules, privacy flags, capstone requirements, TODO lifecycle, language lint, exchange smoke, logging smoke, and memory-bank checks pass.
- Actual outcome: passed.
- Follow-up fix needed: no
