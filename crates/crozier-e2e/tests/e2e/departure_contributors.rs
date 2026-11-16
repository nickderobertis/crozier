//! The committed inventory of the tests whose comparisons record departure
//! ledger and example-inventory rows, `tests/fixtures/departures-contributors.tsv`,
//! and the two steps of `just departures-ledger` that use it besides the merge:
//! renaming moved goldens before anything records (issue #819), and holding a
//! recording run to the inventory before its records are merged (issue #820).
//!
//! `just departures-ledger` runs only the inventoried tests, so a small change
//! no longer pays for — or fails on — every unrelated journey of the suite. The
//! inventory is never trusted: every run must record exactly the
//! `(golden, test)` pairs it lists for the tests that ran, a ledger record for
//! each of their goldens, and an example-inventory record for each of them the
//! committed example inventory names, so a stale or incomplete inventory fails
//! before any row is merged. A compared golden only an `#[ignore]`d journey
//! compares (the `sdk_env_*` ones) is recorded by no run, as it never was by
//! the whole-suite run either, and keeps its rows. `just departures-ledger
//! --discover-contributors` rederives the inventory from the whole suite.

use std::collections::BTreeSet;
use std::path::Path;

use super::departures_ledger::{self, Inventory, CONTRIBUTOR_ENV};
use super::example_values_inventory;

/// The inventory, relative to the repository root.
pub const CONTRIBUTORS: &str = "tests/fixtures/departures-contributors.tsv";

/// The inventory's first line.
pub const HEADER: &str = "golden\tbinary\ttest";

/// The command that rederives the inventory from the whole suite.
pub const DISCOVER: &str = "just departures-ledger --discover-contributors";

/// The goldens a run was asked to record, space-separated; unset or empty for
/// every golden.
pub const SELECTION_ENV: &str = "CROZIER_LEDGER_SELECTION";

/// Set to `1`, the run was the whole suite, and the inventory is rewritten
/// from what it recorded before being held to it.
pub const DISCOVER_ENV: &str = "CROZIER_DISCOVER_CONTRIBUTORS";

/// The `OLD=NEW` golden-tree renames to apply, space-separated.
pub const RENAME_ENV: &str = "CROZIER_RENAME_GOLDENS";

/// Where the contributor check reads (and discovery writes) the inventory;
/// unset, the committed [`CONTRIBUTORS`]. The script never sets it.
pub const INVENTORY_PATH_ENV: &str = "CROZIER_CONTRIBUTOR_INVENTORY";

/// The compared goldens no recording run records: each is compared only by an
/// `#[ignore]`d `sdk_env_*` journey (a PyPI install), which neither the whole
/// suite nor the selected run starts, so its ledger rows are kept as they are.
pub const JOURNEY_ONLY_GOLDENS: [&str; 6] = [
    "docs/fern-measurements/superseded-fixtures/depot-bin-ledger/fern-expected",
    "docs/fern-measurements/superseded-fixtures/described-scalar-bodies/fern-expected",
    "docs/fern-measurements/superseded-fixtures/event-stream-event-dispatch/fern-expected",
    "docs/fern-measurements/superseded-fixtures/ferry-berth-desk/fern-expected",
    "docs/fern-measurements/superseded-fixtures/request-example-deprecated/fern-expected",
    "docs/fern-measurements/superseded-fixtures/request-example-nulls/fern-expected",
];

/// One test recording one golden.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
pub struct Contributor {
    pub golden: String,
    /// The nextest binary id, `crozier-e2e::e2e`.
    pub binary: String,
    pub test: String,
}

impl Contributor {
    fn parse(line: &str) -> Option<Self> {
        let [golden, binary, test] = line.split('\t').collect::<Vec<_>>()[..] else {
            return None;
        };
        [golden, binary, test]
            .iter()
            .all(|cell| !cell.is_empty())
            .then(|| Self {
                golden: golden.to_owned(),
                binary: binary.to_owned(),
                test: test.to_owned(),
            })
    }

    fn render(&self) -> String {
        format!("{}\t{}\t{}", self.golden, self.binary, self.test)
    }

    /// The test, as nextest identifies it.
    fn test_id(&self) -> (&str, &str) {
        (&self.binary, &self.test)
    }
}

