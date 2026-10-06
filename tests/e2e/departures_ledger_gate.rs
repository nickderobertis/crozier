//! The departure ledger's contract, driven through the entry points the gates
//! use — [`load_departure_ledger`], then the tree comparisons — over a ledger,
//! goldens and crozier outputs each test authors itself in a scratch
//! repository. The real ledger's own checks are every golden comparison, the
//! load below, and [`compared_goldens_inventory_is_current`].

use std::collections::BTreeSet;
use std::path::Path;

use super::departures_ledger::{self, GoldenLedger, Ledger, Row};
use super::{
    assert_generated_tree_matches, compared_goldens, corpus_golden_ledger, golden_differences,
    golden_tree_failures, load_departure_ledger, Corpus, CORPORA, OPENFIGI, WEBFLOW_V2,
    WEBFLOW_V2_CROZIER_ONLY,
};

/// The directory, inside each case under the catalog's evidence directory, of
/// the Fern reference tree a departure's evidence holds.
pub const REFERENCE_TREE: &str = "fern-reference";

/// The authored golden most tests compare against, as a row names it.
const GOLDEN: &str = "docs/openapi-surface/authored-probes/demo/fern-expected";

/// The client wrapper both sides write.
const WRAPPER: &str = "core/client_wrapper.py";

/// Fern's client wrapper, comment-stripped as a golden is.
const FERN_WRAPPER: &str = "\nheaders = {\n    \"X-Fern-Language\": \"Python\",\n}\n";

/// crozier's client wrapper: its header comment, then its own header name.
const CROZIER_WRAPPER: &str =
    "# crozier\nheaders = {\n    \"X-Crozier-Language\": \"Python\",\n}\n";

/// A module both sides write identically.
const CLIENT: &str = "class Demo:\n    pass\n";

/// The row that records crozier's header departure in [`GOLDEN`].
fn wrapper_row(golden: &str) -> String {
    format!("{golden}\t{WRAPPER}\t3\tsdk-identity-header-prefix\n")
}

/// A ledger holding `rows`, after the header.
fn ledger_text(rows: &str) -> String {
    format!("{}\n{rows}", departures_ledger::HEADER)
}

/// The scratch repository's inventory: [`GOLDEN`] and the corpus and overlay
/// goldens the corpus-gate tests author, with no carve-out recorded.
const SCRATCH_INVENTORY: &str = r#"{
  "goldens": {
    "docs/openapi-surface/authored-probes/demo/fern-expected": {},
    "tests/fixtures/openfigi.com/expected": {},
    "tests/fixtures/openfigi.com/expected-literals": {
      "excluded": [".crozier-overlay.json"]
    },
    "tests/fixtures/webflow-v2/expected": {}
  }
}
"#;

/// A scratch repository holding `ledger`, the inventory, and [`GOLDEN`].
fn repository(ledger: &str) -> tempfile::TempDir {
    let root = tempfile::tempdir().expect("scratch repository");
    write(root.path(), departures_ledger::LEDGER, ledger);
    write(root.path(), departures_ledger::INVENTORY, SCRATCH_INVENTORY);
    golden(root.path(), GOLDEN);
    root
}

/// Fern's two files at `golden` under `root`.
fn golden(root: &Path, golden: &str) {
    write(root, &format!("{golden}/{WRAPPER}"), FERN_WRAPPER);
    write(root, &format!("{golden}/client.py"), CLIENT);
}

/// crozier's authored output tree, with its client wrapper `wrapper`.
fn output(wrapper: &str) -> tempfile::TempDir {
    let out = tempfile::tempdir().expect("authored crozier output");
    write(out.path(), WRAPPER, wrapper);
    write(out.path(), "client.py", CLIENT);
    out
}

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().expect("a file has a parent")).expect("mkdir");
    std::fs::write(path, text).expect("write authored file");
}

/// Load `root`'s ledger as every gate does and compare `out` to [`GOLDEN`]
/// through the probe, authored-probe and hand-written gates' comparison.
fn compare(root: &Path, out: &Path) -> Vec<String> {
    let ledger = loaded(root)
        .golden(GOLDEN, &[])
        .unwrap_or_else(|failures| panic!("{failures:?}"));
    golden_tree_failures(
        "demo",
        "the authored document",
        &ledger,
        &root.join(GOLDEN),
        out,
    )
}

