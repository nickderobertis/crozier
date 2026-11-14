#!/usr/bin/env python3
"""Drive real corpus recipes without sockets or an ignored corpus cache (Linux)."""

from __future__ import annotations

import ctypes
import errno
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
import unittest
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import ClassVar

REPO = Path(__file__).resolve().parents[2]
HANDOFF_ENV = "CROZIER_COLD_REGISTRY_HANDOFF"
# The golden replays' profile (Cargo.toml `[profile.e2e]`): the build every corpus recipe uses.
CARGO_TEST = ("cargo", "test", "--locked", "--profile", "e2e", "--no-run", "-p", "crozier-e2e", "--test", "e2e")
CARGO_BIN = ("cargo", "build", "--locked", "--quiet", "--profile", "e2e", "-p", "crozier", "--bin", "crozier")


# The recipes proved with sockets denied, in two halves so each runs on its own inputs:
# `goldens` holds the corpus byte-match (the `corpus-match` project's `test-offline`),
# `tools` the census, the refusal-class gate and the fallback samples (`test-offline-tools`).
# The refusal-class gate is the offline `fern-refusals` project's target, not the
# `test-fern-refusals` alias: that alias also runs fern-refusals-strict, whose `measure`
# journeys fetch from a loopback server, and a denied socket() denies loopback too.
OFFLINE_RECIPES: dict[str, tuple[tuple[str, ...], ...]] = {
    "goldens": (("test-corpus-match",), ("test-corpus-match-strict",)),
    "tools": (("surface-census",), ("nx", "run", "fern-refusals:test"), ("test-census-fallback-samples",)),
}
RECIPES_ENV = "CORPUS_OFFLINE_RECIPES"


def offline_recipes() -> tuple[tuple[str, ...], ...]:
    """The recipes `CORPUS_OFFLINE_RECIPES` names (`goldens` or `tools`), or both halves when unset."""
    half = os.environ.get(RECIPES_ENV, "")
    if not half:
        return (*OFFLINE_RECIPES["goldens"], *OFFLINE_RECIPES["tools"])
    if half not in OFFLINE_RECIPES:
        raise SystemExit(f"{RECIPES_ENV} is {half!r}; set it to goldens or tools, or unset it for both")
    return OFFLINE_RECIPES[half]


def deny_network() -> None:
    """Install an inherited seccomp filter denying socket creation, even in curl."""
    socket_syscall = {"x86_64": 41, "aarch64": 198}[platform.machine()]

    class Filter(ctypes.Structure):
        _fields_: ClassVar = [
            ("code", ctypes.c_ushort),
            ("jt", ctypes.c_ubyte),
            ("jf", ctypes.c_ubyte),
            ("k", ctypes.c_uint),
        ]

    class Program(ctypes.Structure):
        _fields_: ClassVar = [("len", ctypes.c_ushort), ("filter", ctypes.POINTER(Filter))]

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
    fetch = subprocess.run(["cargo", "fetch", "--locked"], cwd=REPO, env=env, capture_output=True, text=True)
    case.assertEqual(0, fetch.returncode, fetch.stderr)
    # The fallback samples need the pinned parser: install that package so
    # the denied run resolves it from uv's cache alone.
    # The pin is read, and held to its one exact `package==version`, by the
    # fallback's own runner, the one place that parses it. A checkout without
    # the fallback (the recovery suite's synthetic root) has no parser to warm.
    if (REPO / "tools/surface-census/golden-reach-search.py").is_file():
        pin = subprocess.run(
            ["bash", "tests/census_fallback/run.sh", "pin", "tools/surface-census/golden-reach-search.py"],
            cwd=REPO,
            env=env,
            capture_output=True,
            text=True,
        )
        case.assertEqual(0, pin.returncode, pin.stderr)
        warm = subprocess.run(
            ["uv", "run", "--no-project", "--with", pin.stdout.strip(), "python3", "-c", ""],
            cwd=REPO,
            env=env,
            capture_output=True,
            text=True,
        )
        case.assertEqual(0, warm.returncode, warm.stderr)


def denied(*command: str, env: Mapping[str, str]) -> subprocess.CompletedProcess[str]:
    """`command` with sockets denied, from the repository root."""
    argv = [sys.executable, str(Path(__file__).resolve()), "--deny-network", *command]
    return subprocess.run(argv, cwd=REPO, env=env, capture_output=True, text=True)


def denied_cargo_test(env: Mapping[str, str]) -> subprocess.CompletedProcess[str]:
    """The proof's build: the e2e suite, compiled and linked, with sockets denied."""
    return denied(*CARGO_TEST, "--message-format=json", env=env)