/// Parse an inventory, refusing a wrong header, a malformed, repeated or
/// unsorted row.
pub fn parse(text: &str) -> Result<BTreeSet<Contributor>, String> {
    let mut lines = text.lines();
    if lines.next() != Some(HEADER) {
        return Err(format!("{CONTRIBUTORS}: the first line is not `{HEADER}`"));
    }
    let mut rows = BTreeSet::new();
    let mut previous: Option<Contributor> = None;
    for line in lines {
        let row = Contributor::parse(line)
            .ok_or_else(|| format!("{CONTRIBUTORS}: `{line}` is not a row"))?;
        if previous.as_ref().is_some_and(|previous| *previous >= row) {
            return Err(format!(
                "{CONTRIBUTORS}: `{line}` is repeated or out of order; rederive it with `{DISCOVER}`"
            ));
        }
        previous = Some(row.clone());
        rows.insert(row);
    }
    Ok(rows)
}

/// The inventory as the committed file spells it.
pub fn render(rows: &BTreeSet<Contributor>) -> String {
    let mut text = format!("{HEADER}\n");
    for row in rows {
        text.push_str(&row.render());
        text.push('\n');
    }
    text
}

/// Every `(golden, test)` pair a recording run noted under `dir`.
pub fn recorded(dir: &Path) -> Result<BTreeSet<Contributor>, String> {
    let mut rows = BTreeSet::new();
    let entries = std::fs::read_dir(dir).map_err(|error| format!("{}: {error}", dir.display()))?;
    for entry in entries {
        let path = entry
            .map_err(|error| format!("{}: {error}", dir.display()))?
            .path();
        let text = std::fs::read_to_string(&path)
            .map_err(|error| format!("{}: {error}", path.display()))?;
        for line in text.lines() {
            rows.insert(
                Contributor::parse(line)
                    .ok_or_else(|| format!("{}: `{line}` is not a note", path.display()))?,
            );
        }
    }
    Ok(rows)
}

/// The inventory's rows a run of `selected` goldens must record: those of
/// every test recording a selected golden, closed over every other golden
/// those tests record, so no golden's rows are merged from only some of its
/// comparisons. No selection is every row.
pub fn selected_rows(
    inventory: &BTreeSet<Contributor>,
    selected: &[String],
) -> Result<BTreeSet<Contributor>, String> {
    if selected.is_empty() {
        return Ok(inventory.clone());
    }
    let unknown: Vec<&String> = selected
        .iter()
        .filter(|golden| !inventory.iter().any(|row| row.golden == **golden))
        .collect();
    if !unknown.is_empty() {
        return Err(format!(
            "{CONTRIBUTORS} names no test recording {unknown:?}; name a golden of \
             tests/fixtures/compared-goldens.json, or rederive the inventory with `{DISCOVER}`"
        ));
    }
    let mut goldens: BTreeSet<&str> = selected.iter().map(String::as_str).collect();
    loop {
        let tests: BTreeSet<(&str, &str)> = inventory
            .iter()
            .filter(|row| goldens.contains(row.golden.as_str()))
            .map(Contributor::test_id)
            .collect();
        let closed: BTreeSet<&str> = inventory
            .iter()
            .filter(|row| tests.contains(&row.test_id()))
            .map(|row| row.golden.as_str())
            .collect();
        if closed == goldens {
            return Ok(inventory
                .iter()
                .filter(|row| tests.contains(&row.test_id()))
                .cloned()
                .collect());
        }
        goldens = closed;
    }
}

/// Every reason a recording run cannot be merged: the run noted `observed`
/// under the inventory's `expected` rows and wrote its records under the two
/// record directories. Every expected golden owes a ledger record, and one the
/// committed example inventory names (`with_examples`) an example record too:
/// the merge replaces only what was recorded.
pub fn failures(
    expected: &BTreeSet<Contributor>,
    observed: &BTreeSet<Contributor>,
    with_examples: &BTreeSet<String>,
    records: [&Path; 2],
) -> Vec<String> {
    let mut failures = Vec::new();
    for row in observed.difference(expected) {
        failures.push(format!(
            "{CONTRIBUTORS}: `{}` recorded {}, which the inventory does not attribute to it, so \
             a selected run would merge that golden from only some of its comparisons — \
             rederive it with `{DISCOVER}`",
            row.test, row.golden
        ));
    }
    for row in expected.difference(observed) {
        failures.push(format!(
            "{CONTRIBUTORS}: `{}` is inventoried as recording {}, but the run recorded no such \
             thing: the test was renamed or removed, or no longer compares that golden — \
             rederive the inventory with `{DISCOVER}`",
            row.test, row.golden
        ));
    }
    let goldens: BTreeSet<&str> = expected.iter().map(|row| row.golden.as_str()).collect();
    for golden in &goldens {
        for (dir, kind) in records
            .iter()
            .zip(["departure ledger", "example inventory"])
        {
            let owed = kind == "departure ledger" || with_examples.contains(*golden);
            if owed && !dir.join(golden.replace('/', "%")).is_dir() {
                failures.push(format!(
                    "{golden}: the run wrote no {kind} record for it, so its rows cannot be \
                     replaced — fix its comparison, then rerun `{}`",
                    departures_ledger::REGENERATE
                ));
            }
        }
    }
    failures
}

