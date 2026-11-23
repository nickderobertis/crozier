//! The union-nullability and inherited-model repairs of tickets #825, #826,
//! #827, #838 and #839 (with the union-nullability rules the tickets' Vercel
//! and Hookdeck documents exposed beside them, and the schema-combination
//! repairs the certified screen of `combo-success-anyof-nullable`,
//! `combo-map-beside-oneof` and `combo-unrequired-tag-oneof-reference` exposed,
//! and the annotated-`$ref` description precedence the
//! `combo-annotated-ref-to-nullable-target` independence documents exposed,
//! and the Hookdeck and Vercel `union-member-nullability-and-object-models`
//! residual with ticket #828's list-item worked examples), each settled
//! against a from-scratch document under [`DIR`] and the certified pair's
//! complete tree for it (Fern CLI 5.200.0, fern-python-sdk 5.41.25), in both
//! enum modes.
//!
//! Every measurement runs the real binary and compares its SDK with the
//! certified tree file for file; each is shown to fail for its own rule by
//! writing back into crozier's output the bytes crozier wrote before the repair.

use std::collections::BTreeSet;
use std::path::{Path, PathBuf};

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, walk_files};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/union-inheritance";

/// A case's literals overlay, laid over its `fern-expected/`.
pub(crate) const LITERALS: &str = "expected-literals/fern-expected";

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
const MANIFEST: &str = ".crozier-overlay.json";

