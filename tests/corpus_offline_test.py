#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier uses Cargo and just rather than Nx; this real-recipe journey belongs to test-corpus-offline and CI live-e2e.
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


@unittest.skipUnless(sys.platform == "linux" and platform.machine() in {"x86_64", "aarch64"},
                     "network-denial proof uses Linux seccomp")
class OfflineCorpusRecipes(unittest.TestCase):
    def test_real_recipes_without_network_or_cache(self) -> None:
        cache = REPO / ".local/corpus"
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as directory:
            hidden = Path(directory) / "cache"
            had_cache = cache.exists()
            if had_cache:
                cache.rename(hidden)
            try:
                self.assertFalse(cache.exists())
                probe = subprocess.run(
                    [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                     sys.executable, "-c", "import socket; socket.socket()"],
                    cwd=REPO, capture_output=True, text=True,
                )
                self.assertNotEqual(0, probe.returncode)
                self.assertIn("Operation not permitted", probe.stderr)
                for recipe in ("test-corpus-match", "test-corpus-match-strict", "surface-census",
                               "test-fern-refusals"):
                    with self.subTest(recipe=recipe):
                        result = subprocess.run(
                            [sys.executable, str(Path(__file__).resolve()), "--deny-network",
                             "just", recipe], cwd=REPO, capture_output=True, text=True,
                            # A user-level sccache daemon needs a socket; the repo
                            # build contract has no wrapper and works offline.
                            env={**os.environ, "RUSTC_WRAPPER": ""},
                        )
                        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                        self.assertFalse(cache.exists(), "recipe recreated the corpus cache")
            finally:
                # A failing recipe can create a new cache. Move that test output
                # aside before restoring the caller's original directory.
                if cache.exists():
                    cache.rename(Path(directory) / "unexpected-cache")
                if had_cache:
                    hidden.rename(cache)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--deny-network":
        deny_network()
        os.execvp(sys.argv[2], sys.argv[2:])
    (REPO / ".local").mkdir(exist_ok=True)
    unittest.main()
