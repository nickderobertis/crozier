"""Move one region row to `handwritten` in a copy of the region files.

A node that admits a hand-written fixture moves its row out of `gap` exactly
this way (docs/openapi-surface/handwritten/AGENTS.md): the category reads
`handwritten`, the evidence cell names the fixture and the failed search, and
the last three cells are empty. The tools that derive a key set from the region
files are each tested over such a copy, so a flip is shown to move none of them.
`restore_gap_row` is the inverse, for suites about a frozen `gap` row once the
tree no longer holds one.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
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


def restore_gap_row(region: Path, key: str) -> str:
    """Turn `key`'s `handwritten` row in the region-file copy `region` back into a frozen `gap` row.

    It is the row a search-incomplete key carried before a fixture moved it: its
    census selector, read from the tracked key set beside the copy, and the
    inline outcome `search-incomplete`. Suites that exercise how a frozen gap row
    is derived use it once the tree no longer holds one. Returns the new line.
    """
    tracked = dict(
        line.split("\t")[:2]
        for line in (region.parent / "witness-search-keys.tsv").read_text(encoding="utf-8").splitlines()[1:]
    )
    lines = region.read_text(encoding="utf-8").splitlines(keepends=True)
    restored = None
    for index, line in enumerate(lines):
        cells = [c.strip() for c in line.replace("\\|", "\0").strip().strip("|").split("|")]
        if line.startswith("| ") and len(cells) == 8 and cells[0].strip("`") == key:
            assert cells[3] == "handwritten", f"{key} is `{cells[3]}`, not `handwritten`"
            cells = [c.replace("\0", "\\|") for c in cells[:3]] + [
                "gap",
                f"census `{tracked[key]}`: **0** declaration sites across every registered source; "
                "search outcome `search-incomplete`",
                "`src/ir.rs`: 1 place",
                "The types module would differ.",
                "`FIXTURE` — registration remains pending.",
            ]
            restored = "| " + " | ".join(cells) + " |"
            lines[index] = restored + "\n"
    assert restored is not None, f"{key} has no row in {region.name}"
    region.write_text("".join(lines), encoding="utf-8")
    return restored
