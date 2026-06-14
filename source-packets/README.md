# Source Packets

Source packets document source provenance, rights, cultural context, excerpt boundaries, and reviewer status before any source text is copied into lessons.

## Rules

- Keep all sources reference-only until a packet is approved.
- Use `source-packets/TEMPLATE.md` for human-readable packets.
- Future machine-readable packets should follow `schemas/source_packet.schema.json`.
- Do not include full source text, copied translations, scans, or course assets in this repo unless rights and excerpt boundaries are explicitly approved.
- Western packet records that are approved for original lessons may support original outlines, drills, and assessments, but not copied excerpts.
- Comparative packet candidates must stay `needs_cultural_review` until source rights and cultural framing are reviewed.

## Layout

- `source-packets/western/`: Western spine packets used for first lesson outlines.
- `source-packets/comparative/`: comparative candidates for future reviewed extensions.
- `source-packets/index.json`: machine-readable packet readiness index for downstream ingestion.

## First Packet Priority

1. Euclid, `Elements`.
2. Aristotle, `Categories`.
3. Aristotle, `Prior Analytics`.
4. Aristotle, `Rhetoric`.
5. Plato, selected dialogue.
6. Cicero or Quintilian rhetorical work.

Comparative packets come after the Western packet workflow is proven.

## Downstream Index

Use `source-packets/index.json` when a consumer needs packet status without parsing Markdown. The index records source IDs, packet paths, review status, rights status, source references, whether original lesson use is allowed, whether excerpt use is allowed, and whether cultural review is still required.

Current policy:

- Western packets may support original lesson outlines.
- No packet currently allows copied excerpts.
- Comparative candidates remain blocked on cultural review.
