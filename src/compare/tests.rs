//! In-process tests of `crozier compare` over real temporary repositories, the
//! committed fixture specs and goldens, and real `sh` reference commands.

use std::path::{Path, PathBuf};

use super::*;

/// The `client-class-name` fixture: a small spec with a packaged and a flat
/// golden, generated with package `fern`, project `default_package_name` and
/// client class `AcmeClient`.
fn fixture(rel: &str) -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures/client-class-name")
        .join(rel)
}

/// The generator settings the fixture's goldens were produced with.
fn golden_settings(layout: &str) -> String {
    format!(
        "    spec: {}\n    package-name: fern\n    project-name: default_package_name\n    client-class-name: AcmeClient\n    layout: {layout}\n",
        fixture("openapi.yml").display()
    )
}

/// A reference command copying a committed golden into place.
fn copy_golden(golden: &str) -> String {
    format!(
        "cp -R '{}/.' \"$CROZIER_REFERENCE_OUTPUT\"",
        fixture(golden).display()
    )
}

struct Run {
    code: Result<u8, String>,
    stderr: String,
    stdout: String,
}

fn compare(options: &Options, cwd: &Path, color: bool, shell_supported: bool) -> Run {
    let mut stderr = Vec::new();
    let mut stdout = Vec::new();
    let code = {
        let mut io = Io {
            stderr: &mut stderr,
            stdout: &mut stdout,
            color,
            shell_supported,
        };
        run(options, cwd, &mut io)
    };
    Run {
        code,
        stderr: String::from_utf8(stderr).unwrap(),
        stdout: String::from_utf8(stdout).unwrap(),
    }
}

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().unwrap()).unwrap();
    std::fs::write(path, text).unwrap();
}

fn read_report(path: &Path) -> Report {
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}

fn result_for<'a>(
    report: &'a Report,
    config: &str,
    generator: Option<&str>,
) -> &'a GeneratorResult {
    report
        .results
        .iter()
        .find(|r| r.config_file == config && r.generator.as_deref() == generator)
        .unwrap_or_else(|| panic!("no result for {config} {generator:?}: {report:#?}"))
}

