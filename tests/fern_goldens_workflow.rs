use serde_yaml_ng::{Mapping, Value};

fn mapping<'a>(value: &'a Value, key: &str) -> &'a Mapping {
    value
        .get(key)
        .and_then(Value::as_mapping)
        .unwrap_or_else(|| panic!("{key} must be a mapping"))
}

fn nested_mapping<'a>(mapping: &'a Mapping, key: &str) -> &'a Mapping {
    mapping
        .get(key)
        .and_then(Value::as_mapping)
        .unwrap_or_else(|| panic!("{key} must be a mapping"))
}

fn named_step<'a>(steps: &'a [Value], name: &str) -> (usize, &'a Mapping) {
    steps
        .iter()
        .enumerate()
        .find_map(|(index, step)| {
            let step = step.as_mapping()?;
            (step.get("name").and_then(Value::as_str) == Some(name)).then_some((index, step))
        })
        .unwrap_or_else(|| panic!("missing workflow step {name:?}"))
}

fn action_step<'a>(steps: &'a [Value], uses: &str) -> (usize, &'a Mapping) {
    steps
        .iter()
        .enumerate()
        .find_map(|(index, step)| {
            let step = step.as_mapping()?;
            (step.get("uses").and_then(Value::as_str) == Some(uses)).then_some((index, step))
        })
        .unwrap_or_else(|| panic!("missing workflow action {uses:?}"))
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
fn fern_goldens_workflow_is_valid_branch_safe_and_least_privilege() {
    let source = include_str!("../.github/workflows/fern-goldens.yml");
    let justfile = include_str!("../justfile");
    let tool = include_str!("../scripts/fern-goldens");
    let workflow: Value = serde_yaml_ng::from_str(source).expect("workflow is valid YAML");

    let triggers = mapping(&workflow, "on");
    assert_eq!(triggers.len(), 2, "only weekly and manual runs are allowed");
    let schedule = triggers
        .get("schedule")
        .and_then(Value::as_sequence)
        .expect("schedule must be a sequence");
    assert_eq!(schedule.len(), 1, "exactly one weekly run is expected");
    assert_eq!(
        schedule[0].get("cron").and_then(Value::as_str),
        Some("17 5 * * 1"),
        "schedule must remain deterministic and weekly"
    );
    let dispatch = nested_mapping(triggers, "workflow_dispatch");
    let inputs = nested_mapping(dispatch, "inputs");
    assert_optional_string_input(inputs, "fern-version");
    assert_optional_string_input(inputs, "fixtures");

    let permissions = mapping(&workflow, "permissions");
    assert_eq!(
        permissions.len(),
        1,
        "default every job to read-only contents"
    );
    assert_eq!(
        permissions.get("contents").and_then(Value::as_str),
        Some("read")
    );

    let concurrency = mapping(&workflow, "concurrency");
    assert_eq!(
        concurrency.get("group").and_then(Value::as_str),
        Some("fern-goldens-${{ github.repository }}-${{ github.ref }}")
    );
    assert_eq!(
        concurrency
            .get("cancel-in-progress")
            .and_then(Value::as_bool),
        Some(false),
        "a branch writer must not be cancelled midway through publication"
    );

    let jobs = mapping(&workflow, "jobs");
    assert_eq!(jobs.len(), 3);
    let generate = nested_mapping(jobs, "generate_publish");
    assert_eq!(
        generate.get("runs-on").and_then(Value::as_str),
        Some("ubuntu-latest")
    );
    let generate_permissions = nested_mapping(generate, "permissions");
    assert_eq!(generate_permissions.len(), 1);
    assert_eq!(
        generate_permissions.get("contents").and_then(Value::as_str),
        Some("write"),
        "only the publication job may write contents"
    );
    let generate_outputs = nested_mapping(generate, "outputs");
    for (name, expression) in [
        ("generation", "${{ steps.generation.outcome }}"),
        ("publication", "${{ steps.publication.outcome }}"),
        (
            "generation_evidence",
            "${{ steps.generation_evidence.outcome }}",
        ),
        (
            "generation_summary",
            "${{ steps.generation_summary.outcome }}",
        ),
    ] {
        assert_eq!(
            generate_outputs.get(name).and_then(Value::as_str),
            Some(expression)
        );
    }
    let generate_steps = generate
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("generation/publication steps must be a sequence");

    let (branch_index, branch) = named_step(generate_steps, "Require a supported branch event");
    let branch_env = nested_mapping(branch, "env");
    for (name, expression) in [
        ("EVENT_NAME", "${{ github.event_name }}"),
        ("REF", "${{ github.ref }}"),
        ("REF_TYPE", "${{ github.ref_type }}"),
    ] {
        assert_eq!(
            branch_env.get(name).and_then(Value::as_str),
            Some(expression)
        );
    }
    let branch_run = branch
        .get("run")
        .and_then(Value::as_str)
        .expect("event/ref guard command");
    for required in [
        "schedule)",
        "refs/heads/main",
        "workflow_dispatch)",
        "REF_TYPE",
    ] {
        assert!(
            branch_run.contains(required),
            "event/ref guard is missing {required}"
        );
    }
    let (checkout_index, checkout) = action_step(generate_steps, "actions/checkout@v4");
    assert!(branch_index < checkout_index);
    let checkout_with = nested_mapping(checkout, "with");
    assert_eq!(
        checkout_with.get("ref").and_then(Value::as_str),
        Some("${{ github.ref_name }}")
    );
    assert_eq!(
        checkout_with.get("fetch-depth").and_then(Value::as_u64),
        Some(0)
    );

    let (generation_index, generation_step) = named_step(
        generate_steps,
        "Generate every selected fixture independently",
    );
    let (publication_index, publication) =
        named_step(generate_steps, "Publish successful Fern goldens");
    let (generation_summary_index, generation_summary) =
        named_step(generate_steps, "Write generation summary");
    let (generation_evidence_index, generation_evidence) =
        named_step(generate_steps, "Upload generation evidence");
    assert!(
        generation_index < publication_index
            && publication_index < generation_summary_index
            && generation_summary_index < generation_evidence_index
    );
    for step in [
        generation_step,
        publication,
        generation_summary,
        generation_evidence,
    ] {
        assert_eq!(
            step.get("continue-on-error").and_then(Value::as_bool),
            Some(true)
        );
    }
    for step in [publication, generation_summary, generation_evidence] {
        assert_eq!(step.get("if").and_then(Value::as_str), Some("always()"));
    }

    let generation_env = nested_mapping(generation_step, "env");
    assert_eq!(
        generation_env.get("FERN_VERSION").and_then(Value::as_str),
        Some("${{ github.event_name == 'workflow_dispatch' && inputs.fern-version || '' }}")
    );
    assert_eq!(
        generation_env.get("FIXTURES").and_then(Value::as_str),
        Some("${{ github.event_name == 'workflow_dispatch' && inputs.fixtures || '' }}")
    );
    let generation_run = generation_step
        .get("run")
        .and_then(Value::as_str)
        .expect("generation command");
    assert!(generation_run.contains("set -- \"$@\" --version \"$FERN_VERSION\""));
    assert!(generation_run.contains("set -- \"$@\" --fixtures \"$FIXTURES\""));
    assert!(generation_run.contains("fern-goldens-generate \"$@\""));
    assert!(
        !generation_run.contains("${args[@]}"),
        "Bash 3.2 treats an empty array expansion as unbound under set -u"
    );

    let publication_env = nested_mapping(publication, "env");
    assert_eq!(
        publication_env.get("BRANCH").and_then(Value::as_str),
        Some("${{ github.ref_name }}")
    );
    assert!(publication
        .get("run")
        .and_then(Value::as_str)
        .is_some_and(|run| run.contains("fern-goldens-publish \"$BRANCH\"")));

    let generation_summary_run = generation_summary
        .get("run")
        .and_then(Value::as_str)
        .expect("generation summary command");
    assert!(generation_summary_run.contains("generation-summary.txt"));
    assert!(generation_summary_run.contains("$GITHUB_STEP_SUMMARY"));

    let generation_evidence_with = nested_mapping(generation_evidence, "with");
    assert_eq!(
        generation_evidence_with.get("name").and_then(Value::as_str),
        Some("fern-goldens-generation-${{ github.run_id }}-${{ github.run_attempt }}")
    );
    let generation_evidence_paths = generation_evidence_with
        .get("path")
        .and_then(Value::as_str)
        .expect("generation artifact paths");
    for path in [
        "generation-summary.txt",
        "generation-failures.txt",
        "known-upstream-failures.txt",
        "generation-logs/",
        "generated-goldens.tar.gz",
        "fern-goldens.patch",
    ] {
        assert!(generation_evidence_paths.contains(path), "missing {path}");
    }

    let comparison = nested_mapping(jobs, "compare");
    assert_eq!(
        comparison.get("needs").and_then(Value::as_str),
        Some("generate_publish"),
        "comparison cannot start before publication and generation evidence finish"
    );
    assert_eq!(
        comparison.get("if").and_then(Value::as_str),
        Some("always()")
    );
    assert_eq!(
        comparison.get("runs-on").and_then(Value::as_str),
        Some("ubuntu-latest")
    );
    assert!(
        comparison.get("permissions").is_none(),
        "comparison must inherit read-only contents"
    );
    let comparison_outputs = nested_mapping(comparison, "outputs");
    assert_eq!(
        comparison_outputs.get("comparison").and_then(Value::as_str),
        Some("${{ steps.comparison.outcome }}")
    );
    assert_eq!(
        comparison_outputs
            .get("comparison_summary")
            .and_then(Value::as_str),
        Some("${{ steps.comparison_summary.outcome }}")
    );
    assert_eq!(
        comparison_outputs
            .get("comparison_evidence")
            .and_then(Value::as_str),
        Some("${{ steps.comparison_evidence.outcome }}")
    );
    let comparison_steps = comparison
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("comparison steps must be a sequence");
    let (_, comparison_checkout) = action_step(comparison_steps, "actions/checkout@v4");
    let comparison_checkout_with = nested_mapping(comparison_checkout, "with");
    assert_eq!(
        comparison_checkout_with.get("ref").and_then(Value::as_str),
        Some("${{ github.ref_name }}")
    );
    assert_eq!(
        comparison_checkout_with
            .get("fetch-depth")
            .and_then(Value::as_u64),
        Some(0)
    );
    let (comparison_index, comparison_step) = named_step(
        comparison_steps,
        "Compare every available golden without fail-fast",
    );
    let (comparison_summary_index, comparison_summary) =
        named_step(comparison_steps, "Write comparison summary");
    let (comparison_evidence_index, comparison_evidence) =
        named_step(comparison_steps, "Upload comparison evidence");
    assert!(
        comparison_index < comparison_summary_index
            && comparison_summary_index < comparison_evidence_index
    );
    for step in [comparison_step, comparison_summary, comparison_evidence] {
        assert_eq!(
            step.get("continue-on-error").and_then(Value::as_bool),
            Some(true)
        );
    }
    for step in [comparison_summary, comparison_evidence] {
        assert_eq!(step.get("if").and_then(Value::as_str), Some("always()"));
    }
    let comparison_summary_run = comparison_summary
        .get("run")
        .and_then(Value::as_str)
        .expect("comparison summary command");
    assert!(comparison_summary_run.contains("comparison-summary.txt"));
    assert!(comparison_summary_run.contains("$GITHUB_STEP_SUMMARY"));
    let comparison_evidence_with = nested_mapping(comparison_evidence, "with");
    assert_eq!(
        comparison_evidence_with.get("name").and_then(Value::as_str),
        Some("fern-goldens-comparison-${{ github.run_id }}-${{ github.run_attempt }}")
    );
    let comparison_evidence_paths = comparison_evidence_with
        .get("path")
        .and_then(Value::as_str)
        .expect("comparison artifact paths");
    for path in [
        "comparison-summary.txt",
        "comparison.log",
        "comparison-fetch-failures.txt",
        "comparison-processing-failures.txt",
        "comparison-known-upstream-failures.txt",
    ] {
        assert!(comparison_evidence_paths.contains(path), "missing {path}");
    }

    let final_job = nested_mapping(jobs, "final_status");
    assert!(
        final_job.get("permissions").is_none(),
        "final status must inherit read-only contents"
    );
    assert_eq!(
        final_job.get("if").and_then(Value::as_str),
        Some("always()")
    );
    let final_needs = final_job
        .get("needs")
        .and_then(Value::as_sequence)
        .expect("final status needs both phase jobs");
    assert_eq!(
        final_needs
            .iter()
            .filter_map(Value::as_str)
            .collect::<Vec<_>>(),
        ["generate_publish", "compare"]
    );
    let final_steps = final_job
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("final status steps must be a sequence");
    let (_, final_checkout) = action_step(final_steps, "actions/checkout@v4");
    assert_eq!(
        nested_mapping(final_checkout, "with")
            .get("ref")
            .and_then(Value::as_str),
        Some("${{ github.ref_name }}")
    );
    let (_, final_status) = named_step(final_steps, "Apply final status");
    let final_env = nested_mapping(final_status, "env");
    for (name, expression) in [
        (
            "GENERATION",
            "${{ needs.generate_publish.outputs.generation }}",
        ),
        (
            "PUBLICATION",
            "${{ needs.generate_publish.outputs.publication }}",
        ),
        (
            "GENERATION_EVIDENCE",
            "${{ needs.generate_publish.outputs.generation_evidence }}",
        ),
        (
            "GENERATION_SUMMARY",
            "${{ needs.generate_publish.outputs.generation_summary }}",
        ),
        ("COMPARISON", "${{ needs.compare.outputs.comparison }}"),
        (
            "COMPARISON_SUMMARY",
            "${{ needs.compare.outputs.comparison_summary }}",
        ),
        (
            "COMPARISON_EVIDENCE",
            "${{ needs.compare.outputs.comparison_evidence }}",
        ),
    ] {
        assert_eq!(
            final_env.get(name).and_then(Value::as_str),
            Some(expression)
        );
    }
    let final_run = final_status
        .get("run")
        .and_then(Value::as_str)
        .expect("final status command");
    assert!(final_run.contains("fern-goldens-result"));
    assert!(final_run.contains("--generation-evidence"));
    assert!(final_run.contains("--generation-summary"));
    assert!(final_run.contains("--comparison-evidence"));
    assert!(final_run.contains("--comparison-summary"));

    assert!(tool.contains("\"fetch\", \"--no-tags\""));
    assert!(tool.contains("HEAD:refs/heads/{branch}"));
    assert!(!source.contains("--force") && !tool.contains("--force"));
    assert!(!source.contains("pull-requests: write"));
    assert!(justfile.contains("set positional-arguments := true"));
    assert!(justfile.contains("./scripts/fern-goldens generate \"$@\""));
    assert!(justfile.contains("./scripts/fern-goldens publish --branch \"$1\""));
    assert!(justfile.contains("crozier-fixtures-diff.XXXXXX"));
    assert!(!justfile.contains("out=$(CROZIER_DIFF_CORPUS"));
}

#[cfg(unix)]
#[test]
fn fern_goldens_event_guard_accepts_only_scheduled_main_or_a_dispatched_branch() {
    use std::process::Command;

    let workflow: Value =
        serde_yaml_ng::from_str(include_str!("../.github/workflows/fern-goldens.yml"))
            .expect("workflow is valid YAML");
    let generate = nested_mapping(mapping(&workflow, "jobs"), "generate_publish");
    let steps = generate
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("generation/publication steps must be a sequence");
    let (_, guard) = named_step(steps, "Require a supported branch event");
    let command = guard
        .get("run")
        .and_then(Value::as_str)
        .expect("event/ref guard command");

    for (event, reference, ref_type, accepted) in [
        ("schedule", "refs/heads/main", "branch", true),
        (
            "workflow_dispatch",
            "refs/heads/feat/fern-upgrade",
            "branch",
            true,
        ),
        ("schedule", "refs/heads/release", "branch", false),
        ("workflow_dispatch", "refs/tags/v1.0.0", "tag", false),
        ("push", "refs/heads/main", "branch", false),
    ] {
        let output = Command::new("/bin/bash")
            .args(["-euo", "pipefail", "-c", command])
            .env("EVENT_NAME", event)
            .env("REF", reference)
            .env("REF_TYPE", ref_type)
            .output()
            .expect("run event/ref guard with the workflow shell");
        assert_eq!(
            output.status.success(),
            accepted,
            "unexpected guard result for {event} on {reference}: {}",
            String::from_utf8_lossy(&output.stderr)
        );
    }
}

#[cfg(unix)]
#[test]
fn fern_goldens_generation_step_preserves_blank_schedule_and_exact_manual_inputs() {
    use std::fs;
    use std::os::unix::fs::PermissionsExt;
    use std::process::Command;

    let workflow: Value =
        serde_yaml_ng::from_str(include_str!("../.github/workflows/fern-goldens.yml"))
            .expect("workflow is valid YAML");
    let generate = nested_mapping(mapping(&workflow, "jobs"), "generate_publish");
    let steps = generate
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("generation/publication steps must be a sequence");
    let (_, generation) = named_step(steps, "Generate every selected fixture independently");
    let command = generation
        .get("run")
        .and_then(Value::as_str)
        .expect("generation command");

    let temporary = tempfile::tempdir().expect("temporary fake action PATH");
    let fake_just = temporary.path().join("just");
    fs::write(&fake_just, "#!/bin/sh\nprintf '%s\\n' \"$@\"\n")
        .expect("write fake just executable");
    fs::set_permissions(&fake_just, fs::Permissions::from_mode(0o755))
        .expect("make fake just executable");

    for (version, fixtures, expected) in [
        ("", "", "fern-goldens-generate\n"),
        (
            "5.20.0",
            "redocly.com-museum,anchore.io",
            "fern-goldens-generate\n--version\n5.20.0\n--fixtures\nredocly.com-museum,anchore.io\n",
        ),
    ] {
        let output = Command::new("/bin/bash")
            .args(["-euo", "pipefail", "-c", command])
            .env("PATH", temporary.path())
            .env("FERN_VERSION", version)
            .env("FIXTURES", fixtures)
            .output()
            .expect("run generation argument boundary with the workflow shell");
        assert!(
            output.status.success(),
            "generation boundary failed: {}",
            String::from_utf8_lossy(&output.stderr)
        );
        assert_eq!(String::from_utf8_lossy(&output.stdout), expected);
    }
}
