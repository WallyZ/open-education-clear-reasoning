# Cross-Repo Exchange

This document defines the repo-kit exchange loop: how downstream repos borrow useful assets from `00-repo-kit`, how they propose reusable local work back to `00-repo-kit`, and how drift stays visible without silent automation.

## Goal

- Let repos learn from `00-repo-kit` and from each other.
- Avoid duplicate local solutions for common problems.
- Keep shared process/tooling centralized without overwriting repo-specific behavior.
- Require explicit approval before applying any cross-repo changes.

## Authority Model

`00-repo-kit` is the canonical source for reusable process and tooling assets.
Downstream repos are canonical for their product code, domain docs, private artifacts, and repo-specific operating choices.

Exchange automation may propose changes. It must not silently apply, push, publish, delete, or rewrite files.

## Tracked State

Each downstream repo should keep `.repo-kit/exchange.json` with these sections:

- `repo`: repo identity, kind, owner, and default privacy classification.
- `cadence`: prompt interval, last prompt time, last catalog time, and idle-gate settings.
- `imports`: assets borrowed from `00-repo-kit`, including source path, target path, source ref, source hash, status, and override reason.
- `exports`: local reusable candidates shared or proposed back to `00-repo-kit`, including local path, proposed destination, category, privacy classification, status, and evidence.
- `exclusions`: paths/globs that must not be proposed for export.
- `ledger`: append-only exchange history path.

The canonical schema is `repo-standards/exchange/exchange.schema.json`.
The downstream template is `docs/templates/repo-kit/exchange.json`.

## Downstream Installation

`scripts/bootstrap/install_repo_standards.ps1` installs the exchange baseline into downstream repos:

- `.repo-kit/exchange.json`
- `.repo-kit/exchange.schema.json`
- `docs/CROSS_REPO_EXCHANGE.md`
- `scripts/exchange/**`

For existing repos, local `.repo-kit/exchange.json` content is preserved by default.
If it differs from the managed template, the installer reports a pending update instead of replacing local imports, exports, exclusions, or ledger settings.
Replacing the manifest requires both `-Force` and `-ResetExchangeManifest`.

## Privacy Classifications

Use the strictest reasonable classification:

- `public`: safe to share across repos.
- `internal`: repo/process information that is safe inside trusted private repos.
- `private`: owner/project content that must not be exported by automation.
- `secret`: credentials, tokens, private keys, `.env` values, or anything requiring rotation if exposed.
- `local_only`: machine-specific state or generated local artifacts.

Only `public` and approved `internal` items may become export proposals.
`private`, `secret`, and `local_only` items are hard exclusions.

## Idle Gate

A repo is eligible for an exchange prompt only when all are true:

- The configured cadence interval has elapsed.
- No staged changes exist.
- The working tree is clean, except configured allowed-dirty paths.
- No repo-kit exchange lock is present.
- No active task-pack lock is present.
- The operator is not in the middle of another verification or implementation flow.

The first implementation checks Git status and known lock files. Repos may add stricter local gates later.

## Watchdog Prompt

Use the watchdog command to check one or more repos without mutating them:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\watch_due.ps1 -RepoRoot F:\dev\youtube-automation -RepoKitRoot F:\dev\00-repo-kit
```

Use a repo list file for fleet checks. Blank lines and `#` comments are ignored:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\watch_due.ps1 -RepoListPath .\repo-standards\exchange\registered_repos.example.txt -RepoKitRoot F:\dev\00-repo-kit -ReportPath archive\local-reports\exchange_watchdog_report.json
```

Interactive prompting is explicit:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\watch_due.ps1 -RepoRoot F:\dev\youtube-automation -RepoKitRoot F:\dev\00-repo-kit -Prompt
```

Prompt choices are `review`, `postpone`, and `skip`.
The command prints review commands when `review` is selected.
It does not apply changes, update manifests, or push commits.

Optional scheduled use should run the watchdog in report mode only, then let the operator run `-Prompt` interactively.
Example Task Scheduler action:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File F:\dev\00-repo-kit\scripts\exchange\watch_due.ps1 -RepoListPath F:\dev\00-repo-kit\repo-standards\exchange\registered_repos.example.txt -RepoKitRoot F:\dev\00-repo-kit -ReportPath F:\dev\00-repo-kit\archive\local-reports\exchange_watchdog_report.json
```

## Fleet Dashboard

Build the fleet dashboard to summarize manifest adoption, due/idle status, drift findings, and duplicate reusable candidates across repos:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\build_dashboard.ps1 -RepoListPath .\repo-standards\exchange\registered_repos.example.txt -RepoKitRoot F:\dev\00-repo-kit
```

The dashboard writes:

- `archive/local-reports/exchange_dashboard_report.json`
- `archive/local-reports/exchange_dashboard_report.md`

Duplicate candidates are grouped by content hash and category across at least two repos.
This intentionally favors deterministic duplicate detection over fuzzy matching.

