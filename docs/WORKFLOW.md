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
- Voice Studio practice for spoken explanations and disputation.
- Video Studio for lecture and board-work production.
- Source Preservation Kit for public-domain edition evidence.
- QA Live checks once a learner-facing UI exists.
