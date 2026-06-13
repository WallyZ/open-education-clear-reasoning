# Open Education Clear Reasoning

`open-education-clear-reasoning` is a subject-owned open education repo for training clear thought, disciplined reasoning, honest disagreement, and persuasive communication.

The program is built from public-domain great-works traditions and original course design, especially:

- Euclid's `Elements` for definitions, axioms, proof discipline, construction, and demonstration.
- Aristotle's logical works, `Rhetoric`, and ethical/practical reasoning for categories, propositions, demonstration, dialectic, fallacy detection, persuasion, and judgment.
- Plato, Cicero, Quintilian, Boethius, classical rhetoric, the trivium, and later logic/rhetoric traditions for dialogue, grammar, dialectic, and public speech.

## Goal

Train learners until clear reasoning becomes an operating habit:

- define terms before arguing
- distinguish claims, evidence, warrants, assumptions, and conclusions
- identify valid, invalid, strong, weak, fair, and manipulative arguments
- build proof-like explanations from first principles where possible
- speak with clarity under pressure
- disagree without losing discipline or charity
- hold their own with serious thinkers, aggressive disputants, and confused audiences

## Repo Role

This repo owns the subject curriculum. It is designed to be consumed by `open-education-suite` and future courseware tooling.

It contains:

- source canon and use boundaries
- course architecture
- module sequence
- practice drills
- assessment rubrics
- machine-readable curriculum metadata
- deterministic validation scripts

It does not contain learner private data, generated media, copyrighted translations, or platform-specific UI code.

## Start Here

1. Read `docs/PROGRAM_DESIGN.md`.
2. Review `study-plans/clear-reasoning-foundations/COURSE.md`.
3. Inspect `curriculum/clear_reasoning_program.json`.
4. Run verification:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\codex-verify.ps1 -RepoRoot . -ContextProfile cloud -Mode changed -IncludeUntracked
```

## Design Standard

The program should be harder, clearer, and more useful than a typical critical-thinking course. Every unit must connect great works to visible habits:

- reading precisely
- questioning fairly
- proving carefully
- speaking persuasively
- detecting confusion and manipulation
- practicing in live disagreement
- transferring the method to everyday life