## Full Intake Wave

Use the intake wave runner to scan local repos in one pass and generate a consolidated report for reusable-candidate review:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\run_full_intake_wave.ps1 -DevRoot F:\dev -RepoKitRoot F:\dev\00-repo-kit
```

The intake wave remains proposal-first and non-mutating. It runs catalog/import/export/drift/due checks for each repo and writes:

- `archive/local-reports/reuse_intake_wave_<timestamp>.json`
- `archive/local-reports/reuse_intake_wave_<timestamp>.md`
- `archive/local-reports/reuse_intake_wave_latest.json`
- `archive/local-reports/reuse_intake_wave_latest.md`

Use `-RepoListPath` when you want a curated repo subset instead of scanning all Git repos under `-DevRoot`.
Catalog/export generation skips zero-byte files, `.gitkeep`, and `docs/wavekit/_archive/**` by default to reduce placeholder noise in duplicate/proposal reports.
For focused lanes, pass `-LatestAliasPrefix` so lane reports do not overwrite fleet-level `reuse_intake_wave_latest.*`.

Example (game/Unreal lane):

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\run_full_intake_wave.ps1 -RepoListPath .\repo-standards\exchange\registered_repos.game_unreal.txt -RepoKitRoot F:\dev\00-repo-kit -LatestAliasPrefix reuse_intake_game_unreal
```

## Proposal-First Flow

1. Run due check.

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\check_due.ps1 -RepoRoot . -RepoKitRoot F:\dev\00-repo-kit
```

2. Catalog local repeatable assets.

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\catalog_repo.ps1 -RepoRoot .
```

3. Propose imports from repo-kit defaults.

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\propose_imports.ps1 -RepoRoot . -RepoKitRoot F:\dev\00-repo-kit
```

4. Propose exports back to repo-kit.

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\propose_exports.ps1 -RepoRoot .
```

5. Check drift for tracked imports.

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\check_drift.ps1 -RepoRoot . -RepoKitRoot F:\dev\00-repo-kit
```

6. Review reports under `.repo-kit/` before any apply step.

7. Apply an approved proposal only after review.

Plan mode is the default and writes only a report:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\apply_approved_exchange.ps1 -RepoRoot . -RepoKitRoot F:\dev\00-repo-kit -ProposalPath .\.repo-kit\proposals\import_proposal.json -ProposalType import
```

Execute mode requires an explicit approval token:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\exchange\apply_approved_exchange.ps1 -RepoRoot . -RepoKitRoot F:\dev\00-repo-kit -ProposalPath .\.repo-kit\proposals\import_proposal.json -ProposalType import -Execute -ApprovalToken APPROVED
```

If a target already exists, execution blocks unless `-AllowOverwrite` is supplied.
The command appends applied items to `.repo-kit/exchange-ledger.jsonl` or the manifest-defined ledger path.

## Drift Status

- `current`: local copy matches recorded source hash.
- `missing`: tracked local target is absent.
- `stale`: repo-kit source hash differs from recorded source hash.
- `local_override`: local target differs and the manifest documents why.
- `untracked`: local reusable asset is not tracked in imports or exports.
- `rejected`: reviewed and intentionally not adopted or exported.

## Export Criteria

Promote a local solution to `00-repo-kit` only when all are true:

- It solves a repeatable problem likely to recur in more than one repo.
- It has a deterministic command, checklist, schema, or verification signal.
- It is not private, secret, or domain-specific content.
- It has clear ownership and stable target paths.
- The source repo records evidence for why the pattern is reusable.

## Reports and Ledgers

The default downstream files are:

- `.repo-kit/catalog.json`
- `docs/repo-kit/CATALOG.md`
- `.repo-kit/proposals/import_proposal.json`
- `.repo-kit/proposals/import_proposal.md`
- `.repo-kit/proposals/export_proposal.json`
- `.repo-kit/proposals/export_proposal.md`
- `.repo-kit/exchange-ledger.jsonl`
- `archive/local-reports/exchange_watchdog_report.json` when a report path is supplied
- `archive/local-reports/exchange_dashboard_report.json`
- `archive/local-reports/exchange_dashboard_report.md`

Reports are local review artifacts unless a repo explicitly tracks them.
The manifest is the durable state that prevents repeated duplicate decisions.

## Rollback

Preferred rollback is Git-based:

1. Run apply commands in a dedicated branch.
2. Review `git diff` and the generated apply report before committing.
3. If the apply is wrong before commit, restore the touched files from Git.
4. If the apply was committed, revert the commit instead of rewriting history.

For imports, the report lists every target path and before/after hash.
For exports, the report lists every repo-kit target path and ledger entry.
When `-AllowOverwrite` is used, review the apply report before committing because existing targets may have been overwritten.

## Maintenance Integration

Weekly maintenance should run the due check without applying changes.
Monthly maintenance should review import/export proposals and drift findings.
Scheduled prompting may be added after the manual proposal flow is stable.
