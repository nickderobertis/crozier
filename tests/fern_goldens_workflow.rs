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

fn assert_optional_string_input(inputs: &Mapping, name: &str) {
    let input = nested_mapping(inputs, name);
    assert_eq!(input.get("required").and_then(Value::as_bool), Some(false));
    assert_eq!(input.get("type").and_then(Value::as_str), Some("string"));
}

#[test]
fn fern_goldens_workflow_is_valid_branch_safe_and_least_privilege() {
    let source = include_str!("../.github/workflows/fern-goldens.yml");
    let justfile = include_str!("../justfile");
    let tool = include_str!("../scripts/fern-goldens");
    let workflow: Value = serde_yaml_ng::from_str(source).expect("workflow is valid YAML");

    let triggers = mapping(&workflow, "on");
    assert_eq!(
        triggers.len(),
        1,
        "workflow_dispatch must be the only trigger"
    );
    let dispatch = nested_mapping(triggers, "workflow_dispatch");
    let inputs = nested_mapping(dispatch, "inputs");
    assert_optional_string_input(inputs, "fern-version");
    assert_optional_string_input(inputs, "fixtures");

    let permissions = mapping(&workflow, "permissions");
    assert_eq!(
        permissions.len(),
        1,
        "grant only the permission publication needs"
    );
    assert_eq!(
        permissions.get("contents").and_then(Value::as_str),
        Some("write")
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
    assert_eq!(jobs.len(), 1);
    let refresh = nested_mapping(jobs, "refresh");
    assert_eq!(
        refresh.get("runs-on").and_then(Value::as_str),
        Some("ubuntu-latest")
    );
    let steps = refresh
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("refresh steps must be a sequence");

    let (branch_index, branch) = named_step(steps, "Require a branch dispatch");
    assert!(branch
        .get("run")
        .and_then(Value::as_str)
        .is_some_and(|run| run.contains("REF_TYPE") && run.contains("branch")));
    let (checkout_index, checkout) = steps
        .iter()
        .enumerate()
        .find_map(|(index, step)| {
            let step = step.as_mapping()?;
            (step.get("uses").and_then(Value::as_str) == Some("actions/checkout@v4"))
                .then_some((index, step))
        })
        .expect("checkout step");
    assert!(branch_index < checkout_index);
    let checkout_with = nested_mapping(checkout, "with");
    assert_eq!(
        checkout_with.get("ref").and_then(Value::as_str),
        Some("${{ github.ref }}")
    );
    assert_eq!(
        checkout_with.get("fetch-depth").and_then(Value::as_u64),
        Some(0)
    );

    let (generation_index, generation) =
        named_step(steps, "Generate every selected fixture independently");
    let (comparison_index, comparison) =
        named_step(steps, "Compare every available golden without fail-fast");
    let (artifact_index, artifact) = named_step(steps, "Upload generation and comparison evidence");
    let (publication_index, publication) = named_step(steps, "Publish successful Fern goldens");
    let (final_index, final_status) = named_step(steps, "Apply final status");
    assert!(
        generation_index < comparison_index
            && comparison_index < artifact_index
            && artifact_index < publication_index
            && publication_index < final_index
    );
    for step in [generation, comparison, artifact, publication] {
        assert_eq!(
            step.get("continue-on-error").and_then(Value::as_bool),
            Some(true)
        );
    }
    for step in [artifact, publication, final_status] {
        assert_eq!(step.get("if").and_then(Value::as_str), Some("always()"));
    }

    let generation_env = nested_mapping(generation, "env");
    assert_eq!(
        generation_env.get("FERN_VERSION").and_then(Value::as_str),
        Some("${{ inputs.fern-version }}")
    );
    assert_eq!(
        generation_env.get("FIXTURES").and_then(Value::as_str),
        Some("${{ inputs.fixtures }}")
    );
    let generation_run = generation
        .get("run")
        .and_then(Value::as_str)
        .expect("generation command");
    assert!(generation_run.contains("args+=(--version \"$FERN_VERSION\")"));
    assert!(generation_run.contains("args+=(--fixtures \"$FIXTURES\")"));
    assert!(generation_run.contains("fern-goldens-generate \"${args[@]}\""));

    let publication_env = nested_mapping(publication, "env");
    assert_eq!(
        publication_env.get("BRANCH").and_then(Value::as_str),
        Some("${{ github.ref_name }}")
    );
    assert!(publication
        .get("run")
        .and_then(Value::as_str)
        .is_some_and(|run| run.contains("fern-goldens-publish \"$BRANCH\"")));

    let final_env = nested_mapping(final_status, "env");
    for (name, expression) in [
        ("GENERATION", "${{ steps.generation.outcome }}"),
        ("COMPARISON", "${{ steps.comparison.outcome }}"),
        ("PUBLICATION", "${{ steps.publication.outcome }}"),
        ("ARTIFACTS", "${{ steps.artifacts.outcome }}"),
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
    assert!(final_run.contains("ARTIFACTS"));
    assert!(final_run.contains("fern-goldens-result"));

    assert!(tool.contains("\"fetch\", \"--no-tags\""));
    assert!(tool.contains("HEAD:refs/heads/{branch}"));
    assert!(!source.contains("--force") && !tool.contains("--force"));
    assert!(!source.contains("pull-requests: write"));
    assert!(justfile.contains("set positional-arguments := true"));
    assert!(justfile.contains("./scripts/fern-goldens generate \"$@\""));
    assert!(justfile.contains("./scripts/fern-goldens publish --branch \"$1\""));
}
