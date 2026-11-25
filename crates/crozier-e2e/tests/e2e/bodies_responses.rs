//! Request-body, form/multipart and response causes, each measured on a
//! from-scratch document against the certified pair
//! (`docs/fern-measurements/bodies-responses/<case>/`, registered in
//! `docs/fern-measurements/cases.tsv`).
//!
//! crozier's complete SDK for each document must equal the certified pair's
//! committed tree, and the line each repair decides must fail that comparison
//! when written the way crozier wrote it before the repair. The header/body
//! argument-name collision is driven on the wire too, by
//! `tests/runtime/test_header_body_collision.py`.

use std::path::{Path, PathBuf};

use super::{copy_dir, departure_ledger, golden_tree_failures, probe_command, repo_root};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/bodies-responses";

fn case_dir(case: &str) -> PathBuf {
    repo_root().join(DIR).join(case)
}

/// crozier's SDK at `out` against `golden` (relative to the repository), apart
/// from the departures the ledger records for it.
fn failures(case: &str, golden: &str, out: &Path) -> Vec<String> {
    let ledger = departure_ledger()
        .golden(golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        case,
        &case_dir(case).join("openapi.yml").display().to_string(),
        &ledger,
        &repo_root().join(golden),
        out,
    )
}

/// Generate `case`'s SDK and hold it whole to the certified pair's tree.
fn matched(case: &str) -> (tempfile::TempDir, PathBuf) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&case_dir(case).join("openapi.yml"), &out)
        .assert()
        .success();
    let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), &out);
    assert!(
        unexplained.is_empty(),
        "{case}: {}",
        unexplained.join("\n\n")
    );
    (temp, out)
}

fn read(path: &Path) -> String {
    std::fs::read_to_string(path).unwrap_or_else(|error| panic!("{}: {error}", path.display()))
}

/// `file` spells `fern` in both trees, and written as crozier wrote it before
/// the repair (`before`), the comparison names `file`.
fn decides(case: &str, out: &Path, file: &str, fern: &str, before: &str) {
    for tree in [case_dir(case).join("fern-expected"), out.to_path_buf()] {
        let text = read(&tree.join(file));
        assert!(
            text.contains(fern),
            "{}: no {fern:?}",
            tree.join(file).display()
        );
    }
    let generated = out.join(file);
    let text = read(&generated);
    std::fs::write(&generated, text.replacen(fern, before, 1)).expect("rewrite the file");
    let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{case}: {file} written as {before:?} must fail the comparison: {unexplained:?}"
    );
    std::fs::write(&generated, text).expect("restore the file");
}

/// crozier writes no `file`, and written back with `contents`, the model it
/// used to declare fails the comparison.
fn declares_none(case: &str, out: &Path, file: &str, contents: &str) {
    let path = out.join(file);
    assert!(!path.exists(), "{case}: crozier still writes {file}");
    std::fs::create_dir_all(path.parent().expect("a parent")).expect("the directory");
    std::fs::write(&path, contents).expect("write the file back");
    let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{case}: a written-back {file} must fail the comparison: {unexplained:?}"
    );
    std::fs::remove_file(&path).expect("remove it again");
}

const JSON_HEADER: &str = "\"content-type\": \"application/json\"";

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares.
/// #888: a body naming a one-member `oneOf` or `anyOf` around an object
/// component spreads the member's fields into keyword arguments.
#[test]
fn single_member_union_body_spreads_the_member_fields() {
    let (_temp, out) = matched("single-member-union-body");
    let raw = "src/fern/firings/raw_client.py";
    decides(
        "single-member-union-body",
        &out,
        raw,
        "        region: str,\n",
        "        request: CloneFiringBody,\n",
    );
    decides(
        "single-member-union-body",
        &out,
        raw,
        "        shelf: str,\n",
        "        request: CopyFiringBody,\n",
    );
}

/// #890: an inline union body keeps the JSON content type only when its schema
/// describes (or titles) itself, discriminated or not, under either enum mode.
#[test]
fn inline_union_body_keeps_its_content_type_only_when_described() {
    let case = "inline-union-body-content-type";
    let (_temp, out) = matched(case);
    let raw = "src/fern/verifications/raw_client.py";
    let text = read(&out.join(raw));
    assert_eq!(
        text.matches(JSON_HEADER).count(),
        2,
        "send_notice alone, sync and async"
    );
    decides(
        case,
        &out,
        raw,
        "annotation=RecheckVerificationRequest, direction=\"write\"\n            ),\n            request_options",
        "annotation=RecheckVerificationRequest, direction=\"write\"\n            ),\n            headers={\n                \"content-type\": \"application/json\",\n            },\n            request_options",
    );
    literals_match(case);
}

