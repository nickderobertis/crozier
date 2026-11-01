//! The union-modelling root causes the fixture-only witness searches handed
//! off, each measured in a document written for it under
//! `docs/fern-measurements/handed-off/union-modelling/` and held whole against
//! the certified pair's tree, in both enum modes where the mode changes the
//! result. The triage record is
//! `docs/fern-measurements/handed-off/union-modelling.tsv`; each case's
//! `README.md` states the rule and its verdict.

use std::path::{Path, PathBuf};

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root};

/// Where the measurements live; every `fern-expected/` beneath is a compared golden.
pub(crate) const UNION_MODELLING_DIR: &str = "docs/fern-measurements/handed-off/union-modelling";

/// Every measured case, and whether its `literals/fern-expected/` tree is
/// committed (only where the enum mode changes more than `core/enum.py`).
const CASES: &[(&str, bool)] = &[
    ("R8", true),
    ("R9", true),
    ("R13", true),
    ("allof-oneof-inline-member-consts", true),
    ("const-tag-variants-undiscriminated", true),
    ("inline-response-union-variant-naming", true),
    ("inline-union-hoisting", true),
    ("map-value-union-hoisting", false),
    ("nullable-anyof-ref-member-optional", false),
    ("pattern-properties-only-oneof-member", false),
    ("query-anyof-date-time-or-array-named", false),
    ("query-oneof-of-arrays", false),
    ("union-modelling/identical-primitive-members", false),
    ("union-modelling/multi-type-open-object", false),
    ("union-modelling/nullable-reference-member", false),
    ("union-modelling/singleton-enum-tags", false),
];

/// Every committed tree under [`UNION_MODELLING_DIR`], for the compared-goldens
/// inventory: each case's `fern-expected/` and, where committed, its
/// `literals/fern-expected/`.
pub(crate) fn goldens() -> Vec<String> {
    CASES
        .iter()
        .flat_map(|(case, literals)| {
            let mut trees = vec![golden(case, "python-enums")];
            if *literals {
                trees.push(golden(case, "literals"));
            }
            trees
        })
        .collect()
}

fn spec(case: &str) -> PathBuf {
    repo_root()
        .join(UNION_MODELLING_DIR)
        .join(case)
        .join("openapi.yml")
}

fn golden(case: &str, mode: &str) -> String {
    if mode == "literals" {
        format!("{UNION_MODELLING_DIR}/{case}/literals/fern-expected")
    } else {
        format!("{UNION_MODELLING_DIR}/{case}/fern-expected")
    }
}

fn modes(case: &str) -> &'static [&'static str] {
    let literals = CASES
        .iter()
        .find(|(name, _)| *name == case)
        .unwrap_or_else(|| panic!("{case} is no registered case"))
        .1;
    if literals {
        &["python-enums", "literals"]
    } else {
        &["python-enums"]
    }
}

fn generate(case: &str, mode: &str, out: &Path) {
    probe_command(&spec(case), out)
        .args(["--enum-type", mode])
        .assert()
        .success();
}

