//! The type-lowering tickets of #965 (#438, #539, #889, #893–#902, #904–#912,
//! #925, #949), each settled against a from-scratch document under [`DIR`] and
//! the certified pair's complete tree for it (Fern CLI 5.216.0,
//! fern-python-sdk 5.42.0), in both enum modes.
//!
//! Every case runs the real binary, compares its SDK with the certified tree
//! file for file under the departures ledger, and asserts the bytes each ticket
//! decides in the generated file it decides them in.

use super::union_inheritance::{enum_failures_in, generate_in, literals_failures_in};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/type-lowering";

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

/// #438: a 3.1 `type: [T, "null"]` member keeps its nullability in a hoisted
/// query-parameter union alias, as the 3.0 `nullable: true` member does.
#[test]
fn parameter_union_members_keep_their_type_array_nullability() {
    holds(
        "parameter-member-nullability",
        &[
            (
                "#438",
                "src/fern/types/list_beacons_request_range.py",
                "ListBeaconsRequestRange = typing.Union[typing.Optional[str], int]",
            ),
            (
                "#438",
                "src/fern/types/list_beacons_request_weight.py",
                "ListBeaconsRequestWeight = typing.Union[str, typing.Optional[int]]",
            ),
        ],
    );
}

/// #899: an `anyOf` mapping over members whose tags declare `type: string` is
/// honoured, an unrequired tag and a member mapped twice included, while one
/// over untyped `enum` tags stays a plain union. #900: a lone `$ref` under a
/// discriminator mapping nothing is its target; a mapped lone member stays a
/// one-variant union.
#[test]
fn any_of_mappings_and_lone_references_match_the_certified_pair() {
    holds(
        "anyof-discriminators",
        &[
            (
                "#899",
                "src/fern/types/lock_sensor.py",
                "typing.Union[LockSensor_LevelUpstream, LockSensor_LevelDownstream, LockSensor_Flow]",
            ),
            (
                "#899",
                "src/fern/types/lock_paddle.py",
                "LockPaddle = typing.Union[ManualPaddle, PoweredPaddle]",
            ),
            (
                "#900",
                "src/fern/types/lock.py",
                "warden: typing.Optional[Lockkeeper] = pydantic.Field(default=None)",
            ),
            (
                "#900",
                "src/fern/types/lock_relief.py",
                "class LockRelief_Volunteer(UniversalBaseModel):",
            ),
        ],
    );
}

/// #910: a variant-only member drops its `const` tag whatever the tag's value
/// (`message`, `tool`, `approval`), as Letta's golden keeps only the tags of
/// members it also uses on their own. #911: a mapping-less discriminator over
/// bare `const` tags leaves a plain union whose members keep their tag enums,
/// where one over typed one-value enums (Tally's `Block`) discriminates.
#[test]
fn const_tags_are_stripped_and_discriminated_by_the_schema() {
    holds(
        "const-discriminator-tags",
        &[
            (
                "#910",
                "src/fern/types/message_item.py",
                "class MessageItem(UniversalBaseModel):\n    text: str",
            ),
            (
                "#910",
                "src/fern/types/approval_envelope.py",
                "class ApprovalEnvelope(UniversalBaseModel):\n    approved: bool",
            ),
            (
                "#911",
                "src/fern/types/event.py",
                "Event = typing.Union[EventVesselArrived, EventVesselDeparted]",
            ),
            (
                "#911",
                "src/fern/types/event_vessel_arrived.py",
                "type: EventVesselArrivedType",
            ),
            (
                "#911",
                "src/fern/types/signal.py",
                "pydantic.Field(discriminator=\"type\")",
            ),
        ],
    );
}

/// #912: unrequired plain string `type` tags with examples discriminate. #925:
/// a tag named `schema` is the escaped `schema_` field of every variant, and
/// the discriminator names that field: the certified pair's wire name fails to
/// import (the `escaped-discriminator-field-name` departure).
#[test]
fn inferred_tags_discriminate_and_name_the_variant_field() {
    holds(
        "inferred-discriminator-tags",
        &[
            (
                "#912",
                "src/fern/types/store_item_wearable.py",
                "typing.Union[StoreItemWearable_TShirt, StoreItemWearable_Jacket]",
            ),
            (
                "#925",
                "src/fern/types/query_response.py",
                "pydantic.Field(discriminator=\"schema_\")",
            ),
        ],
    );
}

/// #539: a recursive JSON alias is named under pydantic v2 and bounded at
/// `typing.Any` under v1 (the `recursive-alias-named-type` departure).
#[test]
fn recursive_json_aliases_are_named() {
    holds(
        "recursive-json-alias",
        &[(
            "#539",
            "src/fern/types/json_value.py",
            "elif IS_PYDANTIC_V2:\n    JsonValue = typing_extensions.TypeAliasType(",
        )],
    );
}

