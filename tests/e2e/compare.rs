//! `crozier compare` journeys: the compiled binary over real temporary git
//! repositories, with small shell scripts as the reference commands — a user's
//! reference command is just a command, so a script that copies a committed
//! golden into `$CROZIER_REFERENCE_OUTPUT` is a real input, not a double.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

use super::crozier;

/// The fixture whose committed packaged and flat goldens the references copy:
/// generated with package `fern`, project `default_package_name` and client
/// class `AcmeClient`.
const FIXTURE: &str = "client-class-name";

fn fixture_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures")
        .join(FIXTURE)
}

/// The settings the fixture's goldens were produced under, as config lines at
/// `indent`.
fn golden_naming(indent: &str) -> String {
    format!(
        "{indent}package-name: fern\n{indent}project-name: default_package_name\n{indent}client-class-name: AcmeClient\n"
    )
}

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().unwrap()).unwrap();
    std::fs::write(path, text).unwrap();
}

fn write_script(root: &Path, rel: &str, body: &str) {
    write(root, rel, &format!("#!/bin/sh\nset -eu\n{body}"));
    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;
        std::fs::set_permissions(root.join(rel), std::fs::Permissions::from_mode(0o755)).unwrap();
    }
}

fn git(root: &Path, args: &[&str]) {
    let status = std::process::Command::new("git")
        .env_remove("GIT_DIR")
        .env_remove("GIT_WORK_TREE")
        .env_remove("GIT_INDEX_FILE")
        .arg("-C")
        .arg(root)
        .args(args)
        .status()
        .expect("run git");
    assert!(status.success(), "git {args:?}");
}

/// A repository a migrating team might have: two configs with several
/// generators, every status among them, a git-ignored config that must not be
/// found, and reference scripts that write only to `$CROZIER_REFERENCE_OUTPUT`.
fn migration_repo() -> tempfile::TempDir {
    let repo = tempfile::tempdir().expect("repo tempdir");
    let root = repo.path();
    git(root, &["init", "-q"]);
    write(root, ".gitignore", "ignored/\n");
    write(
        root,
        "openapi.yml",
        &std::fs::read_to_string(fixture_root().join("openapi.yml")).unwrap(),
    );
    // `reference.sh <golden> [edit]`: copy a committed golden, optionally
    // editing it so the reference differs.
    write_script(
        root,
        "scripts/reference.sh",
        &format!(
            "cp -R '{}'/\"$1\"/. \"$CROZIER_REFERENCE_OUTPUT\"\n\
             if [ \"${{2:-}}\" = edit ]; then echo 'an edited line' >> \"$CROZIER_REFERENCE_OUTPUT/README.md\"; fi\n",
            fixture_root().display()
        ),
    );
    write_script(
        root,
        "scripts/refuse.sh",
        "echo 'reference tool: this document is not supported' >&2\nexit 9\n",
    );
    write(
        root,
        "crozier.yml",
        &format!(
            "spec: ./openapi.yml\noutput: ./sdk\n{}\
             reference:\n  command: ./scripts/reference.sh expected\n\
             generators:\n\
             \x20 packaged: {{}}\n\
             \x20 flat:\n    layout: flat\n    reference:\n      command: ./scripts/reference.sh expected-flat\n\
             \x20 edited:\n    reference:\n      command: ./scripts/reference.sh expected edit\n\
             \x20 packaged-into-flat:\n    layout: flat\n\
             \x20 refused:\n    reference:\n      command: ./scripts/refuse.sh\n",
            golden_naming("")
        ),
    );
    write(
        root,
        "services/billing/.crozier.yml",
        &format!(
            "spec: ../../openapi.yml\n{}generators:\n  billing:\n    reference:\n      command: ../../scripts/reference.sh expected\n  unconfigured: {{}}\n",
            golden_naming("")
        ),
    );
    write(root, "ignored/crozier.yml", "spec: ./nope.yml\n");
    repo
}

/// Every file under `root` (`.git` included) with its bytes.
fn snapshot(root: &Path) -> BTreeMap<PathBuf, Vec<u8>> {
    fn rec(base: &Path, dir: &Path, out: &mut BTreeMap<PathBuf, Vec<u8>>) {
        for entry in std::fs::read_dir(dir).unwrap() {
            let path = entry.unwrap().path();
            if path.is_dir() {
                rec(base, &path, out);
            } else {
                out.insert(
                    path.strip_prefix(base).unwrap().to_path_buf(),
                    std::fs::read(&path).unwrap(),
                );
            }
        }
    }
    let mut out = BTreeMap::new();
    rec(root, root, &mut out);
    out
}

fn compare_cmd(cwd: &Path) -> assert_cmd::Command {
    let mut cmd = crozier();
    cmd.current_dir(cwd)
        .arg("compare")
        .env_remove("NO_COLOR")
        .env_remove("CLICOLOR_FORCE");
    cmd
}

