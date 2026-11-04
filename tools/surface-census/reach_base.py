"""Find the saved golden-reach base a measurement steps from.

CI publishes one base per burst of pushes to `main`: the GitHub Actions artifact
``golden-reach-base-<40-hex sha>``, holding one ``base.json.gz`` (the store
``reach_store.py`` documents), kept 90 days. A consumer (``census-repin``,
``golden-reach.py measure --incremental``, and the CI job itself) takes the base
of the **nearest first-parent ancestor of HEAD that has one**:

1. It looks first in the host cache,
   ``${XDG_CACHE_HOME:-$HOME/.cache}/crozier/golden-reach-base/<sha>/base.json.gz``
   (``CROZIER_GOLDEN_REACH_BASE_CACHE`` overrides the directory), where every
   measurement on this host also leaves its own store.
2. It asks GitHub only when an ancestor nearer than the nearest cached base could
   carry an artifact — a commit on ``origin/main`` (or every commit when that ref
   is absent) — and then makes one artifact-list call and at most one download,
   both through ``tools/witness-search/rate_limit_guard.py``.
3. It authenticates with ``GITHUB_TOKEN`` or ``GH_TOKEN``, else with the token
   ``gh auth token`` prints from this host's ``gh`` login.
4. With no artifact, no token, a failed download, a refused or mismatched base,
   or a guard that would make the call wait, it uses the nearest cached base, and
   with none of those, the caller measures fully. ``Choice.reason`` says which
   happened and why.

The drift bound (``reach_store.MAX_AGE_DAYS``, ``reach_store.MAX_STEPS``) is the
caller's to apply, since it decides between an incremental and a full step.
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, NamedTuple, Protocol

if TYPE_CHECKING:
    from reach_store import Store

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
ARTIFACT_PREFIX = "golden-reach-base-"
ARTIFACT_FILE = "base.json.gz"
CACHE_ENV = "CROZIER_GOLDEN_REACH_BASE_CACHE"
ANCESTORS = 400
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")


def _load(name: str, path: Path) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"census-repin: cannot load {path}; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RS = _load("reach_store", HERE / "reach_store.py")


def _guard_module() -> Any:
    return _load("rate_limit_guard", REPO / "tools" / "witness-search" / "rate_limit_guard.py")


class Artifact(NamedTuple):
    """One `golden-reach-base-<sha>` record of GitHub's artifact list."""

    commit: str
    id: int
    expired: bool

    @classmethod
    def parse(cls, record: object) -> Artifact | None:
        """The record if it names a base artifact with an integer id, else None (any other artifact)."""
        if not isinstance(record, dict):
            return None
        name, ident, expired = record.get("name"), record.get("id"), record.get("expired", False)
        if not isinstance(name, str) or not name.startswith(ARTIFACT_PREFIX):
            return None
        commit = name[len(ARTIFACT_PREFIX) :]
        if not RS.SHA.fullmatch(commit) or type(ident) is not int or not isinstance(expired, bool):
            return None
        return cls(commit, ident, expired)


class Choice(NamedTuple):
    """The base a step starts from (None: measure fully), where it came from, and why."""

    store: Store | None
    commit: str | None
    source: Literal["cache", "artifact", "none"]
    reason: str


def cache_dir() -> Path:
    override = os.environ.get(CACHE_ENV)
    return Path(override) if override else RS.cache_root() / "golden-reach-base"


def cached_path(commit: str) -> Path:
    return cache_dir() / commit / ARTIFACT_FILE


def publish(store: Store) -> Path:
    """Leave `store` in the host cache under its own commit, for the next step on this host."""
    path = cached_path(store["commit"])
    RS.save(store, path)
    return path


def first_parent_ancestors(root: Path, head: str = "HEAD", limit: int = ANCESTORS) -> list[str]:
    """HEAD and its first-parent ancestors, nearest first."""
    return RS.git(root, "rev-list", "--first-parent", f"--max-count={limit}", head).split()


def _published_candidates(root: Path, commits: list[str]) -> list[str]:
    """The commits among `commits` that CI could have published a base for: those on `origin/main`."""
    have = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", "refs/remotes/origin/main"], cwd=root, capture_output=True
    )
    if have.returncode != 0:
        return commits
    return [
        commit
        for commit in commits
        if subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, "refs/remotes/origin/main"], cwd=root, capture_output=True
        ).returncode
        == 0
    ]


