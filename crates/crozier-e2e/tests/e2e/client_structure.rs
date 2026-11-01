//! The client-structure root causes the three fixture-only witness searches
//! handed off, each in a document written for it, held whole against the
//! certified pair's tree (`docs/fern-measurements/handed-off/client-structure/`,
//! triaged in `docs/fern-measurements/handed-off/client-structure.tsv`).
//!
//! Every journey runs the real binary on the measurement document, compares
//! the SDK it writes with the committed `fern-expected/` tree (and the
//! `expected-literals/` tree where the enum mode changes the result) apart from
//! the departures the ledger records, asserts the lines the cause decides, and
//! then puts back what crozier wrote before the repair to show the comparison
//! names it.

use std::path::{Path, PathBuf};

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root};

/// Where the measurements live; each case's trees are compared goldens.
pub(crate) const CLIENT_STRUCTURE_DIR: &str = "docs/fern-measurements/handed-off/client-structure";
/// The complete certified-pair tree generated with `enum_type: python_enums`.
pub(crate) const PYTHON_ENUMS_TREE: &str = "fern-expected";
/// The complete certified-pair tree generated with Fern's default literals.
pub(crate) const LITERALS_TREE: &str = "expected-literals";

fn spec(case: &str) -> PathBuf {
    repo_root()
        .join(CLIENT_STRUCTURE_DIR)
        .join(case)
        .join("openapi.yml")
}

fn golden(case: &str, mode: &str) -> String {
    let tree = if mode == "literals" {
        LITERALS_TREE
    } else {
        PYTHON_ENUMS_TREE
    };
    format!("{CLIENT_STRUCTURE_DIR}/{case}/{tree}")
}

/// crozier's SDK for `case` in `mode`, written by the binary into a tempdir.
fn generate(case: &str, mode: &str) -> (tempfile::TempDir, PathBuf) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&spec(case), &out)
        .args(["--enum-type", mode])
        .assert()
        .success();
    (temp, out)
}

/// Every file of `out` that differs from the case's certified tree, apart from
/// the departures the ledger records for it.
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

fn read(out: &Path, rel: &str) -> String {
    std::fs::read_to_string(out.join(rel)).unwrap_or_else(|e| panic!("{rel}: {e}"))
}

/// Generate `case` in `mode`, require the certified tree byte for byte, and
/// return the SDK for the cause's own assertions.
fn matching(case: &str, mode: &str) -> (tempfile::TempDir, PathBuf) {
    let (temp, out) = generate(case, mode);
    let found = failures(case, mode, &out);
    assert!(found.is_empty(), "{case} ({mode}): {}", found.join("\n\n"));
    (temp, out)
}

/// Rewrite `rel` of `out` as crozier wrote it before the repair (`from` →
/// `to`) and require the comparison to name that file.
fn regression_is_named(case: &str, mode: &str, out: &Path, rel: &str, from: &str, to: &str) {
    let text = read(out, rel);
    assert!(text.contains(from), "{case}: {rel} lacks {from:?}:\n{text}");
    std::fs::write(out.join(rel), text.replacen(from, to, 1)).unwrap();
    let found = failures(case, mode, out);
    assert!(
        found.iter().any(|failure| failure.contains(rel)),
        "{case} ({mode}): the pre-repair {rel} must differ: {found:?}"
    );
    std::fs::write(out.join(rel), text).unwrap();
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".

/// `untagged-operation-grouping`: a method named by `x-fern-sdk-method-name`
/// alone is the root client's, whatever its tag.
#[test]
fn a_method_name_without_a_group_lands_on_the_root_client() {
    let case = "untagged-operation-grouping";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "src/fern/client.py").contains("def book_stay("));
    assert!(!read(&out, "src/fern/stays/client.py").contains("def book_stay("));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "README.md",
        "client.book_stay(",
        "client.stays.book_stay(",
    );
}

/// `subpackage-order`: a package's children follow each one's first own
/// operation, a child holding only nested operations last.
#[test]
fn nested_sub_clients_follow_their_first_own_operation() {
    let case = "subpackage-order";
    let (_temp, out) = matching(case, "python-enums");
    let library = read(&out, "src/fern/library/client.py");
    let at = |name: &str| {
        library
            .find(&format!("def {name}(self)"))
            .unwrap_or_else(|| panic!("library.{name}"))
    };
    assert!(at("members") < at("loans") && at("loans") < at("archive"));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/library/client.py",
        "self._members: typing.Optional[MembersClient] = None\n        self._loans: typing.Optional[LoansClient] = None",
        "self._loans: typing.Optional[LoansClient] = None\n        self._members: typing.Optional[MembersClient] = None",
    );
}