#[test]
fn every_status_in_one_run_with_json_and_diffs() {
    let repo = tempfile::tempdir().unwrap();
    let root = repo.path();
    write(
        root,
        "crozier.yml",
        &format!(
            "generators:\n  packaged:\n{}    reference:\n      command: {}\n  flat:\n{}    reference:\n      command: {}\n  edited:\n{}    reference:\n      command: {} && echo changed >> \"$CROZIER_REFERENCE_OUTPUT/README.md\" && rm \"$CROZIER_REFERENCE_OUTPUT/reference.md\" && touch \"$CROZIER_REFERENCE_OUTPUT/extra.txt\"\n  failing:\n{}    reference:\n      command: echo the reference tool refused the spec >&2; exit 5\n  silent:\n{}    reference:\n      command: 'true'\n  unconfigured:\n{}",
            golden_settings("packaged"),
            copy_golden("expected"),
            golden_settings("flat"),
            copy_golden("expected-flat"),
            golden_settings("packaged"),
            copy_golden("expected"),
            golden_settings("packaged"),
            golden_settings("packaged"),
            golden_settings("packaged"),
        ),
    );
    write(root, "broken/crozier.yml", "generators: [not, a, map]\n");
    write(
        root,
        "nospec/.crozier.yml",
        "generators:\n  python:\n    reference:\n      command: 'true'\n",
    );

    let options = Options {
        paths: vec![],
        reference_command: None,
        json: Some(PathBuf::from("report.json")),
        diff_dir: Some(PathBuf::from("diffs")),
    };
    let run = compare(&options, root, false, true);
    assert_eq!(run.code, Ok(3), "{}", run.stderr);
    assert!(run.stdout.is_empty());
    let report = read_report(&root.join("report.json"));
    assert_eq!(report.exit_code, 3);
    assert_eq!(report.searched_paths, [root.display().to_string()]);
    assert_eq!(
        (
            report.counts.matched,
            report.counts.mismatched,
            report.counts.could_not_check
        ),
        (2, 1, 5)
    );

    let packaged = result_for(&report, "crozier.yml", Some("packaged"));
    assert_eq!(packaged.status, Status::Matched);
    let comparison = packaged.comparison.as_ref().unwrap();
    assert_eq!(comparison.layout, ComparedLayout::Packaged);
    assert!(comparison.files_compared >= 40, "{comparison:?}");
    assert_eq!(comparison.diff_file, None);
    let timing = packaged.timing.unwrap();
    let (r, c) = (
        timing.reference_seconds.unwrap(),
        timing.crozier_seconds.unwrap(),
    );
    assert_eq!(timing.speedup, Some(r / c));
    assert_eq!(timing.saved_seconds, Some(r - c));
    assert_eq!(
        packaged.spec,
        Some(fixture("openapi.yml").display().to_string())
    );

    let flat = result_for(&report, "crozier.yml", Some("flat"));
    assert_eq!(flat.status, Status::Matched);
    assert_eq!(
        flat.comparison.as_ref().unwrap().layout,
        ComparedLayout::Flat
    );

    let edited = result_for(&report, "crozier.yml", Some("edited"));
    assert_eq!(edited.status, Status::Mismatched);
    let comparison = edited.comparison.as_ref().unwrap();
    assert_eq!(comparison.differing, ["README.md"]);
    assert_eq!(comparison.only_in_reference, ["extra.txt"]);
    assert_eq!(comparison.only_in_crozier, ["reference.md"]);
    let diff_file = comparison.diff_file.as_ref().unwrap();
    assert_eq!(diff_file, "diffs/003-crozier.yml-edited.diff");
    let diff = std::fs::read_to_string(root.join(diff_file)).unwrap();
    assert!(
        diff.contains("--- reference/README.md\n+++ crozier/README.md\n"),
        "{diff}"
    );
    assert!(diff.contains("- changed"), "{diff}");
    assert!(diff.contains("Only in reference: extra.txt"), "{diff}");
    assert!(diff.contains("Only in crozier: reference.md"), "{diff}");
    assert!(!diff.contains('\u{1b}'));

    let failing = result_for(&report, "crozier.yml", Some("failing"));
    assert_eq!(failing.status, Status::CouldNotCheck);
    let reference = failing.reference.as_ref().unwrap();
    assert_eq!(reference.exit_code, Some(5));
    assert_eq!(
        reference.diagnostic.as_deref(),
        Some("the reference tool refused the spec")
    );
    assert!(failing
        .reason
        .as_deref()
        .unwrap()
        .starts_with("the reference command exited with status 5"));
    let timing = failing.timing.unwrap();
    assert!(timing.reference_seconds.is_some());
    assert_eq!((timing.crozier_seconds, timing.speedup), (None, None));

    let silent = result_for(&report, "crozier.yml", Some("silent"));
    assert_eq!(silent.status, Status::CouldNotCheck);
    assert!(
        silent.reason.as_deref().unwrap().contains("empty"),
        "{silent:?}"
    );
    assert_eq!(silent.reference.as_ref().unwrap().exit_code, Some(0));

    let unconfigured = result_for(&report, "crozier.yml", Some("unconfigured"));
    assert_eq!(unconfigured.reason.as_deref(), Some(NO_REFERENCE_COMMAND));
    assert_eq!(
        (&unconfigured.reference, &unconfigured.timing),
        (&None, &None)
    );

    let broken = result_for(&report, "broken/crozier.yml", None);
    assert_eq!(broken.status, Status::CouldNotCheck);
    assert!(broken.reason.as_deref().unwrap().contains("invalid config"));

    let nospec = result_for(&report, "nospec/.crozier.yml", Some("python"));
    assert!(
        nospec.reason.as_deref().unwrap().contains("has no spec"),
        "{nospec:?}"
    );
    assert_eq!(nospec.spec, None);

    // Progress names each config and each side of each generator as it goes.
    for want in [
        "compare: found config crozier.yml",
        "compare: found config broken/crozier.yml",
        "compare: crozier.yml packaged: reference command starting: cp -R",
        "compare: crozier.yml packaged: reference command finished in ",
        "compare: crozier.yml packaged: crozier generation starting",
        "compare: crozier.yml packaged: crozier generation finished in ",
        "compare: crozier.yml packaged: matched",
        "compare: crozier.yml edited: mismatched",
        "compare: crozier.yml failing: could_not_check (the reference command exited with status 5:)",
        "crozier compare report",
        "Result: 1 generator(s) mismatched the reference (exit 3)",
    ] {
        assert!(run.stderr.contains(want), "missing {want:?} in:\n{}", run.stderr);
    }
    assert!(!run.stderr.contains('\u{1b}'));
}

