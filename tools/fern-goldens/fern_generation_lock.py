#!/usr/bin/env python3
"""Serialize Fern on this host: the one lock every crozier Fern entry point holds.

Fern generations run one at a time on a host, because two overlapping runs spoil
any measurement that must run alone. Every crozier entry point that starts Fern
(`fern-references.py generate`, `fern-refusals.py`'s Fern runs, `weekly.py
shard`, `fern-goldens generate|run`, `generate-fern-fixture.sh` and the scripts
looping over it, `witness_screen.py`'s Fern screen, `output-insensitive-remeasure.py`
and the `justfile` recipes reaching Fern by another route) holds

    ${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock

for its whole Fern interval, so no caller wraps one in `flock`.

Nesting: an entry point started inside another one's hold shares that hold
rather than taking the lock again, which would deadlock. The holder exports
`CROZIER_FERN_GENERATION_LOCK_HOLDER=<its pid>` and records the same pid in
`fern-generation.lock.holder` beside the lock for as long as it holds it. A
process is inside that hold when the variable it inherited names that recorded
pid and the pid is the process itself or one of its ancestors, so a variable
leaked into an unrelated process, or one left from a hold already released,
never stands in for the lock. Where the platform offers no parent lookup (no
`/proc` and no `ps`, as on Windows), the ancestry cannot be read, so the
inherited variable naming the recorded pid is the hold: a nested entry point
there still shares its parent's hold rather than deadlocking on it, and one left
from a released hold still is not one, because releasing removes the record. A hold made outside these entry points (a hand
`flock` around a bare `fern` run) records no holder, so an entry point started
under it waits for it rather than joining it.

Usage: fern_generation_lock.py held
       fern_generation_lock.py run --label LABEL -- COMMAND [ARG...]

`held` exits 0 when this process is inside a hold, 1 when it is not. `run` holds
the lock (or shares the hold it was started in) while COMMAND runs and exits
with COMMAND's status; while another process holds it, it says so once on
stderr and waits. Where the lock cannot be taken (its directory is not
writable), `run` and every entry point exit 1 naming it and run no Fern. Exit 2
on a usage error.
"""

from __future__ import annotations

import argparse
import contextlib
import enum
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from collections.abc import Generator
from pathlib import Path
from typing import IO, NewType

HOLDER_ENV = "CROZIER_FERN_GENERATION_LOCK_HOLDER"
LOCK_NAME = "fern-generation.lock"
# How far up the process tree a holder is looked for: an entry point nests a few
# levels (a recipe, a family delegate, a script), never this many.
MAX_DEPTH = 64


def cache_root() -> Path:
    base = os.environ.get("XDG_CACHE_HOME") or ""
    return (Path(base) if os.path.isabs(base) else Path.home() / ".cache") / "crozier"


def lock_path() -> Path:
    return cache_root() / LOCK_NAME


def holder_path() -> Path:
    return lock_path().with_name(LOCK_NAME + ".holder")


# A process id read from outside this process (the inherited variable, the holder
# record, `/proc` or `ps`), only ever made by `parse_pid` or `own_pid`.
Pid = NewType("Pid", int)
PID = re.compile(r"[1-9][0-9]{0,9}")


def own_pid() -> Pid:
    return Pid(os.getpid())


def parse_pid(text: str) -> Pid | None:
    """A pid written as plain ASCII decimal, or None for anything else."""
    text = text.strip()
    return Pid(int(text)) if PID.fullmatch(text) else None


def recorded_holder() -> Pid | None:
    """The pid the current holder recorded, or None when no crozier entry point holds the lock."""
    try:
        text = holder_path().read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    return parse_pid(text)


PROC = Path("/proc")


class ParentLookup(enum.Enum):
    """How a platform reads a process's parent."""

    PROC = "proc"
    PS = "ps"


def parent_lookup() -> ParentLookup | None:
    """How this platform reads a process's parent: `PROC` where `/proc` is
    mounted, `PS` where a `ps` is on PATH off Windows (one on a Windows PATH is a
    POSIX layer's, naming its own pids), None where it offers neither. Decided
    from the platform, never from a lookup's result, so a lookup that fails where
    one exists refuses the hold rather than standing for no lookup."""
    if PROC.is_dir():
        return ParentLookup.PROC
    if sys.platform != "win32" and shutil.which("ps"):
        return ParentLookup.PS
    return None


