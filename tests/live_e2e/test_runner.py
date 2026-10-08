"""The runner's own failure paths: the real run.sh, with the real cargo, node,
ruff and uv, pointed at a scratch venv whose creation or install genuinely fails —
a venv path under a regular file, and an install with no network and no cache."""
import os
import subprocess
from pathlib import Path

import pytest

RUNNER = Path(__file__).resolve().with_name("run.sh")
pytestmark = pytest.mark.skipif(os.name == "nt", reason="run.sh is the Linux/macOS runner")


def _run(venv: Path, **env: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", str(RUNNER)],
        capture_output=True, text=True, timeout=1800,
        env={**os.environ, "CROZIER_LIVE_E2E_VENV": str(venv), **env},
    )


def test_a_venv_that_cannot_be_created_names_the_directory_and_the_repair(tmp_path):
    blocker = tmp_path / "not-a-directory"
    blocker.write_text("", encoding="utf-8")
    venv = blocker / "venv"
    done = _run(venv)
    assert done.returncode == 1, done.stderr
    assert f"live-e2e: could not create the test venv at {venv}" in done.stderr
    assert f"rm -rf '{venv}'" in done.stderr


def test_an_install_that_fails_names_the_packages_and_the_retry(tmp_path):
    venv = tmp_path / "venv"
    done = _run(venv, UV_OFFLINE="1", UV_NO_CACHE="1")
    assert done.returncode == 1, done.stderr
    assert (venv / "bin" / "python").exists(), done.stderr
    assert f"live-e2e: could not install httpx, pydantic, pytest and pyyaml into {venv}" in done.stderr
    assert "check that PyPI is reachable" in done.stderr
