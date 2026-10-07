#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace (no nx.json or project.json anywhere); this audit sits in scripts/ beside witness-search-github.py, whose committed evidence and notes it reads, and tests/witness_search_github_test.py drives it.
"""Reject public locators for excluded inputs in committed evidence and notes."""
from __future__ import annotations

import argparse
import gzip
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "locator_audit_index", ROOT / "scripts/witness-search-github-index.py"
)
assert spec is not None and spec.loader is not None
INDEX = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = INDEX
spec.loader.exec_module(INDEX)
TOKEN = re.compile(re.escape(INDEX.OPAQUE_PREFIX) + r"[0-9a-f]{32}:[1-9][0-9]*")
REPOSITORIES = "|".join(re.escape(repo) for repo in INDEX.EXCLUDED_REPOSITORIES)
LOCATOR = re.compile(
    rf"(?:https?://(?:raw\.)?github(?:usercontent)?\.com/)?(?:{REPOSITORIES})(?P<separator>[:/@])(?P<value>[^\s`\"<>]*)",
    re.IGNORECASE,
)
# Certified SDK contribution and issue links identify no input document.
ALLOWED_URLS = frozenset((
    "https://github.com/fern-api/fern/blob/main/CONTRIBUTING.md",
    "https://github.com/fern-api/fern/issues",
))
QUALIFIED_REVISION = re.compile(
    rf"(?:{REPOSITORIES})[`\"']?\s+(?:at\s+)?[`\"']?[0-9a-f]{{40}}", re.IGNORECASE
)

PROSE_LOCATOR = re.compile(
    rf"(?:{REPOSITORIES})[`\"']?(?:'s)?\s+(?:(?:own|input|document|fixture|test|file)\s+)*"
    r"[`\"'][^`\"'\n]+\.(?:yaml|yml|json)(?:\.source)?[`\"']",
    re.IGNORECASE,
)


def findings(text: str) -> list[str]:
    errors = []
    if not any(repo.lower() in text.lower() for repo in INDEX.EXCLUDED_REPOSITORIES):
        return errors
    for match in LOCATOR.finditer(text):
        if match[0].rstrip(').,;') in ALLOWED_URLS:
            continue
        value = match['value'].rstrip('.,;)')
        if not value:
            continue
        parts = value.split('@', 1)
        if not all(TOKEN.fullmatch(part) for part in parts):
            errors.append('excluded repository retains a public locator')
    if PROSE_LOCATOR.search(text):
        errors.append('excluded repository retains a public locator in prose')
    if QUALIFIED_REVISION.search(text):
        errors.append('excluded repository retains a public revision')
    return errors


def structured_findings(value: Any) -> list[str]:
    errors = []
    if isinstance(value, dict):
        repository = value.get('repository')
        if isinstance(repository, dict):
            repository = repository.get('nameWithOwner') or repository.get('full_name')
        if isinstance(repository, str) and INDEX.excluded_repository(repository):
            for field in ('path', *INDEX.OPAQUE_LOCATORS, 'supersedes'):
                locator = value.get(field)
                if locator is not None and not INDEX.opaque_subject(locator):
                    errors.append(f'excluded repository retains a public {field}')
        for item in value.values():
            errors.extend(structured_findings(item))
    elif isinstance(value, list):
        for item in value:
            errors.extend(structured_findings(item))
    return errors


def audit(root: Path) -> list[str]:
    paths = subprocess.check_output(
        ['git', '-C', str(root), 'ls-files', '-z', 'docs/openapi-surface', 'docs/openapi-surface-coverage.md']
    ).decode().split('\0')
    errors = []
    for name in filter(None, paths):
        path = root / name
        if path.suffix not in ('.md', '.json', '.jsonl', '.tsv', '.gz'):
            continue
        compressed = path.suffix == '.gz'
        format_suffix = path.with_suffix('').suffix if compressed else path.suffix
        text = gzip.decompress(path.read_bytes()).decode() if compressed else path.read_text()
        for line_number, line in enumerate(text.splitlines(), 1):
            problems = findings(line)
            if format_suffix == '.jsonl':
                problems.extend(structured_findings(json.loads(line)))
            errors.extend(f'{name}:{line_number}: {problem}' for problem in problems)
        if format_suffix == '.json':
            errors.extend(f'{name}: {problem}' for problem in structured_findings(json.loads(text)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = audit(args.root)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f'witness-locator-audit: {error}; restore valid evidence and retry', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        print('Replace excluded input locators with their existing anonymous identities and retry.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