/// crozier's SDK for `case` in `mode` against its committed certified-pair
/// tree, apart from the departures the ledger records for that tree. Where a
/// mode's tree is not committed (the mode changes only `core/enum.py`), the
/// `python-enums` tree is the reference and that mode is not compared.
fn failures(case: &str, mode: &str, out: &Path) -> Vec<String> {
    let golden = golden(case, mode);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        &format!("{case} ({mode})"),
        &spec(case).display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

fn read(out: &Path, path: &str) -> String {
    std::fs::read_to_string(out.join(path)).unwrap_or_else(|error| panic!("{path}: {error}"))
}

/// Generate `case` in every committed mode, require each byte-match, and
/// return the `python-enums` output for the case's own assertions.
fn matched(case: &str) -> tempfile::TempDir {
    let mut first = None;
    for mode in modes(case) {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(case, mode, &out);
        let found = failures(case, mode, &out);
        assert!(found.is_empty(), "{case} ({mode}): {}", found.join("\n\n"));
        first.get_or_insert(temp);
    }
    first.expect("every case has a python-enums tree")
}

/// Rewrite `path` in the `python-enums` output back to what crozier wrote
/// before the repair (`from` → `to`), and require the comparison to name it:
/// the byte-match above is not vacuous.
fn mutation_is_named(case: &str, temp: &tempfile::TempDir, path: &str, from: &str, to: &str) {
    let out = temp.path().join("sdk");
    let text = read(&out, path);
    assert!(
        text.contains(from),
        "{case}: {path} lacks {from:?}:\n{text}"
    );
    std::fs::write(out.join(path), text.replacen(from, to, 1)).expect("rewrite the module");
    let found = failures(case, "python-enums", &out);
    assert!(
        found.iter().any(|failure| failure.contains(path)),
        "{case}: the pre-repair {path} must fail the comparison: {found:?}"
    );
}

fn sdk(temp: &tempfile::TempDir) -> PathBuf {
    temp.path().join("sdk")
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// A `nullable: true` beside a multi-member union is not read onto the alias,
/// and a member naming a component that admits null is optional in its slot.
#[test]
fn a_nullable_union_keeps_its_members_and_a_nullable_target_its_optional() {
    let case = "nullable-anyof-ref-member-optional";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/swatch_or_name.py")
        .contains("SwatchOrName = typing.Union[str, Swatch]"));
    assert!(read(&out, "src/fern/types/glaze_or_swatch.py")
        .contains("GlazeOrSwatch = typing.Union[typing.Optional[Glaze], Swatch]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/swatch_or_name.py",
        "typing.Union[str, Swatch]",
        "typing.Union[str, typing.Optional[Swatch]]",
    );
}

/// A `$ref` written beside `anyOf` is that reference, and a one-member union
/// of a type-less `patternProperties`-only closed object is undocumented `Any`.
#[test]
fn a_reference_beside_a_union_and_a_pattern_only_member_read_as_fern_reads_them() {
    let case = "pattern-properties-only-oneof-member";
    let temp = matched(case);
    let out = sdk(&temp);
    let labels = read(&out, "src/fern/types/label_translations.py");
    assert!(labels.contains("LabelTranslations = typing.Any"), "{labels}");
    assert!(!labels.contains("Translations keyed"), "{labels}");
    assert!(read(&out, "src/fern/types/collector_note.py").contains("CollectorNote = CollectorRef"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/label_translations.py",
        "typing.Any",
        "typing.Dict[str, typing.Any]",
    );
}

/// Ruling 6 (`inline-union-types`): a map value that is an `allOf` of one
/// `$ref` is that reference, with no value model of crozier's own, and a
/// nested-array map leaf names the inline value model Fern names.
#[test]
fn map_values_take_the_certified_pairs_types_rather_than_hoisted_value_models() {
    let case = "map-value-union-hoisting";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/depths_by_station.py")
        .contains("DepthsByStation = typing.Dict[str, Depth]"));
    assert!(read(&out, "src/fern/types/buoys_by_station.py")
        .contains("typing.Dict[str, typing.Optional[Buoy]]"));
    assert!(!out.join("src/fern/types/depths_by_station_value.py").exists());
    assert!(read(&out, "src/fern/types/tide_grid.py")
        .contains("typing.List[typing.List[typing.Dict[str, TideGridItemItemValue]]]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/depths_by_station.py",
        "typing.Dict[str, Depth]",
        "typing.Dict[str, DepthsByStationValue]",
    );
}

/// `$ref` members fixing an unrequired tag with a bare `const` are a plain
/// union, each member keeping its tag as a one-value enum (an open literal in
/// `literals` mode).
#[test]
fn bare_const_tags_leave_a_reference_union_undiscriminated() {
    let case = "const-tag-variants-undiscriminated";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/vessel.py")
        .contains("Vessel = typing.Union[Sailboat, Barge]"));
    assert!(read(&out, "src/fern/types/sailboat.py")
        .contains("hull: typing.Optional[SailboatHull] = None"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/vessel.py",
        "typing.Union[Sailboat, Barge]",
        "typing.Union[Vessel_Sail, Vessel_Barge]",
    );
}

/// Beside an open, property-less object, a `oneOf` or `anyOf` of inline
/// objects lends every branch's properties, each as the first branch writes
/// it, `const` and one-value `enum` tags alike hoisted as enums.
#[test]
fn an_open_base_s_union_lends_its_first_branch_s_properties() {
    let case = "allof-oneof-inline-member-consts";
    let temp = matched(case);
    let out = sdk(&temp);
    for module in [
        "handover_one_of_const",
        "handover_any_of_const",
        "handover_one_of_enum",
        "handover_any_of_enum",
    ] {
        let model = read(&out, &format!("src/fern/types/{module}.py"));
        assert!(model.contains("Collection region, chosen at pickup."), "{module}: {model}");
        assert!(model.contains("courier: typing.Optional[str] = None"), "{module}: {model}");
        assert!(read(&out, &format!("src/fern/types/{module}_mode.py")).contains("PICKUP = \"pickup\""));
    }
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/handover_any_of_const.py",
        "Collection region, chosen at pickup.",
        "Delivery region.",
    );
}

/// Two query arrays of one element type are the one-or-many array.
#[test]
fn a_query_one_of_two_like_arrays_is_one_or_many() {
    let case = "query-oneof-of-arrays";
    let temp = matched(case);
    let out = sdk(&temp);
    let client = read(&out, "src/fern/client.py");
    assert!(
        client.contains(
            "typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]"
        ),
        "{client}"
    );
    mutation_is_named(
        case,
        &temp,
        "src/fern/client.py",
        "typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]",
        "typing.Sequence[typing.Dict[str, typing.Any]]",
    );
}

/// A query `anyOf` of a nullable scalar and an array of it is the named
/// request union, its nullable scalar member optional.
#[test]
fn a_query_any_of_nullable_scalar_or_array_is_a_named_union() {
    let case = "query-anyof-date-time-or-array-named";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/list_parcels_request_shipped_at.py").contains(
        "ListParcelsRequestShippedAt = typing.Union[typing.Optional[dt.datetime], typing.List[typing.Optional[dt.datetime]]]"
    ));
    assert!(read(&out, "src/fern/client.py")
        .contains("shipped_at: typing.Optional[ListParcelsRequestShippedAt] = None"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/list_parcels_request_weight.py",
        "typing.Optional[int], typing.List",
        "int, typing.List",
    );
}

/// Ruling 6 (`inline-union-types`): a lone `$ref` element is that reference,
/// its model keeping its tag, and an annotated map beside `null` is the map.
#[test]
fn inline_unions_are_written_as_the_certified_pair_writes_them() {
    let case = "inline-union-hoisting";
    let temp = matched(case);
    let out = sdk(&temp);
    let toolbox = read(&out, "src/fern/types/toolbox.py");
    assert!(toolbox.contains("tools: typing.List[ChiselTool]"), "{toolbox}");
    assert!(
        toolbox.contains("labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None"),
        "{toolbox}"
    );
    assert!(read(&out, "src/fern/types/chisel_tool.py").contains("kind: ChiselToolKind"));
    for hoisted in ["toolbox_tools_item.py", "toolbox_labels.py"] {
        assert!(!out.join("src/fern/types").join(hoisted).exists(), "{hoisted}");
    }
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/toolbox.py",
        "typing.List[ChiselTool]",
        "typing.List[ToolboxToolsItem]",
    );
}

