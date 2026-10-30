#!/usr/bin/env python3
"""Validate the SwarmForge Agent Skill package with the Python standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = (
    "docs/ARCHITECTURE.md",
    "docs/ADAPTER_CONTRACT.md",
    "docs/EXECUTION_MODES.md",
    "docs/INSTALLATION.md",
    "docs/ORCHESTRATION_PATTERNS.md",
    "docs/PLATFORM_COMPATIBILITY.md",
    "docs/SCALING_TO_500.md",
    "docs/SECURITY_MODEL.md",
    "docs/SOURCES.md",
    "docs/WORKFLOWS.md",
)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FIELD = re.compile(r"^([a-z][a-z0-9_-]*):\s*(.*?)\s*$")
SHA = re.compile(r"^[0-9a-fA-F]{40}$")


def frontmatter() -> list[str]:
    errors: list[str] = []
    try:
        text = SKILL.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"SKILL.md: cannot read ({exc})"]

    if not text.startswith("---\n"):
        return ["SKILL.md: frontmatter must begin on line 1"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return ["SKILL.md: frontmatter closing delimiter is missing"]

    values: dict[str, str] = {}
    for number, line in enumerate(text[4:end].splitlines(), 2):
        if not line or line.startswith((" ", "\t", "#")):
            continue
        match = FIELD.fullmatch(line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("\"'")
        else:
            errors.append(f"SKILL.md:{number}: unsupported frontmatter line")

    name = values.get("name", "")
    description = values.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("SKILL.md: name must be a lowercase hyphenated slug (max 64 chars)")
    if not description or len(description) > 1024:
        errors.append("SKILL.md: description is required and must be <= 1024 chars")
    compatibility = values.get("compatibility", "")
    if len(compatibility) > 500:
        errors.append("SKILL.md: compatibility must be <= 500 chars")
    return errors


def local_links() -> list[str]:
    errors: list[str] = []
    candidates = [ROOT / "README.md", SKILL]
    candidates.extend((ROOT / "docs").rglob("*.md"))
    for path in candidates:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path.relative_to(ROOT)}: cannot read ({exc})")
            continue
        for raw in LINK.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or urlparse(target).scheme or target.startswith("/"):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")
    return errors


def main() -> int:
    errors = frontmatter()
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"required document missing: {rel}")
    errors.extend(local_links())

    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors), file=sys.stderr)
        return 1
    print("SwarmForge Skill package checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
