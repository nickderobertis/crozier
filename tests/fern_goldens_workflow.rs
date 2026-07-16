use serde_yaml_ng::Value;

fn mapping<'a>(value: &'a Value, key: &str) -> &'a serde_yaml_ng::Mapping {
    value
        .get(key)
        .and_then(Value::as_mapping)
        .unwrap_or_else(|| panic!("{key} must be a mapping"))
}

#[test]
fn fern_goldens_workflow_is_valid_branch_safe_and_least_privilege() {
    let source = include_str!("../.github/workflows/fern-goldens.yml");
    let tool = include_str!("../scripts/fern-goldens");
    let workflow: Value = serde_yaml_ng::from_str(source).expect("workflow is valid YAML");

    let triggers = mapping(&workflow, "on");
    assert_eq!(
        triggers.len(),
        1,
        "workflow_dispatch must be the only trigger"
    );
    assert!(triggers.contains_key("workflow_dispatch"));

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
    let group = concurrency
        .get("group")
        .and_then(Value::as_str)
        .expect("concurrency group");
    assert!(
        group.contains("github.ref"),
        "concurrency must be branch/ref scoped"
    );
    assert_eq!(
        concurrency
            .get("cancel-in-progress")
            .and_then(Value::as_bool),
        Some(false),
        "a writer must not be cancelled midway through publication"
    );

    assert!(source.contains("github.ref_type"));
    assert!(source.contains("github.ref_name"));
    assert!(tool.contains("\"fetch\", \"--no-tags\""));
    assert!(tool.contains("HEAD:refs/heads/{branch}"));
    assert!(!source.contains("--force") && !tool.contains("--force"));
    assert!(!source.contains("pull-requests: write"));

    let artifact = source
        .find("Upload generation and comparison evidence")
        .unwrap();
    let publication = source.find("Publish successful Fern goldens").unwrap();
    let final_status = source.find("Apply final status").unwrap();
    assert!(artifact < publication && publication < final_status);
    assert!(source[publication..final_status].contains("continue-on-error: true"));
    assert!(source[final_status..].contains("if: always()"));
}
