# TODO_AUDIT.md

Canonical TODO formatting and audit enforcement for this repo is implemented by `scripts/todo_audit.py` and `scripts/lifecycle/check_todo_format.py`.

## Scope

- Primary TODO files: `docs/todo/*.md` (excluding `docs/todo/_archive/**` by default).
- Linting is non-destructive.
- Repair is deterministic and creates a backup before writing.

## Canonical TODO contract

### Checkbox line shape

- Canonical checkbox syntax:
  - `- [ ] ...`
  - `- [x] ...`
- Canonical marker is `-` (not `*`).
- Canonical checked state is lowercase `x`.
- Phase designation must be inline on TODO items using `[PH1]`, `[PH2]`, or `[PH3]` (no heading-scoped phases).

### Tag namespaces

- Supported namespaces: `ms:*` and `yta:*`.
- Use one namespace consistently on a given line.
- Do not mix `ms:*` and `yta:*` tags on the same checkbox item.

### Evidence and IDs

- Completed items (`- [x]`) must have audit tags:
  - evidence tag (`*:evidence ...`) or
  - id tag (`*:id ...`) at minimum.
- Evidence keys should use canonical names and order:
  - `id`, `path`, `symbols`, `strings`, `fields`, `keys`

## Commands

### Lint one TODO file

```powershell
python scripts/todo_audit.py --todo docs/todo/03_scripts_and_repo_standards.md --lint --lint-min-severity info --lint-fail-on error
```

### Preview canonical repair (no file writes)

```powershell
python scripts/todo_audit.py --todo docs/todo/03_scripts_and_repo_standards.md --repair --dry-run
```

### Apply canonical repair

```powershell
python scripts/todo_audit.py --todo docs/todo/03_scripts_and_repo_standards.md --repair
```

Notes:
- Apply mode writes a backup next to the TODO file (`.bak*`).
- Use `--repair-namespace auto|ms|yta` to control generated tag namespace when missing.

### Enforce across repo TODO files

```powershell
python scripts/lifecycle/check_todo_format.py --repo-root . --todo-root docs/todo --min-severity info --fail-on error
```

This check is also wired into:
- `scripts/lint/run_all.ps1`
- `.github/workflows/reusable-consistency.yml`

## Repair behavior (deterministic)

Repair normalization does the following:

- Normalizes checkbox marker/spacing/state to canonical form.
- Consolidates supported TODO tags into one canonical comment form.
- Preserves non-TODO HTML comments on the line.
- Keeps evidence keys in canonical order.
- Adds stable IDs for completed items when missing.
- Optional phase-only mode (`--repair-scope phase-tags`) maps markdown phase headings to inline checkbox tags (`[PH1]`, `[PH2]`, `[PH3]`) for top-level TODO items.
- Markdown phase headings like `### Phase 2 (...)` are lint errors (`PHASE_HEADING_NON_CANONICAL`).

## Example

Before:

```md
* [ X ] Harden todo_audit [PH1] <!-- yta:evidence symbols=lint_todo path=scripts/todo_audit/lint.py id=todo.audit.harden -->
```

After:

```md
- [x] Harden todo_audit [PH1] <!-- yta:evidence id=todo.audit.harden path=scripts/todo_audit/lint.py symbols=lint_todo -->
```

## Idempotence check

Run repair twice; second pass should be a no-op:

```powershell
python scripts/todo_audit.py --todo docs/todo/03_scripts_and_repo_standards.md --repair
python scripts/todo_audit.py --todo docs/todo/03_scripts_and_repo_standards.md --repair --dry-run
```

Expected second output: `No changes required; file is already canonical.`

## Metadata and ready queue (required for open PH2/PH3)

TODO lines should include metadata tags for queueing; open PH2/PH3 items are required to include them:

- `<!-- ms:meta priority=p1 owner=@team depends-on=<id1,id2> blocked-by=<id3> target-repo=<repo> stale-days=14 automation-level=auto human-checkpoint=none rollout-scope=fleet validation-profile=cloud safe-autofix=safe -->`

Lint validates metadata keys and values (`META_*`) and fails when open PH2/PH3 items are missing required metadata fields.

Generate a cross-file ready queue:

```powershell
python scripts/lifecycle/check_todo_ready_queue.py --repo-root . --todo-root docs/todo --min-severity info --fail-on error --report -
```

See `docs/TODO_PROCESS.md` for the full TODO workflow.


