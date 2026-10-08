"""The runner's own failure paths: run.sh, copied into a scratch checkout, with
the tools it starts stubbed on PATH so the venv step fails the way a full disk or
an unreachable PyPI makes it fail."""
import os
import shutil
import subprocess
from pathlib import Path

import pytest

RUNNER = Path(__file__).resolve().with_name("run.sh")


def _stub(bin_dir: Path, name: str, body: str) -> None:
    path = bin_dir / name
    path.write_text(f"#!/bin/sh\n{body}\n", encoding="utf-8")
    path.chmod(0o755)


def _run(tmp_path: Path, uv_body: str) -> subprocess.CompletedProcess:
    checkout = tmp_path / "checkout"
    (checkout / "tests" / "live_e2e").mkdir(parents=True)
    shutil.copy(RUNNER, checkout / "tests" / "live_e2e" / "run.sh")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    for tool in ("cargo", "node", "ruff"):
        _stub(bin_dir, tool, "exit 0")
    _stub(bin_dir, "uv", uv_body)
    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
    return subprocess.run(
        ["bash", str(checkout / "tests" / "live_e2e" / "run.sh")],
        capture_output=True, text=True, env=env, timeout=60,
    )


@pytest.mark.skipif(os.name == "nt", reason="run.sh is the Linux/macOS runner")
def test_a_venv_that_cannot_be_created_names_the_directory_and_the_repair(tmp_path):
    done = _run(tmp_path, 'echo "error: No space left on device" >&2; exit 2')
    assert done.returncode == 1, done.stderr
    assert "live-e2e: could not create the test venv at" in done.stderr
    assert ".crozier-tmp/live-e2e-venv" in done.stderr
    assert "then re-run" in done.stderr


@pytest.mark.skipif(os.name == "nt", reason="run.sh is the Linux/macOS runner")
def test_an_install_that_fails_names_the_packages_and_the_retry(tmp_path):
    done = _run(tmp_path, '[ "$1" = venv ] && exit 0; echo "error: Failed to fetch" >&2; exit 2')
    assert done.returncode == 1, done.stderr
    assert "live-e2e: could not install httpx, pydantic, pytest and pyyaml" in done.stderr
    assert "check that PyPI is reachable" in done.stderr
