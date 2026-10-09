#!/usr/bin/env python3
"""Drive real corpus recipes without sockets or an ignored corpus cache (Linux)."""
from __future__ import annotations

import ctypes
import errno
import os
import platform
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from collections.abc import Mapping

REPO = Path(__file__).resolve().parents[2]


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
    # The pin is read, and held to its one exact `package==version`, by the
    # fallback's own runner, the one place that parses it. A checkout without
    # the fallback (the recovery suite's synthetic root) has no parser to warm.
    if (REPO / "tools/surface-census/golden-reach-search.py").is_file():
        pin = subprocess.run(["bash", "tests/census_fallback/run.sh", "pin", "tools/surface-census/golden-reach-search.py"],
                             cwd=REPO, env=env, capture_output=True, text=True)
        case.assertEqual(0, pin.returncode, pin.stderr)
        warm = subprocess.run(
            ["uv", "run", "--no-project", "--with", pin.stdout.strip(), "python3", "-c", ""],
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
                # The refusal-class gate is the offline `fern-refusals` project's
                # target, not the `test-fern-refusals` alias: that alias also runs
                # fern-refusals-strict, whose `measure` journeys fetch from a
                # loopback server, and a denied socket() denies loopback too.
                for recipe in (("test-corpus-match",), ("test-corpus-match-strict",), ("surface-census",),
                               ("nx", "run", "fern-refusals:test"), ("test-census-fallback-samples",)):
                    with self.subTest(recipe=" ".join(recipe)):
                        result = subprocess.run(
                            [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                             "just", *recipe], cwd=REPO, capture_output=True, text=True,
                            # A user-level sccache daemon needs a socket; the repo
                            # build contract has no wrapper and works offline.
                            # A replayed cache entry would prove nothing about the
                            # network, so each recipe's target really runs; and Nx
                            # loads its plugins in-process, since an isolated plugin
                            # worker reaches Nx over a socket the filter denies.
                            env={**os.environ, "RUSTC_WRAPPER": "", "UV_OFFLINE": "1", "NX_SKIP_NX_CACHE": "true",
                                 "NX_ISOLATE_PLUGINS": "false"},
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
