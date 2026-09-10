#!/usr/bin/env python3
"""Derive, acquire and validate the finite wide witness-search evidence."""

from __future__ import annotations

import argparse
import csv
import concurrent.futures
import gzip
import tempfile
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import urllib.request
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REGIONS = (
    "bodies-media",
    "document-paths",
    "oas31-extensions",
    "parameters",
    "schemas",
    "security",
)
RANK_FIELDS = (
    "rank",
    "artifact_sha256",
    "artifact",
    "keys",
    "fern_evidence",
    "comparison_evidence",
)
SLOT_FIELDS = ("slot", "artifact_sha256", "keys", "disposition", "evidence")
CANDIDATE_FIELDS = (
    "artifact",
    "keys",
    "redistribution",
    "immutable publisher reference",
    "Fern acceptance",
    "retention",
    "disposition",
    "evidence",
)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


REDO = load("wide_redo", REPO / "scripts/witness-search-redo.py")
LOCAL = load("wide_local", REPO / "scripts/witness-search-local-census.py")
ROWS = load(
    "wide_rows", REPO / "tests/surface_census_test.py"
).RankedBacklogTests.region_rows


def baseline(regions: Path, contract: Path) -> dict[str, dict]:
    frozen = REDO.contract_keys(contract)
    result = {}
    for name in REGIONS:
        for row in ROWS((regions / f"{name}.md").read_text(encoding="utf-8")):
            if (
                REDO.value(row[3]) != "gap"
                or REDO.authoritative_details(row)[0] != "search-incomplete"
            ):
                continue
            key = REDO.value(row[0])
            match = re.search(r"census `([^`]+)`", " ".join(row))
            if not match or frozen.get(key) != match[1]:
                raise ValueError(
                    f"{name}/{key}: selector disagrees with frozen authority"
                )
            error = LOCAL.CENSUS.selector_error(match[1])
            if error:
                raise ValueError(error)
            item = {"selector": match[1], "region": name}
            if key in result and result[key] != item:
                raise ValueError(f"conflicting authoritative rows for {key}")
            result[key] = item
    return dict(sorted(result.items()))


def candidate_rows(path: Path) -> list[list[str]]:
    return [
        [cell.strip() for cell in line.strip("|").split("|")]
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("| `")
    ]


def derive(args) -> None:
    items = baseline(args.regions, args.contract)
    candidates = candidate_rows(args.contract.with_name("candidates.md"))
    passed = REDO.screened_keys(args.contract.with_name("candidates.md"))
    for key, item in items.items():
        item["usable_witness"] = key in passed
        item["candidates"] = [
            {
                "artifact": REDO.value(row[0]),
                "screens": row[2:6],
                "disposition": REDO.value(row[6]),
                "discarded": key
                in re.findall(r"`([^`]+)`", row[5].split("discarded keys:", 1)[1])
                if "discarded keys:" in row[5]
                else False,
            }
            for row in candidates
            if len(row) == 8 and key in re.findall(r"`([^`]+)`", row[1])
        ]
    args.report.mkdir(parents=True, exist_ok=True)
    write_json(
        args.report / "baseline.json",
        {
            "schema_version": 1,
            "source_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=REPO, encoding="utf-8"
            ).strip(),
            "keys": items,
        },
    )
    (args.report / "keys.md").write_text(
        "# Frozen derived baseline\n\n| key | selector |\n|---|---|\n"
        + "".join(
            f"| `{key}` | `{item['selector']}` |\n" for key, item in items.items()
        ),
        encoding="utf-8",
    )


def write_json(path: Path, value) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_inventory(path: Path) -> dict:
    text = (
        gzip.decompress(path.read_bytes()).decode("utf-8")
        if path.suffix == ".gz"
        else path.read_text(encoding="utf-8")
    )
    value = json.loads(text)
    if value.get("schema_version") != 1 or not isinstance(value.get("sources"), list):
        raise ValueError(
            f"{path}: expected inventory schema_version 1 and sources array"
        )
    seen = set()
    for row in value["sources"]:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("artifact"), str)
            or not row["artifact"]
        ):
            raise ValueError(f"{path}: missing artifact identity")
        if row["artifact"] in seen:
            raise ValueError(f"{path}: duplicate artifact {row['artifact']}")
        seen.add(row["artifact"])
        for field in ("sha256", "prior_sha256"):
            if field in row and not re.fullmatch("[0-9a-f]{64}", row[field]):
                raise ValueError(f"{path}: malformed {field}")
    return value


def atomic_bytes(path: Path, data: bytes) -> None:
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        staging = Path(stream.name)
        stream.write(data)
    staging.replace(path)