fn result<'a>(
    report: &'a serde_json::Value,
    config: &str,
    generator: &str,
) -> &'a serde_json::Value {
    report["results"]
        .as_array()
        .unwrap()
        .iter()
        .find(|r| r["config_file"] == config && r["generator"] == generator)
        .unwrap_or_else(|| panic!("no result for {config} {generator}: {report:#}"))
}

// Unix only: crozier runs reference commands under `sh` on Linux and macOS;
// on Windows it runs none (`compare_on_windows_runs_no_reference_command`).
#[cfg(unix)]
#[test]
fn compare_checks_every_generator_and_reports_each_status() {
    let repo = migration_repo();
    let root = repo.path();
    let outputs = tempfile::tempdir().unwrap();
    let json = outputs.path().join("report.json");
    let diffs = outputs.path().join("diffs");
    let before = snapshot(root);

    let out = compare_cmd(root)
        .arg("--json")
        .arg(&json)
        .arg("--diff-dir")
        .arg(&diffs)
        .output()
        .unwrap();
    let stderr = String::from_utf8(out.stderr).unwrap();
    // A mismatch dominates the exit status.
    assert_eq!(out.status.code(), Some(3), "{stderr}");
    assert!(out.stdout.is_empty());

    // crozier's own writes left the searched tree byte-for-byte as it was.
    let after = snapshot(root);
    let changed: Vec<&PathBuf> = before
        .keys()
        .chain(after.keys())
        .filter(|path| before.get(*path) != after.get(*path))
        .collect();
    assert!(
        changed.is_empty(),
        "compare changed the searched tree: {changed:?}"
    );

    let report: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(&json).unwrap()).unwrap();
    validate_against_committed_schema(&report);
    assert_eq!(report["exit_code"], 3);
    assert_eq!(
        report["counts"],
        serde_json::json!({"matched": 3, "mismatched": 2, "could_not_check": 2})
    );
    // The git-ignored config was never found; both others were, every
    // generator of each was checked, and a failure skipped nothing after it.
    let configs: Vec<&str> = report["results"]
        .as_array()
        .unwrap()
        .iter()
        .map(|r| r["config_file"].as_str().unwrap())
        .collect();
    assert_eq!(configs.len(), 7);
    assert!(!configs.iter().any(|c| c.starts_with("ignored")));

    let packaged = result(&report, "crozier.yml", "packaged");
    assert_eq!(packaged["status"], "matched");
    assert_eq!(packaged["comparison"]["layout"], "packaged");
    assert_eq!(
        packaged["reference"]["command"],
        "./scripts/reference.sh expected"
    );
    assert_eq!(packaged["reference"]["exit_code"], 0);

    // A `layout: flat` generator matches the committed flat golden.
    let flat = result(&report, "crozier.yml", "flat");
    assert_eq!(flat["status"], "matched");
    assert_eq!(flat["comparison"]["layout"], "flat");

    // A packaged reference handed to a flat generator is simply a mismatch:
    // the whole trees are compared, with no layout detection.
    let crossed = result(&report, "crozier.yml", "packaged-into-flat");
    assert_eq!(crossed["status"], "mismatched");
    assert_eq!(crossed["comparison"]["layout"], "flat");
    let only_ref = crossed["comparison"]["only_in_reference"]
        .as_array()
        .unwrap();
    assert!(
        only_ref.iter().any(|p| p == "pyproject.toml"),
        "{crossed:#}"
    );
    let only_crozier = crossed["comparison"]["only_in_crozier"].as_array().unwrap();
    assert!(
        only_crozier.iter().any(|p| p == "__init__.py"),
        "{crossed:#}"
    );

    let edited = result(&report, "crozier.yml", "edited");
    assert_eq!(edited["status"], "mismatched");
    assert_eq!(
        edited["comparison"]["differing"],
        serde_json::json!(["README.md"])
    );
    let diff_file = edited["comparison"]["diff_file"].as_str().unwrap();
    let diff = std::fs::read_to_string(diff_file).unwrap();
    assert!(diff.contains("--- reference/README.md"), "{diff}");
    assert!(diff.contains("- an edited line"), "{diff}");
    assert!(Path::new(crossed["comparison"]["diff_file"].as_str().unwrap()).is_file());
    // One diff file per mismatched generator, and nothing else.
    assert_eq!(std::fs::read_dir(&diffs).unwrap().count(), 2);
    assert_eq!(packaged["comparison"]["diff_file"], serde_json::Value::Null);

    // A failing reference command: could-not-check with its own diagnostic.
    let refused = result(&report, "crozier.yml", "refused");
    assert_eq!(refused["status"], "could_not_check");
    assert_eq!(refused["reference"]["exit_code"], 9);
    assert_eq!(
        refused["reference"]["diagnostic"],
        "reference tool: this document is not supported"
    );
    assert_eq!(refused["timing"]["speedup"], serde_json::Value::Null);
    assert!(refused["timing"]["reference_seconds"].is_number());

    // Relative paths resolve against the config's own directory.
    let billing = result(&report, "services/billing/.crozier.yml", "billing");
    assert_eq!(billing["status"], "matched", "{billing:#}");
    let spec = std::fs::canonicalize(root).unwrap().join("openapi.yml");
    assert_eq!(billing["spec"], spec.display().to_string());

    let unconfigured = result(&report, "services/billing/.crozier.yml", "unconfigured");
    assert_eq!(unconfigured["status"], "could_not_check");
    assert_eq!(unconfigured["reference"], serde_json::Value::Null);
    let reason = unconfigured["reason"].as_str().unwrap();
    assert!(reason.contains("`reference.command`"), "{reason}");
    assert!(reason.contains("--reference-command"), "{reason}");

    // Timings: both sides per matched generator, and totals over those where
    // both ran (every compared generator: 3 matched + 2 mismatched).
    let timing = &packaged["timing"];
    let (r, c) = (
        timing["reference_seconds"].as_f64().unwrap(),
        timing["crozier_seconds"].as_f64().unwrap(),
    );
    assert!((timing["speedup"].as_f64().unwrap() - r / c).abs() < 1e-9);
    assert!((timing["saved_seconds"].as_f64().unwrap() - (r - c)).abs() < 1e-9);
    assert_eq!(report["timing_totals"]["generators_timed"], 5);

    // Progress as it happens, then one collated report.
    for want in [
        "compare: found config crozier.yml",
        "compare: found config services/billing/.crozier.yml",
        "compare: crozier.yml packaged: reference command starting: ./scripts/reference.sh expected",
        "compare: crozier.yml packaged: crozier generation finished in",
        "compare: crozier.yml refused: could_not_check (the reference command exited with status 9)",
        "crozier compare report",
        "    differing (1):\n      README.md",
        "    reference command: ./scripts/refuse.sh",
        "reference tool: this document is not supported",
        "Timing totals (5 generator(s) where both sides ran)",
        "Result: 2 generator(s) mismatched the reference (exit 3)",
    ] {
        assert!(stderr.contains(want), "missing {want:?} in:\n{stderr}");
    }
    // The command's own text never names the reference's tool.
    assert!(
        !stderr.contains("Fern") && !stderr.contains("fern generate"),
        "{stderr}"
    );
}