def _token() -> tuple[str | None, str]:
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(name):
            return os.environ[name], name
    if shutil.which("gh") is None:
        return None, "no GITHUB_TOKEN or GH_TOKEN is set and `gh` is not installed"
    run = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    token = run.stdout.strip()
    if run.returncode != 0 or not token:
        return None, "no GITHUB_TOKEN or GH_TOKEN is set and `gh auth token` printed none (run `gh auth login`)"
    return token, "`gh auth token`"


def repository(root: Path) -> str | None:
    """`owner/name` of the GitHub repository: `GITHUB_REPOSITORY`, else the `origin` remote."""
    named = os.environ.get("GITHUB_REPOSITORY")
    if named:
        # It is interpolated into an API path, so it is one `owner/name` and nothing else.
        return named if REPOSITORY.fullmatch(named) else None
    url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=root, capture_output=True, text=True).stdout
    found = re.search(r"github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?\s*$", url)
    slug = f"{found.group(1)}/{found.group(2)}" if found else None
    return slug if slug is not None and REPOSITORY.fullmatch(slug) else None


class Guard(Protocol):
    """The rate-limit guard's reservation interface, as `rate_limit_guard.RateLimitGuard` offers it."""

    def acquire(self, bucket: str, *, cost: int = 1) -> None: ...

    def record(self, response: object) -> None: ...


class _WouldWait(RuntimeError):
    """The guard would sleep before admitting the call."""


def _no_wait_guard() -> Guard:
    guard_module = _guard_module()

    class NoWaitGuard(guard_module.RateLimitGuard):
        def _sleep(self, duration: float, entry: dict[str, Any]) -> None:
            raise _WouldWait(f"the rate-limit guard would wait {duration:.0f}s ({entry.get('cause', 'floor')})")

    return NoWaitGuard("github")


def _allowed_redirect(url: str) -> bool:
    parts = urllib.parse.urlsplit(url)
    host = parts.hostname or ""
    if parts.scheme == "http" and host in ("127.0.0.1", "localhost", "::1"):
        return True
    # GitHub answers an artifact download with a redirect to its blob storage.
    return parts.scheme == "https" and (
        host == "api.github.com" or host.endswith((".githubusercontent.com", ".blob.core.windows.net"))
    )


def _call(guard: Guard, url: str, token: str, accept: str = "application/vnd.github+json") -> tuple[int, bytes]:
    """One GET through the guard: acquire, call, record. Returns the status and the body."""
    guard_module = _guard_module()
    request = urllib.request.Request(
        url,
        headers={
            "Accept": accept,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "crozier-census-repin",
            "Authorization": f"Bearer {token}",
        },
    )
    guard.acquire("core")
    try:
        # llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps this tooling stdlib-only and synchronous so it runs installless, and the rate-limit guard it reserves through is synchronous; a lookup makes at most two calls in sequence, which an async client would not speed up.
        response = guard_module.open_checked(request, _allowed_redirect, timeout=120)
    except urllib.error.HTTPError as error:
        body = error.read() if error.fp else b""
        guard.record(error)
        return error.code, body
    except BaseException as error:
        guard.record(error)
        raise
    try:
        with response:
            body = response.read()
    except BaseException as error:
        guard.record(error)
        raise
    guard.record(response)
    return response.status, body


def _cached(commits: list[str]) -> tuple[int, Store, str] | tuple[None, None, str]:
    """The nearest valid cached base among `commits` as `(index, store, note)`."""
    notes = []
    for index, commit in enumerate(commits):
        path = cached_path(commit)
        if not path.is_file():
            continue
        try:
            store = RS.load(path)
        except RS.StoreError as error:
            notes.append(f"refused the cached base {path}: {error}")
            continue
        if store["commit"] != commit:
            notes.append(f"refused the cached base {path}: it records commit {store['commit']}")
            continue
        return index, store, "; ".join(notes)
    return None, None, "; ".join(notes)


