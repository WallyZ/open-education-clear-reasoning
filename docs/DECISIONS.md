# Decisions

Lightweight permanent decision log for repo-kit and downstream repos.

Use this file when a decision affects future maintenance but does not need a full ADR. Use `docs/adr/` for substantial architecture decisions, high-risk tradeoffs, or decisions that need alternatives and consequences.

## Format

```markdown
## YYYY-MM-DD - Decision Title

- Status: accepted | superseded | proposed
- Context: why the decision was needed.
- Decision: what will be done.
- Consequences: maintenance, rollout, or verification impact.
- Verification: command, report, or manual check that proves the decision is applied.
```

## 2026-06-04 - MIT License For Repo-Kit

- Status: accepted
- Context: The release governance backlog required an owner-approved repository license before downstream reuse could be treated as explicit rather than inferred.
- Decision: Repo-kit uses the MIT license recorded in root `LICENSE`.
- Consequences: Downstream standards updates may reference repo-kit's MIT license as the repo-kit source license, but must still preserve each downstream repo's owner-approved license and notice files instead of overwriting them.
- Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

## 2026-06-04 - Repo Health Self-Assessment Is Report-First

- Status: accepted
- Context: OpenSSF Best Practices and community-health review needs a durable local mapping without implying that live hosted GitHub settings or external badge submissions have already been completed.
- Decision: Repo-kit records `docs/REPO_HEALTH_SELF_ASSESSMENT.md` as the local self-assessment baseline. The report separates local file/script evidence from hosted GitHub confirmations and owner decisions, and downstream adoption stays report-first by default.
- Consequences: Scorecard and upgrade-planner gaps can point to the self-assessment doc, but automation must not submit live OpenSSF badge checks, change hosted GitHub settings, or overwrite downstream governance decisions without explicit owner approval.
- Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

## 2026-06-04 - Post-TODO Completion Contract

- Status: accepted
- Context: TODO work across downstream repos needs a consistent closeout path so completed items include evidence, docs, tests, memory updates, QA Live validation guidance, and clearly bounded user-only exceptions.
- Decision: Every TODO-scoped wave must follow the post-TODO completion contract in `AGENTS.md` and `docs/TODO_PROCESS.md`.
- Consequences: Agents must add follow-up TODOs for discovered gaps, update docs/decisions, run verification and required QA Live/artifact gates, refresh memory, record reusable pitfalls or solutions, commit/push according to repo policy, recommend QA Live-first validation for real functionality, and list user-only checks only when automation or QA Live cannot prove the behavior.
- Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.

## 2026-06-04 - Solo-Owner Main And QA Live Coverage Defaults

- Status: accepted
- Context: These repos are currently maintained by one owner, so branch/PR overhead creates friction; at the same time, automatable validation should move into `qa-live-test-system` rather than becoming manual user work.
- Decision: Repo-kit-managed repos default to solo-owner direct-main commit/push. Team/PR flow is opt-in through `.repo-kit/workflow_policy.local.json` or hosted branch protection. All automatable UI/game/Unreal/browser/VM/installer/runtime checks must run through QA Live; missing automatable coverage requires adding repo-owned QA Live specs/contracts or updating `qa-live-test-system` and pushing that repo to `main` before listing a user-only exception.
- Consequences: Agents should push completed waves to `origin/main` by default, improve QA Live coverage instead of asking for user-only checks, and reserve user-only verification for work that truly requires human judgment, private account access, physical hardware, or inaccessible credentials.
- Verification: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.
