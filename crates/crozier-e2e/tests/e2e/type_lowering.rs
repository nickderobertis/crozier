//! The type-lowering tickets of #965 (#438, #539, #889, #893–#902, #904–#912,
//! #925, #949) and of #994 (#982, #984), each settled against a from-scratch
//! document under [`DIR`] and the certified pair's complete tree for it (Fern
//! CLI 5.216.0, fern-python-sdk 5.42.0), in both enum modes.
//!
//! Every case runs the real binary, compares its SDK with the certified tree
//! file for file under the departures ledger, and asserts the bytes each ticket
//! decides in the generated file it decides them in.

use super::union_inheritance::{enum_failures_in, generate_in, literals_failures_in};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/type-lowering";

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
/// `typing.Any` under v1 (the `recursive-alias-named-type` departure), and one
/// naming a model that refers back to it imports that model for type checkers
/// only, as the certified module does.
#[test]
fn recursive_json_aliases_are_named() {
    holds(
        "recursive-json-alias",
        &[
            (
                "#539",
                "src/fern/types/json_value.py",
                "elif IS_PYDANTIC_V2:\n    JsonValue = typing_extensions.TypeAliasType(",
            ),
            (
                "#539",
                "src/fern/types/tree.py",
                "if typing.TYPE_CHECKING:\n    from .node import Node\nif typing.TYPE_CHECKING:\n    Tree = ",
            ),
        ],
    );
}

/// #539 extended to a cycle made only of aliases (`JsonValueOutput`, a union of
/// `JsonArrayOutput` and `JsonObjectOutput`, each holding it): the alias that
/// closes the cycle is named, and a model reaching the cycle through another is
/// repaired as the certified module repairs it.
#[test]
fn recursive_alias_cycles_are_named() {
    holds(
        "recursive-alias-cycle",
        &[
            (
                "#539",
                "src/fern/types/json_value_output.py",
                "elif IS_PYDANTIC_V2:\n    JsonValueOutput = typing_extensions.TypeAliasType(",
            ),
            (
                "#539",
                "src/fern/types/run_summary.py",
                "update_forward_refs(RunSummary)",
            ),
        ],
    );
}

