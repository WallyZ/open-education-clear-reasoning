# Repo Health Self-Assessment

This self-assessment maps OpenSSF Best Practices and community health criteria to repo-kit local evidence, hosted GitHub setup, and owner decisions.

The goal is report-first governance: maintainers can review what is already satisfied locally, what requires hosted setup, and what should remain an explicit owner decision before downstream repos adopt the same baseline.

## Review Scope

- Scope: repo-kit source checkout and downstream standards assets.
- Last reviewed: 2026-06-04.
- Owner: `repo-kit/governance`.
- Verification entrypoint: `pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked`.
- External checks: not run by default. OpenSSF badge submission, live Scorecard results, and hosted GitHub community profile settings require explicit owner or maintainer action.

## Status Legend

| Status | Meaning |
| --- | --- |
| Local evidence present | Repo-owned files, scripts, or policies already satisfy the criterion locally. |
| Hosted confirmation required | The repo carries repeatable guidance, but the live GitHub setting must be confirmed in GitHub. |
| Owner decision required | The repo should not guess the policy because it changes public governance or legal posture. |
| Downstream report-first | Downstream adoption should be reported or planned before mutating repo-local decisions. |

## Criteria Mapping

| Area | OpenSSF or community health criterion | Current status | Local evidence or owner decision |
| --- | --- | --- | --- |
| Project identity | Clear project purpose and user-facing documentation | Local evidence present | `README.md`, `docs/README.md`, `docs/QUICKSTART.md` |
| License | Repository license is explicit | Local evidence present | Owner approved MIT in `LICENSE`; third-party surfaces are tracked in `THIRD_PARTY_NOTICES.md`. |
| Notice inventory | Third-party notices and provenance are visible | Local evidence present | `THIRD_PARTY_NOTICES.md`, `docs/SECURITY_SUPPLY_CHAIN_PACK.md` |
| Contribution guidance | Contributors know the expected process | Downstream report-first | `docs/templates/CONTRIBUTING_template.md` is available; downstream repos decide whether to publish root `CONTRIBUTING.md`. |
| Code of conduct | Public community conduct is documented when needed | Owner decision required | No default root code-of-conduct file is forced. Add one only when the owner decides the repo has public community-collaboration needs. |
| Security policy | Vulnerability reporting and supply-chain expectations are documented | Local evidence present | `docs/SECURITY_SUPPLY_CHAIN_PACK.md`, `docs/templates/SECURITY_template.md`, `scripts/security/check_supply_chain_pack.ps1` |
| Review ownership | Sensitive changes have named owners | Local evidence present | `.github/CODEOWNERS` assigns repo, docs, scripts, and GitHub workflow ownership. |
| PR review hygiene | Change review expectations are documented | Local evidence present | `.github/PULL_REQUEST_TEMPLATE.md`, `docs/BRANCH_PROTECTION_POLICY.md`, `docs/WORKFLOW_POLICY.md` |
| Branch protection | Required checks and merge rules are known | Hosted confirmation required | `docs/BRANCH_PROTECTION_POLICY.md` documents solo-owner direct-main and team/PR opt-in. Hosted branch rules must be confirmed in GitHub for team repos. |
| CI and verification | Automated checks are repeatable | Local evidence present | `.github/workflows/ci.yml`, `.github/workflows/reusable-consistency.yml`, `scripts/codex-verify.ps1` |
| OpenSSF Scorecard | Scorecard capability exists and is tracked | Hosted confirmation required | `.github/workflows/scorecard.yml` and `repo-standards/security/security_scanner_profiles.json`; live GitHub results require hosted workflow execution. |
| Dependency updates | Dependency update policy and review cadence are visible | Local evidence present | `docs/DEPENDENCY_UPDATE_POLICY.md`, `docs/DEPENDENCY_DASHBOARD.md`, `docs/templates/renovate.json` |
| Secrets handling | Secrets are not committed and restoration is documented | Local evidence present | `docs/SECRETS_BACKUP_POLICY.md`, `docs/SECRETS_RESTORE_CHECKLIST.md`, `scripts/secrets/check_env_keys.ps1` |
| SBOM readiness | SBOM expectation is documented even when generation is opt-in | Local evidence present | `docs/SECURITY_SUPPLY_CHAIN_PACK.md`, optional scanner profiles in `repo-standards/security/security_scanner_profiles.json` |
| Release governance | Versioning, changelog, release, and maintenance cadence are documented | Local evidence present | `VERSION`, `docs/VERSIONING.md`, `docs/CHANGELOG_POLICY.md`, `docs/RELEASE_CHECKLIST.md`, `docs/MAINTENANCE_SCHEDULE.md` |
| Maintainer continuity | Durable decisions and handoff context are recorded | Local evidence present | `docs/DECISIONS.md`, `memory-bank/context-pack.md`, `memory-bank/repoKitCatalog.md` |