/// `root`'s ledger, which must load.
fn loaded(root: &Path) -> Ledger {
    load_departure_ledger(root).unwrap_or_else(|failures| panic!("{failures:#?}"))
}

/// The failures loading the scratch repository `root`'s ledger, which the load
/// must refuse.
fn load_failures(root: &Path) -> Vec<String> {
    load_departure_ledger(root).expect_err("the ledger must be refused")
}

/// Assert exactly one failure, quoting `row` and saying `says`.
fn assert_names(failures: &[String], row: &str, says: &str) {
    assert!(
        failures.len() == 1 && failures[0].contains(row) && failures[0].contains(says),
        "expected one failure quoting {row:?} and saying {says:?}: {failures:#?}"
    );
}

/// The repository's own ledger holds to its contract against every golden
/// this suite compares and the compiled catalog.
#[test]
fn departure_ledger_holds_to_its_contract() {
    if let Err(failures) = load_departure_ledger(Path::new(env!("CARGO_MANIFEST_DIR"))) {
        panic!(
            "{} breaks its contract:\n{}",
            departures_ledger::LEDGER,
            failures.join("\n")
        );
    }
}

#[test]
fn a_recorded_departure_passes_and_any_other_difference_fails() {
    let root = repository(&ledger_text(&wrapper_row(GOLDEN)));
    let out = output(CROZIER_WRAPPER);
    assert_eq!(compare(root.path(), out.path()), Vec::<String>::new());
    // Another difference on the departure's own line: the rule no longer
    // recognises the line, so the file differs and the row is stale.
    let same_line = output(&CROZIER_WRAPPER.replace("\"Python\"", "\"Python3\""));
    let failures = compare(root.path(), same_line.path());
    assert!(
        failures.len() == 2
            && failures[0].contains("generated core/client_wrapper.py differs")
            && failures[0].contains("+     \"X-Crozier-Language\": \"Python3\",")
            && failures[1].contains("is stale"),
        "{failures:#?}"
    );
    // Another line of the same file: the departure applies, the line fails.
    let same_file = output(&format!("{CROZIER_WRAPPER}x = 1\n"));
    let failures = compare(root.path(), same_file.path());
    assert!(
        failures.len() == 1
            && failures[0].contains("generated core/client_wrapper.py differs")
            && failures[0].contains("+ x = 1")
            && !failures[0].contains("X-Crozier"),
        "{failures:#?}"
    );
}

#[test]
fn a_stale_row_fails_naming_it() {
    let row = wrapper_row(GOLDEN);
    let root = repository(&ledger_text(&row));
    // crozier now writes Fern's header: nothing departs, so the row is stale.
    let out = output(&FERN_WRAPPER.replacen('\n', "# crozier\n", 1));
    let failures = compare(root.path(), out.path());
    assert!(
        failures.len() == 1
            && failures[0].contains(row.trim_end())
            && failures[0].contains("is stale")
            && failures[0].contains(departures_ledger::REGENERATE),
        "{failures:#?}"
    );
    // So is a row whose file crozier no longer writes at all.
    let missing = output(CROZIER_WRAPPER);
    std::fs::remove_file(missing.path().join(WRAPPER)).unwrap();
    let error = golden_differences(
        &root.path().join(GOLDEN),
        missing.path(),
        None,
        true,
        loaded(root.path()).golden(GOLDEN, &[]),
    )
    .expect_err("the stale row fails");
    assert!(
        error.contains(row.trim_end()) && error.contains("is stale"),
        "{error}"
    );
}

#[test]
fn an_unrecorded_departure_fails_naming_it() {
    let root = repository(&ledger_text(""));
    let failures = compare(root.path(), output(CROZIER_WRAPPER).path());
    assert!(
        failures.len() == 1
            && failures[0].contains(wrapper_row(GOLDEN).trim_end())
            && failures[0].contains("is unrecorded")
            && failures[0].contains(departures_ledger::REGENERATE),
        "{failures:#?}"
    );
    // A row on another line does not record it either.
    let elsewhere = wrapper_row(GOLDEN).replace("\t3\t", "\t2\t");
    let root = repository(&ledger_text(&elsewhere));
    let failures = compare(root.path(), output(CROZIER_WRAPPER).path());
    assert!(
        failures
            .iter()
            .any(|failure| failure.contains("is unrecorded"))
            && failures.iter().any(|failure| failure.contains("is stale")),
        "{failures:#?}"
    );
}

