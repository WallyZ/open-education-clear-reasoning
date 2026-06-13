# LOGGING

Repo-local logging standard aligned with `00-repo-kit` global guides.

## Severity model

Use unified levels:

- `TRACE`
- `DEBUG`
- `INFO`
- `WARN`
- `ERROR`
- `FATAL`

No custom levels outside this set.

## Runtime controls

- `LOG_LEVEL`
- optional per-component overrides (`LOG_LEVEL_<COMPONENT>`)
- optional CLI flag override (`--log-level`)
- optional profile switch (`normal|investigation|deep_trace`)

Precedence:

1. CLI flags
2. Environment variables
3. Config defaults
4. Built-in defaults

## Event schema (minimum)

- `ts`
- `level`
- `component`
- `event`
- `msg`
- `run_id`
- `trace_id`
- `source`

Recommended:

- `duration_ms`
- `attempt`
- `exit_code`
- `tool`

## Sinks

- console (`INFO`)
- file (`DEBUG` recommended)
- stable repo-root `logs/` output path
- rotation and retention policy defined (size and/or age)

## Redaction

- redact secret keys/values before writing logs
- never emit raw env dumps or credential-bearing payloads

## Unreal/toolchain integration (if applicable)

- map Unreal verbosity to unified levels
- correlate Unreal + external tooling with `run_id` and `trace_id`
- avoid `LogTemp` for stable production diagnostics
- use explicit `UE_LOG` categories owned by subsystem
- include Unreal Editor + UAT + UBT in one correlated run context
- maintain `docs/logging/unreal_ingestion_contract.json` from repo-kit contract template

## Shared adapter references

- `scripts/logging/repokit_logging_adapter.py`
- `scripts/logging/RepoKit.LoggingAdapter.psm1`
- `scripts/logging/unreal_log_ingest_adapter.py`

## Verification checklist

- [ ] level mapping test
- [ ] redaction test
- [ ] correlation test across emitters
- [ ] default-noise readability check
- [ ] runtime profile toggle test
