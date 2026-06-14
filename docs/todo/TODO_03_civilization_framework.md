# TODO 03 - Civilization Framework

## Goal

Make the program Western-primary while covering disciplined thought from multiple civilizations with explicit cultural-difference guardrails, source packet gates, reviewer standards, and build sequencing.

## Tasks

- [x] [P1] Create the civilization coverage map. <!-- yta:evidence paths="docs/CIVILIZATION_COVERAGE.md,curriculum/civilization_reasoning_framework.json" id=clear-reasoning-civilization-coverage -->
  - What: Define Western civilization as the main spine and comparative lanes for Indian, Islamic, Jewish, Chinese, African/oral, and related traditions.
  - Acceptance: Coverage map identifies program role, cultural difference to preserve, and build status for each lane.
  - Evidence: Added `docs/CIVILIZATION_COVERAGE.md` and `coverage_lanes` in `curriculum/civilization_reasoning_framework.json`.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Add the culture-difference framework. <!-- yta:evidence paths="docs/CULTURE_DIFFERENCE_FRAMEWORK.md,curriculum/civilization_reasoning_framework.json" id=clear-reasoning-culture-difference -->
  - What: Document how to compare traditions without flattening them into Western categories or treating culture as a substitute for reasoning quality.
  - Acceptance: Framework includes knowledge standard, argument goal, disagreement norm, authority structure, transferable moves, misread risks, and review status.
  - Evidence: Added `docs/CULTURE_DIFFERENCE_FRAMEWORK.md`; checker validates each coverage lane has cultural lens fields and misread risks.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Add the source packet system. <!-- yta:evidence paths="docs/SOURCE_PACKET_SYSTEM.md,source-packets/README.md,source-packets/TEMPLATE.md,schemas/source_packet.schema.json" id=clear-reasoning-source-packet-system -->
  - What: Add the packet lifecycle, required fields, approval rule, operator docs, template, and JSON schema.
  - Acceptance: Source packets gate edition/license evidence, excerpt boundaries, cultural caveats, misread risks, attribution, and reviewer status before source excerpts are used.
  - Evidence: Added `docs/SOURCE_PACKET_SYSTEM.md`, `source-packets/README.md`, `source-packets/TEMPLATE.md`, and `schemas/source_packet.schema.json`.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Add the curriculum matrix. <!-- yta:evidence paths="docs/CURRICULUM_MATRIX.md,curriculum/civilization_reasoning_framework.json" id=clear-reasoning-curriculum-matrix -->
  - What: Map course areas and advanced tracks to Western anchors, comparative lanes, cultural caveats, practices, and assessments.
  - Acceptance: Matrix preserves the Western spine and names comparative lanes as reviewed extensions rather than required unreviewed lesson content.
  - Evidence: Added `docs/CURRICULUM_MATRIX.md`; framework JSON includes matrix rules.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Add the reviewer standard. <!-- yta:evidence paths="docs/REVIEWER_STANDARD.md,curriculum/civilization_reasoning_framework.json" id=clear-reasoning-reviewer-standard -->
  - What: Define review categories and required checks for source rights, cultural setting, Western comparison, transfer limits, and cautious claims.
  - Acceptance: Comparative lessons are blocked unless source identity, rights, cultural context, misread risks, and transfer boundary are recorded.
  - Evidence: Added `docs/REVIEWER_STANDARD.md`; framework JSON includes review gates enforced by the checker.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Add the build order. <!-- yta:evidence paths="docs/BUILD_ORDER.md,curriculum/civilization_reasoning_framework.json" id=clear-reasoning-build-order -->
  - What: Define the build sequence: Western spine first, comparative guardrails second, reviewed comparative lessons third, practice/performance fourth, platform integration fifth.
  - Acceptance: Comparative lessons remain blocked until source packets and cultural review exist.
  - Evidence: Added `docs/BUILD_ORDER.md`; framework JSON includes required build phases.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_111209_b2592bb0.log`.

- [x] [P1] Create first Western source packets using the new template. <!-- yta:evidence paths="source-packets/" id=clear-reasoning-first-western-source-packets -->
  - What: Create approved packet records for Euclid, Aristotle `Categories`, Aristotle `Prior Analytics`, Aristotle `Rhetoric`, and one Plato dialogue.
  - Acceptance: Each packet records edition, translation, publication date, license/public-domain evidence, URL/library reference, excerpt boundary, cultural caveat, attribution, and review status.
  - Evidence: Added five Western source packets under `source-packets/western/`; all are `approved_for_original_lesson` and explicitly block copied source excerpts.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_112701_39a66a68.log`.

- [x] [P2] Add comparative source packet candidates for priority non-Western lanes. <!-- yta:evidence paths="source-packets/" id=clear-reasoning-comparative-source-packet-candidates -->
  - What: Add candidate packets for Nyaya, Buddhist logic, Islamic reasoning, Jewish legal reasoning, Chinese classical reasoning, and African/oral deliberative sources.
  - Acceptance: Candidates are explicitly marked `needs_cultural_review` or `needs_review` until source and cultural review is complete.
  - Evidence: Added six comparative candidate packets under `source-packets/comparative/`; each remains `needs_cultural_review` and reference-only.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_112701_39a66a68.log`.

- [x] [P2] Build first lesson outlines from the Western spine. <!-- yta:evidence paths="study-plans/,exercises/" id=clear-reasoning-first-western-lesson-outlines -->
  - What: Build lesson outlines for Euclidean proof, Aristotelian categories, syllogism, rhetoric, and dialectic using the new source-packet gates.
  - Acceptance: Each outline includes objective, source anchor, no copied source text, drill, assessment, revision path, and transfer case.
  - Evidence: Added `study-plans/western-spine-lessons/LESSON_OUTLINES.md` with five original packet-gated outlines and no copied source text.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_112701_39a66a68.log`.

- [x] [P1] Add machine-readable packet index for downstream ingestion. <!-- yta:evidence paths="source-packets/,schemas/" id=clear-reasoning-source-packet-index -->
  - What: Add a JSON index of source packets, packet status, source IDs, and lesson-readiness flags for courseware ingestion.
  - Acceptance: Index lists Western packets, comparative candidates, review status, and whether original lesson use or excerpt use is allowed.
  - Evidence: Added `source-packets/index.json`, `schemas/source_packet_index.schema.json`, exchange exports, and deterministic checks for packet paths, statuses, counts, and usage flags.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260614_121553_27dfe268.log`.

- [ ] [P2] Generate packet index from packet Markdown automatically. <!-- yta:evidence paths="source-packets/,scripts/lifecycle/" id=clear-reasoning-source-packet-index-generator -->
  - What: Add a deterministic script that rebuilds `source-packets/index.json` from packet Markdown front matter or structured fields.
  - Acceptance: Manual index drift is eliminated; verifier can fail when generated output differs from checked-in index.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.




