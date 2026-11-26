//! The recorder's two guarantees, driven through a real recording comparison
//! run as `just departures-ledger` runs one (this suite's own binary, the
//! recording variables set, nextest's test identity given):
//!
//! - issue #988: a comparison over a tree altered on purpose declares itself
//!   [`departures_ledger::perturbed`], and records no ledger row, no example
//!   row and no contributor entry, including in discovery, while an ordinary
//!   comparison beside it records its golden's complete rows;
//! - issue #989: every recorder destination — the ledger, contributor and
//!   example-inventory directories — must be an absolute scratch directory
//!   outside every source checkout, and any other is refused with the remedy
//!   before anything is written.

use std::collections::BTreeSet;
use std::path::Path;
use std::process::{Command, Output};

use super::departure_contributors::{
    self, Contributor, DISCOVER_ENV, INVENTORY_PATH_ENV, SELECTION_ENV,
};
use super::departures_ledger::{self, CONTRIBUTOR_ENV, EXAMPLE_INVENTORY_ENV, RECORD_ENV};
use super::example_values_inventory;

/// Which comparison [`recording_probe`] makes: `ordinary` or `perturbed`.
const PROBE_ENV: &str = "CROZIER_RECORDING_PROBE";

/// The hand-written fixture the probe compares: a small tree whose golden has
/// ledger rows in `README.md`, the file the perturbation shifts.
const FIXTURE: &str = "docs/openapi-surface/handwritten/odometer-reading";
const GOLDEN: &str = "docs/openapi-surface/handwritten/odometer-reading/fern-expected";

/// The nextest binary id the probe is noted under.
const BINARY: &str = "crozier-e2e::e2e";
const ORDINARY: &str = "recording_eligibility::an_ordinary_comparison";
const PERTURBED: &str = "recording_eligibility::a_perturbed_comparison";

/// One comparison of crozier's output over [`FIXTURE`] with its golden,
/// recording as a recording run's comparisons do. `perturbed` plants a line at
/// the top of crozier's `README.md` first, shifting every departure under it,
/// and compares inside [`departures_ledger::perturbed`]; it must still report
/// the planted difference. An ordinary comparison must pass. `nested` makes a
/// planted comparison inside a perturbed closure nested in another, then a
/// second one in the outer closure after the inner returns, then an ordinary
/// comparison once both have; `unwound` makes an ordinary comparison after a
/// perturbed closure that panicked.
#[test]
#[ignore = "a recording comparison the recording_eligibility tests run as a subprocess"]
fn recording_probe() {
    let fixture = crate::repo_root().join(FIXTURE);
    let spec = fixture.join("openapi.yml");
    let out = tempfile::tempdir().expect("crozier output tempdir");
    let sdk = out.path().join("sdk");
    crate::probe_command(&spec, &sdk).assert().success();
    let ledger = crate::departure_ledger()
        .golden(GOLDEN, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let compare = || {
        crate::golden_tree_failures(
            "odometer-reading",
            &spec.display().to_string(),
            &ledger,
            &fixture.join("fern-expected"),
            &sdk,
        )
    };
    let readme = sdk.join("README.md");
    let text = std::fs::read_to_string(&readme).expect("crozier's README.md");
    let ordinary = || {
        std::fs::write(&readme, &text).expect("restore");
        let failures = compare();
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    };
    let planted = || {
        std::fs::write(&readme, format!("A planted line.\n{text}")).expect("perturb");
        let failures = compare();
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains("README.md differs")),
            "the planted line was not reported: {failures:?}"
        );
    };
    match std::env::var(PROBE_ENV).as_deref() {
        Ok("ordinary") => ordinary(),
        Ok("perturbed") => departures_ledger::perturbed(planted),
        Ok("nested") => {
            departures_ledger::perturbed(|| {
                departures_ledger::perturbed(planted);
                assert!(
                    !departures_ledger::recording_eligible(),
                    "an inner closure's end made its outer one eligible"
                );
                planted();
            });
            assert!(departures_ledger::recording_eligible());
            ordinary();
        }
        Ok("unwound") => {
            let unwound = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
                departures_ledger::perturbed(|| panic!("a perturbed comparison panicked"))
            }));
            assert!(unwound.is_err(), "the perturbed closure did not panic");
            assert!(
                departures_ledger::recording_eligible(),
                "unwinding out of a perturbed closure left the thread ineligible"
            );
            ordinary();
        }
        other => panic!("set {PROBE_ENV} to ordinary, perturbed, nested or unwound, not {other:?}"),
    }
}