/// `environment-shape`: path-item servers build the multi-URL environment; a
/// path server that is a top-level server reads `base`, and an operation's own
/// server outranks its path item's.
#[test]
fn path_item_servers_build_the_multi_url_environment() {
    let case = "environment-shape";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "src/fern/environment.py")
        .contains("def __init__(self, *, base: str, production: str, archive: str, alerts: str):"));
    assert!(read(&out, "src/fern/plates/raw_client.py")
        .contains("base_url=self._client_wrapper.get_environment().base,"));
    assert!(read(&out, "src/fern/alerts/raw_client.py")
        .contains("base_url=self._client_wrapper.get_environment().alerts,"));
    // An operation's own server outranks its path item's: `flagPlate`, under
    // the `Archive` path item, names `Alerts` and reads it.
    let plates = read(&out, "src/fern/plates/raw_client.py");
    assert_eq!(
        plates.matches("get_environment().alerts,").count(),
        2,
        "flag_plate reads its own server in the sync and async clients:\n{plates}"
    );
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/plates/raw_client.py",
        "get_environment().alerts,",
        "get_environment().base,",
    );
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/plates/raw_client.py",
        "get_environment().base,",
        "get_environment().archive,",
    );
}

/// `auth-shape`: `x-bearer-format` sends the header key as a bearer token, and
/// two additional schemes naming one header are one credential.
#[test]
fn header_keys_carry_bearer_format_and_dedupe_by_header() {
    let case = "auth-shape";
    let (_temp, out) = matching(case, "python-enums");
    let wrapper = read(&out, "src/fern/core/client_wrapper.py");
    assert!(wrapper.contains("headers[\"Authorization\"] = f\"Bearer {self.api_key}\""));
    assert_eq!(wrapper.matches("headers[\"X-Desk-Agent\"]").count(), 1);
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/core/client_wrapper.py",
        "f\"Bearer {self.api_key}\"",
        "self.api_key",
    );
}

/// `method-name-derivation`, `operation-id-tag-prefix-digit` and
/// `single-operation-tag-root-method`: one rule derives a method from an
/// operationId and its tag.
#[test]
fn one_rule_names_methods_from_operation_ids_and_tags() {
    let case = "method-name-derivation";
    let (_temp, out) = matching(case, "python-enums");
    for (rel, method) in [
        ("src/fern/ping/client.py", "ping_ping"),
        ("src/fern/app/client.py", "info"),
        ("src/fern/relay/client.py", "relay_gateway_info"),
        ("src/fern/relay/client.py", "currentstatus"),
        ("src/fern/relaygateway/client.py", "bandpricing"),
        ("src/fern/assets/client.py", "serve_robots_txt"),
        ("src/fern/assets/client.py", "list_badges_ega_page_of_them"),
        ("src/fern/client.py", "lookup"),
    ] {
        assert!(
            read(&out, rel).contains(&format!("def {method}(")),
            "{rel} lacks {method}"
        );
    }
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/ping/client.py",
        "def ping_ping(",
        "def ping(",
    );

    let case = "operation-id-tag-prefix-digit";
    let (_temp, out) = matching(case, "python-enums");
    let alias = read(&out, "src/fern/alias/client.py");
    assert!(alias.contains("def alias_val2(") && alias.contains("def alias_v3("));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/alias/client.py",
        "def alias_val2(",
        "def val2(",
    );

    let case = "single-operation-tag-root-method";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "src/fern/client.py").contains("def invoice_match("));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "README.md",
        "client.invoice_match(",
        "client.invoice_match.invoice_match(",
    );
}

/// `reserved-name-suffix`: `uuid` is `uuid_` beside a body, `dict` is `dict_`,
/// and a punctuation-only word keeps its separator (`viability (%)`).
#[test]
fn reserved_and_punctuated_names_take_fern_s_suffixes() {
    let case = "reserved-name-suffix";
    let (_temp, out) = matching(case, "python-enums");
    let packet = read(&out, "src/fern/types/packet.py");
    for field in ["viability_:", "dict_:", "moisture_:", "seed__weight:"] {
        assert!(packet.contains(field), "Packet lacks {field}");
    }
    assert_eq!(
        read(&out, "src/fern/packets/client.py")
            .matches("uuid_: str,")
            .count(),
        4,
        "the sync and async get and relabel methods each take uuid_"
    );
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/types/packet.py",
        "dict_: typing_extensions.Annotated[Glossary, FieldMetadata(alias=\"dict\"), pydantic.Field(alias=\"dict\")]",
        "dict: Glossary",
    );
}