// Unix only: crozier runs reference commands under `sh` on Linux and macOS;
// on Windows it runs none (`compare_on_windows_runs_no_reference_command`).
#[cfg(unix)]
#[test]
fn compare_narrows_to_a_directory_or_a_file() {
    let repo = migration_repo();
    let root = repo.path();
    let out = compare_cmd(root)
        .args(["services", "--json", "-"])
        .output()
        .unwrap();
    // The narrowed run holds one match and one could-not-check: exit 4.
    assert_eq!(out.status.code(), Some(4));
    let report: serde_json::Value = serde_json::from_slice(&out.stdout).unwrap();
    assert_eq!(report["searched_paths"], serde_json::json!(["services"]));
    let found: Vec<&str> = report["results"]
        .as_array()
        .unwrap()
        .iter()
        .map(|r| r["config_file"].as_str().unwrap())
        .collect();
    assert_eq!(
        found,
        [
            "services/billing/.crozier.yml",
            "services/billing/.crozier.yml"
        ]
    );

    // A file is a config whatever its name; the flag overrides its command.
    write(
        root,
        "ci/team-config.yaml",
        &format!("spec: ../openapi.yml\n{}layout: flat\n", golden_naming("")),
    );
    let out = compare_cmd(root)
        .args(["ci/team-config.yaml", "--json", "-", "--reference-command"])
        .arg("../scripts/reference.sh expected-flat")
        .output()
        .unwrap();
    assert_eq!(
        out.status.code(),
        Some(0),
        "{}",
        String::from_utf8_lossy(&out.stderr)
    );
    let report: serde_json::Value = serde_json::from_slice(&out.stdout).unwrap();
    let only = result(&report, "ci/team-config.yaml", "python");
    assert_eq!(only["status"], "matched");
    assert_eq!(
        only["reference"]["command"],
        "../scripts/reference.sh expected-flat"
    );
    assert_eq!(report["results"].as_array().unwrap().len(), 1);
}

