#!/usr/bin/env python3
"""Render the complete case index while retaining hand-written descriptions."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "cases" / "README.md"
DOMAINS = (
    "linalg",
    "numthy",
    "commalg",
    "groups",
    "topology",
    "homalg",
    "combin",
    "geometry",
)
HEADING = "## Current cases"
ENTRY = re.compile(r"(?ms)^- \[`([^`]+)`\].*?(?=^- \[`|^### `|\Z)")


def main() -> int:
    current = INDEX.read_text(encoding="utf-8")
    preamble, _, old_index = current.partition(HEADING)
    old_entries = {
        match.group(1): match.group(0).rstrip() for match in ENTRY.finditer(old_index)
    }

    cases: dict[str, list[dict[str, object]]] = {domain: [] for domain in DOMAINS}
    for path in sorted((ROOT / "cases").glob("*/*/case.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        cases[path.parent.parent.name].append(record)

    lines = [preamble.rstrip(), "", HEADING, ""]
    for domain in DOMAINS:
        lines.extend((f"### `{domain}`", ""))
        for record in sorted(cases[domain], key=lambda item: str(item["id"])):
            case_id = str(record["id"])
            old_entry = old_entries.get(case_id)
            if old_entry is not None:
                lines.extend((old_entry, ""))
                continue
            slug = case_id.split(".", 1)[1]
            title = str(record["title"]).rstrip(".")
            description = title[0].lower() + title[1:] if title else title
            lines.extend(
                (
                    f"- [`{case_id}`]({domain}/{slug}/)",
                    f"  {description}.",
                    "",
                )
            )
    INDEX.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"indexed {sum(map(len, cases.values()))} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