/// `init-import-order` (ruling 7): crozier's own import order stands, and the
/// catalogued `init-type-checking-import-order` departure is what lets the
/// root `__init__.py` match.
#[test]
fn the_init_import_order_departure_absorbs_the_root_package_order() {
    let case = "init-import-order";
    for mode in ["python-enums", "literals"] {
        let (_temp, out) = matching(case, mode);
        let comparison = crozier::parity::compare_trees_with_document(
            &repo_root().join(golden(case, mode)),
            &out,
            None,
            true,
            Some(crozier::openapi::load(&spec(case)).unwrap()),
        )
        .expect("real SDK trees can be compared");
        assert!(comparison.differences.is_empty(), "{mode}: {comparison:?}");
        assert!(
            comparison.departures.iter().any(|departure| {
                departure.file == "src/fern/__init__.py"
                    && departure.id == "init-type-checking-import-order"
            }),
            "{mode}: the departure must be what absorbs the order: {comparison:?}"
        );
        regression_is_named(
            case,
            mode,
            &out,
            "src/fern/__init__.py",
            "from .yew_walk import",
            "from .yew_walks import",
        );
    }
}

/// Run the real `crozier compare` on one measurement in `mode`, against a copy
/// of `reference` that its configured reference command writes, and return the
/// JSON report and the process's exit code.
#[cfg(unix)]
fn compare_cli(case: &str, mode: &str, reference: &Path) -> (serde_json::Value, i32) {
    let temp = tempfile::tempdir().expect("config tempdir");
    let config = temp.path().join("crozier.yml");
    let quote = |path: &Path| format!("'{}'", path.display().to_string().replace('\'', "'\\''"));
    std::fs::write(
        &config,
        format!(
            "reference:\n  command: {}\ngenerators:\n  python:\n    spec: {}\n    output: ./sdk\n    enum-type: {mode}\n    package-name: fern\n    project-name: default_package_name\n",
            serde_json::to_string(&format!(
                "cp -R {}/. \"$CROZIER_REFERENCE_OUTPUT\"",
                quote(reference)
            ))
            .unwrap(),
            serde_json::to_string(&spec(case).display().to_string()).unwrap(),
        ),
    )
    .unwrap();
    let output = super::crozier_clean_env()
        .current_dir(temp.path())
        .args(["compare", "--json", "-"])
        .arg(&config)
        .output()
        .expect("crozier compare runs");
    let report = serde_json::from_slice(&output.stdout).unwrap_or_else(|e| {
        panic!(
            "{case} ({mode}): no JSON report ({e}): {}",
            String::from_utf8_lossy(&output.stderr)
        )
    });
    (report, output.status.code().unwrap_or(-1))
}

/// `init-import-order` (ruling 7) through the real `crozier compare` command:
/// with every catalogued departure applied, crozier's SDK byte-matches the
/// committed certified tree in both enum modes, and the departure that makes it
/// so is `init-type-checking-import-order` on the root `__init__.py`. A
/// certified tree whose root block names another module is a mismatch.
#[cfg(unix)]
#[test]
fn crozier_compare_byte_matches_the_init_import_order_measurement() {
    let case = "init-import-order";
    for mode in ["python-enums", "literals"] {
        let reference = repo_root().join(golden(case, mode));
        let (report, code) = compare_cli(case, mode, &reference);
        let result = &report["results"][0];
        assert_eq!(result["status"], "matched", "{mode}: {report:#}");
        assert_eq!(code, 0, "{mode}: {report:#}");
        assert_eq!(
            report["counts"],
            serde_json::json!({"matched": 1, "mismatched": 0, "could_not_check": 0})
        );
        let departures = result["comparison"]["departures"]
            .as_array()
            .expect("the departures list");
        assert!(
            departures.iter().any(|departure| {
                departure["id"] == "init-type-checking-import-order"
                    && departure["file"] == "src/fern/__init__.py"
            }),
            "{mode}: the departure must be what absorbs the order: {report:#}"
        );

        let altered = tempfile::tempdir().expect("altered reference tempdir");
        super::copy_dir(&reference, altered.path());
        let init = altered.path().join("src/fern/__init__.py");
        let text = std::fs::read_to_string(&init).unwrap();
        assert!(text.contains("from .yew_walk import"), "{mode}: {text}");
        std::fs::write(
            &init,
            text.replacen("from .yew_walk import", "from .yew_walks import", 1),
        )
        .unwrap();
        let (report, code) = compare_cli(case, mode, altered.path());
        let result = &report["results"][0];
        assert_eq!(result["status"], "mismatched", "{mode}: {report:#}");
        assert_ne!(code, 0, "{mode}: a mismatch must fail the command");
        assert_eq!(
            result["comparison"]["differing"],
            serde_json::json!(["src/fern/__init__.py"]),
            "{mode}: {report:#}"
        );
    }
}