def assert_unwarmed_refusal(case: unittest.TestCase, env: Mapping[str, str]) -> None:
    """The control: from an unwarmed registry, the same command reaches for the network."""
    unwarmed = denied_cargo_test(env)
    case.assertNotEqual(0, unwarmed.returncode, unwarmed.stderr)
    case.assertIn("crates.io", unwarmed.stderr)


def crozier_artifacts(stdout: str) -> dict[str, bool]:
    """Each crozier or e2e artifact file a JSON-message build reports -> whether cargo compiled it."""
    artifacts: dict[str, bool] = {}
    for line in stdout.splitlines():
        message = json.loads(line) if line.startswith("{") else {}
        if message.get("reason") == "compiler-artifact" and message["target"]["name"] in {"crozier", "e2e"}:
            for path in [*message["filenames"], *filter(None, [message.get("executable")])]:
                if not path.endswith(".rmeta") or Path(path).is_file():
                    artifacts[path] = not message["fresh"]
    return artifacts


def digests(paths: Iterable[str]) -> dict[str, str]:
    return {path: hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in paths}


def handoff_record() -> Path:
    target = os.environ.get("CARGO_TARGET_DIR")
    return (Path(target) if target else REPO / "target") / "cold-registry-handoff.json"


def denied_handoff_build() -> tuple[dict[str, bool], str]:
    """The suite and the binary from this job's CARGO_HOME, sockets denied: what each compiled, or why it failed."""
    env = {**os.environ, "RUSTC_WRAPPER": ""}
    artifacts: dict[str, bool] = {}
    for command in (CARGO_TEST, CARGO_BIN):
        run = denied(*command, "--message-format=json", env=env)
        if run.returncode != 0:
            return artifacts, run.stderr
        # The second command sees what the first just compiled as fresh: compiled by either is compiled.
        for path, compiled in crozier_artifacts(run.stdout).items():
            artifacts[path] = artifacts.get(path, False) or compiled
    return artifacts, ""


