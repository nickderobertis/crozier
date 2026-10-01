//! The Fern reference recipe in `docs/fern-reference.md` is documentation, not a
//! shipped script, so these tests read it straight off the page: its version
//! defaults must be the pair crozier certifies, it must parse, and — run with a
//! stand-in `fern` first on `PATH` that records what it is handed — it must build
//! the workspace and make the invocation the page promises. (The real-Fern run of
//! the same script is evidence gathered outside the suite: Fern needs Docker Hub
//! and npm.)
#![cfg(unix)]

use std::collections::BTreeMap;
use std::os::unix::fs::PermissionsExt;
use std::path::{Path, PathBuf};
use std::process::Command;

fn root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
}

/// The page's one `bash` block: the recipe.
fn recipe() -> String {
    let page = std::fs::read_to_string(root().join("docs/fern-reference.md")).unwrap();
    let blocks: Vec<&str> = page
        .split("\n```bash\n")
        .skip(1)
        .map(|rest| rest.split("\n```\n").next().unwrap())
        .collect();
    assert_eq!(
        blocks.len(),
        1,
        "docs/fern-reference.md must hold exactly one bash block"
    );
    format!("{}\n", blocks[0])
}

fn write_recipe(dir: &Path) -> PathBuf {
    let path = dir.join("fern-reference.sh");
    std::fs::write(&path, recipe()).unwrap();
    std::fs::set_permissions(&path, std::fs::Permissions::from_mode(0o755)).unwrap();
    path
}

/// The default a `NAME="${OVERRIDE:-default}"` line gives `NAME`.
fn default_of(script: &str, name: &str) -> String {
    let line = script
        .lines()
        .find(|l| l.starts_with(&format!("{name}=")))
        .unwrap_or_else(|| panic!("the recipe sets no {name}"));
    let start = line.find(":-").expect("a `${VAR:-default}` form") + 2;
    let end = line[start..].find('}').unwrap() + start;
    line[start..end].to_string()
}

#[test]
fn the_recipe_defaults_to_the_certified_pair_and_parses() {
    let script = recipe();
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(root().join("assets/scaffolding/metadata.json")).unwrap(),
    )
    .unwrap();
    assert_eq!(
        default_of(&script, "FERN_CLI_VERSION"),
        metadata["cliVersion"]
    );
    assert_eq!(
        default_of(&script, "FERN_PYTHON_SDK_VERSION"),
        metadata["generatorVersion"]
    );
    assert_eq!(metadata["generatorName"], "fernapi/fern-python-sdk");
    assert!(script.contains("fernapi/fern-python-sdk"));

    let dir = tempfile::tempdir().unwrap();
    let path = write_recipe(dir.path());
    let parsed = Command::new("bash").arg("-n").arg(&path).output().unwrap();
    assert!(
        parsed.status.success(),
        "{}",
        String::from_utf8_lossy(&parsed.stderr)
    );
    // The check can fail: a script that does not parse is refused.
    std::fs::write(&path, "if then\n").unwrap();
    assert!(!Command::new("bash")
        .arg("-n")
        .arg(&path)
        .status()
        .unwrap()
        .success());
}

/// What the stand-in `fern` recorded: its arguments, the environment variables
/// the page speaks of, and the workspace it ran in.
struct Recorded {
    args: Vec<String>,
    env: BTreeMap<String, String>,
    config: serde_json::Value,
    generators: serde_yaml_ng::Value,
}

/// One run of the recipe with a stand-in `fern`.
struct Run {
    status: std::process::ExitStatus,
    stderr: String,
    recorded: Option<Recorded>,
    output: PathBuf,
    _dirs: [tempfile::TempDir; 2],
}

const BASE: &[(&str, &str)] = &[
    ("CROZIER_REFERENCE_GENERATOR", "python"),
    ("CROZIER_REFERENCE_CONFIG_FILE", "/repo/crozier.yml"),
    ("CROZIER_REFERENCE_PACKAGE_NAME", "fern"),
    ("CROZIER_REFERENCE_PROJECT_NAME", "default_package_name"),
    ("CROZIER_REFERENCE_CLIENT_CLASS_NAME", "AcmeClient"),
    ("CROZIER_REFERENCE_AUDIENCES", "public,internal"),
    ("CROZIER_REFERENCE_AUDIENCE_STRICT", "true"),
    ("CROZIER_REFERENCE_EXTRA_FIELDS", "ignore"),
    ("CROZIER_REFERENCE_LAYOUT", "packaged"),
];

