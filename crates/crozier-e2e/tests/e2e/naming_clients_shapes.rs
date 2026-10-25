//! The client-construction and docstring shapes the `naming-clients` removal
//! controls first showed crozier departing from the certified pair on, each
//! driven through the real binary over one of two from-scratch documents Fern
//! generated `fern-expected/` from (`clients_extensions_measurements_match_fern`
//! compares both whole): the line a shape decides must read as Fern writes it in
//! both trees, and crozier's tree with that line put back the way crozier used to
//! write it must fail the comparison. The removal controls are
//! `docs/openapi-surface/witness-search-operation-combinations-naming-clients/README.md`'s.

use std::path::Path;

use predicates::prelude::*;

use super::{
    departure_ledger, golden_path, golden_tree_failures, probe_command, repo_root,
    CLIENTS_EXTENSIONS_DIR,
};

/// The bearer document: a root `security: [{}]`, root and grouped methods
/// whose descriptions end a line in a backslash, and two `stream-condition`
/// operations, one named by its `operationId` and one by nothing.
const TIDE_DESK: &str = "harbour-tide-desk";

/// The basic document: an HTTP `basic` scheme no Security Requirement Object
/// names.
const KEEPER_ROSTER: &str = "lighthouse-keeper-roster";

fn case_dir(case: &str) -> std::path::PathBuf {
    repo_root().join(CLIENTS_EXTENSIONS_DIR).join(case)
}

/// The comparison failures of crozier's tree at `out` against Fern's.
fn failures(case: &str, out: &Path) -> Vec<String> {
    let expected = case_dir(case).join("fern-expected");
    let ledger = departure_ledger()
        .golden(&golden_path(&expected), &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let spec = case_dir(case).join("openapi.yml");
    golden_tree_failures(case, &spec.display().to_string(), &ledger, &expected, out)
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey below generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Generate `case`'s SDK, hold it whole to Fern's, then show that `file`
/// spelling `fern` (as both trees do) is what the comparison turns on: with
/// `crozier` in its place the comparison names `file`.
fn holds_line(case: &str, file: &str, fern: &str, crozier: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&case_dir(case).join("openapi.yml"), &out)
        .assert()
        .success();
    let matched = failures(case, &out);
    assert!(matched.is_empty(), "{}", matched.join("\n\n"));
    let expected = case_dir(case).join("fern-expected").join(file);
    for tree in [expected.as_path(), out.join(file).as_path()] {
        let text = std::fs::read_to_string(tree)
            .unwrap_or_else(|error| panic!("{}: {error}", tree.display()));
        assert!(text.contains(fern), "{}: no {fern:?}", tree.display());
    }
    let generated = out.join(file);
    let text = std::fs::read_to_string(&generated).unwrap();
    std::fs::write(&generated, text.replacen(fern, crozier, 1)).unwrap();
    let unexplained = failures(case, &out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{file} written as {crozier:?} must fail the comparison: {unexplained:?}"
    );
}

/// A document that cannot be read is an actionable failure that writes no SDK.
#[test]
fn a_missing_naming_clients_document_writes_nothing() {
    let temp = tempfile::tempdir().unwrap();
    let out = temp.path().join("sdk");
    probe_command(&temp.path().join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document writes no SDK");
}

/// A root method's docstring separators keep their 8-space indent in an
/// OpenAPI 3.0 document, where crozier used to indent them only under 3.1.
#[test]
fn a_root_docstring_keeps_its_indent_in_a_3_0_document() {
    holds_line(
        TIDE_DESK,
        "src/fern/client.py",
        "Archived tables are filed under C:\\\\\n        \n        Parameters",
        "Archived tables are filed under C:\\\\\n\n        Parameters",
    );
}

/// A grouped method's docstring separators carry the same indent.
#[test]
fn a_grouped_docstring_keeps_its_indent() {
    holds_line(
        TIDE_DESK,
        "src/fern/gauges/client.py",
        "Calibration files sit under E:\\\\\n        \n        Parameters",
        "Calibration files sit under E:\\\\\n\n        Parameters",
    );
}

/// A raw streaming method's empty return description is a 12-space line.
#[test]
fn a_raw_stream_docstring_writes_its_empty_description_indented() {
    holds_line(
        TIDE_DESK,
        "src/fern/raw_client.py",
        "typing.Iterator[HttpResponse[typing.Iterator[SurgeUpdate]]]\n            \n        \"\"\"",
        "typing.Iterator[HttpResponse[typing.Iterator[SurgeUpdate]]]\n\n        \"\"\"",
    );
}

/// A root `security` holding only the anonymous `{}` leaves the token required.
#[test]
fn an_anonymous_only_requirement_keeps_the_token_required() {
    holds_line(
        TIDE_DESK,
        "src/fern/client.py",
        "        token: typing.Union[str, typing.Callable[[], str]],\n",
        "        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,\n",
    );
}

/// A `stream-condition` operation with neither a method name nor an
/// `operationId` is one buffered method named from its summary, sending the
/// condition cleared.
#[test]
fn an_unnamed_stream_condition_operation_is_one_buffered_method() {
    holds_line(
        TIDE_DESK,
        "src/fern/forecasts/client.py",
        "    def forecast_the_next_tide(self, *, port: str,",
        "    def stream(self, *, port: str,",
    );
    holds_line(
        TIDE_DESK,
        "src/fern/forecasts/raw_client.py",
        "                \"stream\": False,\n",
        "",
    );
}

/// `reference.md` documents the condition field in its declared place, ahead
/// of the `port` declared after it.
#[test]
fn a_stream_condition_field_is_documented_in_its_declared_place() {
    holds_line(
        TIDE_DESK,
        "reference.md",
        "**stream:** `typing.Literal` — Whether to stream the forecast as it is computed.",
        "**port:** `str` — The port to forecast for.",
    );
}

/// An HTTP `basic` scheme no requirement names still wires optional
/// credentials.
#[test]
fn a_basic_scheme_without_a_requirement_keeps_optional_credentials() {
    holds_line(
        KEEPER_ROSTER,
        "src/fern/client.py",
        "        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,\n",
        "",
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
