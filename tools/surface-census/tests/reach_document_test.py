"""Ledger restatement and attribution refusals through real files and the recipe."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import reach_document
import residual_attribution_record as attribution

REPO = Path(__file__).resolve().parents[3]


def synthetic(root: Path) -> attribution.Attribution:
    for name, value in {
        "src/lib.rs": "pub fn generated() {}",
        "crates/crozier-e2e/tests/e2e.rs": 'const DEMO: Corpus = Corpus {\n    api: "demo",\n    unmatched: &["unmatched.py"],\n};\nfn demo_matches_fern_output() { assert_committed_corpus_matches(&DEMO); }\n',
        "tests/fixtures/demo/expected/model.py": "value = 1\n",
        "tests/fixtures/corpus-sources/demo/openapi.yml": "openapi: 3.0.3\n",
    }.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
    (root / attribution.RECORD).parent.mkdir(parents=True, exist_ok=True)
    golden, inputs = attribution.fingerprints(root, "demo")
    return attribution.Attribution("feature", "demo", ["model.py"], [], golden, inputs)


def test_attribution_round_trips_and_refuses_missing_or_changed_inputs(tmp_path: Path) -> None:
    row = synthetic(tmp_path)
    attribution.write(tmp_path, {row.key: row})
    saved = (tmp_path / attribution.RECORD).read_bytes()
    (tmp_path / attribution.RECORD).write_text("{broken", encoding="utf-8")
    with pytest.raises(ValueError, match="residual-attribution.json: cannot read attribution"):
        attribution.read(tmp_path)
    (tmp_path / attribution.RECORD).write_bytes(saved)
    loaded = attribution.read(tmp_path)
    assert attribution.require(tmp_path, row.key, row.fixture, loaded) == row
    attribution.write(tmp_path, loaded)
    assert (tmp_path / attribution.RECORD).read_bytes() == saved
    assert row.cell() == "| `feature` | `demo` | `model.py` | `byte-matched` |\n"
    for key in ("feature", "missing"):
        if key == "feature":
            (tmp_path / "src/lib.rs").write_text("pub fn changed() {}", encoding="utf-8")
        with pytest.raises(ValueError) as failure:
            attribution.require(tmp_path, key, "demo", loaded)
        assert key in str(failure.value)
        assert ("stale residual attribution" if key == "feature" else "no residual attribution") in str(failure.value)
        assert "just residual-attribution" in str(failure.value)
    # Changing only the unmatched registry must invalidate its classification.
    (tmp_path / "src/lib.rs").write_text("pub fn generated() {}", encoding="utf-8")
    registry = tmp_path / "crates/crozier-e2e/tests/e2e.rs"
    original_registry = registry.read_text(encoding="utf-8")
    registry.write_text(original_registry.replace("unmatched.py", "other.py"), encoding="utf-8")
    with pytest.raises(ValueError, match="feature: stale residual attribution"):
        attribution.require(tmp_path, row.key, row.fixture, loaded)
    registry.write_text(original_registry, encoding="utf-8")
    # Adding any discovered config is a changed generation input, even when
    # the previously measured tree had no config file.
    for filename in attribution.CONFIG_NAMES:
        config = tmp_path / filename
        config.write_text("client_class: ChangedClient\n", encoding="utf-8")
        with pytest.raises(ValueError, match="feature: stale residual attribution"):
            attribution.require(tmp_path, row.key, row.fixture, loaded)
        config.unlink()
    # Golden output is an independent content pin as well.
    (tmp_path / "src/lib.rs").write_text("pub fn generated() {}", encoding="utf-8")
    (tmp_path / "tests/fixtures/demo/expected/model.py").write_text("value = 2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="feature: stale residual attribution"):
        attribution.require(tmp_path, row.key, row.fixture, loaded)


@pytest.mark.parametrize("anchor", ["golden rows rest on one document", "golden rows reach every handling site"])
def test_a_missing_summary_anchor_is_refused(anchor: str) -> None:
    with pytest.raises(ValueError, match="restore exactly one summary.*just census-repin"):
        reach_document.summary("missing anchor", rf"\*\*\d+\*\* {anchor}", "replacement", anchor)


def test_a_missing_ownership_source_is_refused_without_inventing_boundaries(tmp_path: Path) -> None:
    text = (
        (REPO / reach_document.INDEX)
        .read_text(encoding="utf-8")
        .replace("#### The rows this measurement's first pass owned", "missing ownership source", 1)
    )
    with pytest.raises(ValueError, match="restore exactly one ownership source.*just census-repin"):
        reach_document.render(tmp_path, text, [], set(), set(), set(), {}, set())


@pytest.mark.parametrize("fault", ["boolean-version", "string-version", "future-version", "unknown-root-field"])
def test_record_versions_and_root_fields_are_validated(tmp_path: Path, fault: str) -> None:
    path = tmp_path / attribution.RECORD
    path.parent.mkdir(parents=True)
    payload: dict[str, object] = {"version": 1, "rows": []}
    match fault:
        case "boolean-version":
            payload["version"] = True
        case "string-version":
            payload["version"] = "1"
        case "future-version":
            payload["version"] = 2
        case "unknown-root-field":
            payload["unrecognized"] = "would be lost on publication"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="unsupported record.*just residual-attribution"):
        attribution.read(tmp_path)


def test_content_digest_uses_canonical_relative_path_order(tmp_path: Path) -> None:
    files = {"src/AGENTS.md": b"upper", "src/a.rs": b"lower"}
    expected = hashlib.sha256()
    for name in sorted(files):
        path = tmp_path / name
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(files[name])
        for value in (name.encode(), files[name]):
            expected.update(len(value).to_bytes(8, "big"))
            expected.update(value)
    assert attribution.content_digest(tmp_path, [tmp_path / name for name in reversed(files)]) == expected.hexdigest()


def test_attribution_config_inputs_match_rust_discovery_names() -> None:
    source = (REPO / "src/settings.rs").read_text(encoding="utf-8")
    declaration = re.search(r"pub const CONFIG_NAMES:.*?=\s*&\[(.*?)\];", source, re.S)
    assert declaration is not None
    assert tuple(re.findall(r'"([^"\n]+)"', declaration[1])) == attribution.CONFIG_NAMES


@pytest.mark.parametrize("fault", ["duplicate-matched", "duplicate-unmatched", "overlap"])
def test_attribution_files_refuse_duplicate_or_contradictory_classifications(tmp_path: Path, fault: str) -> None:
    row = synthetic(tmp_path)
    attribution.write(tmp_path, {row.key: row})
    path = tmp_path / attribution.RECORD
    saved = path.read_text(encoding="utf-8")
    payload = json.loads(saved)
    raw = payload["rows"][0]
    if fault == "duplicate-matched":
        raw["byte_matched"] *= 2
    elif fault == "duplicate-unmatched":
        raw["unmatched"] = ["other.py", "other.py"]
    else:
        raw["unmatched"] = raw["byte_matched"][:]
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="feature: .*attribution files.*just residual-attribution"):
        attribution.read(tmp_path)
    path.write_text(saved, encoding="utf-8")
    assert attribution.read(tmp_path) == {row.key: row}
