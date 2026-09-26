# TODO 04 - Teaching Debate

## Goal

Build Teaching Debate as a reusable Clear Reasoning course while keeping
leadership applications, private channel adaptations, controversial subject
dossiers, learner state, and publishing operations with their existing owners.

## Tasks

- [x] [P1] Establish the Teaching Debate ownership and migration boundary. <!-- yta:evidence paths="study-plans/teaching-debate/COURSE.md,curriculum/teaching_debate_program.json" id=clear-reasoning-teaching-debate-ownership -->
  - Clear Reasoning owns transferable reasoning and debate instruction.
  - `open-education-leadership` retains leadership-specific negotiation,
    coalition, institutional, sales, fundraising, and management applications.
  - Subject repositories own Contested Questions evidence dossiers.
  - Private channel packages own episode framing and adaptation decisions.
  - `youtube-automation` owns production workflow and approval enforcement.

- [x] [P1] Add a prerequisite-complete TD001-TD002 pilot contract and course guide. <!-- yta:evidence paths="curriculum/teaching_debate_program.json,schemas/teaching_debate_program.schema.json,study-plans/teaching-debate/COURSE.md,scripts/lifecycle/check_clear_reasoning_program.py" id=clear-reasoning-teaching-debate-pilot -->
  - Preserve the supplied stable lesson IDs without importing channel IDs,
    scripts, clip decisions, or unresolved factual claims.
  - Map overlap to existing Clear Reasoning modules and practice labs.
  - Keep source and rights readiness explicitly unresolved until reconciled.

- [ ] [P1] Reconcile TD003-TD072 against existing modules, drills, rubrics, sources, and the Leadership boundary before importing them. <!-- yta:evidence paths="curriculum/,study-plans/teaching-debate/,exercises/,assessments/" id=clear-reasoning-teaching-debate-full-reconciliation -->
  - Classify each proposal as `reuse`, `extend`, `new`, `channel-only`, or
    `needs-review`.
  - Import only prerequisite-complete sequences.
  - Keep TD049 and other real-person or footage-dependent work blocked until
    source, context, quotation, and rights review is complete.

- [ ] [P2] Add suite-facing course metadata only after the pilot contract is accepted by the existing content-ingestion path. <!-- yta:evidence paths="content-repo.json,study-plans/courses/,objectives/,assessments/" id=clear-reasoning-teaching-debate-suite-adapter -->
  - Do not add manifest fields a current consumer silently ignores.
  - Do not duplicate the existing Clear Reasoning source registration.

- [ ] [P2] Qualify channel adaptation through the owning YouTube TODOs without copying channel content into this repo. <!-- yta:evidence paths="study-plans/teaching-debate/COURSE.md" id=clear-reasoning-teaching-debate-channel-adaptation -->
  - The Clearer Argument may adapt the reusable course.
  - Contested Questions remains a separate channel and is not a curriculum
    authority.

## Acceptance Notes

- Completion of the pilot proves schema, ownership, prerequisite, and
  public/private-boundary behavior only.
- It does not prove all 72 lessons are complete, source-cleared, instructionally
  effective, ready for publication, or suitable for every audience.