/// `reference-section-title`: a declared multi-word tag a snake_case prefix
/// spells titles its section verbatim.
#[test]
fn a_declared_tag_titles_its_prefix_grouped_section() {
    let case = "reference-section-title";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "reference.md").contains("## Draft Filings\n"));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "reference.md",
        "## Draft Filings\n",
        "## DraftFilings\n",
    );
}

/// `R2`: a path parameter that does not declare `required: true` is optional.
#[test]
fn a_path_parameter_without_required_is_optional() {
    let case = "R2";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "src/fern/client.py").contains("site: typing.Optional[str],"));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/client.py",
        "site: typing.Optional[str],",
        "site: str,",
    );
}

/// `R10`: a discriminated union and its variants share one import statement.
#[test]
fn a_union_and_its_variants_share_one_import() {
    let case = "R10";
    for mode in ["python-enums", "literals"] {
        let (_temp, out) = matching(case, mode);
        const INIT: &str = "src/fern/types/__init__.py";
        let init = read(&out, INIT);
        assert_eq!(
            init.matches("from .payment_request_source import").count(),
            1
        );
        // The repaired block is Fern's as written, so no departure explains
        // it; the pre-repair split leans on `init-type-checking-import-order`.
        let departed = |out: &Path| {
            crozier::parity::compare_trees_with_document(
                &repo_root().join(golden(case, mode)),
                out,
                None,
                true,
                Some(crozier::openapi::load(&spec(case)).unwrap()),
            )
            .expect("real SDK trees can be compared")
            .departures
            .iter()
            .any(|departure| departure.file == INIT)
        };
        assert!(
            !departed(&out),
            "{mode}: the repaired block needs no departure"
        );
        let variants = init
            .lines()
            .find(|line| line.contains("from .payment_request_source import"))
            .expect("the union's import")
            .to_string();
        let (head, names) = variants.split_once(" import ").unwrap();
        let (union, wrappers) = names.split_once(", ").unwrap();
        let card = init
            .lines()
            .find(|line| line.contains("from .payment_request_source_card import"))
            .expect("the card member's import")
            .to_string();
        let pre_repair = init
            .replacen(&variants, &format!("{head} import {union}"), 1)
            .replacen(&card, &format!("{card}\n{head} import {wrappers}"), 1);
        std::fs::write(out.join(INIT), pre_repair).unwrap();
        assert!(
            departed(&out),
            "{mode}: the pre-repair split differs from Fern's block"
        );
    }
}

/// `R12`: a body naming an `x-fern-ignore` component keeps its operation, typed
/// `typing.Any`.
#[test]
fn a_body_naming_an_ignored_component_is_typed_any() {
    let case = "R12";
    let (_temp, out) = matching(case, "python-enums");
    let client = read(&out, "src/fern/snippets/client.py");
    assert!(client.contains("request: typing.Any,"));
    assert!(client.contains("request: typing.Sequence[typing.Any],"));
    let text = read(&out, "src/fern/snippets/client.py");
    std::fs::remove_file(out.join("src/fern/snippets/client.py")).unwrap();
    let found = failures(case, "python-enums", &out);
    assert!(
        found
            .iter()
            .any(|failure| failure.contains("src/fern/snippets/client.py")),
        "a missing group client must be named: {found:?}"
    );
    std::fs::write(out.join("src/fern/snippets/client.py"), text).unwrap();
}

/// `R16`: a group named `core` keeps the runtime's `core/__init__.py` and
/// imports the runtime as siblings.
#[test]
fn a_core_group_shares_the_runtime_package() {
    let case = "R16";
    let (_temp, out) = matching(case, "python-enums");
    assert!(read(&out, "src/fern/core/__init__.py").contains("\"ApiError\": \".api_error\""));
    assert!(read(&out, "src/fern/core/raw_client.py")
        .contains("from .client_wrapper import AsyncClientWrapper, SyncClientWrapper"));
    regression_is_named(
        case,
        "python-enums",
        &out,
        "src/fern/core/raw_client.py",
        "from .client_wrapper import",
        "from ..core.client_wrapper import",
    );
}

/// `R18`, already matching at this node's base (corpus row 3479's repair):
/// required `content-length` and `x-forwarded-for` headers are no arguments.
#[test]
fn required_framing_headers_are_no_arguments() {
    let case = "R18";
    let (_temp, out) = matching(case, "python-enums");
    // The one other required header rides the client wrapper; neither framing
    // header reaches a constructor or a method.
    assert!(read(&out, "src/fern/core/client_wrapper.py").contains("headers[\"x-channel\"]"));
    for rel in ["src/fern/client.py", "src/fern/orders/client.py"] {
        let client = read(&out, rel);
        assert!(
            !client.contains("content_length") && !client.contains("forwarded_for"),
            "{rel} takes a framing header"
        );
    }
}

// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