#[test]
fn rows_naming_an_unknown_departure_golden_or_file_are_refused() {
    let unknown_id = format!("{GOLDEN}\t{WRAPPER}\t3\tno-such-departure");
    assert_names(
        &load_failures(repository(&ledger_text(&format!("{unknown_id}\n"))).path()),
        &unknown_id,
        "which is no entry of the departure catalog",
    );
    let unknown_golden =
        format!("tests/fixtures/nowhere/expected\t{WRAPPER}\t3\tsdk-identity-header-prefix");
    assert_names(
        &load_failures(repository(&ledger_text(&format!("{unknown_golden}\n"))).path()),
        &unknown_golden,
        "which no comparison reads",
    );
    let unknown_file = format!("{GOLDEN}\tcore/absent.py\t3\tsdk-identity-header-prefix");
    assert_names(
        &load_failures(repository(&ledger_text(&format!("{unknown_file}\n"))).path()),
        &unknown_file,
        "which no comparison of golden",
    );
    for escaping in [
        "../core/client_wrapper.py",
        "/etc/passwd",
        "core//x.py",
        "core\\x.py",
    ] {
        let row = format!("{GOLDEN}\t{escaping}\t3\tsdk-identity-header-prefix");
        assert_names(
            &load_failures(repository(&ledger_text(&format!("{row}\n"))).path()),
            &row,
            "is not a relative path inside its golden",
        );
    }
    // The provenance record and an overlay's manifest sit in their goldens,
    // but no comparison reads them.
    let root = repository(&ledger_text(&format!(
        "{GOLDEN}\t.crozier-fern-golden.json\t1\tsdk-identity-header-prefix\n"
    )));
    write(
        root.path(),
        &format!("{GOLDEN}/.crozier-fern-golden.json"),
        "{}",
    );
    assert_eq!(load_failures(root.path()).len(), 1);
    let overlay = format!("tests/fixtures/{}/expected-literals", OPENFIGI.api);
    let root = repository(&ledger_text(&format!(
        "{overlay}\t.crozier-overlay.json\t1\tsdk-identity-header-prefix\n"
    )));
    write(
        root.path(),
        &format!("{overlay}/.crozier-overlay.json"),
        "{}",
    );
    assert!(load_failures(root.path())[0].contains("which no comparison of golden"));
}

#[test]
fn duplicate_or_unsorted_rows_are_refused() {
    let row = wrapper_row(GOLDEN);
    let failures = load_failures(repository(&ledger_text(&format!("{row}{row}"))).path());
    assert_names(&failures, row.trim_end(), "appears twice");
    let later = row.replace("\t3\t", "\t4\t");
    let failures = load_failures(repository(&ledger_text(&format!("{later}{row}"))).path());
    assert_names(
        &failures,
        row.trim_end(),
        "rows are sorted by golden, file, line and departure",
    );
}

#[test]
fn a_malformed_ledger_is_refused() {
    let root = repository("golden\tfile\n");
    assert!(load_failures(root.path())[0].contains("the first line is the header"));
    let short = format!("{GOLDEN}\t{WRAPPER}\t3");
    assert_names(
        &load_failures(repository(&ledger_text(&format!("{short}\n"))).path()),
        &short,
        "is not four tab-separated fields",
    );
    for line in ["0", "x", "-1"] {
        let row = format!("{GOLDEN}\t{WRAPPER}\t{line}\tsdk-identity-header-prefix");
        assert_names(
            &load_failures(repository(&ledger_text(&format!("{row}\n"))).path()),
            &row,
            "the line is not a positive number",
        );
    }
    let missing = tempfile::tempdir().unwrap();
    write(
        missing.path(),
        departures_ledger::INVENTORY,
        SCRATCH_INVENTORY,
    );
    assert!(load_failures(missing.path())[0].contains("cannot be read"));
}