/// On Windows crozier runs no reference command: every generator is
/// could-not-check, naming why, the run exits 4, and the tree is unchanged.
#[cfg(windows)]
#[test]
fn compare_on_windows_runs_no_reference_command() {
    let repo = migration_repo();
    let root = repo.path();
    let before = snapshot(root);
    let out = compare_cmd(root).args(["--json", "-"]).output().unwrap();
    let stderr = String::from_utf8(out.stderr).unwrap();
    assert_eq!(out.status.code(), Some(4), "{stderr}");
    assert_eq!(snapshot(root), before);
    let report: serde_json::Value = serde_json::from_slice(&out.stdout).unwrap();
    validate_against_committed_schema(&report);
    assert_eq!(
        report["counts"],
        serde_json::json!({"matched": 0, "mismatched": 0, "could_not_check": 7})
    );
    let packaged = result(&report, "crozier.yml", "packaged");
    assert_eq!(
        packaged["reference"]["command"],
        "./scripts/reference.sh expected"
    );
    let reason = packaged["reason"].as_str().unwrap();
    assert!(reason.contains("does not support on Windows"), "{reason}");
    let unconfigured = result(&report, "services/billing/.crozier.yml", "unconfigured");
    assert!(unconfigured["reason"]
        .as_str()
        .unwrap()
        .contains("`reference.command`"));
    assert!(!stderr.contains("reference command starting"), "{stderr}");
}

#[test]
fn compare_with_nothing_found_or_a_missing_path() {
    let empty = tempfile::tempdir().unwrap();
    compare_cmd(empty.path())
        .assert()
        .code(0)
        .stderr(predicates::str::contains(
            "No crozier config was found under the searched paths",
        ))
        .stderr(predicates::str::contains(
            "Result: nothing to check (exit 0)",
        ));

    let outputs = tempfile::tempdir().unwrap();
    let json = outputs.path().join("report.json");
    compare_cmd(empty.path())
        .arg("does/not/exist")
        .arg("--json")
        .arg(&json)
        .assert()
        .code(1)
        .stderr(predicates::str::contains("path not found: does/not/exist"));
    assert!(!json.exists(), "a failed command writes no report");

    // An unwritable --json is the command failing too.
    compare_cmd(empty.path())
        .args(["--json", "no/such/dir/report.json"])
        .assert()
        .code(1)
        .stderr(predicates::str::contains("cannot write --json"));
}

/// The reference command receives exactly the generator's resolved settings
/// from its config file, defaults included — and `CROZIER_*` generation
/// variables in the caller's environment change neither what crozier generates
/// nor what the command receives. Unix only, as above.
#[cfg(unix)]
#[test]
fn compare_hands_the_config_files_settings_to_the_reference_command() {
    let repo = tempfile::tempdir().unwrap();
    let dumps = tempfile::tempdir().unwrap();
    let root = repo.path();
    write(
        root,
        "api/openapi.yml",
        &std::fs::read_to_string(fixture_root().join("openapi.yml")).unwrap(),
    );
    write_script(
        root,
        "dump.sh",
        &format!(
            "env | grep '^CROZIER_REFERENCE_' | sort > '{}'/\"$CROZIER_REFERENCE_GENERATOR\"\n\
             if [ \"$CROZIER_REFERENCE_GENERATOR\" = golden ]; then cp -R '{}'/expected/. \"$CROZIER_REFERENCE_OUTPUT\"; fi\n",
            dumps.path().display(),
            fixture_root().display()
        ),
    );
    write(
        root,
        "api/crozier.yml",
        &format!(
            "spec: ./openapi.yml\nreference:\n  command: ../dump.sh\ngenerators:\n  golden:\n{}  defaults:\n    audiences: [public, internal]\n    audience-strict: true\n    extra-fields: ignore\n",
            golden_naming("    ")
        ),
    );

    let out = compare_cmd(root)
        .args(["--json", "-"])
        .env("CROZIER_SPEC", "/nowhere/else.yml")
        .env("CROZIER_OUTPUT", root.join("env-output"))
        .env("CROZIER_PACKAGE_NAME", "from_env")
        .env("CROZIER_PROJECT_NAME", "from-env")
        .env("CROZIER_CLIENT_CLASS_NAME", "FromEnv")
        .env("CROZIER_AUDIENCES", "admin")
        .env("CROZIER_AUDIENCE_STRICT", "false")
        .env("CROZIER_EXTRA_FIELDS", "forbid")
        .env("CROZIER_LAYOUT", "flat")
        .env("CROZIER_CONFIG", "/nowhere/crozier.yml")
        .output()
        .unwrap();
    let stderr = String::from_utf8_lossy(&out.stderr);
    let report: serde_json::Value = serde_json::from_slice(&out.stdout).unwrap();
    // The golden generator still generates packaged `fern` and matches.
    assert_eq!(
        result(&report, "api/crozier.yml", "golden")["status"],
        "matched",
        "{stderr}"
    );
    // The other wrote nothing: could-not-check, so exit 4.
    assert_eq!(out.status.code(), Some(4), "{stderr}");
    assert!(!root.join("env-output").exists());

    let api = std::fs::canonicalize(root.join("api")).unwrap();
    // Both sides are sorted here, in Rust: the stub's `sort` collates by the
    // host's locale, which orders `_` differently on macOS than on Linux.
    let sorted = |mut lines: Vec<String>| {
        lines.sort();
        lines
    };
    let vars = |generator: &str| -> Vec<String> {
        sorted(
            std::fs::read_to_string(dumps.path().join(generator))
                .unwrap()
                .lines()
                .filter(|l| !l.starts_with("CROZIER_REFERENCE_OUTPUT="))
                .map(str::to_string)
                .collect(),
        )
    };
    let common = |generator: &str| {
        [
            format!(
                "CROZIER_REFERENCE_CONFIG_FILE={}",
                api.join("crozier.yml").display()
            ),
            format!("CROZIER_REFERENCE_GENERATOR={generator}"),
        ]
    };
    let spec = format!(
        "CROZIER_REFERENCE_SPEC={}",
        api.join("openapi.yml").display()
    );
    let [config_file, generator] = common("golden");
    assert_eq!(
        vars("golden"),
        sorted(vec![
            "CROZIER_REFERENCE_AUDIENCES=".to_string(),
            "CROZIER_REFERENCE_AUDIENCE_STRICT=false".to_string(),
            "CROZIER_REFERENCE_CLIENT_CLASS_NAME=AcmeClient".to_string(),
            config_file,
            "CROZIER_REFERENCE_EXTRA_FIELDS=allow".to_string(),
            generator,
            "CROZIER_REFERENCE_LAYOUT=packaged".to_string(),
            "CROZIER_REFERENCE_PACKAGE_NAME=fern".to_string(),
            "CROZIER_REFERENCE_PROJECT_NAME=default_package_name".to_string(),
            spec.clone(),
        ])
    );
    // crozier's defaults are passed resolved: the package from the title
    // `Widget API`, the project from the package, the client from both.
    let [config_file, generator] = common("defaults");
    assert_eq!(
        vars("defaults"),
        sorted(vec![
            "CROZIER_REFERENCE_AUDIENCES=public,internal".to_string(),
            "CROZIER_REFERENCE_AUDIENCE_STRICT=true".to_string(),
            "CROZIER_REFERENCE_CLIENT_CLASS_NAME=WidgetApiApi".to_string(),
            config_file,
            "CROZIER_REFERENCE_EXTRA_FIELDS=ignore".to_string(),
            generator,
            "CROZIER_REFERENCE_LAYOUT=packaged".to_string(),
            "CROZIER_REFERENCE_PACKAGE_NAME=widget_api".to_string(),
            "CROZIER_REFERENCE_PROJECT_NAME=widget_api".to_string(),
            spec,
        ])
    );
    let output_dir = std::fs::read_to_string(dumps.path().join("defaults"))
        .unwrap()
        .lines()
        .find_map(|l| {
            l.strip_prefix("CROZIER_REFERENCE_OUTPUT=")
                .map(str::to_string)
        })
        .unwrap();
    assert!(!output_dir.starts_with(&root.display().to_string()));
}

