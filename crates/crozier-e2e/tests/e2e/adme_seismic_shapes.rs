//! The six shapes corpus row 3004 (`microsoft-adme-seismic`) first mismatched
//! Fern on, each driven through the real binary over the minimal document
//! Fern generated `fern-expected/` from: crozier's complete SDK must equal
//! Fern's, the line that shape decides must read as Fern writes it in both
//! trees, and crozier's tree with that line put back the way crozier used to
//! write it must fail the comparison.

use std::path::Path;

use predicates::prelude::*;

use super::{
    certified_pair, departure_ledger, golden_tree_failures, probe_artifact_digest, probe_command,
    repo_root, sha256_hex,
};

const CASE: &str = "docs/fern-measurements/schema-shapes/adme-seismic-shapes";

/// The comparison failures of crozier's tree at `out` against Fern's.
fn failures(out: &Path) -> Vec<String> {
    let golden = format!("{CASE}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let spec = repo_root().join(CASE).join("openapi.yml");
    golden_tree_failures(
        "adme-seismic-shapes",
        &spec.display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey below generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Generate the case's SDK, hold it whole to Fern's, then show that `file`
/// spelling `fern` (as both trees do) is what the comparison turns on: with
/// `crozier` in its place the comparison names `file`.
fn holds_line(file: &str, fern: &str, crozier: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&repo_root().join(CASE).join("openapi.yml"), &out)
        .assert()
        .success();
    let matched = failures(&out);
    assert!(matched.is_empty(), "{}", matched.join("\n\n"));
    let expected = repo_root().join(CASE).join("fern-expected").join(file);
    for tree in [expected.as_path(), out.join(file).as_path()] {
        let text = std::fs::read_to_string(tree)
            .unwrap_or_else(|error| panic!("{}: {error}", tree.display()));
        assert!(text.contains(fern), "{}: no {fern:?}", tree.display());
    }
    let generated = out.join(file);
    let text = std::fs::read_to_string(&generated).unwrap();
    std::fs::write(&generated, text.replacen(fern, crozier, 1)).unwrap();
    let unexplained = failures(&out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{file} written as {crozier:?} must fail the comparison: {unexplained:?}"
    );
}

/// The case's provenance is the certified pair and the committed bytes, and a
/// missing document is an actionable failure that writes nothing.
#[test]
fn adme_seismic_shapes_evidence_pins_the_certified_tree() {
    let case = repo_root().join(CASE);
    let evidence = std::fs::read_to_string(case.join("evidence.toml")).unwrap();
    for field in [
        format!("fern_cli_version = \"{}\"", certified_pair().cli),
        format!(
            "fern_python_sdk_version = \"{}\"",
            certified_pair().python_sdk
        ),
        format!(
            "digest = \"{}\"",
            probe_artifact_digest(&case.join("fern-expected")).unwrap()
        ),
        format!(
            "source_digest = \"{}\"",
            sha256_hex(&std::fs::read(case.join("openapi.yml")).unwrap())
        ),
    ] {
        assert!(evidence.contains(&field), "{CASE}: missing {field}");
    }
    let temp = tempfile::tempdir().unwrap();
    let out = temp.path().join("sdk");
    probe_command(&temp.path().join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document writes no SDK");
}

/// `oneOf` members tagged by a one-member `enum` with no `type: string` form
/// an undiscriminated union, its members named by the property each alone
/// declares.
#[test]
fn an_untyped_enum_tag_leaves_a_one_of_undiscriminated() {
    holds_line(
        "src/fern/items/types/items_create_request_meta_item.py",
        "typing.Union[ItemsCreateRequestMetaItemUnitId, ItemsCreateRequestMetaItemCrsId]",
        "typing.Union[ItemsCreateRequestMetaItem_Unit, ItemsCreateRequestMetaItem_Crs]",
    );
}

/// The undiscriminated union's member carries its tag as an ordinary field, so
/// the README example passes the `kind` value a discriminated variant would
/// have filled in itself.
#[test]
fn an_untyped_enum_tag_is_passed_in_the_readme_example() {
    holds_line(
        "README.md",
        "            kind=ItemsCreateRequestMetaItemUnitIdKind.UNIT,\n",
        "",
    );
}

/// A property two inline `allOf` members declare is typed by the last
/// declaration, at the first one's place.
#[test]
fn an_all_of_property_takes_its_last_declaration() {
    holds_line(
        "src/fern/items/types/items_create_request_data.py",
        "    props: typing_extensions.Annotated[\n        ItemsCreateRequestDataProps,",
        "    props: typing_extensions.Annotated[\n        typing.Dict[str, typing.Any],",
    );
}

/// An unknown map the request example gives as `{}` is exampled by Fern's
/// `{"key": "value"}` placeholder rather than left out.
#[test]
fn an_empty_example_on_an_unknown_map_is_the_placeholder() {
    holds_line(
        "src/fern/items/client.py",
        "                ext={\"key\": \"value\"},\n",
        "",
    );
}

/// A README example string holding `"` is written double-quoted with the
/// quotes escaped, where the method docstring keeps Python's `repr`.
#[test]
fn a_readme_example_string_holding_quotes_is_json_spelled() {
    holds_line(
        "README.md",
        "ref=\"{\\\"a\\\":\\\"b\\\"}\",",
        "ref='{\"a\":\"b\"}',",
    );
    holds_line(
        "src/fern/items/client.py",
        "ref='{\"a\":\"b\"}',",
        "ref=\"{\\\"a\\\":\\\"b\\\"}\",",
    );
}

/// `widgetpart-get` under the tag `WidgetPart` is `get` in a `widgetpart`
/// group titled `Widgetpart`; `widget-part-list` under the same tag, whose
/// words are not the tag's one word, keeps its whole id in `widget_part`.
#[test]
fn a_hyphenated_tag_prefix_groups_by_the_word_it_spells() {
    holds_line(
        "src/fern/widgetpart/client.py",
        "class WidgetpartClient:",
        "class WidgetPartClient:",
    );
    holds_line(
        "src/fern/widget_part/client.py",
        "    def widget_part_list(",
        "    def list(",
    );
    holds_line("reference.md", "## Widgetpart\n", "## WidgetPart\n");
}

/// The async README imports a tag-scoped model before `datetime` when the
/// call passes the model first, as the sync README does.
#[test]
fn an_async_readme_imports_in_first_use_order() {
    holds_line(
        "README.md",
        "import asyncio\nfrom fern.items import ItemsCreateRequestInfo",
        "import asyncio\nimport datetime\nfrom fern.items import ItemsCreateRequestInfo",
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
