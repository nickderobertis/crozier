#!/usr/bin/env python3
"""Screen every APIs.guru version for the owned OpenAPI surface gaps."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = "https://api.apis.guru/v2/list.json"
DEFAULT_PROVENANCE = REPO / "docs/openapi-surface/apis-guru-publisher-provenance.tsv"
HEADER = (
    "snapshot_utc", "catalogue_digest", "gap_key", "selector", "outcome",
    "api_id", "version", "spec_url", "source_url", "immutable_ref", "license",
    "license_screen", "declaration_count", "notes",
)
OWNED_KEYS = (
    "annotated-ref-target-composed", "annotated-ref-target-closed-object",
    "annotated-ref-target-oneof", "annotated-ref-target-string-const",
    "anyof-array-variant-anyof-nullable-item",
    "anyof-array-variant-closed-object-item", "anyof-array-variant-empty-object-item",
    "anyof-array-variant-oneof-nullable-item", "anyof-array-variant-struct-item",
    "anyof-sole-member", "array-item-inheritance-union",
    "array-item-pointer-walk-anyof", "array-item-pointer-walk-oneof",
    "oneof-array-variant-annotated-ref-item",
    "oneof-array-variant-anyof-discriminated-union-item",
    "oneof-array-variant-anyof-item", "oneof-array-variant-anyof-nullable-item",
    "oneof-array-variant-closed-object-item", "oneof-array-variant-composed-item",
    "oneof-array-variant-empty-object-item",
    "property-sole-anyof-closed-object-member",
    "property-sole-anyof-composed-member", "property-sole-anyof-empty-object-member",
    "property-sole-anyof-struct-member", "property-sole-oneof-closed-object-member",
    "property-sole-oneof-composed-member", "property-sole-oneof-empty-object-member",
    "ref-pointer-undeclared-component-head", "ref-pointer-unnamed-segment",
)
CASE_11_KEY = "oneof-bare-object-example-variant"
SHA_REF = re.compile(r"(?:github\.com/[^/]+/[^/]+/(?:blob|raw)/|raw\.githubusercontent\.com/[^/]+/[^/]+/)([0-9a-f]{40})(?:/|$)", re.I)
GRANTS = re.compile(r"(?:apache|\bmit\b|bsd|cc0|gpl|agpl|lgpl|mpl|epl|cc[- ]by)", re.I)
REFUSED = re.compile(r"(?:noassertion|proprietary|unlicensed|all rights reserved)", re.I)


def load_census():
    path = REPO / "scripts/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("gap_screen_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CENSUS = load_census()


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.replace("\\|", "\0").strip().strip("|").split("|")]


def selectors_from_regions(regions: Path) -> dict[str, str]:
    """Derive the frozen key set's selectors from open or probe-settled rows."""
    wanted = set(OWNED_KEYS)
    found: dict[str, str] = {}
    case_11_is_owned = False
    for path in sorted(regions.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = table_cells(line) if line.startswith("|") else []
            if not cells:
                continue
            key = cells[0].strip("` ")
            category = cells[3].strip("` ") if len(cells) == 8 else ""
            if key == CASE_11_KEY and category in {"gap", "limitations"}:
                case_11_is_owned = True
                wanted.add(key)
            if key not in wanted:
                continue
            open_fixture = category == "gap" and "FIXTURE" in cells[7]
            settled_probe = (
                category == "limitations"
                and f"`../fern-limitations.md` `{key}`" in cells[4]
                and "convertible to `golden`" in cells[4]
            )
            if not (open_fixture or settled_probe):
                continue
            match = re.search(r"census `([^`]+)`", line)
            if not match:
                raise ValueError(f"{path}: measurable row {key!r} has no census selector")
            found[key] = match.group(1)
    missing = sorted(wanted - found.keys())
    if missing:
        raise ValueError(f"region rows do not define the owned measurable key(s): {', '.join(missing)}")
    if not case_11_is_owned and CASE_11_KEY in found:
        raise ValueError("case-11 was included without an owned region row")
    for key, selector in found.items():
        problem = CENSUS.selector_error(selector)
        if problem:
            raise ValueError(f"region row {key!r} has invalid selector {selector!r}: {problem}")
    return found


def fetch(url: str, attempts: int, timeout: float) -> bytes:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "crozier-gap-screen/1"})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except (OSError, urllib.error.URLError) as error:
            last = error
            if attempt + 1 < attempts:
                time.sleep(0.25 * (2**attempt))
    raise RuntimeError(f"unanswered after {attempts} bounded attempts: {url}: {last}")