/// #539 and #925 at runtime: crozier's generated modules import, and construct
/// a value through the recursive alias and the escaped-tag union, under both
/// Pydantic majors the SDK declares, where the certified pair's modules fail to
/// import or never finish. Run by `just test-sdk-env`.
#[test]
#[ignore = "SDK Python-environment tier (builds venvs from PyPI); run via `just test-sdk-env`"]
fn sdk_env_escaped_discriminators_and_recursive_aliases_import() {
    let script = super::repo_root().join("docs/departures/evidence/generated-model-imports.py");
    let cases = [
        (
            "recursive-json-alias",
            "fern.types:Signal",
            r#"{"id": "a", "payload": {"k": [1, "x", null, {"n": true}]}, "history": [[1, 2], "y"], "labels": {"l": {"m": [3]}}}"#,
        ),
        (
            "inferred-discriminator-tags",
            "fern.types:QueryResponse",
            r#"{"schema": "store.status.v1", "scope_id": "s", "status": "ready"}"#,
        ),
    ];
    let envs = [
        (
            "pydantic 2",
            super::runtime_python_env().expect("SDK runtime environment"),
        ),
        (
            "pydantic 1",
            super::pydantic_v1_python_env().expect("pydantic v1 environment"),
        ),
    ];
    let run = |python: &std::path::Path,
               root: &std::path::Path,
               target: &str,
               payload: &str,
               expect: &str| {
        let output = std::process::Command::new(python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(root)
            .args([target, payload, expect])
            .output()
            .expect("run the evidence script");
        (
            output.status.code(),
            String::from_utf8_lossy(&output.stdout).trim().to_string(),
        )
    };
    let temp = tempfile::tempdir().expect("output tempdir");
    for (case, target, payload) in cases {
        let ours = temp.path().join(case);
        generate_in(DIR, case, "python-enums", &ours);
        let fern = super::repo_root()
            .join(DIR)
            .join(case)
            .join("fern-expected/src");
        for (label, python) in &envs {
            let (code, said) = run(python, &fern, target, payload, "invalid");
            assert_eq!(
                code,
                Some(0),
                "{case} {label}: the certified tree must fail: {said}"
            );
            let (code, said) = run(python, &ours.join("src"), target, payload, "valid");
            // Under pydantic 1 the escaped-tag union imports, but the shared
            // runtime core's key renaming hides its wire tag (a drafted
            // follow-up), so only its import is held there.
            if case == "inferred-discriminator-tags" && *label == "pydantic 1" {
                assert!(
                    said.contains("\"failed\": \"ValidationError\""),
                    "{case} {label}: {said}"
                );
            } else {
                assert_eq!(
                    code,
                    Some(0),
                    "{case} {label}: crozier's tree must construct: {said}"
                );
            }
        }
    }
    // A root holding no generated package is a usage error.
    let (code, _) = run(&envs[0].1, temp.path(), "fern.types:Signal", "{}", "valid");
    assert_eq!(code, Some(2));
}

/// #949: the members of a discriminated union composed as an `allOf` member
/// keep their tag, since the union is flattened into the composing model.
/// #909: a later `allOf` parent restating an earlier one's tag leaves the
/// earlier, undocumented field.
#[test]
fn inherited_tags_stay_on_flattened_subtypes() {
    holds(
        "inherited-discriminator-tags",
        &[
            (
                "#949",
                "src/fern/types/cat.py",
                "class Cat(UniversalBaseModel):\n    species: str",
            ),
            (
                "#949",
                "src/fern/types/dog.py",
                "class Dog(UniversalBaseModel):\n    species: str",
            ),
            (
                "#909",
                "src/fern/types/grooming_task.py",
                "class GroomingTask(UniversalBaseModel):\n    action: str\n    id: str",
            ),
        ],
    );
}

/// #901: a nullable array component of inline enum items keeps `Optional`.
/// #904: `nullable` left beside an empty composition in an `allOf` does not
/// make the composed model nullable where it is used.
#[test]
fn nullable_components_keep_and_lose_optional_as_declared() {
    holds(
        "nullable-components",
        &[
            (
                "#901",
                "src/fern/types/response_modalities.py",
                "ResponseModalities = typing.Optional[typing.List[ResponseModalitiesItem]]",
            ),
            (
                "#904",
                "src/fern/client.py",
                "queries: typing.Sequence[FeedbackQuery],",
            ),
        ],
    );
}
