#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier uses Cargo and just rather than Nx; this real-recipe journey belongs to test-corpus-offline and CI live-e2e.
"""Drive real corpus recipes without sockets or an ignored corpus cache (Linux)."""
from __future__ import annotations

import ctypes
import errno
import os
import platform
import re
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from collections.abc import Mapping

REPO = Path(__file__).resolve().parent.parent


def deny_network() -> None:
    """Install an inherited seccomp filter denying socket creation, even in curl."""
    socket_syscall = {"x86_64": 41, "aarch64": 198}[platform.machine()]

    class Filter(ctypes.Structure):
        _fields_ = [("code", ctypes.c_ushort), ("jt", ctypes.c_ubyte),
                    ("jf", ctypes.c_ubyte), ("k", ctypes.c_uint)]

    class Program(ctypes.Structure):
        _fields_ = [("len", ctypes.c_ushort), ("filter", ctypes.POINTER(Filter))]

    instructions = (Filter * 4)(
        Filter(0x20, 0, 0, 0),  # load syscall number
        Filter(0x15, 0, 1, socket_syscall),
        Filter(0x06, 0, 0, 0x00050000 | errno.EPERM),
        Filter(0x06, 0, 0, 0x7FFF0000),
    )
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(38, 1, 0, 0, 0) or libc.prctl(22, 2, ctypes.byref(Program(4, instructions))):
        raise OSError(ctypes.get_errno(), "could not disable sockets")


def warm_dependencies(case: unittest.TestCase, env: Mapping[str, str]) -> None:
    """Fetch every build dependency (never a specification) while the network is up."""
    # The recipes compile crozier's tests, so a cold registry (a fresh CI
    # runner's) needs every locked crate downloaded before sockets go away.
    fetch = subprocess.run(["cargo", "fetch", "--locked"], cwd=REPO, env=env,
                           capture_output=True, text=True)
    case.assertEqual(0, fetch.returncode, fetch.stderr)
    # The fallback samples need the pinned parser: install that package so
    # the denied run resolves it from uv's cache alone.
    pin = REPO / "tools/surface-census/golden-reach-search.py"
    if pin.is_file():
        dependency = re.search(r'^# dependencies = \["(.*)"\]$', pin.read_text(encoding="utf-8"), re.M)
        case.assertIsNotNone(dependency, f"{pin.relative_to(REPO)} lost its '# dependencies = [\"...\"]' pin; restore it")
        warm = subprocess.run(
            ["uv", "run", "--no-project", "--with", dependency.group(1), "python3", "-c", ""],
            cwd=REPO, env=env, capture_output=True, text=True,
        )
        case.assertEqual(0, warm.returncode, warm.stderr)


@unittest.skipUnless(sys.platform == "linux" and platform.machine() in {"x86_64", "aarch64"},
                     "network-denial proof uses Linux seccomp")
class OfflineCorpusRecipes(unittest.TestCase):
    def test_warmed_build_needs_no_network_from_a_cold_registry(self) -> None:
        # CI's runner starts with no crates cached; a denied recipe then failed
        # resolving static.crates.io. Reproduce that cold registry here.
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as cold:
            env = {**os.environ, "CARGO_HOME": cold, "RUSTC_WRAPPER": ""}
            warm_dependencies(self, env)
            build = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                 "cargo", "test", "--locked", "--no-run", "-p", "crozier-e2e", "--test", "e2e"],
                cwd=REPO, env=env, capture_output=True, text=True,
            )
            self.assertEqual(0, build.returncode, build.stderr)

    def test_real_recipes_without_network_or_cache(self) -> None:
        # The registered corpus cache, and the cache the census-fallback samples
        # were once fetched into: neither may exist or come back.
        caches = (REPO / ".local/corpus", REPO / ".local/census-fallback-sample")
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as directory:
            hidden = [Path(directory) / f"cache-{index}" for index in range(len(caches))]
            held = [cache.exists() for cache in caches]
            for cache, aside, present in zip(caches, hidden, held):
                if present:
                    cache.rename(aside)
            try:
                self.assertFalse(any(cache.exists() for cache in caches))
                probe = subprocess.run(
                    [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                     sys.executable, "-c", "import socket; socket.socket()"],
                    cwd=REPO, capture_output=True, text=True,
                )
                self.assertNotEqual(0, probe.returncode)
                self.assertIn("Operation not permitted", probe.stderr)
                warm_dependencies(self, os.environ)
                for recipe in ("test-corpus-match", "test-corpus-match-strict", "surface-census",
                               "test-fern-refusals", "test-census-fallback-samples"):
                    with self.subTest(recipe=recipe):
                        result = subprocess.run(
                            [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                             "just", recipe], cwd=REPO, capture_output=True, text=True,
                            # A user-level sccache daemon needs a socket; the repo
                            # build contract has no wrapper and works offline.
                            env={**os.environ, "RUSTC_WRAPPER": "", "UV_OFFLINE": "1"},
                        )
                        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                        for cache in caches:
                            self.assertFalse(cache.exists(), f"recipe recreated {cache.relative_to(REPO)}")
            finally:
                # A failing recipe can create a new cache. Move that test output
                # aside before restoring the caller's original directories.
                for index, (cache, aside, present) in enumerate(zip(caches, hidden, held)):
                    if cache.exists():
                        cache.rename(Path(directory) / f"unexpected-cache-{index}")
                    if present:
                        aside.rename(cache)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--deny-network":
        deny_network()
        os.execvp(sys.argv[2], sys.argv[2:])
    (REPO / ".local").mkdir(exist_ok=True)
    unittest.main()
