"""At most one instrumented measurement runs on a host: every entry point waits for the lock.

The test holds the host-wide lock (`${XDG_CACHE_HOME}/crozier/instrumented-measurement.lock`,
with `XDG_CACHE_HOME` pointed at a scratch directory) and starts each supported
entry point that measures in turn — the `census-repin`, `golden-reach`,
`handwritten-reach` and `golden-reach-base` (CI's command) recipes, and the two
scripts' `measure` — over a real scratch clone of this repository. A `cargo` on
PATH records that it was called, so the case shows each entry point reports it is
waiting and starts no instrumented build until the lock is released, then starts
one.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import textwrap
import time
from collections.abc import Iterator
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[3]
OVERLAY = ("tools", "justfile", "scripts")

pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="the holder takes the lock with fcntl")


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture(scope="module")
def clone(tmp_path_factory: pytest.TempPathFactory) -> Iterator[Path]:
    """This repository's HEAD with the working tree's tooling committed on top, and no remote."""
    root = tmp_path_factory.mktemp("lock") / "repo"
    git(REPO, "clone", "-q", "--shared", str(REPO), str(root))
    for name in OVERLAY:
        source, target = REPO / name, root / name
        if source.is_dir():
            shutil.rmtree(target)
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        else:
            shutil.copy2(source, target)
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "tooling")
    git(root, "remote", "remove", "origin")
    yield root


ENTRY_POINTS = {
    "census-repin recipe": ["just", "census-repin"],
    "golden-reach recipe": ["just", "golden-reach"],
    "handwritten-reach recipe": ["just", "handwritten-reach"],
    "golden-reach.py measure": [sys.executable, "tools/surface-census/golden-reach.py", "measure"],
    "handwritten-fixtures.py measure": [sys.executable, "tools/surface-census/handwritten-fixtures.py", "measure"],
    "the base-publishing CI job's command": ["just", "golden-reach-base", "{package}"],
}


@pytest.mark.parametrize("entry", ENTRY_POINTS, ids=list(ENTRY_POINTS))
def test_an_entry_point_waits_for_the_lock_and_builds_only_once_it_is_released(
    clone: Path, tmp_path: Path, entry: str
) -> None:
    import fcntl

    marker = tmp_path / "cargo-called"
    shims = tmp_path / "bin"
    shims.mkdir()
    cargo = shims / "cargo"
    cargo.write_text(
        textwrap.dedent(
            f"""\
            #!/bin/sh
            echo "$@" >> {marker}
            echo "cargo stand-in: no build in this test" >&2
            exit 1
            """
        ),
        encoding="utf-8",
    )
    cargo.chmod(0o755)
    xdg = tmp_path / "xdg"
    lock = xdg / "crozier" / "instrumented-measurement.lock"
    lock.parent.mkdir(parents=True)
    env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN", "CI", "VIRTUAL_ENV")}
    env |= {
        "XDG_CACHE_HOME": str(xdg),
        "CROZIER_GOLDEN_REACH_BASE_CACHE": str(tmp_path / "bases"),
        "PATH": f"{shims}{os.pathsep}{env['PATH']}",
    }
    argv = [part.replace("{package}", str(tmp_path / "package")) for part in ENTRY_POINTS[entry]]
    with lock.open("a+") as held:
        fcntl.flock(held.fileno(), fcntl.LOCK_EX)
        process = subprocess.Popen(argv, cwd=clone, env=env, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        assert process.stderr is not None
        seen = []
        deadline = time.monotonic() + 600
        while time.monotonic() < deadline:
            line = process.stderr.readline()
            if not line and process.poll() is not None:
                break
            seen.append(line)
            if "waiting for the instrumented-measurement lock" in line:
                break
        assert any("waiting for the instrumented-measurement lock" in line for line in seen), "".join(seen)
        time.sleep(2)
        assert process.poll() is None, f"{entry} went on without the lock: {''.join(seen)}"
        assert not marker.exists(), f"{entry} started an instrumented build while another measurement held the lock"
        fcntl.flock(held.fileno(), fcntl.LOCK_UN)
    _out, err = process.communicate(timeout=600)
    assert marker.exists(), f"{entry} never started its build once the lock was free:\n{err[-2000:]}"
    assert "llvm-cov" in marker.read_text(encoding="utf-8")
    assert process.returncode != 0, "the cargo stand-in fails the build, so the entry point must report it"
