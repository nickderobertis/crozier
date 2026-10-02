//! The Fern reference recipe in `docs/fern-reference.md` is documentation, not a
//! shipped script, so these tests read it straight off the page: its version
//! defaults must be the pair crozier certifies, its one other copy — inline in
//! the consumer example workflow, which `docs/github-action.md` embeds — must be
//! identical to it, it must parse, and — run with a
//! stand-in `fern` first on `PATH` that records what it is handed — it must build
//! the workspace and make the invocation the page promises. (The real-Fern run of
//! the same script is evidence gathered outside the suite: Fern needs Docker Hub
//! and npm.)
#![cfg(unix)]

use std::collections::{BTreeMap, BTreeSet};
use std::os::unix::fs::PermissionsExt;
use std::path::{Path, PathBuf};
use std::process::Command;

use crozier::compare::REFERENCE_VARIABLES;

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

/// The consumer example workflow the GitHub Action's docs publish.
const EXAMPLE: &str = "docs/examples/migrate-from-fern.yml";

/// The recipe a workflow writes inline: the body of its one step's
/// `cat > <file> <<'RECIPE'` here-document, as the runner's shell receives it
/// (the YAML block scalar parsed).
fn inline_recipe(workflow: &str, source: &str) -> String {
    let workflow: serde_yaml_ng::Value =
        serde_yaml_ng::from_str(workflow).unwrap_or_else(|e| panic!("{source} is not YAML: {e}"));
    let bodies: Vec<String> = workflow["jobs"]
        .as_mapping()
        .unwrap_or_else(|| panic!("{source} has no jobs"))
        .values()
        .flat_map(|job| job["steps"].as_sequence().unwrap())
        .filter_map(|step| step["run"].as_str())
        .filter_map(|run| run.split_once("<<'RECIPE'\n").map(|(_, rest)| rest))
        .map(|rest| {
            let (body, _) = rest
                .split_once("\nRECIPE\n")
                .unwrap_or_else(|| panic!("{source}: the RECIPE here-document is not closed"));
            format!("{body}\n")
        })
        .collect();
    assert_eq!(
        bodies.len(),
        1,
        "{source} must write the recipe in exactly one step"
    );
    bodies.into_iter().next().unwrap()
}

/// The first line at which `copy` departs from the docs page's script.
fn first_difference(copy: &str, script: &str) -> Option<String> {
    if copy == script {
        return None;
    }
    let line = copy
        .lines()
        .zip(script.lines())
        .position(|(a, b)| a != b)
        .map_or_else(|| "its length".to_string(), |i| format!("line {}", i + 1));
    Some(line)
}

/// The recipe's one source is the docs page; its copies are the example
/// workflow's inline one and, through it, `docs/github-action.md`'s embedded
/// one. Each is extracted on its own and must equal the page's script.
#[test]
fn the_inline_copies_of_the_recipe_equal_the_docs_page() {
    let script = recipe();
    let example = std::fs::read_to_string(root().join(EXAMPLE)).unwrap();
    let action_page = std::fs::read_to_string(root().join("docs/github-action.md")).unwrap();
    let embedded: Vec<&str> = action_page
        .split("\n```yaml\n")
        .skip(1)
        .map(|rest| rest.split("```\n").next().unwrap())
        .filter(|block| block.contains("<<'RECIPE'"))
        .collect();
    assert_eq!(
        embedded.len(),
        1,
        "docs/github-action.md must embed the recipe-writing workflow once"
    );
    for (source, copy) in [
        (EXAMPLE, inline_recipe(&example, EXAMPLE)),
        (
            "docs/github-action.md",
            inline_recipe(embedded[0], "docs/github-action.md"),
        ),
    ] {
        if let Some(line) = first_difference(&copy, &script) {
            panic!(
                "{source}'s copy of the recipe differs from docs/fern-reference.md's script at \
                 {line}; the docs page is the one source, so copy it unchanged"
            );
        }
    }
    // The comparison can fail: an altered copy is told apart.
    assert!(first_difference(&script.replace("5.67.1", "5.67.2"), &script).is_some());
}

