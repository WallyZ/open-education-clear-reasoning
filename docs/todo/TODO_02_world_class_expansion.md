# TODO 02 - World-Class Expansion

## Goal

Build this from a strong curriculum scaffold into a world-class reasoning, speaking, and discernment program that can be taught, practiced, tested, and integrated with the broader open-education ecosystem.

## Tasks

- [x] [P1] Expand the great-works canon and source integration map. <!-- yta:evidence paths="docs/SOURCE_CANON.md,docs/CANON_INTEGRATION_MAP.md,curriculum/clear_reasoning_program.json,scripts/lifecycle/check_clear_reasoning_program.py" id=clear-reasoning-expanded-canon -->
  - What: Add additional books/authors and define how each source family becomes reasoning practice, assessment, and transfer.
  - Acceptance: Canon includes classical, scholastic, inquiry/evidence, civic/moral, rhetoric/speech, global/comparative, and adversarial reasoning sources; curriculum metadata exposes advanced tracks and practice labs; deterministic verification enforces the expanded contract.
  - Evidence: Added `docs/CANON_INTEGRATION_MAP.md`, expanded `docs/SOURCE_CANON.md`, added `advanced_tracks` and `practice_labs` to `curriculum/clear_reasoning_program.json`, and tightened `scripts/lifecycle/check_clear_reasoning_program.py`.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260613_174411_c1512fd6.log`.

- [x] [P1] Add license-verified source packets for the first public-domain editions. <!-- yta:evidence paths="source-packets/,source-packets/index.json,scripts/lifecycle/generate_source_packet_index.py" id=clear-reasoning-source-packets -->
  - What: Create source packet records for Euclid and Aristotle editions before any source text excerpts are copied.
  - Acceptance: Each packet includes edition, translation, publication date, license/public-domain evidence, URL/library reference, excerpt boundary, and attribution.
  - Evidence: Western source packets, comparative candidate packets, deterministic `source-packets/index.json`, and the generator-backed drift check are present; copied source excerpts remain disabled.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P1] Add courseware metadata export for `open-education-suite` ingestion. <!-- yta:evidence paths="content-repo.json,study-plans/courses/CR-101-clear-reasoning-foundations.md,objectives/clear-reasoning-objectives.md,assessments/clear-reasoning-assessment-bank.md,misconceptions/misconceptions.md,generated-lectures/intro-foundations/lecture-video.json,docs/WORKFLOW.md" id=clear-reasoning-courseware-export -->
  - What: Export public-safe course metadata compatible with the ecosystem content-courseware contract.
  - Acceptance: Export includes course ID, modules, objectives, assessments, source refs, privacy boundary, and logical refs only.
  - Evidence: `content-repo.json` exposes suite discovery; CR-101, objectives, assessments, misconceptions, deterministic lecture fixture metadata, and workflow export surfaces provide public-safe ingestion metadata.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P1] Build the assessment item bank and mastery evidence map. <!-- yta:evidence paths="docs/ASSESSMENT_RUBRICS.md" id=clear-reasoning-assessment-bank -->
  - What: Add module-level essay, proof, dialogue, speech, and fallacy-repair assessments mapped to mastery bands.
  - Acceptance: Every module has at least one written assessment, one spoken assessment, one transfer case, and one revision path.
  - Evidence: Added `Mastery Evidence Map` to `docs/ASSESSMENT_RUBRICS.md` covering written assessment, spoken assessment, transfer case, and revision path for every foundation module.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260613_174411_c1512fd6.log`.