def parent_of(pid: Pid, lookup: ParentLookup) -> Pid | None:
    """`pid`'s parent read through `lookup`, or None when that read fails."""
    if lookup is ParentLookup.PROC:
        try:
            # `pid (comm) state ppid …`: comm may hold spaces and parentheses.
            text = (PROC / str(pid) / "stat").read_text(encoding="utf-8", errors="replace")
            return parse_pid(text.rsplit(")", 1)[1].split()[1])
        except (OSError, IndexError, ValueError):
            return None
    try:
        shown = subprocess.run(
            ["ps", "-o", "ppid=", "-p", str(pid)], capture_output=True, text=True, check=False, timeout=10
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return parse_pid(shown.stdout)


def is_self_or_ancestor(pid: Pid, lookup: ParentLookup) -> bool:
    """Whether `pid` is this process or one of its ancestors, read through `lookup`;
    a failed read is no proof, so it answers False."""
    current: Pid | None = own_pid()
    for _ in range(MAX_DEPTH):
        if current is None:
            return False
        if current == pid:
            return True
        current = parent_of(current, lookup)
    return False


def held() -> bool:
    """Whether this process runs inside a crozier entry point's hold of the lock."""
    pid = parse_pid(os.environ.get(HOLDER_ENV, ""))
    if pid is None:
        return False
    if recorded_holder() != pid:
        return False
    if pid == own_pid():
        return True
    lookup = parent_lookup()
    # With no parent lookup on this platform the ancestry cannot be read, so the
    # inherited variable naming the recorded holder is the hold.
    return lookup is None or is_self_or_ancestor(pid, lookup)


# The lock primitive: `fcntl.flock` where the platform has it, `msvcrt.locking`
# on Windows, both released by the kernel if the holder dies. Where neither
# imports, the lock is the exclusive creation of `fern-generation.lock.held`
# beside the lock file, which a killed holder leaves behind: the wait then names
# that file to remove.
try:
    import fcntl
except ImportError:
    fcntl = None
try:
    import msvcrt
except ImportError:
    msvcrt = None
# How often a wait on the exclusive-create marker re-reads it, and how many of
# those reads pass between reminders naming the marker to remove.
MARKER_POLL_SECONDS = 0.1
MARKER_REMINDER_EVERY = 600


def _marker(handle: IO[str]) -> Path:
    return Path(handle.name).with_name(LOCK_NAME + ".held")


def _try_lock(handle: IO[str]) -> bool:
    if fcntl is not None and sys.platform != "win32":
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except BlockingIOError:
            return False
    if msvcrt is not None and sys.platform == "win32":
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            return True
        except OSError:
            return False
    try:
        os.close(os.open(_marker(handle), os.O_CREAT | os.O_EXCL | os.O_WRONLY))
        return True
    except FileExistsError:
        return False


def _lock(handle: IO[str]) -> None:
    if fcntl is not None and sys.platform != "win32":
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        return
    if msvcrt is not None and sys.platform == "win32":
        while True:
            try:
                # LK_LOCK gives up after about ten seconds, so wait again.
                msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
                return
            except OSError:
                continue
    polls = 0
    while not _try_lock(handle):
        polls += 1
        if polls % MARKER_REMINDER_EVERY == 0:
            print(
                f"still waiting on {_marker(handle)}; remove it if no Fern run holds the lock",
                file=sys.stderr,
                flush=True,
            )
        time.sleep(MARKER_POLL_SECONDS)


def _unlock(handle: IO[str]) -> None:
    if fcntl is not None and sys.platform != "win32":
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return
    if msvcrt is not None and sys.platform == "win32":
        with contextlib.suppress(OSError):
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        return
    _marker(handle).unlink(missing_ok=True)


def _record_holder(pid: Pid) -> None:
    path = holder_path()
    descriptor, staged = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(f"{pid}\n")
    os.replace(staged, path)


def unavailable(label: str, path: Path, error: OSError) -> SystemExit:
    """The exit an entry point takes when it cannot take the lock: no Fern runs."""
    return SystemExit(
        f"{label}: cannot take the host Fern generation lock at {path} ({error.strerror or error}); "
        f"make {path.parent} a writable directory (or point XDG_CACHE_HOME at one), then re-run"
    )


@contextlib.contextmanager
def hold(label: str) -> Generator[None]:
    """Hold the host's Fern generation lock for the block, or share the hold this
    process already runs inside; while another process holds it, say so once on
    stderr and wait."""
    if held():
        yield
        return
    path = lock_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        handle = path.open("a+", encoding="utf-8")
    except OSError as error:
        raise unavailable(label, path, error) from None
    try:
        if not _try_lock(handle):
            holder = recorded_holder()
            print(
                f"{label}: waiting for the host Fern generation lock {path} "
                f"({f'pid {holder}' if holder else 'another Fern run'} holds it; Fern runs one at a time on a host)",
                file=sys.stderr,
                flush=True,
            )
            _lock(handle)
            print(f"{label}: took the host Fern generation lock", file=sys.stderr, flush=True)
        previous = os.environ.get(HOLDER_ENV)
        try:
            try:
                _record_holder(own_pid())
            except OSError as error:
                raise unavailable(label, holder_path(), error) from None
            os.environ[HOLDER_ENV] = str(own_pid())
            yield
        finally:
            if previous is None:
                os.environ.pop(HOLDER_ENV, None)
            else:
                os.environ[HOLDER_ENV] = previous
            with contextlib.suppress(OSError):
                holder_path().unlink()
            _unlock(handle)
    finally:
        handle.close()


def run(label: str, command: list[str]) -> int:
    """`command`'s exit status, run inside the hold; a terminating signal reaches it too."""
    with hold(label):
        try:
            child = subprocess.Popen(command)
        except OSError as error:
            print(f"{label}: cannot start {command[0]}: {error}; check the path and re-run", file=sys.stderr)
            return 127

        def forward(signum: int, _frame: object) -> None:
            with contextlib.suppress(ProcessLookupError):
                child.send_signal(signum)

        forwarded = [signal.SIGTERM] + ([signal.SIGHUP] if hasattr(signal, "SIGHUP") else [])
        previous = {signum: signal.signal(signum, forward) for signum in forwarded}
        # The terminal delivers an interrupt to the child too; this process only
        # waits for it to finish.
        interrupt = signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            status = child.wait()
        finally:
            signal.signal(signal.SIGINT, interrupt)
            for signum, handler in previous.items():
                signal.signal(signum, handler)
    return 128 - status if status < 0 else status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="fern_generation_lock.py", description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("held", help="exit 0 inside a crozier entry point's hold, 1 outside one")
    running = commands.add_parser("run", help="run COMMAND holding the lock (or sharing the hold it runs in)")
    running.add_argument("--label", required=True, help="the entry point's name, for the waiting line")
    running.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    if args.command == "held":
        return 0 if held() else 1
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("run needs a COMMAND after --")
    return run(args.label, command)


if __name__ == "__main__":
    sys.exit(main())
