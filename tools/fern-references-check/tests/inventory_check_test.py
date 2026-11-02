"""`fern-references.py check` over the committed tree, as crozier's pull-request
gate runs it: every item the weekly Fern goldens run regenerates names inputs
that exist and evidence it can restate, so the change that breaks one fails
here, in seconds, rather than an hour into the next Monday's run.

The check starts no Fern, Docker or network request: a stand-in `fern` and
`docker` first on PATH record any call, and a `sitecustomize` refuses every
socket connection, and each run asserts neither happened. A second run traces
every path the check reads and holds this project's `test` inputs to that set,
so a pull request that moves, renames or deletes one reruns this suite.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TOOL = REPO / "tools/fern-goldens/fern-references.py"
PROJECT = REPO / "tools/fern-references-check/project.json"

# Loaded by every Python the check starts, before its own code: a socket
# connection ends the run, recorded where the test reads it, and with
# CHECK_TRACE set, every path under the root the run opens, stats or lists is
# written there as it exits.
SITECUSTOMIZE = r"""
import atexit, json, os, socket, sys

def _refuse(*args, **kwargs):
    with open(os.environ["CHECK_NETWORK"], "a", encoding="utf-8") as handle:
        handle.write(f"connect {args[1:] or kwargs}\n")
    raise SystemExit("inventory check guard: a network connection was attempted")

socket.socket.connect = _refuse
socket.socket.connect_ex = _refuse
socket.create_connection = _refuse

if os.environ.get("CHECK_TRACE"):
    _root = os.path.realpath(os.environ["CROZIER_FERN_REFERENCES_ROOT"])
    _seen = set()
    # Interpreter start-up (a venv's pyvenv.cfg, a coverage hook) is no read of
    # the check's: tracing starts once the interpreter opens the tool's script.
    _started = []

    def _from_coverage():
        # coverage.py (the suite's `patch = ["subprocess"]`) measures this run
        # and reads files of its own, such as a venv's pyvenv.cfg.
        frame = sys._getframe(2)
        while frame is not None:
            if frame.f_globals.get("__name__", "").startswith("coverage"):
                return True
            frame = frame.f_back
        return False

    def _note(kind, path):
        try:
            absolute = os.path.abspath(os.fsdecode(path))
        except TypeError:
            return
        if _from_coverage():
            return
        if not _started:
            if kind == "open" and absolute.endswith(os.sep + "fern-references.py"):
                _started.append(absolute)
            return
        if absolute.startswith(_root + os.sep):
            _seen.add((kind, os.path.relpath(absolute, _root)))

    def _hook(event, args):
        if event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
            _note("open", args[0])
        elif event in ("os.scandir", "os.listdir") and args and args[0] is not None:
            _note("list", args[0])

    sys.addaudithook(_hook)
    _stat = os.stat

    def _traced_stat(path, *args, **kwargs):
        if isinstance(path, (str, bytes, os.PathLike)):
            _note("stat", path)
        return _stat(path, *args, **kwargs)

    os.stat = _traced_stat
    atexit.register(lambda: open(os.environ["CHECK_TRACE"], "w", encoding="utf-8").write(json.dumps(sorted(_seen))))