/// Each ticket's case and the rule's characteristic bytes in the certified
/// pair's tree: `(ticket, case, file, certified bytes, what crozier wrote before)`.
const MEASUREMENTS: &[(&str, &str, &str, &str, &str)] = &[
    (
        "#825",
        "null-union-alternative",
        "src/fern/kilns/types/register_kiln_request_settings_value_zero.py",
        "typing.Union[str, float, bool, typing.Dict[str, typing.Any]]",
        "typing.Union[str, float, bool, typing.Any, typing.Dict[str, typing.Any]]",
    ),
    (
        "#826",
        "nullable-typeless-component",
        "src/fern/types/shuttle_state.py",
        "ShuttleState = typing.Optional[typing.Any]",
        "ShuttleState = typing.Any",
    ),
    (
        "#827",
        "overridden-parent-layout",
        "src/fern/types/vent_closed_alert.py",
        "from .alert_base_severity import AlertBaseSeverity",
        "from .vent_alert_severity import VentAlertSeverity",
    ),
    (
        "#838",
        "restated-default-inherits-enum",
        "src/fern/types/crossing_delayed_notice.py",
        "phase: typing.Optional[CrossingDelayedNoticePhase]",
        "phase: typing.Optional[str]",
    ),
    (
        "#839",
        "declared-scalar-union-members",
        "src/fern/types/reading_value.py",
        "typing.Optional[str]",
        "typing.Optional[ReadingValueText]",
    ),
    (
        "#825 (a sibling `type: null` of a union)",
        "null-typed-composition",
        "src/fern/types/glaze_finish.py",
        "GlazeFinish = typing.Union[str, float, bool, typing.Dict[str, typing.Any], typing.List[\"GlazeFinish\"]]",
        "GlazeFinish = typing.Union[str, float, bool, typing.Dict[str, typing.Any], typing.Optional[typing.List[typing.Optional[\"GlazeFinish\"]]]]",
    ),
    (
        "#825 (a map's nullable object value)",
        "null-typed-composition",
        "src/fern/glazes/types/list_glaze_firings_response.py",
        "firings: typing.Dict[str, typing.Optional[ListGlazeFiringsResponseFiringsValue]]",
        "firings: typing.Dict[str, ListGlazeFiringsResponseFiringsValue]",
    ),
    (
        "#839 (a hoisted member's own nullability)",
        "nullable-union-members",
        "src/fern/types/loom_reading_payload.py",
        "typing.Union[typing.Optional[LoomReadingPayloadZero], typing.Optional[str]]",
        "typing.Union[LoomReadingPayloadZero, typing.Optional[str]]",
    ),
    (
        "a component pointer naming a slash-named component",
        "slash-named-component",
        "src/fern/client.py",
        "-> NotebooksListResponse:",
        "-> typing.Any:",
    ),
    (
        "a union ordinal past a `null` member",
        "slash-named-component",
        "src/fern/types/pages_request_response_page.py",
        "PagesRequestResponsePageContent, PagesRequestResponsePageOne, PagesRequestResponsePageTwo",
        "PagesRequestResponsePageContent, PagesRequestResponsePageTwo, PagesRequestResponsePageThree",
    ),
    (
        "combo-success-anyof-nullable: an unknown success body beside `null`",
        "nullable-unknown-success-body",
        "src/fern/probes/client.py",
        ") -> typing.Optional[typing.Any]:",
        ") -> typing.Any:",
    ),
    (
        "#825 (a response map's scalar value beside `null`)",
        "nullable-unknown-success-body",
        "src/fern/probes/client.py",
        ") -> typing.Dict[str, typing.Optional[str]]:",
        ") -> typing.Dict[str, ListProbeLabelsResponseValue]:",
    ),
    (
        "combo-map-beside-oneof: a discriminated union beside `additionalProperties`",
        "map-beside-union",
        "src/fern/types/glaze.py",
        "Glaze = typing.Dict[str, typing.Any]",
        "Glaze = typing_extensions.Annotated[typing.Union[Glaze_Matte, Glaze_Gloss], pydantic.Field(discriminator=\"finish\")]",
    ),
    (
        "combo-map-beside-oneof: that union sent as a `$ref` body",
        "map-beside-union",
        "src/fern/glazes/raw_client.py",
        "json=request,",
        "json=convert_and_respect_annotation_metadata(object_=request, annotation=Glaze, direction=\"write\"),",
    ),
    (
        "combo-map-beside-oneof: an inline body union beside `additionalProperties`",
        "map-beside-union",
        "src/fern/firings/client.py",
        "request: typing.Dict[str, typing.Any]",
        "request: LogFiringRequest",
    ),
    (
        "combo-unrequired-tag-oneof-reference: a bare `const` tag a member leaves unrequired",
        "unrequired-const-tag-union",
        "src/fern/entries/types/add_entry_request.py",
        "AddEntryRequest = typing.Union[StudioNote, StudioReminder]",
        "AddEntryRequest = typing.Union[AddEntryRequest_Note, AddEntryRequest_Reminder]",
    ),
    (
        "combo-unrequired-tag-oneof-reference: an `allOf` member's branches past an unrequired tag",
        "allof-unrequired-tag-branches",
        "src/fern/types/shelf.py",
        "    brackets: typing.Optional[int] = None\n    height: typing.Optional[float] = None\n",
        "",
    ),
    (
        "combo-unrequired-tag-oneof-reference: the first branch's spelling of a shared property",
        "allof-unrequired-tag-branches",
        "src/fern/types/shelf.py",
        "Mounted on the wall.",
        "Standing on the floor.",
    ),
    (
        "combo-unrequired-tag-oneof-reference: the merged branches keep their tag",
        "allof-unrequired-tag-branches",
        "src/fern/types/wall_shelf.py",
        "    type: typing.Optional[WallShelfType] = pydantic.Field(default=None)\n",
        "",
    ),
    (
        "combo-unrequired-tag-oneof-reference: a written discriminator still strips the tag",
        "allof-unrequired-tag-branches",
        "src/fern/types/rolling_cart.py",
        "class RollingCart(UniversalBaseModel):\n    wheels",
        "class RollingCart(UniversalBaseModel):\n    type: typing.Optional[RollingCartType] = None\n    wheels",
    ),
    (
        "combo-annotated-ref-to-nullable-target: a required annotated `$ref` field takes its annotation's description",
        "annotated-ref-description-precedence",
        "src/fern/types/entry.py",
        "    memo: str = pydantic.Field()\n    \"\"\"\n    The wording.\n",
        "    memo: str = pydantic.Field()\n    \"\"\"\n    A note kept beside the entry.\n",
    ),
    (
        "combo-annotated-ref-to-nullable-target: an annotated `$ref`'s copy takes its annotation's description",
        "annotated-ref-description-precedence",
        "src/fern/types/entry_tone.py",
        "    The tone's wording.\n",
        "    The tone kept beside the entry.\n",
    ),
    (
        "combo-annotated-ref-to-nullable-target: a required annotated `$ref` body argument takes its annotation's description",
        "annotated-ref-description-precedence",
        "src/fern/client.py",
        "        title : str\n            The title's wording.\n",
        "        title : str\n            The draft's title as written.\n",
    ),
    (
        "#827 (an inlined chain's inline type is named for the component declaring it)",
        "inlined-chain-inheritance",
        "src/fern/types/glazing_step.py",
        "    reason: typing.Optional[StepConfigReason] = None\n",
        "    reason: typing.Optional[StepReason] = None\n",
    ),
    (
        "#827 (an inlined chain writes each level's own fields before its parent's)",
        "inlined-chain-inheritance",
        "src/fern/types/firing_summary.py",
        "    shelves: typing.List[str]\n    created: typing.Optional[int] = None\n",
        "    created: typing.Optional[int] = None\n    shelves: typing.List[str]\n",
    ),
    (
        "#827 (a restatement writing no `nullable` keeps the parent's)",
        "inlined-chain-inheritance",
        "src/fern/types/kiln_alarm_view.py",
        "    codes: typing.Optional[typing.List[str]] = None\n",
        "    codes: typing.List[str]\n",
    ),
    (
        "#826 (a nullable free-form object component keeps its nullability)",
        "inlined-chain-inheritance",
        "src/fern/types/firing_notes.py",
        "FiringNotes = typing.Optional[typing.Dict[str, typing.Any]]",
        "FiringNotes = typing.Dict[str, typing.Any]",
    ),
    (
        "union-member-nullability-and-object-models: a query union's closed object member is its named model",
        "query-union-member-models",
        "src/fern/firings/types/list_firings_request_kiln.py",
        "ListFiringsRequestKiln = typing.Union[str, ListFiringsRequestKilnAll, typing.List[str]]",
        "ListFiringsRequestKiln = typing.Union[str, typing.Any, typing.List[str]]",
    ),
    (
        "union-member-nullability-and-object-models: a query union's empty closed object member is an empty model",
        "query-union-member-models",
        "src/fern/types/list_firings_request_glaze.py",
        "ListFiringsRequestGlaze = typing.Union[str, ListFiringsRequestGlazeOne]",
        "ListFiringsRequestGlaze = typing.Union[str, typing.Any]",
    ),
    (
        "union-member-nullability-and-object-models: a query union's open object member is its named model",
        "query-union-member-models",
        "src/fern/types/list_firings_request_cone.py",
        "ListFiringsRequestCone = typing.Union[str, ListFiringsRequestConeCone]",
        "ListFiringsRequestCone = typing.Union[str, typing.Any]",
    ),
    (
        "union-member-nullability-and-object-models: a query union's nullable enum members keep their nullability",
        "query-union-member-models",
        "src/fern/types/list_firings_request_atmosphere.py",
        "typing.Optional[ListFiringsRequestAtmosphereZero], typing.List[typing.Optional[ListFiringsRequestAtmosphereOneItem]]",
        "ListFiringsRequestAtmosphereZero, typing.List[ListFiringsRequestAtmosphereOneItem]",
    ),
    (
        "#827 (overlapping parents are inlined, and an untouched parent stays a base)",
        "inlined-chain-inheritance",
        "src/fern/types/kiln_plate.py",
        "class KilnPlate(StoreIds):",
        "class KilnPlate(UniversalBaseModel):",
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

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These journeys generate one small SDK per measurement row in each enum mode, comparing each whole against its certified tree, and two more without one, on the crozier-e2e edge every other golden comparison shares; a narrower edge for generator-replay journeys is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Each ticket's measurement is the certified pair's tree file for file in
/// both enum modes, and the comparison fails once the rule's bytes are written
/// back the way crozier wrote them before the repair.
#[test]
fn union_inheritance_repairs_match_the_certified_pair() {
    let mut failures = Vec::new();
    for (ticket, case, file, certified, before) in MEASUREMENTS {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(case, "python-enums", &out);
        failures.extend(enum_failures(case, &out));
        let path = out.join(file);
        let written = std::fs::read_to_string(&path)
            .unwrap_or_else(|error| panic!("{ticket} {case}: {file}: {error}"));
        assert!(
            written.contains(certified),
            "{ticket} {case}: {file} lacks the certified bytes {certified:?}"
        );
        std::fs::write(&path, written.replacen(certified, before, 1)).expect("tamper");
        let tampered = enum_failures(case, &out);
        assert!(
            tampered.iter().any(|failure| failure.contains(file)),
            "{ticket} {case}: writing {before:?} back into {file} must fail the comparison: {tampered:?}"
        );
        let literals = temp.path().join("literals");
        generate(case, "literals", &literals);
        failures.extend(literals_failures(case, &literals));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// #828's Markdown half: a list whose items are a union whose first member
/// requires a field typed by a null-bearing nested union is written empty in
/// the README and `reference.md`, as the certified pair writes it, while the
/// docstrings construct that member with the field (the
/// `required-null-union-field-example` departure). Both enum modes match the
/// certified trees whole.
#[test]
fn list_item_nested_union_markdown_lists_match_the_certified_pair() {
    let case = "list-item-nested-union";
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(case, "python-enums", &out);
    let mut failures = enum_failures(case, &out);
    let literals = temp.path().join("literals");
    generate(case, "literals", &literals);
    failures.extend(literals_failures(case, &literals));
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// #828 through `crozier compare`, as a migrating user runs it: against the
/// certified tree it passes, reporting the `required-null-union-field-example`
/// departure, and it fails once Fern's side writes the list populated, or gives
/// the field a default so that no omission remains. Unix only: on Windows
/// crozier runs no reference command (`compare_on_windows_runs_no_reference_command`).
#[cfg(unix)]
#[test]
fn list_item_nested_union_compare_reports_the_departure_and_holds_the_list() {
    let case = "list-item-nested-union";
    let compare = |edit: &dyn Fn(&Path)| -> (Option<i32>, String) {
        let dir = tempfile::tempdir().expect("compare tempdir");
        let reference = dir.path().join("reference");
        let expected = repo_root().join(golden(case));
        for rel in walk_files(&expected) {
            let to = reference.join(&rel);
            std::fs::create_dir_all(to.parent().expect("a parent")).expect("mkdir");
            std::fs::copy(expected.join(&rel), &to).expect("copy a Fern file");
        }
        edit(&reference);
        let config = dir.path().join("crozier.yml");
        std::fs::write(
            &config,
            format!(
                "reference:\n  command: cp -R '{}/.' \"$CROZIER_REFERENCE_OUTPUT\"\n\
                 generators:\n  python:\n    spec: '{}'\n    output: ./sdk\n    package-name: fern\n\
                 \x20   project-name: default_package_name\n    layout: packaged\n",
                reference.display(),
                spec(case).display()
            ),
        )
        .expect("write the config");
        let output = super::crozier()
            .arg("compare")
            .arg(&config)
            .output()
            .expect("run crozier compare");
        let said = format!(
            "{}{}",
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr)
        );
        (output.status.code(), said)
    };
    let differing = |said: &str, rel: &str| {
        said.split("differing (")
            .nth(1)
            .and_then(|rest| rest.split("intended departures").next())
            .is_some_and(|list| list.lines().any(|line| line.trim() == rel))
    };
    let edit = |rel: &'static str, from: &'static str, to: &'static str| {
        move |root: &Path| {
            let path = root.join(rel);
            let text = std::fs::read_to_string(&path).expect("a certified file");
            assert!(text.contains(from), "{rel} lacks {from:?}");
            std::fs::write(&path, text.replacen(from, to, 1)).expect("edit");
        }
    };
    let (code, said) = compare(&|_| {});
    assert_eq!(code, Some(0), "{said}");
    assert!(said.contains("required-null-union-field-example"), "{said}");
    // Fern's side writing a populated list is a difference no departure explains.
    let populated = "entries=[\n        PatchShelfEntriesRequestEntriesItemPayload(\n            label=\"label\",\n            operation=PatchShelfEntriesRequestEntriesItemPayloadOperation.CREATE,\n            payload=\"payload\",\n        )\n    ],";
    let (code, said) = compare(&edit("reference.md", "entries=[],", populated));
    assert_eq!(code, Some(3), "{said}");
    assert!(differing(&said, "reference.md"), "{said}");
    // A model of Fern's that gives the field a default is no omission, so
    // crozier's added argument is no departure there.
    let (code, said) = compare(&edit(
        "src/fern/types/patch_shelf_entries_request_entries_item_payload.py",
        "    payload: PatchShelfEntriesRequestEntriesItemPayloadPayload\n",
        "    payload: typing.Optional[PatchShelfEntriesRequestEntriesItemPayloadPayload] = None\n",
    ));
    assert_eq!(code, Some(3), "{said}");
    assert!(differing(&said, "src/fern/client.py"), "{said}");
}

/// A literal enum value holding `"` and no `'` is single-quoted in a client
/// docstring, as Python's `repr` writes it, and keeps its escaped
/// double-quoted spelling in the Markdown (Vercel's `create_webhook` events),
/// while a value holding `'` stays double-quoted. Both enum modes match the
/// certified pair, and writing the escaped spelling back into the docstring
/// fails the literals comparison.
#[test]
fn literal_enum_docstring_quotes_match_the_certified_pair() {
    let case = "literal-enum-docstring-quotes";
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(case, "python-enums", &out);
    let mut failures = enum_failures(case, &out);
    let literals = temp.path().join("literals");
    generate(case, "literals", &literals);
    failures.extend(literals_failures(case, &literals));
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
    let client = literals.join("src/fern/signs/client.py");
    let written = std::fs::read_to_string(&client).expect("the signs client");
    let certified = "wordings=['say \"cheese\"'],";
    assert!(written.contains(certified), "{written}");
    assert!(written.contains("motto=\"the 'early' bird\","), "{written}");
    std::fs::write(
        &client,
        written.replace(certified, "wordings=[\"say \\\"cheese\\\"\"],"),
    )
    .expect("tamper");
    let tampered = literals_failures(case, &literals);
    assert!(
        tampered
            .iter()
            .any(|failure| failure.contains("src/fern/signs/client.py")),
        "the escaped double-quoted docstring spelling must fail: {tampered:?}"
    );
}

// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), which AGENTS.md promotes out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// The repaired query-union members, imported from crozier's SDK in both enum
/// modes and from the certified tree: a closed or open object member's payload
/// parses into its named model with its fields, and `None` is accepted only by
/// the members the document declares nullable.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_query_union_member_models_parse_their_payloads() {
    let python = super::runtime_python_env().expect("SDK runtime environment");
    let script = repo_root().join("crates/crozier-e2e/tests/e2e/union_member_models_journey.py");
    let case = "query-union-member-models";
    let run = |src: &Path| {
        std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(src)
            .output()
            .expect("run the journey")
    };
    let usage = std::process::Command::new(&python)
        .arg(&script)
        .output()
        .expect("run the journey");
    assert_eq!(usage.status.code(), Some(2), "no SDK_SRC is a usage error");
    assert!(String::from_utf8_lossy(&usage.stderr).contains("usage:"));
    let missing = run(&repo_root().join(DIR).join(case));
    assert_eq!(
        missing.status.code(),
        Some(2),
        "a directory without the package"
    );
    let temp = tempfile::tempdir().expect("output tempdir");
    let mut sources = vec![repo_root().join(golden(case)).join("src")];
    for mode in ["python-enums", "literals"] {
        let out = temp.path().join(mode);
        generate(case, mode, &out);
        sources.push(out.join("src"));
    }
    for src in &sources {
        let output = run(src);
        let stdout = String::from_utf8_lossy(&output.stdout);
        assert!(
            output.status.success(),
            "{}: {stdout}{}",
            src.display(),
            String::from_utf8_lossy(&output.stderr)
        );
        assert!(
            stdout.contains("kiln: {any, all} parses into ListFiringsRequestKilnAll")
                && stdout.contains("null: accepted by atmosphere's nullable members only"),
            "{}: {stdout}",
            src.display()
        );
    }
}

/// #828's departure, executed: every worked-example construction of a model
/// whose required field is typed by a null-bearing union raises pydantic's
/// `ValidationError` for that field in the certified trees (both enum modes),
/// and constructs in crozier's SDKs, whose `reference.md` and README also
/// write the list of such union items empty, as the certified pair does.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_required_null_union_field_examples_construct_where_fern_s_fail() {
    let python = super::runtime_python_env().expect("SDK runtime environment");
    let script = repo_root().join("docs/departures/evidence/required-null-union-field-example.py");
    let case = "list-item-nested-union";
    let run = |root: &Path, expect: &str| {
        let output = std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(root)
            .arg(expect)
            .output()
            .expect("run the evidence script");
        let stdout = String::from_utf8_lossy(&output.stdout).into_owned();
        (output.status.success(), stdout)
    };
    let (literals, _, _) = literals_tree(case);
    for fern in [
        repo_root().join(golden(case)),
        literals.path().to_path_buf(),
    ] {
        let (ok, stdout) = run(&fern, "invalid");
        assert!(ok, "{}: {stdout}", fern.display());
        assert_eq!(
            stdout.matches("ValidationError: missing payload").count(),
            5,
            "{}: {stdout}",
            fern.display()
        );
        assert!(!run(&fern, "valid").0, "{}", fern.display());
    }
    // A usage error, or a root holding no generated package, exits 2.
    for args in [
        vec![],
        vec![
            repo_root().join(golden(case)).display().to_string(),
            "maybe".to_string(),
        ],
        vec![
            repo_root().join(DIR).join(case).display().to_string(),
            "invalid".to_string(),
        ],
    ] {
        let output = std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .args(&args)
            .output()
            .expect("run the evidence script");
        assert_eq!(output.status.code(), Some(2), "{args:?}");
        assert!(!output.stderr.is_empty(), "{args:?}: a diagnostic");
    }
    // A copy of the certified tree without its `reference.md` is no SDK root
    // (exit 2), and one whose constructor never closes is refused (exit 1).
    let broken = tempfile::tempdir().expect("broken tree tempdir");
    let copy = |name: &str| {
        let root = broken.path().join(name);
        let expected = repo_root().join(golden(case));
        for rel in walk_files(&expected) {
            let to = root.join(&rel);
            std::fs::create_dir_all(to.parent().expect("a parent")).expect("mkdir");
            std::fs::copy(expected.join(&rel), &to).expect("copy a Fern file");
        }
        root
    };
    let unreferenced = copy("unreferenced");
    std::fs::remove_file(unreferenced.join("reference.md")).expect("remove reference.md");
    let unclosed = copy("unclosed");
    let client = unclosed.join("src/fern/client.py");
    let text = std::fs::read_to_string(&client).expect("the certified client");
    let opener = "                PatchShelfNotesRequestNotesItem(\n                    label=\"label\",\n                )\n";
    assert!(text.contains(opener), "{text}");
    std::fs::write(&client, text.replacen(opener, "                PatchShelfNotesRequestNotesItem(\n                    label=\"label\",\n", 1))
        .expect("unclose");
    // Fern's constructions also missing another required field (`label`) fail
    // for more than the omission the departure corrects.
    let unlabelled = copy("unlabelled");
    let client = unlabelled.join("src/fern/client.py");
    let text = std::fs::read_to_string(&client).expect("the certified client");
    let dropped: String = text
        .split_inclusive('\n')
        .filter(|line| line.trim() != "label=\"label\",")
        .collect();
    assert_ne!(dropped, text, "the certified client passes label");
    std::fs::write(&client, dropped).expect("drop label");
    // Nor are they when another argument is also invalid (a mistyped `label`).
    let mistyped = copy("mistyped");
    let client = mistyped.join("src/fern/client.py");
    let text = std::fs::read_to_string(&client).expect("the certified client");
    let retyped = text.replace("label=\"label\",", "label=1,");
    assert_ne!(retyped, text, "the certified client passes label");
    std::fs::write(&client, retyped).expect("mistype label");
    for (root, code, said) in [
        (&unreferenced, 2, "reference.md"),
        (
            &mistyped,
            1,
            "ValidationError: missing payload; also label (string_type)",
        ),
        (&unclosed, 1, "never closes"),
        (&unlabelled, 1, "ValidationError: missing label, payload"),
    ] {
        let output = std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(root)
            .arg("invalid")
            .output()
            .expect("run the evidence script");
        let said_all = format!(
            "{}{}",
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr)
        );
        assert_eq!(output.status.code(), Some(code), "{said_all}");
        assert!(said_all.contains(said), "{said_all}");
    }
    // An SDK with no such construction proves nothing, so the script fails.
    let other = repo_root().join(golden("query-union-member-models"));
    let output = std::process::Command::new(&python)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .arg(&script)
        .arg(&other)
        .arg("invalid")
        .output()
        .expect("run the evidence script");
    assert_eq!(output.status.code(), Some(1), "{}", other.display());
    assert!(
        String::from_utf8_lossy(&output.stderr).contains("no worked example constructs a model"),
        "{}",
        String::from_utf8_lossy(&output.stderr)
    );
    let temp = tempfile::tempdir().expect("output tempdir");
    for mode in ["python-enums", "literals"] {
        let out = temp.path().join(mode);
        generate(case, mode, &out);
        let (ok, stdout) = run(&out, "valid");
        assert!(ok, "{mode}: {stdout}");
        assert_eq!(
            stdout.matches(": constructs").count(),
            5,
            "{mode}: {stdout}"
        );
        // crozier's constructions succeed, so they are not Fern's failing ones.
        assert!(!run(&out, "invalid").0, "{mode}");
        // A construction failing for another reason (a mistyped `label`)
        // is not the omission the departure corrects.
        let client = out.join("src/fern/client.py");
        let text = std::fs::read_to_string(&client).expect("the client");
        std::fs::write(&client, text.replace("label=\"label\",", "label=1,")).expect("mistype");
        let (ok, stdout) = run(&out, "invalid");
        let other_failures = stdout
            .lines()
            .filter(|line| line.ends_with("ValidationError: missing ; also label (string_type)"))
            .count();
        assert!(!ok && other_failures == 4, "{mode}: {stdout}");
        for doc in ["README.md", "reference.md"] {
            let text = std::fs::read_to_string(out.join(doc)).expect("a Markdown file");
            assert!(text.contains("    entries=[],\n"), "{mode} {doc}: {text}");
        }
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These journeys generate one small SDK per measurement row in each enum mode, comparing each whole against its certified tree, and two more without one, on the crozier-e2e edge every other golden comparison shares; a narrower edge for generator-replay journeys is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".

/// #839's other half: a structured alternative declaring a type name is still
/// named by it, while the scalar alternatives beside it stay inline and no
/// module is written for them.
#[test]
fn declared_scalar_union_members_stay_inline_and_structured_ones_stay_named() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate("declared-scalar-union-members", "python-enums", &out);
    let types = out.join("src/fern/types");
    assert!(
        types.join("threshold_band.py").is_file(),
        "the object alternative keeps its declared name"
    );
    for scalar in [
        "reading_value_text.py",
        "reading_value_number.py",
        "reading_value_flag.py",
        "reading_value_blob.py",
        "threshold_count.py",
    ] {
        assert!(
            !types.join(scalar).exists(),
            "crozier wrote a module for {scalar}"
        );
    }
    let threshold = std::fs::read_to_string(types.join("reading_threshold.py")).expect("the alias");
    assert!(
        threshold.contains("ReadingThreshold = typing.Union[int, ThresholdBand]"),
        "{threshold}"
    );
}

/// The slash-named-component measurement's pointer, spelled every way a document
/// can reach a component whose name holds a `/`: escaped as JSON Pointer
/// spells it, as a discriminator mapping's target, and from inside a webhook's
/// inline payload. Each names the component's class. Components whose names
/// spell one class (`tags/a/b-c` and `tags/a-b/c`, `drafts/note` and
/// `drafts-note`) each keep a class of their own, so no declaration displaces
/// another and each pointer names its own component's.
#[test]
fn slash_named_components_resolve_from_every_reference_spelling() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let spec = temp.path().join("openapi.yml");
    std::fs::write(&spec, SLASH_NAMED_REFERENCES).expect("write the document");
    let out = temp.path().join("sdk");
    probe_command(&spec, &out).assert().success();
    let read = |rel: &str| {
        std::fs::read_to_string(out.join(rel)).unwrap_or_else(|error| panic!("{rel}: {error}"))
    };
    let client = read("src/fern/client.py");
    assert!(
        client.contains("-> PagesPage:"),
        "the escaped pointer names PagesPage"
    );
    assert!(
        client.contains("-> EventsEvent:"),
        "the unescaped pointer names EventsEvent"
    );
    let event = read("src/fern/types/events_event.py");
    assert!(
        event.contains("typing.Union[EventsEvent_Created, EventsEvent_Deleted], pydantic.Field(discriminator=\"kind\")"),
        "the discriminator mapping reaches both slash-named members: {event}"
    );
    let payload = read("src/fern/types/post_page_changed_payload.py");
    assert!(
        payload.contains("    page: PagesPage"),
        "the webhook payload's pointer: {payload}"
    );
    // Components whose names spell one class each keep a class of their own
    // (`colliding-component-own-class`, #944): the last declaration keeps the
    // shared class, an earlier one its own path's class with an ordinal, and
    // every pointer names its own component's.
    let tags = read("src/fern/types/get_tags_response.py");
    for (field, class) in [
        ("first", "TagsABC2"),
        ("second", "TagsABC"),
        ("slashed", "DraftsNote2"),
        ("declared", "DraftsNote"),
    ] {
        assert!(
            tags.contains(&format!("    {field}: typing.Optional[{class}] = None")),
            "{field} names its own component's class {class}: {tags}"
        );
    }
    for (file, declaration) in [
        ("drafts_note.py", "DraftsNote = int"),
        ("drafts_note2.py", "DraftsNote2 = str"),
        ("tags_abc.py", "TagsABC = int"),
        ("tags_abc2.py", "TagsABC2 = str"),
    ] {
        let text = read(&format!("src/fern/types/{file}"));
        assert!(text.contains(declaration), "{file}: {text}");
    }
}

