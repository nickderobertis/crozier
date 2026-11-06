"""GitHub REST reads for the repin-cost harness, every one through crozier's
rate-limit guard and its shared response cache (tools/witness-search/rate_limit_guard.py).

A cache hit makes no call. A miss acquires the `core` bucket, makes the call,
records it with the guard, and stores the answer. Reads only: no method but GET.
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "witness-search"))

_spec = importlib.util.spec_from_file_location(
    "rate_limit_guard", REPO_ROOT / "tools/witness-search/rate_limit_guard.py"
)
assert _spec is not None and _spec.loader is not None
rlg = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = rlg
_spec.loader.exec_module(rlg)

API = rlg.github_api_url()
OWNER_REPO = "nickderobertis/crozier"


class _NoRedirectAuth(urllib.request.HTTPRedirectHandler):
    """Follow a log download's redirect to blob storage without the credential."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None:
            new.headers.pop("Authorization", None)
            new.unredirected_hdrs.pop("Authorization", None)
        return new


_OPENER = urllib.request.build_opener(_NoRedirectAuth)


class GitHub:
    def __init__(self, evidence_dir: Path) -> None:
        if not (os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")):
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=False).stdout.strip()
            if token:
                os.environ["GH_TOKEN"] = token
        self.guard = rlg.RateLimitGuard("github", evidence_dir=evidence_dir)
        self.ledger = Path(evidence_dir) / "repin-cost-requests.jsonl"
        self.calls = 0
        self.hits = 0

    def get(self, path: str, *, raw: bool = False) -> tuple[int, bytes]:
        url = path if path.startswith("http") else f"{API}{path}"
        if not rlg.is_github_api_url(url):
            raise ValueError("GitHub read must use the validated API origin; refusing to attach credentials")
        headers = {
            "User-Agent": "crozier-repin-cost-spike",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        cached = rlg.cache_lookup("GET", url, headers)
        if cached is not None:
            self.hits += 1
            self._log(url, cached.status, True)
            return cached.status, cached.body()
        request = urllib.request.Request(url, headers=headers, method="GET")
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            request.add_unredirected_header("Authorization", f"Bearer {token}")
        self.guard.acquire("core", cost=1)
        try:
            try:
                response = _OPENER.open(request, timeout=120)
            except urllib.error.HTTPError as error:
                response = error
            body = response.read()
        except BaseException as error:
            self.guard.record(error)
            raise
        self.guard.record(response)
        self.calls += 1
        status = response.status
        if not isinstance(status, int):
            raise RuntimeError("GitHub returned no HTTP status")
        self._log(url, status, False)
        rlg.cache_store("GET", url, headers, status, response.headers, body)
        return status, body

    def _log(self, url: str, status: int, hit: bool) -> None:
        with self.ledger.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"url": url, "status": status, "cache_hit": hit}) + "\n")

    def json(self, path: str):
        status, body = self.get(path)
        if status != 200:
            # Never read a refusal or a transient failure as "nothing there": that undercounts silently.
            raise SystemExit(
                f"GitHub answered {status} for {path}; re-run the harness (answers already cached cost nothing)"
            )
        return json.loads(body)

    def paged(self, path: str, key: str, *, limit_pages: int = 20) -> list:
        out: list = []
        sep = "&" if "?" in path else "?"
        for page in range(1, limit_pages + 1):
            data = self.json(f"{path}{sep}per_page=100&page={page}")
            if not data:
                break
            if not isinstance(data, dict) or not isinstance(data.get(key), list) or not all(isinstance(item, dict) for item in data[key]):
                raise SystemExit(f"GitHub returned a malformed {key} collection for {path}; restore complete evidence before measuring")
            items = data[key]
            out.extend(items)
            if len(items) < 100:
                break
        return out
