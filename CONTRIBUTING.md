# Contributing

Thanks for contributing to this repository.

## Workflow

1. Open or reference a TODO/wave item before coding.
2. Keep changes scoped to the active task.
3. Run local checks before opening a PR:
   - `pwsh -File .\scripts\lint\run_all.ps1 -RepoRoot .`
4. Update docs/TODO evidence when you complete tracked tasks.

## Pull request expectations

- Small, reviewable diffs.
- Verification commands and outcomes included in PR description.
- No unrelated refactors in the same PR.

## Coding standards

- Follow repository language/style guides.
- Keep comments concise and factual.
- Do not remove required evidence/anchor strings without updating dependent checks.

## Security and secrets

- Never commit secrets, tokens, or private keys.
- Report security concerns via `SECURITY.md` process.
