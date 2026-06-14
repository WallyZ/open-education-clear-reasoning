# Source Packet System

## Purpose

Source packets are the gate between reference-only curriculum design and actual source-based lesson construction. They protect the repo from unlicensed text, weak provenance, and culturally careless use.

## Current State

All source works are reference-only unless a packet proves otherwise. A source reference may guide original exercises and summaries, but no excerpt, translation text, scan, lecture asset, or problem set may be copied into this repo until the packet is approved.

## Packet Lifecycle

1. `planned`: source is named and pedagogically useful.
2. `candidate`: edition or translation has been found.
3. `rights_checked`: public-domain or license evidence has been recorded.
4. `culture_checked`: reviewer notes document cultural context and misread risks.
5. `excerpt_approved`: excerpt boundary and attribution are approved.
6. `lesson_ready`: original lesson, drill, assessment, and transfer caveat are ready.

## Required Packet Fields

A packet must include:

- source ID matching `curriculum/clear_reasoning_program.json` when the source is already part of the active program, or a clearly marked candidate ID for sources not yet promoted into the active canon
- author
- work title
- civilization and tradition
- edition or translation
- editor or translator when applicable
- publication date
- source URL or library reference
- license or public-domain evidence
- jurisdiction notes when needed
- excerpt boundary, even when no excerpt is copied yet
- pedagogical reason
- cultural caveat
- misread risks
- attribution text
- reviewer status
- last reviewed date

## Approval Rule

A packet is not usable for source excerpts until these are all true:

- license or public-domain evidence is explicit
- excerpt boundary is narrow and justified
- cultural caveat is present
- reviewer status is not `needs_review`
- attribution text is ready

## File Layout

- `source-packets/README.md`: operator guide.
- `source-packets/TEMPLATE.md`: packet template for human-authored packets.
- `schemas/source_packet.schema.json`: JSON contract for future machine-readable packets.

## First Packet Priority

The first source packets should be Western spine packets:

1. Euclid, `Elements`.
2. Aristotle, `Categories`.
3. Aristotle, `Prior Analytics`.
4. Aristotle, `Rhetoric`.
5. Plato, selected dialogue.
6. Cicero or Quintilian rhetorical work.

Comparative packets should follow only after the Western packet workflow is proven.

## Current Packet Policy

The first Western packets may be used for original lesson outlines when `Reviewer status` is `approved_for_original_lesson`. That status does not approve copied excerpts.

Comparative candidates must remain `needs_cultural_review` until a source and culture reviewer approves the source identity, rights boundary, cultural caveat, and transfer limits.