// Unix only: crozier runs reference commands under `sh` on Linux and macOS;
// on Windows it runs none (`compare_on_windows_runs_no_reference_command`).
#[cfg(unix)]
#[test]
fn compare_colours_statuses_only_when_the_rule_says_so() {
    let repo = migration_repo();
    let root = repo.path();
    let forced = compare_cmd(root)
        .env("CLICOLOR_FORCE", "1")
        .args(["--json", "-"])
        .output()
        .unwrap();
    let stderr = String::from_utf8(forced.stderr).unwrap();
    for coloured in [
        "\u{1b}[32mmatched\u{1b}[0m",
        "\u{1b}[31mmismatched\u{1b}[0m",
        "\u{1b}[33mcould_not_check\u{1b}[0m",
        "\u{1b}[31mResult: 2 generator(s) mismatched the reference (exit 3)\u{1b}[0m",
    ] {
        assert!(
            stderr.contains(coloured),
            "missing {coloured:?} in:\n{stderr}"
        );
    }
    // Progress lines are coloured too, and the JSON on stdout never is.
    assert!(stderr.contains("compare: crozier.yml packaged: \u{1b}[32mmatched"));
    assert!(!String::from_utf8(forced.stdout).unwrap().contains('\u{1b}'));

    // A could-not-check-only run's result line is yellow; a matched one green.
    let yellow = compare_cmd(root)
        .env("CLICOLOR_FORCE", "1")
        .arg("services")
        .output()
        .unwrap();
    assert!(String::from_utf8(yellow.stderr)
        .unwrap()
        .contains("\u{1b}[33mResult: no mismatch, but 1 could not be checked (exit 4)"));
    let green = compare_cmd(root)
        .env("CLICOLOR_FORCE", "1")
        .args([
            "services",
            "--reference-command",
            "../../scripts/reference.sh expected",
        ])
        .output()
        .unwrap();
    assert_eq!(green.status.code(), Some(0));
    assert!(String::from_utf8(green.stderr)
        .unwrap()
        .contains("\u{1b}[32mResult: every checked generator matched"));

    // NO_COLOR wins over CLICOLOR_FORCE; with neither, a non-terminal stderr
    // (a pipe, here) gets none.
    let no_color = compare_cmd(root)
        .env("CLICOLOR_FORCE", "1")
        .env("NO_COLOR", "1")
        .output()
        .unwrap();
    assert_eq!(no_color.status.code(), Some(3));
    assert!(!no_color.stderr.contains(&0x1b));
    let plain = compare_cmd(root).output().unwrap();
    assert_eq!(plain.status.code(), Some(3));
    assert!(!plain.stderr.contains(&0x1b));
}