## Hosted Checks Not Claimed By Local Evidence

These items are intentionally not marked as complete by local files alone:

- OpenSSF Best Practices badge submission and public badge status.
- Live OpenSSF Scorecard results from GitHub Actions or scorecard.dev.
- GitHub Community Standards profile completion as shown in the hosted GitHub UI.
- Branch protection, required status checks, CODEOWNERS enforcement, and admin bypass settings in the hosted repository.
- GitHub private vulnerability reporting or security advisory settings.

When any hosted setting becomes required, record the owner decision in `docs/DECISIONS.md`, update the relevant policy doc, and attach the hosted evidence to the release or maintenance report.

## Hosted Owner Review Checklist

Use this checklist when the owner wants to confirm hosted community-health posture. These checks are manual because they depend on GitHub UI state or external OpenSSF services.

| Check | Where to verify | Expected result | Evidence to keep |
| --- | --- | --- | --- |
| GitHub community profile | GitHub repo `Insights -> Community Standards` | Required profile items are either complete or explicitly not applicable for a solo-owner tooling repo. | Screenshot or release note entry listing incomplete items and owner decisions. |
| Branch protection | GitHub repo `Settings -> Branches` | Solo-owner direct-main mode is intentional, or team/PR branch protection matches `docs/BRANCH_PROTECTION_POLICY.md`. | Rule screenshot or decision note. |
| CODEOWNERS enforcement | GitHub branch protection rule | Code owner review is enabled only when team/PR mode is enabled. | Rule screenshot or workflow-policy decision. |
| Security policy and advisories | GitHub repo `Security` tab | Vulnerability reporting posture matches `docs/SECURITY_SUPPLY_CHAIN_PACK.md` and any root `SECURITY.md`. | Security settings screenshot or owner decision. |
| OpenSSF Scorecard workflow | GitHub Actions and code scanning | `.github/workflows/scorecard.yml` runs successfully when hosted checks are enabled. | Workflow run URL or archived report. |
| OpenSSF Best Practices badge | OpenSSF Best Practices site | Badge submission exists only if the owner chooses public badge tracking. | Badge URL or explicit owner-deferred decision. |

## Downstream Adoption Guidance

Downstream repos should adopt this as a report-first artifact:

1. Run the repo maturity scorecard and upgrade planner before copying governance files.
2. Treat missing `docs/REPO_HEALTH_SELF_ASSESSMENT.md` as a reportable governance gap.
3. Preserve downstream `LICENSE`, `THIRD_PARTY_NOTICES.md`, `CODEOWNERS`, security policy, and contribution files unless the owner explicitly approves replacement.
4. Map every downstream checklist row to one of:
   - local file evidence,
   - repo-owned script or policy evidence,
   - hosted GitHub setup note,
   - explicit owner decision,
   - follow-up TODO with evidence requirements.
5. Do not submit live OpenSSF or hosted GitHub checks from automation unless the downstream repo opts in.

## Maintenance

Review this self-assessment when any of these change:

- repo-kit governance docs or required artifacts,
- GitHub workflow names, permissions, or hosted branch policy,
- security scanner profile expectations,
- public contribution or community-health posture,
- downstream installer or upgrade-planner behavior.