def usable_url(url: str) -> str:
    """Percent-encode catalogue paths which APIs.guru sometimes leaves raw."""
    parsed = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, urllib.parse.quote(urllib.parse.unquote(parsed.path), safe="/%:@"), parsed.query, parsed.fragment)
    )


def parse_bytes(data: bytes, url: str) -> Any:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    temp = Path(url)  # diagnostic name only; the loader does not access it
    text = data.decode("utf-8-sig")
    if suffix == ".json" or text.lstrip().startswith(("{", "[")):
        try:
            return json.loads(text)
        except json.JSONDecodeError as error:
            raise ValueError(f"{url}:{error.lineno}: malformed JSON: {error.msg}") from error
    return CENSUS._YamlReader(temp, text).load()


def licence(document: Any) -> tuple[str, str]:
    value = ""
    if isinstance(document, dict):
        info = document.get("info")
        license_object = info.get("license") if isinstance(info, dict) else None
        if isinstance(license_object, dict):
            value = str(license_object.get("name") or license_object.get("identifier") or "").strip()
        elif isinstance(license_object, str):
            value = license_object.strip()
    if not value or REFUSED.search(value):
        return value, "refused"
    if GRANTS.search(value):
        return value, "admitted"
    return value, "unknown"


def publisher_provenance(path: Path) -> dict[tuple[str, str], tuple[str, str]]:
    """Load explicit publisher-ownership evidence keyed by catalogue identity."""
    result = {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, dialect="excel-tab")
        expected = ("api_id", "version", "source_url", "immutable_ref")
        if tuple(reader.fieldnames or ()) != expected:
            raise ValueError(f"{path}: expected provenance columns: {', '.join(expected)}")
        for line, row in enumerate(reader, 2):
            key = (row["api_id"], row["version"])
            source_url = row["source_url"]
            immutable_ref = row["immutable_ref"]
            match = SHA_REF.search(source_url)
            if not all((*key, source_url, immutable_ref)):
                raise ValueError(f"{path}:{line}: provenance fields must be non-empty")
            if not match or match.group(1).lower() != immutable_ref.lower():
                raise ValueError(f"{path}:{line}: source URL must contain its immutable ref")
            if key in result:
                raise ValueError(f"{path}:{line}: duplicate provenance for {key[0]}/{key[1]}")
            result[key] = (source_url, immutable_ref)
    return result


def rejected_api_guru_versions(path: Path) -> set[tuple[str, str]]:
    """APIs.guru identities already present in the rejected-spec ledger."""
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"api-guru `([^`/]+(?:[:][^`/]+)?)/([^`]+)`", text))


def versions(index: Any) -> list[tuple[str, str, str]]:
    result = []
    if not isinstance(index, dict):
        raise ValueError("catalogue index is not an object")
    for api_id, api in index.items():
        entries = api.get("versions") if isinstance(api, dict) else None
        if not isinstance(entries, dict):
            raise ValueError(f"catalogue API {api_id!r} has no versions object")
        for version, metadata in entries.items():
            url = metadata.get("swaggerUrl") if isinstance(metadata, dict) else None
            url = url or (metadata.get("swaggerYamlUrl") if isinstance(metadata, dict) else None)
            if not isinstance(url, str) or not url:
                raise ValueError(f"catalogue version {api_id}/{version} has no usable spec URL")
            result.append((str(api_id), str(version), usable_url(url)))
    return sorted(result)


