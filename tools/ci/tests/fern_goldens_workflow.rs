#[path = "../../../src/yaml.rs"]
mod yaml;

use serde_json::Value;
type Mapping = serde_json::Map<String, Value>;

const WORKFLOW: &str = include_str!("../../../.github/workflows/fern-goldens.yml");
const WEEKLY: &str = include_str!("../../../tools/fern-goldens/weekly.py");

fn workflow() -> Value {
    crate::yaml::from_str(WORKFLOW).expect("workflow is valid YAML")
}

fn mapping<'a>(value: &'a Value, key: &str) -> &'a Mapping {
    value
        .get(key)
        .and_then(Value::as_object)
        .unwrap_or_else(|| panic!("{key} must be a mapping"))
}

fn nested_mapping<'a>(mapping: &'a Mapping, key: &str) -> &'a Mapping {
    mapping
        .get(key)
        .and_then(Value::as_object)
        .unwrap_or_else(|| panic!("{key} must be a mapping"))
}

fn text<'a>(mapping: &'a Mapping, key: &str) -> &'a str {
    mapping
        .get(key)
        .and_then(Value::as_str)
        .unwrap_or_else(|| panic!("{key} must be a string"))
}

fn steps(job: &Mapping) -> &[Value] {
    job.get("steps")
        .and_then(Value::as_array)
        .expect("a job's steps are a sequence")
}

fn named_step<'a>(steps: &'a [Value], name: &str) -> (usize, &'a Mapping) {
    steps
        .iter()
        .enumerate()
        .find_map(|(index, step)| {
            let step = step.as_object()?;
            (step.get("name").and_then(Value::as_str) == Some(name)).then_some((index, step))
        })
        .unwrap_or_else(|| panic!("missing workflow step {name:?}"))
}

fn uses_steps<'a>(steps: &'a [Value], uses: &str) -> Vec<(usize, &'a Mapping)> {
    steps
        .iter()
        .enumerate()
        .filter_map(|(index, step)| {
            let step = step.as_object()?;
            (step.get("uses").and_then(Value::as_str) == Some(uses)).then_some((index, step))
        })
        .collect()
}

fn assert_optional_string_input(inputs: &Mapping, name: &str) {
    let input = nested_mapping(inputs, name);
    assert_eq!(input.get("required").and_then(Value::as_bool), Some(false));
    assert_eq!(input.get("type").and_then(Value::as_str), Some("string"));
    assert!(
        input.get("default").is_none(),
        "{name} must default to blank"
    );
}

