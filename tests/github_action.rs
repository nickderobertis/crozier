//! The GitHub Action's committed surfaces, held to each other: `action.yml`'s
//! metadata and security shape, `docs/github-action.md`'s inputs and outputs
//! tables, the consumer example workflow the page embeds, and that example's
//! own shape as a workflow. (The Action's behaviour is driven for real in
//! `crates/crozier-e2e/tests/e2e/action.rs`; the recipe the example inlines is held to its docs
//! page in `tests/fern_reference_recipe.rs`.)

use std::collections::BTreeMap;
use std::path::Path;

use serde_yaml_ng::{Mapping, Value};

fn root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
}

fn read(rel: &str) -> String {
    std::fs::read_to_string(root().join(rel)).unwrap_or_else(|e| panic!("read {rel}: {e}"))
}

fn yaml(rel: &str) -> Value {
    serde_yaml_ng::from_str(&read(rel)).unwrap_or_else(|e| panic!("{rel} is not YAML: {e}"))
}

fn mapping<'a>(value: &'a Value, key: &str) -> &'a Mapping {
    value
        .get(key)
        .and_then(Value::as_mapping)
        .unwrap_or_else(|| panic!("no mapping `{key}`"))
}

fn string<'a>(value: &'a Value, key: &str) -> Option<&'a str> {
    value.get(key).and_then(Value::as_str)
}

fn keys(mapping: &Mapping) -> Vec<String> {
    mapping
        .keys()
        .map(|k| k.as_str().unwrap().to_string())
        .collect()
}

const INPUTS: [&str; 4] = [
    "paths",
    "reference-command",
    "diff-artifact-name",
    "version",
];
const OUTPUTS: [&str; 9] = [
    "matched",
    "mismatched",
    "could-not-check",
    "exit-code",
    "report-path",
    "total-reference-seconds",
    "total-crozier-seconds",
    "total-speedup",
    "total-saved-seconds",
];

#[test]
fn action_yml_carries_marketplace_metadata_and_the_contracted_inputs_and_outputs() {
    let action = yaml("action.yml");
    for key in ["name", "description", "author"] {
        assert!(
            string(&action, key).is_some_and(|v| !v.is_empty()),
            "action.yml has no {key}"
        );
    }
    let branding = mapping(&action, "branding");
    assert!(branding.contains_key("icon") && branding.contains_key("color"));
    assert_eq!(string(&action["runs"], "using"), Some("composite"));

    assert_eq!(keys(mapping(&action, "inputs")), INPUTS);
    let inputs = &action["inputs"];
    assert_eq!(string(&inputs["paths"], "default"), Some(""));
    assert_eq!(string(&inputs["reference-command"], "default"), Some(""));
    assert_eq!(string(&inputs["version"], "default"), Some(""));
    assert_eq!(
        string(&inputs["diff-artifact-name"], "default"),
        Some("crozier-compare-diffs")
    );

    assert_eq!(keys(mapping(&action, "outputs")), OUTPUTS);
    for name in OUTPUTS {
        // Every output is the compare step's output of the same name.
        assert_eq!(
            string(&action["outputs"][name], "value"),
            Some(format!("${{{{ steps.compare.outputs.{name} }}}}").as_str())
        );
    }

    // The upload is named by the input and runs only on a mismatch.
    let steps = action["runs"]["steps"].as_sequence().unwrap();
    let upload = steps
        .iter()
        .find(|s| string(s, "uses").is_some_and(|u| u.starts_with("actions/upload-artifact@")))
        .expect("action.yml uploads the diffs");
    assert_eq!(
        string(&upload["with"], "name"),
        Some("${{ inputs.diff-artifact-name }}")
    );
    assert!(string(upload, "if")
        .unwrap()
        .contains("steps.compare.outputs.mismatched != '0'"));
}

