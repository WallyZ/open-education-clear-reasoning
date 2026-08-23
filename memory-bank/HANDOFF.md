# HANDOFF

Compact handoff package for local-context continuity.

## Metadata

- Last updated: 2026-08-23
- Handoff owner: repo maintainer
- Runtime target: local and cloud
- Context profile target: cloud
- Estimated token count: under 1000

## Must-Read Order (receiver)

1. `memory-bank/activeContext.md`
2. `memory-bank/progress.md`
3. `docs/TODO.md`
4. This file (`memory-bank/HANDOFF.md`)

## Current Objective

- Complete root-owned Markdown lint fleet Wave 45 without weakening the repo's curriculum contract.
- Active item: `RK_MARKDOWN_LINT_FLEET_ROLLOUT_001`; repo-local TODOs remain complete.

## Completed Since Last Handoff

- Clean full baseline retained; domain checks passed and six stale memory dates caused the expected failure.
- Shared dependency-free lint assets installed and conservative Markdown repairs applied.

## In Progress

- Corrected-candidate changed/full verification passed; independent promotion review remains pending.

## Next Commands (Max 5)

```powershell
# 1) pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked
# 2) pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode full -IncludeUntracked
# 3) git status --short
```

## Scope Guardrails

- Allowed: lint assets/integration, conservatively normalized Markdown, and memory-bank status.
- Out of scope: curriculum meaning, source rights/status, cultural-review gates, and private/local knowledge data.

## Open Risks / Blockers

- Optional external Markdown tools remain optional; the dependency-free guard is authoritative for this rollout.

## Verification Snapshot

- Full baseline -> failed only stale memory freshness after all selected domain checks passed.
- Corrected candidate changed -> PASS: `.codex-cache/logs/codex-verify_20260823_133555_225768d4.log`.
- Corrected candidate full -> PASS: `.codex-cache/logs/codex-verify_20260823_133614_8c871868.log`.
- Pending: independent promotion review and commit/push.

## Resume Checklist

- [ ] Re-run the listed verification commands.
- [ ] Confirm TODO status and evidence lines before new edits.
- [ ] Keep this handoff under the token budget and refresh date.
