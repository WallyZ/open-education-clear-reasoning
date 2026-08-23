# Context Pack

Use this compact context for a single focused wave.

Generated: 2026-08-23

## Context profile

- Profile: 32k (requested: auto)
- Profile note: Local AI 32k profile: extremely aggressive compression/cutting to stay within tight windows.
- Line budgets: activeContext<=90, progress<=120, context-pack<=60
- Text caps: max_items=3, max_line_length=120

## Objective

- Complete root-owned Markdown lint fleet Wave 45 while preserving all Clear Reasoning domain contracts.

## TODO source files scanned

- docs/TODO.md

## Must-read files

- memory-bank/activeContext.md
- memory-bank/progress.md
- docs/TODO.md

## Constraints

- Keep scope limited to shared lint assets, conservative Markdown repair, verifier composition, and current memory.
- Preserve curriculum meaning, source rights, cultural-review gates, and private/local knowledge boundaries.
- Keep notes compact; avoid raw logs and long transcripts.
- Prefer links over pasted dumps for large context.

## Acceptance criteria

- All policy-scanned tracked Markdown is clean and changed/full canonical verification passes.
- Existing curriculum checks still run, memory is current, and an independent critic approves the exact stage.

## Verification commands

- `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`
- `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode full -IncludeUntracked`
