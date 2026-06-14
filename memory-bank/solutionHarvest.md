# Solution Harvest

## Metadata

- Last updated: 2026-06-14
- Wave ID: clear-reasoning-civilization-framework-v1

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

- Candidate: civilization-reasoning-framework
  - Problem solved: Education repos need to compare reasoning traditions without flattening them into Western categories or treating cultural difference as a substitute for reasoning quality.
  - Reusable assets: docs/CIVILIZATION_COVERAGE.md, docs/CULTURE_DIFFERENCE_FRAMEWORK.md, docs/CURRICULUM_MATRIX.md, curriculum/civilization_reasoning_framework.json, schemas/civilization_reasoning_framework.schema.json
  - Reuse potential: high
  - Adopted this wave: yes; the curriculum checker validates primary Western lanes, comparative lanes, review gates, and build phases.

- Candidate: source-packet-rights-culture-gate
  - Problem solved: Great-works repos need one gate for source rights, excerpt boundaries, attribution, cultural caveats, misread risks, and reviewer status before lesson construction.
  - Reusable assets: docs/SOURCE_PACKET_SYSTEM.md, source-packets/TEMPLATE.md, schemas/source_packet.schema.json, docs/REVIEWER_STANDARD.md
  - Reuse potential: high
  - Adopted this wave: yes; source packet docs and schema are checked by the deterministic verifier.

## Promoted to Repo-Kit

- None in this wave. Candidate exports are recorded in `.repo-kit/exchange.json` for later review.

## Deferred / Not Reusable

- Learner submissions, private recordings, generated media, and copied source texts are intentionally excluded from this repo.

## Test Confirmation Notes

- Command(s) run: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`
- Expected outcome: curriculum docs, source boundaries, civilization framework, source packet schema/template, JSON contracts, TODO lifecycle, language lint, and memory-bank checks pass.
- Actual outcome: passed.
- Follow-up fix needed: no
