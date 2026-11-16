//! The crozier-e2e project's report scripts — `fixtures-report.sh` (`just
//! fixtures-gaps` / `just fixtures-diff`) and `departures-ledger.sh` (`just
//! departures-ledger`) — run as the recipes run them, from a scratch checkout.
//!
//! Each script's whole job is to drive `cargo` over the e2e suite and shape
//! what it printed, so `cargo` is the one thing replaced: a stand-in first on
//! PATH that records how it was called and prints (or writes) what the real
//! reporter would. Running the real `cargo` here would rebuild and rerun this
//! very suite over the whole corpus from inside itself. Everything the script
//! does with that output — the report it extracts, the summary it requires,
//! the ledger it reports, the log and fix it prints on failure — is real.

use std::os::unix::fs::PermissionsExt;
use std::path::Path;
use std::process::Command;

use crate::{DIFFS_SUMMARY, GAPS_SUMMARY};

struct Run {
    /// The scratch checkout, kept until the case has read what the script wrote.
    root: tempfile::TempDir,
    status: i32,
    stdout: String,
    stderr: String,
    calls: String,
}

/// A scratch checkout holding `script` at its repository path, and a `cargo`
/// stand-in running `cargo_body` (under `sh`, `$CALLS` its call record).
fn run_script(script: &str, args: &[&str], cargo_body: &str, setup: impl FnOnce(&Path)) -> Run {
    run_script_with(script, args, &[], cargo_body, setup)
}

/// [`run_script`], with `env` set for the script as a recipe sets it.
fn run_script_with(
    script: &str,
    args: &[&str],
    env: &[(&str, &str)],
    cargo_body: &str,
    setup: impl FnOnce(&Path),
) -> Run {
    let root = tempfile::tempdir().unwrap();
    let repo = Path::new(env!("CARGO_MANIFEST_DIR")).join("../..");
    let at = root.path().join("crates/crozier-e2e").join(script);
    std::fs::create_dir_all(at.parent().unwrap()).unwrap();
    std::fs::copy(repo.join("crates/crozier-e2e").join(script), &at).unwrap();
    let bin = root.path().join("bin");
    std::fs::create_dir(&bin).unwrap();
    let cargo = bin.join("cargo");
    // llmlint: ignore[e2e_not_mocked] a real `cargo` here would rebuild and rerun this suite inside itself; only that boundary is stood in.
    std::fs::write(
        &cargo,
        format!("#!/bin/sh\necho \"$*\" >> \"$CALLS\"\n{cargo_body}"),
    )
    .unwrap();
    std::fs::set_permissions(&cargo, std::fs::Permissions::from_mode(0o755)).unwrap();
    setup(root.path());
    let calls = root.path().join("calls");
    let path = std::env::join_paths(
        std::iter::once(bin).chain(std::env::split_paths(&std::env::var_os("PATH").unwrap())),
    )
    .unwrap();
    let mut command = Command::new("bash");
    // A recording run of `just departures-ledger` runs these tests with its own
    // arguments and record directories set; the script under test must not see them.
    for inherited in [
        "CROZIER_DEPARTURES_LEDGER_ARGS",
        "CROZIER_RECORD_DEPARTURES",
        "CROZIER_RECORD_EXAMPLE_INVENTORY",
        "CROZIER_RECORD_CONTRIBUTORS",
    ] {
        command.env_remove(inherited);
    }
    let out = command
        .arg(&at)
        .args(args)
        .env("PATH", path)
        .env("CALLS", &calls)
        .env("TMPDIR", root.path())
        .envs(env.iter().copied())
        .output()
        .unwrap();
    let leftovers: Vec<_> = std::fs::read_dir(root.path())
        .unwrap()
        .filter_map(|entry| {
            let name = entry.unwrap().file_name().into_string().unwrap();
            name.starts_with("crozier-").then_some(name)
        })
        .collect();
    assert!(leftovers.is_empty(), "the script left {leftovers:?} behind");
    Run {
        root,
        status: out.status.code().unwrap(),
        stdout: String::from_utf8(out.stdout).unwrap(),
        stderr: String::from_utf8(out.stderr).unwrap(),
        calls: std::fs::read_to_string(&calls).unwrap_or_default(),
    }
}