/// The document [`slash_named_components_resolve_from_every_reference_spelling`] generates.
const SLASH_NAMED_REFERENCES: &str = r##"openapi: 3.1.0
info:
  title: Relay
  version: "1.0"
paths:
  /pages/{id}:
    get:
      operationId: getPage
      parameters:
        - {name: id, in: path, required: true, schema: {type: string}}
      responses:
        "200":
          description: The page.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/pages~1page"
  /tags:
    get:
      operationId: getTags
      responses:
        "200":
          description: Both tags.
          content:
            application/json:
              schema:
                type: object
                properties:
                  first:
                    $ref: "#/components/schemas/tags/a/b-c"
                  second:
                    $ref: "#/components/schemas/tags/a-b/c"
                  slashed:
                    $ref: "#/components/schemas/drafts/note"
                  declared:
                    $ref: "#/components/schemas/drafts-note"
  /events:
    get:
      operationId: listEvents
      responses:
        "200":
          description: The latest event.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/events/event"
webhooks:
  pageChanged:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [page]
              properties:
                page:
                  $ref: "#/components/schemas/pages/page"
      responses:
        "200":
          description: Received.
components:
  schemas:
    pages/page:
      type: object
      required: [id]
      properties:
        id: {type: string}
    events/created:
      type: object
      required: [kind]
      properties:
        kind: {type: string}
    events/deleted:
      type: object
      required: [kind]
      properties:
        kind: {type: string}
    drafts/note:
      type: string
    drafts-note:
      type: integer
    tags/a/b-c:
      type: string
    tags/a-b/c:
      type: integer
    events/event:
      oneOf:
        - $ref: "#/components/schemas/events/created"
        - $ref: "#/components/schemas/events/deleted"
      discriminator:
        propertyName: kind
        mapping:
          created: "#/components/schemas/events/created"
          deleted: "#/components/schemas/events/deleted"
"##;
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
