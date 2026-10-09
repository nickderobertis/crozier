"""The runner's own failure paths: the real run.sh, with the real cargo, node,
ruff and uv, failing genuinely — a build into a target directory that is a
regular file, a venv path under one, and an install with no network and no
cache."""
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


def test_a_build_that_fails_keeps_cargos_error_and_names_the_repair(tmp_path):
    blocker = tmp_path / "not-a-directory"
    blocker.write_text("", encoding="utf-8")
    done = _run(tmp_path / "venv", CARGO_TARGET_DIR=str(blocker))
    assert done.returncode == 1, done.stderr
    assert "failed to create directory" in done.stderr
    assert "live-e2e: building the release crozier failed (cargo's error is above)" in done.stderr
    assert not (tmp_path / "venv").exists(), "the runner went on past a failed build"


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
