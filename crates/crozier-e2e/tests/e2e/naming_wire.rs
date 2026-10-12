//! The client naming, request encoding and enum-mode shapes driven through the
//! real binary beyond the hand-written gate: the `python_enums` measurement
//! cases under [`NAMING_WIRE_DIR`], and, for each shape, the proof that an
//! unexplained byte beside the matched one still fails the comparison.
//!
//! The hand-written fixtures of these shapes (`gallery-plaque-groups`,
//! `transcript-format-part`, `ledger-batch-upload`, `survey-field-selector`) are
//! held whole, in both enum modes, by `handwritten_fixtures_match_fern_goldens`
//! and `literals_mode_measurements_match_fern`; the reordered root imports are
//! held by every registered corpus golden that re-exports a tag subpackage's
//! types. This module adds only what those gates do not already say.

use std::path::{Path, PathBuf};

use crozier::departures::Context;
use crozier::parity;

use super::literals_mode::LITERALS_MODE_DIR;
use super::{
    copy_dir, corpus_command, departure_ledger, golden_path, golden_tree_failures, probe_command,
    repo_root, ALMA_FRANCE, HANDWRITTEN_DIR,
};

/// Where the `python_enums` measurement cases live; see its README.
pub(super) const NAMING_WIRE_DIR: &str = "docs/fern-measurements/naming-wire";

/// The tree each case holds: Fern's complete `python_enums` output for the
/// literals-mode case of the same name, whose document it carries no copy of.
const TREE: &str = "fern-expected";

/// Crozier's output over `spec`, compared whole with the Fern tree `expected`,
/// every departure held to `golden`'s ledger rows.
fn tree_failures(key: &str, spec: &Path, golden: &str, expected: &Path) -> Vec<String> {
    let out = tempfile::tempdir().expect("crozier output tempdir");
    let result = probe_command(spec, out.path())
        .output()
        .expect("run crozier");
    if !result.status.success() {
        return vec![format!(
            "{key}: crozier failed over {}: {}",
            spec.display(),
            String::from_utf8_lossy(&result.stderr)
        )];
    }
    match departure_ledger().golden(golden, &[]) {
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

/// A case's document: the literals-mode case of the same name's.
fn case_spec(case: &str) -> PathBuf {
    repo_root()
        .join(LITERALS_MODE_DIR)
        .join(case)
        .join("openapi.yml")
}

// llmlint: ignore[expensive_tests_stay_behind_their_own_edge] Complete certified-tree comparisons join the existing crozier-e2e golden gate and its departure ledger; a separate target for only these measurements would split the repository's shared parity gate, whose deliberate tooling edges are recorded in crates/crozier-e2e/AGENTS.md.
#[test]
fn naming_wire_measurements_match_fern_under_python_enums() {
    let root = repo_root();
    let mut cases: Vec<String> = std::fs::read_dir(root.join(NAMING_WIRE_DIR))
        .expect("the measurement directory exists")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .collect();
    cases.sort();
    assert_eq!(
        cases,
        [
            "enum-extension-names-dropped-under-literals",
            "enum-header-params-stringified"
        ],
        "{NAMING_WIRE_DIR}: every case is a literals-mode document's python_enums tree"
    );
    let failures: Vec<String> = cases
        .iter()
        .flat_map(|case| {
            let spec = case_spec(case);
            assert!(spec.is_file(), "{case}: no literals-mode document");
            let expected = root.join(NAMING_WIRE_DIR).join(case).join(TREE);
            tree_failures(case, &spec, &golden_path(&expected), &expected)
        })
        .collect();
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// A committed Fern tree copied so a test may perturb it, with the golden its
/// ledger rows belong to and the document it was generated from.
fn fern_copy(tree: &Path, spec: PathBuf) -> (tempfile::TempDir, String, PathBuf) {
    let copy = tempfile::tempdir().expect("golden copy tempdir");
    copy_dir(tree, copy.path());
    (copy, golden_path(tree), spec)
}

fn handwritten_copy(fixture: &str) -> (tempfile::TempDir, String, PathBuf) {
    let root = repo_root().join(HANDWRITTEN_DIR).join(fixture);
    fern_copy(&root.join(TREE), root.join("openapi.yml"))
}

fn measurement_copy(case: &str) -> (tempfile::TempDir, String, PathBuf) {
    let tree = repo_root().join(NAMING_WIRE_DIR).join(case).join(TREE);
    fern_copy(&tree, case_spec(case))
}

/// Plant one unexplained byte; a `from` the golden no longer holds fails here,
/// so a regenerated golden cannot leave a negative case silently unperturbed.
fn perturb(tree: &Path, rel: &str, from: &str, to: &str) {
    let path = tree.join(rel);
    let text = std::fs::read_to_string(&path).expect("a committed Fern file");
    assert!(text.contains(from), "{rel} holds no `{from}`");
    std::fs::write(&path, text.replacen(from, to, 1)).expect("perturb the tree");
}

/// Each shape's tree matches as committed, and each perturbation — crozier's
/// former spelling of the shape, or a byte beside it — fails in the file it
/// lands in.
// llmlint: ignore[expensive_tests_stay_behind_their_own_edge] These negative cases exercise the same real-binary golden gate and ledger as their positive cases; keeping both in the existing crozier-e2e target holds unexplained mismatches to that shared boundary.
#[test]
fn naming_wire_shapes_fail_on_an_unexplained_byte() {
    type Copy = fn(&str) -> (tempfile::TempDir, String, PathBuf);
    type Perturbation<'a> = (&'a str, &'a str, &'a str);
    type Case<'a> = (&'a str, Copy, &'a [Perturbation<'a>]);
    let cases: [Case<'_>; 6] = [
        (
            "gallery-plaque-groups",
            handwritten_copy,
            &[
                ("reference.md", "## Galleryplaque\n", "## GalleryPlaque\n"),
                (
                    "src/fern/galleryplaque/raw_client.py",
                    "def show(",
                    "def gallery_plaque_show(",
                ),
                (
                    "src/fern/client.py",
                    "from .gallery_lighting.client import",
                    "from .gallerylighting.client import",
                ),
            ],
        ),
        (
            "transcript-format-part",
            handwritten_copy,
            &[
                (
                    "src/fern/transcripts/raw_client.py",
                    "\"format\": format,",
                    "\"format\": json.dumps(jsonable_encoder(format)) if format is not OMIT else OMIT,",
                ),
                (
                    "src/fern/transcripts/raw_client.py",
                    "\"margins\": json.dumps(jsonable_encoder(margins)) if margins is not OMIT else OMIT,",
                    "\"margins\": margins,",
                ),
            ],
        ),
        (
            "ledger-batch-upload",
            handwritten_copy,
            &[(
                "src/fern/entries/raw_client.py",
                "            headers={\n                \"content-type\": \"application/json\",\n            },\n",
                "",
            )],
        ),
        (
            "survey-field-selector",
            handwritten_copy,
            &[
                (
                    "src/fern/responses/types/list_responses_request_select_item.py",
                    "kwargs_: typing.Callable",
                    "kwargs: typing.Callable",
                ),
                (
                    "src/fern/responses/types/list_responses_request_select_item.py",
                    "json: typing.Callable",
                    "json_: typing.Callable",
                ),
            ],
        ),
        (
            "enum-header-params-stringified",
            measurement_copy,
            &[(
                "src/fern/trams/raw_client.py",
                "\"X-Shift\": shift.value if shift is not None else None,",
                "\"X-Shift\": str(shift) if shift is not None else None,",
            )],
        ),
        (
            "enum-extension-names-dropped-under-literals",
            measurement_copy,
            &[(
                "src/fern/types/relation.py",
                "    \"\"\"\n    The reading is under the threshold.\n    \"\"\"\n",
                "",
            )],
        ),
    ];
    for (case, copy, perturbations) in cases {
        let (tree, golden, spec) = copy(case);
        let check = |tree: &Path| tree_failures(case, &spec, &golden, tree);
        assert_eq!(check(tree.path()), Vec::<String>::new(), "{case}");
        for (rel, from, to) in perturbations {
            let (perturbed, _, _) = copy(case);
            perturb(perturbed.path(), rel, from, to);
            let failures = check(perturbed.path());
            assert!(
                failures.iter().any(|failure| failure.contains(rel)),
                "{case}: perturbing {rel} ({from:?}) was not reported: {failures:?}"
            );
        }
    }
}

