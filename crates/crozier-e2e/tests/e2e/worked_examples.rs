//! The worked-example, example-validity and documentation-rendering tickets
//! of #966, each settled against a from-scratch document under [`DIR`] and the
//! certified pair's complete tree for it (Fern CLI 5.216.0, fern-python-sdk
//! 5.42.0), in both enum modes.
//!
//! Every case runs the real binary, compares its SDK with the certified tree
//! file for file under the departures ledger, and asserts the bytes each ticket
//! decides in the generated file it decides them in.

use std::path::Path;

use super::union_inheritance::{
    enum_failures_in, generate_in, literals_failures_in, literals_tree_in,
};
use super::{python_env_with, repo_root};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/worked-examples";

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey below generates one small SDK per case and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// A ticket's characteristic bytes: `(ticket, file, bytes crozier writes)`.
type Check = (&'static str, &'static str, &'static str);

/// Generate `case` in both enum modes, hold each SDK whole to its certified
/// tree, and assert every check's bytes in the python-enums SDK.
fn holds(case: &str, checks: &[Check]) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate_in(DIR, case, "python-enums", &out);
    let mut failures = enum_failures_in(DIR, case, &out);
    for (ticket, file, bytes) in checks {
        let written = std::fs::read_to_string(out.join(file))
            .unwrap_or_else(|error| panic!("{ticket} {case}: {file}: {error}"));
        if !written.contains(bytes) {
            failures.push(format!(
                "{ticket} {case}: {file} lacks {bytes:?}:\n{written}"
            ));
        }
    }
    let literals = temp.path().join("literals");
    generate_in(DIR, case, "literals", &literals);
    failures.extend(literals_failures_in(DIR, case, &literals));
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// #540: a README or `reference.md` worked argument that is a map of two or
/// more pairs puts each pair on its own line whatever its value type, while a
/// one-pair map stays on the argument's line.
#[test]
fn documentation_maps_spread_every_pair() {
    holds(
        "numeric-dict-pairs",
        &[
            (
                "#540",
                "README.md",
                "    position={\n        \"lat\": 41.5,\n        \"lon\": -70.25\n    },",
            ),
            (
                "#540",
                "README.md",
                "    toggles={\n        \"lamp\": True,\n        \"horn\": False\n    },",
            ),
            ("#540", "README.md", "    offset={\n        \"dx\": 3\n    },"),
        ],
    );
}

/// #927: a placeholder map item of a list inside a README worked argument is
/// spread one pair per line, as `reference.md` writes it.
#[test]
fn readme_list_map_items_spread_as_the_reference_does() {
    holds(
        "readme-list-map-items",
        &[(
            "#927",
            "README.md",
            "    notes=[\n        {\n            \"key\": \"value\"\n        }\n    ],",
        )],
    );
}
/// #928: a fenced root docstring with no line ending in a backslash leaves its
/// blank lines empty; one with such a line keeps them indented, as ruff leaves
/// a docstring it cannot reflow.
#[test]
fn fenced_docstrings_leave_blank_lines_empty_unless_a_line_continues() {
    holds(
        "fenced-docstring-blanks",
        &[
            (
                "#928",
                "src/fern/client.py",
                "        notice = client.list_notices()\n\n        print(notice)\n",
            ),
            (
                "#928",
                "src/fern/client.py",
                "          --data-urlencode 'since=2020-01-01'\n        \n        echo done\n",
            ),
        ],
    );
}

/// #929: a tab in a property description is a `\t` escape inside its
/// `pydantic.Field(description=…)` literal, while the docstring beside it keeps
/// the four spaces Fern's writer puts for a tab.
#[test]
fn field_description_literals_escape_their_tabs() {
    holds(
        "field-description-tabs",
        &[
            (
                "#929",
                "src/fern/types/permit.py",
                "description=\"Exemption codes - Code\\tReason 1.\\tResident 2.\\tVisitor\")",
            ),
            (
                "#929",
                "src/fern/types/permit.py",
                "    Exemption codes - Code    Reason 1.    Resident 2.    Visitor\n",
            ),
        ],
    );
}

/// #930: a keep-chomped (`|+`) description keeps its trailing blank line where
/// it documents the argument of a body schema used only as that body, and is
/// trimmed where the schema is also a model.
#[test]
fn kept_description_blank_lines_follow_the_body_schema() {
    holds(
        "kept-blank-descriptions",
        &[
            (
                "#930",
                "src/fern/client.py",
                "            A free remark.\n\n\n        tide : typing.Optional[float]",
            ),
            (
                "#930",
                "src/fern/client.py",
                "                Give it as a basin name or a pontoon range.\n\n        depth : typing.Optional[int]",
            ),
        ],
    );
}

/// #931: a property restating a described parent field by a bare `$ref` is
/// documented by its own (absent) description, and a required typeless inline
/// body property documents nothing; the optional typeless control keeps its own.
#[test]
fn restated_and_typeless_fields_use_their_own_descriptions() {
    holds(
        "restated-reference-descriptions",
        &[
            (
                "#931",
                "src/fern/types/berth_linked.py",
                "    outline: typing.Optional[Outline] = None\n",
            ),
            (
                "#931",
                "src/fern/client.py",
                "        position : typing.Any\n\n        size : str",
            ),
            (
                "#931",
                "src/fern/client.py",
                "        colour : typing.Optional[typing.Any]\n            Its colour, if painted",
            ),
        ],
    );
}

/// #864: a worked example's string escapes are doubled in the docstring, so the
/// call Python's `help()` shows is the call the README writes (the
/// `docstring-example-escapes` departure).
#[test]
fn docstring_examples_keep_their_string_escapes() {
    holds(
        "docstring-example-escapes",
        &[(
            "#864",
            "src/fern/client.py",
            "            entry='Moored at dawn.\\\\nWind\\\\tNE 12 kn, \"steady\"',",
        )],
    );
}

/// #541: an enum example narrowed by a dropped `allOf` member's constraints
/// takes the first member they admit; #960: so does an enum whose own pattern
/// and length reject its first member (the `pattern-narrowed-enum-example`
/// departure).
#[test]
fn narrowed_enum_examples_take_a_member_the_constraints_admit() {
    holds(
        "composed-enum-constraints",
        &[("#541", "src/fern/client.py", "            state=ParcelState.STAMPED,")],
    );
    holds(
        "inline-enum-constraints",
        &[
            ("#960", "src/fern/client.py", "            window=PassageWindow.EBB,"),
            ("#960", "src/fern/client.py", "            tide=BookMooringRequestTide.EBB,"),
        ],
    );
}

/// #937: a `format: date` property's declared unquoted YAML date is its worked
/// value, the `2000-01-23` sentinel included (the
/// `declared-timestamp-property-example` departure), and a quoted `date`
/// component example is the path argument's value, as the certified pair
/// writes it.
#[test]
fn declared_dates_are_the_worked_values() {
    holds(
        "declared-date-examples",
        &[
            (
                "#937",
                "src/fern/client.py",
                "            sailed_on=datetime.date.fromisoformat(\n                \"2031-04-02\",\n            ),",
            ),
            (
                "#937",
                "src/fern/client.py",
                "            checked_on=datetime.date.fromisoformat(\n                \"2000-01-23\",\n            ),",
            ),
            (
                "#937",
                "src/fern/client.py",
                "            day=datetime.date.fromisoformat(\n                \"2031-06-21\",\n            ),",
            ),
        ],
    );
}

/// #933: a docstring constructor for an `allOf` of two `$ref`s lists the later
/// member's fields first; an `allOf` of a `$ref` and an inline member keeps
/// declaration order.
#[test]
fn reference_compositions_list_the_later_member_first() {
    holds(
        "composed-reference-order",
        &[
            (
                "#933",
                "src/fern/orders/client.py",
                "            buyer=Buyer(\n                pier=\"pier\",\n                slip=1,\n                name=\"name\",\n                phone=\"phone\",\n            ),",
            ),
            (
                "#933",
                "src/fern/orders/client.py",
                "            terms=Terms(\n                kind=\"kind\",\n                due_on=\"due_on\",\n            ),",
            ),
        ],
    );
}

/// #935: an undiscriminated union whose first member declares no example is
/// worked from the first member that does.
#[test]
fn union_examples_take_the_member_declaring_one() {
    holds(
        "union-example-member",
        &[(
            "#935",
            "src/fern/watches/client.py",
            "            trigger=TideTrigger(\n                station=\"harbour-mouth\",\n                height_m=2.5,\n            ),",
        )],
    );
}

/// #891: an operation whose importer builds no example passes no optional body,
/// while a required body and one beside a resolved response keep theirs.
#[test]
fn unexampled_operations_omit_their_optional_bodies() {
    holds(
        "unresolved-response-optional-body",
        &[
            ("#891", "src/fern/firings/client.py", "        client.firings.plan_firing()\n"),
            (
                "#891",
                "src/fern/firings/client.py",
                "        client.firings.record_firing(\n            request={\"key\": \"value\"},\n        )",
            ),
        ],
    );
}

/// #932: an optional query array of enum items is left out of the worked call,
/// a plain string array keeps its item example, and a required enum array is
/// passed.
#[test]
fn optional_enum_query_arrays_are_left_out_of_worked_calls() {
    holds(
        "optional-enum-query-arrays",
        &[
            (
                "#932",
                "src/fern/glazes/client.py",
                "        client.glazes.list_glazes(\n            palette=[\"celadon\"],\n        )",
            ),
            (
                "#932",
                "src/fern/glazes/client.py",
                "        client.glazes.list_required_glazes(\n            finish=[Finish.SATIN],\n        )",
            ),
        ],
    );
}

/// #934: where a shared `$ref` body's duplicate operation collapses, crozier's
/// `reference.md` lists the flattened arguments its methods take, in signature
/// order, where the certified pair lists a `request` it puts ahead of the query
/// parameters (the `request-alias-reference-parameters` departure).
#[test]
fn reference_lists_the_flattened_body_after_the_queries() {
    holds(
        "alias-body-reference-order",
        &[(
            "#934",
            "reference.md",
            "**crew_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` \n    \n</dd>\n</dl>\n\n<dl>\n<dd>\n\n**title:** `typing.Optional[str]` ",
        )],
    );
}

/// #936: typeless body values keep every argument the signature requires (the
/// `typeless-body-required-arguments` departure), and a required nullable
/// typeless field is left out of the docstring's call.
#[test]
fn typeless_body_values_keep_required_arguments() {
    holds(
        "typeless-body-values",
        &[
            (
                "#936",
                "src/fern/locker/client.py",
                "        client.locker.update_annotations(\n            locker_id=\"lockerId\",\n            data={\"key\": \"value\"},\n        )",
            ),
            (
                "#936",
                "src/fern/locker/client.py",
                "        client.locker.create_workspace(\n            kind=\"kind\",\n        )",
            ),
        ],
    );
}

/// #945 and #947: list, map and union path parameters keep crozier's worked
/// values that bind to the signature (the `list-path-parameter-example`
/// departure), and the README anchors on the first operation the certified pair
/// can work.
#[test]
fn composite_path_parameters_keep_valid_worked_values() {
    holds(
        "composite-path-parameters",
        &[
            (
                "#947",
                "src/fern/berths/client.py",
                "        client.berths.get_berth(\n            berth=SlipKey(\n                slip=\"slip\",\n            ),\n        )",
            ),
            (
                "#945",
                "src/fern/berths/client.py",
                "        client.berths.get_hulls(\n            hull_ids=[\"hullIds\"],\n        )",
            ),
            (
                "#945",
                "src/fern/berths/client.py",
                "        client.berths.get_tides(\n            marks={\"key\": \"value\"},\n        )",
            ),
            ("#947", "README.md", "client.berths.get_hulls(\n"),
        ],
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project, which AGENTS.md promotes out of the affected tier into its own required CI leg, so no unrelated edit newly triggers it; `#[ignore]` is the one mechanism crates/crozier-e2e/AGENTS.md gives for routing a journey there.
/// Every worked call each measurement's crozier SDK documents, in both enum
/// modes, binds to that SDK's signatures under pyright, where the certified
/// trees' calls the departures correct do not (a missing required argument, a
/// list or map passed a string, a string passed to bytes, an escape evaluated
/// into a broken literal); and each repaired value validates against its source
/// schema with `validate.py` (`docs/departures/evidence/invalid-example-values/`)
/// where Fern's is rejected, while a declared date and Fern's placeholder both
/// validate.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_worked_examples_bind_and_their_repaired_values_validate() {
    let python = python_env_with(
        "crozier-worked-examples-typecheck",
        &["httpx", "pydantic", "pytest", "pyright==1.1.414", "jsonschema==4.26.0", "PyYAML==6.0.3"],
    )
    .expect("an environment holding pyright, jsonschema and PyYAML");
    let root = repo_root();
    let checker = root.join("crates/crozier-e2e/tests/e2e/worked_examples_typecheck.py");
    let check = |tree: &Path| {
        std::process::Command::new(&python)
            .arg(&checker)
            .arg(tree)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .expect("run the worked-example type check")
    };
    let temp = tempfile::tempdir().expect("output tempdir");
    let mut cases: Vec<String> = std::fs::read_dir(root.join(DIR))
        .expect("the measurements")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().join("fern-expected").is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .collect();
    cases.sort();
    assert!(cases.len() >= 17, "{cases:?}");
    for case in &cases {
        for mode in ["python-enums", "literals"] {
            let out = temp.path().join(format!("{case}-{mode}"));
            generate_in(DIR, case, mode, &out);
            let run = check(&out);
            assert!(
                run.status.success(),
                "{case} ({mode}): {}{}",
                String::from_utf8_lossy(&run.stdout),
                String::from_utf8_lossy(&run.stderr)
            );
        }
    }
    let multipart = "docs/fern-measurements/bodies-responses";
    let out = temp.path().join("multipart-binary-required-part");
    generate_in(multipart, "multipart-binary-required-part", "python-enums", &out);
    assert!(check(&out).status.success(), "the required binary part's calls bind");
    for (dir, case, says) in [
        (DIR, "composite-path-parameters", "error"),
        (DIR, "docstring-example-escapes", "error"),
        (DIR, "typeless-body-values", "missing for parameter"),
        (multipart, "multipart-binary-required-part", "FormFile"),
    ] {
        let run = check(&root.join(dir).join(case).join("fern-expected"));
        let stdout = String::from_utf8_lossy(&run.stdout);
        assert_eq!(run.status.code(), Some(1), "{case}: {stdout}");
        assert!(stdout.contains(says), "{case}: {stdout}");
    }
    // A root without a generated package documents nothing to check.
    assert_eq!(check(&root.join(DIR)).status.code(), Some(2));

    let validator = root.join("docs/departures/evidence/invalid-example-values/validate.py");
    let line_of = |file: &Path, argument: &str| {
        let text = std::fs::read_to_string(file).expect("a generated client");
        let number = text
            .lines()
            .position(|line| line.trim_start().starts_with(&format!("{argument}=")))
            .unwrap_or_else(|| panic!("{} passes no {argument}=", file.display()));
        format!("{}:{}", file.display(), number + 1)
    };
    for (case, mode, pointer, argument, code, says) in [
        ("composed-enum-constraints", "literals", "/components/schemas/Parcel/properties/state", "state", 0, "crozier state='stamped': accepted"),
        ("inline-enum-constraints", "literals", "/components/schemas/Passage/properties/window", "window", 0, "crozier window='ebb': accepted"),
        ("inline-enum-constraints", "literals", "/paths/~1moorings/post/requestBody/content/application~1json/schema/properties/tide", "tide", 0, "crozier tide='ebb': accepted"),
        ("declared-date-examples", "python-enums", "/components/schemas/Voyage/properties/sailed_on", "sailed_on", 1, "crozier sailed_on='2031-04-02': accepted"),
        ("declared-date-examples", "python-enums", "/components/schemas/Voyage/properties/checked_on", "checked_on", 1, "crozier checked_on='2000-01-23': accepted"),
    ] {
        let crozier = temp.path().join(format!("{case}-{mode}")).join("src/fern/client.py");
        // The literals tree is the base laid under its overlay, built for the run.
        let literals = (mode == "literals").then(|| literals_tree_in(DIR, case).0);
        let fern = literals
            .as_ref()
            .map_or_else(|| root.join(DIR).join(case).join("fern-expected"), |tree| tree.path().to_path_buf())
            .join("src/fern/client.py");
        let run = std::process::Command::new(&python)
            .arg(&validator)
            .arg(root.join(DIR).join(case).join("openapi.yml"))
            .arg(pointer)
            .arg(line_of(&fern, argument))
            .arg(line_of(&crozier, argument))
            .arg(argument)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .expect("run the example validator");
        let stdout = String::from_utf8_lossy(&run.stdout);
        assert_eq!(run.status.code(), Some(code), "{case} {argument}: {stdout}{}", String::from_utf8_lossy(&run.stderr));
        assert!(stdout.contains(says), "{case} {argument}: {stdout}");
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
