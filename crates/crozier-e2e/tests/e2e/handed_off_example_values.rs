//! The worked-example value causes the fixture-only witness searches handed off,
//! each measured under [`AREA_DIR`] with a from-scratch document and the
//! certified pair's fresh tree, and held here through the real binary: crozier's
//! output byte-matches every committed tree (in literals mode too, where the
//! enum mode changes the worked call), the values a design-review ruling keeps
//! are what crozier writes, and an unexplained byte beside each kept value
//! still fails. `docs/fern-measurements/handed-off/example-values.tsv` records
//! each cause's verdict.

use std::path::{Path, PathBuf};

use super::{
    copy_dir, departure_ledger, golden_path, golden_tree_failures, probe_command, repo_root,
    walk_files, GoldenLedger,
};

/// Each cause's directory sits here under the record's own spelling of its name,
/// which `example-values.tsv` and the area README cite.
pub(super) const AREA_DIR: &str = "docs/fern-measurements/handed-off/example-values";

/// Every cause the triage record names, each a directory under [`AREA_DIR`].
const CAUSES: &[&str] = &[
    "R11",
    "R4",
    "example-enum-member",
    "example-float-repr",
    "example-matching-union-variant",
    "example-optional-members",
    "example-placeholder-shape",
    "example-value-source",
    "falsy-property-example",
    "map-body-media-example",
    "mistyped-scalar-example",
    "param-oneof-ref-and-const-example",
    "property-schema-examples-array",
    "schema-examples-array-parameter-value",
    "yaml-timestamp-parameter-example",
];

/// The causes whose worked call names an enum, so their literals-mode tree is
/// committed as an `expected-literals/` overlay of the cause's own tree.
const LITERALS: &[&str] = &[
    "example-enum-member",
    "example-matching-union-variant",
    "example-value-source",
    "param-oneof-ref-and-const-example",
];

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
pub(super) const MANIFEST: &str = ".crozier-overlay.json";

/// The literals overlay goldens this module compares, for the inventory of
/// compared goldens (each cause's own `fern-expected/` is found by directory).
pub(super) fn compared_overlays() -> Vec<String> {
    LITERALS
        .iter()
        .map(|cause| format!("{AREA_DIR}/{cause}/expected-literals/fern-expected"))
        .collect()
}

fn cause_dir(cause: &str) -> PathBuf {
    repo_root().join(AREA_DIR).join(cause)
}

/// A failing run is a failure message, not a panic, so one cause's refusal is
/// reported beside the other causes' differences.
fn generate(spec: &Path, flags: &[&str]) -> Result<tempfile::TempDir, String> {
    let out = tempfile::tempdir().expect("crozier output tempdir");
    let result = probe_command(spec, out.path())
        .args(flags)
        .output()
        .expect("run crozier");
    if result.status.success() {
        Ok(out)
    } else {
        Err(format!(
            "crozier failed over {}: {}",
            spec.display(),
            String::from_utf8_lossy(&result.stderr)
        ))
    }
}

/// crozier's output over `spec` compared whole with `expected`, every departure
/// held to `golden`'s ledger rows.
fn tree_failures(
    key: &str,
    spec: &Path,
    flags: &[&str],
    golden: &str,
    expected: &Path,
) -> Vec<String> {
    ledger_tree_failures(
        key,
        spec,
        flags,
        departure_ledger().golden(golden, &[]),
        expected,
    )
}

/// [`tree_failures`] for a tree whose ledger rows are not one golden's: a
/// literals overlay inherits its base's rows (see [`literals_ledger`]).
fn ledger_tree_failures(
    key: &str,
    spec: &Path,
    flags: &[&str],
    ledger: Result<GoldenLedger, Vec<String>>,
    expected: &Path,
) -> Vec<String> {
    let out = match generate(spec, flags) {
        Ok(out) => out,
        Err(failure) => return vec![format!("{key}: {failure}")],
    };
    match ledger {
        Ok(ledger) => golden_tree_failures(
            key,
            &spec.display().to_string(),
            &ledger,
            expected,
            out.path(),
        ),
        Err(failures) => failures,
    }
}