/// The goldens the committed example inventory names: each owes an example record.
pub fn committed_example_goldens(root: &Path) -> Result<BTreeSet<String>, String> {
    let rel = example_values_inventory::INVENTORY;
    let text =
        std::fs::read_to_string(root.join(rel)).map_err(|error| format!("{rel}: {error}"))?;
    let rows = example_values_inventory::parse(&text).map_err(|failures| failures.join("\n"))?;
    Ok(rows.into_iter().map(|row| row.golden).collect())
}

/// `just departures-ledger`'s step between recording and merging: hold what
/// the recording run noted under [`CONTRIBUTOR_ENV`] to the inventory, first
/// rewriting the inventory from it under [`DISCOVER_ENV`].
#[test]
#[ignore = "the ledger's contributor check; run via `just departures-ledger`"]
fn verify_departure_contributors() {
    let root = crate::repo_root();
    let env = |name: &str| {
        std::env::var_os(name).unwrap_or_else(|| panic!("set {name} to the run's directory"))
    };
    let observed = recorded(Path::new(&env(CONTRIBUTOR_ENV))).unwrap_or_else(|e| panic!("{e}"));
    let path = std::env::var_os(INVENTORY_PATH_ENV)
        .map(std::path::PathBuf::from)
        .unwrap_or_else(|| root.join(CONTRIBUTORS));
    if std::env::var(DISCOVER_ENV).as_deref() == Ok("1") {
        // Replaced whole, never truncated in place: other tests read it meanwhile.
        let mut staged =
            tempfile::NamedTempFile::new_in(path.parent().expect("a file has a parent"))
                .expect("stage the contributor inventory");
        std::io::Write::write_all(&mut staged, render(&observed).as_bytes())
            .expect("write the contributor inventory");
        staged
            .persist(&path)
            .expect("replace the contributor inventory");
    }
    let text = std::fs::read_to_string(&path).unwrap_or_else(|error| {
        panic!("{CONTRIBUTORS}: cannot be read ({error}); derive it with `{DISCOVER}`")
    });
    let inventory = parse(&text).unwrap_or_else(|e| panic!("{e}"));
    let selected: Vec<String> = std::env::var(SELECTION_ENV)
        .unwrap_or_default()
        .split_whitespace()
        .map(str::to_owned)
        .collect();
    let expected = selected_rows(&inventory, &selected).unwrap_or_else(|e| panic!("{e}"));
    let with_examples = committed_example_goldens(root).unwrap_or_else(|e| panic!("{e}"));
    let ledger = env(departures_ledger::RECORD_ENV);
    let examples = env(example_values_inventory::RECORD_ENV);
    let failures = failures(
        &expected,
        &observed,
        &with_examples,
        [Path::new(&ledger), Path::new(&examples)],
    );
    assert!(
        failures.is_empty(),
        "the recording run cannot be merged:\n{}",
        failures.join("\n")
    );
}

