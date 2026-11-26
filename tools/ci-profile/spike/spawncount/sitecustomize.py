"""SPIKE ONLY (spike-windows-lane-breakdown): count every child process and tree copy.

Loaded through PYTHONPATH when SPIKE_SPAWN_LOG names a directory: each Python process
appends one JSON line per subprocess start (its program) and per shutil tree copy or
removal (its seconds) to <dir>/py-<pid>.jsonl, tagged with the pytest test and Nx task
it runs under (PYTEST_CURRENT_TEST is inherited by children, so a grandchild's spawn is
still charged to its test). Counts are platform-independent, so a Linux run's counts
times a Windows runner's per-spawn cost divides a Windows test's time into spawns.
"""

import json
import os
import shutil
import subprocess
import sys
import threading
import time

_DIR = os.environ.get("SPIKE_SPAWN_LOG")


def _write(record: dict) -> None:
    record.update(
        pid=os.getpid(),
        test=os.environ.get("PYTEST_CURRENT_TEST"),
        nx=f"{os.environ.get('NX_TASK_TARGET_PROJECT')}:{os.environ.get('NX_TASK_TARGET_TARGET')}",
    )
    try:
        with open(os.path.join(_DIR, f"py-{os.getpid()}.jsonl"), "a", encoding="utf-8") as out:
            out.write(json.dumps(record) + "\n")
    except OSError:
        pass


def _hook(event: str, args: tuple) -> None:
    if event == "subprocess.Popen":
        argv = args[1]
        first = argv if isinstance(argv, (str, bytes)) else (argv[0] if argv else args[0])
        program = os.path.basename(os.fsdecode(first).split()[0]) if first else "?"
        _write({"event": "spawn", "program": program.removesuffix(".exe")})


_depth = threading.local()


def _timed(name: str, function):
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
            _write({"event": name, "seconds": time.perf_counter() - start})

    return wrapper


def _program(argv) -> str:
    first = argv if isinstance(argv, (str, bytes)) else (argv[0] if argv else "?")
    return os.path.basename(os.fsdecode(first).split()[0]).removesuffix(".exe") if first else "?"


_init = subprocess.Popen.__init__
_wait = subprocess.Popen.wait


def _popen_init(self, args, *a, **k):
    self._spike = (time.perf_counter(), _program(args))
    _init(self, args, *a, **k)


def _popen_wait(self, *a, **k):
    code = _wait(self, *a, **k)
    spike = getattr(self, "_spike", None)
    if spike:
        self._spike = None
        _write({"event": "child", "program": spike[1], "seconds": time.perf_counter() - spike[0]})
    return code


if _DIR and not os.environ.get("SPIKE_SPAWN_OFF"):
    sys.addaudithook(_hook)
    shutil.copytree = _timed("copytree", shutil.copytree)
    shutil.rmtree = _timed("rmtree", shutil.rmtree)
    subprocess.Popen.__init__ = _popen_init
    subprocess.Popen.wait = _popen_wait