/// A literals overlay's ledger rows: its own for the files it carries, its
/// cause's `fern-expected/` rows for every file it inherits.
fn literals_ledger(cause: &str) -> Result<GoldenLedger, Vec<String>> {
    let overlay = cause_dir(cause)
        .join("expected-literals")
        .join("fern-expected");
    let own = departure_ledger().golden(&golden_path(&overlay), &[])?;
    let inherited =
        departure_ledger().golden(&golden_path(&cause_dir(cause).join("fern-expected")), &[])?;
    let removed = overlay_removed(&overlay);
    let files = walk_files(&overlay)
        .into_iter()
        .filter(|rel| rel != MANIFEST)
        .collect();
    Ok(own.inherit(inherited, files, &removed))
}

/// The files an overlay's manifest says the literals tree omits. A manifest
/// without a `removed` array of paths is malformed and fails the test rather
/// than standing for an overlay that removes nothing.
fn overlay_removed(overlay: &Path) -> Vec<String> {
    let path = overlay.join(MANIFEST);
    let manifest: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(&path)
            .unwrap_or_else(|error| panic!("{}: {error}", path.display())),
    )
    .unwrap_or_else(|error| panic!("{}: {error}", path.display()));
    manifest
        .get("removed")
        .and_then(serde_json::Value::as_array)
        .unwrap_or_else(|| panic!("{}: `removed` is not an array", path.display()))
        .iter()
        .map(|entry| {
            entry
                .as_str()
                .unwrap_or_else(|| panic!("{}: a `removed` entry is not a path", path.display()))
                .to_string()
        })
        .collect()
}

/// A cause's literals tree: its own `fern-expected/` minus the files the
/// overlay's manifest removes, with the overlay's files laid over it.
fn literals_tree(cause: &str) -> tempfile::TempDir {
    let dir = cause_dir(cause);
    let base = dir.join("fern-expected");
    let overlay = dir.join("expected-literals").join("fern-expected");
    let tree = tempfile::tempdir().expect("literals tree tempdir");
    copy_dir(&base, tree.path());
    for rel in overlay_removed(&overlay) {
        std::fs::remove_file(tree.path().join(rel)).expect("remove a file Fern omits");
    }
    for rel in walk_files(&overlay) {
        if rel != MANIFEST {
            let to = tree.path().join(&rel);
            std::fs::create_dir_all(to.parent().expect("a file has a parent")).expect("mkdir");
            std::fs::copy(overlay.join(&rel), to).expect("lay the overlay");
        }
    }
    tree
}

#[test]
fn every_handed_off_example_value_measurement_is_complete() {
    let mut directories: Vec<String> = std::fs::read_dir(repo_root().join(AREA_DIR))
        .expect("the measurement directory exists")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .collect();
    directories.sort();
    assert_eq!(
        directories, CAUSES,
        "{AREA_DIR}: every cause directory needs a CAUSES row"
    );
    for cause in CAUSES {
        let dir = cause_dir(cause);
        for part in ["openapi.yml", "README.md", "fern-expected/README.md"] {
            assert!(dir.join(part).is_file(), "{cause}: {part} is missing");
        }
    }
}