/// A corpus golden in the scratch repository: `api`'s `expected/` holding the
/// two files and a row naming `file`.
fn corpus_repository(api: &str, file: &str) -> (tempfile::TempDir, String) {
    let golden_path = format!("tests/fixtures/{api}/expected");
    let root = repository(&ledger_text(&format!(
        "{golden_path}\t{file}\t3\tsdk-identity-header-prefix\n"
    )));
    golden(root.path(), &golden_path);
    write(root.path(), &format!("{golden_path}/{file}"), FERN_WRAPPER);
    (root, golden_path)
}

/// The failures the corpus gate's preflight reports for `c` over `ledger`.
fn carve_out_failures(ledger: &Ledger, golden: &str, c: &Corpus) -> Vec<String> {
    corpus_golden_ledger(ledger, golden, c).expect_err("the carve-out must be refused")
}

#[test]
fn a_file_also_carved_out_at_file_level_is_refused() {
    // An `unmatched` entry.
    static UNMATCHED: Corpus = Corpus {
        unmatched: &["README.md"],
        ..OPENFIGI
    };
    let (root, golden) = corpus_repository(OPENFIGI.api, "README.md");
    let ledger = loaded(root.path());
    let row = format!("{golden}\tREADME.md\t3\tsdk-identity-header-prefix");
    assert_names(
        &carve_out_failures(&ledger, &golden, &UNMATCHED),
        &row,
        "also an `unmatched` entry",
    );
    // A crozier-only file.
    let file = WEBFLOW_V2_CROZIER_ONLY[0];
    let (root, golden) = corpus_repository(WEBFLOW_V2.api, file);
    assert_names(
        &carve_out_failures(&loaded(root.path()), &golden, &WEBFLOW_V2),
        file,
        "also a crozier-only file",
    );
    // The same row over a corpus that carves nothing out is admitted.
    assert!(corpus_golden_ledger(&ledger, &golden, &OPENFIGI).is_ok());
}

#[test]
fn a_carve_out_the_inventory_records_is_refused_at_load() {
    let (root, golden) = corpus_repository(OPENFIGI.api, "README.md");
    write(
        root.path(),
        departures_ledger::INVENTORY,
        r#"{"goldens": {"tests/fixtures/openfigi.com/expected": {"carve_outs": {"unmatched": ["README.md"]}}}}"#,
    );
    assert_names(
        &load_failures(root.path()),
        &format!("{golden}\tREADME.md"),
        "also an `unmatched` entry",
    );
    write(
        root.path(),
        departures_ledger::INVENTORY,
        r#"{"goldens": {"tests/fixtures/openfigi.com/expected": {"carve_outs": {"vendored": []}}}}"#,
    );
    assert!(load_failures(root.path())[0].contains("unknown carve-out kind `vendored`"));
}

#[test]
fn the_corpus_gate_holds_its_golden_to_the_ledger() {
    let (root, golden) = corpus_repository(OPENFIGI.api, WRAPPER);
    assert!(CORPORA.iter().any(|corpus| corpus.api == OPENFIGI.api));
    let expected = root.path().join(&golden);
    let ledger =
        corpus_golden_ledger(&loaded(root.path()), &golden, &OPENFIGI).expect("no carve-out");
    assert_generated_tree_matches(
        &OPENFIGI,
        &ledger,
        &expected,
        output(CROZIER_WRAPPER).path(),
    );
    let gate = |out: &Path, ledger: &GoldenLedger| {
        let panic = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
            assert_generated_tree_matches(&OPENFIGI, ledger, &expected, out);
        }))
        .expect_err("the corpus gate fails");
        panic.downcast_ref::<String>().cloned().unwrap_or_default()
    };
    // A line the departure does not account for still fails it.
    let drifted = output(&format!("{CROZIER_WRAPPER}x = 1\n"));
    let message = gate(drifted.path(), &ledger);
    assert!(
        message.contains("generated core/client_wrapper.py does not match")
            && message.contains("+ x = 1"),
        "{message}"
    );
    // A golden with no row: the departure is unrecorded.
    let bare = corpus_golden_ledger(
        &loaded(root.path()),
        "tests/fixtures/other/expected",
        &OPENFIGI,
    )
    .expect("no row");
    let message = gate(output(CROZIER_WRAPPER).path(), &bare);
    assert!(message.contains("is unrecorded"), "{message}");
}