#[test]
fn fern_goldens_workflow_runs_weekly_sharded_and_least_privilege() {
    let workflow = workflow();
    let triggers = mapping(&workflow, "on");
    assert_eq!(triggers.len(), 2, "only weekly and manual runs are allowed");
    let schedule = triggers
        .get("schedule")
        .and_then(Value::as_array)
        .expect("schedule must be a sequence");
    assert_eq!(schedule.len(), 1, "exactly one weekly run is expected");
    assert_eq!(
        schedule[0].get("cron").and_then(Value::as_str),
        Some("17 5 * * 1"),
        "schedule must remain deterministic and weekly"
    );
    let inputs = nested_mapping(nested_mapping(triggers, "workflow_dispatch"), "inputs");
    for name in ["fern-cli-version", "fern-version", "items"] {
        assert_optional_string_input(inputs, name);
    }

    let permissions = mapping(&workflow, "permissions");
    assert_eq!(permissions.len(), 1, "every job reads contents only");
    assert_eq!(text(permissions, "contents"), "read");
    let concurrency = mapping(&workflow, "concurrency");
    assert_eq!(
        text(concurrency, "group"),
        "fern-goldens-${{ github.repository }}"
    );
    assert_eq!(
        concurrency
            .get("cancel-in-progress")
            .and_then(Value::as_bool),
        Some(false),
        "a run must not be cancelled midway through publication"
    );

    let jobs = mapping(&workflow, "jobs");
    assert_eq!(
        jobs.keys().map(String::as_str).collect::<Vec<_>>(),
        ["plan", "shard", "assemble", "decide", "publish"]
    );
    for (name, job) in jobs {
        let job = job.as_object().expect("a job is a mapping");
        assert!(
            job.get("permissions").is_none(),
            "{name} must inherit read-only contents"
        );
        let minutes = job
            .get("timeout-minutes")
            .and_then(Value::as_u64)
            .unwrap_or_else(|| panic!("{name} sets timeout-minutes"));
        assert!(
            minutes < 360,
            "{name} stays inside GitHub's six-hour job limit"
        );
    }

    // The shard matrix is the planner's, never a hand-edited constant.
    let shard = nested_mapping(jobs, "shard");
    assert_eq!(text(shard, "needs"), "plan");
    assert_eq!(text(shard, "if"), "needs.plan.outputs.run == 'true'");
    let strategy = nested_mapping(shard, "strategy");
    assert_eq!(
        strategy.get("fail-fast").and_then(Value::as_bool),
        Some(false)
    );
    assert_eq!(
        text(strategy, "matrix"),
        "${{ fromJSON(needs.plan.outputs.matrix) }}"
    );
    let plan = nested_mapping(jobs, "plan");
    assert_eq!(
        text(nested_mapping(plan, "outputs"), "matrix"),
        "${{ steps.plan.outputs.matrix }}"
    );
    let (_, upload) = uses_steps(steps(shard), "actions/upload-artifact@v4")[0];
    assert_eq!(text(upload, "if"), "always()");
    let upload = nested_mapping(upload, "with");
    assert_eq!(
        text(upload, "name"),
        "fern-goldens-shard-${{ matrix.shard }}"
    );
    assert_eq!(
        upload.get("include-hidden-files").and_then(Value::as_bool),
        Some(true),
        "Fern's .fern/metadata.json and the golden provenance are hidden files"
    );

    // One assembly over every shard, even when one failed, so it names it.
    let assemble = nested_mapping(jobs, "assemble");
    assert_eq!(
        text(assemble, "if"),
        "always() && needs.plan.outputs.run == 'true'"
    );
    let downloads = uses_steps(steps(assemble), "actions/download-artifact@v4");
    let shards = downloads
        .iter()
        .find(|(_, step)| {
            nested_mapping(step, "with")
                .get("pattern")
                .and_then(Value::as_str)
                == Some("fern-goldens-shard-*")
        })
        .expect("the assembly downloads every shard");
    assert_eq!(
        shards.1.get("continue-on-error").and_then(Value::as_bool),
        Some(true)
    );

    // The decision runs crozier's comparison with Nx installed (the old
    // compare job had none, so it failed on every fixture), after the tree is
    // the one the pull request would carry.
    let decide = nested_mapping(jobs, "decide");
    assert!(decide.get("if").is_none(), "decide needs a green assembly");
    let decide_steps = steps(decide);
    let (bootstrap, bootstrap_step) = named_step(decide_steps, "Bootstrap");
    assert_eq!(text(bootstrap_step, "run"), "just bootstrap");
    assert!(!uses_steps(decide_steps, "oven-sh/setup-bun@v2").is_empty());
    let (apply, _) = named_step(
        decide_steps,
        "Lay the regenerated references over this checkout",
    );
    let (build, build_step) = named_step(decide_steps, "Build crozier from that tree");
    assert_eq!(
        text(build_step, "run"),
        "cargo build --locked --bin crozier"
    );
    let (decision, _) = named_step(decide_steps, "Decide with crozier's own comparison");
    assert!(bootstrap < apply && apply < build && build < decision);

    // Only the complete run publishes, with the PAT whose pull requests trigger
    // crozier's required checks.
    let publish = nested_mapping(jobs, "publish");
    assert_eq!(
        publish
            .get("needs")
            .and_then(Value::as_array)
            .map(|needs| needs.iter().filter_map(Value::as_str).collect::<Vec<_>>()),
        Some(vec!["plan", "decide"])
    );
    assert_eq!(text(publish, "if"), "needs.plan.outputs.complete == 'true'");
    let publish_steps = steps(publish);
    let (_, checkout) = uses_steps(publish_steps, "actions/checkout@v4")[0];
    assert_eq!(
        text(nested_mapping(checkout, "with"), "token"),
        "${{ secrets.RELEASE_PLZ_TOKEN }}"
    );
    let (_, opened) = named_step(publish_steps, "Open, update or finish the pull request");
    assert_eq!(
        text(nested_mapping(opened, "env"), "GH_TOKEN"),
        "${{ secrets.RELEASE_PLZ_TOKEN }}"
    );

    // Thin YAML: every phase is the script's.
    for (job, phase) in [
        ("plan", "resolve"),
        ("plan", "plan"),
        ("shard", "shard"),
        ("assemble", "assemble"),
        ("decide", "apply"),
        ("decide", "decide"),
        ("publish", "publish"),
    ] {
        let job = nested_mapping(jobs, job);
        assert!(
            steps(job).iter().any(|step| {
                step.get("run").and_then(Value::as_str).is_some_and(|run| {
                    run.contains(&format!("tools/fern-goldens/weekly.py {phase} "))
                })
            }),
            "{phase} runs as tools/fern-goldens/weekly.py {phase}"
        );
    }
}

