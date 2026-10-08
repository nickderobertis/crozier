#!/usr/bin/env python3
"""Download a pinned public GitHub tree through the shared REST-bucket guard.

Exit status: 0 when the tree was saved; 1 when the acquisition failed or the
rate-limit guard refused it (the attempt is still recorded in
`acquisitions.jsonl`); 2 on a usage error, a URL or bucket it cannot use
among them.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import importlib.util
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def load_guard():
    path = Path(__file__).with_name("rate_limit_guard.py")
    spec = importlib.util.spec_from_file_location("witness_acquire_guard", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


GUARD = load_guard()

DOWNLOAD_HOSTS = ("api.github.com", "codeload.github.com", "raw.githubusercontent.com")
"""The GitHub services a pinned tree or document is downloaded from."""


def is_download_url(value: str) -> bool:
    """A GitHub download over HTTPS, or a loopback HTTP server (the offline tier)."""
    parsed = urllib.parse.urlsplit(value)
    return (
        GUARD.valid_port(parsed)
        and bool(parsed.hostname)
        and (
            (parsed.scheme == "https" and parsed.hostname in DOWNLOAD_HOSTS)
            or (parsed.scheme == "http" and parsed.hostname in GUARD.LOOPBACK_HOSTS)
        )
    )


def download_url(value: str) -> str:
    """`value`, once it is a download this script may make; every redirect it follows is held to the same."""
    if not is_download_url(value):
        raise argparse.ArgumentTypeError(
            f"{value!r} must be an https:// URL on {', '.join(DOWNLOAD_HOSTS)} or a loopback HTTP URL"
        )
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", type=download_url)
    parser.add_argument("output", type=Path)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    parser.add_argument("--bucket", choices=sorted(GUARD.GITHUB_BUCKETS), default="core")
    args = parser.parse_args()
    try:
        api_root = urllib.parse.urlsplit(GUARD.github_api_url())
    except ValueError as error:
        parser.error(str(error))
    guard = GUARD.RateLimitGuard("github", evidence_dir=args.evidence_dir)
    headers = {"User-Agent": "crozier-witness-acquisition/1"}
    target = urllib.parse.urlsplit(args.url)
    if (target.scheme, target.netloc) == (api_root.scheme, api_root.netloc):
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(args.url, headers=headers)
    record = {"url": args.url, "taken_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    temporary = args.output.with_suffix(args.output.suffix + ".part")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    # Success is a completed acquisition: every byte read and written, the
    # reservation closed and the file published. An HTTP 200 alone is not one.
    transferred = acquired = False
    try:
        guard.acquire(args.bucket, cost=1)
        try:
            with GUARD.open_checked(request, is_download_url, timeout=120) as response:
                record["status"] = response.status
                with temporary.open("wb") as handle:
                    while chunk := response.read(1024 * 1024):
                        handle.write(chunk)
                        digest.update(chunk)
                if response.length:
                    # read(amt) ends quietly when the connection drops short of
                    # the declared Content-Length; the bytes it never sent are
                    # an interrupted transfer, not the end of the file.
                    raise http.client.IncompleteRead(b"", response.length)
                guard.record(response)
                transferred = True
        except urllib.error.HTTPError as response:
            guard.record(response)
            record["status"] = response.code
            record["error"] = response.read(500).decode("utf-8", errors="replace")
        except (OSError, urllib.error.URLError, http.client.HTTPException) as error:
            # Transport errors have no HTTP response, and a transfer or write
            # interrupted after the status line has no complete one. Close the
            # reservation and retain the measured error instead of treating the
            # source as empty or its partial bytes as acquired.
            class TransportFailure:
                status = 503
                headers: dict[str, str] = {}
                url = args.url

            guard.record(TransportFailure())
            record["error"] = str(error) or type(error).__name__
        if transferred and record.get("status") == 200:
            try:
                temporary.replace(args.output)
            except OSError as error:
                # Every byte arrived, but the file is not where the caller reads it.
                record["error"] = f"could not publish {args.output}: {error.strerror or error}"
                temporary.unlink(missing_ok=True)
            else:
                record["sha256"] = digest.hexdigest()
                record["bytes"] = args.output.stat().st_size
                acquired = True
        else:
            temporary.unlink(missing_ok=True)
    except (GUARD.SecondaryLimit, GUARD.UnsupportedBucket, OSError, RuntimeError, ValueError) as error:
        record["error"] = f"rate-limit guard refused acquisition: {error}"
        temporary.unlink(missing_ok=True)
    finally:
        args.evidence_dir.mkdir(parents=True, exist_ok=True)
        with (args.evidence_dir / "acquisitions.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    if not acquired:
        print(
            f"witness-acquire-github: {args.url}: {record.get('status', 'transport error')}: "
            f"{record.get('error', 'request failed')}; inspect {args.evidence_dir / 'acquisitions.jsonl'} "
            "and retry the recorded source when available",
            file=sys.stderr,
        )
        return 1
    print(f"witness-acquire-github: saved {record['bytes']} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
