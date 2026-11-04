"""The base `just census-repin` steps from, found the way the verb finds it.

Each case runs the real verb (`census-repin.py --base-only`, which prints the base
a repin would use and why) over a real scratch git history, with GitHub's
artifact API served from a loopback server behind the real
`tools/witness-search/rate_limit_guard.py`. The served base is a real
`base.json.gz` inside a real artifact zip, and the host cache is a scratch
directory (`CROZIER_GOLDEN_REACH_BASE_CACHE`).
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import zipfile
from collections import Counter
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, ClassVar

import pytest

REPO = Path(__file__).resolve().parents[3]
HERE = REPO / "tools" / "surface-census"
VERB = HERE / "census-repin.py"
SLUG = "owner/crozier"


def _load(name: str, file: str) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RS = _load("reach_store", "reach_store.py")


class GitHub(BaseHTTPRequestHandler):
    """GitHub's REST artifact API for one repository, as the guard and the lookup call it."""

    artifacts: ClassVar[dict[str, bytes]] = {}
    expired: ClassVar[set[str]] = set()
    extra: ClassVar[list[object]] = []
    mode: ClassVar[str] = "ok"
    used: ClassVar[int] = 0
    calls: ClassVar[Counter[str]] = Counter()

    def log_message(self, format: str, *args: object) -> None:
        return

    def _send(self, status: int, body: bytes, kind: str = "application/json") -> None:
        self.send_response(status)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/rate_limit":
            reset = int(time.time()) + 3600
            core = {"limit": 5000, "used": self.used, "remaining": 5000 - self.used, "reset": reset}
            self._send(200, json.dumps({"resources": {"core": core}}).encode())
            return
        type(self).calls[path] += 1
        if path.startswith("/blob/"):
            # Blob storage takes the redirect's own signed URL, never the API token.
            self._send(200, self.artifacts[sorted(self.artifacts)[int(path[len("/blob/") :]) - 1]], "application/zip")
            return
        if self.headers.get("Authorization") != "Bearer offline-token" or self.mode == "refused":
            self._send(401, b'{"message": "Bad credentials"}')
            return
        if path == f"/repos/{SLUG}/actions/artifacts":
            if self.mode == "missing":
                self._send(404, b'{"message": "Not Found"}')
                return
            if self.mode == "not-an-array":
                self._send(200, b'{"artifacts": {"id": 1}}')
                return
            listed: list[object] = [
                {"id": index, "name": f"golden-reach-base-{sha}", "expired": sha in self.expired}
                for index, sha in enumerate(sorted(self.artifacts), start=1)
            ]
            listed += self.extra
            self._send(200, json.dumps({"total_count": len(listed), "artifacts": listed}).encode())
            return
        prefix = f"/repos/{SLUG}/actions/artifacts/"
        if path.startswith(prefix) and path.endswith("/zip") and self.mode in ("redirect", "redirect-away"):
            # GitHub answers an artifact download with a redirect to its blob storage.
            index = path[len(prefix) : -len("/zip")]
            host, port = self.headers["Host"].rsplit(":", 1)
            here = f"http://{host}:{port}"
            target = f"{here}/blob/{index}" if self.mode == "redirect" else f"http://storage.example.invalid/{index}"
            self.send_response(302)
            self.send_header("Location", target)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if path.startswith(prefix) and path.endswith("/zip"):
            if self.mode == "download-fails":
                self._send(500, b'{"message": "Server Error"}')
                return
            index = int(path[len(prefix) : -len("/zip")])
            self._send(200, self.artifacts[sorted(self.artifacts)[index - 1]], "application/zip")
            return
        self._send(404, b"{}")


@pytest.fixture
def github() -> Iterator[str]:
    GitHub.artifacts, GitHub.mode, GitHub.used, GitHub.expired, GitHub.extra = {}, "ok", 0, set(), []
    GitHub.calls = Counter()
    server = ThreadingHTTPServer(("127.0.0.1", 0), GitHub)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
    server.server_close()


