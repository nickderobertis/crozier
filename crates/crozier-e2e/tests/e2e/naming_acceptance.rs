//! The naming, import and document-acceptance tickets of the naming-acceptance
//! node (#536, #919, #920, #921, #922, #923, #924, #941, #942, #943, #944,
//! #946, #948, #955, #956) and #981, each settled against a from-scratch document under
//! [`DIR`] and the certified pair's complete tree for it (Fern CLI 5.216.0,
//! fern-python-sdk 5.42.0), in both enum modes.
//!
//! Every measurement runs the real binary and compares its SDK with the
//! certified tree file for file. A repaired rule is shown to fail the
//! comparison once the bytes crozier wrote before the repair are written back;
//! an accepted document is one crozier refused before, so its generating at
//! all is the regression.

use std::collections::BTreeSet;
use std::path::{Path, PathBuf};

use assert_cmd::Command;

use super::{
    crozier, departure_ledger, golden_tree_failures, golden_tree_failures_in, probe_command,
    refusal_run, refused_failures, repo_root, walk_files, FERN_REFUSALS_DIR,
};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/naming-acceptance";

/// A case's literals overlay, laid over its `fern-expected/`.
pub(crate) const LITERALS: &str = "expected-literals/fern-expected";

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
const MANIFEST: &str = ".crozier-overlay.json";

/// Each repaired rule's case and its characteristic bytes in the certified
/// pair's tree: `(ticket, case, file, certified bytes, what crozier wrote before)`.
const REPAIRS: &[(&str, &str, &str, &str, &str)] = &[
    (
        "#536",
        "model-api-field-names",
        "src/fern/types/record.py",
        "    model_dump_: typing_extensions.Annotated[",
        "    model_dump: typing_extensions.Annotated[",
    ),
    (
        "#923",
        "model-api-field-names",
        "src/fern/records/raw_client.py",
        "\"kwargs\": kwargs_,",
        "\"kwargs\": kwargs,",
    ),
    (
        "#919",
        "request-local-union-payloads",
        "src/fern/column_operations/types/__init__.py",
        "    from .update_data_lite_input_input_options_csv import UpdateDataLiteInputInputOptionsCsv\n",
        "",
    ),
    (
        "#920",
        "root-import-order",
        "src/fern/__init__.py",
        "    from .agent_runtime import CreateRuntimeProfileRequestMode\n    from .client import AsyncFernApi, FernApi\n",
        "    from .client import AsyncFernApi, FernApi\n    from .agent_runtime import CreateRuntimeProfileRequestMode\n",
    ),
    (
        "#921",
        "head-shadowed-get-imports",
        "src/fern/folio_api/client.py",
        "from ..types.page import Page\n",
        "from ..types.get_site_response import GetSiteResponse\nfrom ..types.page import Page\n",
    ),
    (
        "#922",
        "recursive-alias-dependents",
        "src/fern/types/fit_summary.py",
        "\n\nupdate_forward_refs(FitSummary)\n",
        "\n",
    ),
    (
        "#924 (a dotted id led by its tag's words)",
        "dotted-operation-tag-names",
        "src/fern/agent_host/client.py",
        "    def pairing_create(",
        "    def agent_host_pairing_create(",
    ),
    (
        "#924 (a punctuated tag's module)",
        "dotted-operation-tag-names",
        "src/fern/client.py",
        "    from .agent_surfaces_me.client import AgentSurfacesMeClient, AsyncAgentSurfacesMeClient\n",
        "    from .agent_surfaces__me_.client import AgentSurfacesMeClient, AsyncAgentSurfacesMeClient\n",
    ),
    (
        "#942",
        "relative-response-ref",
        "src/fern/errors/not_found_error.py",
        "body: Problem",
        "body: typing.Any",
    ),
    (
        "#946",
        "nullable-enum-headers",
        "src/fern/simple_encoding/raw_client.py",
        "wrapped_nullable_enum.value if",
        "str(wrapped_nullable_enum) if",
    ),
    (
        "#948",
        "xml-helper-import",
        "src/fern/types/alert_atom_entry.py",
        "    XmlNode,\n    build_xml_model,",
        "    XmlNode,\n    append_xml_child,\n    build_xml_model,",
    ),
];

