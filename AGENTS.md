# AGENTS.md

## Mission

Minimize Codex usage, context growth, and command churn.
Make the smallest correct change that satisfies the task.

## Operating Model

This file is evergreen repo guidance.
Task-specific instructions belong in `.codex-cache/task-pack.md`.

At the start of every task:

1. Read this file.
2. If present, read `.codex-cache/task-pack.md`.
3. From the task pack, identify the smallest relevant file set before coding.
4. State the intended verification command before editing.
5. Keep scope narrow and avoid unrelated cleanup.

If `.codex-cache/task-pack.md` is missing, create a minimal working plan from the user request and the smallest relevant file set. Do not broaden scope just to compensate for missing task-pack data.

## Scope Discipline

- Prefer the smallest safe patch over a refactor.
- Do not make incidental style, naming, formatting, dependency, or structural changes unless required.
- Do not scan the whole repo when the task can be solved from the task pack, changed files, repo docs, or a narrow search.
- If more than 3-5 files appear necessary, stop and justify why.
- Preserve existing behavior and public interfaces unless the user explicitly asks for change.

## Shell And Tool Policy

Use PowerShell-native commands on Windows unless the repo already requires a different tool.

Prefer:

- `Select-String` for narrow text searches.
- `Get-ChildItem` and `Where-Object` for file discovery.
- `Get-Content` for file reads.
- repo-checked PowerShell or Python scripts over shell one-liners.
- existing repo scripts before inventing new commands.

Do not install new tools, global packages, or dependencies unless the user explicitly asks.

## Codex Cache

- `.codex-cache/task-pack.md` is task-specific input and should not be committed.
- Generated task packs may come from a repo upgrade plan or a selected TODO ready-queue item.
- Verification logs belong under `.codex-cache/logs/`.
- Temporary artifacts belong under `.codex-cache/tmp/<run-id>/`.
- Do not write ad hoc temp files elsewhere in the repo.

## Memory-Bank

Use `memory-bank/` to keep durable context compact:

- `memory-bank/activeContext.md`: current objective and next actions.
- `memory-bank/progress.md`: completed/in-progress/next state.
- `memory-bank/context-pack.md`: compact must-read context for the next wave.
- `memory-bank/HANDOFF.md`: concise handoff package for local or cloud runtime transfer.
- `memory-bank/repoKitCatalog.md`: repo-kit capability snapshot.
- `memory-bank/solutionHarvest.md`: reusable solution capture.
- `memory-bank/commonPitfalls.md`: recurring failure symptoms and fixes.

Refresh memory when a wave changes direction or before handoff:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\memory\refresh_memory_bank.ps1 -RepoRoot . -ContextProfile auto
```

For local AI, `32k` and `64k` profiles are intentionally aggressive. Cloud profile may keep richer context, but still remains bounded for cost and speed.

When a nontrivial failure is fixed and likely to recur, record it:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\memory\record_pitfall.ps1 -RepoRoot . -ErrorText '<failure>' -Solution '<fix>' -VerificationCommand '<passing command>'
```

`scripts/codex-verify.ps1` automatically writes failed verification output to `.codex-cache/pending-pitfalls/latest.json`.
After the fix passes, rerun verification with `-PitfallSolution '<short reusable fix>'` or `-PromptForPitfallSolution` to record it in `memory-bank/commonPitfalls.md`.

## Verification Contract

Use exactly one repo entrypoint for automated verification:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked
```

Do not run test runners directly unless the user explicitly asks.

Verification rules:

- State the exact verification command before editing.
- Use the repo verification entrypoint, not ad hoc test commands.
- Stream stdout and stderr live.
- Stop on the first failure.
- Preserve and report the real exit code.
- Report the log path on failure.

## Repository Workflow Mode

Default mode is solo-owner direct-main:

- Commit completed work on `main`.
- Push completed work to `origin/main`.
- Do not create feature branches or PRs unless a repo-local policy requires them.

To switch a repo to team/PR flow later, add `.repo-kit/workflow_policy.local.json`:

```json
{
  "mode": "team_pr",
  "default_branch": "main",
  "requires_pull_request": true
}
```

When that override exists, follow it and state why the work was not pushed directly to `main`.

## Post-TODO Completion Contract

After completing any TODO item or TODO-scoped wave:

1. Update the relevant TODO item in `docs/TODO.md` or `docs/todo/*.md`.
2. Mark completed items `[x]` only when evidence and verification are present.
3. Add follow-up TODOs for discovered project gaps, useful feature improvements, drift risks, or broad work that should be split.
4. Update all docs affected by the change, including `docs/DECISIONS.md` or `docs/adr/` for durable technical decisions.
5. Run the canonical verifier and every automatable TODO-specific QA Live or artifact gate.
6. Refresh memory-bank context when direction, status, reusable solutions, or pitfalls changed.
7. Record reusable fixes in `memory-bank/commonPitfalls.md` or `memory-bank/solutionHarvest.md` when they can save future work.
8. If QA Live cannot currently cover an automatable UI, game, Unreal, browser, VM, installer, or runtime behavior, add or update the repo-owned QA Live spec/contract or the adjacent `qa-live-test-system` capability before treating the gap as manual. Commit and push any required `qa-live-test-system` change to that repo's `main`.
9. Commit with a related message and push to `main` by default. Use branch/PR flow only when `.repo-kit/workflow_policy.local.json` or hosted branch protection requires it, and state that explicitly.
10. Recommend QA Live-first validation: name the `qa-live-test-system` contract, run-spec, capability check, expected result, and report path when the change affects UI, game, Unreal, browser, VM, installer, or runtime behavior. List user-only checks only for functionality that cannot be verified by automation or QA Live, and state why each one absolutely requires the user.

If the work is broad or touches more files than the task pack suggests, split it into smaller TODO items before continuing. If no TODO remains, run `scripts/status/next_work.ps1`, perform a bounded gap scan, and add a standard TODO for any valuable next improvement instead of silently stopping.

## Downstream Inheritance

Child repos should inherit this file unchanged where possible.
Put repo-specific workflow details in the child repo root `AGENTS.md`.
Put sub-area overrides in nested `AGENTS.override.md` files only when necessary.
Keep task-specific handoff material out of `AGENTS.md`.

For other agent surfaces, project this contract through `docs/AGENT_INSTRUCTIONS_COMPATIBILITY.md` and `repo-standards/agents/agent_instruction_compatibility.json`; do not maintain separate contradictory policies.
