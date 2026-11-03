"""The repin verb finishes a merge whose conflicts are all derived content, and refuses any other.

Each case makes two real branches conflict in a real git repository and hands the
conflicted merge to the verb's merge step (`census-repin.py`'s `resolve_merge`):
the scenario proof index, whose `write` restates some cells and leaves the
hand-decided ones, and the coverage index, whose generated sections sit between
authored prose.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[3]
HERE = REPO / "tools" / "surface-census"
INDEX = "docs/openapi-surface/scenario-proof-index.tsv"
COVERAGE = "docs/openapi-surface-coverage.md"


def _load(name: str, file: str) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VERB = _load("repin_merge_census_repin", "census-repin.py")
SCENARIO = _load("repin_merge_scenario_index", "scenario-proof-index.py")


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=check)


def commit(root: Path, message: str) -> None:
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", message)


def row(**cells: str) -> str:
    values = dict.fromkeys(SCENARIO.INDEX_HEADER, "x") | {"shape": "a-shape", "settings": "literals"} | cells
    return "\t".join(values[name] for name in SCENARIO.INDEX_HEADER)


COVERAGE_TEXT = (
    "# Coverage\n\nAuthored prose before.\n\n<!-- BEGIN GENERATED ARM TABLE: run `just golden-reach-arms` -->\n"
    "| rank | key |\n|---|---|\n| 1 | `a` |\n<!-- END GENERATED ARM TABLE -->\n\nAuthored prose after.\n"
)


def conflicted(tmp_path: Path, path: str, base: str, ours: str, theirs: str) -> Path:
    """A repository mid-merge, its one conflict in `path` between `ours` and `theirs`."""
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-q", "-b", "main")
    (root / path).parent.mkdir(parents=True, exist_ok=True)
    (root / path).write_text(base, encoding="utf-8")
    commit(root, "base")
    git(root, "checkout", "-q", "-b", "theirs")
    (root / path).write_text(theirs, encoding="utf-8")
    commit(root, "theirs")
    git(root, "checkout", "-q", "main")
    (root / path).write_text(ours, encoding="utf-8")
    commit(root, "ours")
    assert git(root, "merge", "-q", "theirs", check=False).returncode != 0, "the branches must conflict"
    return root


def header() -> str:
    return "\t".join(SCENARIO.INDEX_HEADER) + "\n"


@pytest.mark.parametrize(
    ("case", "edit", "derived"),
    [
        ("a derived cell", {"settings": "python_enums"}, True),
        ("a hand-decided cell", {"closer": "nodes:a-difference"}, False),
    ],
    ids=["derived settings cell", "hand-decided closer cell"],
)
def test_a_scenario_index_conflict_resolves_only_in_the_cells_its_writer_restates(
    tmp_path: Path, case: str, edit: dict[str, str], derived: bool
) -> None:
    ours = {name: f"{value}-ours" for name, value in edit.items()}
    root = conflicted(
        tmp_path, INDEX, header() + row() + "\n", header() + row(**ours) + "\n", header() + row(**edit) + "\n"
    )
    if derived:
        assert VERB.resolve_merge(root) == 1, case
        assert len(git(root, "rev-list", "--parents", "-n", "1", "HEAD").stdout.split()) == 3, "HEAD is the merge"
        assert "<<<<<<<" not in (root / INDEX).read_text(encoding="utf-8")
        return
    with pytest.raises(SystemExit) as refused:
        VERB.resolve_merge(root)
    assert f"{INDEX}:2: `" in str(refused.value) and "is not derived content" in str(refused.value)
    assert git(root, "rev-parse", "-q", "--verify", "MERGE_HEAD", check=False).returncode == 0, "the merge is left open"


@pytest.mark.parametrize(
    ("case", "old", "derived"),
    [
        ("inside a generated section", "| 1 | `a` |", True),
        ("on the authored line after it", "Authored prose after.", False),
        (
            "across its end marker into authored prose",
            "| 1 | `a` |\n<!-- END GENERATED ARM TABLE -->\n\nAuthored prose after.",
            False,
        ),
    ],
)
def test_a_coverage_index_conflict_resolves_only_inside_its_generated_sections(
    tmp_path: Path, case: str, old: str, derived: bool
) -> None:
    root = conflicted(
        tmp_path,
        COVERAGE,
        COVERAGE_TEXT,
        COVERAGE_TEXT.replace(old, f"{old} ours"),
        COVERAGE_TEXT.replace(old, f"{old} theirs"),
    )
    if derived:
        assert VERB.resolve_merge(root) == 1, case
        assert "<<<<<<<" not in (root / COVERAGE).read_text(encoding="utf-8")
        return
    with pytest.raises(SystemExit) as refused:
        VERB.resolve_merge(root)
    assert f"{COVERAGE}:" in str(refused.value) and "is not derived content" in str(refused.value)
    assert git(root, "rev-parse", "-q", "--verify", "MERGE_HEAD", check=False).returncode == 0, "the merge is left open"
