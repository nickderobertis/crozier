//! The union-nullability and inherited-model repairs of tickets #825, #826,
//! #827, #838 and #839 (with the union-nullability rules the tickets' Vercel
//! and Hookdeck documents exposed beside them, and the schema-combination
//! repairs the certified screen of `combo-success-anyof-nullable`,
//! `combo-map-beside-oneof` and `combo-unrequired-tag-oneof-reference` exposed),
//! each settled against a from-scratch document under
//! [`DIR`] and the certified pair's complete tree for it (Fern CLI 5.200.0,
//! fern-python-sdk 5.41.25), in both enum modes.
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

/// crozier's literals SDK for `case` against the certified pair's literals
/// tree: the base less the files the overlay removes, with the overlay's own
/// files laid over it.
fn literals_failures(case: &str, out: &Path) -> Vec<String> {
    let base = repo_root().join(golden(case));
    let overlay_golden = format!("{DIR}/{case}/{LITERALS}");
    let overlay = repo_root().join(&overlay_golden);
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
/// inline payload. Each names the component's class. A slash-named component
/// whose renaming would coincide with another's, or with a declared name, keeps
/// its own name, so no declaration displaces another, and its pointer stays
/// unresolved: the unknown type.
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
    let tags = read("src/fern/types/get_tags_response.py");
    for field in ["first", "second", "slashed"] {
        assert!(
            tags.contains(&format!("    {field}: typing.Optional[typing.Any] = None")),
            "{field} stays an unresolved pointer: {tags}"
        );
    }
    // `drafts/note` would rename onto the declared `drafts-note`, so it keeps its
    // name: the declared component is still the one its own pointer names.
    assert!(
        tags.contains("    declared: typing.Optional[DraftsNote] = None"),
        "the declared `drafts-note` is still the component its pointer names: {tags}"
    );
    let note = read("src/fern/types/drafts_note.py");
    assert!(
        note.contains("DraftsNote = int"),
        "`drafts-note` keeps its own integer declaration: {note}"
    );
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
