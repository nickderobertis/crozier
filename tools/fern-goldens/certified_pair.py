#!/usr/bin/env python3
"""Hold every statement of the certified Fern pair to its one declaration.

`assets/scaffolding/metadata.json` declares the pair crozier is certified
against: `cliVersion` (the Fern CLI) and `generatorVersion`
(`fernapi/fern-python-sdk`). Code, tools, recipes and tests derive the pair from
that file; one that spells it out instead drifts the day the pair moves. This
check scans every tracked file for the forms a pair statement takes in this
repository, and fails on any that names a version other than the file's.

Committed Fern output and dated records (`tests/fixtures/`, `docs/`,
`CHANGELOG.md`) are history, not statements of the current pair, and are never
scanned; nor is a comment line, which is prose like `docs/` (often a dated
measurement: "measured at fernapi/fern-python-sdk:X"). Test data that
deliberately names another version (a stand-in to prove a mismatch is caught)
carries `certified-pair: stand-in` on the line the statement starts on; nothing
else is exempt.

A target's inputs are its cache key and affected trigger, and nx.json's
`boundaries` let the project running the whole-tree check (`fern-goldens-git`)
take no input from the promoted tiers, the release-packaging suite or the
workspace aggregate. So `check` scans every tracked file outside those
`DELEGATED` roots, and each of those projects runs `check --within <its root>`
as its own `lint-certified-pair` target: together they cover the tree. `--within`
takes only a `DELEGATED` root, and holds that root's own `project.json` to the
wiring: a `lint-certified-pair` target running exactly that command, which its
`lint` depends on.

Usage: certified_pair.py check [ROOT] [--within DIR]

Exit status: 0 when every statement names the declared pair; 1 when one names
another (each printed on stderr), the declaration is unreadable or malformed, or
a `--within` root is not delegated or not wired; 2 on a usage error.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Literal, NamedTuple

METADATA = Path("assets") / "scaffolding" / "metadata.json"
# Committed Fern output, its provenance records and dated prose: history, not
# the pair.
HISTORY_DIRS = ("tests/fixtures/", "docs/")
HISTORY_FILES = ("CHANGELOG.md",)
# Roots whose own project checks them with `--within` (see the docstring). The
# whole-tree check may not read those projects' definitions (nx.json's
# `boundaries`), so each `--within` run reconciles its own project's wiring
# (`wiring_failures`); a project whose target is dropped together with its
# `lint` dependency is beyond any check this project may run.
# llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] Each delegated project's own lint reconciles its wiring to this tuple (`wiring_failures`), and the tuple to the tracked tree is tested; a gate catching a target removed together with its lint dependency would have to read the promoted tiers' and the workspace aggregate's project definitions, an edge nx.json's `boundaries` forbid this tooling project and every project those definitions may be read from.
DELEGATED = (
    "tests/census_fallback/",
    "tests/corpus_match/",
    "tests/corpus_match_selection/",
    "tests/live_e2e/",
    "tests/runtime/",
    "tests/sdk_env/",
    "tools/release-packaging/",
    "tools/workspace/",
)
# llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]
MARKER = "certified-pair: stand-in"
COMMENT = ("//", "#", "/*", "* ")

# The declaration's grammar: an exact stable version, as every reader of
# metadata.json takes it.
STABLE = r"\d+\.\d+\.\d+"
# A statement's whole version: a suffix is part of what it states, so one on the
# declared numbers still differs from the declaration.
V = r"(" + STABLE + r"(?:[-+][0-9A-Za-z.-]*[0-9A-Za-z])?)"
# An optional backslash, for the forms written inside a Rust or Python string.
Q = r'\\?["\']'
Member = Literal["cli", "sdk"]
CLI: Member = "cli"
SDK: Member = "sdk"


class Form(NamedTuple):
    """One way the repository states the pair: its pattern, and the pair member
    each of its version groups states, in group order."""

    pattern: re.Pattern[str]
    members: tuple[Member, ...]


FORMS: tuple[Form, ...] = (
    # `.fern/metadata.json`'s keys.
    Form(re.compile(Q + r"cliVersion" + Q + r"\s*:\s*" + Q + V), (CLI,)),
    Form(re.compile(Q + r"generatorVersion" + Q + r"\s*:\s*" + Q + V), (SDK,)),
    # Provenance keys: TOML, YAML, JSON and tuple spellings alike.
    Form(re.compile(r"\bfern_cli_version" + r"""[\\"'\s:=,]*""" + V), (CLI,)),
    Form(re.compile(r"\bfern_python_sdk_version" + r"""[\\"'\s:=,]*""" + V), (SDK,)),
    # Install and image references.
    Form(re.compile(r"\bfern-api@" + V), (CLI,)),
    Form(re.compile(r"fern-python-sdk:" + V), (SDK,)),
    Form(re.compile(r"\bpython-sdk@" + V), (SDK,)),
    # Labels naming both.
    Form(re.compile(r"\bFern CLI " + V + r"(?:,| /) python-sdk " + V), (CLI, SDK)),
    # A fern.config.json literal.
    Form(re.compile(r"organization" + Q + r"\s*:\s*[^,\n]*,\s*" + Q + r"version" + Q + r"\s*:\s*" + Q + V), (CLI,)),
    # A generators.yml block: the version line under the python generator's name.
    Form(re.compile(r"fernapi/fern-python-sdk(?:\\n|[\"'\s+])*version:\s*" + V), (SDK,)),
    # Constants and shell defaults.
    Form(
        re.compile(r"\bFERN_CLI(?:_VERSION)?\b(?:\s*:\s*&(?:'static\s+)?str|\s*:\s*str)?(?:\s*=\s*|:-)[\"']?" + V),
        (CLI,),
    ),
    Form(
        re.compile(
            r"\bFERN_PYTHON(?:_SDK)?(?:_VERSION)?\b(?:\s*:\s*&(?:'static\s+)?str|\s*:\s*str)?(?:\s*=\s*|:-)[\"']?" + V
        ),
        (SDK,),
    ),
    Form(re.compile(r"FernPair\(\s*cli\s*=\s*[\"']" + V + r"[\"']\s*,\s*generator\s*=\s*[\"']" + V), (CLI, SDK)),
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
    fix = f"restore it with git checkout -- {METADATA.as_posix()}"
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SystemExit(
            f"certified-pair: cannot read cliVersion and generatorVersion from {METADATA.as_posix()} ({error}); {fix}"
        ) from error
    cli = record.get("cliVersion") if isinstance(record, dict) else None
    sdk = record.get("generatorVersion") if isinstance(record, dict) else None
    if not (isinstance(cli, str) and re.fullmatch(STABLE, cli) and isinstance(sdk, str) and re.fullmatch(STABLE, sdk)):
        raise SystemExit(
            f"certified-pair: {METADATA.as_posix()} must be an object whose cliVersion and generatorVersion "
            f"are exact versions, not {cli!r} and {sdk!r}; {fix}"
        )
    return Pair(cli=cli, sdk=sdk)