/// `init-type-checking-import-order` over a registered golden whose tag
/// subpackages re-export types: crozier writes `from .client` and
/// `from .environment` ahead of `from .balance_transactions`, which Fern sorts
/// first. A name only Fern's `.types` statement imports leaves the moved window
/// a departure and the name a difference; a tag subpackage's statement moving,
/// or a moved statement importing another name, is no departure at all.
// llmlint: ignore[expensive_tests_stay_behind_their_own_edge] This registered-corpus comparison belongs to the existing crozier-e2e golden gate, where the positive departure and its negative name-set cases run against the same binary and catalog.
#[test]
fn reordered_root_imports_are_a_departure_only_beside_identical_statements() {
    let rel = "src/fern/__init__.py";
    let golden = repo_root().join("tests/fixtures/alma-france/expected");
    let out = tempfile::tempdir().expect("crozier output tempdir");
    let (mut command, _source) = corpus_command(&ALMA_FRANCE, out.path());
    command.assert().success();
    let crozier = std::fs::read_to_string(out.path().join(rel)).expect("crozier's root init");
    let fern = std::fs::read_to_string(golden.join(rel)).expect("Fern's root init");
    let context = Context::from_trees(&golden, out.path());
    let compare = |reference: &str| {
        parity::compare_file(&context, rel, &crozier, reference).expect("the rules run")
    };
    let departures = |compared: &parity::FileComparison| -> Vec<String> {
        compared
            .departures
            .iter()
            .map(|departure| departure.id.to_string())
            .collect()
    };

    let committed = compare(&fern);
    assert!(committed.matches(), "{:?}", committed.diff());
    assert_eq!(departures(&committed), ["init-type-checking-import-order"]);

    let types = "    from .types import (\n";
    assert!(fern.contains(types), "{rel} has no `.types` statement");
    let named = fern.replacen(types, &format!("{types}        AlmaExtraName,\n"), 1);
    let compared = compare(&named);
    assert_eq!(departures(&compared), ["init-type-checking-import-order"]);
    let diff = compared.diff().expect("the extra name stays a difference");
    assert!(
        diff.contains("AlmaExtraName") && !diff.contains("from .client"),
        "{diff}"
    );

    let moved = "    from .balance_transactions import ListbalancetransactionsResponse\n";
    let payments = "    from .payments import CreatePaymentRequestPayment, ListpaymentsResponse\n";
    assert!(fern.contains(moved) && fern.contains(payments));
    let swapped = named
        .replacen(moved, "", 1)
        .replacen(payments, &format!("{payments}{moved}"), 1);
    let compared = compare(&swapped);
    assert!(!compared.matches() && compared.departures.is_empty());

    let renamed = named.replacen(
        "ListbalancetransactionsResponse\n",
        "ListbalancetransactionsResponse, AlmaOtherName\n",
        1,
    );
    let compared = compare(&renamed);
    assert!(!compared.matches() && compared.departures.is_empty());
}