/// #539 and #925 at runtime: crozier's generated modules import, and construct
/// a value through the recursive alias, the alias cycle and the escaped-tag union, under both
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
            r#"{"id": "a", "payload": {"k": [1, "x", null, {"n": true}]}, "history": [[1, 2], "y"], "labels": {"l": {"m": [3]}}, "tree": ["leaf", {"name": "n", "children": ["x", ["y"]]}]}"#,
        ),
        (
            "recursive-alias-cycle",
            "fern.types:RunSummary",
            r#"{"report": {"engine": "e", "inference_diagnostics": {"a": [1, "x", null, {"b": [true]}], "c": {"d": 2.5}}}, "label": "l"}"#,
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
        // stderr rides along in every message: a usage error (exit 2) says why
        // there and nowhere else.
        (
            output.status.code(),
            format!(
                "{} [stderr: {}]",
                String::from_utf8_lossy(&output.stdout).trim(),
                String::from_utf8_lossy(&output.stderr).trim()
            ),
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
                assert_eq!(code, Some(1), "{case} {label}: {said}");
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
                // The opposite expectations are mismatches, which exit 1.
                let (code, said) = run(python, &ours.join("src"), target, payload, "invalid");
                assert_eq!(code, Some(1), "{case} {label}: {said}");
                let (code, said) = run(python, &fern, target, payload, "valid");
                assert_eq!(code, Some(1), "{case} {label}: {said}");
            }
        }
    }
    // A root holding no generated package, a malformed target or payload, and a
    // child interpreter that dies without reporting an outcome are usage errors,
    // never an expected SDK failure.
    let python = &envs[0].1;
    let ours = temp.path().join("recursive-json-alias").join("src");
    assert_eq!(
        run(python, temp.path(), "fern.types:Signal", "{}", "invalid").0,
        Some(2)
    );
    assert_eq!(run(python, &ours, "fern.types", "{}", "invalid").0, Some(2));
    assert_eq!(
        run(python, &ours, "fern.types:Signal", "{", "invalid").0,
        Some(2)
    );
    // A child whose package behaves as `init` does on import: its outcome, if
    // any, decides the exit for an `invalid` expectation.
    let child = |label: &str, init: &str| {
        let root = temp.path().join(label);
        std::fs::create_dir_all(root.join("fern")).expect("mkdir");
        std::fs::write(root.join("fern/__init__.py"), init).expect("write");
        run(python, &root, "fern.types:Signal", "{}", "invalid")
    };
    let exits = "import os, sys\nsys.stdout.flush()\nos._exit(0)\n";
    for (label, init) in [
        ("exits-with-an-error", "raise SystemExit(3)\n".to_string()),
        ("reports-nothing", exits.to_string()),
        ("reports-no-json", format!("print('not json')\n{exits}")),
        (
            "reports-another-shape",
            format!("print('{{\"pydantic\": \"2\", \"other\": 1}}')\n{exits}"),
        ),
    ] {
        assert_eq!(
            child(label, &init).0,
            Some(2),
            "{label}: no outcome is a usage error"
        );
    }
    // Death by a signal is the import's own failure, as a stack overflow is.
    // Windows has no signals: an overflow ends the process with the NTSTATUS
    // 0xC00000FD, which `ExitProcess` reproduces as the parent sees it.
    let (crash, reported) = if cfg!(windows) {
        (
            "import ctypes\nctypes.windll.kernel32.ExitProcess(0xC00000FD)\n",
            "killed by exception 0xC00000FD",
        )
    } else {
        (
            "import os, signal\nos.kill(os.getpid(), signal.SIGSEGV)\n",
            "killed by signal 11",
        )
    };
    let (code, said) = child("killed-by-a-crash", crash);
    assert_eq!(code, Some(0), "{said}");
    assert!(said.contains(reported), "{said}");
    // An import that outgrows the child's 4 GiB address space fails as
    // `MemoryError`, as pydantic 1 expanding a recursive alias does, rather
    // than growing until it takes the host down. Linux enforces the bound;
    // elsewhere this allocation would really happen, so it is asked only here.
    if cfg!(target_os = "linux") {
        let (code, said) = child("outgrows-memory", "bytearray(8 * 1024**3)\n");
        assert_eq!(code, Some(0), "{said}");
        assert!(said.contains(r#""failed": "MemoryError""#), "{said}");
    }
    // A child that never reports within the limit is the import's own failure,
    // as pydantic 1 expanding a recursive alias without end is: under a one
    // second limit, an import that sleeps ten is stopped and reported.
    let sleeper = temp.path().join("never-finishes");
    std::fs::create_dir_all(sleeper.join("fern")).expect("mkdir");
    std::fs::write(
        sleeper.join("fern/__init__.py"),
        "import time\ntime.sleep(10)\n",
    )
    .expect("write");
    let limited = |limit: &str, expect: &str| {
        let output = std::process::Command::new(python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .env("GENERATED_MODEL_IMPORTS_LIMIT_SECONDS", limit)
            .arg(&script)
            .arg(&sleeper)
            .args(["fern.types:Signal", "{}", expect])
            .output()
            .expect("run the evidence script");
        (
            output.status.code(),
            String::from_utf8_lossy(&output.stdout).trim().to_string(),
            String::from_utf8_lossy(&output.stderr).trim().to_string(),
        )
    };
    let (code, said, stderr) = limited("1", "invalid");
    assert_eq!(code, Some(0), "{said} [stderr: {stderr}]");
    assert_eq!(said, r#"{"failed": "no result within 1s"}"#, "{stderr}");
    let (code, said, stderr) = limited("1", "valid");
    assert_eq!(code, Some(1), "{said} [stderr: {stderr}]");
    // A limit that is no positive whole number of seconds is a usage error,
    // refused before any child starts.
    for limit in ["0", "-1", "1.5", "soon", "\u{b2}", "01"] {
        let (code, _said, stderr) = limited(limit, "invalid");
        assert_eq!(code, Some(2), "{limit}: {stderr}");
        assert!(
            stderr.contains("GENERATED_MODEL_IMPORTS_LIMIT_SECONDS"),
            "{limit}: {stderr}"
        );
    }
    let usage = |args: &[&str]| {
        std::process::Command::new(python)
            .arg(&script)
            .args(args)
            .output()
            .expect("run the evidence script")
            .status
            .code()
    };
    assert_eq!(usage(&[]), Some(2));
    let root = ours.display().to_string();
    assert_eq!(usage(&[&root, "fern.types:Signal", "{}", "maybe"]), Some(2));
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
                "src/fern/feedback/raw_client.py",
                "queries: typing.Sequence[FeedbackQuery],",
            ),
        ],
    );
}