fn run(overrides: &[(&str, &str)], removed: &[&str]) -> Run {
    let work = tempfile::tempdir().unwrap();
    let output = tempfile::tempdir().unwrap();
    let bin = work.path().join("bin");
    let record = work.path().join("record");
    std::fs::create_dir_all(&bin).unwrap();
    let fern = bin.join("fern");
    std::fs::write(
        &fern,
        "#!/bin/sh\nset -eu\nmkdir -p \"$RECORD\"\n\
         for a in \"$@\"; do printf '%s\\n' \"$a\"; done > \"$RECORD/args\"\n\
         env | grep -E '^(CI|GITHUB_ACTIONS|FERN_TOKEN)=' > \"$RECORD/env\" || true\n\
         cp fern.config.json generators.yml \"$RECORD/\"\n",
    )
    .unwrap();
    std::fs::set_permissions(&fern, std::fs::Permissions::from_mode(0o755)).unwrap();
    let spec = work.path().join("api.json");
    std::fs::write(&spec, "{\"openapi\": \"3.0.3\"}").unwrap();
    let script = write_recipe(work.path());

    let mut cmd = Command::new(&script);
    cmd.env(
        "PATH",
        format!("{}:{}", bin.display(), std::env::var("PATH").unwrap()),
    )
    .env("RECORD", &record)
    .env("CROZIER_REFERENCE_OUTPUT", output.path())
    .env("CROZIER_REFERENCE_SPEC", &spec)
    .env_remove("CI")
    .env_remove("GITHUB_ACTIONS")
    .env_remove("FERN_TOKEN")
    .env_remove("FERN_REFERENCE_CLI_VERSION")
    .env_remove("FERN_REFERENCE_PYTHON_SDK_VERSION");
    for (k, v) in BASE.iter().chain(overrides) {
        cmd.env(k, v);
    }
    for k in removed {
        cmd.env_remove(k);
    }
    let out = cmd.output().unwrap();
    let recorded = record.join("args").exists().then(|| Recorded {
        args: std::fs::read_to_string(record.join("args"))
            .unwrap()
            .lines()
            .map(str::to_string)
            .collect(),
        env: std::fs::read_to_string(record.join("env"))
            .unwrap()
            .lines()
            .filter_map(|l| l.split_once('='))
            .map(|(k, v)| (k.to_string(), v.to_string()))
            .collect(),
        config: serde_json::from_str(
            &std::fs::read_to_string(record.join("fern.config.json")).unwrap(),
        )
        .unwrap(),
        generators: serde_yaml_ng::from_str(
            &std::fs::read_to_string(record.join("generators.yml")).unwrap(),
        )
        .unwrap(),
    });
    Run {
        status: out.status,
        stderr: String::from_utf8_lossy(&out.stderr).into_owned(),
        recorded,
        output: output.path().to_path_buf(),
        _dirs: [work, output],
    }
}

fn generator(recorded: &Recorded) -> &serde_yaml_ng::Value {
    &recorded.generators["groups"]["crozier-reference"]["generators"][0]
}

fn strings(values: &[&str]) -> Vec<String> {
    values.iter().map(|s| (*s).to_string()).collect()
}

#[test]
fn packaged_builds_the_workspace_and_generates_in_preview_mode() {
    let run = run(&[], &[]);
    assert!(run.status.success(), "{}", run.stderr);
    let recorded = run.recorded.expect("fern ran");
    // The certified pair, and the organization that reproduces package `fern`.
    assert_eq!(
        recorded.config,
        serde_json::json!({"organization": "fern", "version": "5.67.1"})
    );
    let generator = generator(&recorded);
    assert_eq!(generator["name"], "fernapi/fern-python-sdk");
    assert_eq!(generator["version"], "5.20.0");
    let config = &generator["config"];
    assert_eq!(config["client_class_name"], "AcmeClient");
    assert_eq!(config["pydantic_config"]["enum_type"], "python_enums");
    assert_eq!(config["pydantic_config"]["extra_fields"], "ignore");
    let group = &recorded.generators["groups"]["crozier-reference"];
    let audiences: Vec<&str> = group["audiences"]
        .as_sequence()
        .unwrap()
        .iter()
        .map(|a| a.as_str().unwrap())
        .collect();
    assert_eq!(audiences, ["public", "internal"]);
    // The spec is in the workspace under its own name.
    assert_eq!(recorded.generators["api"]["path"], "openapi/api.json");
    // A scratch local-file-system output, so Fern emits the plain package.
    assert_eq!(generator["output"]["location"], "local-file-system");
    assert_ne!(
        generator["output"]["path"].as_str(),
        Some(run.output.to_str().unwrap())
    );
    // Locally, in preview mode, into $CROZIER_REFERENCE_OUTPUT.
    assert_eq!(
        recorded.args,
        strings(&[
            "generate",
            "--group",
            "crozier-reference",
            "--local",
            "--preview",
            "--output",
            run.output.to_str().unwrap(),
            "--force",
        ])
    );
    // Unset, the three variables are set for the run.
    assert_eq!(recorded.env["CI"], "true");
    assert_eq!(recorded.env["GITHUB_ACTIONS"], "true");
    assert_eq!(recorded.env["FERN_TOKEN"], "preview-only-no-publish");
}