def screen_one(entry: tuple[str, str, str], selectors: dict[str, str], attempts: int, timeout: float):
    api_id, version, url = entry
    document = parse_bytes(fetch(url, attempts, timeout), url)
    conjunctions = {
        selector: CENSUS.COMPILED_CONJUNCTIONS[selector]
        for selector in selectors.values()
        if selector in CENSUS.COMPILED_CONJUNCTIONS
    }
    counts = CENSUS.census_document(document, conjunctions=conjunctions)
    hits = {key: counts.get(selector, 0) for key, selector in selectors.items()}
    license_text, license_screen = licence(document)
    source_url = immutable_ref = ""
    notes = "publisher-owned immutable source not evidenced"
    if not license_text:
        notes += "; document declares no info.license"
    return entry, hits, license_text, license_screen, source_url, immutable_ref, notes


def write_report(path: Path, rows: list[dict[str, str]]) -> None:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=HEADER, dialect="excel-tab", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output.getvalue(), encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index-url", default=DEFAULT_INDEX)
    parser.add_argument("--output", type=Path, default=REPO / "docs/openapi-surface/apis-guru-gap-witnesses.tsv")
    parser.add_argument("--regions-dir", type=Path, default=REPO / "docs/openapi-surface")
    parser.add_argument("--provenance-map", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--snapshot-utc")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--workers", type=int, default=12)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.attempts < 1 or args.workers < 1 or args.timeout <= 0:
        print("apis-guru-gap-screen: attempts, workers, and timeout must be positive", file=sys.stderr)
        return 2
    try:
        selectors = selectors_from_regions(args.regions_dir)
        provenance = publisher_provenance(args.provenance_map)
        index_bytes = fetch(args.index_url, args.attempts, args.timeout)
        index = parse_bytes(index_bytes, args.index_url)
        entries = versions(index)
        results = []
        failures = []
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(screen_one, entry, selectors, args.attempts, args.timeout): entry for entry in entries}
            for future in as_completed(futures):
                try:
                    results.append(future.result())
                except Exception as error:  # every unanswered version invalidates the snapshot
                    failures.append(f"{futures[future][0]}/{futures[future][1]}: {error}")
        if failures:
            raise RuntimeError(f"{len(failures)} catalogue document(s) unanswered; first: {sorted(failures)[0]}")
        snapshot = args.snapshot_utc or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        digest = hashlib.sha256(index_bytes).hexdigest()
        rejected = rejected_api_guru_versions(REPO / "tests/fixtures/AGENTS.md")
        rows = []
        for key in selectors:
            for entry, hits, license_text, license_screen, source_url, immutable_ref, notes in results:
                count = hits[key]
                if count:
                    api_id, version, spec_url = entry
                    if (api_id, version) in provenance:
                        source_url, immutable_ref = provenance[(api_id, version)]
                        notes = notes.replace(
                            "publisher-owned immutable source not evidenced",
                            "publisher ownership evidenced by provenance mapping",
                            1,
                        )
                    if (api_id, version) in rejected:
                        notes += "; repeats the rejected-spec table in tests/fixtures/AGENTS.md"
                    rows.append(dict(zip(HEADER, (snapshot, digest, key, selectors[key], "candidate", api_id, version, spec_url, source_url, immutable_ref, license_text, license_screen, str(count), notes))))
            if not any(row["gap_key"] == key for row in rows):
                rows.append(dict(zip(HEADER, (snapshot, digest, key, selectors[key], "none-found", "", "", "", "", "", "", "", "", "no catalogue version declared this selector"))))
        rows.sort(key=lambda row: (row["gap_key"], row["api_id"], row["version"], row["spec_url"]))
        write_report(args.output, rows)
    except (OSError, ValueError, RuntimeError, CENSUS.DocumentError) as error:
        print(f"apis-guru-gap-screen: {error}", file=sys.stderr)
        return 1
    print(f"apis-guru-gap-screen: wrote {len(rows)} rows for {len(selectors)} gaps from {len(entries)} versions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