/// The `literals` SDK against the case's base tree with its `expected-literals`
/// overlay applied.
fn literals_match(case: &str) {
    let dir = case_dir(case);
    let overlay = dir.join("expected-literals/fern-expected");
    let manifest: serde_json::Value =
        serde_json::from_str(&read(&overlay.join(".crozier-overlay.json")))
            .expect("overlay manifest");
    assert_eq!(manifest["enum_type"], "literals");
    let removed: Vec<String> = manifest["removed"]
        .as_array()
        .expect("removed overlay paths")
        .iter()
        .map(|value| value.as_str().expect("a path").to_string())
        .collect();
    let work = tempfile::tempdir().expect("literals work");
    let reference = work.path().join("reference-literals");
    for source in [dir.join("fern-expected"), overlay.clone()] {
        for relative in crozier::parity::walk_files(&source).expect("walk") {
            if relative == ".crozier-overlay.json"
                || source != overlay && removed.contains(&relative)
            {
                continue;
            }
            let destination = reference.join(&relative);
            std::fs::create_dir_all(destination.parent().expect("a parent")).expect("dir");
            std::fs::copy(source.join(&relative), destination).expect("copy");
        }
    }
    let literals = work.path().join("sdk-literals");
    probe_command(&dir.join("openapi.yml"), &literals)
        .args(["--enum-type", "literals"])
        .assert()
        .success();
    let own = crozier::parity::walk_files(&overlay)
        .expect("walk")
        .into_iter()
        .filter(|path| path != ".crozier-overlay.json")
        .collect();
    let inherited = departure_ledger()
        .golden(&format!("{DIR}/{case}/fern-expected"), &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let ledger = departure_ledger()
        .golden(
            &format!("{DIR}/{case}/expected-literals/fern-expected"),
            &[],
        )
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
        .inherit(inherited, own, &removed);
    let unexplained = golden_tree_failures(
        &format!("{case} (literals)"),
        &dir.join("openapi.yml").display().to_string(),
        &ledger,
        &reference,
        &literals,
    );
    assert!(unexplained.is_empty(), "{}", unexplained.join("\n\n"));
}

/// #892: a titled component passed whole as one `request` and posted by two
/// operations keeps the JSON content type on its parameterless operation.
#[test]
fn titled_shared_single_body_keeps_its_content_type() {
    let case = "titled-shared-single-body";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/account/raw_client.py",
        "            \"account\",\n            method=\"PUT\",\n            json=request,\n            headers={\n                \"content-type\": \"application/json\",\n            },\n",
        "            \"account\",\n            method=\"PUT\",\n            json=request,\n",
    );
}

/// #903: a required nullable free-form body is optional, and an inline `oneOf`
/// body is required even where the Request Body Object says `required: false`.
#[test]
fn request_body_requiredness_follows_the_measured_shapes() {
    let case = "body-requiredness-shapes";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/functions/raw_client.py",
        "request: typing.Optional[typing.Dict[str, typing.Any]] = None,",
        "request: typing.Dict[str, typing.Any],",
    );
    decides(
        case,
        &out,
        "src/fern/drops/raw_client.py",
        "annotation=CreateDropRequest, direction=\"write\"",
        "annotation=typing.Optional[CreateDropRequest], direction=\"write\"",
    );
}

/// #913: an error whose first media declares no schema, or `{}`, is unknown
/// though a typed representation follows; a typed first media still decides.
#[test]
fn error_bodies_read_their_first_declared_media() {
    let case = "schemaless-error-media";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/errors/conflict_error.py",
        "body: typing.Any,",
        "body: ProblemDetail,",
    );
    decides(
        case,
        &out,
        "src/fern/errors/unprocessable_entity_error.py",
        "body: typing.Any,",
        "body: ProblemDetail,",
    );
    assert!(read(&out.join("src/fern/errors/bad_request_error.py")).contains("body: str,"));
}

/// #914: an inline error object named as a component model already is declares
/// nothing; the component's nested model stays.
#[test]
fn inline_error_models_leave_component_models_alone() {
    let case = "inline-error-component-name";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/types/conflict_error_body_data.py",
        "    message: str\n",
        "    current: Session\n",
    );
}