def record_handoff(artifacts: Iterable[str]) -> None:
    """Name exactly the bytes a denied build left, for this CARGO_HOME, for later steps to be held to."""
    record = {"cargo_home": os.environ["CARGO_HOME"], "artifacts": digests(artifacts)}
    handoff_record().parent.mkdir(parents=True, exist_ok=True)
    handoff_record().write_text(json.dumps(record, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def handoff_answers(case: unittest.TestCase) -> bool:
    """Whether the build this job's later steps use came from the cold registry with sockets denied.

    Cargo decides what is current, and each current artifact needs its own provenance:
    one compiled in this denied run has it, and one reused must be the bytes the record
    names. A single reused artifact outside the record came from a build with sockets up,
    whatever else was rebuilt beside it, so the caller proves it from a cold registry
    itself and the record stands unchanged.
    """
    if not handoff_record().is_file() or HANDOFF_ENV not in os.environ:
        return False
    record = json.loads(handoff_record().read_text(encoding="utf-8"))
    if record["cargo_home"] != os.environ.get("CARGO_HOME"):
        return False
    artifacts, failure = denied_handoff_build()
    case.assertEqual("", failure, "the job's build needed the network once its registry was warmed")
    rebuilt = [path for path, compiled in artifacts.items() if compiled]
    reused = digests(path for path, compiled in artifacts.items() if not compiled)
    unproven = sorted(path for path, digest in reused.items() if record["artifacts"].get(path) != digest)
    if unproven:
        names = ", ".join(Path(path).name for path in unproven)
        print(
            f"cold-registry: rejected the handoff; {len(rebuilt)} artifact(s) rebuilt with sockets denied, "
            f"but these reused ones were not made that way: {names}",
            file=sys.stderr,
        )
        return False
    if rebuilt:
        record_handoff(artifacts)
        print("cold-registry: rebuilt a changed input with sockets denied", file=sys.stderr)
        return True
    print("cold-registry: the job's build is the one made with sockets denied", file=sys.stderr)
    return True


def cold_registry_build() -> int:
    """The first dev build of a job that asks for the handoff; every other caller only builds the binary.

    `CARGO_HOME` stays the job's, because cargo fingerprints a crate's absolute source
    path: only a later step under this same path can reuse what this builds.
    """
    home = os.environ.get("CARGO_HOME")
    if HANDOFF_ENV in os.environ and not handoff_record().is_file():
        if not home:
            print(f"cold-registry: {HANDOFF_ENV} needs CARGO_HOME; set both on the job's step", file=sys.stderr)
            return 2
        if (Path(home) / "registry" / "src").exists():
            print(
                f"cold-registry: {home} already holds crates; point CARGO_HOME at an empty directory", file=sys.stderr
            )
            return 2
        case = unittest.TestCase()
        env = {**os.environ, "RUSTC_WRAPPER": ""}
        assert_unwarmed_refusal(case, env)
        warm_dependencies(case, env)
        artifacts, failure = denied_handoff_build()
        if failure:
            print(
                f"cold-registry: the build needed the network once its registry was warmed:\n{failure}", file=sys.stderr
            )
            return 1
        record_handoff(artifacts)
        return 0
    return subprocess.run(CARGO_BIN, cwd=REPO, check=False).returncode


@unittest.skipUnless(
    sys.platform == "linux" and platform.machine() in {"x86_64", "aarch64"}, "network-denial proof uses Linux seccomp"
)
class OfflineCorpusRecipes(unittest.TestCase):
    def test_warmed_build_needs_no_network_from_a_cold_registry(self) -> None:
        # CI's runner starts with no crates cached; a denied recipe then failed
        # resolving static.crates.io. Reproduce that cold registry here.
        if handoff_answers(self):
            return
        # No build of the job's came from a cold registry, so this one does it, in
        # its own target directory: another CARGO_HOME's build replaces the
        # fingerprints the job's normal builds use.
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as cold:
            env = {
                **os.environ,
                "CARGO_HOME": cold,
                "CARGO_TARGET_DIR": str(Path(cold) / "target"),
                "RUSTC_WRAPPER": "",
            }
            assert_unwarmed_refusal(self, env)
            warm_dependencies(self, env)
            build = denied_cargo_test(env)
            self.assertEqual(0, build.returncode, build.stderr)
            self.assertNotIn("Downloading", build.stderr)

    def test_real_recipes_without_network_or_cache(self) -> None:
        # The registered corpus cache, and the cache the census-fallback samples
        # were once fetched into: neither may exist or come back.
        caches = (REPO / ".local/corpus", REPO / ".local/census-fallback-sample")
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as directory:
            hidden = [Path(directory) / f"cache-{index}" for index in range(len(caches))]
            held = [cache.exists() for cache in caches]
            for cache, aside, present in zip(caches, hidden, held, strict=False):
                if present:
                    cache.rename(aside)
            try:
                self.assertFalse(any(cache.exists() for cache in caches))
                probe = subprocess.run(
                    [
                        sys.executable,
                        str(Path(__file__).resolve()),
                        "--deny-network",
                        sys.executable,
                        "-c",
                        "import socket; socket.socket()",
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(0, probe.returncode)
                self.assertIn("Operation not permitted", probe.stderr)
                warm_dependencies(self, os.environ)
                for recipe in offline_recipes():
                    with self.subTest(recipe=" ".join(recipe)):
                        result = subprocess.run(
                            [sys.executable, str(Path(__file__).resolve()), "--deny-network", "just", *recipe],
                            cwd=REPO,
                            capture_output=True,
                            text=True,
                            # A user-level sccache daemon needs a socket; the repo
                            # build contract has no wrapper and works offline.
                            # A replayed cache entry would prove nothing about the
                            # network, so each recipe's target really runs; and Nx
                            # loads its plugins in-process, since an isolated plugin
                            # worker reaches Nx over a socket the filter denies.
                            env={
                                **os.environ,
                                "RUSTC_WRAPPER": "",
                                "UV_OFFLINE": "1",
                                "NX_SKIP_NX_CACHE": "true",
                                "NX_ISOLATE_PLUGINS": "false",
                            },
                        )
                        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                        for cache in caches:
                            self.assertFalse(cache.exists(), f"recipe recreated {cache.relative_to(REPO)}")
            finally:
                # A failing recipe can create a new cache. Move that test output
                # aside before restoring the caller's original directories.
                for index, (cache, aside, present) in enumerate(zip(caches, hidden, held, strict=False)):
                    if cache.exists():
                        cache.rename(Path(directory) / f"unexpected-cache-{index}")
                    if present:
                        aside.rename(cache)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--deny-network":
        deny_network()
        os.execvp(sys.argv[2], sys.argv[2:])
    if len(sys.argv) > 1 and sys.argv[1] == "--cold-registry-build":
        (REPO / ".local").mkdir(exist_ok=True)
        sys.exit(cold_registry_build())
    (REPO / ".local").mkdir(exist_ok=True)
    unittest.main()