- [x] [P2] Add a debate and hostile-conversation practice lab. <!-- yta:evidence paths="exercises/reasoning-drills.md,study-plans/courses/CR-101-clear-reasoning-foundations.md,curriculum/clear_reasoning_program.json" id=clear-reasoning-debate-lab -->
  - What: Create progressive scripts and rubrics for friendly, skeptical, combative, and bad-faith opponents.
  - Acceptance: Practice protects truthfulness, charity, and safety while training composure under pressure.
  - Evidence: Added the Debate And Persuasion Practice Lab with pressure ladder, disingenuous-move recognition, response scripts, scenario bank, persuasion-to-self-revision drill, and observer scorecard; CR-101 now maps it into weekly lecture/practice.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P2] Add change-research practice for helping others see and sustain needed change. <!-- yta:evidence paths="docs/SOURCE_CANON.md,docs/CANON_INTEGRATION_MAP.md,curriculum/clear_reasoning_program.json,exercises/reasoning-drills.md,study-plans/courses/CR-101-clear-reasoning-foundations.md,assessments/clear-reasoning-assessment-bank.md,misconceptions/misconceptions.md" id=clear-reasoning-change-research-lab -->
  - What: Add public-safe research coverage for change facilitation, including readiness, ambivalence, autonomy, self-efficacy, implementation planning, habit design, reactance, social norms, adult learning, coaching, relapse repair, and ethical persuasion.
  - Acceptance: Learners practice helping another person see the need for change, own a concrete next step, and sustain revision without coercion, humiliation, hidden pressure, or copied proprietary materials.
  - Evidence: Added the Change Research canon shelf, integration lane, machine-readable source/track/lab metadata, CR-101 change standard, Change Facilitation Research Lab, assessment hooks, and misconception remediation.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_233428_19cae5a7.log`.

- [x] [P2] Integrate Voice Studio for spoken explanations and disputation practice. <!-- yta:evidence paths="docs/WORKFLOW.md,study-plans/courses/CR-101-clear-reasoning-foundations.md" id=clear-reasoning-voice-studio-integration -->
  - What: Define how `voice-studio` can record, review, and score spoken reasoning practice without storing private audio here.
  - Acceptance: This repo stores only public-safe practice metadata and rubrics; recordings stay in consumer-owned private storage.
  - Evidence: Added the Voice Studio Practice Contract with practice modes, prompt sources, external evidence storage, and rubric focus while preserving public-safe boundaries.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P2] Add generated lecture/video production hooks after content contracts stabilize. <!-- yta:evidence paths="docs/WORKFLOW.md,generated-lectures/intro-foundations/lecture-video.json,study-plans/courses/CR-101-clear-reasoning-foundations.md" id=clear-reasoning-video-hooks -->
  - What: Prepare handoffs for Video Studio and open-education-suite lecture generation.
  - Acceptance: Handoffs describe board work, proof visualization, dialogue reenactments, and accessibility requirements without generated media committed here.
  - Evidence: Added lecture/video production handoff requirements, required lecture styles, and full CR-101 weekly lecture/practice blueprints while keeping generated media outside this repo except deterministic fixtures.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P2] Add learner UI QA Live specs once a learner-facing surface exists. <!-- yta:evidence paths="docs/WORKFLOW.md" id=clear-reasoning-qa-live-ui -->
  - What: Define browser/operator tests for course navigation, drills, assessments, accessibility, and source provenance.
  - Acceptance: QA Live can open the learner surface, complete a representative drill, inspect feedback, and capture logs/screenshots.
  - Evidence: Added QA Live readiness contract and first run-spec name `clear-reasoning-cr101-learner-flow`; this content repo does not own a learner-facing UI, so execution belongs to the suite once it consumes CR-101.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260626_232427_7dd1d491.log`.

- [x] [P2] Add offline AI knowledge seed for local AI tutoring. <!-- yta:evidence paths="ai-knowledge/manifest.json,ai-knowledge/records.jsonl,content-repo.json,docs/WORKFLOW.md,scripts/lifecycle/check_clear_reasoning_program.py,scripts/lint/run_changed_scope.ps1" id=clear-reasoning-offline-ai-knowledge-seed -->
  - What: Expose public-safe Clear Reasoning retrieval records for the suite offline AI knowledge-store template.
  - Acceptance: The seed supports Ollama and LM Studio runtime profiles, requires citations, avoids private learner data and copied source text, keeps local overlays out of git, and is validated by canonical verification.
  - Evidence: Added the `ai-knowledge` manifest and record set, wired `content-repo.json`, documented the workflow, and extended the Clear Reasoning checker plus changed-scope routing.
  - Verification: Passed `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`; log `.codex-cache\logs\codex-verify_20260627_092021_f2a589c1.log`.