#[test]
fn the_reference_command_receives_resolved_settings_with_defaults() {
    let repo = tempfile::tempdir().unwrap();
    let dump = tempfile::tempdir().unwrap();
    let root = repo.path();
    write(
        root,
        "svc/openapi.yml",
        &std::fs::read_to_string(fixture("openapi.yml")).unwrap(),
    );
    write(
        root,
        "svc/crozier.yml",
        "spec: ./openapi.yml\naudiences: [public, internal]\ngenerators:\n  python:\n    extra-fields: forbid\n",
    );
    let dump_file = dump.path().join("env");
    let options = Options {
        paths: vec![PathBuf::from("svc")],
        reference_command: Some(format!(
            "pwd > '{0}'; env | grep '^CROZIER_REFERENCE_' | sort >> '{0}'; exit 1",
            dump_file.display()
        )),
        ..Options::default()
    };
    let run = compare(&options, root, false, true);
    assert_eq!(run.code, Ok(4), "{}", run.stderr);
    let dumped = std::fs::read_to_string(&dump_file).unwrap();
    let svc = std::fs::canonicalize(root.join("svc")).unwrap();
    let mut lines = dumped.lines();
    assert_eq!(lines.next(), Some(svc.display().to_string().as_str()));
    let vars: Vec<&str> = lines.collect();
    let output = vars
        .iter()
        .find_map(|l| l.strip_prefix("CROZIER_REFERENCE_OUTPUT="))
        .unwrap();
    assert_eq!(
        vars,
        [
            "CROZIER_REFERENCE_AUDIENCES=public,internal".to_string(),
            "CROZIER_REFERENCE_AUDIENCE_STRICT=false".to_string(),
            "CROZIER_REFERENCE_CLIENT_CLASS_NAME=WidgetApiApi".to_string(),
            format!(
                "CROZIER_REFERENCE_CONFIG_FILE={}",
                svc.join("crozier.yml").display()
            ),
            "CROZIER_REFERENCE_EXTRA_FIELDS=forbid".to_string(),
            "CROZIER_REFERENCE_GENERATOR=python".to_string(),
            "CROZIER_REFERENCE_LAYOUT=packaged".to_string(),
            format!("CROZIER_REFERENCE_OUTPUT={output}"),
            "CROZIER_REFERENCE_PACKAGE_NAME=widget_api".to_string(),
            "CROZIER_REFERENCE_PROJECT_NAME=widget_api".to_string(),
            format!(
                "CROZIER_REFERENCE_SPEC={}",
                svc.join("openapi.yml").display()
            ),
        ]
    );
    // The output directory was a fresh temporary one, gone after the run.
    assert!(!Path::new(output).exists());
}

#[test]
fn a_refused_spec_a_bad_reference_tree_and_no_shell_are_could_not_check() {
    let repo = tempfile::tempdir().unwrap();
    let root = repo.path();
    let refused =
        Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/openapi-surface/probes/header-array.yml");
    write(
        root,
        "crozier.yml",
        &format!(
            "generators:\n  refused:\n    spec: {}\n    reference:\n      command: touch \"$CROZIER_REFERENCE_OUTPUT/x\"\n  linked:\n{}    reference:\n      command: ln -s /etc/hostname \"$CROZIER_REFERENCE_OUTPUT/link\"\n  badtitle:\n    spec: {}\n    package-name: ../escape\n",
            refused.display(),
            golden_settings("packaged"),
            fixture("openapi.yml").display(),
        ),
    );
    let run = compare(&Options::default(), root, false, true);
    assert_eq!(run.code, Ok(4), "{}", run.stderr);
    let lines: Vec<&str> = run.stderr.lines().collect();
    let reason_of = |generator: &str| {
        lines
            .iter()
            .find(|l| {
                l.starts_with(&format!(
                    "compare: crozier.yml {generator}: could_not_check"
                ))
            })
            .unwrap_or_else(|| panic!("{generator}: {}", run.stderr))
            .to_string()
    };
    // A document crozier refuses is reported with crozier's own diagnostic.
    assert!(reason_of("refused").contains("unsupported array schema"));
    assert!(reason_of("linked").contains("the trees could not be compared"));
    assert!(reason_of("badtitle").contains("could not read the generator's settings"));

    // Without `sh`, every generator with a command is could-not-check, unrun.
    let run = compare(&Options::default(), root, false, false);
    assert_eq!(run.code, Ok(4));
    assert!(run.stderr.contains(NO_SHELL), "{}", run.stderr);
    assert!(!run.stderr.contains("reference command starting"));
}

