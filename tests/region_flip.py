# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this helper sits in tests/ beside the suites that import it, which run under `just check`.
"""Move one region row to `handwritten` in a copy of the region files.

A node that admits a hand-written fixture moves its row out of `gap` exactly
this way (docs/openapi-surface/handwritten/AGENTS.md): the category reads
`handwritten`, the evidence cell names the fixture and the failed search, and
the last three cells are empty. The tools that derive a key set from the region
files are each tested over such a copy, so a flip is shown to move none of them.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REGIONS = REPO / "docs" / "openapi-surface"


def flipped_regions(target: Path, key: str, record: str = "schemas.md#witness-search-exhaustive") -> Path:
    """Copy the region files and the tracked key set into `target`, `key`'s row flipped."""
    target.mkdir(parents=True, exist_ok=True)
    flipped = 0
    for path in sorted(REGIONS.glob("*.md")):
        lines = []
        for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
            cells = [c.strip() for c in line.replace("\\|", "\0").strip().strip("|").split("|")]
            if line.startswith("| ") and len(cells) == 8 and cells[0].strip("`") == key:
                cells = [c.replace("\0", "\\|") for c in cells[:3]] + [
                    "handwritten",
                    f"handwritten: {key}-fixture; search: exhausted ([record]({record}))",
                    "", "", "",
                ]
                line = "| " + " | ".join(cells) + " |\n"
                flipped += 1
            lines.append(line)
        (target / path.name).write_text("".join(lines), encoding="utf-8")
    (target / "witness-search-keys.tsv").write_bytes((REGIONS / "witness-search-keys.tsv").read_bytes())
    assert flipped == 1, f"{key} is not exactly one region row"
    return target
