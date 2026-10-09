#!/usr/bin/env python3
"""Hold the Python tooling to one combined line-coverage floor.

    python tools/python-workspace/coverage_gate.py --fail-under PERCENT [--data DIR] [--by-project]

Every tooling project's `test` targets run pytest with coverage on and write
their data under `DIR/<project>/<target>/.coverage` (DIR defaults to
`.coverage-data`), subprocesses included (`[tool.coverage.run] patch`). This
combines all of it into `DIR/.coverage`, then holds the union to one floor.

The denominator is every Python source file under each tooling project's
directory — the first path of each `[tool.coverage.paths]` entry in the root
pyproject.toml — less the `omit` patterns (the test files themselves): `*.py`
files and extensionless scripts whose first line is a Python shebang. A file no
run recorded is added with nothing executed, so it counts as wholly uncovered;
coverage itself would never find a file that no test ran.

It reads `[tool.coverage]` from `./pyproject.toml` and does its combining and
reporting through the `coverage` CLI in child processes: a second
`coverage.Coverage` inside a process that is itself being measured (as this one
is, under its own suite) stops that process's data from being saved.

Quiet on success: one line. Below the floor: the files with missed lines, the
per-project totals, the total, and the next step. `--by-project` prints the
per-project totals on success too.

Exit status: 0 at or above the floor; 1 below it, or with no data to combine;
2 for an invocation it does not take.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path
from typing import TypeGuard

from coverage import CoverageData

TOOL = "python-coverage"
DATA_FILE = ".coverage"


def fail(message: str, action: str) -> int:
    print(f"{TOOL}: {message}", file=sys.stderr)
    print(f"{TOOL}: {action}", file=sys.stderr)
    return 1


def coverage_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """`python -m coverage ARGS` in a child, unmeasured itself."""
    environment = {name: value for name, value in os.environ.items() if not name.startswith("COVERAGE_PROCESS_")}
    return subprocess.run(
        [sys.executable, "-m", "coverage", *args], capture_output=True, text=True, env=environment, check=False
    )


def is_python_source(path: Path) -> bool:
    """A `*.py` file, or an extensionless script whose shebang runs Python."""
    if path.suffix == ".py":
        return True
    if path.suffix:
        return False
    with path.open("rb") as stream:
        first = stream.readline(256)
    return first.startswith(b"#!") and b"python" in first


def denominator(root: Path, sources: list[str], omit: list[str]) -> list[Path]:
    """Every Python source file under `sources`, relative to `root`, less `omit`."""
    found: set[Path] = set()
    for source in sources:
        top = (root / source).resolve()
        if not top.is_dir():
            raise FileNotFoundError(f"coverage path {source!r} is not a directory under {root}")
        for directory, subdirectories, files in os.walk(top):
            subdirectories[:] = sorted(name for name in subdirectories if name != "__pycache__")
            for name in files:
                path = Path(directory) / name
                if any(fnmatch.fnmatch(str(path), pattern) for pattern in omit):
                    continue
                if is_python_source(path):
                    found.add(path.relative_to(root.resolve()))
    return sorted(found)


def project_of(path: Path, sources: list[str]) -> str:
    """The tooling project directory holding `path`."""
    for source in sorted(sources, key=len, reverse=True):
        if path.as_posix().startswith(source.rstrip("/") + "/"):
            return source
    return "(outside every source)"


def by_project(analysis: dict[Path, tuple[int, int]], sources: list[str]) -> list[str]:
    totals: dict[str, list[int]] = {}
    for path, (statements, missed) in analysis.items():
        total = totals.setdefault(project_of(path, sources), [0, 0])
        total[0] += statements
        total[1] += missed
    lines = []
    for project, (statements, missed) in sorted(totals.items()):
        percent = 100.0 * (statements - missed) / statements if statements else 100.0
        lines.append(f"  {project:<36} {statements - missed:>6}/{statements:<6} {percent:6.2f}%")
    return lines


def strings(value: object) -> TypeGuard[list[str]]:
    return isinstance(value, list) and all(isinstance(item, str) and item for item in value)


def coverage_config(root: Path) -> tuple[list[str], list[str]]:
    """Each tooling project's directory (the first path of each `[tool.coverage.paths]`
    entry) and the `[tool.coverage.run] omit` patterns, from `root/pyproject.toml`.

    Raises ValueError naming the first setting that is not the shape coverage reads.
    """
    try:
        manifest = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f"pyproject.toml is not TOML: {error}") from error
    settings = manifest.get("tool", {}).get("coverage", {})
    paths = settings.get("paths", {}) if isinstance(settings, dict) else None
    if not isinstance(paths, dict):
        raise ValueError("[tool.coverage.paths] is not a table")
    for name, entries in paths.items():
        if not strings(entries) or not entries:
            raise ValueError(f"[tool.coverage.paths] {name} is {entries!r}, not a list of paths")
    run = settings.get("run", {})
    omit = run.get("omit", []) if isinstance(run, dict) else None
    if not strings(omit):
        raise ValueError(f"[tool.coverage.run] omit is {omit!r}, not a list of patterns")
    return [entries[0].rstrip("/") for entries in paths.values()], list(omit)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="coverage_gate.py", description=__doc__.split("\n\n")[0])
    parser.add_argument("--fail-under", type=float, required=True, help="the floor, in percent of lines")
    parser.add_argument("--data", type=Path, default=Path(".coverage-data"), help="the per-target data root")
    parser.add_argument("--by-project", action="store_true", help="print per-project totals on success too")
    args = parser.parse_args(argv)
    if not 0 < args.fail_under <= 100:
        parser.error(f"--fail-under must be a percentage in (0, 100], not {args.fail_under:g}")

    root = Path.cwd()
    if not (root / "pyproject.toml").is_file():
        return fail(f"no pyproject.toml in {root}", "run the gate from the repository root")
    try:
        sources, omit = coverage_config(root)
    except ValueError as error:
        return fail(str(error), "fix the coverage configuration in pyproject.toml")
    if not sources:
        return fail(
            "the coverage configuration names no project directories",
            "give every tooling project a [tool.coverage.paths] entry in pyproject.toml, its directory first",
        )
    try:
        files = denominator(root, sources, omit)
    except FileNotFoundError as error:
        return fail(str(error), "fix [tool.coverage.paths] in pyproject.toml")

    parts = sorted(args.data.glob(f"*/*/{DATA_FILE}"))
    if not parts:
        return fail(
            f"no coverage data under {args.data}/<project>/<target>/{DATA_FILE}",
            "run the tooling projects' tests first (`just test`, or `just nx run python-workspace:coverage`)",
        )
    combined = args.data / DATA_FILE
    combined.unlink(missing_ok=True)
    merged = coverage_cli("combine", "--keep", "--quiet", f"--data-file={combined}", *map(str, parts))
    if merged.returncode != 0:
        return fail(f"`coverage combine` failed: {merged.stderr.strip()}", "re-run the tooling projects' tests")

    data = CoverageData(basename=str(combined))
    data.read()
    recorded = {Path(name).resolve() for name in data.measured_files()}
    unrecorded = [path for path in files if (root / path).resolve() not in recorded]
    if unrecorded:
        data.touch_files([str(path) for path in unrecorded])
        data.write()

    with tempfile.TemporaryDirectory() as scratch:
        report = Path(scratch) / "coverage.json"
        # Only the denominator: a suite's scratch-only script (a patched copy under
        # another name) is in the data too, with no source left to read.
        exported = coverage_cli("json", "--quiet", f"--data-file={combined}", "-o", str(report), *map(str, files))
        if exported.returncode != 0:
            return fail(f"`coverage json` failed: {exported.stderr.strip()}", "re-run the tooling projects' tests")
        measured = {
            (root / name).resolve(): summary["summary"]
            for name, summary in json.loads(report.read_text(encoding="utf-8"))["files"].items()
        }
    analysis: dict[Path, tuple[int, int]] = {}
    for path in files:
        summary = measured.get((root / path).resolve())
        if summary is None:
            return fail(f"{path} is missing from the combined report", "re-run the tooling projects' tests")
        analysis[path] = (summary["num_statements"], summary["missing_lines"])
    total_statements = sum(statements for statements, _ in analysis.values())
    total_missed = sum(missed for _, missed in analysis.values())
    percent = 100.0 * (total_statements - total_missed) / total_statements if total_statements else 100.0
    summary_line = (
        f"{percent:.2f}% of {total_statements} lines across {len(files)} files "
        f"(floor {args.fail_under:g}%, {len(unrecorded)} never run)"
    )

    if round(percent, 2) < args.fail_under:
        table = coverage_cli("report", f"--data-file={combined}", "--skip-covered", "--sort=-miss", *map(str, files))
        print(table.stdout.rstrip(), file=sys.stderr)
        print(f"{TOOL}: per project:", file=sys.stderr)
        print("\n".join(by_project(analysis, sources)), file=sys.stderr)
        return fail(
            f"combined line coverage {summary_line} is below the floor",
            "cover the files above with real tests (a journey through the script, not a mock of it); "
            "lower the floor only with the measurement and the reason recorded in AGENTS.md",
        )
    print(f"{TOOL}: {summary_line}")
    if args.by_project:
        print("\n".join(by_project(analysis, sources)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
