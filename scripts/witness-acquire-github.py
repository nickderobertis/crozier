#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate uses just rather than Nx; this guarded archive acquisition command lives with the other repository scripts and is exercised by the witness-search acquisition tier.
"""Download a pinned public GitHub tree through the shared REST-bucket guard."""

from __future__ import annotations

import argparse
import hashlib
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    parser.add_argument("--bucket", default="core")
    args = parser.parse_args()
    guard = GUARD.RateLimitGuard("github", evidence_dir=args.evidence_dir)
    headers = {"User-Agent": "crozier-witness-acquisition/1"}
    api_root = os.environ.get("CROZIER_GITHUB_API_URL", "https://api.github.com")
    if urllib.parse.urlsplit(args.url).netloc == urllib.parse.urlsplit(api_root).netloc:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(args.url, headers=headers)
    record = {"url": args.url, "taken_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    temporary = args.output.with_suffix(args.output.suffix + ".part")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    try:
        guard.acquire(args.bucket, cost=1)
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                record["status"] = response.status
                with temporary.open("wb") as handle:
                    while chunk := response.read(1024 * 1024):
                        handle.write(chunk)
                        digest.update(chunk)
                guard.record(response)
        except urllib.error.HTTPError as response:
            guard.record(response)
            record["status"] = response.code
            record["error"] = response.read(500).decode("utf-8", errors="replace")
        except (OSError, urllib.error.URLError) as error:
            # Transport errors have no HTTP response. Close the reservation and
            # retain the measured error instead of treating the source as empty.
            class TransportFailure:
                status = 503
                headers: dict[str, str] = {}
                url = args.url

            guard.record(TransportFailure())
            record["error"] = str(error)
        if record.get("status") == 200:
            temporary.replace(args.output)
            record["sha256"] = digest.hexdigest()
            record["bytes"] = args.output.stat().st_size
        else:
            temporary.unlink(missing_ok=True)
    finally:
        args.evidence_dir.mkdir(parents=True, exist_ok=True)
        with (args.evidence_dir / "acquisitions.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    if record.get("status") != 200:
        print(f"witness-acquire-github: {args.url}: {record.get('status', 'transport error')}: "
              f"{record.get('error', 'request failed')}; inspect {args.evidence_dir / 'acquisitions.jsonl'} "
              "and retry the recorded source when available", file=sys.stderr)
        return 1
    print(f"witness-acquire-github: saved {record['bytes']} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