/// Rename each `old` golden tree to `new` in the four committed files that
/// name goldens — the ledger, the inventory of compared goldens, the example
/// inventory and the contributor inventory — staging all four before
/// replacing any, so a refused rename leaves every file as it was. The tree's
/// bytes are the script's to verify first.
pub fn rename_goldens(root: &Path, renames: &[(String, String)]) -> Result<(), String> {
    let mut compared = Inventory::read(root)?;
    let read = |rel: &str| {
        std::fs::read_to_string(root.join(rel)).map_err(|error| format!("{rel}: {error}"))
    };
    let mut ledger = departures_ledger::parse(&read(departures_ledger::LEDGER)?)
        .map_err(|failures| failures.join("\n"))?;
    let mut examples = example_values_inventory::parse(&read(example_values_inventory::INVENTORY)?)
        .map_err(|failures| failures.join("\n"))?;
    let mut contributors = parse(&read(CONTRIBUTORS)?)?;
    for (old, new) in renames {
        let entry = compared.goldens.remove(old).ok_or_else(|| {
            format!(
                "{}: {old} is not a compared golden to rename",
                departures_ledger::INVENTORY
            )
        })?;
        if compared.goldens.insert(new.clone(), entry).is_some() {
            return Err(format!(
                "{}: {new} is already a compared golden; a rename moves one golden onto a new path",
                departures_ledger::INVENTORY
            ));
        }
        let renamed = |golden: &mut String| {
            if golden == old {
                golden.clone_from(new);
            }
        };
        ledger.iter_mut().for_each(|row| renamed(&mut row.golden));
        examples.iter_mut().for_each(|row| renamed(&mut row.golden));
        contributors = contributors
            .into_iter()
            .map(|mut row| {
                renamed(&mut row.golden);
                row
            })
            .collect();
    }
    let outputs = [
        (
            departures_ledger::LEDGER,
            departures_ledger::render(&ledger.into_iter().collect()),
        ),
        (departures_ledger::INVENTORY, compared.render()),
        (
            example_values_inventory::INVENTORY,
            example_values_inventory::render(&examples.into_iter().collect()),
        ),
        (CONTRIBUTORS, render(&contributors)),
    ];
    let mut staged = Vec::new();
    for (rel, text) in &outputs {
        let target = root.join(rel);
        let mut file =
            tempfile::NamedTempFile::new_in(target.parent().expect("a file has a parent"))
                .map_err(|error| format!("{rel}: {error}"))?;
        std::io::Write::write_all(&mut file, text.as_bytes())
            .map_err(|error| format!("{rel}: {error}"))?;
        staged.push((file, target));
    }
    for (file, target) in staged {
        file.persist(&target)
            .map_err(|error| format!("{}: {error}", target.display()))?;
    }
    Ok(())
}

/// `just departures-ledger --rename OLD=NEW`'s step before anything records:
/// the recording run loads the ledger, which a moved golden's old path breaks.
#[test]
#[ignore = "the ledger's golden-rename step; run via `just departures-ledger --rename`"]
fn rename_departure_goldens() {
    let renames: Vec<(String, String)> = std::env::var(RENAME_ENV)
        .unwrap_or_else(|_| panic!("set {RENAME_ENV} to the OLD=NEW renames"))
        .split_whitespace()
        .map(|pair| {
            let (old, new) = pair
                .split_once('=')
                .unwrap_or_else(|| panic!("{RENAME_ENV}: `{pair}` is not OLD=NEW"));
            (old.to_owned(), new.to_owned())
        })
        .collect();
    rename_goldens(crate::repo_root(), &renames).unwrap_or_else(|error| panic!("{error}"));
}

const OLD: &str = "docs/openapi-surface/authored-probes/zz-old/fern-expected";
const NEW: &str = "docs/openapi-surface/authored-probes/aa-new/fern-expected";
const KEPT: &str = "docs/openapi-surface/authored-probes/mm-kept/fern-expected";
const BINARY: &str = "crozier-e2e::e2e";

/// A scratch repository holding [`NEW`] and [`KEPT`], the tree at [`OLD`]
/// having moved to [`NEW`] byte for byte, whose four committed files still
/// name [`OLD`].
fn moved() -> tempfile::TempDir {
    let root = tempfile::tempdir().expect("scratch repository");
    let write = |rel: &str, text: &str| {
        let path = root.path().join(rel);
        std::fs::create_dir_all(path.parent().expect("a parent")).expect("mkdir");
        std::fs::write(path, text).expect("write");
    };
    for golden in [NEW, KEPT] {
        write(
            &format!("{golden}/core/client_wrapper.py"),
            "headers = {}\n",
        );
    }
    let row =
        |golden: &str| format!("{golden}\tcore/client_wrapper.py\t1\tsdk-identity-header-prefix\n");
    write(
        departures_ledger::LEDGER,
        &format!("{}\n{}{}", departures_ledger::HEADER, row(KEPT), row(OLD)),
    );
    write(
        departures_ledger::INVENTORY,
        &format!("{{\n  \"goldens\": {{\n    \"{KEPT}\": {{}},\n    \"{OLD}\": {{}}\n  }}\n}}\n"),
    );
    let example = |golden: &str| {
        format!(
            "{golden}\tcore/client_wrapper.py\t1\tid\t\"id\"\tformat=uuid\t\
             schema-rejected-name-example\trepaired\n"
        )
    };
    write(
        example_values_inventory::INVENTORY,
        &format!(
            "{}\n{}{}",
            example_values_inventory::HEADER,
            example(KEPT),
            example(OLD)
        ),
    );
    write(
        CONTRIBUTORS,
        &format!("{HEADER}\n{KEPT}\t{BINARY}\tkept_test\n{OLD}\t{BINARY}\tmoved_test\n"),
    );
    root
}