/// [`recording_probe`] as `test`, with each `(variable, value)` of
/// `destinations` set and no other recording variable inherited, from `cwd`.
fn probe(kind: &str, test: &str, destinations: &[(&str, &Path)], cwd: &Path) -> Output {
    let mut command = Command::new(std::env::current_exe().expect("this suite"));
    command
        .args([
            "recording_eligibility::recording_probe",
            "--exact",
            "--ignored",
            "--nocapture",
        ])
        .current_dir(cwd)
        .env(PROBE_ENV, kind)
        .env("NEXTEST_BINARY_ID", BINARY)
        .env("NEXTEST_TEST_NAME", test);
    for variable in [RECORD_ENV, CONTRIBUTOR_ENV, EXAMPLE_INVENTORY_ENV] {
        command.env_remove(variable);
    }
    for (variable, value) in destinations {
        command.env(variable, value);
    }
    command.output().expect("run the recording probe")
}

fn said(output: &Output) -> String {
    format!(
        "{}{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    )
}

/// Every file under `dir`, hidden ones included, relative to it and sorted.
fn files(dir: &Path) -> Vec<String> {
    let mut found = Vec::new();
    let mut pending = vec![dir.to_owned()];
    while let Some(next) = pending.pop() {
        for entry in std::fs::read_dir(&next).expect("a readable directory") {
            let path = entry.expect("a readable entry").path();
            if path.is_dir() {
                pending.push(path);
            } else {
                let rel = path.strip_prefix(dir).expect("under dir");
                found.push(rel.to_string_lossy().replace('\\', "/"));
            }
        }
    }
    found.sort();
    found
}

/// Link `link` to the directory `target`, where the platform lets a test do so
/// unprivileged (Windows needs Developer Mode for a symlink); whether it did.
#[cfg(unix)]
fn symlink_dir(target: &Path, link: &Path) -> bool {
    std::os::unix::fs::symlink(target, link).expect("a symlink");
    true
}

#[cfg(not(unix))]
fn symlink_dir(target: &Path, link: &Path) -> bool {
    std::os::windows::fs::symlink_dir(target, link).is_ok()
}

/// The three recording directories a run keeps in scratch.
struct Scratch {
    ledger: tempfile::TempDir,
    noted: tempfile::TempDir,
    examples: tempfile::TempDir,
}

impl Scratch {
    fn new() -> Self {
        Self {
            ledger: tempfile::tempdir().expect("ledger records"),
            noted: tempfile::tempdir().expect("contributor notes"),
            examples: tempfile::tempdir().expect("example records"),
        }
    }

    fn destinations(&self) -> [(&'static str, &Path); 3] {
        [
            (RECORD_ENV, self.ledger.path()),
            (CONTRIBUTOR_ENV, self.noted.path()),
            (EXAMPLE_INVENTORY_ENV, self.examples.path()),
        ]
    }
}

/// Issue #988: a perturbed comparison recorded beside an ordinary one of the
/// same golden leaves exactly the ordinary one's records — the merged ledger
/// and example inventory are the committed ones, and the only contributor
/// noted is the ordinary test — and discovery, run over those records through
/// the real contributor step, derives an inventory naming only it.
#[test]
fn a_perturbed_comparison_records_nothing_beside_an_ordinary_one() {
    let root = crate::repo_root();
    let scratch = Scratch::new();
    let cwd = tempfile::tempdir().expect("probe working directory");
    for (kind, test) in [("ordinary", ORDINARY), ("perturbed", PERTURBED)] {
        let output = probe(kind, test, &scratch.destinations(), cwd.path());
        assert!(output.status.success(), "{kind}: {}", said(&output));
    }

    let committed = |rel: &str| std::fs::read_to_string(root.join(rel)).expect("committed");
    assert_eq!(
        departures_ledger::merge_records(root, scratch.ledger.path()).expect("merge"),
        committed(departures_ledger::LEDGER),
        "the perturbed comparison's shifted departures reached the ledger"
    );
    assert_eq!(
        example_values_inventory::merge_records(root, scratch.examples.path()).expect("merge"),
        committed(example_values_inventory::INVENTORY),
        "the perturbed comparison's rows reached the example inventory"
    );
    let ordinary: BTreeSet<Contributor> = [Contributor {
        golden: GOLDEN.to_owned(),
        binary: BINARY.to_owned(),
        test: ORDINARY.to_owned(),
    }]
    .into();
    assert_eq!(
        departure_contributors::recorded(scratch.noted.path()).expect("the notes"),
        ordinary,
        "only the ordinary comparison is a contributor"
    );

    // Discovery's own step rederives the inventory from those notes and holds
    // the run's records to it.
    let inventory = cwd.path().join("departures-contributors.tsv");
    let output = Command::new(std::env::current_exe().expect("this suite"))
        .args([
            "departure_contributors::verify_departure_contributors",
            "--exact",
            "--ignored",
            "--nocapture",
        ])
        .envs(scratch.destinations())
        .env(SELECTION_ENV, "")
        .env(DISCOVER_ENV, "1")
        .env(INVENTORY_PATH_ENV, &inventory)
        .output()
        .expect("run discovery's contributor step");
    assert!(output.status.success(), "{}", said(&output));
    assert_eq!(
        std::fs::read_to_string(&inventory).expect("the derived inventory"),
        departure_contributors::render(&ordinary),
        "discovery listed a perturbed comparison"
    );
}

/// Issue #988's contract holds across nesting and unwinding: a planted
/// comparison inside a nested perturbed closure, and another in its outer
/// closure after the inner one returns, record nothing, while an ordinary one
/// after both records the golden's complete rows; and after a perturbed
/// closure panics and is caught, an ordinary comparison records again.
#[test]
fn eligibility_survives_nested_and_unwound_perturbed_comparisons() {
    let root = crate::repo_root();
    let committed = |rel: &str| std::fs::read_to_string(root.join(rel)).expect("committed");
    for (kind, test) in [
        (
            "nested",
            "recording_eligibility::nested_perturbed_comparisons",
        ),
        (
            "unwound",
            "recording_eligibility::an_unwound_perturbed_comparison",
        ),
    ] {
        let scratch = Scratch::new();
        let cwd = tempfile::tempdir().expect("probe working directory");
        let output = probe(kind, test, &scratch.destinations(), cwd.path());
        assert!(output.status.success(), "{kind}: {}", said(&output));
        let directory = GOLDEN.replace('/', "%");
        let records = files(scratch.ledger.path());
        assert!(
            !records.is_empty()
                && records
                    .iter()
                    .all(|record| record.starts_with(&format!("{directory}/"))),
            "{kind}: the ordinary comparison recorded nothing: {records:?}"
        );
        assert_eq!(
            departures_ledger::merge_records(root, scratch.ledger.path()).expect("merge"),
            committed(departures_ledger::LEDGER),
            "{kind}: a perturbed comparison's shifted departures reached the ledger"
        );
        assert_eq!(
            departure_contributors::recorded(scratch.noted.path()).expect("the notes"),
            [Contributor {
                golden: GOLDEN.to_owned(),
                binary: BINARY.to_owned(),
                test: test.to_owned(),
            }]
            .into(),
            "{kind}: the ordinary comparison is noted once"
        );
    }
}

/// Issue #989: each recorder destination — ledger, contributor and example
/// inventory — pointed inside the source checkout, at a relative path, at an
/// absolute path that does not exist, at a regular file, or at a symlink
/// outside the checkout resolving into it is refused with the remedy, and
/// nothing is written anywhere; all three in scratch outside the checkout
/// record, and the scratch goes with its owner.
#[test]
fn a_recorder_destination_that_is_no_scratch_directory_is_refused_before_writing() {
    let root = crate::repo_root();
    for variable in [RECORD_ENV, CONTRIBUTOR_ENV, EXAMPLE_INVENTORY_ENV] {
        let inside = tempfile::Builder::new()
            .prefix(".crozier-recorder-destination-")
            .tempdir_in(root)
            .expect("a directory inside the checkout");
        let cwd = tempfile::tempdir().expect("probe working directory");
        let relative = Path::new("records");
        std::fs::create_dir(cwd.path().join(relative)).expect("an existing relative directory");
        let outside = tempfile::tempdir().expect("scratch outside the checkout");
        let missing = outside.path().join("missing");
        let file = outside.path().join("a-file");
        std::fs::write(&file, "").expect("a regular file");
        // Outside the checkout by its own path, inside it once resolved.
        let link = outside.path().join("into-the-checkout");
        let linked = symlink_dir(inside.path(), &link);
        let cases: Vec<(&Path, &str)> = [
            (inside.path(), "is inside the source checkout"),
            (relative, "is a relative path"),
            (missing.as_path(), "is no directory to record into"),
            (file.as_path(), "is not a directory"),
        ]
        .into_iter()
        .chain(linked.then_some((link.as_path(), "is inside the source checkout")))
        .collect();
        for (bad, says) in cases {
            let scratch = Scratch::new();
            let destinations: Vec<(&str, &Path)> = scratch
                .destinations()
                .into_iter()
                .map(|(name, dir)| (name, if name == variable { bad } else { dir }))
                .collect();
            let output = probe("ordinary", ORDINARY, &destinations, cwd.path());
            let said = said(&output);
            assert!(!output.status.success(), "{variable}={bad:?} was accepted");
            assert!(
                said.contains(&format!("{variable}: `{}` {says}", bad.display()))
                    && said.contains("nothing was recorded")
                    && said.contains(&format!(
                        "point {variable} at an absolute scratch directory outside every \
                         source checkout"
                    )),
                "{variable}={bad:?}: {said}"
            );
            for dir in [
                inside.path(),
                &cwd.path().join(relative),
                scratch.ledger.path(),
                scratch.noted.path(),
                scratch.examples.path(),
            ] {
                assert_eq!(
                    files(dir),
                    Vec::<String>::new(),
                    "{variable}={bad:?} left a record in {}",
                    dir.display()
                );
            }
            assert!(!missing.exists(), "{variable}={bad:?} created {missing:?}");
            assert_eq!(
                std::fs::read(&file).expect("the regular file"),
                b"",
                "{variable}={bad:?} wrote into {file:?}"
            );
        }
    }

    let scratch = Scratch::new();
    let cwd = tempfile::tempdir().expect("probe working directory");
    let output = probe("ordinary", ORDINARY, &scratch.destinations(), cwd.path());
    assert!(output.status.success(), "{}", said(&output));
    let directory = GOLDEN.replace('/', "%");
    for (what, dir) in [
        ("ledger", scratch.ledger.path()),
        ("example", scratch.examples.path()),
    ] {
        let recorded = files(dir);
        assert!(
            recorded.len() == 1
                && recorded[0].starts_with(&format!("{directory}/"))
                && recorded[0].ends_with(".tsv"),
            "{what} records: {recorded:?}"
        );
    }
    assert_eq!(files(scratch.noted.path()).len(), 1, "one contributor note");
    assert_eq!(
        files(cwd.path()),
        Vec::<String>::new(),
        "nothing outside scratch"
    );
    let kept = [
        scratch.ledger.path().to_owned(),
        scratch.noted.path().to_owned(),
        scratch.examples.path().to_owned(),
    ];
    drop(scratch);
    assert!(
        kept.iter().all(|dir| !dir.exists()),
        "the scratch outlived its owner"
    );
}
