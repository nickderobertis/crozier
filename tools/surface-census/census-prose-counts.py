#!/usr/bin/env python3
"""Hold every census count the region pages restate to the witnesses listed beside it.

A census evidence cell in `docs/openapi-surface/*.md` that says how many sources
declare a feature, and then enumerates them, carries the measurement twice:

    **6** golden-bearing sources, 6 sites — `daniweb-connect` (1), …
    **7** declaration sites in **2** registered sources — `viskit-studio` (1), `waylay-queries` (6)
    183 declarations in 183 fixtures — `groundhog-day.com` (2), …

The enumerated list, one `` `source` (sites) `` entry per declaring source, is
the measurement as the census printed it; the counts before it are derived from
that list. Issue #477: they were written by hand and drifted from it (a count of
five beside six names). This tool reads only the forms that claim a *complete*
list — a cell naming "the five largest" of a larger set is not one — and:

``check``  prints every cell whose counts disagree with its list, as
           ``PATH:LINE: key: says …, lists …``, and exits 1 when there is one.
``write``  renders those counts from the lists, leaving every other byte as it is.

Exit status: 0 clean (or written), 1 on drift, 2 on a usage error.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

REPO = Path(__file__).resolve().parents[2]
PAGES = Path("docs") / "openapi-surface"

_NUMBER = r"(\*\*)?(\d+|one)(?:\*\*)?"
_ENTRY = r"`[^`]+` \((\d+)\)"
_LIST = r"((?:`[^`]+` \(\d+\))(?:, `[^`]+` \(\d+\))*)"


class Counts(NamedTuple):
    """A cell's two counts: the entries its list names, and the sites they sum to.

    `entries` counts list entries, not distinct names: the census prints a
    population that joins two sorted runs (a fixture's packaged and flat
    goldens, say) with each run's entries, and counts every one of them.
    """

    entries: int
    sites: int


def _plural(count: int, noun: str) -> str:
    return noun if count == 1 else f"{noun}s"


def _number(count: int, bold: str | None) -> str:
    return f"**{count}**" if bold else str(count)


class Form(NamedTuple):
    """One phrasing of a count followed by its complete list."""

    name: str
    pattern: re.Pattern[str]
    # The count groups as (entries, sites), each a (bold, number) pair of group indices.
    entries: tuple[int, int]
    sites: tuple[int, int]
    render: Callable[[re.Match[str], Counts], str]


def _sites_in_sources(match: re.Match[str], counts: Counts) -> str:
    golden = "golden-bearing " if match.group("golden") else ""
    return (
        f"{_number(counts.sites, match.group(1))} declaration {_plural(counts.sites, 'site')} in "
        f"{_number(counts.entries, match.group(3))} {golden}registered {_plural(counts.entries, 'source')}"
        f"{match.group('separator')} "
    )


FORMS = (
    Form(
        "sites-in-sources",
        re.compile(
            rf"{_NUMBER} declaration sites? in {_NUMBER} (?P<golden>golden-bearing )?registered sources?"
            rf"(?P<separator> —|,) (?={_LIST})"
        ),
        (3, 4),
        (1, 2),
        _sites_in_sources,
    ),
    Form(
        "sites-across-sources",
        re.compile(rf"{_NUMBER} declaration sites? across {_NUMBER} sources? — (?={_LIST})"),
        (3, 4),
        (1, 2),
        lambda match, counts: (
            f"{_number(counts.sites, match.group(1))} declaration {_plural(counts.sites, 'site')} across "
            f"{_number(counts.entries, match.group(3))} {_plural(counts.entries, 'source')} — "
        ),
    ),
    Form(
        "golden-bearing-sources",
        re.compile(rf"{_NUMBER} golden-bearing sources?, {_NUMBER} sites? — (?={_LIST})"),
        (1, 2),
        (3, 4),
        lambda match, counts: (
            f"{_number(counts.entries, match.group(1))} golden-bearing {_plural(counts.entries, 'source')}, "
            f"{_number(counts.sites, match.group(3))} {_plural(counts.sites, 'site')} — "
        ),
    ),
    Form(
        "declarations-in-fixtures",
        re.compile(rf"{_NUMBER} declarations? in {_NUMBER} fixtures? — (?={_LIST})"),
        (3, 4),
        (1, 2),
        lambda match, counts: (
            f"{_number(counts.sites, match.group(1))} {_plural(counts.sites, 'declaration')} in "
            f"{_number(counts.entries, match.group(3))} {_plural(counts.entries, 'fixture')} — "
        ),
    ),
)


def _value(match: re.Match[str], group: int) -> int:
    text = match.group(group)
    return 1 if text == "one" else int(text)


def listed(text: str, after: int) -> Counts:
    """The counts the complete list starting at `after` gives."""
    entries = re.match(_LIST, text[after:])
    assert entries is not None, "a form only matches before a list"
    sites = [int(count) for count in re.findall(_ENTRY, entries.group(1))]
    return Counts(len(sites), sum(sites))


class Drift(NamedTuple):
    line: int
    key: str
    form: str
    said: Counts
    listed: Counts

    def __str__(self) -> str:
        return (
            f"{self.key}: says {self.said.entries} listed entr(ies) and {self.said.sites} site(s) "
            f"({self.form}), lists {self.listed.entries} entr(ies) and {self.listed.sites} site(s)"
        )


def _row_key(line: str) -> str:
    cells = line.split("|")
    return cells[1].strip().strip("`") if len(cells) > 2 and line.startswith("|") else "(prose)"


def restate(text: str) -> tuple[str, list[Drift]]:
    """`text` with every count rendered from its list, and each cell that disagreed."""
    drifts: list[Drift] = []
    lines = text.splitlines(keepends=True)
    for number, line in enumerate(lines):
        for form in FORMS:

            def rendered(match: re.Match[str], form: Form = form, number: int = number) -> str:
                said = Counts(_value(match, form.entries[1]), _value(match, form.sites[1]))
                counts = listed(match.string, match.end())
                if said == counts:
                    return match.group(0)
                drifts.append(Drift(number + 1, _row_key(match.string), form.name, said, counts))
                return form.render(match, counts)

            line = form.pattern.sub(rendered, line)
        lines[number] = line
    return "".join(lines), drifts


def pages(root: Path) -> list[Path]:
    return sorted((root / PAGES).glob("*.md"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("command", choices=("check", "write"))
    args = parser.parse_args(argv)
    if not (args.repo_root / PAGES).is_dir():
        print(
            f"census-prose-counts: {args.repo_root / PAGES} is no directory, so there is nothing to hold; "
            "pass the repository root as --repo-root",
            file=sys.stderr,
        )
        return 2
    drifted = 0
    for path in pages(args.repo_root):
        text = path.read_text(encoding="utf-8")
        restated, drifts = restate(text)
        drifted += len(drifts)
        if args.command == "write":
            if restated != text:
                path.write_text(restated, encoding="utf-8", newline="\n")
            continue
        for drift in drifts:
            print(f"{path.relative_to(args.repo_root).as_posix()}:{drift.line}: {drift}", file=sys.stderr)
    if args.command == "check" and drifted:
        print(
            f"census-prose-counts: {drifted} count(s) disagree with the witnesses listed beside them; "
            "render them from the lists with `python3 tools/surface-census/census-prose-counts.py write`, "
            "after checking each list against the census measurement it restates",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
