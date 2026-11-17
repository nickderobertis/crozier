#!/usr/bin/env python3
"""`tools/surface-census/residual-attribution.py`, run for real, against the table
it feeds.

The coverage report's residual-attribution table names, for every `golden` row
resting only on goldens that declare an `unmatched` residual, which of the
witness's files byte-match and which stay an open gap. The script measures that
by generating every such witness twice with the built `crozier` and formatting
with `ruff`, so this suite needs both: `crozier:build` runs before it, and a
missing binary or `ruff` fails it with the command that supplies it. The
table's offline shape checks are `tools/surface-census/tests/surface_census_test.py`'s.
"""

from __future__ import annotations

import contextlib
import dataclasses
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools" / "surface-census"))
sys.path.insert(0, str(REPO / "tools" / "surface-census" / "tests"))

from surface_census_test import residual_attributions  # noqa: E402 - sys.path must name its directory first

SCRIPT = REPO / "tools" / "surface-census" / "residual-attribution.py"
BINARY = REPO / "target" / "debug" / ("crozier.exe" if os.name == "nt" else "crozier")


class ResidualAttributionTests(unittest.TestCase):
    def test_the_residual_attribution_table_is_the_scripts_own_output(self) -> None:
        self.assertTrue(BINARY.is_file(), f"no {BINARY.relative_to(REPO)}; run `just nx run crozier:build`")
        self.assertIsNotNone(shutil.which("ruff"), "no ruff on PATH; install it with `just bootstrap`")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=1800,
            encoding="utf-8",
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        measured = {
            row["key"]: (row["fixture"], row["byte_matched"], row["unmatched"])
            for row in map(json.loads, completed.stdout.splitlines())
        }
        table = residual_attributions(REPO)
        self.assertEqual(set(table), set(measured))
        for key, (witness, files, gaps, verdict) in table.items():
            with self.subTest(key=key):
                fixture, matched, unmatched = measured[key]
                self.assertEqual(witness, fixture)
                self.assertEqual(sorted(files), sorted(matched))
                self.assertEqual(
                    sorted(gaps),
                    sorted(unmatched),
                    f"{key}: every `unmatched` file it moves is an open gap the table names",
                )
                expected = "split" if matched and unmatched else "byte-matched" if matched else "open gap"
                self.assertEqual(expected, verdict)

    def test_supplemental_null_proof_closes_only_the_approved_feature(self) -> None:
        commands = (
            [sys.executable, str(SCRIPT), "--key", "schema-example-null"],
            [sys.executable, str(SCRIPT), "--key", "schema-example-null", "--real-witnesses-only"],
        )
        closed, original = [
            subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=1800, encoding="utf-8")
            for command in commands
        ]
        self.assertEqual(0, closed.returncode, closed.stderr)
        self.assertEqual("", closed.stdout)
        self.assertEqual(0, original.returncode, original.stderr)
        measured = json.loads(original.stdout)
        self.assertEqual("schema-example-null", measured["key"])
        self.assertEqual([], measured["byte_matched"])
        self.assertEqual([], measured["unmatched"])


class AMissingWitnessSource(unittest.TestCase):
    def test_a_case_whose_witness_has_no_committed_source_names_the_fix(self) -> None:
        """The script's own refusal, before it builds anything over a source that is not there."""
        spec = importlib.util.spec_from_file_location("residual_attribution_missing", SCRIPT)
        assert spec is not None and spec.loader is not None
        # The script's globals are reassigned below, which a plain `ModuleType` does not declare.
        module: Any = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.CROZIER = Path(sys.executable)
        module.CASES = {"some-row": ("no-such-witness", lambda document: 1)}
        if shutil.which("ruff") is None:
            self.fail("no ruff on PATH; install it with `just bootstrap`")
        with self.assertRaises(SystemExit) as refused, contextlib.redirect_stdout(io.StringIO()):
            module.main([])
        self.assertIn("some-row's witness no-such-witness has no committed source", str(refused.exception))
        self.assertIn("`just lint-corpus-sources` names what is missing", str(refused.exception))