/// What `cargo test` prints around a reporter's report: build lines before,
/// the harness's verdict after.
fn reporter_output(report: &str) -> String {
    format!(
        "printf '%s\\n' '   Compiling crozier-e2e' 'running 1 test' {report} 'test result: ok. 1 passed'\n"
    )
}

#[test]
fn each_report_prints_only_from_its_first_corpus_through_its_summary() {
    for (mode, reporter, summary) in [
        ("gaps", "report_fixture_gaps", GAPS_SUMMARY),
        ("diff", "report_fixture_diffs", DIFFS_SUMMARY),
    ] {
        let body = reporter_output(&format!(
            "'=== petstore' '  unmatched: a.py' '2 {summary}.'"
        ));
        let run = run_script("fixtures-report.sh", &[mode], &body, |_| {});
        assert_eq!(run.status, 0, "{mode}: {}", run.stderr);
        assert_eq!(
            run.stdout,
            format!("=== petstore\n  unmatched: a.py\n2 {summary}.\n")
        );
        assert_eq!(
            run.calls,
            format!(
                "test --locked -p crozier-e2e --test e2e -- --ignored --nocapture {reporter}\n"
            )
        );
    }
}

#[test]
fn a_report_of_any_size_survives_the_temporary_file() {
    let body = format!(
        "printf '=== big\\n'\nyes 'line of a long diff' | head -n 200000\nprintf '1 {GAPS_SUMMARY}.\\n'\n"
    );
    let run = run_script("fixtures-report.sh", &["gaps"], &body, |_| {});
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(run.stdout.lines().count(), 200_002);
}