def acquire_one(job) -> dict:
    source, cache = job
    documents = cache / "documents"
    row = dict(source)
    expected = source.get("sha256")
    suffix = Path(source["artifact"]).suffix.lower()
    suffix = suffix if suffix in {".json", ".yaml", ".yml"} else ".json"
    cached = cache / expected if expected else None
    try:
        data = cached.read_bytes() if cached and cached.is_file() else None
        if data is not None and digest(data) != expected:
            row["cache_diagnostic"] = "cached digest changed; reacquire exact source"
            data = None
        if data is None:
            if source.get("local_path"):
                data = Path(source["local_path"]).read_bytes()
            else:
                with urllib.request.urlopen(source["artifact"], timeout=60) as response:
                    data = response.read()
            row["acquisition"] = "newly-fetched"
        else:
            row["acquisition"] = "verified-reuse"
        sha = digest(data)
        row["sha256"] = sha
        if expected and expected != sha:
            row.update(
                status="digest-changed",
                diagnostic=f"expected {expected}, acquired {sha}; excluded from census",
            )
            return row
        atomic_bytes(cache / sha, data)
        row["prior_relation"] = (
            "verified-already-scanned"
            if source.get("prior_sha256") == sha
            else "changed-bytes"
            if source.get("prior_sha256")
            else "not-proven-previously-scanned"
        )
        # Some publisher .yaml paths contain JSON. Preserve every byte while
        # choosing the census loader for the actual serialization.
        if data.decode("utf-8-sig").lstrip().startswith(("{", "[")):
            suffix = ".json"
        path = documents / (sha + suffix)
        atomic_bytes(path, data)
        try:
            doc = LOCAL.CENSUS.load_document(path)
            if not isinstance(doc, dict) or not re.fullmatch(
                r"3\.[01]\.\d+(?:[-+].*)?", str(doc.get("openapi", ""))
            ):
                row.update(
                    status="excluded",
                    diagnostic="not an OpenAPI 3 document; no conversion performed",
                )
            else:
                info = doc.get("info") or {}
                if not isinstance(info, dict):
                    raise ValueError("OpenAPI info must be an object")
                row.update(
                    status="readable",
                    document=path.name,
                )
                if info.get("license"):
                    row["document_license"] = info["license"]
        except (ValueError, LOCAL.CENSUS.DocumentError) as error:
            row.update(status="unreadable", diagnostic=str(error))
    except (ValueError, UnicodeError) as error:
        row.update(status="unreadable", diagnostic=str(error))
    except OSError as error:
        row.update(status="inaccessible", diagnostic=str(error))
    return row


def acquire(args) -> None:
    """Fetch each identity once; only verified digests authorize cached reuse."""
    inventory = read_inventory(args.inventory)
    LOCAL.contract_keys(args.contract)
    if args.workers < 1:
        raise ValueError("workers must be positive")
    args.cache.mkdir(parents=True, exist_ok=True)
    documents = args.cache / "documents"
    documents.mkdir(exist_ok=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        outcomes = list(
            pool.map(acquire_one, ((row, args.cache) for row in inventory["sources"]))
        )
    # Census only this invocation's readable bytes, never stale cache documents.
    selected = {row["document"] for row in outcomes if row["status"] == "readable"}
    for path in documents.iterdir():
        if path.name not in selected:
            path.unlink()
    output = {
        "schema_version": 1,
        "inventory_sha256": digest(args.inventory.read_bytes()),
        "sources": outcomes,
    }
    write_json(args.output, output)
    run = subprocess.run(
        [
            "just",
            "witness-search-local-census",
            "--contract",
            str(args.contract),
            "--workers",
            str(args.workers),
            "--documents",
            f"acquired={documents}",
        ],
        cwd=REPO,
        capture_output=True,
        encoding="utf-8",
    )
    args.output.with_suffix(".census.tsv").write_text(run.stdout, encoding="utf-8")
    args.output.with_suffix(".census.log").write_text(run.stderr, encoding="utf-8")
    output["census_exit"] = run.returncode
    write_json(args.output, output)
    if run.returncode:
        raise ValueError(f"census failed; see {args.output.with_suffix('.census.log')}")


def json_keys(text: str, known: set[str]) -> list[str]:
    keys = json.loads(text)
    if not isinstance(keys, list) or any(not isinstance(k, str) for k in keys):
        raise ValueError("keys must be a JSON array of strings")
    if len(keys) != len(set(keys)) or set(keys) - known:
        raise ValueError(f"duplicate or unknown keys: {keys}")
    return keys


def evidence(root: Path, name: str) -> None:
    path = (root / name).resolve()
    if not name or not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f"missing or outside-report evidence: {name}")


