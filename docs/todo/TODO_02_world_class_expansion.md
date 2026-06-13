# TODO 02 - World-Class Expansion

## Goal

Build this from a strong curriculum scaffold into a world-class reasoning, speaking, and discernment program that can be taught, practiced, tested, and integrated with the broader open-education ecosystem.

## Tasks

- [x] [P1] Expand the great-works canon and source integration map. <!-- yta:evidence paths="docs/SOURCE_CANON.md,docs/CANON_INTEGRATION_MAP.md,curriculum/clear_reasoning_program.json,scripts/lifecycle/check_clear_reasoning_program.py" id=clear-reasoning-expanded-canon -->
  - What: Add additional books/authors and define how each source family becomes reasoning practice, assessment, and transfer.
  - Acceptance: Canon includes classical, scholastic, inquiry/evidence, civic/moral, rhetoric/speech, global/comparative, and adversarial reasoning sources; curriculum metadata exposes advanced tracks and practice labs; deterministic verification enforces the expanded contract.
  - Evidence: Added `docs/CANON_INTEGRATION_MAP.md`, expanded `docs/SOURCE_CANON.md`, added `advanced_tracks` and `practice_labs` to `curriculum/clear_reasoning_program.json`, and tightened `scripts/lifecycle/check_clear_reasoning_program.py`.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260613_174411_c1512fd6.log`.

- [ ] [P1] Add license-verified source packets for the first public-domain editions. <!-- yta:evidence paths="docs/SOURCE_CANON.md" id=clear-reasoning-source-packets -->
  - What: Create source packet records for Euclid and Aristotle editions before any source text excerpts are copied.
  - Acceptance: Each packet includes edition, translation, publication date, license/public-domain evidence, URL/library reference, excerpt boundary, and attribution.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [ ] [P1] Add courseware metadata export for `open-education-suite` ingestion. <!-- yta:evidence paths="curriculum/clear_reasoning_program.json,docs/WORKFLOW.md" id=clear-reasoning-courseware-export -->
  - What: Export public-safe course metadata compatible with the ecosystem content-courseware contract.
  - Acceptance: Export includes course ID, modules, objectives, assessments, source refs, privacy boundary, and logical refs only.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [x] [P1] Build the assessment item bank and mastery evidence map. <!-- yta:evidence paths="docs/ASSESSMENT_RUBRICS.md" id=clear-reasoning-assessment-bank -->
  - What: Add module-level essay, proof, dialogue, speech, and fallacy-repair assessments mapped to mastery bands.
  - Acceptance: Every module has at least one written assessment, one spoken assessment, one transfer case, and one revision path.
  - Evidence: Added `Mastery Evidence Map` to `docs/ASSESSMENT_RUBRICS.md` covering written assessment, spoken assessment, transfer case, and revision path for every foundation module.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260613_174411_c1512fd6.log`.

- [ ] [P2] Add a debate and hostile-conversation practice lab. <!-- yta:evidence paths="exercises/reasoning-drills.md" id=clear-reasoning-debate-lab -->
  - What: Create progressive scripts and rubrics for friendly, skeptical, combative, and bad-faith opponents.
  - Acceptance: Practice protects truthfulness, charity, and safety while training composure under pressure.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [ ] [P2] Integrate Voice Studio for spoken explanations and disputation practice. <!-- yta:evidence paths="docs/WORKFLOW.md" id=clear-reasoning-voice-studio-integration -->
  - What: Define how `voice-studio` can record, review, and score spoken reasoning practice without storing private audio here.
  - Acceptance: This repo stores only public-safe practice metadata and rubrics; recordings stay in consumer-owned private storage.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [ ] [P2] Add generated lecture/video production hooks after content contracts stabilize. <!-- yta:evidence paths="docs/WORKFLOW.md" id=clear-reasoning-video-hooks -->
  - What: Prepare handoffs for Video Studio and open-education-suite lecture generation.
  - Acceptance: Handoffs describe board work, proof visualization, dialogue reenactments, and accessibility requirements without generated media committed here.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

- [ ] [P2] Add learner UI QA Live specs once a learner-facing surface exists. <!-- yta:evidence paths="docs/WORKFLOW.md" id=clear-reasoning-qa-live-ui -->
  - What: Define browser/operator tests for course navigation, drills, assessments, accessibility, and source provenance.
  - Acceptance: QA Live can open the learner surface, complete a representative drill, inspect feedback, and capture logs/screenshots.
  - Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