/// Values reach the scripts only through `env`: no `run:` holds an
/// expression, and each runs a script under `scripts/action/` that exists.
#[test]
fn action_run_steps_take_every_value_through_env() {
    let action = yaml("action.yml");
    let steps = action["runs"]["steps"].as_sequence().unwrap();
    let runs: Vec<&Value> = steps.iter().filter(|s| s.get("run").is_some()).collect();
    assert_eq!(runs.len(), 3, "install, compare and finish");
    for step in runs {
        let run = string(step, "run").unwrap();
        assert!(!run.contains("${{"), "a run: script interpolates: {run}");
        assert_eq!(string(step, "shell"), Some("bash"));
        let script = run
            .strip_prefix("bash \"$GITHUB_ACTION_PATH/")
            .and_then(|rest| rest.strip_suffix('"'))
            .unwrap_or_else(|| panic!("{run} is not one action script"));
        assert!(script.starts_with("scripts/action/"), "{script}");
        assert!(root().join(script).is_file(), "{script} does not exist");
    }
}

/// The Action's surface is neutral: it runs whatever reference command it is
/// given, and nothing in it is specific to one reference tool.
#[test]
fn neither_action_yml_nor_its_scripts_name_a_reference_tool() {
    let mut files = vec!["action.yml".to_string()];
    for entry in std::fs::read_dir(root().join("scripts/action")).unwrap() {
        let name = entry.unwrap().file_name().into_string().unwrap();
        files.push(format!("scripts/action/{name}"));
    }
    assert!(files.len() >= 5, "{files:?}");
    for file in files {
        assert!(
            !read(&file).to_lowercase().contains("fern"),
            "{file} names Fern"
        );
    }
}

/// The rows of the Markdown table under `## {heading}`: first cell (without its
/// backticks) to the remaining cells.
fn table(page: &str, heading: &str) -> Vec<(String, Vec<String>)> {
    let section = page
        .split(&format!("\n## {heading}\n"))
        .nth(1)
        .unwrap_or_else(|| panic!("no `## {heading}` section"))
        .split("\n## ")
        .next()
        .unwrap();
    section
        .lines()
        .filter(|line| line.starts_with("| `"))
        .map(|line| {
            let cells: Vec<String> = line
                .trim_matches('|')
                .split(" | ")
                .map(|cell| cell.trim().to_string())
                .collect();
            (cells[0].trim_matches('`').to_string(), cells[1..].to_vec())
        })
        .collect()
}

#[test]
fn the_docs_tables_agree_with_action_yml() {
    let page = read("docs/github-action.md");
    let action = yaml("action.yml");

    let inputs = table(&page, "Inputs");
    let names: Vec<&str> = inputs.iter().map(|(n, _)| n.as_str()).collect();
    assert_eq!(names, keys(mapping(&action, "inputs")));
    for (name, cells) in &inputs {
        let default = string(&action["inputs"][name.as_str()], "default").unwrap();
        let documented = &cells[0];
        if default.is_empty() {
            assert!(
                documented.starts_with("empty"),
                "{name}: action.yml defaults to empty, the docs say {documented}"
            );
        } else {
            assert_eq!(documented, &format!("`{default}`"), "{name}'s default");
        }
    }

    let outputs: Vec<String> = table(&page, "Outputs")
        .into_iter()
        .map(|(n, _)| n)
        .collect();
    assert_eq!(outputs, keys(mapping(&action, "outputs")));
}

const EXAMPLE: &str = "docs/examples/migrate-from-fern.yml";

#[test]
fn the_docs_embed_the_example_workflow_byte_identical() {
    let page = read("docs/github-action.md");
    let example = read(EXAMPLE);
    let blocks: Vec<&str> = page
        .split("\n```yaml\n")
        .skip(1)
        .map(|rest| rest.split("```\n").next().unwrap())
        .filter(|block| block.contains("nickderobertis/crozier@v0") && block.contains("\non:\n"))
        .collect();
    assert_eq!(
        blocks.len(),
        1,
        "docs/github-action.md must embed {EXAMPLE} exactly once"
    );
    if blocks[0] != example {
        let line = blocks[0]
            .lines()
            .zip(example.lines())
            .position(|(doc, file)| doc != file)
            .map_or_else(|| "the length".to_string(), |i| format!("line {}", i + 1));
        panic!("docs/github-action.md's copy of {EXAMPLE} differs from the file at {line}");
    }
}

