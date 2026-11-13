# llmlint: ignore-file[shell_test_tiers_stay_split] Only `git init` beside the suite's other offline cases: every lane carries git, and it reaches no network.
"""`capture-visual-docs.sh` from a real git checkout up to the container's boundary: `docker` is
a recorder of its arguments, so the mounts, the inner program handed to it and the failure message
are the script's own. The lint lane really runs the capture on every pull request."""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "screenshots" / "capture-visual-docs.sh"

pytestmark = pytest.mark.skipif(os.name == "nt", reason="the capture runs on the Linux lint lane")


@pytest.fixture
def checkout(tmp_path: Path) -> Path:
    root = tmp_path / "checkout"
    root.mkdir()
    (root / "rust-toolchain.toml").write_text('[toolchain]\nchannel = "1.96.0"\n', encoding="utf-8")
    subprocess.run(["git", "init", "--quiet"], cwd=root, check=True)
    return root


def docker(tmp_path: Path, exit_status: int) -> tuple[dict[str, str], Path]:
    """A `docker` that records its arguments, then exits with `exit_status`."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    record = tmp_path / "docker-args"
    stub = bin_dir / "docker"
    stub.write_text(f'#!/bin/sh\nprintf "%s\\n" "$@" > "{record}"\nexit {exit_status}\n', encoding="utf-8")
    stub.chmod(stub.stat().st_mode | stat.S_IEXEC)
    return {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}, record


def run(root: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["bash", str(SCRIPT)], cwd=root, env=env, capture_output=True, text=True, check=False)


def test_it_pins_the_toolchain_mounts_the_checkout_and_keeps_the_build_off_the_host(
    checkout: Path, tmp_path: Path
) -> None:
    env, record = docker(tmp_path, 0)
    result = run(checkout, env)
    assert result.returncode == 0, result.stderr
    arguments = record.read_text(encoding="utf-8")
    assert "rust:1.96.0-bookworm" in arguments
    assert f"{checkout}:/work" in arguments
    assert "crozier-visual-docs-target:/work/target" in arguments
    assert f"{checkout / '.git'}:{checkout / '.git'}:ro" in arguments
    assert "RUSTUP_TOOLCHAIN=1.96.0" in arguments
    for tree in ("shots/current/x86_64", "shots/verify/x86_64"):
        assert f"capture {tree}" in arguments
    assert 'chown -R "$HOST_OWNER" shots docs/screenshots' in arguments
    # Both pinned tools come through the retrying download, never a single curl attempt.
    assert 'bash screenshots/fetch-tool.sh "https://github.com/charmbracelet/freeze/releases/download/' in arguments
    assert 'bash screenshots/fetch-tool.sh "https://github.com/astral-sh/ruff/releases/download/' in arguments
    assert "curl " not in arguments


def test_outside_a_checkout_it_says_so_before_any_container(tmp_path: Path) -> None:
    bare = tmp_path / "plain"
    bare.mkdir()
    (bare / "rust-toolchain.toml").write_text('channel = "1.96.0"\n', encoding="utf-8")
    env, record = docker(tmp_path, 0)
    result = run(bare, {**env, "GIT_CEILING_DIRECTORIES": str(tmp_path)})
    assert result.returncode == 2
    assert "not a git checkout" in result.stderr
    assert not record.exists()


def test_a_failed_capture_exits_with_its_status_and_says_what_to_do(checkout: Path, tmp_path: Path) -> None:
    env, _ = docker(tmp_path, 7)
    result = run(checkout, env)
    assert result.returncode == 7
    assert "capture-visual-docs: the capture failed (status 7" in result.stderr
    assert "run ./screenshots/capture-visual-docs.sh locally" in result.stderr


def test_it_refuses_to_run_outside_the_repository_root(tmp_path: Path) -> None:
    empty = tmp_path / "elsewhere"
    empty.mkdir()
    (empty / "rust-toolchain.toml").write_text("[toolchain]\n", encoding="utf-8")
    env, record = docker(tmp_path, 0)
    result = run(empty, env)
    assert result.returncode == 2
    assert "no channel in rust-toolchain.toml" in result.stderr
    assert not record.exists(), "no container starts without a toolchain"
