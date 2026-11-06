"""At most one instrumented measurement runs on a host: every entry point waits for the lock.

The test holds the host-wide lock (`${XDG_CACHE_HOME}/crozier/instrumented-measurement.lock`,
with `XDG_CACHE_HOME` pointed at a scratch directory) and starts each supported
entry point that measures, all at once — the `census-repin`, `golden-reach`,
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


def small_inputs(root: Path) -> None:
    """Keep lock coverage independent of the size of crozier's measured sources."""
    # This lock fixture replaces the measured crate with lock_target alone;
    # it carries no Python ports of that synthetic function.
    census = root / "tools/surface-census/openapi-surface-census.py"
    census.write_text(census.read_text(encoding="utf-8") + "\nPORT_PINS = ()\n", encoding="utf-8")
    shutil.rmtree(root / "src")
    (root / "src").mkdir()
    (root / "src/lib.rs").write_text("pub fn lock_target() -> u8 { 1 }\n", encoding="utf-8")
    (root / "src/main.rs").write_text("fn main() {}\n", encoding="utf-8")
    (root / "crates/crozier-e2e/tests/e2e.rs").write_text(
        "struct Corpus { api: &'static str }\n"
        'const LOCK: Corpus = Corpus {\n    api: "lock",\n};\n'
        "fn assert_committed_corpus_matches(_: &Corpus) { assert_eq!(crozier::lock_target(), 1); }\n"
        "#[test]\nfn lock_matches_fern_output() { assert_committed_corpus_matches(&LOCK); }\n",
        encoding="utf-8",
    )
    regions = root / "docs/openapi-surface"
    (regions / "golden-reach-sites.tsv").write_text(
        "key\tselectors\tsites\tnote\ntype\tschema.type\tsrc/lib.rs::lock_target\t\n", encoding="utf-8"
    )
    shutil.rmtree(regions / "handwritten")
    fixture = regions / "handwritten/lock-fixture"
    fixture.mkdir(parents=True)
    document = "openapi: 3.0.3\ninfo: {title: Lock fixture, version: '1'}\npaths: {}\n"
    (fixture / "openapi.yml").write_text(document, encoding="utf-8")
    (fixture / "evidence.toml").write_text(
        'fern_cli_version = "0.0.0"\n'  # certified-pair: stand-in; lock probe never generates an SDK
        'fern_python_sdk_version = "0.0.0"\n'  # certified-pair: stand-in; lock probe never generates an SDK
        f'digest = "{"0" * 64}"\n'
        'audiences = ["public"]\n[[covers]]\nkey = "type"\n'
        'arm = "src/lib.rs::lock_target"\nverdict = "config-gated"\n'
        'search = "docs/openapi-surface/golden-reach-witnesses/searches/type.md#configuration-gate"\n',
        encoding="utf-8",
    )
    golden = root / "tests/fixtures/lock"
    golden.mkdir()
    (golden / "openapi.yml").write_text(document, encoding="utf-8")


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
    small_inputs(root)
    # The six entry points share this fixture. Restate its synthetic ledger
    # before committing so repin's offline preflight leaves it clean for the others.
    subprocess.run(
        [
            sys.executable,
            "-c",
            "import runpy, sys; from pathlib import Path; "
            "sys.path.insert(0, 'tools/surface-census'); "
            "m = runpy.run_path('tools/surface-census/census-repin.py'); "
            "m['reach_document'].rewrite(Path.cwd(), m['REACH'], "
            "m['_load']('census_repin_handwritten', 'handwritten-fixtures.py'))",
        ],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
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


def _stand_in_cargo(shims: Path, marker: Path) -> None:
    shims.mkdir(parents=True)
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


def _wait_line(process: subprocess.Popen[str], deadline: float) -> list[str]:
    """Stderr up to the line saying the process waits for the lock (or to its exit)."""
    assert process.stderr is not None
    seen: list[str] = []
    while time.monotonic() < deadline:
        line = process.stderr.readline()
        if not line and process.poll() is not None:
            break
        seen.append(line)
        if "waiting for the instrumented-measurement lock" in line:
            break
    return seen


def test_every_entry_point_waits_for_the_lock_and_builds_only_once_it_is_released(clone: Path, tmp_path: Path) -> None:
    """All six start together against one held lock, so the case costs one entry point's wait, not six."""
    if sys.platform == "win32":
        pytest.skip("the holder takes the lock with fcntl")

    import fcntl

    xdg = tmp_path / "xdg"
    lock = xdg / "crozier" / "instrumented-measurement.lock"
    lock.parent.mkdir(parents=True)
    base_env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN", "CI", "VIRTUAL_ENV")}
    processes: dict[str, tuple[subprocess.Popen[str], Path]] = {}
    with lock.open("a+") as held:
        fcntl.flock(held.fileno(), fcntl.LOCK_EX)
        for index, (entry, command) in enumerate(ENTRY_POINTS.items()):
            scratch = tmp_path / f"entry-{index}"
            marker = scratch / "cargo-called"
            _stand_in_cargo(scratch / "bin", marker)
            env = base_env | {
                "XDG_CACHE_HOME": str(xdg),
                "CROZIER_GOLDEN_REACH_BASE_CACHE": str(scratch / "bases"),
                "PATH": f"{scratch / 'bin'}{os.pathsep}{base_env['PATH']}",
            }
            argv = [part.replace("{package}", str(scratch / "package")) for part in command]
            processes[entry] = (
                subprocess.Popen(argv, cwd=clone, env=env, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True),
                marker,
            )
        deadline = time.monotonic() + 600
        seen = {entry: _wait_line(process, deadline) for entry, (process, _marker) in processes.items()}
        time.sleep(2)
        for entry, (process, marker) in processes.items():
            said = "".join(seen[entry])
            assert "waiting for the instrumented-measurement lock" in said, f"{entry}: {said}"
            assert process.poll() is None, f"{entry} went on without the lock: {said}"
            assert not marker.exists(), f"{entry} started an instrumented build while another measurement held the lock"
        fcntl.flock(held.fileno(), fcntl.LOCK_UN)
    for entry, (process, marker) in processes.items():
        _out, err = process.communicate(timeout=600)
        assert marker.exists(), f"{entry} never started its build once the lock was free:\n{err[-2000:]}"
        assert "llvm-cov" in marker.read_text(encoding="utf-8"), entry
        assert process.returncode != 0, (
            f"{entry}: the cargo stand-in fails the build, so the entry point must report it"
        )
