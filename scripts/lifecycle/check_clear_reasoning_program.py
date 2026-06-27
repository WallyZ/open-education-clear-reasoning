"""Validate the Clear Reasoning curriculum scaffold."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "open-education-clear-reasoning/program/v1"
FRAMEWORK_SCHEMA_VERSION = "open-education-clear-reasoning/civilization-framework/v1"
REPO_ID = "open-education-clear-reasoning"
FORBIDDEN_TOKENS = [
    "excerpt_text",
    "full_text",
    "translation_text",
    "generated_media_path",
    "F:\\\\",
]
REQUIRED_DOC_TOKENS = {
    "README.md": ["open-education-clear-reasoning", "Euclid", "Aristotle"],
    "docs/PROGRAM_DESIGN.md": ["World-Class Bar", "Mastery Model", "Course Architecture"],
    "docs/SOURCE_CANON.md": ["Use Boundary", "Integration Stages", "Global And Comparative Extensions"],
    "docs/CANON_INTEGRATION_MAP.md": ["Integration Lanes", "Reference-Only Modern Sources", "Integration Rule"],
    "docs/CIVILIZATION_COVERAGE.md": ["Western civilization is the main spine", "Civilization Lanes", "Cultural Comparison Questions"],
    "docs/CULTURE_DIFFERENCE_FRAMEWORK.md": ["Primary Rule", "Required Lens Fields", "Misread Controls"],
    "docs/SOURCE_PACKET_SYSTEM.md": ["Packet Lifecycle", "Required Packet Fields", "Approval Rule"],
    "docs/CURRICULUM_MATRIX.md": ["Foundation Matrix", "Advanced Track Matrix", "Matrix Completion Standard"],
    "docs/REVIEWER_STANDARD.md": ["Review Categories", "Required Reviewer Checks", "Cultural Humility Standard"],
    "docs/BUILD_ORDER.md": ["Phase 1: Western Foundation Spine", "Phase 3: Comparative Lesson Extensions", "Build Rule"],
    "docs/PEDAGOGY.md": ["Daily Practice Loop", "Source-Move Method", "Performance Pressure Ladder"],
    "docs/ASSESSMENT_RUBRICS.md": ["Capstone Standard", "Definition discipline", "Mastery Evidence Map"],
    "docs/WORKFLOW.md": ["Courseware Integration", "Source Rules", "CANON_INTEGRATION_MAP"],
    "study-plans/clear-reasoning-foundations/COURSE.md": ["Clear Reasoning Foundations", "Module Map", "Completion Evidence"],
    "study-plans/western-spine-lessons/LESSON_OUTLINES.md": ["Packet Gate", "Euclidean Proof Craft", "No copied source text: yes"],
    "exercises/reasoning-drills.md": ["Term Lock", "Steelman Ladder", "Combative Opponent Reset", "Source-Move Extraction"],
    "source-packets/README.md": ["Western packet records", "Comparative packet candidates", "Downstream Index"],
    "source-packets/TEMPLATE.md": ["Source Packet Template", "Is any source text copied into this repo? no", "Reviewer status"],
}

REQUIRED_FRAMEWORKS = {
    "civilization_coverage",
    "culture_difference_framework",
    "source_packet_system",
    "curriculum_matrix",
    "reviewer_standard",
    "build_order",
}

REQUIRED_COVERAGE_LANES = {
    "western-greek-roman",
    "western-scholastic",
    "western-early-modern-scientific",
    "western-civic-constitutional",
    "indian-nyaya-buddhist",
    "islamic-reasoning",
    "jewish-legal-philosophical",
    "chinese-classical",
    "african-oral-deliberative",
}

REQUIRED_WESTERN_PACKETS = {
    "euclid-elements-casey.md",
    "aristotle-categories-edghill.md",
    "aristotle-prior-analytics-owen.md",
    "aristotle-rhetoric-cope-sandys.md",
    "plato-apology-jowett.md",
}

REQUIRED_COMPARATIVE_PACKETS = {
    "indian-nyaya-sutras-candidate.md",
    "buddhist-logic-candidate.md",
    "islamic-ghazali-deliverance-candidate.md",
    "jewish-pirke-avot-candidate.md",
    "chinese-confucian-analects-candidate.md",
    "african-oral-deliberation-candidate.md",
}

REQUIRED_AI_KNOWLEDGE_RECORDS = {
    "clear-reasoning-program",
    "cr-101-course",
    "objective-index",
    "assessment-bank",
    "misconception-map",
    "reasoning-drills",
    "debate-persuasion-practice-lab",
    "change-facilitation-research-lab",
    "source-canon-boundary",
    "source-packet-index",
    "offline-ai-workflow",
}


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return data


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            raw = line.strip()
            if not raw:
                continue
            data = json.loads(raw)
            if not isinstance(data, dict):
                raise ValueError(f"Expected JSON object in {path}:{line_number}")
            records.append(data)
    return records


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def _is_relative_public_path(value: str) -> bool:
    return bool(value) and ":" not in value and not value.startswith(("/", "\\"))


def _validate_docs(root: Path, errors: list[str]) -> None:
    for relative_path, tokens in REQUIRED_DOC_TOKENS.items():
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing required doc: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{relative_path} missing token: {token}")


def _validate_program(root: Path, errors: list[str]) -> None:
    schema_path = root / "schemas" / "clear_reasoning_program.schema.json"
    program_path = root / "curriculum" / "clear_reasoning_program.json"
    _require(schema_path.is_file(), "missing schema file", errors)
    _require(program_path.is_file(), "missing curriculum file", errors)
    if not schema_path.is_file() or not program_path.is_file():
        return

    schema = _load_json(schema_path)
    program = _load_json(program_path)

    _require(schema.get("title") == "Clear Reasoning Program", "schema title drifted", errors)
    _require(program.get("schema_version") == SCHEMA_VERSION, "unexpected program schema_version", errors)
    _require(program.get("repo_id") == REPO_ID, "unexpected repo_id", errors)

    privacy = program.get("privacy_boundary") or {}
    for key in ("contains_learner_private_data", "contains_copyrighted_source_text", "contains_generated_media"):
        _require(privacy.get(key) is False, f"privacy_boundary.{key} must be false", errors)

    blob = json.dumps(program, sort_keys=True)
    for token in FORBIDDEN_TOKENS:
        _require(token not in blob, f"curriculum includes forbidden token: {token}", errors)

    sources = program.get("source_canon") or []
    _require(isinstance(sources, list) and len(sources) >= 24, "source_canon must include at least 24 sources", errors)
    source_ids = {str(source.get("id")) for source in sources if isinstance(source, dict)}
    for required in (
        "euclid-elements",
        "aristotle-categories",
        "aristotle-prior-analytics",
        "aristotle-rhetoric",
        "porphyry-isagoge",
        "aquinas-disputation",
        "bacon-novum-organum",
        "mill-system-of-logic",
        "peirce-inquiry",
        "confucius-analects",
        "federalist-papers",
    ):
        _require(required in source_ids, f"missing required source: {required}", errors)
    for source in sources:
        if not isinstance(source, dict):
            errors.append("source_canon entries must be objects")
            continue
        source_id = source.get("id")
        _require(bool(source.get("use_boundary")), f"source {source.get('id')} missing use_boundary", errors)
        _require(bool(source.get("tradition")), f"source {source_id} missing tradition", errors)
        _require(source.get("integration_stage") == "reference_only", f"source {source_id} must stay reference_only until packet is verified", errors)
        _require(source.get("source_packet_status") == "needed", f"source {source_id} must require a source packet before excerpts", errors)
        _require(bool(source.get("recommended_use")), f"source {source_id} missing recommended_use", errors)

    mastery_bands = program.get("mastery_bands") or []
    _require(mastery_bands == ["recognize", "name", "analyze", "produce", "perform"], "mastery bands must match expected ladder", errors)

    advanced_tracks = program.get("advanced_tracks") or []
    _require(len(advanced_tracks) >= 6, "advanced_tracks must include at least 6 tracks", errors)
    track_ids: set[str] = set()
    for track in advanced_tracks:
        if not isinstance(track, dict):
            errors.append("advanced_tracks entries must be objects")
            continue
        track_id = str(track.get("id") or "")
        _require(bool(track_id), "advanced track missing id", errors)
        _require(track_id not in track_ids, f"duplicate advanced track id: {track_id}", errors)
        track_ids.add(track_id)
        refs = track.get("source_refs") or []
        _require(bool(refs), f"advanced track {track_id} missing source_refs", errors)
        for ref in refs:
            _require(str(ref) in source_ids, f"advanced track {track_id} references unknown source {ref}", errors)
        _require(len(track.get("outcomes") or []) >= 2, f"advanced track {track_id} needs at least 2 outcomes", errors)
        _require(len(track.get("labs") or []) >= 2, f"advanced track {track_id} needs at least 2 labs", errors)
        _require(bool(track.get("capstone_artifact")), f"advanced track {track_id} missing capstone_artifact", errors)
    for required_track in ("grammar-meaning", "proof-demonstration", "dialectic-disputation", "rhetoric-public-speech", "inquiry-evidence", "civic-moral-judgment", "adversarial-reasoning"):
        _require(required_track in track_ids, f"missing required advanced track: {required_track}", errors)

    practice_labs = program.get("practice_labs") or []
    _require(len(practice_labs) >= 6, "practice_labs must include at least 6 labs", errors)
    lab_ids: set[str] = set()
    for lab in practice_labs:
        if not isinstance(lab, dict):
            errors.append("practice_labs entries must be objects")
            continue
        lab_id = str(lab.get("id") or "")
        _require(bool(lab_id), "practice lab missing id", errors)
        _require(lab_id not in lab_ids, f"duplicate practice lab id: {lab_id}", errors)
        lab_ids.add(lab_id)
        _require(bool(lab.get("skill_family")), f"practice lab {lab_id} missing skill_family", errors)
        _require(bool(lab.get("evidence")), f"practice lab {lab_id} missing evidence", errors)
        refs = lab.get("source_refs") or []
        for ref in refs:
            _require(str(ref) in source_ids, f"practice lab {lab_id} references unknown source {ref}", errors)
    for required_lab in ("source-move-extraction", "objection-box", "induction-ladder", "eristic-shield", "teach-back"):
        _require(required_lab in lab_ids, f"missing required practice lab: {required_lab}", errors)

    course = program.get("course") or {}
    modules = course.get("modules") or []
    _require(course.get("id") == "clear-reasoning-foundations", "course id drifted", errors)
    _require(len(modules) >= 12, "course must include at least 12 modules", errors)
    module_ids: set[str] = set()
    for module in modules:
        if not isinstance(module, dict):
            errors.append("module entries must be objects")
            continue
        module_id = str(module.get("id") or "")
        _require(bool(module_id), "module missing id", errors)
        _require(module_id not in module_ids, f"duplicate module id: {module_id}", errors)
        module_ids.add(module_id)
        refs = module.get("source_refs") or []
        _require(bool(refs), f"module {module_id} missing source_refs", errors)
        for ref in refs:
            _require(str(ref) in source_ids, f"module {module_id} references unknown source {ref}", errors)
        _require(len(module.get("skills") or []) >= 2, f"module {module_id} needs at least 2 skills", errors)
        _require(len(module.get("practice") or []) >= 2, f"module {module_id} needs at least 2 practice items", errors)
        _require(bool(module.get("assessment")), f"module {module_id} missing assessment", errors)
        _require(bool(module.get("performance_pressure")), f"module {module_id} missing performance pressure", errors)

    capstone = program.get("capstone") or {}
    artifacts = capstone.get("required_artifacts") or []
    _require(len(artifacts) >= 8, "capstone must require at least 8 artifacts", errors)
    _require("self-audit" in json.dumps(capstone).lower(), "capstone must include self-audit", errors)


def _validate_civilization_framework(root: Path, errors: list[str]) -> None:
    schema_path = root / "schemas" / "civilization_reasoning_framework.schema.json"
    framework_path = root / "curriculum" / "civilization_reasoning_framework.json"
    packet_schema_path = root / "schemas" / "source_packet.schema.json"
    packet_readme_path = root / "source-packets" / "README.md"
    packet_template_path = root / "source-packets" / "TEMPLATE.md"

    for path, label in (
        (schema_path, "civilization framework schema"),
        (framework_path, "civilization framework"),
        (packet_schema_path, "source packet schema"),
        (packet_readme_path, "source packet readme"),
        (packet_template_path, "source packet template"),
    ):
        _require(path.is_file(), f"missing {label}", errors)
    if not schema_path.is_file() or not framework_path.is_file() or not packet_schema_path.is_file():
        return

    schema = _load_json(schema_path)
    framework = _load_json(framework_path)
    packet_schema = _load_json(packet_schema_path)

    _require(schema.get("title") == "Civilization Reasoning Framework", "civilization framework schema title drifted", errors)
    _require(packet_schema.get("title") == "Clear Reasoning Source Packet", "source packet schema title drifted", errors)
    _require(framework.get("schema_version") == FRAMEWORK_SCHEMA_VERSION, "unexpected civilization framework schema_version", errors)
    _require(framework.get("repo_id") == REPO_ID, "unexpected civilization framework repo_id", errors)
    _require(framework.get("primary_spine") == "western-civilization", "civilization framework must keep western-civilization as primary spine", errors)

    frameworks = set(str(item) for item in (framework.get("required_frameworks") or []))
    for required in REQUIRED_FRAMEWORKS:
        _require(required in frameworks, f"civilization framework missing required framework: {required}", errors)

    lanes = framework.get("coverage_lanes") or []
    _require(len(lanes) >= 8, "civilization framework must include at least 8 coverage lanes", errors)
    lane_ids: set[str] = set()
    primary_count = 0
    comparative_count = 0
    for lane in lanes:
        if not isinstance(lane, dict):
            errors.append("coverage_lanes entries must be objects")
            continue
        lane_id = str(lane.get("id") or "")
        _require(bool(lane_id), "coverage lane missing id", errors)
        _require(lane_id not in lane_ids, f"duplicate coverage lane id: {lane_id}", errors)
        lane_ids.add(lane_id)
        priority = lane.get("priority")
        if priority == "primary":
            primary_count += 1
        if priority == "comparative":
            comparative_count += 1
        for key in ("knowledge_standard", "argument_goal", "disagreement_norm", "authority_structure", "build_status"):
            _require(bool(lane.get(key)), f"coverage lane {lane_id} missing {key}", errors)
        _require(len(lane.get("transferable_moves") or []) >= 1, f"coverage lane {lane_id} missing transferable moves", errors)
        _require(len(lane.get("misread_risks") or []) >= 1, f"coverage lane {lane_id} missing misread risks", errors)
        if priority == "comparative":
            _require("review" in str(lane.get("build_status")), f"comparative lane {lane_id} must require review before lesson build", errors)

    for required_lane in REQUIRED_COVERAGE_LANES:
        _require(required_lane in lane_ids, f"missing required coverage lane: {required_lane}", errors)
    _require(primary_count >= 4, "civilization framework must include at least 4 primary Western lanes", errors)
    _require(comparative_count >= 4, "civilization framework must include at least 4 comparative lanes", errors)

    review_gates = set(str(item) for item in (framework.get("review_gates") or []))
    for required_gate in ("source_identity_checked", "rights_checked", "cultural_context_checked", "misread_risks_recorded", "transfer_boundary_recorded"):
        _require(required_gate in review_gates, f"civilization framework missing review gate: {required_gate}", errors)

    build_phase_ids = {str(item.get("id")) for item in framework.get("build_phases") or [] if isinstance(item, dict)}
    for required_phase in ("phase-1-western-foundation", "phase-2-comparative-guardrails", "phase-3-comparative-extensions"):
        _require(required_phase in build_phase_ids, f"civilization framework missing build phase: {required_phase}", errors)


def _validate_generated_source_packet_index(root: Path, errors: list[str]) -> None:
    generator_path = root / "scripts" / "lifecycle" / "generate_source_packet_index.py"
    index_path = root / "source-packets" / "index.json"
    _require(generator_path.is_file(), "missing source packet index generator", errors)
    if not generator_path.is_file() or not index_path.is_file():
        return

    spec = importlib.util.spec_from_file_location("generate_source_packet_index", generator_path)
    if spec is None or spec.loader is None:
        errors.append("could not load source packet index generator")
        return
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generated = module.format_index(module.build_index(root))
    current = index_path.read_text(encoding="utf-8")
    _require(
        current == generated,
        "source-packets/index.json drifted; run python scripts/lifecycle/generate_source_packet_index.py --repo-root . --write",
        errors,
    )


def _validate_source_packets(root: Path, errors: list[str]) -> None:
    western_dir = root / "source-packets" / "western"
    comparative_dir = root / "source-packets" / "comparative"
    index_path = root / "source-packets" / "index.json"
    index_schema_path = root / "schemas" / "source_packet_index.schema.json"
    _require(western_dir.is_dir(), "missing source-packets/western directory", errors)
    _require(comparative_dir.is_dir(), "missing source-packets/comparative directory", errors)
    _require(index_path.is_file(), "missing source packet index", errors)
    _require(index_schema_path.is_file(), "missing source packet index schema", errors)
    if not western_dir.is_dir() or not comparative_dir.is_dir():
        return

    western_files = {path.name for path in western_dir.glob("*.md")}
    comparative_files = {path.name for path in comparative_dir.glob("*.md")}
    for required in REQUIRED_WESTERN_PACKETS:
        _require(required in western_files, f"missing required western source packet: {required}", errors)
    for required in REQUIRED_COMPARATIVE_PACKETS:
        _require(required in comparative_files, f"missing required comparative source packet: {required}", errors)

    required_packet_tokens = (
        "## Identity",
        "## Location",
        "## Rights",
        "## Excerpt Boundary",
        "## Pedagogical Use",
        "## Cultural Context",
        "## Review",
        "Is any source text copied into this repo? no",
    )
    for path in list(western_dir.glob("*.md")) + list(comparative_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for token in required_packet_tokens:
            _require(token in text, f"{path.relative_to(root)} missing packet token: {token}", errors)
        _require("full source text" not in text.lower(), f"{path.relative_to(root)} appears to mention full source text", errors)

    for path in western_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        _require(
            "Reviewer status: approved_for_original_lesson" in text,
            f"{path.relative_to(root)} must be approved_for_original_lesson for first western outlines",
            errors,
        )
        _require(
            "no source excerpt is approved" in text.lower() or "no copied source text" in text.lower(),
            f"{path.relative_to(root)} must block copied excerpts",
            errors,
        )

    for path in comparative_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        _require(
            "Reviewer status: needs_cultural_review" in text,
            f"{path.relative_to(root)} must remain needs_cultural_review",
            errors,
        )
        _require(
            "Reference-only" in text or "reference-only" in text,
            f"{path.relative_to(root)} must be reference-only",
            errors,
        )

    if not index_path.is_file() or not index_schema_path.is_file():
        return
    index_schema = _load_json(index_schema_path)
    index = _load_json(index_path)
    _require(index_schema.get("title") == "Clear Reasoning Source Packet Index", "source packet index schema title drifted", errors)
    _require(index.get("schema_version") == "open-education-clear-reasoning/source-packet-index/v1", "unexpected source packet index schema_version", errors)
    _require(index.get("repo_id") == REPO_ID, "unexpected source packet index repo_id", errors)
    policy = index.get("policy") or {}
    _require(policy.get("source_text_copied") is False, "source packet index must state source_text_copied=false", errors)
    _require(policy.get("excerpt_use_requires_packet_approval") is True, "source packet index must require excerpt approval", errors)
    _require(policy.get("western_packets_support_original_lessons") is True, "source packet index must allow western original lessons", errors)
    _require(policy.get("comparative_packets_require_cultural_review") is True, "source packet index must require comparative cultural review", errors)

    packets = index.get("packets") or []
    _require(len(packets) == len(REQUIRED_WESTERN_PACKETS) + len(REQUIRED_COMPARATIVE_PACKETS), "source packet index packet count drifted", errors)
    packet_ids: set[str] = set()
    western_index_count = 0
    comparative_index_count = 0
    original_allowed_count = 0
    needs_review_count = 0
    for packet in packets:
        if not isinstance(packet, dict):
            errors.append("source packet index entries must be objects")
            continue
        packet_id = str(packet.get("id") or "")
        _require(bool(packet_id), "source packet index entry missing id", errors)
        _require(packet_id not in packet_ids, f"duplicate source packet index id: {packet_id}", errors)
        packet_ids.add(packet_id)
        relative_path = str(packet.get("path") or "")
        _require(bool(relative_path), f"source packet index entry {packet_id} missing path", errors)
        if relative_path:
            _require((root / relative_path).is_file(), f"source packet index path does not exist: {relative_path}", errors)
        _require(packet.get("excerpt_use_allowed") is False, f"source packet index packet {packet_id} must not allow excerpt use", errors)
        category = packet.get("category")
        if category == "western":
            western_index_count += 1
            original_allowed_count += 1 if packet.get("original_lesson_allowed") is True else 0
            _require(packet.get("review_status") == "approved_for_original_lesson", f"western index packet {packet_id} must be approved_for_original_lesson", errors)
            _require(packet.get("needs_cultural_review") is False, f"western index packet {packet_id} should not require cultural review", errors)
            _require(len(packet.get("lesson_refs") or []) >= 1, f"western index packet {packet_id} must include lesson_refs", errors)
        elif category == "comparative":
            comparative_index_count += 1
            needs_review_count += 1 if packet.get("needs_cultural_review") is True else 0
            _require(packet.get("review_status") == "needs_cultural_review", f"comparative index packet {packet_id} must be needs_cultural_review", errors)
            _require(packet.get("original_lesson_allowed") is False, f"comparative index packet {packet_id} must not allow original lessons yet", errors)
            _require(len(packet.get("lesson_refs") or []) == 0, f"comparative index packet {packet_id} should not include lesson_refs yet", errors)
        else:
            errors.append(f"source packet index packet {packet_id} has invalid category: {category}")

    summary = index.get("summary") or {}
    _require(summary.get("western_packets") == western_index_count, "source packet index western summary mismatch", errors)
    _require(summary.get("comparative_candidate_packets") == comparative_index_count, "source packet index comparative summary mismatch", errors)
    _require(summary.get("original_lesson_allowed") == original_allowed_count, "source packet index original lesson summary mismatch", errors)
    _require(summary.get("excerpt_use_allowed") == 0, "source packet index must have zero excerpt-use packets", errors)
    _require(summary.get("needs_cultural_review") == needs_review_count, "source packet index cultural review summary mismatch", errors)
    _validate_generated_source_packet_index(root, errors)


def _validate_lesson_outlines(root: Path, errors: list[str]) -> None:
    path = root / "study-plans" / "western-spine-lessons" / "LESSON_OUTLINES.md"
    _require(path.is_file(), "missing western spine lesson outlines", errors)
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for lesson_title in (
        "Euclidean Proof Craft",
        "Aristotelian Categories And Definitions",
        "Syllogism And Valid Inference",
        "Ethical Rhetoric And Audience",
        "Socratic Questioning Under Pressure",
    ):
        _require(lesson_title in text, f"western lesson outlines missing lesson: {lesson_title}", errors)
    _require(text.count("No copied source text: yes") >= 5, "every first western outline must state no copied source text", errors)
    for token in ("Objective:", "Drill:", "Assessment:", "Revision path:", "Transfer case:", "Mastery evidence:"):
        _require(text.count(token) >= 5, f"western lesson outlines must include {token} for each lesson", errors)


def _validate_offline_ai_knowledge_store(root: Path, errors: list[str]) -> None:
    content_manifest_path = root / "content-repo.json"
    manifest_path = root / "ai-knowledge" / "manifest.json"
    records_path = root / "ai-knowledge" / "records.jsonl"

    _require(content_manifest_path.is_file(), "missing content-repo.json", errors)
    _require(manifest_path.is_file(), "missing AI knowledge store manifest", errors)
    _require(records_path.is_file(), "missing AI knowledge store records", errors)
    if not content_manifest_path.is_file() or not manifest_path.is_file() or not records_path.is_file():
        return

    content_manifest = _load_json(content_manifest_path)
    ai_config = content_manifest.get("aiKnowledgeStore") or {}
    _require(ai_config.get("manifestPath") == "ai-knowledge/manifest.json", "content manifest must expose AI knowledge manifest", errors)
    _require(ai_config.get("recordsPath") == "ai-knowledge/records.jsonl", "content manifest must expose AI knowledge records", errors)
    _require(ai_config.get("status") == "seed-ready", "AI knowledge store status must be seed-ready", errors)
    for profile_id in ("ollama-local", "lm-studio-local"):
        _require(profile_id in (ai_config.get("preferredRuntimeProfiles") or []), f"content manifest missing runtime profile: {profile_id}", errors)

    manifest = _load_json(manifest_path)
    _require(manifest.get("schemaVersion") == "open-education/offline-ai-knowledge-store/v1", "AI knowledge manifest schemaVersion drifted", errors)
    _require(manifest.get("storeId") == "clear-reasoning-offline-ai-knowledge", "AI knowledge manifest storeId drifted", errors)
    _require(manifest.get("ownerRepoId") == "clear-reasoning", "AI knowledge manifest ownerRepoId drifted", errors)
    _require(manifest.get("role") == "content-knowledge-seed", "AI knowledge manifest role must be content-knowledge-seed", errors)
    _require(manifest.get("sourceRecordsPath") == "ai-knowledge/records.jsonl", "AI knowledge manifest records path drifted", errors)

    profile_ids = {str(profile.get("id")) for profile in manifest.get("runtimeProfiles") or [] if isinstance(profile, dict)}
    for profile_id in ("ollama-local", "lm-studio-local"):
        _require(profile_id in profile_ids, f"AI knowledge manifest missing runtime profile: {profile_id}", errors)
    for profile in manifest.get("runtimeProfiles") or []:
        if not isinstance(profile, dict):
            errors.append("AI knowledge runtime profile entries must be objects")
            continue
        _require(profile.get("networkScope") == "localhost-only", f"AI runtime profile {profile.get('id')} must be localhost-only", errors)
        _require(str(profile.get("apiBase") or "").startswith("http://127.0.0.1:"), f"AI runtime profile {profile.get('id')} must use localhost apiBase", errors)

    privacy = manifest.get("privacyBoundary") or {}
    for key in ("containsLearnerPrivateData", "containsCredentials", "containsPrivateNotes", "containsEmbeddings", "containsCopiedSourceText"):
        _require(privacy.get(key) is False, f"AI knowledge privacyBoundary.{key} must be false", errors)
    _require(privacy.get("allowsLocalPrivateOverlays") is True, "AI knowledge store must allow local private overlays", errors)

    writeback = manifest.get("writebackPolicy") or {}
    for key in ("seedRecordsAreReadOnly", "privateOverlaysStayLocal", "publicPromotionRequiresReview", "durableLearnerStateRequiresCheckedCode"):
        _require(writeback.get(key) is True, f"AI knowledge writebackPolicy.{key} must be true", errors)

    records = _load_jsonl(records_path)
    _require(len(records) >= len(REQUIRED_AI_KNOWLEDGE_RECORDS), "AI knowledge store must include required seed records", errors)
    seen_ids: set[str] = set()
    for record in records:
        record_id = str(record.get("recordId") or "")
        _require(bool(record_id), "AI knowledge record missing recordId", errors)
        _require(record_id not in seen_ids, f"duplicate AI knowledge record id: {record_id}", errors)
        seen_ids.add(record_id)
        for key in ("kind", "title", "sourceRepo", "sourcePath", "summary"):
            _require(bool(record.get(key)), f"AI knowledge record {record_id} missing {key}", errors)
        source_path = str(record.get("sourcePath") or "")
        _require(_is_relative_public_path(source_path), f"AI knowledge record {record_id} sourcePath must be relative", errors)
        if source_path:
            _require((root / source_path).is_file(), f"AI knowledge record {record_id} sourcePath does not exist: {source_path}", errors)
        _require(record.get("sourceRepo") == "clear-reasoning", f"AI knowledge record {record_id} sourceRepo must be clear-reasoning", errors)
        _require(record.get("privacyClass") == "public-course-seed", f"AI knowledge record {record_id} privacyClass must be public-course-seed", errors)
        _require(record.get("writePolicy") == "read-only-seed", f"AI knowledge record {record_id} writePolicy must be read-only-seed", errors)
        _require(record.get("citationRequired") is True, f"AI knowledge record {record_id} must require citation", errors)
        _require(len(record.get("retrievalTerms") or []) >= 3, f"AI knowledge record {record_id} needs at least 3 retrievalTerms", errors)
        serialized = json.dumps(record, sort_keys=True)
        for token in ("F:\\", "api_key", "bearer ", "secret", "token=", "learnerId", "privateNote", "excerpt_text", "full_text"):
            _require(token.lower() not in serialized.lower(), f"AI knowledge record {record_id} includes forbidden token: {token}", errors)

    for required_record in REQUIRED_AI_KNOWLEDGE_RECORDS:
        _require(required_record in seen_ids, f"AI knowledge store missing required record: {required_record}", errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    errors: list[str] = []
    _validate_docs(root, errors)
    _validate_program(root, errors)
    _validate_civilization_framework(root, errors)
    _validate_source_packets(root, errors)
    _validate_lesson_outlines(root, errors)
    _validate_offline_ai_knowledge_store(root, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Clear Reasoning curriculum checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
