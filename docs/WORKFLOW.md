# Workflow

## Repo Workflow

This repo is a subject content repo. The normal workflow is:

1. Add or revise source metadata in `docs/SOURCE_CANON.md` and `curriculum/clear_reasoning_program.json`.
2. Add lesson, module, practice, or assessment material under `study-plans/` or `exercises/`.
3. Update TODO evidence for completed curriculum work.
4. Run canonical verification.
5. Commit and push to `main`.

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
- study plans
- exercises
- assessment rubrics
- source-use boundaries

## Source Rules

Do not copy source text unless the edition or translation is public domain or otherwise licensed for reuse. Prefer source references and original exercises until source preservation packets exist.

## Future Integration Targets

- Content Courseware Kit metadata export.
- Assessment Mastery Engine rubrics and evidence contracts.
- Voice Studio practice for spoken explanations and disputation.
- Video Studio for lecture and board-work production.
- Source Preservation Kit for public-domain edition evidence.
- QA Live checks once a learner-facing UI exists.