#[test]
fn flat_writes_a_local_file_system_output_and_generates_without_preview() {
    let run = run(
        &[
            ("CROZIER_REFERENCE_LAYOUT", "flat"),
            ("CROZIER_REFERENCE_PACKAGE_NAME", "my_api2"),
            // A flat tree has no distribution: any project name is accepted.
            ("CROZIER_REFERENCE_PROJECT_NAME", "my-api-dist"),
            ("CROZIER_REFERENCE_AUDIENCES", ""),
            ("CROZIER_REFERENCE_EXTRA_FIELDS", "allow"),
            ("CROZIER_REFERENCE_CLIENT_CLASS_NAME", "MyApi2Api"),
        ],
        &[],
    );
    assert!(run.status.success(), "{}", run.stderr);
    let recorded = run.recorded.expect("fern ran");
    assert_eq!(recorded.config["organization"], "my_api2");
    assert_eq!(recorded.config["version"], "5.67.1");
    let generator = generator(&recorded);
    assert_eq!(generator["version"], "5.20.0");
    assert_eq!(generator["config"]["client_class_name"], "MyApi2Api");
    assert_eq!(
        generator["config"]["pydantic_config"]["enum_type"],
        "python_enums"
    );
    assert_eq!(
        generator["config"]["pydantic_config"]["extra_fields"],
        "allow"
    );
    assert_eq!(generator["output"]["location"], "local-file-system");
    assert_eq!(generator["output"]["path"], run.output.to_str().unwrap());
    // No audiences, no `audiences:` key.
    assert!(recorded.generators["groups"]["crozier-reference"]
        .get("audiences")
        .is_none());
    assert_eq!(
        recorded.args,
        strings(&[
            "generate",
            "--group",
            "crozier-reference",
            "--local",
            "--force"
        ])
    );
    assert_eq!(recorded.env["CI"], "true");
    assert_eq!(recorded.env["GITHUB_ACTIONS"], "true");
    assert!(!recorded.env.contains_key("FERN_TOKEN"));
}

#[test]
fn preset_variables_and_version_overrides_are_respected() {
    let run = run(
        &[
            ("CI", "1"),
            ("GITHUB_ACTIONS", "false"),
            ("FERN_TOKEN", "a-real-token"),
            ("FERN_REFERENCE_CLI_VERSION", "9.9.9"),
            ("FERN_REFERENCE_PYTHON_SDK_VERSION", "8.8.8"),
        ],
        &[],
    );
    assert!(run.status.success(), "{}", run.stderr);
    let recorded = run.recorded.expect("fern ran");
    assert_eq!(recorded.env["CI"], "1");
    assert_eq!(recorded.env["GITHUB_ACTIONS"], "false");
    assert_eq!(recorded.env["FERN_TOKEN"], "a-real-token");
    assert_eq!(recorded.config["version"], "9.9.9");
    assert_eq!(generator(&recorded)["version"], "8.8.8");
}

#[test]
fn values_the_recipe_cannot_reproduce_exit_without_running_fern() {
    for (overrides, named) in [
        (
            vec![("CROZIER_REFERENCE_LAYOUT", "nested")],
            "unknown layout 'nested'",
        ),
        (
            vec![("CROZIER_REFERENCE_PACKAGE_NAME", "acme")],
            "package name 'acme' cannot be reproduced under the packaged layout",
        ),
        (
            vec![("CROZIER_REFERENCE_PROJECT_NAME", "acme-dist")],
            "project name 'acme-dist' cannot be reproduced under the packaged layout",
        ),
        (
            vec![
                ("CROZIER_REFERENCE_LAYOUT", "flat"),
                ("CROZIER_REFERENCE_PACKAGE_NAME", "my-api"),
            ],
            "package name 'my-api' cannot be reproduced",
        ),
        (
            vec![
                ("CROZIER_REFERENCE_LAYOUT", "flat"),
                ("CROZIER_REFERENCE_PACKAGE_NAME", "Acme"),
            ],
            "package name 'Acme' cannot be reproduced",
        ),
    ] {
        let run = run(&overrides, &[]);
        assert!(!run.status.success(), "{overrides:?} succeeded");
        assert!(run.stderr.contains(named), "{overrides:?}: {}", run.stderr);
        assert!(run.recorded.is_none(), "{overrides:?} ran fern");
    }

    // Run outside `crozier compare`, it says what is missing.
    let run = run(&[], &["CROZIER_REFERENCE_LAYOUT"]);
    assert!(!run.status.success());
    assert!(
        run.stderr.contains("CROZIER_REFERENCE_LAYOUT is not set"),
        "{}",
        run.stderr
    );
    assert!(run.recorded.is_none());
}