/// Each accepted document's case, the refusal (or parse failure) crozier
/// answered it with before, and the certified bytes its SDK now carries:
/// `(ticket, case, the old refusal's class, file, certified bytes)`.
const ACCEPTED: &[(&str, &str, &str, &str, &str)] = &[
    (
        "#941",
        "boolean-component-schemas",
        "invalid OpenAPI document",
        "src/fern/types/never.py",
        "Never = typing.Any",
    ),
    (
        "#955",
        "discriminator-only-parent",
        "object-extends-non-object",
        "src/fern/types/instance_provider.py",
        "typing.Union[InstanceProvider_BarcodeScan, InstanceProvider_Manual], pydantic.Field(discriminator=\"type\")",
    ),
    (
        "#956",
        "ignored-accept-header-enum",
        "enum-name-unsuitable",
        "src/fern/config/raw_client.py",
        "\"accept\": \"*/*\",",
    ),
    (
        "#943 (not reproducing: a query and a path parameter both named `type`)",
        "path-query-same-name",
        "",
        "src/fern/client.py",
        "type_path_param: str,",
    ),
    (
        "#981 (ruff refused the duplicate `request_options` parameter)",
        "request-options-body-property",
        "Duplicate parameter",
        "src/fern/dispatches/raw_client.py",
        "        request_options: str,\n        kwargs_: typing.Optional[str] = OMIT,\n        self_: typing.Optional[str] = OMIT,\n        _request_options: typing.Optional[RequestOptions] = None,\n",
    ),
    (
        "#944 (the control: one component)",
        "normalized-component-identity-control",
        "",
        "src/fern/types/kiln_glaze_coat.py",
        "class KilnGlazeCoat(UniversalBaseModel):\n    left: str",
    ),
    (
        "#985 (a property two `allOf` parents declare, one through its own `$ref`)",
        "repeated-inherited-properties",
        "object-property-name-collision",
        "src/fern/types/oligo_create.py",
        "    folder_id: typing_extensions.Annotated[\n        typing.Optional[str],\n        FieldMetadata(alias=\"folderId\"),\n        pydantic.Field(alias=\"folderId\", description=\"ID of the folder containing the oligo.\"),\n    ] = None",
    ),
    (
        "#944 (two components spelling one class, reached from a request)",
        "normalized-component-identity",
        "",
        "src/fern/types/kiln_glaze_coat.py",
        "class KilnGlazeCoat(UniversalBaseModel):\n    right: int",
    ),
    (
        "#983 (a union tagged by an aliased wire key; its runtime parse is the sdk_env_ journey)",
        "aliased-union-discriminator",
        "",
        "src/fern/types/query_response.py",
        "typing.Union[QueryResponse_Table, QueryResponse_Graph], pydantic.Field(discriminator=\"schema_\")",
    ),
];

fn spec(case: &str) -> PathBuf {
    repo_root().join(DIR).join(case).join("openapi.yml")
}

fn golden(case: &str) -> String {
    format!("{DIR}/{case}/fern-expected")
}

fn generate(case: &str, mode: &str, out: &Path) {
    probe_command(&spec(case), out)
        .args(["--enum-type", mode])
        .assert()
        .success();
}

/// crozier's python-enums SDK for `case` against its certified-pair tree.
fn enum_failures(case: &str, out: &Path) -> Vec<String> {
    let golden = golden(case);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        &format!("{case} (python-enums)"),
        &spec(case).display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

/// [`enum_failures`] over a tree a test tampered with on purpose: every
/// difference no departure explains still fails, but no departure it applies is
/// held to the golden's ledger rows, and as a
/// [`super::departures_ledger::perturbed`] comparison it records nothing under
/// `just departures-ledger`, where a tampered tree's shifted lines would
/// otherwise become rows the untouched tree never applies.
fn tampered_enum_failures(case: &str, out: &Path) -> Vec<String> {
    let golden = golden(case);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    super::departures_ledger::perturbed(|| {
        golden_tree_failures_in(
            &format!("{case} (python-enums, tampered)"),
            &spec(case).display().to_string(),
            &ledger,
            &repo_root().join(&golden),
            out,
            &|_| false,
        )
    })
}

/// The removed base files a literals overlay's manifest names.
fn removed(overlay: &Path) -> Vec<String> {
    let manifest: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(overlay.join(MANIFEST)).expect("the overlay manifest"),
    )
    .expect("the overlay manifest is JSON");
    assert_eq!(manifest["enum_type"], "literals", "{}", overlay.display());
    manifest["removed"]
        .as_array()
        .expect("a removed list")
        .iter()
        .map(|rel| rel.as_str().expect("a path").to_string())
        .collect()
}