"""

STAND_IN = '#!/bin/sh\necho "$(basename "$0") $*" >> "$CHECK_TOOL_CALLS"\nexit 97\n'


class Guarded:
    """A scratch PATH and site directory under which a run of the check can
    start neither Fern nor Docker nor a network connection unnoticed."""

    def __init__(self, scratch: Path) -> None:
        self.scratch = scratch
        self.bin = scratch / "bin"
        self.bin.mkdir()
        for tool in ("fern", "docker"):
            (self.bin / tool).write_text(STAND_IN, encoding="utf-8")
            (self.bin / tool).chmod(0o755)
        self.site = scratch / "site"
        self.site.mkdir()
        (self.site / "sitecustomize.py").write_text(textwrap.dedent(SITECUSTOMIZE), encoding="utf-8")
        self.calls = scratch / "tool-calls.log"
        self.network = scratch / "network.log"

    def env(self, root: Path, **extra: str) -> dict[str, str]:
        return {
            **os.environ,
            "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            "PYTHONPATH": str(self.site),
            "CROZIER_FERN_REFERENCES_ROOT": str(root),
            "CHECK_TOOL_CALLS": str(self.calls),
            "CHECK_NETWORK": str(self.network),
            **extra,
        }

    def run(
        self, case: unittest.TestCase, argv: list[str], root: Path, **extra: str
    ) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            argv, env=self.env(root, **extra), capture_output=True, text=True, encoding="utf-8", check=False
        )
        case.assertFalse(self.calls.exists(), f"the check started a tool: {self.read(self.calls)}")
        case.assertFalse(self.network.exists(), f"the check opened a connection: {self.read(self.network)}")
        return result

    @staticmethod
    def read(path: Path) -> str:
        return path.read_text(encoding="utf-8") if path.exists() else ""


def covers(pattern: str, path: str, *, directory: bool) -> bool:
    """Whether an Nx input glob (`*` within a segment, `**` across any number)
    matches `path`, or, for a directory, could match a file under it, which is
    how an input sees a directory appear or vanish."""
    parts, wanted = pattern.split("/"), path.split("/")

    def segment(glob: str, name: str) -> bool:
        return re.fullmatch(re.escape(glob).replace(r"\*", "[^/]*"), name) is not None

    def walk(i: int, j: int) -> bool:
        if j == len(wanted):
            return i < len(parts) if directory else i == len(parts) or parts[i:] == ["**"]
        if i == len(parts):
            return False
        if parts[i] == "**":
            return walk(i + 1, j) or walk(i, j + 1)
        return segment(parts[i], wanted[j]) and walk(i + 1, j + 1)

    return walk(0, 0)


@unittest.skipIf(os.name == "nt", "the stand-in tools are POSIX executables")
class CommittedInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.guard = Guarded(Path(temporary.name))

    def test_every_weekly_item_on_the_committed_tree_names_inputs_that_exist(self) -> None:
        result = self.guard.run(self, [sys.executable, str(TOOL), "check"], REPO)
        broken = result.stderr.strip()
        self.assertEqual(
            0,
            result.returncode,
            "the weekly Fern goldens run would fail these items before Fern starts; restore each input named, or "
            f"remove the entry that names it:\n{broken}",
        )
        self.assertEqual("", result.stdout)

    def test_this_suites_inputs_cover_every_path_the_check_reads(self) -> None:
        trace = self.guard.scratch / "trace.json"
        result = self.guard.run(self, [sys.executable, str(TOOL), "check"], REPO, CHECK_TRACE=str(trace))
        self.assertIn(result.returncode, (0, 1), result.stderr)
        reads = json.loads(trace.read_text(encoding="utf-8"))
        self.assertGreater(len(reads), 1000, "the trace saw the check read the inventory")
        self.assertIn(["open", "docs/fern-measurements/cases.tsv"], reads)
        inputs = json.loads(PROJECT.read_text(encoding="utf-8"))["targets"]["test"]["inputs"]
        globs = [entry.removeprefix("{workspaceRoot}/") for entry in inputs if entry.startswith("{workspaceRoot}/")]

        def covered(kind: str, path: str) -> bool:
            # A listed directory, or one that exists, is seen through a file under
            # it; a path the check found absent may later appear as either.
            target = REPO / path
            seen_as_directory = kind == "list" or target.is_dir()
            kinds = (True,) if seen_as_directory else (False,) if target.exists() else (False, True)
            return any(covers(glob, path, directory=directory) for glob in globs for directory in kinds)

        uncovered = sorted(
            {
                path
                for kind, path in reads
                if not path.startswith((".venv/", "tools/fern-references-check/")) and not covered(kind, path)
            }
        )
        self.assertEqual(
            [],
            uncovered,
            "fern-references.py check reads these, which tools/fern-references-check/project.json's test inputs "
            "do not cover, so a change to them would not rerun this gate; add an input glob for each",
        )

    def test_the_guard_catches_a_tool_call_and_a_connection(self) -> None:
        """What makes the two runs above evidence: under the same environment, a
        call to `fern` or `docker` and a socket connection are each recorded."""
        env = self.guard.env(REPO)
        subprocess.run(["fern", "check"], env=env, capture_output=True, check=False)
        subprocess.run(["docker", "info"], env=env, capture_output=True, check=False)
        self.assertEqual("fern check\ndocker info\n", self.guard.read(self.guard.calls))
        connected = subprocess.run(
            [sys.executable, "-c", "import socket; socket.create_connection(('127.0.0.1', 9))"],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(0, connected.returncode)
        self.assertIn("a network connection was attempted", connected.stderr)
        self.assertIn("connect", self.guard.read(self.guard.network))


class GlobTests(unittest.TestCase):
    def test_a_glob_covers_files_and_the_directories_files_could_appear_in(self) -> None:
        self.assertTrue(covers("docs/x/*/openapi.yml", "docs/x/a/openapi.yml", directory=False))
        self.assertFalse(covers("docs/x/*/openapi.yml", "docs/x/a/b/openapi.yml", directory=False))
        self.assertTrue(covers("docs/x/**/evidence.md", "docs/x/a/b/evidence.md", directory=False))
        self.assertTrue(covers("docs/x/**/*", "docs/x/a", directory=False))
        self.assertTrue(covers("docs/x/*/fern-expected/.fern/metadata.json", "docs/x/a/fern-expected", directory=True))
        self.assertFalse(covers("docs/x/*/openapi.yml", "docs/x/a/openapi.yml", directory=True))
        self.assertFalse(covers("tests/fixtures/*/openapi.yml", "docs/x/a", directory=True))


if __name__ == "__main__":
    unittest.main()