#[test]
fn a_reporter_that_prints_no_summary_fails_with_its_log_and_the_fix() {
    // `cargo test <name>` exits 0 when the name matches no test.
    let body = "printf 'running 0 tests\\ntest result: ok. 0 passed\\n'\n";
    let run = run_script("fixtures-report.sh", &["gaps"], body, |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(run.stderr.contains("running 0 tests"), "{}", run.stderr);
    assert!(
        run.stderr
            .contains("fixtures-report: no report from report_fixture_gaps (output above)"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("restore report_fixture_gaps in crates/crozier-e2e/tests/e2e.rs"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_failing_reporter_fails_with_its_log() {
    let body =
        format!("printf '=== x\\n1 {DIFFS_SUMMARY}.\\npanicked at corpus missing\\n'\nexit 101\n");
    let run = run_script("fixtures-report.sh", &["diff"], &body, |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(
        run.stderr.contains("panicked at corpus missing"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr.contains("pass a corpus that exists"),
        "{}",
        run.stderr
    );
}

#[test]
fn an_unknown_report_is_refused_with_the_usage() {
    let run = run_script("fixtures-report.sh", &["gap"], "", |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.calls, "");
    assert!(
        run.stderr.contains("unknown report 'gap'")
            && run
                .stderr
                .contains("usage: crates/crozier-e2e/fixtures-report.sh gaps|diff"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_report_given_extra_arguments_is_refused_with_the_usage() {
    for args in [&[][..], &["gaps", "unexpected"][..]] {
        let run = run_script("fixtures-report.sh", args, "", |_| {});
        assert_eq!(run.status, 1, "{args:?}: {}", run.stderr);
        assert_eq!(run.calls, "", "{args:?} ran cargo");
        assert!(
            run.stderr
                .contains(&format!("takes exactly one report, got {}", args.len()))
                && run
                    .stderr
                    .contains("usage: crates/crozier-e2e/fixtures-report.sh gaps|diff"),
            "{args:?}: {}",
            run.stderr
        );
    }
}

/// The stand-in for `cargo nextest`: the recording run leaves one record per
/// golden under `$CROZIER_RECORD_DEPARTURES` and one example-value row under
/// `$CROZIER_RECORD_EXAMPLE_INVENTORY`; the merge (`write_departures_ledger` and
/// `write_example_values_inventory`, one run) writes the ledger and the
/// inventory from them, failing as `$MERGE_FAILS` says. The rename and
/// contributor-check steps note in `$CALLS.env` what they were given, failing
/// as `$RENAME_FAILS` and `$VERIFY_FAILS` say.
// llmlint: ignore[e2e_not_mocked] A real `cargo nextest` here would rebuild and rerun this whole suite inside itself, as line 39 states; only that boundary is stood in. The recording, rename, contributor check and merge it stands in for run for real in every golden comparison, in `departure_contributors`' tests (the rename over a scratch repository, the check as this suite's own ignored step) and in `example_values_inventory::the_merge_replaces_recorded_goldens_and_keeps_every_other`, which drives the real `merge_records`.
const NEXTEST: &str = r#"case "$*" in
  *rename_departure_goldens*)
    echo "renames=$CROZIER_RENAME_GOLDENS" >> "$CALLS.env"
    [ -z "${RENAME_FAILS:-}" ] || { echo "rename refused: $RENAME_FAILS"; exit 100; } ;;
  *verify_departure_contributors*)
    [ -d "${CROZIER_RECORD_CONTRIBUTORS:-}" ] || { echo "checked without CROZIER_RECORD_CONTRIBUTORS"; exit 100; }
    echo "selection=$CROZIER_LEDGER_SELECTION discover=$CROZIER_DISCOVER_CONTRIBUTORS" >> "$CALLS.env"
    [ -z "${VERIFY_FAILS:-}" ] || { echo "contributors refused: $VERIFY_FAILS"; exit 100; } ;;
  *write_departures_ledger*write_example_values_inventory*)
    [ -z "${MERGE_FAILS:-}" ] || { echo "ledger refused: $MERGE_FAILS"; exit 100; }
    { printf 'golden\tfile\tline\tdeparture\n'; cat "$CROZIER_RECORD_DEPARTURES"/*; } > tests/fixtures/departures-ledger.tsv
    { printf 'golden\tfile\tline\targument\tfern_value\tconstraint\tmechanism\tdisposition\n'; cat "$CROZIER_RECORD_EXAMPLE_INVENTORY"/*; } > docs/departures/evidence/invalid-example-values/inventory.tsv ;;
  *)
    [ "${CROZIER_REQUIRE_CORPUS:-}" = 1 ] || { echo "recorded without CROZIER_REQUIRE_CORPUS"; exit 100; }
    [ -d "${CROZIER_RECORD_CONTRIBUTORS:-}" ] || { echo "recorded without CROZIER_RECORD_CONTRIBUTORS"; exit 100; }
    [ -z "${RECORD_FAILS:-}" ] || { echo "comparison failed: $RECORD_FAILS"; exit 100; }
    printf 'petstore\tREADME.md\t1\tbranding\n' > "$CROZIER_RECORD_DEPARTURES/petstore"
    printf 'plantstore\tREADME.md\t1\tbranding\n' > "$CROZIER_RECORD_DEPARTURES/plantstore"
    printf 'petstore\tREADME.md\t9\tpet_id\t"pet_id"\tformat=uuid\tschema-rejected-name-example\trepaired\n' > "$CROZIER_RECORD_EXAMPLE_INVENTORY/petstore" ;;
esac
"#;

/// The scratch contributor inventory: one test per store, one journey two
/// stores share, and a test of the second binary.
const CONTRIBUTORS: &str = "golden\tbinary\ttest\n\
    petstore\tcrozier-e2e::e2e\tpetstore_matches_fern_output\n\
    plantstore\tcrozier-e2e::e2e\tplantstore_matches_fern_output\n\
    plantstore\tcrozier-e2e::e2e\tstores_share_a_journey\n\
    treestore\tcrozier-e2e::e2e\tstores_share_a_journey\n\
    zoo\tcrozier-nested-discriminator-tests::nested_discriminator\tzoo_journey\n";

/// The filter term nextest selects one inventoried test by.
fn selects(binary: &str, test: &str) -> String {
    format!("binary_id(={binary}) & test(={test})")
}

/// The ledger files of a scratch checkout, as the repository commits them,
/// with the contributor inventory when `contributors` is given.
fn ledger_checkout(root: &Path, contributors: Option<&str>) {
    std::fs::create_dir_all(root.join("tests/fixtures")).unwrap();
    std::fs::write(
        root.join("tests/fixtures/departures-ledger.tsv"),
        "golden\tfile\tline\tdeparture\n",
    )
    .unwrap();
    if let Some(contributors) = contributors {
        std::fs::write(
            root.join("tests/fixtures/departures-contributors.tsv"),
            contributors,
        )
        .unwrap();
    }
    std::fs::create_dir_all(root.join("docs/departures/evidence/invalid-example-values")).unwrap();
    std::fs::write(
        root.join("docs/departures/evidence/invalid-example-values/inventory.tsv"),
        "golden\tfile\tline\targument\tfern_value\tconstraint\tmechanism\tdisposition\n",
    )
    .unwrap();
}

fn departures_ledger(env: &str) -> Run {
    departures_ledger_with(env, &[], &[], |root| {
        ledger_checkout(root, Some(CONTRIBUTORS))
    })
}

fn departures_ledger_with(
    env: &str,
    args: &[&str],
    script_env: &[(&str, &str)],
    setup: impl FnOnce(&Path),
) -> Run {
    run_script_with(
        "departures-ledger.sh",
        args,
        script_env,
        &format!("{env}{NEXTEST}"),
        setup,
    )
}

/// What the rename and contributor-check steps were given, one line each.
fn steps(run: &Run) -> String {
    std::fs::read_to_string(run.root.path().join("calls.env")).unwrap_or_default()
}

/// The `-E` filter the recording run (the first `nextest run` given both
/// packages) was given.
fn recording_filter(run: &Run) -> String {
    let call = run
        .calls
        .lines()
        .find(|call| call.contains("-p crozier-nested-discriminator-tests"))
        .unwrap_or_else(|| panic!("no recording run: {}", run.calls));
    call.split_once(" -E ").unwrap().1.to_owned()
}

#[test]
fn the_ledger_is_recorded_then_merged_and_its_rows_reported() {
    let run = departures_ledger("");
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(
        std::fs::read_to_string(run.root.path().join("tests/fixtures/departures-ledger.tsv")).unwrap(),
        "golden\tfile\tline\tdeparture\npetstore\tREADME.md\t1\tbranding\nplantstore\tREADME.md\t1\tbranding\n"
    );
    assert_eq!(
        std::fs::read_to_string(
            run.root
                .path()
                .join("docs/departures/evidence/invalid-example-values/inventory.tsv")
        )
        .unwrap(),
        "golden\tfile\tline\targument\tfern_value\tconstraint\tmechanism\tdisposition\n\
         petstore\tREADME.md\t9\tpet_id\t\"pet_id\"\tformat=uuid\tschema-rejected-name-example\trepaired\n"
    );
    assert_eq!(
        run.stdout,
        "departures-ledger: wrote tests/fixtures/departures-ledger.tsv (2 rows) and \
         docs/departures/evidence/invalid-example-values/inventory.tsv (1 rows)\n"
    );
    let calls: Vec<_> = run.calls.lines().collect();
    assert_eq!(calls.len(), 3, "{}", run.calls);
    assert!(
        calls[0].starts_with(
            "nextest run --locked -p crozier-e2e -p crozier-nested-discriminator-tests --no-fail-fast",
        ),
        "{}",
        calls[0]
    );
    // Issue #820: every inventoried test, and nothing but them — not the
    // suite's every other journey.
    assert_eq!(
        recording_filter(&run),
        [
            selects("crozier-e2e::e2e", "petstore_matches_fern_output"),
            selects("crozier-e2e::e2e", "plantstore_matches_fern_output"),
            selects("crozier-e2e::e2e", "stores_share_a_journey"),
            selects(
                "crozier-nested-discriminator-tests::nested_discriminator",
                "zoo_journey"
            ),
        ]
        .join("|")
    );
    assert!(
        calls[1].contains("--run-ignored only")
            && calls[1].contains("test(=departure_contributors::verify_departure_contributors)"),
        "{}",
        calls[1]
    );
    assert_eq!(steps(&run), "selection= discover=0\n");
    assert!(
        calls[2].contains("--run-ignored only")
            && calls[2].contains("test(=departures_ledger_gate::write_departures_ledger)")
            && calls[2].contains("test(=example_values_inventory::write_example_values_inventory)"),
        "{}",
        calls[2]
    );
}

/// A selection runs only the tests recording its goldens, closed over every
/// other golden those tests record, and says so to the contributor check —
/// given as arguments or, as the recipe forwards them, in the environment.
#[test]
fn a_selection_records_only_its_goldens_contributors() {
    let e2e = "crozier-e2e::e2e";
    for (selected, tests) in [
        ("petstore", vec!["petstore_matches_fern_output"]),
        (
            "plantstore",
            vec!["plantstore_matches_fern_output", "stores_share_a_journey"],
        ),
        (
            "treestore",
            vec!["plantstore_matches_fern_output", "stores_share_a_journey"],
        ),
    ] {
        let expected = tests
            .iter()
            .map(|test| selects(e2e, test))
            .collect::<Vec<_>>()
            .join("|");
        for forwarded in [false, true] {
            let run = if forwarded {
                departures_ledger_with(
                    "",
                    &[],
                    &[("CROZIER_DEPARTURES_LEDGER_ARGS", selected)],
                    |root| ledger_checkout(root, Some(CONTRIBUTORS)),
                )
            } else {
                departures_ledger_with("", &[selected], &[], |root| {
                    ledger_checkout(root, Some(CONTRIBUTORS))
                })
            };
            assert_eq!(run.status, 0, "{selected}: {}", run.stderr);
            assert_eq!(recording_filter(&run), expected, "{selected}");
            assert_eq!(steps(&run), format!("selection={selected} discover=0\n"));
        }
    }
}

#[test]
fn a_golden_no_inventoried_test_records_is_refused_before_cargo() {
    let run = departures_ledger_with("", &["nowhere"], &[], |root| {
        ledger_checkout(root, Some(CONTRIBUTORS))
    });
    assert_eq!(run.status, 1);
    assert_eq!(run.calls, "");
    assert!(
        run.stderr.contains(
            "departures-ledger: tests/fixtures/departures-contributors.tsv names no test recording nowhere"
        ) && run.stderr.contains("--discover-contributors"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_missing_contributor_inventory_names_how_to_derive_it() {
    let run = departures_ledger_with("", &[], &[], |root| ledger_checkout(root, None));
    assert_eq!(run.status, 1);
    assert_eq!(run.calls, "");
    assert!(
        run.stderr
            .contains("tests/fixtures/departures-contributors.tsv is missing")
            && run
                .stderr
                .contains("derive it with just departures-ledger --discover-contributors"),
        "{}",
        run.stderr
    );
}

/// The inventory becomes the recording's nextest filter, so a header or row that
/// is not one is refused, naming its line, before cargo runs.
#[test]
fn a_malformed_contributor_inventory_is_refused_before_cargo() {
    for (inventory, says) in [
        (
            "golden\ttest\npetstore\tpetstore_matches_fern_output\n",
            "departures-contributors.tsv line 1: its header is not golden/binary/test",
        ),
        (
            "golden\tbinary\ttest\npetstore\tcrozier-e2e::e2e\tpetstore) | test(=other\n",
            "departures-contributors.tsv line 2: `petstore\tcrozier-e2e::e2e\tpetstore) | test(=other` is not golden, binary id and test name",
        ),
        (
            "golden\tbinary\ttest\npetstore\tcrozier-e2e::e2e\n",
            "departures-contributors.tsv line 2: `petstore\tcrozier-e2e::e2e` is not golden, binary id and test name",
        ),
    ] {
        let run = departures_ledger_with("", &[], &[], |root| {
            ledger_checkout(root, Some(inventory))
        });
        assert_eq!(run.status, 1, "{inventory:?}");
        assert_eq!(run.calls, "", "{inventory:?}: cargo must not run");
        assert!(
            run.stderr.contains(says)
                && run
                    .stderr
                    .contains("rederive it with just departures-ledger --discover-contributors"),
            "{}",
            run.stderr
        );
    }
}

/// Discovery runs the whole suite as the recording did before the inventory,
/// less the steps' own tests, and has the check rederive the inventory.
#[test]
fn discovery_runs_the_whole_suite_and_rederives_the_inventory() {
    let run = departures_ledger_with("", &["--discover-contributors"], &[], |root| {
        ledger_checkout(root, None)
    });
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(
        recording_filter(&run),
        "not test(/^(departures_ledger_gate|departure_contributors)::/)"
    );
    assert_eq!(steps(&run), "selection= discover=1\n");
    let refused =
        departures_ledger_with("", &["--discover-contributors", "petstore"], &[], |root| {
            ledger_checkout(root, None)
        });
    assert_eq!(refused.status, 1);
    assert_eq!(refused.calls, "");
    assert!(
        refused
            .stderr
            .contains("--discover-contributors runs the whole suite, so it takes no GOLDEN"),
        "{}",
        refused.stderr
    );
}

#[test]
fn a_run_the_inventory_does_not_describe_stops_before_the_merge() {
    let run = departures_ledger("VERIFY_FAILS=unattributed\n");
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert_eq!(run.calls.lines().count(), 2, "the merge ran: {}", run.calls);
    assert!(
        run.stderr.contains("contributors refused: unattributed")
            && run.stderr.contains(
                "departures-ledger: the recording run does not match \
                 tests/fixtures/departures-contributors.tsv (above)"
            ),
        "{}",
        run.stderr
    );
}

#[test]
fn a_comparison_that_fails_while_recording_stops_before_the_merge() {
    let run = departures_ledger("RECORD_FAILS=petstore\n");
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert_eq!(
        run.calls.lines().count(),
        1,
        "the merge ran after a failed recording"
    );
    assert!(
        run.stderr.contains("comparison failed: petstore"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("departures-ledger: a comparison failed while recording (above)")
            && run
                .stderr
                .contains("fix it, then rerun just departures-ledger"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_refused_merge_fails_with_its_log_and_the_fix() {
    let run = departures_ledger("MERGE_FAILS=duplicate-row\n");
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(
        run.stderr.contains("ledger refused: duplicate-row"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("departures-ledger: the merged ledger or inventory was refused (above)"),
        "{}",
        run.stderr
    );
}

const OLD: &str = "docs/fern-measurements/area/old-case/fern-expected";
const NEW: &str = "docs/fern-measurements/area/new-case/fern-expected";

fn git(root: &Path, args: &[&str]) {
    let status = Command::new("git")
        .args([
            "-c",
            "user.name=crozier",
            "-c",
            "user.email=crozier@example.invalid",
        ])
        .args(args)
        .current_dir(root)
        .output()
        .unwrap();
    assert!(status.status.success(), "git {args:?}: {status:?}");
}

/// A scratch git checkout whose committed golden tree [`OLD`] and its source
/// document were moved to [`NEW`], then changed by `edit`.
fn moved_checkout(root: &Path, edit: impl FnOnce(&Path)) {
    ledger_checkout(root, Some(CONTRIBUTORS));
    let write = |rel: &str, text: &str| {
        let path = root.join(rel);
        std::fs::create_dir_all(path.parent().unwrap()).unwrap();
        std::fs::write(path, text).unwrap();
    };
    write(&format!("{OLD}/src/client.py"), "class Client:\n    pass\n");
    write(&format!("{OLD}/README.md"), "# Client\n");
    write(
        "docs/fern-measurements/area/old-case/openapi.yml",
        "openapi: 3.0.3\n",
    );
    git(root, &["init", "-q"]);
    git(root, &["add", "-A"]);
    git(root, &["commit", "-q", "-m", "golden"]);
    std::fs::rename(
        root.join("docs/fern-measurements/area/old-case"),
        root.join("docs/fern-measurements/area/new-case"),
    )
    .unwrap();
    edit(root);
}

/// Issue #819: an unchanged move is renamed in the committed files before
/// anything records, so the recording run's ledger load finds the new path.
// llmlint: ignore[shell_test_tiers_stay_split] `git` is part of every lane's base toolchain (this suite already shells out to it), and the rename step verifies a moved tree's bytes against the commit it moved from, which only a real repository has; the case stays offline, installs nothing and reaches no network.
#[test]
fn a_moved_golden_is_renamed_before_anything_records() {
    let rename = format!("{OLD}={NEW}");
    let run = departures_ledger_with("", &["--rename", &rename], &[], |root| {
        moved_checkout(root, |_| {})
    });
    assert_eq!(run.status, 0, "{}", run.stderr);
    let calls: Vec<_> = run.calls.lines().collect();
    assert_eq!(calls.len(), 4, "{}", run.calls);
    assert!(
        calls[0].contains("--run-ignored only")
            && calls[0].contains("test(=departure_contributors::rename_departure_goldens)"),
        "{}",
        calls[0]
    );
    assert!(
        steps(&run).starts_with(&format!("renames={rename}\n")),
        "{}",
        steps(&run)
    );
    let refused = departures_ledger_with(
        "RENAME_FAILS=collision\n",
        &[&format!("--rename={rename}")],
        &[],
        |root| moved_checkout(root, |_| {}),
    );
    assert_eq!(refused.status, 1);
    assert_eq!(
        refused.calls.lines().count(),
        1,
        "recorded after a refused rename"
    );
    assert!(
        refused.stderr.contains("rename refused: collision")
            && refused
                .stderr
                .contains("departures-ledger: the rename was refused (above)"),
        "{}",
        refused.stderr
    );
}

/// What a refused rename names, and the edit to the moved tree that earns it.
type RefusedRename = (&'static str, fn(&Path));

/// A rename is only for a byte-preserving move: a changed file, an added one,
/// a changed or missing source document, or a tree still at its old path is
/// refused before cargo runs, naming what differs.
// llmlint: ignore[shell_test_tiers_stay_split] `git` is part of every lane's base toolchain (this suite already shells out to it), and the rename step verifies a moved tree's bytes against the commit it moved from, which only a real repository has; the case stays offline, installs nothing and reaches no network.
#[test]
fn a_changed_or_copied_golden_is_refused_as_a_rename() {
    let rename = format!("--rename={OLD}={NEW}");
    let cases: [RefusedRename; 5] = [
        ("differs from", |root| {
            std::fs::write(root.join(NEW).join("README.md"), "# Client!\n").unwrap()
        }),
        ("does not hold exactly the files of", |root| {
            std::fs::write(root.join(NEW).join("extra.py"), "").unwrap()
        }),
        (
            "is not docs/fern-measurements/area/old-case/openapi.yml at HEAD",
            |root| {
                std::fs::write(
                    root.join("docs/fern-measurements/area/new-case/openapi.yml"),
                    "openapi: 3.1.0\n",
                )
                .unwrap()
            },
        ),
        (
            "is not docs/fern-measurements/area/old-case/openapi.yml at HEAD",
            |root| {
                std::fs::remove_file(root.join("docs/fern-measurements/area/new-case/openapi.yml"))
                    .unwrap()
            },
        ),
        ("still exists, so it was copied, not moved", |root| {
            std::fs::create_dir_all(root.join(OLD)).unwrap()
        }),
    ];
    for (says, edit) in cases {
        let run = departures_ledger_with("", &[&rename], &[], |root| moved_checkout(root, edit));
        assert_eq!(run.status, 1, "{says}");
        assert_eq!(run.calls, "", "{says}: cargo ran");
        assert!(run.stderr.contains(says), "{says}: {}", run.stderr);
    }
    let malformed = departures_ledger_with("", &["--rename", "no-equals-sign"], &[], |root| {
        moved_checkout(root, |_| {})
    });
    assert_eq!(malformed.status, 1);
    assert!(
        malformed
            .stderr
            .contains("--rename 'no-equals-sign' is not OLD=NEW"),
        "{}",
        malformed.stderr
    );
}
