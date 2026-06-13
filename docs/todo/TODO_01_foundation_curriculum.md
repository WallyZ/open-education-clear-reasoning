# TODO 01 - Foundation Curriculum

## Goal

Create the first public-safe, machine-readable Clear Reasoning Foundations course scaffold grounded in Euclid, Aristotle, the trivium, dialectic, rhetoric, and original practice/assessment design.

## Tasks

- [x] [P1] Choose the repo name and mission boundary. <!-- yta:evidence paths="README.md,docs/PROGRAM_DESIGN.md" id=clear-reasoning-name-boundary -->
  - Evidence (2026-06-13): Selected `open-education-clear-reasoning` because the program is broader than logic alone and includes proof, dialectic, rhetoric, communication, and practical judgment.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [x] [P1] Add the course design, source canon, pedagogy, and assessment rubrics. <!-- yta:evidence paths="docs/PROGRAM_DESIGN.md,docs/SOURCE_CANON.md,docs/PEDAGOGY.md,docs/ASSESSMENT_RUBRICS.md" id=clear-reasoning-core-docs -->
  - Evidence (2026-06-13): Added the course mission, twelve-module architecture, source-use boundary, daily practice loop, pressure ladder, and capstone rubric.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [x] [P1] Add the first study plan and practice drill library. <!-- yta:evidence paths="study-plans/clear-reasoning-foundations/COURSE.md,exercises/reasoning-drills.md" id=clear-reasoning-course-drills -->
  - Evidence (2026-06-13): Added the Clear Reasoning Foundations course map and ten repeatable reasoning/speaking drills.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [x] [P1] Add a machine-readable curriculum contract and deterministic verifier. <!-- yta:evidence paths="curriculum/clear_reasoning_program.json,schemas/clear_reasoning_program.schema.json,scripts/lifecycle/check_clear_reasoning_program.py,scripts/lint/run_changed_scope.ps1" id=clear-reasoning-curriculum-contract -->
  - Evidence (2026-06-13): Added `open-education-clear-reasoning/program/v1` metadata, a schema file, and a stdlib checker wired into changed-scope verification.
  - Verification: `python scripts\lifecycle\check_clear_reasoning_program.py --repo-root .` passed before canonical verification.

## Acceptance Notes

- The repo contains no learner private data, generated media, private recordings, or copied copyrighted translations.
- The curriculum is structured enough for future ingestion by `open-education-suite`.
- Follow-up implementation is split into `TODO_02_world_class_expansion.md`.

