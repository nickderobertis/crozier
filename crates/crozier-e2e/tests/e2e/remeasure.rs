//! Residuals measured after the handed-off repairs, against complete certified trees.

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root};

pub(crate) const DIR: &str = "docs/fern-measurements/handed-off/remeasure";

fn generate(cause: &str) -> (tempfile::TempDir, std::path::PathBuf, std::path::PathBuf) {
    let work = tempfile::tempdir().expect("measurement output");
    let out = work.path().join("sdk");
    let case = repo_root().join(DIR).join(cause);
    probe_command(&case.join("openapi.yml"), &out)
        .assert()
        .success();
    let golden = format!("{DIR}/{cause}/fern-expected");
    let inherited = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let failures = golden_tree_failures(
        cause,
        &case.join("openapi.yml").display().to_string(),
        &inherited,
        &case.join("fern-expected"),
        &out,
    );
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
    let overlay = case.join("expected-literals/fern-expected");
    if overlay.is_dir() {
        let manifest: serde_json::Value = serde_json::from_str(
            &std::fs::read_to_string(overlay.join(".crozier-overlay.json")).unwrap(),
        )
        .unwrap();
        assert_eq!(manifest["enum_type"], "literals");
        let removed = manifest["removed"]
            .as_array()
            .expect("removed overlay paths");
        let reference = work.path().join("reference-literals");
        for source in [case.join("fern-expected"), overlay.clone()] {
            for relative in crozier::parity::walk_files(&source).unwrap() {
                if relative == ".crozier-overlay.json"
                    || source != overlay
                        && removed
                            .iter()
                            .any(|value| value.as_str() == Some(relative.as_str()))
                {
                    continue;
                }
                let destination = reference.join(&relative);
                std::fs::create_dir_all(destination.parent().unwrap()).unwrap();
                std::fs::copy(source.join(&relative), destination).unwrap();
            }
        }
        let literals = work.path().join("sdk-literals");
        probe_command(&case.join("openapi.yml"), &literals)
            .args(["--enum-type", "literals"])
            .assert()
            .success();
        let own = crozier::parity::walk_files(&overlay)
            .unwrap()
            .into_iter()
            .filter(|path| path != ".crozier-overlay.json")
            .collect();
        let removed: Vec<String> = removed
            .iter()
            .map(|value| value.as_str().unwrap().to_string())
            .collect();
        let ledger = departure_ledger()
            .golden(
                &format!("{DIR}/{cause}/expected-literals/fern-expected"),
                &[],
            )
            .unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
            .inherit(inherited, own, &removed);
        let failures = golden_tree_failures(
            &format!("{cause} (literals)"),
            &case.join("openapi.yml").display().to_string(),
            &ledger,
            &reference,
            &literals,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n\n"));
    }
    (work, case, out)
}

#[test]
fn remeasure_collapsed_body_keeps_the_shared_model_and_documents_accepted_fields() {
    let (_work, case, out) = generate("json-ref-body-kept-whole");
    assert!(out.join("src/fern/types/label_registration.py").is_file());
    let raw = std::fs::read_to_string(out.join("src/fern/raw_client.py")).unwrap();
    assert!(raw.contains("label: str"));
    assert!(!raw.contains("\"content-type\""));
    let reference = std::fs::read_to_string(out.join("reference.md")).unwrap();
    assert!(reference.contains("**label:** `str`"));
    assert!(!reference.contains("**request:** `LabelRegistration`"));
    assert_eq!(
        reference
            .matches("**request:** `ArchiveRegistration`")
            .count(),
        2
    );
    std::fs::write(
        out.join("reference.md"),
        reference.replace("**label:** `str`", "**label:** `int`"),
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path == "reference.md"));
}

#[test]
fn remeasure_split_media_body_writes_no_unreferenced_json_model() {
    let (_work, case, out) = generate("split-media-body-orphan-model");
    let model = out.join("src/fern/types/recording_url.py");
    assert!(!model.exists());
    std::fs::create_dir_all(model.parent().unwrap()).unwrap();
    std::fs::write(&model, "class RecordingUrl:\n    url: str\n").unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path.ends_with("recording_url.py")));
}

#[test]
fn remeasure_nullable_union_keeps_response_names_and_unknown_body_omits_header() {
    let (_work, case, out) = generate("nullable-union-and-unknown-body");
    let raw = std::fs::read_to_string(out.join("src/fern/raw_client.py")).unwrap();
    assert!(!raw.contains("\"content-type\""));
    assert!(out
        .join("src/fern/types/get_shipment_response.py")
        .is_file());
    assert!(!out
        .join("src/fern/types/get_shipment_response_zero.py")
        .exists());
    std::fs::write(
        out.join("src/fern/raw_client.py"),
        raw.replace(
            "json=request,",
            "json=request,\n            headers={\"content-type\": \"application/json\"},",
        ),
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path.ends_with("raw_client.py")));
}