#[test]
fn handed_off_example_value_measurements_match_fern() {
    let mut failures = Vec::new();
    for cause in CAUSES {
        let dir = cause_dir(cause);
        let expected = dir.join("fern-expected");
        failures.extend(tree_failures(
            cause,
            &dir.join("openapi.yml"),
            &[],
            &golden_path(&expected),
            &expected,
        ));
    }
    // The float defect lived in crozier's JSON reading: the same document as
    // JSON is held to the same tree.
    let float = cause_dir("example-float-repr");
    let expected = float.join("fern-expected");
    failures.extend(tree_failures(
        "example-float-repr (JSON)",
        &float.join("openapi.json"),
        &[],
        &golden_path(&expected),
        &expected,
    ));
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

#[test]
fn handed_off_example_value_literals_overlays_match_fern() {
    let mut failures = Vec::new();
    for cause in LITERALS {
        let tree = literals_tree(cause);
        failures.extend(ledger_tree_failures(
            &format!("{cause} (literals)"),
            &cause_dir(cause).join("openapi.yml"),
            &["--enum-type", "literals"],
            literals_ledger(cause),
            tree.path(),
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// `reference.md` is the one writer that carries every worked call of a cause's
/// document, so the ruled lines are read there (the docstrings and README
/// carry the same values, held by the whole-tree comparison).
fn reference_lines(cause: &str) -> (String, String) {
    let dir = cause_dir(cause);
    let out = generate(&dir.join("openapi.yml"), &[]).unwrap_or_else(|failure| panic!("{failure}"));
    let read = |path: PathBuf| std::fs::read_to_string(path).expect("a reference.md");
    (
        read(dir.join("fern-expected/reference.md")),
        read(out.path().join("reference.md")),
    )
}

/// What crozier writes where a ruling keeps its value, beside the certified
/// pair's line, and where a repair now matches the pair.
#[test]
fn ruled_example_values_are_what_crozier_writes() {
    for (cause, fern, crozier) in [
        // Ruling 2 (falsy-property-example): the declared "" and 0.
        (
            "falsy-property-example",
            "    label=\"label\",",
            "    label=\"\",",
        ),
        (
            "falsy-property-example",
            "    depth_metres=1,",
            "    depth_metres=0,",
        ),
        (
            "falsy-property-example",
            "    survey_ref=\"X-Survey-Ref\",",
            "    survey_ref=\"\",",
        ),
        // Ruling 3 (yaml-timestamp-parameter-example): the unquoted timestamp.
        (
            "yaml-timestamp-parameter-example",
            "    since=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),",
            "    since=datetime.datetime.fromisoformat(\"2031-04-02T08:15:00+00:00\"),",
        ),
        (
            "yaml-timestamp-parameter-example",
            "    recorded_on=\"recordedOn\",",
            "    recorded_on=\"2031-04-01T06:00:00Z\",",
        ),
        // Ruling 5 (declared-examples-array): the examples array and map.
        (
            "schema-examples-array-parameter-value",
            "    lamp_id=\"lampId\",",
            "    lamp_id=\"lmp_8f2kq\",",
        ),
        (
            "R4",
            "    keeper_id=\"KPR-from-schema\",",
            "    keeper_id=\"KPR-from-map\",",
        ),
        // Ruling 2's principle: the enum's example member and the kept
        // example-value-source sub-rules.
        (
            "example-enum-member",
            "        AlertKind.ALL",
            "        AlertKind.BEACON_LIT",
        ),
        (
            "example-value-source",
            "    title=\"title\",",
            "    title=\"Lizard Point\",",
        ),
        (
            "example-value-source",
            "    scale=\"scale\",",
            "    scale=\"1:25000\",",
        ),
        (
            "example-value-source",
            "            match=\"match\",",
            "            match=[",
        ),
        (
            "example-value-source",
            "    harbour_slug=\"harbourSlug\",",
            "    harbour_slug=\"cornwall/porthleven\",",
        ),
    ] {
        let (fern_reference, crozier_reference) = reference_lines(cause);
        let has = |text: &str, line: &str| text.lines().any(|candidate| candidate == line);
        assert!(
            has(&fern_reference, fern),
            "{cause}: the certified pair's `{fern}`"
        );
        assert!(
            has(&crozier_reference, crozier),
            "{cause}: crozier's `{crozier}`"
        );
        assert!(
            !has(&crozier_reference, fern),
            "{cause}: crozier still writes `{fern}`"
        );
    }
    // Ruling 3 keeps an optional timestamp parameter the pair leaves out;
    // ruling 4 (minimal-worked-call) leaves out the two the pair omits, and
    // keeps one carrying a plain declared example, as the pair does.
    let (fern_timestamps, timestamps) = reference_lines("yaml-timestamp-parameter-example");
    assert!(
        !fern_timestamps.contains("as_of="),
        "the certified pair leaves an optional timestamp out"
    );
    assert!(timestamps
        .contains("    as_of=datetime.datetime.fromisoformat(\"2031-05-01T00:00:00+00:00\"),"));
    assert!(timestamps
        .contains("    until=datetime.datetime.fromisoformat(\"2031-04-03T08:15:00+00:00\"),"));
    let (fern_optional, crozier_optional) = reference_lines("example-optional-members");
    assert!(
        !crozier_optional.contains("observed_from="),
        "an unquoted examples-array timestamp leaves the call"
    );
    assert!(!fern_optional.contains("observed_from="));
    assert!(
        crozier_optional.contains("    lamp=\"lamp-east\","),
        "a quoted examples entry stays"
    );
    let (_, vessels) = reference_lines("R11");
    assert!(
        !vessels.contains("owners=") && !vessels.contains("hulls="),
        "{vessels}"
    );
    assert!(vessels.contains("    port=\"falmouth\","));
}

/// A copy of a cause's committed tree with one line changed: a `from` the tree
/// no longer holds fails here, so a regenerated tree cannot leave a negative
/// case silently unperturbed.
fn perturbed(cause: &str, rel: &str, from: &str, to: &str) -> tempfile::TempDir {
    let copy = tempfile::tempdir().expect("tree copy tempdir");
    copy_dir(&cause_dir(cause).join("fern-expected"), copy.path());
    let path = copy.path().join(rel);
    let text = std::fs::read_to_string(&path).expect("a committed Fern file");
    assert!(text.contains(from), "{cause}/{rel} holds no `{from}`");
    std::fs::write(&path, text.replacen(from, to, 1)).expect("perturb the tree");
    copy
}

/// Each declared-value departure explains only its own line: a different
/// placeholder on the certified side, or a changed line beside it, fails. A
/// missing document writes no SDK.
#[test]
fn declared_value_departures_hold_only_their_lines() {
    for (cause, rel, from, to) in [
        // declared-example-over-placeholder
        (
            "falsy-property-example",
            "reference.md",
            "    label=\"label\",",
            "    label=\"tag\",",
        ),
        (
            "falsy-property-example",
            "reference.md",
            "    harbour=\"harbour\",",
            "    harbour=\"north-basin\",\n    pier=\"pier\",",
        ),
        (
            "example-enum-member",
            "reference.md",
            "        AlertKind.ALL",
            "        AlertKind.BEACON_OUT",
        ),
        // unquoted-timestamp-parameter-example
        (
            "yaml-timestamp-parameter-example",
            "reference.md",
            "    recorded_on=\"recordedOn\",",
            "    recorded_on=\"recorded\",",
        ),
        // declared-examples-array-parameter-value
        (
            "schema-examples-array-parameter-value",
            "src/fern/lamps/client.py",
            "lamp_id=\"lampId\",",
            "lamp_id=\"lamp\",",
        ),
        (
            "R4",
            "reference.md",
            "    keeper_id=\"KPR-from-schema\",",
            "    keeper_id=\"KPR-other\",",
        ),
    ] {
        let tree = perturbed(cause, rel, from, to);
        let dir = cause_dir(cause);
        let golden = golden_path(&dir.join("fern-expected"));
        let failures = tree_failures(cause, &dir.join("openapi.yml"), &[], &golden, tree.path());
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains(&format!("{rel} differs"))),
            "{cause} {rel}: {failures:?}"
        );
    }
    let missing = tempfile::tempdir().expect("missing source tempdir");
    let out = missing.path().join("sdk");
    probe_command(&missing.path().join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicates::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document must write no SDK");
}
