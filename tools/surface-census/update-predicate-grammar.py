#!/usr/bin/env python3
"""Regenerate the predicate list and its partition counts from the census.

Exit 0 means success, 1 means check-mode drift, and 2 means an operational error.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
START = "A shape the two kinds above cannot express emits a **predicate selector**,"
END = "A predicate selector is a selector like any other everywhere else:"


def number_words(value: int) -> str:
    units = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    teens = (
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    )
    tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    if value < 10:
        return units[value]
    if value < 20:
        return teens[value - 10]
    if value < 100:
        return tens[value // 10] + ("-" + units[value % 10] if value % 10 else "")
    raise ValueError("partition count exceeds 99; extend number_words before regenerating")


def regenerate(document: str) -> str:
    spec = importlib.util.spec_from_file_location(
        "predicate_census", REPO / "tools/surface-census/openapi-surface-census.py"
    )
    if spec is None or spec.loader is None:
        raise ValueError("cannot load the census constants; restore tools/surface-census/openapi-surface-census.py")
    census = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = census
    spec.loader.exec_module(census)
    if not frozenset(census.DOCUMENT_COMPARING_PREDICATES) <= census.PREDICATES.keys():
        undeclared = sorted(frozenset(census.DOCUMENT_COMPARING_PREDICATES) - census.PREDICATES.keys())
        raise ValueError(
            f"document-comparing partition names undeclared predicates {undeclared}; reconcile DOCUMENT_COMPARING_PREDICATES with PREDICATES"
        )
    prefix, separator, rest = document.partition(START)
    body, ending, suffix = rest.partition(END)
    if not separator or not ending:
        raise ValueError("predicate grammar boundaries are missing; restore the grammar section")
    before, split, after = body.partition("\n- ")
    _listing, partition, prose = after.partition("\n**")
    if not split or not partition:
        raise ValueError("predicate list or partition is missing; restore the grammar section")
    before, count = re.subn(r"closed list of\s+\d+", f"closed list of\n{len(census.PREDICATES)}", before, count=1)
    if count != 1:
        raise ValueError("predicate total is missing; restore the grammar section")
    entries = "\n".join(
        textwrap.fill(f"- `{name}` — {description}", width=88, subsequent_indent="  ")
        for name, description in census.PREDICATES.items()
    )
    local = len(census.PREDICATES) - len(census.DOCUMENT_COMPARING_PREDICATES)
    prose, count = re.subn(
        r"^[A-Z][a-z-]+ of the \d+ are node-local\*\*",
        f"{number_words(local).capitalize()} of the {len(census.PREDICATES)} are node-local**",
        prose,
        count=1,
    )
    if count != 1:
        raise ValueError("node-local count is missing; restore the grammar section")
    prose, count = re.subn(
        r"The other\s+[a-z-]+ — .*? — read the document beyond the",
        "The other\n"
        + number_words(len(census.DOCUMENT_COMPARING_PREDICATES))
        + " — "
        + ", ".join(f"`{name}`" for name in census.DOCUMENT_COMPARING_PREDICATES)
        + " — read the document beyond the",
        prose,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise ValueError("document-comparing list is missing; restore the grammar section")
    return prefix + START + before + "\n" + entries + "\n\n**" + prose + END + suffix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document", type=Path, default=REPO / "docs/openapi-surface-coverage.md")
    parser.add_argument("--check", action="store_true", help="fail on drift without writing")
    args = parser.parse_args()
    try:
        original = args.document.read_text(encoding="utf-8")
        updated = regenerate(original)
        if original != updated:
            if args.check:
                print("predicate grammar is stale; regenerate with just predicate-grammar", file=sys.stderr)
                return 1
            with args.document.open("w", encoding="utf-8", newline="\n") as output:
                output.write(updated)
    except (OSError, ValueError) as error:
        print(
            f"predicate-grammar: {error}; restore the input file and ensure it is writable UTF-8 text", file=sys.stderr
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