def store(commit: str, **top: object) -> dict:
    return {
        "schema": 1,
        "commit": commit,
        "rustc": "1.96.0 abc",
        "llvm": "22.1.2",
        "full_at": commit,
        "steps_since_full": 0,
        "measured_at": RS.now_iso(),
        "tests": {},
        "fixtures": {},
        "functions": {},
        **top,
    }


def artifact(base: dict, tmp: Path) -> bytes:
    path = tmp / f"{base['commit']}.json.gz"
    RS.save(base, path)
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.write(path, "base.json.gz")
    return buffer.getvalue()


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture
def history(tmp_path: Path) -> tuple[Path, list[str]]:
    """A first-parent history c1..c4 (HEAD c4), with a side branch merged in at c3."""
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-q", "-b", "main")
    commits = []
    for index in range(1, 5):
        if index == 3:
            git(root, "checkout", "-q", "-b", "side")
            (root / "side.txt").write_text("side\n", encoding="utf-8")
            git(root, "add", "-A")
            git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "side")
            git(root, "checkout", "-q", "main")
            git(root, "-c", "user.name=t", "-c", "user.email=t@t", "merge", "-q", "--no-ff", "-m", "c3", "side")
        else:
            (root / "file.txt").write_text(f"{index}\n", encoding="utf-8")
            git(root, "add", "-A")
            git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", f"c{index}")
        commits.append(git(root, "rev-parse", "HEAD"))
    git(root, "remote", "add", "origin", f"https://github.com/{SLUG}.git")
    git(root, "update-ref", "refs/remotes/origin/main", commits[-1])
    return root, commits