def scanned(root: Path, within: str | None = None) -> list[str]:
    """The tracked files under `root` that may state the pair: those under
    `within` when it is given, else every one outside the `DELEGATED` roots."""
    listed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=False, text=True, encoding="utf-8"
    )
    if listed.returncode != 0:
        raise SystemExit(f"certified-pair: git ls-files failed in {root}: {listed.stderr.strip()}; run it in a clone")
    prefix = within.strip("/") + "/" if within is not None else None
    return [
        path
        for path in listed.stdout.split("\0")
        if path
        and not path.startswith(HISTORY_DIRS)
        and path not in HISTORY_FILES
        and (path.startswith(prefix) if prefix is not None else not path.startswith(DELEGATED))
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


def wiring_failures(root: Path, within: str) -> list[str]:
    """Why the project rooted at `within` does not run this check over itself from its `lint`, or nothing."""
    path = f"{within}/project.json"
    command = f"python3 tools/fern-goldens/certified_pair.py check --within {within}"
    try:
        targets = json.loads((root / path).read_text(encoding="utf-8")).get("targets")
    except (OSError, ValueError, AttributeError) as error:
        return [f"{path} is no readable project definition ({error}); restore it with git checkout -- {path}"]
    if not isinstance(targets, dict):
        return [f"{path} declares no targets; restore it with git checkout -- {path}"]
    target, lint = targets.get("lint-certified-pair"), targets.get("lint")
    options = target.get("options") if isinstance(target, dict) else None
    depends = lint.get("dependsOn") if isinstance(lint, dict) else None
    wrong = []
    if not isinstance(options, dict) or options.get("command") != command:
        wrong.append(f"{path}'s lint-certified-pair target must run `{command}`")
    if not isinstance(depends, list) or "lint-certified-pair" not in depends:
        wrong.append(f"{path}'s lint target must depend on lint-certified-pair")
    return wrong


def check(root: Path, within: str | None = None) -> list[Drift]:
    pair = certified(root)
    found: list[Drift] = []
    for path in scanned(root, within):
        try:
            text = (root / path).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            # Binary, deleted in the worktree, replaced by a directory (Windows reports that as
            # PermissionError, not IsADirectoryError), or otherwise unreadable.
            continue
        found.extend(drifts(path, text, pair))
    return sorted(set(found))


def main(argv: list[str]) -> int:
    within = None
    if len(argv) >= 2 and argv[-2] == "--within":
        within, argv = argv[-1].removeprefix("./").strip("/"), argv[:-2]
    if not argv or argv[0] != "check" or len(argv) > 2 or within == "":
        print("usage: certified_pair.py check [ROOT] [--within DIR]", file=sys.stderr)
        return 2
    root = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parents[2]
    if within is not None:
        if f"{within}/" not in DELEGATED:
            print(
                f"certified-pair: --within {within} is no delegated root ({', '.join(DELEGATED)}); "
                "the whole-tree check covers every other path",
                file=sys.stderr,
            )
            return 1
        wiring = wiring_failures(root, within)
        if wiring:
            for line in wiring:
                print(f"certified-pair: {line}", file=sys.stderr)
            return 1
    found = check(root, within)
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