def validate(args) -> None:
    root = args.report
    fingerprints = root / "historical-sha256.tsv"
    if fingerprints.is_file():
        with fingerprints.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, dialect="excel-tab"):
                path = (REPO / row["path"]).resolve()
                if (
                    not path.is_relative_to(REPO)
                    or digest(path.read_bytes()) != row["sha256"]
                ):
                    raise ValueError(f"historical report bytes changed: {row['path']}")
    stored = json.loads((root / "baseline.json").read_text(encoding="utf-8"))
    if stored.get("schema_version") != 1:
        raise ValueError("baseline schema_version must be 1")
    authority = baseline(args.regions, args.contract)
    # Frozen keys may later become golden; selectors remain tied to entry rows.
    all_selectors = {}
    for name in REGIONS:
        for row in ROWS((args.regions / f"{name}.md").read_text(encoding="utf-8")):
            match = re.search(r"census `([^`]+)`", " ".join(row))
            if match:
                all_selectors[REDO.value(row[0])] = match[1]
    keys = dict(LOCAL.contract_keys(root / "keys.md"))
    expected = {k: v["selector"] for k, v in stored["keys"].items()}
    if (
        keys != expected
        or any(all_selectors.get(k) != v for k, v in keys.items())
        or set(authority) - keys.keys()
    ):
        raise ValueError(
            "derived selectors/keys disagree with authority or frozen baseline"
        )
    known = set(keys)
    candidates = root / "candidates.md"
    header = next(
        (
            line
            for line in candidates.read_text(encoding="utf-8").splitlines()
            if line.startswith("| artifact")
        ),
        "",
    )
    if tuple(cell.strip() for cell in header.strip("|").split("|")) != CANDIDATE_FIELDS:
        raise ValueError("candidate header differs from eight-column contract")
    passing = {}
    candidate_identities = set()
    for row in candidate_rows(candidates):
        if len(row) != 8:
            raise ValueError("candidate row must have eight columns")
        if REDO.value(row[6]) not in {
            "witness-found",
            "witness-blocked",
            "fern-rejected",
            "search-incomplete",
        }:
            raise ValueError("unknown candidate disposition")
        if not all(row[2:6]):
            raise ValueError("candidate is missing a screen state")
        identity = REDO.value(row[0])
        if identity in candidate_identities:
            raise ValueError(f"duplicate candidate artifact: {identity}")
        candidate_identities.add(identity)
        owned = set(re.findall(r"`([^`]+)`", row[1]))
        if owned - known:
            raise ValueError(f"candidate has unknown keys: {owned - known}")
        # Use the canonical screening function per artifact, without duplicating precedence.
        if REDO.value(row[6]) == "witness-found":
            passing[REDO.value(row[0])] = REDO.screened_keys(
                candidates, artifact=REDO.value(row[0])
            )
    screened = REDO.screened_keys(candidates)
    ranks = {}
    identities = set()
    ranked_keys = {}
    with (root / "ranking.tsv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, dialect="excel-tab")
        if tuple(reader.fieldnames or ()) != RANK_FIELDS:
            raise ValueError("ranking header differs from contract")
        for row in reader:
            rank = row["rank"]
            sha = row["artifact_sha256"]
            if not re.fullmatch("[1-9][0-9]*", rank) or int(rank) in ranks:
                raise ValueError(f"malformed or duplicate rank: {rank}")
            if not re.fullmatch("[0-9a-f]{64}", sha) or sha in identities:
                raise ValueError(f"malformed or duplicate ranked digest: {sha}")
            owned = json_keys(row["keys"], known)
            if (
                not owned
                or not set(owned) <= screened
                or not set(owned) <= passing.get(row["artifact"], set())
            ):
                raise ValueError("ranked artifact lacks retained candidate screens")
            for field in ("fern_evidence", "comparison_evidence"):
                evidence(root, row[field])
            ranks[int(rank)] = row
            identities.add(sha)
            ranked_keys[sha] = set(owned)
    ranked_artifacts = {row["artifact"] for row in ranks.values()}
    aliases = {}
    firmness = {}
    acquisition = root / (
        "acquisition.json.gz"
        if (root / "acquisition.json.gz").exists()
        else "acquisition.json"
    )
    if acquisition.is_file():
        for row in read_inventory(acquisition)["sources"]:
            sha = row.get("sha256")
            aliases[row["artifact"]] = sha
            grade = (
                (
                    int(bool(row.get("repository_licences")))
                    + int(bool(row.get("document_license")))
                )
                if row.get("ref")
                and row.get("repository") != "APIs-guru/openapi-directory"
                else 0
            )
            firmness[sha] = max(firmness.get(sha, 0), grade)
    for artifact, retained in passing.items():
        if (
            retained
            and artifact not in ranked_artifacts
            and aliases.get(artifact) not in identities
        ):
            raise ValueError(f"retained candidate missing rank: {artifact}")
    if sorted(ranks) != list(range(1, len(ranks) + 1)):
        raise ValueError("ranks must be contiguous from 1")
    expected_order = sorted(
        ranks.values(),
        key=lambda row: (
            -len(json.loads(row["keys"])),
            -firmness.get(row["artifact_sha256"], 0),
            row["artifact_sha256"],
        ),
    )
    if [ranks[k] for k in sorted(ranks)] != expected_order:
        raise ValueError(
            "ranking violates retained-key coverage, publisher/licence firmness or SHA order"
        )
    slots = set()
    claimed = set()
    registered_keys = set()
    text = (root / "slots.md").read_text(encoding="utf-8")
    header = next((line for line in text.splitlines() if line.startswith("| slot")), "")
    if tuple(cell.strip() for cell in header.strip("|").split("|")) != SLOT_FIELDS:
        raise ValueError("slot header differs from contract")
    for line in text.splitlines():
        if not line.startswith("| ") or line == header:
            continue
        cells = [REDO.value(cell.strip()) for cell in line.strip("|").split("|")]
        if len(cells) != 5:
            raise ValueError("slot row must have five columns")
        slot, sha, raw_keys, disposition, proof = cells
        owned = set(json_keys(raw_keys, known))
        if not slot or slot in slots:
            raise ValueError("duplicate or empty slot")
        slots.add(slot)
        if disposition not in {"registered", "blocked", "exhausted"}:
            raise ValueError("unknown slot disposition")
        evidence(root, proof)
        if disposition == "exhausted":
            if sha != "—" or owned:
                raise ValueError("exhausted slot must have absent artifact and keys")
        else:
            if (
                sha in claimed
                or sha not in ranked_keys
                or not owned
                or not owned <= ranked_keys[sha]
            ):
                raise ValueError("conflicting slot claim or unranked artifact/keys")
            claimed.add(sha)
            if disposition == "registered":
                if owned & registered_keys:
                    raise ValueError("conflicting registered key claims")
                registered_keys.update(owned)
    if args.inventory:
        inventory = read_inventory(args.inventory)
        outcomes = read_inventory(acquisition)
        if outcomes.get("inventory_sha256") != digest(args.inventory.read_bytes()) or {
            r["artifact"] for r in inventory["sources"]
        } != {r["artifact"] for r in outcomes["sources"]}:
            raise ValueError(
                "partial inventory accounting or inventory digest mismatch"
            )
        for row in outcomes["sources"]:
            if row.get("status") not in {
                "readable",
                "unreadable",
                "inaccessible",
                "excluded",
                "digest-changed",
            }:
                raise ValueError("missing acquisition outcome")
            if row["status"] != "readable" and not row.get("diagnostic"):
                raise ValueError("failed acquisition missing diagnostic")
        if "census_runs" in outcomes:
            declarations: dict[str, set[str]] = {}
            documents = {
                row.get("document")
                for row in outcomes["sources"]
                if row["status"] == "readable"
            }
            if not outcomes["census_runs"]:
                raise ValueError("missing census runs")
            for run in outcomes["census_runs"]:
                if run["exit_code"] != 0:
                    raise ValueError("unfinished or failed census")
                for stream in ("stdout", "stderr"):
                    evidence(root, run[stream])
                    if (
                        digest((root / run[stream]).read_bytes())
                        != run[stream + "_sha256"]
                    ):
                        raise ValueError("census evidence digest changed")
                with (root / run["stdout"]).open(
                    encoding="utf-8", newline=""
                ) as stream:
                    reader = csv.DictReader(stream, dialect="excel-tab")
                    if tuple(reader.fieldnames or ()) != (
                        "source",
                        "key",
                        "selector",
                        "document",
                        "count",
                    ):
                        raise ValueError("census evidence header changed")
                    for row in reader:
                        if (
                            row["document"] not in documents
                            or keys.get(row["key"]) != row["selector"]
                        ):
                            raise ValueError(
                                "census has unknown document, selector or key"
                            )
                        if not re.fullmatch("[1-9][0-9]*", row["count"]):
                            raise ValueError("invalid declaration count")
                        declarations.setdefault(Path(row["document"]).stem, set()).add(
                            row["key"]
                        )
            accounted = set()
            for row in candidate_rows(candidates):
                artifact = REDO.value(row[0])
                sha = aliases.get(artifact)
                if declarations.get(sha) != set(re.findall(r"`([^`]+)`", row[1])):
                    raise ValueError(
                        "candidate keys disagree with measured declarations"
                    )
                evidence(root, REDO.value(row[7]))
                accounted.add(sha)
            if accounted != set(declarations):
                raise ValueError(
                    "declaring artifacts missing completed or blocked screens"
                )


def index_tree(args) -> None:
    """Associate every version with its exact indexed YAML alternative, if tracked."""
    if digest(args.index.read_bytes()) != args.index_sha256:
        raise ValueError("complete catalogue digest changed")
    pin = subprocess.check_output(
        ["git", "-C", str(args.tree), "rev-parse", "HEAD"], encoding="utf-8"
    ).strip()
    if pin != args.ref:
        raise ValueError("tree commit differs from the requested pin")
    dirty = subprocess.run(
        ["git", "-C", str(args.tree), "diff", "--quiet", "HEAD", "--", "APIs"]
    )
    if dirty.returncode:
        raise ValueError("pinned tree has changed bytes")
    tracked = {}
    tree_records = subprocess.check_output(
        ["git", "-C", str(args.tree), "ls-tree", "-r", "-z", "HEAD", "--", "APIs"],
        encoding="utf-8",
    )
    for record in tree_records.split("\0"):
        if record:
            metadata, path = record.split("\t", 1)
            _mode, kind, object_id = metadata.split()
            if kind == "blob":
                tracked[path] = object_id
    guru = load("wide_guru", REPO / "scripts/apis-guru-gap-screen.py")
    index = json.loads(args.index.read_text(encoding="utf-8"))
    sources = []
    for api, version, primary in guru.versions(index):
        metadata = index[api]["versions"][version]
        alternate = metadata.get("swaggerYamlUrl", "")
        path = "APIs/" + urllib.parse.unquote(
            urllib.parse.urlsplit(alternate).path.partition("/specs/")[2]
        )
        row = {
            "artifact": primary,
            "api_id": api,
            "version": version,
            "catalogue_url": primary,
        }
        if alternate and path in tracked and (args.tree / path).is_file():
            data = (args.tree / path).read_bytes()
            # Git's clean filters can hide changed literal bytes (for example CRLF).
            # Compare the raw Git blob identity as well as the working-tree diff.
            object_id = tracked[path]
            algorithm = "sha1" if len(object_id) == 40 else "sha256"
            blob = f"blob {len(data)}\0".encode("ascii") + data
            if hashlib.new(algorithm, blob).hexdigest() != object_id:
                raise ValueError(f"pinned tree has changed literal bytes: {path}")
            row.update(
                artifact=f"https://raw.githubusercontent.com/APIs-guru/openapi-directory/{pin}/{path}",
                indexed_alternative=alternate,
                repository="APIs-guru/openapi-directory",
                ref=pin,
                path=path,
                sha256=digest(data),
            )
            if args.prior_ref == pin:
                row["prior_sha256"] = row["sha256"]
            if args.local_paths:
                row["local_path"] = str((args.tree / path).resolve())
        else:
            row["tree_diagnostic"] = (
                "indexed alternative absent from pinned repository tree"
            )
        sources.append(row)
    write_json(
        args.output,
        {
            "schema_version": 1,
            "catalogue_sha256": args.index_sha256,
            "sources": sources,
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("derive", "validate"):
        p = sub.add_parser(command)
        p.add_argument("--report", type=Path, required=True)
        p.add_argument("--regions", type=Path, default=REPO / "docs/openapi-surface")
        p.add_argument(
            "--contract",
            type=Path,
            default=REPO / "docs/openapi-surface/witness-search-redo/contract.md",
        )
        if command == "validate":
            p.add_argument("--inventory", type=Path)
    p = sub.add_parser("acquire")
    p.add_argument("--inventory", type=Path, required=True)
    p.add_argument("--cache", type=Path, required=True)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--workers", type=int, default=1)
    p = sub.add_parser("index-tree")
    p.add_argument("--index", type=Path, required=True)
    p.add_argument("--index-sha256", required=True)
    p.add_argument("--tree", type=Path, required=True)
    p.add_argument("--ref", required=True)
    p.add_argument("--prior-ref")
    p.add_argument("--local-paths", action="store_true")
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        {
            "derive": derive,
            "acquire": acquire,
            "validate": validate,
            "index-tree": index_tree,
        }[args.command](args)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"witness-scrape-wide: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