/// The example workflow states, installs and pre-pulls the pair crozier
/// certifies, and no other pair; `docs/github-action.md` states it too.
#[test]
fn the_example_and_the_action_docs_state_the_certified_pair() {
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(root().join("assets/scaffolding/metadata.json")).unwrap(),
    )
    .unwrap();
    let cli = metadata["cliVersion"].as_str().unwrap();
    let generator = metadata["generatorVersion"].as_str().unwrap();

    let example = std::fs::read_to_string(root().join(EXAMPLE)).unwrap();
    assert!(example.contains(&format!(
        "# Fern versions crozier certifies: Fern CLI {cli} with\n# fernapi/fern-python-sdk {generator}."
    )));
    assert!(example.contains(&format!("npm install -g fern-api@{cli}\n")));
    assert!(example.contains(&format!(
        "docker pull fernapi/fern-python-sdk:{generator}\n"
    )));
    let versions = example
        .split(|c: char| !(c.is_ascii_digit() || c == '.'))
        .map(|token| token.trim_matches('.'))
        .filter(|token| token.split('.').count() == 3 && token.split('.').all(|p| !p.is_empty()));
    for version in versions {
        assert!(
            // `0.0.1`: the inline recipe's comment on Fern's publishable
            // repository, as on the docs page.
            [cli, generator, "0.0.1"].contains(&version),
            "{EXAMPLE} states version {version}, not the certified pair {cli} / {generator}"
        );
    }

    let action_page = std::fs::read_to_string(root().join("docs/github-action.md")).unwrap();
    let prose = action_page.split_whitespace().collect::<Vec<_>>().join(" ");
    assert!(
        prose.contains(&format!(
            "**Fern CLI {cli}** with **`fernapi/fern-python-sdk` {generator}**"
        )),
        "docs/github-action.md does not state the certified pair {cli} / {generator}"
    );
}

/// Every version the page states outside the script — the certified-pair prose,
/// the measurement note, the `docker pull` tag — is the pair
/// `assets/scaffolding/metadata.json` records. (`0.0.1` is the version Fern stamps
/// on a publishable repository, which the page describes, not a pair.)
#[test]
fn every_version_the_page_states_is_the_certified_pair() {
    let page = std::fs::read_to_string(root().join("docs/fern-reference.md")).unwrap();
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(root().join("assets/scaffolding/metadata.json")).unwrap(),
    )
    .unwrap();
    let cli = metadata["cliVersion"].as_str().unwrap();
    let generator = metadata["generatorVersion"].as_str().unwrap();
    assert!(page.contains(&format!("**Fern CLI {cli}**")));
    assert!(page.contains(&format!("Measured with Fern CLI {cli} and")));
    assert!(page.contains(&format!(
        "docker pull fernapi/fern-python-sdk:{generator}\n"
    )));
    let versions = page
        .split(|c: char| !(c.is_ascii_digit() || c == '.'))
        .map(|token| token.trim_matches('.'))
        .filter(|token| token.split('.').count() == 3 && token.split('.').all(|p| !p.is_empty()));
    for version in versions {
        assert!(
            [cli, generator, "0.0.1"].contains(&version),
            "docs/fern-reference.md states version {version}, not the certified pair \
             {cli} / {generator}"
        );
    }
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
    ("CROZIER_REFERENCE_ENUM_TYPE", "python-enums"),
    ("CROZIER_REFERENCE_DEFAULT_MAX_RETRIES", "2"),
    ("CROZIER_REFERENCE_LAYOUT", "packaged"),
];

/// The `CROZIER_REFERENCE_*` names the recipe reads must be the ones crozier
/// exports: `BASE` plus the two `run` sets (`OUTPUT`, `SPEC`) is exactly
/// [`REFERENCE_VARIABLES`], so a renamed variable fails here and then fails every
/// recipe run below until the script reads the new name; and every name the page's
/// mapping table or the script itself spells out is one crozier exports.
#[test]
fn the_recipe_reads_only_variables_crozier_exports() {
    let exported: BTreeSet<&str> = REFERENCE_VARIABLES.into_iter().collect();
    let mut given: BTreeSet<&str> = BASE.iter().map(|(name, _)| *name).collect();
    given.extend(["CROZIER_REFERENCE_OUTPUT", "CROZIER_REFERENCE_SPEC"]);
    assert_eq!(given, exported);

    let page = std::fs::read_to_string(root().join("docs/fern-reference.md")).unwrap();
    let table: Vec<String> = page
        .lines()
        .filter_map(|line| line.strip_prefix("| `"))
        .map(|rest| rest[..rest.find('`').unwrap()].to_string())
        .filter(|name| name.chars().all(|c| c.is_ascii_uppercase() || c == '_'))
        .map(|name| format!("CROZIER_REFERENCE_{name}"))
        .collect();
    assert_eq!(table.len(), 11, "the mapping table's rows: {table:?}");
    let script = recipe();
    let spelled = script
        .split("CROZIER_REFERENCE_")
        .skip(1)
        .filter_map(|rest| {
            let end = rest
                .find(|c: char| !(c.is_ascii_uppercase() || c == '_'))
                .unwrap_or(rest.len());
            (end > 0).then(|| format!("CROZIER_REFERENCE_{}", &rest[..end]))
        });
    for name in table.into_iter().chain(spelled) {
        assert!(
            exported.contains(name.as_str()),
            "{name} is not a variable crozier exports"
        );
    }
}

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
    // crozier's default of 2 is Fern's: no key, so Fern applies its own.
    assert!(config.get("default_max_retries").is_none(), "{config:?}");
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

