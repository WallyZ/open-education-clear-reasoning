"""Generate the source packet readiness index from packet Markdown."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "open-education-clear-reasoning/source-packet-index/v1"
REPO_ID = "open-education-clear-reasoning"
DEFAULT_LAST_REVIEWED = "2026-06-14"
INDEX_PATH = Path("source-packets/index.json")
LESSON_OUTLINE_PATH = Path("study-plans/western-spine-lessons/LESSON_OUTLINES.md")

PREFERRED_PACKET_ORDER = [
    "source-packets/western/euclid-elements-casey.md",
    "source-packets/western/aristotle-categories-edghill.md",
    "source-packets/western/aristotle-prior-analytics-owen.md",
    "source-packets/western/aristotle-rhetoric-cope-sandys.md",
    "source-packets/western/plato-apology-jowett.md",
    "source-packets/comparative/indian-nyaya-sutras-candidate.md",
    "source-packets/comparative/buddhist-logic-candidate.md",
    "source-packets/comparative/islamic-ghazali-deliverance-candidate.md",
    "source-packets/comparative/jewish-pirke-avot-candidate.md",
    "source-packets/comparative/chinese-confucian-analects-candidate.md",
    "source-packets/comparative/african-oral-deliberation-candidate.md",
]
PREFERRED_ORDER_INDEX = {path: index for index, path in enumerate(PREFERRED_PACKET_ORDER)}


def _relative_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _parse_packet_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^-\s+([^:]+):\s*(.*)$")
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(raw_line)
        if not match:
            continue
        key = match.group(1).strip()
        value = match.group(2).strip()
        fields[key] = value
    return fields


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug


def _lesson_refs_by_packet(repo_root: Path) -> dict[str, list[str]]:
    path = repo_root / LESSON_OUTLINE_PATH
    if not path.is_file():
        return {}

    refs: dict[str, list[str]] = {}
    current_slug = ""
    heading_pattern = re.compile(r"^##\s+Lesson\s+\d+:\s+(.+?)\s*$")
    packet_pattern = re.compile(r"^- Source packet:\s+`([^`]+)`")
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = heading_pattern.match(line)
        if heading:
            current_slug = _slugify(heading.group(1))
            continue
        packet = packet_pattern.match(line)
        if packet and current_slug:
            packet_path = packet.group(1)
            refs.setdefault(packet_path, []).append(f"{LESSON_OUTLINE_PATH.as_posix()}#{current_slug}")
    return refs


def _rights_status(fields: dict[str, str], category: str, review_status: str) -> str:
    claim = fields.get("License or public-domain claim", "")
    evidence = fields.get("Evidence for license/public-domain status", "")
    rights_text = f"{claim} {evidence}".lower()
    needs_cultural_review = "needs_cultural_review" in review_status

    if needs_cultural_review and "project gutenberg" in rights_text and "public-domain" in rights_text:
        return "public_domain_usa_source_page_checked_but_cultural_review_needed"
    if category == "comparative":
        return "candidate_needs_review"
    if "project gutenberg" in rights_text and "public domain" in rights_text:
        return "public_domain_usa_source_page_checked"
    if "public-domain candidate" in rights_text or "published in" in rights_text:
        return "publication_date_public_domain_candidate_checked"
    return "candidate_needs_review"


def _packet_author(fields: dict[str, str]) -> str:
    author = fields.get("Author", "")
    editor_or_translator = fields.get("Editor or translator", "")
    translator_lower = editor_or_translator.lower()
    if not editor_or_translator or editor_or_translator == "To verify" or translator_lower in author.lower():
        return author
    if "translation candidate by" in author.lower():
        return author
    if " translation as represented" in translator_lower:
        translator = re.split(r"\s+translation\s+", editor_or_translator, maxsplit=1)[0].strip()
        return f"{author}; translated by {translator}"
    if "translator" in translator_lower or "translation" in translator_lower:
        return f"{author}; {editor_or_translator}"
    return f"{author}; translated by {editor_or_translator}"


def _packet_entry(path: Path, repo_root: Path, lesson_refs: dict[str, list[str]]) -> dict[str, Any]:
    fields = _parse_packet_fields(path)
    relative_path = _relative_path(path, repo_root)
    category = path.parent.name
    review_status = fields.get("Reviewer status", "")
    original_lesson_allowed = category == "western" and review_status == "approved_for_original_lesson"
    needs_cultural_review = category == "comparative" or "needs_cultural_review" in review_status

    return {
        "id": path.stem,
        "source_id": fields.get("Source ID", ""),
        "path": relative_path,
        "category": category,
        "work": fields.get("Work", ""),
        "author": _packet_author(fields),
        "review_status": review_status,
        "rights_status": _rights_status(fields, category, review_status),
        "source_reference": fields.get("Source URL or library reference", ""),
        "original_lesson_allowed": original_lesson_allowed,
        "excerpt_use_allowed": False,
        "needs_cultural_review": needs_cultural_review,
        "lesson_refs": lesson_refs.get(relative_path, []) if original_lesson_allowed else [],
    }


def _last_reviewed(repo_root: Path) -> str:
    path = repo_root / INDEX_PATH
    if not path.is_file():
        return DEFAULT_LAST_REVIEWED
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return DEFAULT_LAST_REVIEWED
    value = data.get("last_reviewed")
    return value if isinstance(value, str) and value else DEFAULT_LAST_REVIEWED


def build_index(repo_root: Path) -> dict[str, Any]:
    root = repo_root.resolve()
    lesson_refs = _lesson_refs_by_packet(root)
    packet_paths = list((root / "source-packets" / "western").glob("*.md"))
    packet_paths.extend((root / "source-packets" / "comparative").glob("*.md"))
    packet_paths.sort(
        key=lambda path: (
            PREFERRED_ORDER_INDEX.get(_relative_path(path, root), len(PREFERRED_ORDER_INDEX)),
            _relative_path(path, root),
        )
    )

    packets = [_packet_entry(path, root, lesson_refs) for path in packet_paths]
    summary = {
        "western_packets": sum(1 for packet in packets if packet["category"] == "western"),
        "comparative_candidate_packets": sum(1 for packet in packets if packet["category"] == "comparative"),
        "original_lesson_allowed": sum(1 for packet in packets if packet["original_lesson_allowed"] is True),
        "excerpt_use_allowed": sum(1 for packet in packets if packet["excerpt_use_allowed"] is True),
        "needs_cultural_review": sum(1 for packet in packets if packet["needs_cultural_review"] is True),
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "repo_id": REPO_ID,
        "last_reviewed": _last_reviewed(root),
        "policy": {
            "source_text_copied": False,
            "excerpt_use_requires_packet_approval": True,
            "western_packets_support_original_lessons": True,
            "comparative_packets_require_cultural_review": True,
        },
        "summary": summary,
        "packets": packets,
    }


def format_index(index: dict[str, Any]) -> str:
    return json.dumps(index, indent=2, ensure_ascii=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--write", action="store_true", help="Write source-packets/index.json.")
    parser.add_argument("--check", action="store_true", help="Fail if source-packets/index.json is not generated output.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    generated = format_index(build_index(repo_root))
    index_path = repo_root / INDEX_PATH

    if args.write:
        index_path.write_text(generated, encoding="utf-8")
        print(f"Wrote {INDEX_PATH.as_posix()}")
        return 0

    if args.check:
        if not index_path.is_file():
            print(f"ERROR: missing {INDEX_PATH.as_posix()}")
            return 1
        current = index_path.read_text(encoding="utf-8")
        if current != generated:
            print(
                "ERROR: source-packets/index.json drifted; run "
                "python scripts/lifecycle/generate_source_packet_index.py --repo-root . --write"
            )
            return 1
        print("source-packets/index.json is current.")
        return 0

    print(generated, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