/// #915: a later inline error body replaces an earlier one's model, and the
/// models the earlier one nested that the later one does not stay declared.
#[test]
fn superseded_error_bodies_keep_their_nested_types() {
    let case = "superseded-error-types";
    let (_temp, out) = matched(case);
    for file in [
        "src/fern/types/bad_request_error_body_exception_error_list_item.py",
        "src/fern/types/forbidden_error_body_exception.py",
    ] {
        let path = out.join(file);
        let text = read(&path);
        std::fs::remove_file(&path).expect("drop the model");
        let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), &out);
        assert!(
            unexplained.iter().any(|failure| failure.contains(file)),
            "{case}: dropping {file} must fail the comparison: {unexplained:?}"
        );
        std::fs::write(&path, text).expect("restore the model");
    }
}

/// #916: two multipart-only components whose names collide on one class are
/// each inlined once, and neither keeps a model.
#[test]
fn multipart_only_body_collisions_declare_no_model() {
    let case = "multipart-only-body-collision";
    let (_temp, out) = matched(case);
    declares_none(
        case,
        &out,
        "src/fern/types/body_upload_file_files_post.py",
        "class BodyUploadFileFilesPost:\n    file: bytes\n",
    );
}

/// #917: a form body composed only of inline `allOf` members sends every
/// member's field, multipart and urlencoded alike.
#[test]
fn composed_form_bodies_send_every_field() {
    let case = "composed-form-body";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/account/raw_client.py",
        "            data={\n                \"reason\": reason,\n                \"everywhere\": everywhere,\n            },\n",
        "            data={},\n",
    );
    decides(
        case,
        &out,
        "src/fern/documents/raw_client.py",
        "            files={\n                \"file\": file,\n            },\n",
        "            files={},\n",
    );
}

/// #918: a part referencing a binary component, plain or nullable, is that
/// `bytes` alias and is sent as the part's value, not JSON-encoded.
#[test]
fn multipart_binary_references_are_sent_as_their_value() {
    let case = "multipart-binary-reference";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/uploads/raw_client.py",
        "                \"model\": model,\n                \"file\": file,\n",
        "                \"model\": model,\n                \"file\": json.dumps(jsonable_encoder(file)) if file is not OMIT else OMIT,\n",
    );
}

/// The same document with the plain part required: its transport matches, and
/// every worked call passes the required part as the `bytes` its `FormFile`
/// annotation takes (`file=b"file"`), in `README.md`, `reference.md` and the
/// client docstrings alike, where the certified pair passes the `str`
/// `file="file"` (the `binary-form-part-example` departure, which the ledger
/// pins at each of those lines). The untouched tree is held whole.
#[test]
fn required_binary_reference_part_is_exampled_as_bytes() {
    let case = "multipart-binary-required-part";
    let (_temp, out) = matched(case);
    for (file, calls) in [
        ("README.md", 2),
        ("reference.md", 1),
        ("src/fern/uploads/client.py", 2),
    ] {
        let text = read(&out.join(file));
        assert_eq!(
            text.matches("file=b\"file\",\n").count(),
            calls,
            "{file}: {text}"
        );
        assert!(
            !text.contains("file=\"file\"") && !text.contains("file=\"string\""),
            "{file} passes a str for the bytes part: {text}"
        );
    }
    // The departure admits only the bytes spelling of Fern's own sample: the
    // value crozier wrote before (`"string"`, which the annotation rejects)
    // fails the comparison.
    let reference = out.join("reference.md");
    let text = read(&reference);
    std::fs::write(
        &reference,
        text.replace("file=b\"file\",", "file=\"string\","),
    )
    .expect("rewrite");
    let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), &out);
    assert!(
        unexplained
            .iter()
            .any(|failure| failure.contains("reference.md")),
        "{unexplained:?}"
    );
}