/// Validate `instance` against the committed `assets/compare-report.schema.json`,
/// for the keywords that schema uses. Hand-rolled like the suite's other small
/// checkers, so the contract test needs no validator dependency.
fn validate_against_committed_schema(instance: &serde_json::Value) {
    let schema: serde_json::Value =
        serde_json::from_str(include_str!("../../assets/compare-report.schema.json")).unwrap();
    let mut errors = Vec::new();
    validate(&schema, &schema, instance, "$", &mut errors);
    assert!(
        errors.is_empty(),
        "report violates its schema:\n{}",
        errors.join("\n")
    );
}

fn validate(
    root: &serde_json::Value,
    schema: &serde_json::Value,
    value: &serde_json::Value,
    at: &str,
    errors: &mut Vec<String>,
) {
    use serde_json::Value;
    let Some(schema) = schema.as_object() else {
        return;
    };
    let known = [
        "$schema",
        "$id",
        "title",
        "description",
        "type",
        "properties",
        "required",
        "additionalProperties",
        "items",
        "enum",
        "const",
        "$ref",
        "$defs",
        "anyOf",
        "oneOf",
        "format",
        "minimum",
        "maximum",
    ];
    for key in schema.keys() {
        assert!(
            known.contains(&key.as_str()),
            "the validator does not know `{key}`"
        );
    }
    if let Some(Value::String(reference)) = schema.get("$ref") {
        let name = reference.strip_prefix("#/$defs/").expect("a local $ref");
        validate(root, &root["$defs"][name], value, at, errors);
    }
    if let Some(Value::Array(branches)) = schema.get("anyOf").or_else(|| schema.get("oneOf")) {
        let matching = branches
            .iter()
            .filter(|branch| {
                let mut inner = Vec::new();
                validate(root, branch, value, at, &mut inner);
                inner.is_empty()
            })
            .count();
        if matching == 0 {
            errors.push(format!("{at}: matches no branch"));
        }
    }
    if let Some(kind) = schema.get("type") {
        let kinds: Vec<&str> = match kind {
            Value::String(k) => vec![k.as_str()],
            Value::Array(ks) => ks.iter().filter_map(Value::as_str).collect(),
            _ => vec![],
        };
        let fits = |k: &str| match k {
            "null" => value.is_null(),
            "boolean" => value.is_boolean(),
            "string" => value.is_string(),
            "integer" => value.is_i64() || value.is_u64(),
            "number" => value.is_number(),
            "array" => value.is_array(),
            "object" => value.is_object(),
            _ => false,
        };
        if !kinds.iter().any(|k| fits(k)) {
            errors.push(format!("{at}: {value} is not {kinds:?}"));
            return;
        }
    }
    if let Some(Value::Array(allowed)) = schema.get("enum") {
        if !allowed.contains(value) {
            errors.push(format!("{at}: {value} is not one of {allowed:?}"));
        }
    }
    if let Some(constant) = schema.get("const") {
        if constant != value {
            errors.push(format!("{at}: {value} is not {constant}"));
        }
    }
    if let (Some(minimum), Some(number)) = (schema.get("minimum"), value.as_f64()) {
        if number < minimum.as_f64().unwrap() {
            errors.push(format!("{at}: {number} is below {minimum}"));
        }
    }
    if let Value::Object(object) = value {
        let properties = schema.get("properties").and_then(Value::as_object);
        if let Some(Value::Array(required)) = schema.get("required") {
            for key in required.iter().filter_map(Value::as_str) {
                if !object.contains_key(key) {
                    errors.push(format!("{at}: missing required `{key}`"));
                }
            }
        }
        for (key, field) in object {
            match properties.and_then(|p| p.get(key)) {
                Some(property) => validate(root, property, field, &format!("{at}.{key}"), errors),
                None if schema.get("additionalProperties") == Some(&Value::Bool(false)) => {
                    errors.push(format!("{at}: unexpected `{key}`"));
                }
                None => {}
            }
        }
    }
    if let (Value::Array(items), Some(item_schema)) = (value, schema.get("items")) {
        for (index, item) in items.iter().enumerate() {
            validate(root, item_schema, item, &format!("{at}[{index}]"), errors);
        }
    }
}

