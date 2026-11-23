#!/usr/bin/env python3
"""Offline checks for links, placeholders, and accidental secret material."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
PLACEHOLDER_FILES = {
    ROOT / "examples" / "compose" / "secure-service.yml",
    ROOT / "examples" / "workflows" / "container-scan-caller.yml",
}


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def check_links(path: Path, text: str) -> list[str]:
    problems: list[str] = []
    for target in MARKDOWN_LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            problems.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            problems.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
    return problems


def main() -> int:
    problems: list[str] = []
    scanned = 0
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts):
        if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml"}:
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8")
        if PRIVATE_KEY.search(text):
            problems.append(f"{path.relative_to(ROOT)}: private-key material detected")
        if path.suffix.lower() == ".md":
            problems.extend(check_links(path, text))

    for path in PLACEHOLDER_FILES:
        if not path.exists() or "REPLACE_WITH_" not in path.read_text(encoding="utf-8"):
            problems.append(f"{path.relative_to(ROOT)}: explicit placeholders are required")

    if problems:
        print("\n".join(f"FAIL {problem}" for problem in problems))
        return 1
    print(f"checked {scanned} documentation and example files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