/// The four committed files that name goldens, as `root` holds them.
fn committed(root: &Path) -> [String; 4] {
    [
        departures_ledger::LEDGER,
        departures_ledger::INVENTORY,
        example_values_inventory::INVENTORY,
        CONTRIBUTORS,
    ]
    .map(|rel| std::fs::read_to_string(root.join(rel)).expect("read"))
}

// llmlint: ignore-block[tests_mirror_real_usage] The rename step's entry point, `rename_departure_goldens`, fixes its root at this repository, so applying a rename can only be watched over a scratch tree through `rename_goldens`, the function that entry point calls; the entry point's own parsing of `CROZIER_RENAME_GOLDENS` is driven through this binary by `the_rename_step_reads_its_renames_as_the_script_passes_them`, and the script's byte checks by report_scripts.rs.
/// Issue #819: a golden moved unchanged leaves every committed row naming its
/// old path, which the ledger load every recording comparison makes refuses;
/// renaming it in the four files restores the load, the rows re-sorted.
#[test]
fn a_moved_golden_breaks_the_ledger_until_it_is_renamed() {
    let root = moved();
    let refused = super::load_departure_ledger(root.path()).expect_err("the old path is gone");
    assert!(
        refused
            .iter()
            .any(|failure| failure.contains(OLD)
                && failure.contains("which no comparison of golden")),
        "{refused:#?}"
    );
    rename_goldens(root.path(), &[(OLD.to_owned(), NEW.to_owned())]).expect("renamed");
    super::load_departure_ledger(root.path()).unwrap_or_else(|failures| panic!("{failures:#?}"));
    let [ledger, inventory, examples, contributors] = committed(root.path());
    assert_eq!(
        ledger,
        format!(
            "{}\n{NEW}\tcore/client_wrapper.py\t1\tsdk-identity-header-prefix\n\
             {KEPT}\tcore/client_wrapper.py\t1\tsdk-identity-header-prefix\n",
            departures_ledger::HEADER
        )
    );
    assert_eq!(
        inventory,
        format!("{{\n  \"goldens\": {{\n    \"{NEW}\": {{}},\n    \"{KEPT}\": {{}}\n  }}\n}}\n")
    );
    assert!(
        examples
            .lines()
            .nth(1)
            .is_some_and(|row| row.starts_with(NEW))
            && !examples.contains(OLD),
        "{examples}"
    );
    assert_eq!(
        contributors,
        format!("{HEADER}\n{NEW}\t{BINARY}\tmoved_test\n{KEPT}\t{BINARY}\tkept_test\n")
    );
}

/// A rename that cannot apply — an unknown old path, or a new one already
/// compared — is refused and leaves all four files as they were.
#[test]
fn a_refused_rename_writes_nothing() {
    let root = moved();
    let before = committed(root.path());
    for (old, new, says) in [
        (
            "docs/nowhere/fern-expected",
            NEW,
            "is not a compared golden to rename",
        ),
        (OLD, KEPT, "is already a compared golden"),
    ] {
        let error =
            rename_goldens(root.path(), &[(old.to_owned(), new.to_owned())]).expect_err("refused");
        assert!(error.contains(says), "{error}");
        assert_eq!(committed(root.path()), before);
    }
}