/// #926: a body property sharing its argument name with a header is renamed in
/// the signature and sent from that renamed argument. Where the body is inlined
/// the certified pair does the same; where it is a shared component, the pair
/// sends the header's variable instead, the catalogued
/// `body-query-parameter-value` departure, which the ledger pins at that line.
#[test]
fn header_and_body_sharing_a_name_keep_their_own_arguments() {
    let case = "header-body-collision";
    let (_temp, out) = matched(case);
    let raw = "src/fern/actions/raw_client.py";
    decides(
        case,
        &out,
        raw,
        "\"kilnToken\": run_action_request_kiln_token,",
        "\"kilnToken\": kiln_token,",
    );
    let fern = read(&case_dir(case).join("fern-expected").join(raw));
    let generated = read(&out.join(raw));
    let renamed = "                \"idempotency_key\": action_batch_request_idempotency_key,\n";
    let header = "                \"idempotency_key\": idempotency_key,\n";
    // `run_action_batch` (sync and async) sends the renamed body argument where
    // the certified pair sends the header's; `preview_action_batch`, with no
    // header, sends `idempotency_key` in both trees.
    assert_eq!(generated.matches(renamed).count(), 2, "{generated}");
    assert_eq!(generated.matches(header).count(), 2, "{generated}");
    assert_eq!(fern.matches(header).count(), 4, "{fern}");
    std::fs::write(
        out.join(raw),
        generated.replacen(
            renamed,
            "                \"idempotency_key\": actions,\n",
            1,
        ),
    )
    .expect("rewrite the client");
    let unexplained = failures(case, &format!("{DIR}/{case}/fern-expected"), &out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(raw)),
        "any other value must fail the comparison: {unexplained:?}"
    );
}

/// #926's departure covers the header's variable only where the request maps
/// that header from it. With the header block rewritten identically in the
/// certified tree and in crozier's, mapping another variable or no longer
/// sending headers at all, the header lines still agree, so the comparison
/// fails only because the departure no longer explains the body line.
#[test]
fn header_body_departure_needs_the_header_to_map_that_variable() {
    let case = "header-body-collision";
    let (temp, out) = matched(case);
    let raw = "src/fern/actions/raw_client.py";
    let golden = format!("{DIR}/{case}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let header = "                \"Idempotency-Key\": str(idempotency_key) if idempotency_key is not None else None,\n";
    let block = format!(
        "            headers={{\n                \"content-type\": \"application/json\",\n{header}"
    );
    let unmapped = header.replace("idempotency_key", "request_options");
    let absent = block.replacen("headers={", "params={", 1);
    for (label, from, to) in [
        ("unchanged", header, header.to_owned()),
        ("another variable", header, unmapped),
        ("no headers", block.as_str(), absent),
    ] {
        let reference = temp
            .path()
            .join(format!("reference-{}", label.replace(' ', "-")));
        copy_dir(&repo_root().join(&golden), &reference);
        let sdk = temp.path().join(format!("sdk-{}", label.replace(' ', "-")));
        copy_dir(&out, &sdk);
        for tree in [&reference, &sdk] {
            let text = read(&tree.join(raw));
            assert_eq!(text.matches(from).count(), 2, "{label}: {}", tree.display());
            std::fs::write(tree.join(raw), text.replace(from, &to)).expect("rewrite the client");
        }
        let unexplained = golden_tree_failures(
            case,
            &case_dir(case).join("openapi.yml").display().to_string(),
            &ledger,
            &reference,
            &sdk,
        );
        if label == "unchanged" {
            assert!(unexplained.is_empty(), "{label}: {unexplained:?}");
        } else {
            assert!(
                unexplained.iter().any(|failure| failure.contains(raw)),
                "{label}: the departure must not explain the body line: {unexplained:?}"
            );
        }
    }
}

/// #938: a nullable scalar alias body is sent raw, and a map of a union alias
/// is written through the converter.
#[test]
fn request_conversion_follows_the_body_classification() {
    let case = "request-convert-decision";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/forms/raw_client.py",
        "            method=\"PUT\",\n            json=request,\n",
        "            method=\"PUT\",\n            json=convert_and_respect_annotation_metadata(\n                object_=request, annotation=typing.Optional[ValidateOutput], direction=\"write\"\n            ),\n",
    );
    decides(
        case,
        &out,
        "src/fern/datasources/raw_client.py",
        "json=convert_and_respect_annotation_metadata(\n                object_=request, annotation=DatasourceQuery, direction=\"write\"\n            ),",
        "json=request,",
    );
}

/// #939: a success response naming a component declared `typing.Any` guards
/// the empty body.
#[test]
fn unknown_success_alias_keeps_the_empty_body_guard() {
    let case = "unknown-response-guard";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/transactions/raw_client.py",
        "            if _response is None or not _response.text.strip():\n                return HttpResponse(response=_response, data=None)\n",
        "",
    );
}

/// #950: a body referencing a schema outside `components` that does not exist
/// is `typing.Any`, and the operation keeps its method.
#[test]
fn unresolved_non_component_body_reference_is_any() {
    let case = "non-component-ref-body";
    let (_temp, out) = matched(case);
    decides(
        case,
        &out,
        "src/fern/feature_flags/raw_client.py",
        "self, *, request: typing.Any, request_options",
        "self, *, request: FeatureFlag, request_options",
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