/// `run:` scripts of every step of every job.
fn run_scripts(workflow: &Value) -> Vec<&str> {
    mapping(workflow, "jobs")
        .values()
        .flat_map(|job| job["steps"].as_sequence().unwrap())
        .filter_map(|step| string(step, "run"))
        .collect()
}

#[test]
fn the_example_workflow_is_a_pull_request_check_on_specs_and_configs() {
    let workflow = yaml(EXAMPLE);
    let on = mapping(&workflow, "on");
    assert_eq!(
        keys(on),
        ["pull_request", "push"],
        "no schedule, no other trigger"
    );
    assert_eq!(
        workflow["on"]["push"]["branches"],
        serde_yaml_ng::from_str::<Value>("[main]").unwrap()
    );
    for trigger in ["pull_request", "push"] {
        let paths: Vec<&str> = workflow["on"][trigger]["paths"]
            .as_sequence()
            .unwrap_or_else(|| panic!("{trigger} has no paths: filter"))
            .iter()
            .map(|p| p.as_str().unwrap())
            .collect();
        for config in [
            "crozier.yml",
            "crozier.yaml",
            ".crozier.yml",
            ".crozier.yaml",
        ] {
            assert!(
                paths.contains(&format!("**/{config}").as_str()),
                "{trigger} does not filter on {config} at any depth: {paths:?}"
            );
        }
        assert!(
            paths.iter().any(|p| p.contains("openapi")),
            "{trigger} names no OpenAPI spec glob: {paths:?}"
        );
    }

    let mut permissions = BTreeMap::new();
    for (k, v) in mapping(&workflow, "permissions") {
        permissions.insert(k.as_str().unwrap(), v.as_str().unwrap());
    }
    assert_eq!(permissions, BTreeMap::from([("contents", "read")]));

    for run in run_scripts(&workflow) {
        assert!(!run.contains("${{"), "a run: script interpolates: {run}");
    }

    let jobs = mapping(&workflow, "jobs");
    assert_eq!(jobs.len(), 1, "one job");
    let steps = jobs.values().next().unwrap()["steps"]
        .as_sequence()
        .unwrap();
    let uses = |prefix: &str| {
        steps
            .iter()
            .position(|s| string(s, "uses").is_some_and(|u| u.starts_with(prefix)))
    };
    let runs = |needle: &str| {
        steps
            .iter()
            .position(|s| string(s, "run").is_some_and(|r| r.contains(needle)))
    };
    let checkout = uses("actions/checkout@").expect("checks out");
    let node = uses("actions/setup-node@").expect("sets up Node");
    let launcher = runs("npm install -g fern-api").expect("installs the fern-api launcher");
    let docker = runs("docker version").expect("confirms the container runtime");
    let recipe = runs("<<'RECIPE'").expect("writes the recipe");
    let action = steps
        .iter()
        .position(|s| string(s, "uses") == Some("nickderobertis/crozier@v0"))
        .expect("runs nickderobertis/crozier@v0");
    assert_eq!(checkout, 0);
    for before in [node, launcher, docker, recipe] {
        assert!(before < action, "the action runs after the setup");
    }
    assert!(node < launcher);

    // The recipe is written to a file, and the action's reference command names
    // that file.
    let written = string(&steps[recipe], "run").unwrap();
    let file = written
        .split("cat > \"")
        .nth(1)
        .and_then(|rest| rest.split('"').next())
        .expect("the recipe is written with cat > \"<file>\"");
    assert!(written.contains(&format!("chmod +x \"{file}\"")));
    let with = &steps[action]["with"];
    assert_eq!(
        string(with, "reference-command"),
        Some(file.replace("$RUNNER_TEMP", "${{ runner.temp }}").as_str())
    );
    assert!(with.get("version").is_none(), "the example pins no version");
}
