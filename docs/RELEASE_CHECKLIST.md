# RELEASE_CHECKLIST

Release checklist for `00-repo-kit` maintainers.

## 1) Scope and readiness

- [ ] Confirm release scope and target version bump (`patch`/`minor`/`major`).
- [ ] Verify TODO evidence is up to date for completed release-wave items.
- [ ] Review dependency dashboard decisions (`docs/DEPENDENCY_DASHBOARD.md`) and capture any release-relevant updates.

## 2) Version + docs updates

- [ ] Update root `VERSION`.
- [ ] Update `docs/VERSIONING.md` if policy changed.
- [ ] Update release changelog entries per `docs/CHANGELOG_POLICY.md` (`Unreleased` -> `v<VERSION>` section).
- [ ] Ensure release-facing commit messages follow `docs/COMMIT_CONVENTIONS.md`.
- [ ] Update impacted docs/changelogs:
  - [ ] `docs/changelogs/*` for changed packs
  - [ ] any changed policy docs referenced by rollout
- [ ] Update `repo-standards/pack_versions.json` for pack-version rollouts.

## 3) Validation gates

Run from repo root:

```powershell
python scripts/inventory/generate_inventory.py --repo-root . --write
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/lint/run_all.ps1 -RepoRoot . -ContextProfile cloud
```

- [ ] Inventory regenerated and clean.
- [ ] Canonical verifier passes and the log is under `.codex-cache/logs/`.
- [ ] Full lint/consistency suite passes.
- [ ] `scripts/status/next_work.ps1` reports the expected next TODO, dirty state, last verify log, and latest QA Live status.
- [ ] QA Live gate reviewed before user-only checks:
  - [ ] Required repo-owned QA Live specs/workflows were dry-run or capability-checked first.
  - [ ] Every automatable UI/game/Unreal/browser/VM/installer/runtime check has a QA Live contract/run-spec or was added to `qa-live-test-system` before release.
  - [ ] Any required `qa-live-test-system` capability change was committed and pushed to that repo's `main`.
  - [ ] Live QA was run only when the release scope requires it and host prerequisites are available.
  - [ ] Latest QA Live report/status is recorded or explicitly marked not required.
- [ ] Artifact review completed:
  - [ ] Generated docs, inventory, schemas, reports, packages, screenshots, logs, or build outputs are intentionally tracked or ignored.
  - [ ] Archive/local report schemas are updated for new report shapes.
  - [ ] No secrets, local caches, or `.codex-cache/` artifacts are staged.
- [ ] User-only verification exceptions documented where applicable:
  - [ ] Each exception states why automation or QA Live cannot verify it.
  - [ ] Each exception includes the exact user action, location, expected result, and confirmation artifact when possible.
  - [ ] Release notes include only the checks that absolutely require a human, such as creative judgment, private account state, physical-device behavior, or credentials the agent cannot access.

## 4) Commit and tag

- [ ] Commit release changes with clear message.
- [ ] Confirm workflow mode:
  - [ ] Default solo-owner mode: commit on `main` and push to `origin/main`.
  - [ ] Team/PR mode only when `.repo-kit/workflow_policy.local.json` or hosted branch protection requires it.
- [ ] Create annotated tag matching `VERSION` (example: `v0.1.0`).
- [ ] Push commit and tag.

Example:

```powershell
git tag -a v<VERSION> -m "release: v<VERSION>"
git push origin main
git push origin v<VERSION>
```

## 5) Post-release rollout

- [ ] Publish downstream rollout notes (installer/sync expectations).
- [ ] If pack versions changed, run pinned sync commands with `-ExpectedPackVersion`.
- [ ] Record any follow-up work in `docs/todo/*.md`.