#[test]
fn remeasure_parent_examples_keep_valid_map_values_and_replace_invalid_ones() {
    let (_work, case, out) = generate("parent-example-map-values");
    let reference = std::fs::read_to_string(out.join("reference.md")).unwrap();
    assert!(reference.contains("\"key\": \"{}\""));
    assert!(reference.contains("\"key\": {\n                    \"key\": \"value\""));
    std::fs::write(
        out.join("reference.md"),
        reference.replace("\"key\": \"{}\"", "\"key\": \"unexpected\""),
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path == "reference.md"));
}

#[test]
fn remeasure_group_placement_carries_synthetic_children_but_not_other_components() {
    let (_work, case, out) = generate("group-placed-nested-type-placement");
    for file in [
        "depot_record_status.py",
        "depot_record_contents_item.py",
        "depot_record_contents_item_size.py",
    ] {
        assert!(
            out.join("src/fern/depot/types").join(file).is_file(),
            "{file}"
        );
        assert!(!out.join("src/fern/types").join(file).exists(), "{file}");
    }
    assert!(out.join("src/fern/types/warehouse.py").is_file());
    assert!(!out.join("src/fern/depot/types/warehouse.py").exists());
    let misplaced = out.join("src/fern/types/depot_record_status.py");
    std::fs::copy(
        out.join("src/fern/depot/types/depot_record_status.py"),
        &misplaced,
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path == "src/fern/types/depot_record_status.py"));
}

fn generate_control(
    work: &std::path::Path,
    label: &str,
    document: &serde_json::Value,
) -> std::path::PathBuf {
    let spec = work.join(format!("{label}.json"));
    let out = work.join(label);
    std::fs::write(&spec, serde_json::to_string_pretty(document).unwrap()).unwrap();
    probe_command(&spec, &out).assert().success();
    out
}

#[test]
fn remeasure_datetime_override_preserves_the_declared_temporal_type() {
    let (work, case, out) = generate("x-fern-type-extension");
    let original: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(case.join("openapi.yml")).unwrap()).unwrap();
    for (label, canonical, temporal) in [
        ("canonical-datetime", "datetime", true),
        ("unsupported-canonical", "unsupported", false),
        ("boolean-canonical", "literal<false>", false),
    ] {
        let mut document = original.clone();
        for name in ["capturedAt", "queuedAt"] {
            let field = document
                .pointer_mut(&format!("/components/schemas/Scan/properties/{name}"))
                .unwrap()
                .as_object_mut()
                .unwrap();
            field.insert("x-crozier-type".into(), canonical.into());
            if temporal {
                field.insert("x-fern-type".into(), "literal<true>".into());
            }
        }
        let generated = generate_control(work.path(), label, &document);
        let model = std::fs::read_to_string(generated.join("src/fern/types/scan.py")).unwrap();
        assert_eq!(
            model.matches("typing.Optional[dt.datetime]").count(),
            if temporal { 2 } else { 0 },
            "{label}"
        );
        if temporal {
            let failures = golden_tree_failures(
                label,
                "canonical datetime wins over the conflicting legacy value",
                &departure_ledger()
                    .golden(&format!("{DIR}/x-fern-type-extension/fern-expected"), &[])
                    .unwrap(),
                &case.join("fern-expected"),
                &generated,
            );
            assert!(failures.is_empty(), "{}", failures.join("\n\n"));
        } else {
            assert_eq!(model.matches("typing.Optional[str]").count(), 2, "{label}");
        }
    }
    let path = out.join("src/fern/types/scan.py");
    let model = std::fs::read_to_string(&path).unwrap();
    assert_eq!(model.matches("typing.Optional[dt.datetime]").count(), 2);
    assert!(model.contains("typing.Optional[typing.Literal[True]]"));
    std::fs::write(
        &path,
        model.replace("typing.Optional[dt.datetime]", "typing.Optional[str]"),
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path == "src/fern/types/scan.py"));
}