def find(root: Path, *, include_head: bool = True) -> Choice:
    """The base for a step to HEAD of the tree at `root` (see the module docstring)."""
    commits = first_parent_ancestors(root)
    if not include_head:
        commits = commits[1:]
    index, store, note = _cached(commits)
    prefix = f"{note}; " if note else ""

    def fallback(why: str) -> Choice:
        if store is not None and index is not None:
            return Choice(
                store, commits[index], "cache", f"{prefix}{why}; using the cached base at {commits[index][:12]}"
            )
        return Choice(None, None, "none", f"{prefix}{why}; no cached base either")

    nearer = commits if index is None else commits[:index]
    candidates = _published_candidates(root, nearer)
    if not candidates:
        if store is not None and index is not None:
            return Choice(
                store,
                commits[index],
                "cache",
                f"{prefix}the cached base at {commits[index][:12]}, with no nearer ancestor CI could have published",
            )
        return Choice(None, None, "none", f"{prefix}no base: no cached base and no ancestor on origin/main")
    slug = repository(root)
    if slug is None:
        return fallback("cannot ask GitHub for a nearer base: the `origin` remote names no GitHub repository")
    token, via = _token()
    if token is None:
        return fallback(f"cannot ask GitHub for a nearer base: {via}")
    guard_module = _guard_module()
    try:
        api = guard_module.github_api_url()
    except ValueError as error:
        return fallback(f"cannot ask GitHub: {error}")
    guard = _no_wait_guard()
    try:
        status, body = _call(guard, f"{api}/repos/{slug}/actions/artifacts?per_page=100", token)
    except _WouldWait as error:
        return fallback(f"did not list artifacts: {error}")
    except (OSError, RuntimeError, ValueError, guard_module.SecondaryLimit) as error:
        return fallback(f"listing artifacts failed ({error})")
    if status in (401, 403):
        return fallback(f"GitHub refused the token from {via} (HTTP {status}) listing artifacts")
    if status != 200:
        return fallback(f"listing artifacts answered HTTP {status}")
    try:
        listed = json.loads(body)["artifacts"]
    except (ValueError, KeyError, TypeError):
        listed = None
    if not isinstance(listed, list):
        return fallback("the artifact list was not JSON with an `artifacts` array")
    published: dict[str, Artifact] = {}
    for record in listed:
        artifact = Artifact.parse(record)
        if artifact is not None and not artifact.expired:
            published.setdefault(artifact.commit, artifact)
    chosen = next((commit for commit in candidates if commit in published), None)
    if chosen is None:
        return fallback(f"no nearer ancestor has a `{ARTIFACT_PREFIX}<sha>` artifact")
    artifact = published[chosen]
    try:
        status, body = _call(guard, f"{api}/repos/{slug}/actions/artifacts/{artifact.id}/zip", token)
    except _WouldWait as error:
        return fallback(f"found {ARTIFACT_PREFIX}{chosen} but did not download it: {error}")
    except (OSError, RuntimeError, ValueError, guard_module.SecondaryLimit) as error:
        return fallback(f"downloading {ARTIFACT_PREFIX}{chosen} failed ({error})")
    if status != 200:
        return fallback(f"downloading {ARTIFACT_PREFIX}{chosen} answered HTTP {status}")
    with tempfile.TemporaryDirectory(prefix="golden-reach-base-") as scratch:
        try:
            with zipfile.ZipFile(io.BytesIO(body)) as archive:
                archive.extract(ARTIFACT_FILE, scratch)
            downloaded = RS.load(Path(scratch) / ARTIFACT_FILE)
        except (zipfile.BadZipFile, KeyError, OSError) as error:
            return fallback(f"{ARTIFACT_PREFIX}{chosen} holds no readable {ARTIFACT_FILE} ({error})")
        except RS.StoreError as error:
            return fallback(f"refused {ARTIFACT_PREFIX}{chosen}: {error}")
    if downloaded["commit"] != chosen:
        return fallback(f"refused {ARTIFACT_PREFIX}{chosen}: it records commit {downloaded['commit']}")
    publish(downloaded)
    return Choice(downloaded, chosen, "artifact", f"{prefix}downloaded {ARTIFACT_PREFIX}{chosen}")