/// The component union of constraint-only branches matched the certified
/// pair at this node's base (`already-matching`), and still does.
#[test]
fn a_constraint_only_union_names_its_variants_as_fern_does() {
    let case = "inline-response-union-variant-naming";
    let temp = matched(case);
    assert!(read(&sdk(&temp), "src/fern/types/harvest_board.py")
        .contains("HarvestBoard = typing.Union[HarvestBoardZero, HarvestBoardHarvests]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/harvest_board.py",
        "HarvestBoardZero, HarvestBoardHarvests",
        "HarvestBoard_, HarvestBoardLedgerClosed",
    );
}

/// R8: array items over type-less object members are a named union of
/// models, and a model hoisted out of its own recursive base restates it.
#[test]
fn object_member_items_are_a_named_union_of_models() {
    let case = "R8";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/link_patch_item.py")
        .contains("LinkPatchItem = typing.Union[LinkPatchItemZero, LinkPatchItemOne]"));
    assert!(read(&out, "src/fern/client.py").contains("request=[LinkPatchItemZero()]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/link_patch.py",
        "typing.List[LinkPatchItem]",
        "typing.List[typing.Dict[str, typing.Any]]",
    );
}

/// R9: a `discriminator` over `$ref`s it cannot tell apart names the union
/// after the property, and a model inheriting the property reuses that name.
#[test]
fn an_undecidable_discriminator_names_the_property_union() {
    let case = "R9";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/types/shift_assignment.py")
        .contains("ShiftAssignment = typing.Union[Cover, Training, Leave]"));
    assert!(read(&out, "src/fern/types/shift.py")
        .contains("assignment: typing.Optional[ShiftAssignment] = None"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/shift.py",
        "typing.Optional[ShiftAssignment]",
        "typing.Optional[typing.Union[Cover, Training, Leave]]",
    );
}

/// R13: a query array of an inline enum beside `null` names its item enum.
#[test]
fn a_nullable_query_array_of_an_inline_enum_names_its_item() {
    let case = "R13";
    let temp = matched(case);
    let out = sdk(&temp);
    assert!(read(&out, "src/fern/client.py")
        .contains("channels: typing.Optional[typing.Sequence[ToggleAssistantRequestChannelsItem]] = None"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/client.py",
        "typing.Sequence[ToggleAssistantRequestChannelsItem]",
        "typing.Sequence[typing.Union[typing.Literal[\"portal\", \"chat\"], typing.Any]]",
    );
}

/// `union-modelling`'s sub-rules, each in its own document.
#[test]
fn union_modelling_sub_rules_match_the_certified_pair() {
    let case = "union-modelling/identical-primitive-members";
    let temp = matched(case);
    assert!(read(&sdk(&temp), "src/fern/types/survey.py")
        .contains("corners: typing.Optional[typing.List[typing.List[str]]]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/survey.py",
        "typing.List[typing.List[str]]",
        "typing.List[typing.List[SurveyCornersItemItem]]",
    );

    let case = "union-modelling/nullable-reference-member";
    let temp = matched(case);
    assert!(read(&sdk(&temp), "src/fern/types/recording_started_at.py")
        .contains("RecordingStartedAt = typing.Union[typing.Optional[Moment], int]"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/recording_started_at.py",
        "typing.Optional[Moment], int",
        "Moment, int",
    );

    let case = "union-modelling/multi-type-open-object";
    let temp = matched(case);
    assert!(read(&sdk(&temp), "src/fern/types/batch_receipt_details.py").contains(
        "BatchReceiptDetails = typing.Union[typing.Dict[str, typing.Any], typing.List[typing.Any]]"
    ));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/batch_receipt.py",
        "typing.Optional[BatchReceiptDetails]",
        "typing.Optional[typing.Dict[str, typing.Any]]",
    );

    let case = "union-modelling/singleton-enum-tags";
    let temp = matched(case);
    let author = read(&sdk(&temp), "src/fern/types/author.py");
    assert!(author.contains("class Author_Harbour("), "{author}");
    assert!(!read(&sdk(&temp), "src/fern/types/crew_member.py").contains("kind:"));
    mutation_is_named(
        case,
        &temp,
        "src/fern/types/crew_member.py",
        "class CrewMember(UniversalBaseModel):\n",
        "class CrewMember(UniversalBaseModel):\n    kind: CrewMemberKind\n",
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