/// The certified pair's literals tree for `case`: the base less the files the
/// overlay removes, with the overlay's own files laid over it.
fn literals_tree(case: &str) -> (tempfile::TempDir, BTreeSet<String>, Vec<String>) {
    let base = repo_root().join(golden(case));
    let overlay = repo_root().join(format!("{DIR}/{case}/{LITERALS}"));
    let removed = removed(&overlay);
    let tree = tempfile::tempdir().expect("literals tree tempdir");
    let copy = |from: &Path, rel: &str| {
        let to = tree.path().join(rel);
        std::fs::create_dir_all(to.parent().expect("a file has a parent")).expect("mkdir");
        std::fs::copy(from.join(rel), &to).expect("copy a Fern file");
    };
    for rel in walk_files(&base) {
        if !removed.contains(&rel) {
            copy(&base, &rel);
        }
    }
    let own: BTreeSet<String> = walk_files(&overlay)
        .into_iter()
        .filter(|rel| rel != MANIFEST)
        .collect();
    for rel in &own {
        copy(&overlay, rel);
    }
    (tree, own, removed)
}

/// crozier's literals SDK for `case` against the certified pair's literals
/// tree ([`literals_tree`]).
fn literals_failures(case: &str, out: &Path) -> Vec<String> {
    let overlay_golden = format!("{DIR}/{case}/{LITERALS}");
    let (tree, own, removed) = literals_tree(case);
    let inherited = departure_ledger()
        .golden(&golden(case), &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let ledger = departure_ledger()
        .golden(&overlay_golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
        .inherit(inherited, own, &removed);
    golden_tree_failures(
        &format!("{case} (literals)"),
        &spec(case).display().to_string(),
        &ledger,
        tree.path(),
        out,
    )
}

/// `case`'s SDK in both enum modes against the certified pair's trees, the
/// python-enums output left in `temp/sdk` for the caller to read.
fn both_modes_failures(case: &str, temp: &Path) -> Vec<String> {
    let out = temp.join("sdk");
    generate(case, "python-enums", &out);
    let mut failures = enum_failures(case, &out);
    let literals = temp.join("literals");
    generate(case, "literals", &literals);
    failures.extend(literals_failures(case, &literals));
    failures
}

fn read(path: &Path) -> String {
    std::fs::read_to_string(path).unwrap_or_else(|error| panic!("{}: {error}", path.display()))
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These journeys generate one small SDK per measurement in each enum mode, comparing each whole against its certified tree, on the crozier-e2e edge every other golden comparison shares; a narrower edge for generator-replay journeys is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Each repaired rule's measurement is the certified pair's tree file for file
/// in both enum modes, and the comparison fails once the rule's bytes are
/// written back the way crozier wrote them before the repair.
#[test]
fn naming_acceptance_repairs_match_the_certified_pair() {
    let mut failures = Vec::new();
    for (ticket, case, file, certified, before) in REPAIRS {
        let temp = tempfile::tempdir().expect("output tempdir");
        failures.extend(both_modes_failures(case, temp.path()));
        let path = temp.path().join("sdk").join(file);
        let written = read(&path);
        assert!(
            written.contains(certified),
            "{ticket} {case}: {file} lacks the certified bytes {certified:?}"
        );
        std::fs::write(&path, written.replacen(certified, before, 1)).expect("tamper");
        let tampered = enum_failures(case, &temp.path().join("sdk"));
        assert!(
            tampered.iter().any(|failure| failure.contains(file)),
            "{ticket} {case}: writing {before:?} back into {file} must fail the comparison: {tampered:?}"
        );
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// Each accepted document generates in both enum modes, with and without
/// `--fern-strict`, and is the certified pair's tree file for file, carrying
/// the bytes that decide it; none of them prints the refusal crozier answered
/// it with before.
#[test]
fn naming_acceptance_documents_generate_as_the_certified_pair_does() {
    let mut failures = Vec::new();
    for (ticket, case, refusal, file, certified) in ACCEPTED {
        let temp = tempfile::tempdir().expect("output tempdir");
        failures.extend(both_modes_failures(case, temp.path()));
        let written = read(&temp.path().join("sdk").join(file));
        assert!(
            written.contains(certified),
            "{ticket} {case}: {file} lacks the certified bytes {certified:?}"
        );
        let strict = temp.path().join("strict");
        let run = probe_command(&spec(case), &strict)
            .arg("--fern-strict")
            .assert()
            .success();
        let stderr = String::from_utf8_lossy(&run.get_output().stderr).into_owned();
        assert!(
            refusal.is_empty() || !stderr.contains(refusal),
            "{ticket} {case}: {stderr}"
        );
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// #956's refusal shapes, measured at the certified pair under
/// `docs/fern-refusals/enum-name-unsuitable/`: an inline header enum Fern cannot
/// name a member of is still refused in both modes when it has no default,
/// while a string default makes it a constant header (`accept` and any other
/// name alike) that generates identically with and without `--fern-strict`.
#[test]
fn header_enum_defaults_decide_the_enum_name_refusal() {
    let class = repo_root()
        .join(FERN_REFUSALS_DIR)
        .join("enum-name-unsuitable");
    for strict in [false, true] {
        let run = refusal_run(
            &crozier,
            &class.join("header-enum-without-default-probe.yml"),
            strict,
        )
        .expect("the probe runs");
        let failures = refused_failures(
            "enum-name-unsuitable",
            &run,
            "parameter x-format enum value \"*/*\"",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    }
    for control in [
        "header-enum-string-default-control.yml",
        "accept-header-default-control.yml",
    ] {
        let normal = refusal_run(&crozier, &class.join(control), false).unwrap();
        let strict = refusal_run(&crozier, &class.join(control), true).unwrap();
        assert_eq!(normal.code, Some(0), "{control}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{control}: {}", strict.stderr);
        assert_eq!(normal.files, strict.files, "{control}");
    }
}

/// #940: a response example and an error example each invalid for their own
/// schema (`kind: 'wx:Point'` outside the enum, `title: 12345` for a string).
/// Fern refuses the document (its `fern-refusal.txt`), a limitation of valid
/// OpenAPI under manager ruling a0, so crozier generates it in both enum modes
/// with and without `--fern-strict`. Neither tool writes a response or error
/// example into any generated file, so no invalid value reaches the SDK: the
/// repair rule of `schema-rejected-declared-example` has nothing to repair here,
/// and this test fails the day one of these values is emitted unrepaired.
#[test]
fn invalid_response_examples_generate_and_reach_no_generated_file() {
    let case = "invalid-response-examples";
    let record = read(&repo_root().join(DIR).join(case).join("fern-refusal.txt"));
    assert!(
        record.contains("generate_exit: 1") && record.contains("fern_cli_version: 5.216.0"),
        "{record}"
    );
    for mode in ["python-enums", "literals"] {
        for strict in [false, true] {
            let temp = tempfile::tempdir().expect("output tempdir");
            let out = temp.path().join("sdk");
            let mut command = probe_command(&spec(case), &out);
            command.args(["--enum-type", mode]);
            if strict {
                command.arg("--fern-strict");
            }
            command.assert().success();
            for rel in walk_files(&out) {
                let text = std::fs::read_to_string(out.join(&rel)).unwrap_or_default();
                for value in ["wx:Point", "Grid point OKX-33-35", "12345"] {
                    assert!(
                        !text.contains(value),
                        "{mode} strict={strict}: {rel} writes the invalid example value {value:?}"
                    );
                }
            }
        }
    }
}

/// #944's colliding responses: Fern refuses this document (its `fern-refusal.txt`
/// records its example of `kiln/glaze-coat` failing against the merged class),
/// a limitation of valid OpenAPI crozier does not copy (manager ruling a3). In
/// both enum modes crozier gives each component its own class and types each
/// operation with its own component's.
#[test]
fn colliding_response_components_each_keep_their_own_class() {
    let case = "normalized-component-identity-responses";
    let record = read(&repo_root().join(DIR).join(case).join("fern-refusal.txt"));
    assert!(
        record.contains("generate_exit: 1") && record.contains("fern_cli_version: 5.216.0"),
        "{record}"
    );
    for mode in ["python-enums", "literals"] {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(case, mode, &out);
        let types = out.join("src/fern/types");
        assert!(read(&types.join("kiln_glaze_coat.py"))
            .contains("class KilnGlazeCoat(UniversalBaseModel):\n    right: int"));
        assert!(read(&types.join("kiln_glaze_coat2.py"))
            .contains("class KilnGlazeCoat2(UniversalBaseModel):\n    left: str"));
        let client = read(&out.join("src/fern/client.py"));
        for signature in [
            "def get_left(self, *, request_options: typing.Optional[RequestOptions] = None) -> KilnGlazeCoat2:",
            "def get_right(self, *, request_options: typing.Optional[RequestOptions] = None) -> KilnGlazeCoat:",
        ] {
            assert!(client.contains(signature), "{mode}: {signature}");
        }
    }
}

// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// The SDK-environment journeys `naming_acceptance_runtime.py` runs, each over
/// the case's SDK under every Pydantic major the generated `pyproject.toml`
/// admits.
const RUNTIME: &str = "crates/crozier-e2e/tests/e2e/naming_acceptance_runtime.py";
const PYDANTIC_MAJORS: [&str; 2] = ["1.10.26", "2.14.1"];

/// Run `journey` over `case`'s SDK (generated in `mode`) under each Pydantic
/// major, through `uv`'s pinned Python 3.11 environments.
fn runtime_journey(case: &str, mode: &str, journey: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(case, mode, &out);
    for pydantic in PYDANTIC_MAJORS {
        let mut command = Command::new("uv");
        command.args(["run", "--no-project", "--python", "3.11"]);
        for dependency in [
            format!("pydantic=={pydantic}"),
            "httpx==0.28.1".to_string(),
            "typing_extensions==4.16.0".to_string(),
        ] {
            command.args(["--with", &dependency]);
        }
        command
            .arg(repo_root().join(RUNTIME))
            .arg(journey)
            .arg(out.join("src"))
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .assert()
            .success();
    }
}

/// #944: through the generated client, under both Pydantic majors and both
/// enum modes, a request built from each colliding component's own fields
/// sends exactly those fields, and each operation's declared response parses
/// into its own component's class.
#[test]
#[ignore = "SDK Python-environment tier (builds Pydantic 1 and 2 environments from PyPI with uv); run via `just test-sdk-env`"]
fn sdk_env_colliding_components_send_and_parse_their_own_shapes() {
    for mode in ["python-enums", "literals"] {
        runtime_journey("normalized-component-identity", mode, "colliding-request");
        runtime_journey(
            "normalized-component-identity-responses",
            mode,
            "colliding-responses",
        );
        runtime_journey(
            "normalized-component-identity-control",
            mode,
            "colliding-control",
        );
    }
}

/// #981: through the generated client, under both Pydantic majors and both
/// enum modes, every module imports and the sync, async and both raw clients
/// send the caller's `request_options` body value while applying
/// `_request_options` as the SDK's options (its header reaches the server).
#[test]
#[ignore = "SDK Python-environment tier (builds Pydantic 1 and 2 environments from PyPI with uv); run via `just test-sdk-env`"]
fn sdk_env_request_options_body_property_sends_beside_the_sdk_options() {
    for mode in ["python-enums", "literals"] {
        runtime_journey(
            "request-options-body-property",
            mode,
            "request-options-body-property",
        );
    }
}

/// #922: every module of the recursive-alias measurement imports under both
/// Pydantic majors and `FitSummary`, which reaches the alias-only cycle through
/// `InferenceReport`, constructs a value holding a recursive JSON object.
///
/// The cycle itself is `JsonValueOutput`/`JsonObjectOutput`/`JsonArrayOutput`,
/// three aliases, which the certified pair's tree does not import:
/// `InferenceReport`'s `update_forward_refs` raises `RecursionError` under
/// Pydantic 2.14.1 and the process segfaults under 1.10.26. An unimportable SDK
/// is a Fern defect crozier does not keep, so crozier names the alias closing
/// the cycle (#539's `recursive-alias-named-type` departure) and the SDK imports.
#[test]
#[ignore = "SDK Python-environment tier (builds Pydantic 1 and 2 environments from PyPI with uv); run via `just test-sdk-env`"]
fn sdk_env_recursive_alias_dependents_import_and_construct() {
    runtime_journey(
        "recursive-alias-dependents",
        "python-enums",
        "recursive-alias-dependents",
    );
}

/// #983: a response of a discriminated union whose tag's wire key `schema`
/// is the aliased field `schema_` parses through the generated client into
/// its variant under both Pydantic majors and both enum modes. The certified
/// runtime dealiases the union's input, and Pydantic 1.10 then reports the
/// discriminator missing: crozier's `discriminated-union-v1-wire-keys`
/// departure keeps the wire keys there.
#[test]
#[ignore = "SDK Python-environment tier (builds Pydantic 1 and 2 environments from PyPI with uv); run via `just test-sdk-env`"]
fn sdk_env_aliased_discriminated_unions_parse_under_both_pydantic_majors() {
    for mode in ["python-enums", "literals"] {
        runtime_journey("aliased-union-discriminator", mode, "aliased-discriminator");
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These journeys generate one small SDK per measurement in each enum mode, comparing each whole against its certified tree, on the crozier-e2e edge every other golden comparison shares; a narrower edge for generator-replay journeys is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".

/// A document whose `404` is `./components.yml#/components/responses/<name>`,
/// beside the sibling `components` text, both written under `dir`.
fn sibling_response_document(dir: &Path, name: &str, components: &str) -> PathBuf {
    let spec = dir.join("openapi.yml");
    std::fs::write(
        &spec,
        format!(
            "openapi: 3.0.3\ninfo: {{title: Vendor Notes, version: 1.0.0}}\npaths:\n  /notes:\n    get:\n      operationId: getNote\n      responses:\n        '200': {{description: The note.}}\n        '404':\n          $ref: './components.yml#/components/responses/{name}'\n"
        ),
    )
    .expect("write the document");
    std::fs::write(dir.join("components.yml"), components).expect("write the sibling");
    spec
}

/// #942's resolution rule beyond the measured case: a sibling's response that
/// is itself a local pointer resolves inside that sibling, while a cycle, a
/// pointer the sibling does not hold and a target that is no Response Object
/// each fail with an actionable message and write nothing.
#[test]
fn sibling_response_references_resolve_from_their_file_or_fail_actionably() {
    const PROBLEM: &str = "  schemas:\n    Problem:\n      type: object\n      required: [title]\n      properties:\n        title: {type: string}\n";
    let temp = tempfile::tempdir().expect("tempdir");
    let chained = sibling_response_document(
        temp.path(),
        "NotFound",
        &format!("components:\n  responses:\n    NotFound:\n      $ref: '#/components/responses/Missing'\n    Missing:\n      description: Gone.\n      content:\n        application/json:\n          schema:\n            $ref: '#/components/schemas/Problem'\n{PROBLEM}"),
    );
    let out = temp.path().join("sdk");
    probe_command(&chained, &out).assert().success();
    let error = read(&out.join("src/fern/errors/not_found_error.py"));
    assert!(error.contains("body: Problem"), "{error}");

    for (name, components, message) in [
        (
            "NotFound",
            "components:\n  responses:\n    NotFound:\n      $ref: '#/components/responses/Missing'\n    Missing:\n      $ref: '#/components/responses/NotFound'\n",
            "the response references form a cycle",
        ),
        (
            "Absent",
            "components:\n  responses:\n    NotFound:\n      description: Gone.\n",
            "the referenced document has no response at that pointer",
        ),
        (
            "NotFound",
            "components:\n  responses:\n    NotFound: [Gone]\n",
            "not a response",
        ),
    ] {
        let case = tempfile::tempdir().expect("tempdir");
        let spec = sibling_response_document(case.path(), name, components);
        let out = case.path().join("sdk");
        let run = probe_command(&spec, &out).assert().failure();
        let stderr = String::from_utf8_lossy(&run.get_output().stderr).into_owned();
        assert!(stderr.contains(message), "{name}: {stderr}");
        assert!(!out.exists(), "{name}: a refused document writes no SDK");
    }
}

/// #944's naming beyond one pair: three components spelling one class, beside
/// a component already named like the first ordinal, each keep a class of
/// their own; the last declaration keeps the shared class, and the earlier ones
/// take their own path's class with the first ordinal no other component's
/// class spells.
#[test]
fn colliding_components_take_the_first_free_ordinal_of_their_own_path() {
    let temp = tempfile::tempdir().expect("tempdir");
    let spec = temp.path().join("openapi.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.3\ninfo: {title: Kilns, version: 1.0.0}\npaths:\n  /kilns:\n    post:\n      operationId: createKilns\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              properties:\n                first: {$ref: '#/components/schemas/kiln/glaze-coat'}\n                second: {$ref: '#/components/schemas/kiln-glaze/coat'}\n                third: {$ref: '#/components/schemas/kiln-glaze-coat'}\n                taken: {$ref: '#/components/schemas/KilnGlazeCoat2'}\n      responses:\n        '204': {description: Created.}\ncomponents:\n  schemas:\n    KilnGlazeCoat2: {type: object, properties: {taken: {type: boolean}}}\n    kiln/glaze-coat: {type: object, properties: {first: {type: string}}}\n    kiln-glaze/coat: {type: object, properties: {second: {type: integer}}}\n    kiln-glaze-coat: {type: object, properties: {third: {type: number}}}\n",
    )
    .expect("write the document");
    let out = temp.path().join("sdk");
    probe_command(&spec, &out).assert().success();
    let client = read(&out.join("src/fern/client.py"));
    for (field, class) in [
        ("first", "KilnGlazeCoat3"),
        ("second", "KilnGlazeCoat4"),
        ("third", "KilnGlazeCoat"),
        ("taken", "KilnGlazeCoat2"),
    ] {
        assert!(
            client.contains(&format!(
                "        {field}: typing.Optional[{class}] = OMIT,"
            )),
            "{field} is typed {class}: {client}"
        );
    }
    for (module, field) in [
        ("kiln_glaze_coat", "third"),
        ("kiln_glaze_coat2", "taken"),
        ("kiln_glaze_coat3", "first"),
        ("kiln_glaze_coat4", "second"),
    ] {
        let text = read(&out.join(format!("src/fern/types/{module}.py")));
        assert!(text.contains(&format!("    {field}: ")), "{module}: {text}");
    }
}

/// The `colliding-component-own-class` rule takes exactly the renamed class's
/// own lines: once the #944 measurement matches, an unrelated change on a line
/// naming `KilnGlazeCoat2`, an added line naming no renamed class, and a
/// crozier-only module that is no renamed class's each remain a difference.
#[test]
fn the_colliding_component_departure_explains_only_the_renamed_class() {
    let case = "normalized-component-identity";
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(case, "python-enums", &out);
    assert!(enum_failures(case, &out).is_empty());
    let client = out.join("src/fern/client.py");
    let text = read(&client);
    let renamed = "        left: typing.Optional[KilnGlazeCoat2] = OMIT,\n";
    assert!(text.contains(renamed), "{text}");
    for (what, edit) in [
        (
            "an unrelated change on a renamed line",
            text.replacen(
                renamed,
                "        left: typing.Optional[KilnGlazeCoat2] = None,\n",
                1,
            ),
        ),
        (
            "an added line naming no renamed class",
            text.replacen(
                renamed,
                &format!("{renamed}        glaze: str = OMIT,\n"),
                1,
            ),
        ),
    ] {
        std::fs::write(&client, &edit).expect("tamper");
        let failures = tampered_enum_failures(case, &out);
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains("src/fern/client.py")),
            "{what} must fail the comparison: {failures:?}"
        );
    }
    std::fs::write(&client, &text).expect("restore");
    let extra = out.join("src/fern/types/kiln_glaze_coat9.py");
    std::fs::write(&extra, "KilnGlazeCoat9 = str\n").expect("an extra module");
    let failures = tampered_enum_failures(case, &out);
    assert!(
        failures
            .iter()
            .any(|failure| failure.contains("kiln_glaze_coat9.py")),
        "a module no renamed class owns must fail the comparison: {failures:?}"
    );
}

/// #992: a run of one-letter words in a component name is one class word, as
/// the certified pair cases it (`a/b-c` is `Abc`, `p-q-r` `Pqr`, `m_n` `Mn`,
/// `k/l-mn` `KlMn`), at its declaration and at every annotation naming it,
/// while a lone one-letter word beside longer ones keeps its capital (`EFgH`).
#[test]
fn single_letter_component_words_use_the_certified_casing() {
    let case = "single-letter-component-words";
    let temp = tempfile::tempdir().expect("output tempdir");
    let mut failures = both_modes_failures(case, temp.path());
    let sdk = temp.path().join("sdk");
    for (file, certified) in [
        ("src/fern/types/abc.py", "class Abc(UniversalBaseModel):"),
        ("src/fern/types/kl_mn.py", "class KlMn(UniversalBaseModel):"),
        ("src/fern/types/uvw.py", "class Uvw(enum.StrEnum):"),
        (
            "src/fern/types/roster.py",
            "    first: typing.Optional[Abc] = None\n    second: typing.Optional[Pqr] = None\n    \
             third: typing.Optional[Mn] = None\n    fourth: typing.Optional[AbCd] = None\n    \
             fifth: typing.Optional[EFgH] = None\n    sixth: typing.Optional[KlMn] = None\n    \
             lamp: typing.Optional[Uvw] = None\n",
        ),
        (
            "src/fern/client.py",
            "    def get_entry(self, entry_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Abc:",
        ),
    ] {
        if !read(&sdk.join(file)).contains(certified) {
            failures.push(format!("#992 {case}: {file} lacks {certified:?}"));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// What an `allOf` requires through a bare `{required: [...]}` member and
/// across repeated parents, as the certified pair decides it: a trailing bare
/// member requires the `$ref` parent's `name` and drops that parent's own
/// `required` (`PacketForCreate`, Benchling's `OligoBaseRequestForCreate`), and
/// so do models built on it (`PacketCreate`). It requires what an inline sibling
/// declares where no `$ref` stands beside it (`TrialCreate`, Benchling's
/// `StudyCreate`), and leaves optional a name two parents of the body declare
/// (`create_packet`'s `bin_id`, Benchling's `create_dna_oligo_with_helm`'s
/// `folder_id`). A property a later parent requires, which the earlier one
/// declares optional, is required (`Harvest.crop`).
#[test]
fn required_only_members_and_repeated_parents_decide_the_certified_requiredness() {
    let case = "required-only-members";
    let temp = tempfile::tempdir().expect("output tempdir");
    let mut failures = both_modes_failures(case, temp.path());
    let sdk = temp.path().join("sdk");
    for (file, certified) in [
        ("src/fern/types/packet_for_create.py", "    name: str\n"),
        (
            "src/fern/types/packet_for_create.py",
            "    grower: typing.Optional[str] = None\n",
        ),
        (
            "src/fern/types/packet_create.py",
            "    grower: typing.Optional[str] = None\n",
        ),
        ("src/fern/types/trial_create.py", "    title: str\n"),
        ("src/fern/types/harvest.py", "    crop: str\n"),
        (
            "src/fern/client.py",
            "        name: str,\n        label: typing.Optional[str] = OMIT,\n        \
             bin_id: typing.Optional[str] = OMIT,\n        grower: typing.Optional[str] = OMIT,\n",
        ),
    ] {
        if !read(&sdk.join(file)).contains(certified) {
            failures.push(format!("#985 {case}: {file} lacks {certified:?}"));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// The #981 and #983 departures explain only the change each catalogues: an
/// options entry, README call or path keyword renamed to anything but the
/// method's own name, or a vendored-runtime parse change other than the one
/// shipped, fails the comparison of the real generated tree.
#[test]
fn the_request_options_and_wire_key_departures_explain_only_their_own_change() {
    for (case, file, shipped, unexplained) in [
        (
            "request-options-body-property",
            "reference.md",
            "**_request_options:** `typing.Optional[RequestOptions]`",
            "**_options:** `typing.Optional[RequestOptions]`",
        ),
        (
            "request-options-body-property",
            "README.md",
            "_request_options={",
            "options={",
        ),
        (
            "request-options-body-property",
            "reference.md",
            "request_options_=\"request_options\",",
            "request_options_=\"labels\",",
        ),
        (
            "aliased-union-discriminator",
            "src/fern/core/pydantic_utilities.py",
            "if not IS_PYDANTIC_V2 and _has_discriminated_union(type_)",
            "if _has_discriminated_union(type_)",
        ),
    ] {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(case, "python-enums", &out);
        let path = out.join(file);
        let written = read(&path);
        assert!(
            written.contains(shipped),
            "{case}: {file} lacks {shipped:?}"
        );
        std::fs::write(&path, written.replacen(shipped, unexplained, 1)).expect("tamper");
        let failures = tampered_enum_failures(case, &out);
        assert!(
            failures.iter().any(|failure| failure.contains(file)),
            "{case}: writing {unexplained:?} into {file} must fail the comparison: {failures:?}"
        );
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