#[test]
fn remeasure_declared_enum_casing_preserves_digit_separators() {
    let (work, case, out) = generate("enum-member-digit-separator");
    let original: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(case.join("openapi.yml")).unwrap()).unwrap();
    for (label, canonical, member, visitor) in [
        (
            "canonical-casing",
            serde_json::json!({
                "grow-2-7-leaf": {"casing": {"snake": "canonical_leaf", "screamingSnake": "CANONICAL_LEAF"}}
            }),
            "CANONICAL_LEAF",
            "canonical_leaf",
        ),
        (
            "canonical-name-without-casing",
            serde_json::json!({"grow-2-7-leaf": {"name": "CANONICAL_MEMBER"}}),
            "CANONICAL_MEMBER",
            "canonical_member",
        ),
        (
            "canonical-empty-map",
            serde_json::json!({}),
            "GROW27LEAF",
            "grow27leaf",
        ),
    ] {
        let mut document = original.clone();
        document
            .pointer_mut("/components/schemas/DeliveryModel")
            .unwrap()
            .as_object_mut()
            .unwrap()
            .insert("x-crozier-enum".into(), canonical);
        let generated = generate_control(work.path(), label, &document);
        let model =
            std::fs::read_to_string(generated.join("src/fern/types/delivery_model.py")).unwrap();
        assert!(
            model.contains(&format!("{member} = \"grow-2-7-leaf\"")),
            "{label}: {member}"
        );
        assert!(
            model.contains(&format!("{visitor}: typing.Callable")),
            "{label}: {visitor}"
        );
        assert!(
            !model.contains("GROW2_7_LEAF"),
            "{label}: legacy casing leaked"
        );
    }
    let path = out.join("src/fern/types/delivery_model.py");
    let model = std::fs::read_to_string(&path).unwrap();
    assert!(model.contains("GROW2_7_LEAF = \"grow-2-7-leaf\""));
    assert!(model.contains("grow2_7_leaf: typing.Callable"));
    assert!(model.contains("AGENT412LARGE = \"agent-4-12-large\""));
    std::fs::write(&path, model.replace("GROW2_7_LEAF", "GROW27LEAF")).unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path.ends_with("delivery_model.py")));
}

#[test]
fn remeasure_typed_single_reference_allof_is_an_alias_without_own_fields() {
    let (_work, case, out) = generate("typed-single-ref-allof-alias");
    for name in ["plain_ack", "closed_ack", "example_ack"] {
        let model =
            std::fs::read_to_string(out.join("src/fern/types").join(format!("{name}.py"))).unwrap();
        assert!(model.contains(" = Payload"), "{name}");
        assert!(!model.contains("class "), "{name}");
    }
    assert!(
        std::fs::read_to_string(out.join("src/fern/receipts/types/grouped_ack.py"))
            .unwrap()
            .contains("GroupedAck = Payload")
    );
    assert!(
        std::fs::read_to_string(out.join("src/fern/types/own_fields_ack.py"))
            .unwrap()
            .contains("class OwnFieldsAck(Payload):")
    );
    std::fs::write(
        out.join("src/fern/types/plain_ack.py"),
        "from .payload import Payload\n\nclass PlainAck(Payload):\n    pass\n",
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path.ends_with("plain_ack.py")));
}

#[test]
fn remeasure_unused_multipart_fields_do_not_refuse_a_selected_bytes_body() {
    let (work, case, out) = generate("ignored-multipart-query-collision");
    let raw = std::fs::read_to_string(out.join("src/fern/raw_client.py")).unwrap();
    assert!(raw.contains("content=request,"));
    assert!(!raw.contains("files="));
    let original = std::fs::read_to_string(case.join("openapi.yml")).unwrap();
    let mut document: serde_json::Value = serde_json::from_str(&original).unwrap();
    document
        .pointer_mut("/paths/~1scans/post/requestBody/content")
        .unwrap()
        .as_object_mut()
        .unwrap()
        .remove("application/octet-stream");
    let control = work.path().join("openapi.json");
    std::fs::write(&control, serde_json::to_string_pretty(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let refused = work
            .path()
            .join(if strict { "refused-strict" } else { "refused" });
        let mut command = probe_command(&control, &refused);
        if strict {
            command.arg("--fern-strict");
        }
        command
            .assert()
            .failure()
            .stderr(predicates::str::contains("request-property-name-collision"));
        assert!(!refused.join("src/fern/client.py").exists());
    }
    std::fs::write(&control, original).unwrap();
    let recovered = work.path().join("recovered");
    probe_command(&control, &recovered).assert().success();
    let comparison =
        crozier::parity::compare_trees(&case.join("fern-expected"), &recovered, None, true)
            .unwrap();
    assert!(comparison.differences.is_empty(), "{comparison:#?}");
}