#[test]
fn the_flat_and_reporter_comparison_holds_the_ledger() {
    let root = repository(&ledger_text(&wrapper_row(GOLDEN)));
    let expected = root.path().join(GOLDEN);
    let ledger = || loaded(root.path()).golden(GOLDEN, &[]);
    let differences = golden_differences(
        &expected,
        output(CROZIER_WRAPPER).path(),
        None,
        true,
        ledger(),
    )
    .expect("the row records the departure");
    assert!(differences.is_empty(), "{differences:?}");
    // A filter that leaves the file out holds no row to it.
    let differences = golden_differences(
        &expected,
        output(&FERN_WRAPPER.replacen('\n', "# crozier\n", 1)).path(),
        Some("client.py"),
        true,
        ledger(),
    )
    .expect("the wrapper is outside the filter");
    assert!(differences.is_empty(), "{differences:?}");
    let drifted = output(&format!("{CROZIER_WRAPPER}x = 1\n"));
    let differences =
        golden_differences(&expected, drifted.path(), None, true, ledger()).expect("recorded");
    assert!(
        matches!(&differences[..], [(rel, crozier::parity::Difference::Text(Some(diff)))]
            if rel == WRAPPER && diff.contains("+ x = 1")),
        "{differences:?}"
    );
    let refused = golden_differences(
        &expected,
        drifted.path(),
        None,
        true,
        Err(vec!["no ledger".to_string()]),
    );
    assert_eq!(refused, Err("no ledger".to_string()));
}

#[test]
fn an_overlay_takes_base_rows_only_for_the_files_it_inherits() {
    let base = format!("tests/fixtures/{}/expected", OPENFIGI.api);
    let overlay = format!("tests/fixtures/{}/expected-literals", OPENFIGI.api);
    let root = repository(&ledger_text(&format!(
        "{}{}",
        wrapper_row(&base),
        format_args!("{overlay}\tclient.py\t1\tsdk-identity-header-prefix\n")
    )));
    golden(root.path(), &base);
    write(root.path(), &format!("{overlay}/client.py"), CLIENT);
    let ledger = loaded(root.path());
    let own: BTreeSet<String> = ["client.py".to_string()].into_iter().collect();
    let tree = ledger.golden(&overlay, &[]).unwrap().inherit(
        ledger.golden(&base, &[]).unwrap(),
        own.clone(),
        &[],
    );
    // The wrapper's departure is the base golden's row; the overlay's own row
    // on client.py is stale, since nothing departs there.
    let observed = vec![(
        WRAPPER.to_string(),
        3,
        "sdk-identity-header-prefix".to_string(),
    )];
    let failures = tree.check(&observed, &|_| true);
    assert!(
        failures.len() == 1
            && failures[0].contains(&format!("{overlay}\tclient.py\t1"))
            && failures[0].contains("is stale"),
        "{failures:#?}"
    );
    // A base file the overlay removes takes no base row.
    let tree = ledger.golden(&overlay, &[]).unwrap().inherit(
        ledger.golden(&base, &[]).unwrap(),
        own,
        &[WRAPPER.to_string()],
    );
    let failures = tree.check(&[], &|rel| rel != "client.py");
    assert!(failures.is_empty(), "{failures:#?}");
}