def lookup(
    root: Path,
    cache: Path,
    api: str,
    *,
    token: str | None = "offline-token",
    extra: dict[str, str] | None = None,
    gh_token: str | None = None,
) -> subprocess.CompletedProcess:
    """`census-repin --base-only` over `root`. With no `token`, isolate the gh login from the host; a
    stand-in `gh` prints `gh_token` for `gh auth token` when one is given."""
    env = {
        key: value for key, value in os.environ.items() if key not in ("GITHUB_TOKEN", "GH_TOKEN", "GITHUB_REPOSITORY")
    }
    env |= {"CROZIER_GITHUB_API_URL": api, "CROZIER_GOLDEN_REACH_BASE_CACHE": str(cache)} | (extra or {})
    if token is not None:
        env["GITHUB_TOKEN"] = token
    elif gh_token is not None:
        tools = cache.parent / "bin"
        tools.mkdir(exist_ok=True)
        if not (tools / "git").exists():
            (tools / "git").symlink_to(shutil.which("git") or "/usr/bin/git")
        (tools / "gh").write_text(f'#!/bin/sh\n[ "$1 $2" = "auth token" ] && echo {gh_token}\n', encoding="utf-8")
        (tools / "gh").chmod(0o755)
        env["PATH"] = str(tools)
    else:
        env["GH_CONFIG_DIR"] = str(cache.parent / "empty-gh-config")
    run = subprocess.run(
        [sys.executable, str(VERB), "--repo-root", str(root), "--base-only"],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    assert run.returncode == 0, run.stderr
    return run


def cached(cache: Path, commit: str) -> Path:
    path = cache / commit / "base.json.gz"
    RS.save(store(commit), path)
    return path


def test_the_nearest_first_parent_ancestor_with_an_artifact_is_chosen_and_cached(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (c1, _c2, c3, c4) = history
    cache = tmp_path / "cache"
    side = git(root, "rev-parse", "side")
    # c4 has no artifact of its own; its parent c3 has; c1 is farther; the merged
    # side commit is no first-parent ancestor, so its artifact is never taken.
    GitHub.artifacts = {sha: artifact(store(sha), tmp_path) for sha in (c1, c3, side)}
    run = lookup(root, cache, github)
    assert f"census-repin: base {c3} (artifact): downloaded golden-reach-base-{c3}" in run.stdout
    assert RS.load(cache / c3 / "base.json.gz")["commit"] == c3
    download = f"/repos/{SLUG}/actions/artifacts/{sorted(GitHub.artifacts).index(c3) + 1}/zip"
    assert GitHub.calls == Counter({f"/repos/{SLUG}/actions/artifacts": 1, download: 1}), "one list call, one download"


def test_a_cached_base_is_used_without_a_request_when_no_nearer_ancestor_was_published(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (_c1, c2, c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c3)
    git(root, "update-ref", "refs/remotes/origin/main", c2)  # c4 is a local commit no CI run published
    GitHub.artifacts = {c3: artifact(store(c3), tmp_path)}
    run = lookup(root, cache, github)
    assert (
        f"base {c3} (cache): the cached base at {c3[:12]}, with no nearer ancestor CI could have published"
        in run.stdout
    )
    assert GitHub.calls == Counter(), "a cached base nothing nearer could beat costs no request"


@pytest.mark.parametrize(
    ("mode", "token", "reason"),
    [
        ("missing", "offline-token", "listing artifacts answered HTTP 404"),
        ("refused", "offline-token", "GitHub refused the token from GITHUB_TOKEN (HTTP 401)"),
        ("ok", None, "no GITHUB_TOKEN or GH_TOKEN is set"),
        ("busy", "offline-token", "the rate-limit guard would wait"),
    ],
    ids=["artifact list 404", "refused token", "no token", "guard would wait"],
)
@pytest.mark.parametrize("with_cache", [True, False], ids=["cached fallback", "full fallback"])
def test_a_failed_lookup_falls_back_to_the_nearest_cached_base_or_to_a_full_measurement(
    history: tuple[Path, list[str]],
    github: str,
    tmp_path: Path,
    mode: str,
    token: str | None,
    reason: str,
    with_cache: bool,
) -> None:
    root, (c1, _c2, c3, _c4) = history
    cache = tmp_path / "cache"
    if with_cache:
        cached(cache, c1)
    GitHub.artifacts = {c3: artifact(store(c3), tmp_path)}
    GitHub.mode = "ok" if mode == "busy" else mode
    GitHub.used = 4000 if mode == "busy" else 0
    run = lookup(root, cache, github, token=token)
    assert reason in run.stdout
    if with_cache:
        assert f"census-repin: base {c1} (cache):" in run.stdout and f"using the cached base at {c1[:12]}" in run.stdout
    else:
        assert "census-repin: base none (none):" in run.stdout and "no cached base either" in run.stdout
    assert not (cache / c3).exists(), "nothing was downloaded"


def test_a_downloaded_base_recording_another_commit_is_refused(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (c1, c2, c3, _c4) = history
    GitHub.artifacts = {c3: artifact(store(c2), tmp_path)}
    run = lookup(root, tmp_path / "cache", github)
    assert f"refused golden-reach-base-{c3}: it records commit {c2}" in run.stdout
    assert "base none (none)" in run.stdout
    assert c1  # the history has an older commit the refused base could not stand in for


def test_a_downloaded_base_of_another_schema_is_refused(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (_c1, _c2, c3, _c4) = history
    path = tmp_path / "schema2.json.gz"
    import gzip

    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump({**store(c3), "schema": 2}, handle)
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.write(path, "base.json.gz")
    GitHub.artifacts = {c3: buffer.getvalue()}
    run = lookup(root, tmp_path / "cache", github)
    assert f"refused golden-reach-base-{c3}:" in run.stdout and "schema 2" in run.stdout


@pytest.mark.parametrize(
    ("case", "reason"),
    [
        ("download-fails", "downloading golden-reach-base-{c3} answered HTTP 500"),
        ("no-member", "golden-reach-base-{c3} holds no readable base.json.gz"),
    ],
    ids=["download answers 500", "zip without base.json.gz"],
)
def test_a_failed_download_falls_back_to_the_nearest_cached_base(
    history: tuple[Path, list[str]], github: str, tmp_path: Path, case: str, reason: str
) -> None:
    root, (c1, _c2, c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c1)
    if case == "no-member":
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("other.txt", "not a base")
        GitHub.artifacts = {c3: buffer.getvalue()}
    else:
        GitHub.artifacts = {c3: artifact(store(c3), tmp_path)}
        GitHub.mode = case
    run = lookup(root, cache, github)
    assert reason.format(c3=c3) in run.stdout
    assert f"census-repin: base {c1} (cache):" in run.stdout and f"using the cached base at {c1[:12]}" in run.stdout
    assert not (cache / c3).exists()


@pytest.mark.parametrize(
    ("case", "reason"),
    [("not gzip", "is not a gzip-compressed JSON store"), ("another commit", "it records commit")],
    ids=["a corrupt cached base", "a cached base recording another commit"],
)
def test_a_refused_cached_base_is_skipped_for_the_next_one_down(
    history: tuple[Path, list[str]], github: str, tmp_path: Path, case: str, reason: str
) -> None:
    root, (c1, c2, c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c1)
    nearest = cache / c3 / "base.json.gz"
    nearest.parent.mkdir(parents=True)
    if case == "not gzip":
        nearest.write_text("not a store", encoding="utf-8")
    else:
        RS.save(store(c2), nearest)
    git(root, "update-ref", "refs/remotes/origin/main", c1)  # no nearer ancestor CI published: no request
    run = lookup(root, cache, github)
    assert f"refused the cached base {nearest}" in run.stdout and reason in run.stdout
    assert f"census-repin: base {c1} (cache):" in run.stdout
    assert GitHub.calls == Counter()


def test_an_artifact_list_that_is_not_an_array_falls_back_with_its_reason(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (c1, _c2, _c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c1)
    GitHub.mode = "not-an-array"
    run = lookup(root, cache, github)
    assert "the artifact list was not JSON with an `artifacts` array" in run.stdout
    assert f"census-repin: base {c1} (cache):" in run.stdout


def test_an_expired_or_malformed_artifact_record_is_passed_over_for_the_next_ancestor(
    history: tuple[Path, list[str]], github: str, tmp_path: Path
) -> None:
    root, (_c1, c2, c3, _c4) = history
    GitHub.artifacts = {sha: artifact(store(sha), tmp_path) for sha in (c2, c3)}
    GitHub.expired = {c3}
    GitHub.extra = [
        "not a record",
        {"name": "golden-reach-base-not-a-sha", "id": 9},
        {"name": f"golden-reach-base-{c3}", "id": "9"},
    ]
    run = lookup(root, tmp_path / "cache", github)
    assert f"census-repin: base {c2} (artifact): downloaded golden-reach-base-{c2}" in run.stdout


@pytest.mark.parametrize(
    ("case", "token", "extra", "gh_token", "base"),
    [
        ("GH_TOKEN alone", None, {"GH_TOKEN": "offline-token"}, None, "c3"),
        ("gh auth token when neither variable is set", None, {}, "offline-token", "c3"),
        ("GITHUB_TOKEN before GH_TOKEN", "a-refused-token", {"GH_TOKEN": "offline-token"}, None, "c1"),
    ],
    ids=["GH_TOKEN", "gh auth token", "GITHUB_TOKEN wins"],
)
@pytest.mark.skipif(sys.platform == "win32", reason="the stand-in `gh` is a shell script")
def test_the_lookup_authenticates_with_each_credential_in_order(
    history: tuple[Path, list[str]],
    github: str,
    tmp_path: Path,
    case: str,
    token: str | None,
    extra: dict[str, str],
    gh_token: str | None,
    base: str,
) -> None:
    root, (c1, _c2, c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c1)
    GitHub.artifacts = {c3: artifact(store(c3), tmp_path)}
    run = lookup(root, cache, github, token=token, extra=extra, gh_token=gh_token)
    expected = {"c1": c1, "c3": c3}[base]
    assert f"census-repin: base {expected} " in run.stdout, (case, run.stdout)
    if base == "c1":
        assert "GitHub refused the token from GITHUB_TOKEN (HTTP 401)" in run.stdout


@pytest.mark.parametrize(
    ("mode", "chosen"),
    [("redirect", "artifact"), ("redirect-away", "cache")],
    ids=["a redirect to artifact storage", "a redirect to a host the lookup refuses"],
)
def test_an_artifact_download_follows_only_the_redirects_it_allows(
    history: tuple[Path, list[str]], github: str, tmp_path: Path, mode: str, chosen: str
) -> None:
    root, (c1, _c2, c3, _c4) = history
    cache = tmp_path / "cache"
    cached(cache, c1)
    GitHub.artifacts = {c3: artifact(store(c3), tmp_path)}
    GitHub.mode = mode
    run = lookup(root, cache, github)
    if chosen == "artifact":
        assert f"census-repin: base {c3} (artifact): downloaded golden-reach-base-{c3}" in run.stdout
        assert GitHub.calls["/blob/1"] == 1
    else:
        assert f"downloading golden-reach-base-{c3} failed" in run.stdout and "redirect" in run.stdout
        assert f"census-repin: base {c1} (cache):" in run.stdout


def test_the_ci_jobs_packaged_base_is_found_by_the_verb_on_a_later_commit(
    history: tuple[Path, list[str]], github: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The job's own command (`golden-reach.py base --package`, which `just golden-reach-base` runs) packages
    `base.json.gz`; uploaded under the name `ci.yml` gives it, the verb at a child commit with no artifact of
    its own takes it. Only the instrumented measurement is stood in for: its stores are proven elsewhere."""
    root, (c1, _c2, c3, c4) = history
    workflow = (REPO / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    job = workflow.split("\n  golden-reach-base:\n", 1)[1].split("\n  gate:\n", 1)[0]
    assert 'run: just golden-reach-base "$RUNNER_TEMP/golden-reach-base"' in job
    assert "path: ${{ runner.temp }}/golden-reach-base/base.json.gz" in job
    assert "name: golden-reach-base-${{ github.sha }}" in job
    recipe = (REPO / "justfile").read_text(encoding="utf-8").split("\ngolden-reach-base dir:\n", 1)[1].split("\n\n")[0]
    assert recipe.strip() == "python3 tools/surface-census/golden-reach.py base --package {{dir}}"

    reach = _load("repin_base_golden_reach", "golden-reach.py")
    stepped_from: list[str | None] = []

    def measured(repo_root: Path, *, base: dict | None, full_reason: str, jobs: int) -> Any:
        """Return the real Step; the hyphenated CLI loaded by path has no importable annotation."""
        stepped_from.append(base["commit"] if base else None)
        head = git(repo_root, "rev-parse", "HEAD")
        return reach.Step(store(head, full_at=c1, steps_since_full=1), c1, None, (), (), (), (), {})

    monkeypatch.setattr(reach, "measure_step", measured)
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "xdg"))
    monkeypatch.setenv("CROZIER_GOLDEN_REACH_BASE_CACHE", str(tmp_path / "job-cache"))
    monkeypatch.setenv("CROZIER_GITHUB_API_URL", github)
    monkeypatch.setenv("GITHUB_TOKEN", "offline-token")
    monkeypatch.delenv("GITHUB_REPOSITORY", raising=False)
    GitHub.artifacts = {c1: artifact(store(c1), tmp_path)}
    git(root, "checkout", "-q", "--detach", c3)
    runner_temp = tmp_path / "runner-temp"
    assert reach.main(["--repo-root", str(root), "base", "--package", str(runner_temp / "golden-reach-base")]) == 0
    git(root, "checkout", "-q", "main")
    assert stepped_from == [c1], "the job measures from the nearest earlier published base"
    packaged = runner_temp / "golden-reach-base" / "base.json.gz"
    assert RS.load(packaged)["commit"] == c3

    # actions/upload-artifact zips the one file at its base name, under the name the job gives it.
    upload = io.BytesIO()
    with zipfile.ZipFile(upload, "w") as archive:
        archive.write(packaged, packaged.name)
    name = "golden-reach-base-${{ github.sha }}".replace("${{ github.sha }}", c3)
    assert name == f"golden-reach-base-{c3}"
    GitHub.artifacts, GitHub.calls = {c1: GitHub.artifacts[c1], c3: upload.getvalue()}, Counter()
    assert git(root, "rev-parse", "HEAD") == c4 and git(root, "rev-parse", "HEAD^") == c3
    cache = tmp_path / "cache"
    run = lookup(root, cache, github)
    assert f"census-repin: base {c3} (artifact): downloaded {name}" in run.stdout, run.stdout
    assert RS.load(cache / c3 / "base.json.gz") == RS.load(packaged), (
        "the verb steps from exactly what the job packaged"
    )