/// A non-default `default-max-retries` is Fern's `default_max_retries`, written
/// as an integer beside the generator's other settings, in either layout.
#[test]
fn a_non_default_max_retries_is_written_to_the_fern_config() {
    for layout in ["packaged", "flat"] {
        let run = run(
            &[
                ("CROZIER_REFERENCE_DEFAULT_MAX_RETRIES", "0"),
                ("CROZIER_REFERENCE_LAYOUT", layout),
            ],
            &[],
        );
        assert!(run.status.success(), "{layout}: {}", run.stderr);
        let recorded = run.recorded.expect("fern ran");
        let config = &generator(&recorded)["config"];
        assert_eq!(
            config["default_max_retries"],
            serde_yaml_ng::Value::from(0),
            "{layout}: {config:?}"
        );
        assert_eq!(config["client_class_name"], "AcmeClient", "{layout}");
        assert_eq!(
            config["pydantic_config"]["enum_type"], "python_enums",
            "{layout}"
        );
    }
}

/// crozier's `enum-type: literals` is Fern with `enum_type` unset: the reference
/// generator's `pydantic_config` keeps every other setting and carries no
/// `enum_type` key, so Fern applies its `literals` default — in either layout.
#[test]
fn literals_leaves_fern_enum_type_unset() {
    for layout in ["packaged", "flat"] {
        let run = run(
            &[
                ("CROZIER_REFERENCE_ENUM_TYPE", "literals"),
                ("CROZIER_REFERENCE_LAYOUT", layout),
            ],
            &[],
        );
        assert!(run.status.success(), "{layout}: {}", run.stderr);
        let recorded = run.recorded.expect("fern ran");
        let pydantic = &generator(&recorded)["config"]["pydantic_config"];
        assert!(
            pydantic.get("enum_type").is_none(),
            "{layout}: {pydantic:?}"
        );
        assert_eq!(pydantic["extra_fields"], "ignore", "{layout}");
    }
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
fn preset_empty_variables_are_respected() {
    let run = run(
        &[("CI", ""), ("GITHUB_ACTIONS", ""), ("FERN_TOKEN", "")],
        &[],
    );
    assert!(run.status.success(), "{}", run.stderr);
    let recorded = run.recorded.expect("fern ran");
    for name in ["CI", "GITHUB_ACTIONS", "FERN_TOKEN"] {
        assert_eq!(recorded.env[name], "", "the recipe replaced set {name}");
    }
}

#[test]
fn values_the_recipe_cannot_reproduce_exit_without_running_fern() {
    for (overrides, named) in [
        (
            vec![("CROZIER_REFERENCE_LAYOUT", "nested")],
            "unknown layout 'nested'",
        ),
        (
            vec![("CROZIER_REFERENCE_ENUM_TYPE", "python_enums")],
            "unknown enum type 'python_enums'",
        ),
        (
            vec![("CROZIER_REFERENCE_DEFAULT_MAX_RETRIES", "-1")],
            "default max retries '-1' is not a non-negative integer",
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

/// Values reach the workspace as written, whatever YAML or JSON would make of
/// them unquoted; one the workspace cannot carry is refused before `fern` runs.
#[test]
fn values_with_yaml_meaning_reach_the_workspace_as_written() {
    let client = r#"Acme: {x} # "quoted" \ back"#;
    let quoted = run(
        &[
            ("CROZIER_REFERENCE_CLIENT_CLASS_NAME", client),
            ("CROZIER_REFERENCE_AUDIENCES", "a: b,#c,[d]"),
            ("FERN_REFERENCE_CLI_VERSION", r#"1", "x": "y"#),
        ],
        &[],
    );
    assert!(quoted.status.success(), "{}", quoted.stderr);
    let recorded = quoted.recorded.expect("fern ran");
    assert_eq!(generator(&recorded)["config"]["client_class_name"], client);
    let audiences: Vec<&str> = recorded.generators["groups"]["crozier-reference"]["audiences"]
        .as_sequence()
        .unwrap()
        .iter()
        .map(|a| a.as_str().unwrap())
        .collect();
    assert_eq!(audiences, ["a: b", "#c", "[d]"]);
    assert_eq!(
        recorded.config,
        serde_json::json!({"organization": "fern", "version": r#"1", "x": "y"#})
    );

    let refused = run(&[("CROZIER_REFERENCE_CLIENT_CLASS_NAME", "Acme\nApi")], &[]);
    assert!(!refused.status.success());
    assert!(
        refused
            .stderr
            .contains("value 'Acme\nApi' holds a control character"),
        "{}",
        refused.stderr
    );
    assert!(refused.recorded.is_none(), "fern ran");
}
