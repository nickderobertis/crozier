//! The worked-example, example-validity and documentation-rendering tickets
//! of #966, each settled against a from-scratch document under [`DIR`] and the
//! certified pair's complete tree for it (Fern CLI 5.216.0, fern-python-sdk
//! 5.42.0), in both enum modes.
//!
//! Every case runs the real binary, compares its SDK with the certified tree
//! file for file under the departures ledger, and asserts the bytes each ticket
//! decides in the generated file it decides them in.

use super::union_inheritance::{enum_failures_in, generate_in, literals_failures_in};

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
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