/// Repeated renames apply together, in the four files at once; a batch whose
/// later pair is refused leaves every file as it was, the earlier pair too.
#[test]
fn a_batch_of_renames_applies_whole_or_not_at_all() {
    let root = moved();
    let renamed_kept = "docs/openapi-surface/authored-probes/nn-kept/fern-expected";
    let both = [
        (OLD.to_owned(), NEW.to_owned()),
        (KEPT.to_owned(), renamed_kept.to_owned()),
    ];
    let before = committed(root.path());
    let refused = [
        (OLD.to_owned(), NEW.to_owned()),
        ("docs/nowhere/fern-expected".to_owned(), KEPT.to_owned()),
    ];
    let error = rename_goldens(root.path(), &refused).expect_err("the second pair is refused");
    assert!(
        error.contains("docs/nowhere/fern-expected is not a compared golden"),
        "{error}"
    );
    assert_eq!(
        committed(root.path()),
        before,
        "a refused batch writes nothing"
    );
    rename_goldens(root.path(), &both).expect("both renamed");
    for file in committed(root.path()) {
        assert!(
            !file.contains(OLD) && !file.contains(&format!("{KEPT}\t")),
            "{file}"
        );
        assert!(file.contains(NEW) && file.contains(renamed_kept), "{file}");
    }
}
// llmlint: ignore-end[tests_mirror_real_usage]

/// The rename step, run as the script runs it (this suite's own binary, its
/// renames in [`RENAME_ENV`]), refuses a pair that is not `OLD=NEW` and a golden
/// the committed inventory does not compare, before writing anything.
#[test]
fn the_rename_step_reads_its_renames_as_the_script_passes_them() {
    let root = crate::repo_root();
    let before = committed(root);
    for (renames, says) in [
        ("docs/nowhere/fern-expected", "is not OLD=NEW"),
        (
            "docs/nowhere/fern-expected=docs/elsewhere/fern-expected",
            "docs/nowhere/fern-expected is not a compared golden to rename",
        ),
    ] {
        let output = std::process::Command::new(std::env::current_exe().expect("this suite"))
            .args([
                "departure_contributors::rename_departure_goldens",
                "--exact",
                "--ignored",
                "--nocapture",
            ])
            .env(RENAME_ENV, renames)
            .output()
            .expect("run the rename step");
        let said = format!(
            "{}{}",
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr)
        );
        assert!(!output.status.success() && said.contains(says), "{said}");
        assert_eq!(committed(root), before, "a refused rename writes nothing");
    }
}

/// The script passes each step its inputs by the variable names, and runs the
/// steps by the test names, these Rust constants and functions declare.
#[test]
fn the_script_names_the_variables_and_steps_these_constants_declare() {
    let script =
        std::fs::read_to_string(crate::repo_root().join("crates/crozier-e2e/departures-ledger.sh"))
            .expect("the script");
    for name in [
        RENAME_ENV,
        CONTRIBUTOR_ENV,
        SELECTION_ENV,
        DISCOVER_ENV,
        departures_ledger::RECORD_ENV,
        example_values_inventory::RECORD_ENV,
        "test(=departure_contributors::rename_departure_goldens)",
        "test(=departure_contributors::verify_departure_contributors)",
        CONTRIBUTORS,
    ] {
        assert!(
            script.contains(name),
            "departures-ledger.sh does not name `{name}`"
        );
    }
}

/// A selection is closed over shared tests: selecting a golden runs every
/// test recording it, and every golden those tests record is recorded whole.
#[test]
fn a_selection_closes_over_every_test_its_goldens_share() {
    let row = |golden: &str, test: &str| Contributor {
        golden: golden.to_owned(),
        binary: BINARY.to_owned(),
        test: test.to_owned(),
    };
    let inventory: BTreeSet<Contributor> = [
        row("a", "only_a"),
        row("b", "only_b"),
        row("b", "shared"),
        row("c", "shared"),
        row("c", "only_c"),
        row("d", "only_d"),
    ]
    .into();
    let pairs = |selected: &[&str]| -> Vec<String> {
        let selected: Vec<String> = selected.iter().map(|golden| (*golden).to_owned()).collect();
        selected_rows(&inventory, &selected)
            .expect("known goldens")
            .iter()
            .map(|row| format!("{}:{}", row.golden, row.test))
            .collect()
    };
    assert_eq!(pairs(&["a"]), ["a:only_a"]);
    assert_eq!(
        pairs(&["b"]),
        ["b:only_b", "b:shared", "c:only_c", "c:shared"]
    );
    assert_eq!(pairs(&[]).len(), inventory.len());
    let unknown = selected_rows(&inventory, &["e".to_owned()]).expect_err("unknown golden");
    assert!(
        unknown.contains("names no test recording [\"e\"]"),
        "{unknown}"
    );
}