/// #893: a JSON `format: binary` string is `bytes` as a scalar and `str` as an
/// array item or map value. #894: a `contentEncoding: base64` string beside
/// `null` is `bytes`, where a bare one and an array of them stay `str`.
#[test]
fn json_binary_and_base64_strings_take_the_certified_types() {
    holds(
        "json-binary-strings",
        &[
            (
                "#893",
                "src/fern/types/contact_sheet.py",
                "frames: typing.Optional[typing.List[str]] = None",
            ),
            (
                "#893",
                "src/fern/types/contact_sheet.py",
                "layers: typing.Optional[typing.Dict[str, str]] = None",
            ),
            ("#893", "src/fern/types/contact_sheet.py", "master: bytes"),
            (
                "#894",
                "src/fern/types/print.py",
                "thumbnail: typing.Optional[bytes] = None",
            ),
            ("#894", "src/fern/types/print.py", "image: str"),
        ],
    );
}

/// #898: a map of a discriminated union beside `null` keeps the discriminated
/// value union. #902: a component map of `$ref` values beside `null` makes its
/// values optional, as a nullable map does.
#[test]
fn nullable_map_wrappers_keep_value_discrimination_and_optionality() {
    holds(
        "nullable-map-wrappers",
        &[
            (
                "#898",
                "src/fern/types/plan_activities_value.py",
                "typing.Union[PlanActivitiesValue_Inline, PlanActivitiesValue_Git], pydantic.Field(discriminator=\"kind\")",
            ),
            (
                "#902",
                "src/fern/types/job_results.py",
                "JobResults = typing.Optional[typing.Dict[str, typing.Optional[ResultValue]]]",
            ),
        ],
    );
}

/// #905: a `$ref` beside `properties` (3.1) or `type: object` (3.0) aliases
/// its target. #906: a pointer naming no `properties` segment (an array
/// component's own `items`) is the unknown type, where one through
/// `properties` is copied. #907: an element that is only `allOf: [$ref]` is
/// the reference. #908: an undescribed `allOf: [$ref]` beside an open map is a
/// model extending the reference, where a described one is the reference.
#[test]
fn reference_compositions_match_the_certified_pair() {
    holds(
        "reference-compositions",
        &[
            (
                "#905",
                "src/fern/types/accepted_response.py",
                "AcceptedResponse = BaseResponse",
            ),
            (
                "#906",
                "src/fern/types/portal.py",
                "votes: typing.Optional[typing.List[typing.Any]]",
            ),
            (
                "#906",
                "src/fern/types/portal.py",
                "tallies: typing.Optional[typing.List[PortalTalliesItem]]",
            ),
            (
                "#907",
                "src/fern/types/portal.py",
                "links: typing.Optional[typing.List[SeamlessLink]]",
            ),
            (
                "#908",
                "src/fern/types/portal_overrides.py",
                "class PortalOverrides(PortalSettings):",
            ),
            (
                "#908",
                "src/fern/types/portal.py",
                "settings: typing.Optional[PortalSettings]",
            ),
        ],
    );
    holds(
        "reference-siblings-legacy",
        &[
            (
                "#905",
                "src/fern/types/font_assignments.py",
                "FontAssignments = ThemeFonts",
            ),
            (
                "#908",
                "src/fern/types/export_response_tables_item_configuration.py",
                "class ExportResponseTablesItemConfiguration(TableConfig):",
            ),
            (
                "#907",
                "src/fern/types/export_response_tables_item.py",
                "columns: typing.Optional[typing.List[ColumnConfig]] = None",
            ),
        ],
    );
}

