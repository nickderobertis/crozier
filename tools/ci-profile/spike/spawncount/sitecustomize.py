"""SPIKE ONLY (spike-windows-lane-breakdown): count every child process and tree copy.

Loaded through PYTHONPATH when SPIKE_SPAWN_LOG names a directory: each Python process
appends one JSON line per subprocess start, per finished child (its wall seconds) and per
outermost shutil tree copy or removal (its seconds) to <dir>/py-<pid>.jsonl, tagged with
the pytest test and Nx task it runs under. PYTEST_CURRENT_TEST is inherited by children,
so a grandchild's spawn is still charged to its test. Counts are platform-independent, so
a Linux run's counts times a Windows runner's per-spawn cost divides a Windows test's time
into spawns.
"""

import json
import os
import shutil
import subprocess
import sys
import threading
import time
from dataclasses import asdict, dataclass, field
from typing import Literal

_DIR = os.environ.get("SPIKE_SPAWN_LOG", "")


@dataclass(frozen=True)
class Record:
    """One line of the log: what happened, under which test and Nx task."""

    event: Literal["spawn", "child", "copytree", "rmtree"]
    program: str | None = None
    seconds: float | None = None
    pid: int = field(default_factory=os.getpid)
    test: str | None = field(default_factory=lambda: os.environ.get("PYTEST_CURRENT_TEST"))
    nx: str = field(
        default_factory=lambda: f"{os.environ.get('NX_TASK_TARGET_PROJECT')}:{os.environ.get('NX_TASK_TARGET_TARGET')}"
    )


@dataclass(frozen=True)
class Started:
    """A child's start time and program, kept on its Popen until it is waited for."""

    at: float
    program: str


def _write(record: Record) -> None:
    # A log write that fails loses one record; it never fails the test being measured.
    try:
        with open(os.path.join(_DIR, f"py-{os.getpid()}.jsonl"), "a", encoding="utf-8") as out:
            out.write(json.dumps({k: v for k, v in asdict(record).items() if v is not None}) + "\n")
    except OSError:
        pass


def _program(argv) -> str:
    first = argv if isinstance(argv, (str, bytes)) else (argv[0] if argv else "?")
    return os.path.basename(os.fsdecode(first).split()[0]).removesuffix(".exe") if first else "?"


def _hook(event: str, args: tuple) -> None:
    if event == "subprocess.Popen":
        _write(Record("spawn", program=_program(args[1] or args[0])))


_depth = threading.local()


def _timed(name: Literal["copytree", "rmtree"], function):
    # copytree recurses through the module-level name: only the outermost call is timed.
    def wrapper(*a, **k):
        if getattr(_depth, name, 0):
            return function(*a, **k)
        setattr(_depth, name, 1)
        start = time.perf_counter()
        try:
            return function(*a, **k)
        finally:
            setattr(_depth, name, 0)
            _write(Record(name, seconds=time.perf_counter() - start))

    return wrapper


_init = subprocess.Popen.__init__
_wait = subprocess.Popen.wait


def _popen_init(self, args, *a, **k):
    self._spike = Started(time.perf_counter(), _program(args))
    _init(self, args, *a, **k)


def _popen_wait(self, *a, **k):
    code = _wait(self, *a, **k)
    started = getattr(self, "_spike", None)
    if started:
        self._spike = None
        _write(Record("child", program=started.program, seconds=time.perf_counter() - started.at))
    return code


if _DIR and not os.environ.get("SPIKE_SPAWN_OFF"):
    sys.addaudithook(_hook)
    shutil.copytree = _timed("copytree", shutil.copytree)
    shutil.rmtree = _timed("rmtree", shutil.rmtree)
    subprocess.Popen.__init__ = _popen_init
    subprocess.Popen.wait = _popen_wait