/// What [`verify_departure_contributors`] reads after a recording run: the
/// notes and the two record directories.
struct Recording {
    noted: tempfile::TempDir,
    ledger: tempfile::TempDir,
    examples: tempfile::TempDir,
    /// Whether the check runs as discovery's, rewriting the inventory first.
    discover: bool,
    /// The inventory the check reads and discovery writes; the committed one if None.
    inventory: Option<std::path::PathBuf>,
}

impl Recording {
    /// The directories a run recording exactly `rows` leaves.
    fn of(rows: &BTreeSet<Contributor>) -> Self {
        let recording = Self {
            noted: tempfile::tempdir().expect("notes"),
            ledger: tempfile::tempdir().expect("ledger records"),
            examples: tempfile::tempdir().expect("example records"),
            discover: false,
            inventory: None,
        };
        let notes: String = rows.iter().map(|row| row.render() + "\n").collect();
        std::fs::write(recording.noted.path().join("run.tsv"), notes).expect("notes");
        for row in rows {
            for dir in [&recording.ledger, &recording.examples] {
                std::fs::create_dir_all(dir.path().join(row.golden.replace('/', "%")))
                    .expect("record");
            }
        }
        recording
    }

    /// The real step, as the script runs it — this suite's own binary, over
    /// the repository's committed inventories — for `selection`; its stdout
    /// when it refuses.
    fn check(&self, selection: &str) -> Result<(), String> {
        let mut command = std::process::Command::new(std::env::current_exe().expect("this suite"));
        command
            .args([
                "departure_contributors::verify_departure_contributors",
                "--exact",
                "--ignored",
                "--nocapture",
            ])
            .env(CONTRIBUTOR_ENV, self.noted.path())
            .env(departures_ledger::RECORD_ENV, self.ledger.path())
            .env(example_values_inventory::RECORD_ENV, self.examples.path())
            .env(SELECTION_ENV, selection)
            .env(DISCOVER_ENV, if self.discover { "1" } else { "0" });
        if let Some(inventory) = &self.inventory {
            command.env(INVENTORY_PATH_ENV, inventory);
        } else {
            command.env_remove(INVENTORY_PATH_ENV);
        }
        let output = command.output().expect("run the check");
        let said = format!(
            "{}{}",
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr)
        );
        if output.status.success() {
            Ok(())
        } else {
            Err(said)
        }
    }
}

/// Issue #820: the step between recording and merging accepts a selected run
/// that recorded exactly the inventory's rows for it, and refuses — naming the
/// fix — one that missed a row, recorded an unlisted one, or wrote no record
/// for a golden, and a whole run that recorded only one golden's tests.
#[test]
fn the_contributor_check_holds_a_run_to_the_inventory() {
    let root = crate::repo_root();
    let inventory =
        parse(&std::fs::read_to_string(root.join(CONTRIBUTORS)).expect("the inventory"))
            .expect("the committed inventory parses");
    let golden = inventory.first().expect("a contributor").golden.clone();
    let rows = selected_rows(&inventory, std::slice::from_ref(&golden)).expect("listed");
    if let Err(said) = Recording::of(&rows).check(&golden) {
        panic!("a run recording exactly the inventory's rows was refused:\n{said}");
    }

    let mut short = rows.clone();
    let missing = short.pop_first().expect("a row");
    let said = Recording::of(&short)
        .check(&golden)
        .expect_err("a row missing");
    assert!(
        said.contains(&format!("`{}` is inventoried as recording", missing.test))
            && said.contains(DISCOVER),
        "{said}"
    );

    let mut extra = rows.clone();
    extra.insert(Contributor {
        test: "an_unlisted_test".to_owned(),
        ..missing.clone()
    });
    let said = Recording::of(&extra)
        .check(&golden)
        .expect_err("an unlisted row");
    assert!(said.contains("`an_unlisted_test` recorded"), "{said}");

    let recording = Recording::of(&rows);
    std::fs::remove_dir(recording.ledger.path().join(golden.replace('/', "%"))).expect("unrecord");
    let said = recording.check(&golden).expect_err("a golden unrecorded");
    assert!(
        said.contains(&format!(
            "{golden}: the run wrote no departure ledger record"
        )),
        "{said}"
    );
    // An example record is owed only by a golden the committed example
    // inventory names; one it names must have been recorded.
    let named = committed_example_goldens(root).expect("the committed example inventory");
    let examined = inventory
        .iter()
        .find(|row| named.contains(&row.golden))
        .expect("an inventoried golden with example rows")
        .golden
        .clone();
    let examined_rows = selected_rows(&inventory, std::slice::from_ref(&examined)).expect("listed");
    let recording = Recording::of(&examined_rows);
    std::fs::remove_dir(recording.examples.path().join(examined.replace('/', "%")))
        .expect("unrecord");
    let said = recording
        .check(&examined)
        .expect_err("an example golden unrecorded");
    assert!(
        said.contains(&format!(
            "{examined}: the run wrote no example inventory record"
        )),
        "{said}"
    );
    if !named.contains(&golden) {
        let recording = Recording::of(&rows);
        std::fs::remove_dir(recording.examples.path().join(golden.replace('/', "%")))
            .expect("unrecord");
        if let Err(said) = recording.check(&golden) {
            panic!("a golden with no example rows owes no example record:\n{said}");
        }
    }

    if rows.len() < inventory.len() {
        let said = Recording::of(&rows)
            .check("")
            .expect_err("a partial whole run");
        assert!(said.contains("is inventoried as recording"), "{said}");
    }
}