#[test]
fn json_to_stdout_nothing_found_and_colour() {
    let empty = tempfile::tempdir().unwrap();
    let options = Options {
        json: Some(PathBuf::from("-")),
        ..Options::default()
    };
    let run = compare(&options, empty.path(), true, true);
    assert_eq!(run.code, Ok(0));
    let report: Report = serde_json::from_str(&run.stdout).unwrap();
    assert!(report.results.is_empty());
    assert!(!run.stdout.contains('\u{1b}'));
    assert!(run
        .stderr
        .contains("No crozier config was found under the searched paths"));
    assert!(run
        .stderr
        .contains("\u{1b}[32mResult: nothing to check (exit 0)\u{1b}[0m"));

    let repo = tempfile::tempdir().unwrap();
    write(
        repo.path(),
        "crozier.yml",
        &format!(
            "reference:\n  command: {}\ngenerators:\n  python:\n{}",
            copy_golden("expected"),
            golden_settings("packaged")
        ),
    );
    let run = compare(&options, repo.path(), true, true);
    assert_eq!(run.code, Ok(0), "{}", run.stderr);
    assert!(
        run.stderr.contains("\u{1b}[32mmatched\u{1b}[0m"),
        "{}",
        run.stderr
    );
    assert!(!run.stdout.contains('\u{1b}'));
    let report: Report = serde_json::from_str(&run.stdout).unwrap();
    assert_eq!(report.timing_totals.generators_timed, 1);
}

#[test]
fn the_command_itself_failing_writes_no_report() {
    let repo = tempfile::tempdir().unwrap();
    write(repo.path(), "file", "");
    let missing = compare(
        &Options {
            paths: vec![PathBuf::from("absent")],
            ..Options::default()
        },
        repo.path(),
        false,
        true,
    );
    assert_eq!(missing.code, Err("path not found: absent".to_string()));

    let bad_json = compare(
        &Options {
            json: Some(PathBuf::from("no/such/dir/report.json")),
            ..Options::default()
        },
        repo.path(),
        false,
        true,
    );
    assert!(bad_json.code.unwrap_err().contains("cannot write --json"));

    let bad_diffs = compare(
        &Options {
            diff_dir: Some(PathBuf::from("file/diffs")),
            ..Options::default()
        },
        repo.path(),
        false,
        true,
    );
    assert!(bad_diffs
        .code
        .unwrap_err()
        .contains("could not create --diff-dir"));
    assert!(bad_diffs.stderr.is_empty());
}

#[test]
fn diff_file_names_are_unique_and_safe() {
    assert_eq!(
        diff_file_name(7, "a b/crozier.yml", "py:thon"),
        "007-a_b_crozier.yml-py_thon.diff"
    );
    let body = render_diff(
        "c.yml",
        "g",
        &[
            (
                "bin".into(),
                Difference::Binary {
                    reference: 1,
                    crozier: 2,
                },
            ),
            ("x".into(), Difference::Processing("boom".into())),
            ("t".into(), Difference::Text(None)),
        ],
    );
    assert!(body.contains("Binary files differ: bin (reference 1 bytes, crozier 2 bytes)"));
    assert!(body.contains("Could not compare x: boom"));
    assert!(body.contains("--- reference/t\n+++ crozier/t\n"));
    assert_eq!(
        clean_join(Path::new("/a"), Path::new("./b/./c.yml")),
        PathBuf::from("/a/b/c.yml")
    );
}