def test_record_publication_runs_the_cli_and_preserves_unselected_rows(tmp_path: Path) -> None:
    """The real binary measures a small document; only the selected record changes."""
    for directory in ("src", "templates", "assets"):
        shutil.copytree(REPO / directory, tmp_path / directory)
    for name in (
        "Cargo.toml",
        "Cargo.lock",
        "rust-toolchain.toml",
        ".ruff-version",
        ".cargo/config.toml",
        "pyproject.toml",
    ):
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / name, target)
    scripts = tmp_path / "tools/surface-census"
    scripts.mkdir(parents=True)
    for source in SCRIPT.parent.glob("*.py"):
        shutil.copy2(source, scripts / source.name)
    corpus = tmp_path / "tools/corpus"
    corpus.mkdir()
    shutil.copy2(REPO / "tools/corpus/corpus_remote_ref_pins.py", corpus)
    binary = tmp_path / "target/debug" / BINARY.name
    binary.parent.mkdir(parents=True)
    shutil.copy2(BINARY, binary)
    document = tmp_path / "tests/fixtures/corpus-sources/webflow-v2/openapi.json"
    document.parent.mkdir(parents=True)
    document.write_text(
        json.dumps(
            {
                "openapi": "3.1.0",
                "info": {"title": "Record", "version": "1"},
                "paths": {},
                "components": {"schemas": {"Thing": {"type": "object", "properties": {"value": True}}}},
            }
        ),
        encoding="utf-8",
    )
    golden = tmp_path / "tests/fixtures/webflow-v2/expected"
    generated = subprocess.run(
        [
            str(binary),
            "generate",
            "--spec",
            str(document),
            "--output",
            str(golden),
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert generated.returncode == 0, generated.stderr
    registry = tmp_path / "crates/crozier-e2e/tests/e2e.rs"
    registry.parent.mkdir(parents=True)
    registry.write_text(
        'const DEMO: Corpus = Corpus {\n    api: "webflow-v2",\n'
        '    unmatched: &["src/fern/types/thing.py"],\n};\n'
        "fn demo_matches_fern_output() { assert_committed_corpus_matches(&DEMO); }\n",
        encoding="utf-8",
    )
    record = tmp_path / "docs/openapi-surface/residual-attribution.json"
    record.parent.mkdir(parents=True)
    argv = [sys.executable, str(scripts / SCRIPT.name), "--key", "boolean-schema-true", "--write-record"]
    record.write_text("{broken", encoding="utf-8")
    refused = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert refused.returncode != 0
    assert "residual-attribution.json: cannot read attribution" in refused.stderr
    assert "just residual-attribution" in refused.stderr
    assert "Traceback" not in refused.stderr
    assert record.read_text(encoding="utf-8") == "{broken"
    kept = {
        "key": "unselected",
        "fixture": "other",
        "byte_matched": [],
        "unmatched": [],
        "golden_digest": "0" * 64,
        "inputs_digest": "0" * 64,
    }
    record.write_text(json.dumps({"version": 1, "rows": [kept]}), encoding="utf-8")
    run = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert run.returncode == 0, run.stderr
    published = json.loads(record.read_text(encoding="utf-8"))
    assert published["version"] == 1
    assert next(row for row in published["rows"] if row["key"] == "unselected") == kept
    assert run.stdout == "residual-attribution: wrote docs/openapi-surface/residual-attribution.json\n"
    selected = next(row for row in published["rows"] if row["key"] == "boolean-schema-true")
    assert selected["fixture"] == "webflow-v2"
    assert selected["byte_matched"] == []
    assert selected["unmatched"] == ["src/fern/types/thing.py"]
    assert len(selected["golden_digest"]) == len(selected["inputs_digest"]) == 64
    diagnostic = subprocess.run(argv[:-1], cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert diagnostic.returncode == 0, diagnostic.stderr
    measured = json.loads(diagnostic.stdout)
    assert {name: selected[name] for name in measured} == measured
    import residual_attribution_record as record_model

    loaded = record_model.read(tmp_path)
    record_model.require(tmp_path, selected["key"], selected["fixture"], loaded)
    reader = scripts / "openapi-surface-census.py"
    reader.write_bytes(reader.read_bytes() + b"\n# A changed measurement reader.\n")
    with pytest.raises(ValueError, match="boolean-schema-true: stale residual attribution"):
        record_model.require(tmp_path, selected["key"], selected["fixture"], loaded)


def linked_repository(root: Path, *written: str) -> Path:
    """`root` as this checkout: every entry linked back to it except the scripts and `written`.

    The scripts are copied so they take `root` as their repository; each path in
    `written` (and every directory above it) is a real copy, so what the command
    under test writes lands here and never through a link into this checkout.
    The whole-tree proof gate reads far more than a test could copy. `target` is
    linked too, so a `cargo build` there reuses this checkout's built dependencies.
    """
    copied = {"tools/surface-census", *written}

    def stage(source: Path, target: Path) -> None:
        relative = source.relative_to(REPO).as_posix()
        if relative in copied and source.is_dir():
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__"))
        elif relative in copied:
            shutil.copy2(source, target)
        elif any(path.startswith(relative + "/") for path in copied):
            target.mkdir()
            for child in source.iterdir():
                stage(child, target / child.name)
        elif relative not in {".git", ".venv", ".local"}:
            target.symlink_to(source, target_is_directory=source.is_dir())

    for child in REPO.iterdir():
        stage(child, root / child.name)
    return root


def test_a_closed_key_leaves_the_record_when_it_is_rewritten(tmp_path: Path) -> None:
    """Issue #837: a key the supplemental proof gate closes is pruned from the saved record."""
    if shutil.which("ruff") is None:
        pytest.fail("no ruff on PATH; install it with `just bootstrap`")
    assert BINARY.is_file(), f"no {BINARY.relative_to(REPO)}; run `just nx run crozier:build`"
    try:
        root = linked_repository(tmp_path, "docs/openapi-surface/residual-attribution.json")
    except OSError as error:
        pytest.skip(f"this host cannot create symbolic links ({error}); the linux and macos lanes run it")
    import residual_attribution_record as record_model

    proofs = (REPO / "docs/openapi-surface/residual-handwritten.toml").read_text(encoding="utf-8")
    assert 'key = "schema-example-null"' in proofs, "the committed supplemental proof this case reads moved"
    path = root / record_model.RECORD
    saved = json.loads(path.read_text(encoding="utf-8"))
    stale = {
        "key": "schema-example-null",
        "fixture": "webflow-v2",
        "byte_matched": [],
        "unmatched": [],
        "golden_digest": "0" * 64,
        "inputs_digest": "0" * 64,
    }
    path.write_text(json.dumps({"version": 1, "rows": [*saved["rows"], stale]}), encoding="utf-8")
    # A key no case measures any more (its row survives from an earlier CASES).
    obsolete = {**stale, "key": "retired-residual-key"}
    script = root / "tools/surface-census" / SCRIPT.name
    # A scoped rewrite and a whole-population one: each prunes the closed key;
    # only the whole-population one, which rebuilds every row, drops the retired key.
    for argv, kept in (
        (["--key", "boolean-schema-true"], ["boolean-schema-true", "retired-residual-key"]),
        (["--real-witnesses-only"], ["boolean-schema-true"]),
    ):
        with_stale = json.loads(path.read_text(encoding="utf-8"))
        with_stale["rows"] = [row for row in with_stale["rows"] if row["key"] not in (stale["key"], obsolete["key"])]
        with_stale["rows"] += [stale, obsolete]
        path.write_text(json.dumps(with_stale), encoding="utf-8")
        run = subprocess.run(
            [sys.executable, str(script), *argv, "--write-record"],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=1800,
            encoding="utf-8",
        )
        assert run.returncode == 0, (argv, run.stderr)
        rows = json.loads(path.read_text(encoding="utf-8"))["rows"]
        assert [row["key"] for row in rows] == kept, argv
        record_model.require(root, "boolean-schema-true", "webflow-v2", record_model.read(root))


def test_a_record_is_never_rewritten_over_a_failing_supplemental_proof(tmp_path: Path) -> None:
    """Even measuring the real witnesses only, `--write-record` first holds the
    supplemental proofs to their gate, and a failing one leaves the record as it was."""
    if shutil.which("ruff") is None:
        pytest.fail("no ruff on PATH; install it with `just bootstrap`")
    try:
        root = linked_repository(
            tmp_path,
            "docs/openapi-surface/residual-attribution.json",
            "docs/openapi-surface/residual-handwritten.toml",
        )
    except OSError as error:
        pytest.skip(f"this host cannot create symbolic links ({error}); the linux and macos lanes run it")
    record = root / "docs/openapi-surface/residual-attribution.json"
    proofs = root / "docs/openapi-surface/residual-handwritten.toml"
    saved, valid = record.read_bytes(), proofs.read_text(encoding="utf-8")
    assert 'fixture = "harbor-signal-null"' in valid, "the committed supplemental proof this case breaks moved"
    proofs.write_text(valid.replace('fixture = "harbor-signal-null"', 'fixture = "no-such-fixture"'), encoding="utf-8")
    refused = subprocess.run(
        [sys.executable, str(root / "tools/surface-census" / SCRIPT.name), "--real-witnesses-only", "--write-record"],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=600,
        encoding="utf-8",
    )
    assert refused.returncode != 0
    assert refused.stderr.startswith("residual-attribution: "), refused.stderr
    assert "residual-handwritten.toml `schema-example-null`: its fixture needs the matching" in refused.stderr
    assert record.read_bytes() == saved, "a refused rewrite leaves the saved record"


def test_a_merge_conflicted_record_is_regenerated_from_the_merged_tree(tmp_path: Path) -> None:
    """Issue #832: `just census-repin` resolves a conflicted attribution record by re-measuring it."""
    if shutil.which("ruff") is None:
        pytest.fail("no ruff on PATH; install it with `just bootstrap`")
    try:
        root = linked_repository(
            tmp_path,
            "docs/openapi-surface/residual-attribution.json",
            "docs/openapi-surface-coverage.md",
            "scripts/census-python.sh",
        )
    except OSError as error:
        pytest.skip(f"this host cannot create symbolic links ({error}); the linux and macos lanes run it")
    import residual_attribution_record as record_model

    # The verb stops at its interpreter selector, after the merge and the
    # restatement that validates the record, and before any measurement.
    (root / "scripts/census-python.sh").write_text("exit 7\n", encoding="utf-8")

    def git(*args: str) -> str:
        return subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    git("init", "-qb", "main")
    git("config", "core.autocrlf", "false")
    # The merge and the verb's own merge commit run without `-c`: a host with
    # no global identity (a CI runner) needs the repository's.
    git("config", "user.name", "t")
    git("config", "user.email", "t@t")
    git("add", "-A")
    git("commit", "-qm", "the measured tree")
    path = root / record_model.RECORD
    saved = json.loads(path.read_text(encoding="utf-8"))

    def digest(fill: str) -> None:
        rows = [dict(row, inputs_digest=fill * 64) for row in saved["rows"]]
        path.write_text(json.dumps({"version": 1, "rows": rows}, indent=2) + "\n", encoding="utf-8")

    git("checkout", "-qb", "side")
    digest("1")
    git("commit", "-qam", "side's measurement")
    git("checkout", "-q", "main")
    digest("2")
    git("commit", "-qam", "main's measurement")
    main, side = git("rev-parse", "main"), git("rev-parse", "side")
    merge = subprocess.run(["git", "merge", "-q", "side"], cwd=root, capture_output=True, text=True)
    assert merge.returncode != 0 and "<<<<<<<" in path.read_text(encoding="utf-8")
    conflicted = path.read_bytes()

    def without(tool: str) -> str:
        """PATH with every directory holding `tool` dropped, keeping `git` reachable."""
        kept = os.pathsep.join(
            directory
            for directory in os.environ["PATH"].split(os.pathsep)
            if not (Path(directory) / (f"{tool}.exe" if os.name == "nt" else tool)).exists()
        )
        found = shutil.which("git")
        if shutil.which("git", path=kept) is None and found is not None:
            shim = tmp_path / f"git-without-{tool}"
            shim.mkdir(exist_ok=True)
            (shim / Path(found).name).symlink_to(found)
            kept = os.pathsep.join((str(shim), kept))
        return kept

    # A regeneration that cannot start (no `cargo` to build crozier) is refused
    # the same way: the conflicted bytes are put back and the merge stays open.
    unstarted = subprocess.run(
        [sys.executable, str(root / "tools/surface-census/census-repin.py")],
        cwd=root,
        env=dict(os.environ, PATH=without("cargo")),
        capture_output=True,
        text=True,
        timeout=1800,
        encoding="utf-8",
    )
    assert unstarted.returncode != 0
    assert "is regenerated by building crozier, which could not start" in unstarted.stderr, unstarted.stderr
    assert "run `just bootstrap`, then re-run `just census-repin`" in unstarted.stderr
    assert "Traceback" not in unstarted.stderr
    assert (root / git("rev-parse", "--git-path", "MERGE_HEAD")).is_file()
    assert path.read_bytes() == conflicted, "the conflicted record is restored byte for byte"
    # A regeneration that cannot run refuses, naming why, and leaves the merge
    # uncommitted for a rerun: here `ruff`, which the measurement needs, is absent.
    blocked = subprocess.run(
        [sys.executable, str(root / "tools/surface-census/census-repin.py")],
        cwd=root,
        env=dict(os.environ, PATH=without("ruff")),
        capture_output=True,
        text=True,
        timeout=1800,
        encoding="utf-8",
    )
    assert blocked.returncode != 0
    assert "re-measuring the residual attribution failed" in blocked.stderr, blocked.stderr
    assert "`ruff` is not on PATH" in blocked.stderr and "the merge is left uncommitted" in blocked.stderr
    assert (root / git("rev-parse", "--git-path", "MERGE_HEAD")).is_file()
    assert "<<<<<<<" in path.read_text(encoding="utf-8"), "the conflict is left for the rerun to resolve"
    run = subprocess.run(
        [sys.executable, str(root / "tools/surface-census/census-repin.py"), "--verbose"],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=1800,
        encoding="utf-8",
    )
    assert "is not derived content" not in run.stderr, run.stderr
    assert "census-repin: resolved 1 derived conflict hunk(s) and committed the merge" in run.stderr, run.stderr
    assert "interpreter selector scripts/census-python.sh" in run.stderr, run.stderr
    assert set(git("rev-list", "--parents", "-1", "HEAD").split()[1:]) == {main, side}
    regenerated = record_model.read(root)
    assert set(regenerated) == {row["key"] for row in saved["rows"]}
    for row in regenerated.values():
        assert row.inputs_digest not in ("1" * 64, "2" * 64)
        record_model.require(root, row.key, row.fixture, regenerated)


def test_a_version_only_release_keeps_the_saved_attribution_valid(tmp_path: Path) -> None:
    """Issue #831: bumping only crozier's own version leaves `just census-repin` accepting the record."""
    if shutil.which("ruff") is None:
        pytest.fail("no ruff on PATH; install it with `just bootstrap`")
    try:
        root = linked_repository(
            tmp_path,
            "docs/openapi-surface/residual-attribution.json",
            "docs/openapi-surface-coverage.md",
            "scripts/census-python.sh",
            "Cargo.toml",
            "Cargo.lock",
        )
    except OSError as error:
        pytest.skip(f"this host cannot create symbolic links ({error}); the linux and macos lanes run it")
    # The verb stops at its interpreter selector, after the restatement that
    # validates the record and before any measurement.
    (root / "scripts/census-python.sh").write_text("exit 7\n", encoding="utf-8")
    measured = subprocess.run(
        [sys.executable, str(root / "tools/surface-census" / SCRIPT.name), "--write-record"],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=1800,
        encoding="utf-8",
    )
    assert measured.returncode == 0, measured.stderr

    def git(*args: str) -> None:
        subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=root, check=True, capture_output=True
        )

    def repin() -> subprocess.CompletedProcess[str]:
        git("add", "-A")
        git("commit", "-qm", "a change")
        return subprocess.run(
            [sys.executable, str(root / "tools/surface-census/census-repin.py")],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=600,
            encoding="utf-8",
        )

    git("init", "-qb", "main")
    git("config", "core.autocrlf", "false")
    import residual_attribution_record as record_model

    # A record saved before this change hashed the version line as it read; it
    # stays valid for exactly the tree it measured.
    record = root / record_model.RECORD
    neutral = record.read_bytes()
    current = record_model.fingerprints(root, "webflow-v2")
    [legacy] = record_model.accepted_fingerprints(root, "webflow-v2") - {current}
    saved = record_model.read(root)
    record_model.write(
        root, {key: dataclasses.replace(row, inputs_digest=legacy.inputs_digest) for key, row in saved.items()}
    )
    unchanged = repin()
    assert "stale residual attribution" not in unchanged.stderr, unchanged.stderr
    assert "interpreter selector scripts/census-python.sh" in unchanged.stderr, unchanged.stderr
    manifest, lock = root / "Cargo.toml", root / "Cargo.lock"
    version = re.search(r'(?m)^version = "([^"]+)"', manifest.read_text(encoding="utf-8"))
    assert version is not None
    released = version[1] + "-released"
    manifest.write_text(
        manifest.read_text(encoding="utf-8").replace(f'version = "{version[1]}"', f'version = "{released}"', 1),
        encoding="utf-8",
        newline="\n",  # a release edits the version alone; Windows' default CRLF would rewrite every line
    )
    entry = f'name = "crozier"\nversion = "{version[1]}"\n'
    assert entry in lock.read_text(encoding="utf-8")
    lock.write_text(
        lock.read_text(encoding="utf-8").replace(entry, entry.replace(version[1], released)),
        encoding="utf-8",
        newline="\n",
    )
    legacy_bumped = repin()
    assert "boolean-schema-true: stale residual attribution" in legacy_bumped.stderr, legacy_bumped.stderr
    record.write_bytes(neutral)
    bumped = repin()
    assert "stale residual attribution" not in bumped.stderr, bumped.stderr
    assert "interpreter selector scripts/census-python.sh" in bumped.stderr, bumped.stderr
    # A dependency's version is still a generator input.
    dependency = re.search(r'(?m)^name = "clap"\nversion = "([^"]+)"', lock.read_text(encoding="utf-8"))
    assert dependency is not None
    lock.write_text(
        lock.read_text(encoding="utf-8").replace(dependency[0], dependency[0] + "-moved", 1),
        encoding="utf-8",
        newline="\n",
    )
    moved = repin()
    assert "boolean-schema-true: stale residual attribution" in moved.stderr, moved.stderr


if __name__ == "__main__":
    unittest.main()