#[test]
fn recorded_departures_merge_into_the_ledger_golden_by_golden() {
    let base = format!("tests/fixtures/{}/expected", OPENFIGI.api);
    let root = repository(&ledger_text(&format!(
        "{}{}",
        wrapper_row(GOLDEN),
        wrapper_row(&base)
    )));
    golden(root.path(), &base);
    let ledger = loaded(root.path());
    let records = tempfile::tempdir().unwrap();
    // Two comparisons of GOLDEN record one departure each; nothing records the
    // base golden, so its row stays.
    let tree = ledger.golden(GOLDEN, &[]).unwrap();
    for observed in [
        (
            WRAPPER.to_string(),
            3,
            "sdk-identity-header-prefix".to_string(),
        ),
        (
            WRAPPER.to_string(),
            4,
            "sdk-identity-header-prefix".to_string(),
        ),
    ] {
        tree.record_to(records.path(), &[observed]).unwrap();
    }
    let merged = departures_ledger::merge_records(root.path(), records.path()).unwrap();
    let rows = departures_ledger::parse(&merged).unwrap();
    assert_eq!(
        rows.iter().map(Row::render).collect::<Vec<_>>(),
        [
            wrapper_row(GOLDEN).trim_end().to_string(),
            wrapper_row(GOLDEN).trim_end().replace("\t3\t", "\t4\t"),
            wrapper_row(&base).trim_end().to_string(),
        ]
    );
    // A golden recorded with nothing loses its rows.
    let empty = tempfile::tempdir().unwrap();
    tree.record_to(empty.path(), &[]).unwrap();
    let merged = departures_ledger::merge_records(root.path(), empty.path()).unwrap();
    assert_eq!(merged, ledger_text(&wrapper_row(&base)));
    // A record that is not one is refused.
    let broken = tempfile::tempdir().unwrap();
    write(
        broken.path(),
        &format!("{}/x.tsv", GOLDEN.replace('/', "%")),
        "README.md\n",
    );
    assert!(departures_ledger::merge_records(root.path(), broken.path())
        .unwrap_err()
        .contains("is not a record"));
}

/// `just departures-ledger`'s second half: merge what its first half recorded
/// under [`departures_ledger::RECORD_ENV`] into the committed ledger, then
/// hold the result to the ledger's contract.
#[test]
#[ignore = "the ledger's regeneration step; run via `just departures-ledger`"]
fn write_departures_ledger() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let records = std::env::var_os(departures_ledger::RECORD_ENV)
        .unwrap_or_else(|| panic!("set {} to the records", departures_ledger::RECORD_ENV));
    let merged = departures_ledger::merge_records(root, Path::new(&records))
        .unwrap_or_else(|error| panic!("{error}"));
    std::fs::write(root.join(departures_ledger::LEDGER), merged).expect("write the ledger");
    if let Err(failures) = load_departure_ledger(root) {
        panic!(
            "the regenerated ledger breaks its contract:\n{}",
            failures.join("\n")
        );
    }
}

/// The committed inventory of compared goldens is exactly the one the
/// comparisons' registrations derive, so the in-process comparison of
/// `tests/generation.rs`, which reads it, validates against the same list.
#[test]
fn compared_goldens_inventory_is_current() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let derived = compared_goldens(root).render();
    let path = root.join(departures_ledger::INVENTORY);
    if std::env::var_os("CROZIER_UPDATE_COMPARED_GOLDENS").is_some() {
        std::fs::write(&path, &derived).expect("write the inventory");
        return;
    }
    let committed = std::fs::read_to_string(&path).unwrap_or_default();
    assert!(
        committed == derived,
        "{} is not the inventory the registered comparisons derive; regenerate it with \
         `CROZIER_UPDATE_COMPARED_GOLDENS=1 cargo nextest run --locked -E \
         'binary(e2e) and test(compared_goldens_inventory_is_current)'` and commit it",
        departures_ledger::INVENTORY
    );
}

/// The ledger's documented format is the loader's: the header and the
/// regeneration command `docs/departures/README.md` states are the ones the
/// loader and the failures use, and the `justfile` holds that recipe.
#[test]
fn the_documented_ledger_format_is_the_loaders() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let page = std::fs::read_to_string(root.join("docs/departures/README.md")).unwrap();
    for said in [
        departures_ledger::LEDGER,
        departures_ledger::REGENERATE,
        departures_ledger::RECORD_ENV,
        "`golden`, `file`, `line`, `departure`",
    ] {
        assert!(
            page.contains(said),
            "docs/departures/README.md does not say {said:?}"
        );
    }
    assert_eq!(departures_ledger::HEADER, "golden\tfile\tline\tdeparture");
    let justfile = std::fs::read_to_string(root.join("justfile")).unwrap();
    let recipe = departures_ledger::REGENERATE.trim_start_matches("just ");
    assert!(
        justfile.contains(&format!("\n{recipe}:")),
        "the justfile has no `{recipe}` recipe"
    );
    assert!(justfile.contains(departures_ledger::RECORD_ENV));
    assert!(justfile.contains("write_departures_ledger"));
}