#[test]
fn the_schema_checker_rejects_a_report_that_breaks_the_contract() {
    // The checker must be able to fail, or a passing validation proves nothing.
    let schema: serde_json::Value =
        serde_json::from_str(include_str!("../../assets/compare-report.schema.json")).unwrap();
    let mut errors = Vec::new();
    let broken = serde_json::json!({
        "schema_version": 2,
        "crozier_version": "x",
        "searched_paths": ["."],
        "exit_code": 1,
        "counts": {"matched": 0, "mismatched": 0, "could_not_check": 0},
        "timing_totals": {"generators_timed": 0, "reference_seconds": 0.0, "crozier_seconds": 0.0, "speedup": null, "saved_seconds": 0.0},
        "results": [{"status": "unknown", "config_file": "c", "generator": null, "spec": null,
                     "reference": null, "comparison": null, "timing": null, "reason": null, "extra": 1}]
    });
    validate(&schema, &schema, &broken, "$", &mut errors);
    let joined = errors.join("\n");
    for want in [
        "$.schema_version",
        "$.exit_code",
        "$.results[0].status",
        "unexpected `extra`",
    ] {
        assert!(joined.contains(want), "missing {want:?} in:\n{joined}");
    }
}

/// A small git repository: the fixture spec, a reference script that copies
/// the packaged golden (editing it when given `edit`), and `crozier.yml` at
/// `config_rel` declaring `generators` (YAML lines at two-space indent).
#[cfg(unix)]
fn small_repo(config_rel: &str, generators: &str) -> tempfile::TempDir {
    let repo = tempfile::tempdir().expect("repo tempdir");
    let root = repo.path();
    git(root, &["init", "-q"]);
    write(
        root,
        "openapi.yml",
        &std::fs::read_to_string(fixture_root().join("openapi.yml")).unwrap(),
    );
    write_script(
        root,
        "scripts/reference.sh",
        &format!(
            "cp -R '{}'/expected/. \"$CROZIER_REFERENCE_OUTPUT\"\n\
             if [ \"${{1:-}}\" = edit ]; then echo 'an edited line' >> \"$CROZIER_REFERENCE_OUTPUT/README.md\"; fi\n",
            fixture_root().display()
        ),
    );
    let up = "../".repeat(config_rel.matches('/').count());
    write(
        root,
        config_rel,
        &format!(
            "spec: ./{up}openapi.yml\n{}reference:\n  command: ./{up}scripts/reference.sh\ngenerators:\n{generators}",
            golden_naming("")
        ),
    );
    repo
}

/// Whether this process can still write into a directory it made read-only (it
/// runs as root), which would make a permission-denied journey unprovable.
#[cfg(unix)]
fn permissions_bind(dir: &Path) -> bool {
    let probe = dir.join(".probe");
    let bound = std::fs::write(&probe, "").is_err();
    let _ = std::fs::remove_file(&probe);
    bound
}

#[cfg(unix)]
fn read_only(dir: &Path) {
    use std::os::unix::fs::PermissionsExt;
    std::fs::create_dir_all(dir).unwrap();
    std::fs::set_permissions(dir, std::fs::Permissions::from_mode(0o555)).unwrap();
}

/// With no paths, `compare` searches the whole repository the working directory
/// is in — so run from one subdirectory it still finds a config in another — and
/// the report names that root. Explicit paths still narrow.
#[cfg(unix)]
#[test]
fn compare_with_no_paths_searches_the_whole_repository() {
    let repo = small_repo("other/crozier.yml", "  python: {}\n");
    let root = repo.path();
    write(root, "sub/notes.txt", "a subdirectory with no config\n");
    let assert = compare_cmd(&root.join("sub"))
        .args(["--json", "-"])
        .assert()
        .code(0)
        .stderr(predicates::str::contains("found config other/crozier.yml"));
    let report: serde_json::Value = serde_json::from_slice(&assert.get_output().stdout).unwrap();
    assert_eq!(
        result(&report, "other/crozier.yml", "python")["status"],
        "matched"
    );
    let searched = report["searched_paths"].as_array().unwrap();
    assert_eq!(searched.len(), 1);
    assert_eq!(
        std::fs::canonicalize(searched[0].as_str().unwrap()).unwrap(),
        std::fs::canonicalize(root).unwrap()
    );

    // An explicit path keeps narrowing to its own tree.
    compare_cmd(&root.join("sub"))
        .arg(".")
        .assert()
        .code(0)
        .stderr(predicates::str::contains("No crozier config was found"));
}

