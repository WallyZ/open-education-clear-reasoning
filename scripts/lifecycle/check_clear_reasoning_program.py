"""Validate the Clear Reasoning curriculum scaffold."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "open-education-clear-reasoning/program/v1"
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
    "docs/SOURCE_CANON.md": ["Use Boundary", "Euclid", "Aristotle"],
    "docs/PEDAGOGY.md": ["Daily Practice Loop", "Performance Pressure Ladder"],
    "docs/ASSESSMENT_RUBRICS.md": ["Capstone Standard", "Definition discipline"],
    "docs/WORKFLOW.md": ["Courseware Integration", "Source Rules"],
    "study-plans/clear-reasoning-foundations/COURSE.md": ["Clear Reasoning Foundations", "Module Map", "Completion Evidence"],
    "exercises/reasoning-drills.md": ["Term Lock", "Steelman Ladder", "Combative Opponent Reset"],
}


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return data


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


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
    _require(isinstance(sources, list) and len(sources) >= 8, "source_canon must include at least 8 sources", errors)
    source_ids = {str(source.get("id")) for source in sources if isinstance(source, dict)}
    for required in ("euclid-elements", "aristotle-categories", "aristotle-prior-analytics", "aristotle-rhetoric"):
        _require(required in source_ids, f"missing required source: {required}", errors)
    for source in sources:
        if not isinstance(source, dict):
            errors.append("source_canon entries must be objects")
            continue
        _require(bool(source.get("use_boundary")), f"source {source.get('id')} missing use_boundary", errors)

    mastery_bands = program.get("mastery_bands") or []
    _require(mastery_bands == ["recognize", "name", "analyze", "produce", "perform"], "mastery bands must match expected ladder", errors)

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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    errors: list[str] = []
    _validate_docs(root, errors)
    _validate_program(root, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Clear Reasoning curriculum checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