#[test]
fn fern_goldens_never_pushes_to_main_and_force_pushes_only_its_own_branch_with_a_lease() {
    for source in [WORKFLOW, WEEKLY] {
        for forbidden in [
            "HEAD:refs/heads/main",
            "HEAD:main",
            "push origin main",
            "--force ",
            "pull-requests: write",
            "contents: write",
        ] {
            assert!(!source.contains(forbidden), "found {forbidden:?}");
        }
    }
    assert!(WEEKLY.contains("BRANCH = \"fern-goldens/update\""));
    assert!(WEEKLY.contains("LABEL = \"fern-goldens\""));
    assert!(WEEKLY.contains("f\"--force-with-lease=refs/heads/{BRANCH}:{remote}\""));
    assert!(WEEKLY.contains("f\"HEAD:refs/heads/{BRANCH}\""));
    assert_eq!(WEEKLY.matches("--force").count(), 1);
}

#[cfg(unix)]
#[test]
fn fern_goldens_resolve_step_passes_blank_schedule_inputs_and_exact_dispatch_inputs() {
    use std::fs;
    use std::os::unix::fs::PermissionsExt;
    use std::process::Command;

    let workflow = workflow();
    let plan = nested_mapping(mapping(&workflow, "jobs"), "plan");
    let (_, resolve) = named_step(steps(plan), "Resolve the pair to check");
    let env = nested_mapping(resolve, "env");
    for (name, expression) in [
        ("REF", "${{ github.ref }}"),
        (
            "CLI_VERSION",
            "${{ github.event_name == 'workflow_dispatch' && inputs.fern-cli-version || '' }}",
        ),
        (
            "GENERATOR_VERSION",
            "${{ github.event_name == 'workflow_dispatch' && inputs.fern-version || '' }}",
        ),
        (
            "ITEMS",
            "${{ github.event_name == 'workflow_dispatch' && inputs.items || '' }}",
        ),
        ("TOKEN_PRESENT", "${{ secrets.RELEASE_PLZ_TOKEN != '' }}"),
    ] {
        assert_eq!(text(env, name), expression);
    }
    let command = text(resolve, "run");

    let temporary = tempfile::tempdir().expect("temporary fake action PATH");
    let fake = temporary.path().join("python3");
    fs::write(&fake, "#!/bin/sh\nprintf '%s\\n' \"$@\"\n").expect("write fake python3");
    fs::set_permissions(&fake, fs::Permissions::from_mode(0o755)).expect("make it executable");
    for (versions, items, token, expected) in [
        (
            ("", ""),
            "",
            "true",
            "tools/fern-goldens/weekly.py\nresolve\n--ref\nrefs/heads/main\n--cli-version\n\n\
             --generator-version\n\n--items\n\n--token-present\n",
        ),
        (
            ("5.170.0", "5.42.0"),
            "handwritten,corpus:anchore.io",
            "false",
            "tools/fern-goldens/weekly.py\nresolve\n--ref\nrefs/heads/main\n--cli-version\n5.170.0\n\
             --generator-version\n5.42.0\n--items\nhandwritten,corpus:anchore.io\n",
        ),
    ] {
        let output = Command::new("/bin/bash")
            .args(["-euo", "pipefail", "-c", command])
            .env("PATH", temporary.path())
            .env("REF", "refs/heads/main")
            .env("CLI_VERSION", versions.0)
            .env("GENERATOR_VERSION", versions.1)
            .env("ITEMS", items)
            .env("TOKEN_PRESENT", token)
            .env("GITHUB_OUTPUT", "/dev/null")
            .env("GITHUB_STEP_SUMMARY", "/dev/null")
            .output()
            .expect("run the resolve step with the workflow shell");
        assert!(
            output.status.success(),
            "resolve step failed: {}",
            String::from_utf8_lossy(&output.stderr)
        );
        let printed = String::from_utf8_lossy(&output.stdout);
        let expected = format!(
            "{expected}--github-output\n/dev/null\n--summary\n/dev/null\n"
        );
        assert_eq!(printed, expected);
    }
}
