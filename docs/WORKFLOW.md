# Workflow

## Repo Workflow

This repo is a subject content repo. The normal workflow is:

1. Add or revise source metadata in `docs/SOURCE_CANON.md`, `docs/CANON_INTEGRATION_MAP.md`, and `curriculum/clear_reasoning_program.json`.
2. For comparative material, update `docs/CIVILIZATION_COVERAGE.md`, `docs/CULTURE_DIFFERENCE_FRAMEWORK.md`, `docs/CURRICULUM_MATRIX.md`, and `curriculum/civilization_reasoning_framework.json`.
3. For source excerpts or source-grounded lessons, create or update a source packet under `source-packets/` using `source-packets/TEMPLATE.md`.
4. Add lesson, module, practice, or assessment material under `study-plans/` or `exercises/`.
5. Update TODO evidence for completed curriculum work.
6. Run canonical verification.
7. Commit and push to `main`.

## Verification

Run:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked
```

The changed-scope verifier runs the clear reasoning curriculum checker when curriculum, schema, docs, exercises, or study plans change.

## Courseware Integration

`open-education-suite` should consume this repo as a subject content source. The platform owns ingestion, adaptive teaching, learner UI, learner state, package generation, and media production.

This repo owns:

- curriculum metadata
- source canon
- canon integration map
- study plans
- exercises
- assessment rubrics
- source-use boundaries

Courseware export surfaces are:

- `content-repo.json` for suite discovery and repository status.
- `study-plans/courses/CR-101-clear-reasoning-foundations.md` for suite-facing course structure.
- `objectives/clear-reasoning-objectives.md` for objective IDs.
- `assessments/clear-reasoning-assessment-bank.md` for assessment metadata.
- `misconceptions/misconceptions.md` for remediation signals.
- `generated-lectures/intro-foundations/lecture-video.json` for deterministic lecture fixture shape.

## Voice Studio Practice Contract

Voice Studio may record spoken explanations, objection handling, and disputation practice, but this repository must store only public-safe prompts, rubrics, objective IDs, transcript requirements, and scoring fields. Private audio, private transcripts, learner names, and review notes stay in learner-owned or platform-owned storage.

Recommended Voice Studio practice modes:

| Mode | Prompt Source | Evidence Stored Outside This Repo | Rubric Focus |
| --- | --- | --- | --- |
| Spoken explanation | weekly lecture blueprint | learner recording or transcript reference | order, precision, warrant defense |
| Objection handling | Objection Box and Question Ladder | objection response recording | fairness, concession, answer quality |
| Combative reset | Debate And Persuasion Practice Lab | pressure exchange recording | composure, term lock, tactic naming |
| Persuasive revision | persuasion-to-self-revision drill | before/after transcript reference | audience adaptation, dignity, changed mind path |
| Capstone defense | capstone portfolio | final defense recording reference | synthesis, clarity, revision after questions |

## Lecture And Video Production Handoff

Lecture production should use repo-authored outlines, objective IDs, board plans, and practice prompts. Generated media belongs outside this repo unless it is a deterministic fixture explicitly approved for public inclusion.

Each full lecture handoff should include:

1. course ID and objective IDs;
2. target duration and accessibility requirements;
3. board-work plan for definitions, argument maps, or proof steps;
4. source references by packet ID or link-only source reference;
5. no copied source text unless a packet authorizes excerpt use;
6. pause-practice prompts;
7. transcript/caption requirement;
8. practice artifact and assessment link.

Required lecture styles:

- board lecture for definitions, propositions, proof, inference, and evidence;
- seminar dialogue for dialectic, disagreement, and capstone defense;
- worked example for fallacy repair, word games, and hostile conversation reset;
- audience-adaptation rehearsal for rhetoric and persuasion.

## QA Live Readiness Contract

No learner-facing UI is owned by this repo today. Once a suite learner surface consumes this content, QA Live should validate that the UI can:

1. load CR-101 from the content repository manifest;
2. display weekly lecture, practice, objective, assessment, and source-reference data;
3. complete a representative drill without storing private learner data in this repo;
4. surface source-use boundaries and no-hidden-testing guidance;
5. run a Debate And Persuasion Practice Lab scenario;
6. record only public-safe report metadata, screenshots, and logs in the QA report path.

The first QA Live run-spec should be named `clear-reasoning-cr101-learner-flow` and should report the course load, objective visibility, practice launch, assessment prompt visibility, accessibility text, and source provenance checks.

## Offline AI Knowledge Store

This repo exposes the first course-owned offline AI knowledge seed for `open-education-suite`.

Seed files:

- `ai-knowledge/manifest.json` defines the Clear Reasoning store, privacy boundary, runtime profiles, retrieval policy, and writeback policy.
- `ai-knowledge/records.jsonl` lists public-safe retrieval records with source paths, summaries, tags, and retrieval terms.
- `content-repo.json` points the suite to the seed through `aiKnowledgeStore`.

Design rule: the suite owns the reusable schema, builder, local SQLite package, provider switching, and private overlay location. This content repo owns only public-safe course seed metadata. Local AIs may use Ollama through `ollama-local` or LM Studio through `lm-studio-local`, but model inventory, embeddings, private notes, learner data, and generated local databases stay outside this repo.

Allowed in the seed:

- course, objective, assessment, misconception, practice, source-boundary, source-index, lecture metadata, and workflow records;
- original repo-authored summaries;
- relative source paths and required citations;
- public-safe tags and retrieval terms.

Not allowed in the seed:

- private learner state, private notes, chat transcripts, recordings, embeddings, credentials, local absolute paths, or copied source text;
- AI-generated claims promoted into public seed records without human review and normal verification;
- learner-state mutation rules, which remain suite-owned checked code.

## Source Rules

Do not copy source text unless the edition or translation is public domain or otherwise licensed for reuse. Prefer source references and original exercises until source preservation packets exist.

Each source integration should answer:

1. What reasoning move does this source train?
2. What modern confusion does the move solve?
3. What drill builds it?
4. What assessment proves it?
5. What misuse must be prevented?

## Cross-Civilizational Rules

Western civilization is the primary spine for this program. Comparative material is used as contrast, enrichment, and correction only when cultural context and source boundaries are clear.

Before building a comparative lesson:

1. Confirm the lane exists in `docs/CIVILIZATION_COVERAGE.md`.
2. Record the culture lens fields from `docs/CULTURE_DIFFERENCE_FRAMEWORK.md`.
3. Map the unit in `docs/CURRICULUM_MATRIX.md`.
4. Apply `docs/REVIEWER_STANDARD.md`.
5. Keep the item reference-only until source packets and cultural review are ready.

## Source Packet Workflow

For Western spine lessons, create the packet first, then write the outline. The outline may use original summaries, drills, and assessments when the packet is approved for original lesson use, but it still may not copy source text.

For comparative lanes, create candidate packets first and leave them `needs_cultural_review`. Comparative lesson writing waits until the packet is reviewed.

Downstream tools should read `source-packets/index.json` for packet readiness instead of parsing packet Markdown directly.

## Future Integration Targets

- Content Courseware Kit metadata export.
- Assessment Mastery Engine rubrics and evidence contracts.
- Source Preservation Kit for public-domain edition evidence.