/// A `--json` target that cannot be written is refused with exit 1 before any
/// reference command runs, so a run never spends every reference and then
/// discards the result.
#[cfg(unix)]
#[test]
fn compare_refuses_an_unwritable_json_target_before_any_reference_runs() {
    use predicates::prelude::*;

    let outputs = tempfile::tempdir().unwrap();
    let marker = outputs.path().join("reference-ran");
    let repo = small_repo(
        "crozier.yml",
        &format!(
            "  python:\n    reference:\n      command: touch '{}'\n",
            marker.display()
        ),
    );
    let locked = outputs.path().join("locked");
    read_only(&locked);
    if !permissions_bind(&locked) {
        eprintln!("skipped: this process writes through read-only directories");
        return;
    }
    compare_cmd(repo.path())
        .arg("--json")
        .arg(locked.join("report.json"))
        .assert()
        .code(1)
        .stderr(predicates::str::contains("cannot write --json"))
        .stderr(predicates::str::contains("reference command starting").not());
    assert!(!marker.exists(), "a reference ran before the refusal");
}

/// A `--diff-dir` file that cannot be written does not stop the run: every
/// generator is still checked, both reports are still written, the human one
/// states the failure, and the command exits 1.
#[cfg(unix)]
#[test]
fn compare_still_checks_and_reports_when_a_diff_file_cannot_be_written() {
    let repo = small_repo(
        "crozier.yml",
        "  edited:\n    reference:\n      command: ./scripts/reference.sh edit\n  \
         also-edited:\n    reference:\n      command: ./scripts/reference.sh edit\n  matched: {}\n",
    );
    let outputs = tempfile::tempdir().unwrap();
    let diffs = outputs.path().join("diffs");
    read_only(&diffs);
    if !permissions_bind(&diffs) {
        eprintln!("skipped: this process writes through read-only directories");
        return;
    }
    let json = outputs.path().join("report.json");
    let assert = compare_cmd(repo.path())
        .arg("--diff-dir")
        .arg(&diffs)
        .arg("--json")
        .arg(&json)
        .assert()
        .code(1);
    let stderr = String::from_utf8_lossy(&assert.get_output().stderr).into_owned();
    assert!(stderr.contains("crozier compare report"), "{stderr}");
    assert!(
        stderr.contains("2 --diff-dir file(s) could not be written, so the command exits 1:"),
        "{stderr}"
    );
    assert_eq!(
        stderr.matches("could not write --diff-dir file").count(),
        4,
        "{stderr}"
    );
    let report: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(&json).unwrap()).unwrap();
    validate_against_committed_schema(&report);
    for generator in ["edited", "also-edited"] {
        let edited = result(&report, "crozier.yml", generator);
        assert_eq!(edited["status"], "mismatched");
        assert_eq!(edited["comparison"]["diff_file"], serde_json::Value::Null);
    }
    assert_eq!(
        result(&report, "crozier.yml", "matched")["status"],
        "matched"
    );
}

/// When the reference produced output and crozier's own generation fails — here
/// because `ruff`, which crozier formats with, is not on `PATH` — the generator
/// is mismatched, with crozier's error as the reason.
#[cfg(unix)]
#[test]
fn compare_reports_a_crozier_failure_after_a_good_reference_as_mismatched() {
    use predicates::prelude::*;

    let repo = small_repo(
        "crozier.yml",
        "  python:\n    reference:\n      command: echo reference > \"$CROZIER_REFERENCE_OUTPUT/README.md\"\n",
    );
    // A PATH holding only `sh`: the reference command needs nothing else.
    let bin = tempfile::tempdir().unwrap();
    std::os::unix::fs::symlink("/bin/sh", bin.path().join("sh")).unwrap();
    let json = bin.path().join("report.json");
    compare_cmd(repo.path())
        .env("PATH", bin.path())
        .arg("--json")
        .arg(&json)
        .assert()
        .code(3)
        .stderr(predicates::str::contains(
            "compare: crozier.yml python: crozier generation failed",
        ))
        .stderr(predicates::str::contains("\u{1b}").not());
    let report: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(&json).unwrap()).unwrap();
    validate_against_committed_schema(&report);
    let python = result(&report, "crozier.yml", "python");
    assert_eq!(python["status"], "mismatched");
    assert_eq!(python["comparison"], serde_json::Value::Null);
    let reason = python["reason"].as_str().unwrap();
    assert!(
        reason.starts_with("crozier could not generate: "),
        "{reason}"
    );
    assert!(reason.contains("ruff"), "{reason}");
    assert_eq!(report["exit_code"], 3);
}

/// Every usage error of `compare` exits 2 with clap's usage text — clap's own,
/// and combining `compare` with the global `--config` or `--no-config`.
#[test]
fn compare_usage_errors_exit_2() {
    let empty = tempfile::tempdir().unwrap();
    for args in [
        ["--config", "crozier.yml", "compare"].as_slice(),
        ["--no-config", "compare"].as_slice(),
    ] {
        crozier()
            .current_dir(empty.path())
            .args(args)
            .assert()
            .code(2)
            .stderr(predicates::str::contains("pass a config file as a PATH"))
            .stderr(predicates::str::contains("Usage: crozier compare"));
    }
    compare_cmd(empty.path())
        .arg("--no-such-flag")
        .assert()
        .code(2)
        .stderr(predicates::str::contains("Usage: crozier compare"));
}