/// #889: a union composed as an `allOf` member lends its branches' fields,
/// the first branch's spelling winning a conflict, inline branches with an
/// unrequired tag merging, a branch's inline `allOf` members lending too, and
/// an `allOf` member referencing a union component lending its branches, the
/// last branch's spelling winning there.
#[test]
fn flattened_union_branches_keep_fields_and_first_branch_precedence() {
    holds(
        "union-branch-flattening",
        &[
            (
                "#889",
                "src/fern/types/ramp.py",
                "source: typing.Optional[FiatSource] = None",
            ),
            (
                "#889",
                "src/fern/types/ramp_method.py",
                "fiat: typing.Optional[str] = None",
            ),
            (
                "#889",
                "src/fern/types/ticket.py",
                "price: typing.Optional[str] = None",
            ),
            (
                "#889",
                "src/fern/types/instructed_off_ramp_properties_payment_instructions.py",
                "iban: typing.Optional[str] = None",
            ),
            (
                "#889",
                "src/fern/types/instructed_off_ramp_properties_payment_instructions.py",
                "holder: typing.Optional[int] = None",
            ),
        ],
    );
}

/// #895: members that lower alike are deduplicated, keeping the last copy.
/// #896: a component `oneOf` of typed string enums is one enum, where bare
/// `const` members stay a union of their own. #897: a union nested in a map of
/// maps, an array of arrays or a map of arrays is hoisted under its container
/// path, discriminated where its members tag themselves.
#[test]
fn union_members_lower_dedupe_merge_and_hoist_as_the_certified_pair() {
    holds(
        "union-member-lowering",
        &[
            (
                "#895",
                "src/fern/types/session_problem_details_item.py",
                "SessionProblemDetailsItemOne, SessionProblemDetailsItemDescription, SessionProblemDetailsItemThree, str",
            ),
            ("#896", "src/fern/types/presence.py", "class Presence(enum.StrEnum):"),
            ("#896", "src/fern/types/exposure_unit.py", "ExposureUnit = typing.Union[ExposureUnitZero, ExposureUnitOne]"),
            ("#897", "src/fern/types/session_readings_by_owner_value_value.py", "pydantic.Field(discriminator=\"reading_type\")"),
            ("#897", "src/fern/types/session_reading_batches_item_item.py", "pydantic.Field(discriminator=\"reading_type\")"),
            (
                "#897",
                "src/fern/types/session_calibrations_value_item.py",
                "SessionCalibrationsValueItem = typing.Union[str, SessionCalibrationsValueItemOffset]",
            ),
        ],
    );
}

/// #984: an `allOf` beside a plain `type: string` member is the certified
/// pair's `str` alias, before inheritance (`TagCode` over `$ref Hound`) or
/// union flattening (`BadgeCode` over a `oneOf`), documented by the string
/// member's description over the composition's own (`CollarCode`); the object
/// composition `Hound` stays a model.
#[test]
fn string_compositions_keep_the_certified_scalar_type() {
    holds(
        "string-member-compositions",
        &[
            (
                "#984",
                "src/fern/types/tag_code.py",
                "TagCode = str\n\"\"\"\nA tag code, after the referenced hound.\n\"\"\"\n",
            ),
            (
                "#984",
                "src/fern/types/badge_code.py",
                "BadgeCode = str\n\"\"\"\nA badge code, before a union of breeds.\n\"\"\"\n",
            ),
            (
                "#984",
                "src/fern/types/collar_code.py",
                "CollarCode = str\n\"\"\"\nThe string member's description.\n\"\"\"\n",
            ),
            ("#984", "src/fern/types/leash_code.py", "LeashCode = str\n"),
            ("#984", "src/fern/types/hound.py", "class Hound(Animal):"),
        ],
    );
}

/// #982: a property narrowing an enum whose use-site copy is named as the enum
/// itself (`Parcel.state` over `ParcelState`) leaves the enum documented with
/// its own description; the property keeps the narrowing member's sentence.
#[test]
fn enum_components_keep_their_own_description() {
    holds(
        "enum-use-site-descriptions",
        &[
            (
                "#982",
                "src/fern/types/parcel_state.py",
                "class ParcelState(enum.StrEnum):\n    \"\"\"\n    Where a parcel is in its journey.\n    \"\"\"\n",
            ),
            (
                "#982",
                "src/fern/client.py",
                "        state : ParcelState\n            A registered parcel is never a draft.\n",
            ),
        ],
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
