#!/usr/bin/env python3
"""Hold every statement of the certified Fern pair to its one declaration.

`assets/scaffolding/metadata.json` declares the pair crozier is certified
against: `cliVersion` (the Fern CLI) and `generatorVersion`
(`fernapi/fern-python-sdk`). Code, tools, recipes and tests derive the pair from
that file; one that spells it out instead drifts the day the pair moves. This
check scans the tracked files that may state the pair — `src/`, `crates/`,
`tools/`, `scripts/`, `.github/`, `tests/`, `justfile`, `action.yml` — for the
forms a pair statement takes in this repository, and fails on any that names a
version other than the file's.

Committed Fern output and dated records (`tests/fixtures/`, `docs/`,
`CHANGELOG.md`) are history, not statements of the current pair, and are never
scanned; nor is a comment line, which is prose like `docs/` (often a dated
measurement: "measured at fernapi/fern-python-sdk:X"). Nor are the promoted
tiers, the release-packaging suite and the workspace aggregate: the project
running this check (`fern-goldens-git`) may not take their files as inputs
under nx.json's `boundaries`, and a file it scanned outside its inputs would
never rerun it. None states a pair. Test data that deliberately names another version
(a stand-in to prove a mismatch is caught) carries `certified-pair: stand-in`
on the line the statement starts on; nothing else is exempt.

Usage: certified_pair.py check [ROOT]
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import NamedTuple

METADATA = Path("assets") / "scaffolding" / "metadata.json"
SCANNED_DIRS = ("src/", "crates/", "tools/", "scripts/", ".github/", "tests/")
SCANNED_FILES = ("justfile", "action.yml")
EXCLUDED_DIRS = (
    # Committed Fern output and its provenance records: history, not the pair.
    "tests/fixtures/",
    # Projects the checking project may not depend on (see the docstring).
    "tests/census_fallback/",
    "tests/corpus_match/",
    "tests/corpus_match_selection/",
    "tests/live_e2e/",
    "tests/runtime/",
    "tests/sdk_env/",
    "tools/release-packaging/",
    "tools/workspace/",
)
MARKER = "certified-pair: stand-in"
COMMENT = ("//", "#", "/*", "* ")

V = r"(\d+\.\d+\.\d+)"
# An optional backslash, for the forms written inside a Rust or Python string.
Q = r'\\?["\']'
CLI, SDK = "cli", "sdk"
# Each form, and the pair member(s) its version groups state, in group order.
FORMS: tuple[tuple[re.Pattern[str], tuple[str, ...]], ...] = (
    # `.fern/metadata.json`'s keys.
    (re.compile(Q + r"cliVersion" + Q + r"\s*:\s*" + Q + V), (CLI,)),
    (re.compile(Q + r"generatorVersion" + Q + r"\s*:\s*" + Q + V), (SDK,)),
    # Provenance keys: TOML, YAML, JSON and tuple spellings alike.
    (re.compile(r"\bfern_cli_version" + r"""[\\"'\s:=,]*""" + V), (CLI,)),
    (re.compile(r"\bfern_python_sdk_version" + r"""[\\"'\s:=,]*""" + V), (SDK,)),
    # Install and image references.
    (re.compile(r"\bfern-api@" + V), (CLI,)),
    (re.compile(r"fern-python-sdk:" + V), (SDK,)),
    (re.compile(r"\bpython-sdk@" + V), (SDK,)),
    # Labels naming both.
    (re.compile(r"\bFern CLI " + V + r"(?:,| /) python-sdk " + V), (CLI, SDK)),
    # A fern.config.json literal.
    (re.compile(r"organization" + Q + r"\s*:\s*[^,\n]*,\s*" + Q + r"version" + Q + r"\s*:\s*" + Q + V), (CLI,)),
    # A generators.yml block: the version line under the python generator's name.
    (re.compile(r"fernapi/fern-python-sdk(?:\\n|[\"'\s+])*version:\s*" + V), (SDK,)),
    # Constants and shell defaults.
    (
        re.compile(r"\bFERN_CLI(?:_VERSION)?\b(?:\s*:\s*&(?:'static\s+)?str|\s*:\s*str)?(?:\s*=\s*|:-)[\"']?" + V),
        (CLI,),
    ),
    (
        re.compile(
            r"\bFERN_PYTHON(?:_SDK)?(?:_VERSION)?\b(?:\s*:\s*&(?:'static\s+)?str|\s*:\s*str)?(?:\s*=\s*|:-)[\"']?" + V
        ),
        (SDK,),
    ),
    (re.compile(r"FernPair\(\s*cli\s*=\s*[\"']" + V + r"[\"']\s*,\s*generator\s*=\s*[\"']" + V), (CLI, SDK)),
)


class Pair(NamedTuple):
    cli: str
    sdk: str


class Drift(NamedTuple):
    path: str
    line: int
    text: str
    member: str
    stated: str


def certified(root: Path) -> Pair:
    """The pair `root`'s metadata.json declares."""
    path = root / METADATA
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
        return Pair(cli=str(record["cliVersion"]), sdk=str(record["generatorVersion"]))
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise SystemExit(
            f"certified-pair: cannot read cliVersion and generatorVersion from {METADATA.as_posix()} ({error}); "
            f"restore it with git checkout -- {METADATA.as_posix()}"
        ) from error


def scanned(root: Path) -> list[str]:
    """The tracked files under `root` that may state the pair."""
    listed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=False, text=True, encoding="utf-8"
    )
    if listed.returncode != 0:
        raise SystemExit(f"certified-pair: git ls-files failed in {root}: {listed.stderr.strip()}; run it in a clone")
    return [
        path
        for path in listed.stdout.split("\0")
        if (path.startswith(SCANNED_DIRS) or path in SCANNED_FILES) and not path.startswith(EXCLUDED_DIRS)
    ]


def drifts(path: str, text: str, pair: Pair) -> Iterable[Drift]:
    """Each statement in `text` naming a version other than `pair`'s."""
    lines = text.splitlines()
    wanted = {CLI: pair.cli, SDK: pair.sdk}
    for pattern, members in FORMS:
        for match in pattern.finditer(text):
            number = text.count("\n", 0, match.start()) + 1
            line = lines[number - 1] if number <= len(lines) else ""
            if MARKER in line or line.lstrip().startswith(COMMENT):
                continue
            for member, stated in zip(members, match.groups(), strict=True):
                if stated != wanted[member]:
                    yield Drift(path, number, line.strip(), member, stated)


def check(root: Path) -> list[Drift]:
    pair = certified(root)
    found: list[Drift] = []
    for path in scanned(root):
        try:
            text = (root / path).read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            continue  # binary, or a tracked file deleted in the worktree
        found.extend(drifts(path, text, pair))
    return sorted(set(found))


def main(argv: list[str]) -> int:
    if not argv or argv[0] != "check" or len(argv) > 2:
        print("usage: certified_pair.py check [ROOT]", file=sys.stderr)
        return 2
    root = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parents[2]
    found = check(root)
    if not found:
        return 0
    pair = certified(root)
    for drift in found:
        name = "Fern CLI" if drift.member == CLI else "fern-python-sdk"
        print(f"{drift.path}:{drift.line}: states {name} {drift.stated}: {drift.text}", file=sys.stderr)
    print(
        f"certified-pair: {len(found)} statement(s) disagree with {METADATA.as_posix()} "
        f"(Fern CLI {pair.cli}, fern-python-sdk {pair.sdk}); derive the version from that file, "
        f"or mark deliberate stand-in test data with `{MARKER}` on its line",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
