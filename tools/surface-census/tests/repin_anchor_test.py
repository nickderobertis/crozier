"""The repin verb follows a moved site anchor into HEAD, and refuses, rewriting nothing, where it cannot.

Each case commits a base and a HEAD version of one Rust source in a real git
repository whose site table anchors an arm in it, then runs the verb's
re-anchoring step (`census-repin.py`'s `reanchor_all`) from the base commit.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[3]
SPEC = "src/lib.rs::pick[if x \\{]"
SITES = "docs/openapi-surface/golden-reach-sites.tsv"
BASE = "pub fn pick(x: bool, y: u8) -> u8 {\n    if x {\n        return y + 1;\n    }\n    y\n}\n"


def _verb() -> Any:
    name = "repin_anchor_census_repin"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, REPO / "tools/surface-census/census-repin.py")
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout.strip()


def repository(tmp_path: Path, base: str, head: str | None) -> tuple[Path, str]:
    """A repository whose base commit holds `base`, and whose HEAD holds `head` (deleted when None)."""
    root = tmp_path / "repo"
    (root / "src").mkdir(parents=True)
    (root / SITES).parent.mkdir(parents=True)
    (root / SITES).write_text(f"key\tselectors\tsites\tnote\nk\tschema.x\t{SPEC}\t\n", encoding="utf-8")
    (root / "src/lib.rs").write_text(base, encoding="utf-8")
    git(root, "init", "-q", "-b", "main")
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "base")
    commit = git(root, "rev-parse", "HEAD")
    if head is None:
        (root / "src/lib.rs").write_text("pub fn other() {}\n", encoding="utf-8")
    else:
        (root / "src/lib.rs").write_text(head, encoding="utf-8")
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "head")
    return root, commit


def test_a_line_rustfmt_split_is_followed_into_head(tmp_path: Path) -> None:
    root, base = repository(tmp_path, BASE, BASE.replace("    if x {\n", "    if x\n    {\n"))
    moves = _verb().reanchor_all(root, base)
    assert list(moves) == [SPEC]
    _verb().REACH.resolve_site(moves[SPEC], root)


REFUSALS = {
    "a site that did not resolve at the base either": (
        BASE.replace("    if x {\n", "    if x {\n    // if x {\n"),
        BASE.replace("    if x {\n", "    if x\n    {\n"),
        "does not resolve at the base",
    ),
    "a function removed at HEAD": (BASE, None, "its function is gone from src/lib.rs at HEAD"),
    "anchored code duplicated at HEAD": (
        BASE,
        BASE.replace("    y\n}", "    if x {\n        return y + 1;\n    }\n    y\n}"),
        "holds 2 copies of it",
    ),
    "unchanged tokens no single line anchors uniquely": (
        BASE,
        BASE.replace("    y\n}", "    if x {\n        return y + 2;\n    }\n    y\n}"),
        "no single-line pattern anchors them uniquely",
    ),
}


@pytest.mark.parametrize("case", REFUSALS, ids=list(REFUSALS))
def test_a_site_the_verb_cannot_follow_is_refused_by_name_and_nothing_is_rewritten(tmp_path: Path, case: str) -> None:
    base_text, head_text, reason = REFUSALS[case]
    root, base = repository(tmp_path, base_text, head_text)
    sites = (root / SITES).read_bytes()
    with pytest.raises(SystemExit) as refused:
        _verb().reanchor_all(root, base)
    message = str(refused.value)
    assert "1 site(s) cannot be re-anchored, so nothing was rewritten" in message
    assert f"`{SPEC}`" in message and reason in message, message
    assert (root / SITES).read_bytes() == sites
    assert git(root, "status", "--porcelain") == "", "a refusal rewrites no file"