/// Issue #820: discovery's own step replaces the inventory with what the whole
/// run recorded — a test it no longer lists dropped, a new one added — and then
/// holds the run to it, through the real verifier, over a scratch copy.
#[test]
fn discovery_rewrites_the_inventory_from_what_the_run_recorded() {
    let root = crate::repo_root();
    let committed =
        parse(&std::fs::read_to_string(root.join(CONTRIBUTORS)).expect("the inventory"))
            .expect("parses");
    let mut rows = committed.clone();
    let dropped = rows.pop_first().expect("a row");
    rows.insert(Contributor {
        test: "a_comparison_added_since".to_owned(),
        ..dropped.clone()
    });
    let scratch = tempfile::tempdir().expect("scratch");
    let inventory = scratch.path().join("departures-contributors.tsv");
    std::fs::write(&inventory, render(&committed)).expect("the copy");
    let mut recording = Recording::of(&rows);
    recording.discover = true;
    recording.inventory = Some(inventory.clone());
    if let Err(said) = recording.check("") {
        panic!("discovery was refused:\n{said}");
    }
    let written = std::fs::read_to_string(&inventory).expect("the rewritten inventory");
    assert_eq!(
        written,
        render(&rows),
        "discovery writes exactly the rows the run recorded"
    );
    assert!(written.contains("a_comparison_added_since"));
    // Without discovery the same run is held to the inventory it differs from.
    let mut held = Recording::of(&rows);
    held.inventory = Some(scratch.path().join("held.tsv"));
    std::fs::write(held.inventory.as_ref().expect("set"), render(&committed)).expect("the copy");
    let said = held
        .check("")
        .expect_err("a run the inventory does not describe");
    assert!(
        said.contains("`a_comparison_added_since` recorded"),
        "{said}"
    );
}

/// Every compared golden has an inventoried contributor, except those only an
/// ignored journey compares ([`JOURNEY_ONLY_GOLDENS`]): a new comparison
/// missing from the inventory would never run in a selected regeneration, so
/// its golden fails here until `just departures-ledger --discover-contributors`.
#[test]
fn every_compared_golden_has_a_contributor_or_is_journey_only() {
    let root = crate::repo_root();
    let inventory =
        parse(&std::fs::read_to_string(root.join(CONTRIBUTORS)).expect("the inventory"))
            .expect("parses");
    let inventoried: BTreeSet<&str> = inventory.iter().map(|row| row.golden.as_str()).collect();
    let compared = Inventory::read(root).expect("the compared goldens");
    let uncovered: Vec<&str> = compared
        .goldens
        .keys()
        .map(String::as_str)
        .filter(|golden| !inventoried.contains(golden))
        .collect();
    assert_eq!(
        uncovered,
        JOURNEY_ONLY_GOLDENS.to_vec(),
        "a compared golden no inventoried test records: rederive the inventory with `{DISCOVER}`"
    );
}
