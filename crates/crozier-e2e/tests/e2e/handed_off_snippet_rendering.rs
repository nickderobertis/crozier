//! The usage-snippet causes the fixture-only witness searches handed off — how a
//! worked call is written and whether one is written at all — each measured
//! under [`AREA_DIR`] with a from-scratch document and the certified pair's fresh
//! tree, and held here through the real binary: crozier's output byte-matches
//! every committed tree (in literals mode too, where the enum mode changes the
//! worked call), each catalogued Fern defect is what crozier writes in its
//! place, an unexplained byte beside it still fails, and the corrected calls
//! bind to and drive crozier's generated SDK. `docs/fern-measurements/handed-off/snippet-rendering.tsv`
//! records each cause's verdict.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::handed_off_example_values::{
    generate, ledger_tree_failures, literals_ledger_in, literals_tree_in, tree_failures,
};
use super::{golden_path, repo_root, runtime_python_env};

/// Each cause's directory sits here under the record's own spelling of its name,
/// which `snippet-rendering.tsv` and the area README cite.
pub(super) const AREA_DIR: &str = "docs/fern-measurements/handed-off/snippet-rendering";

/// Every cause the triage record names, each a directory under [`AREA_DIR`].
const CAUSES: &[&str] = &[
    "R15",
    "R17",
    "byte-text-response-reference-snippet",
    "example-empty-array-field",
    "example-inline-union-member-constructor",
    "example-map-of-model-values",
    "example-presence",
    "json-binary-body-snippet",
    "map-body-placeholder-layout",
    "readme-endpoint-choice",
    "request-example-union-variant-fields",
    "snippet-rendering",
];

/// The causes whose worked call names an enum, so their literals-mode tree is
/// committed as an `expected-literals/` overlay of the cause's own tree.
const LITERALS: &[&str] = &[
    "example-inline-union-member-constructor",
    "request-example-union-variant-fields",
];

/// The causes whose verdict rests on behaviour, each keeping the `runtime.txt`
/// its journey below reproduces.
const RUNTIME: &[&str] = &["json-binary-body-snippet", "snippet-rendering"];

const WIRE: &str = "crates/crozier-e2e/tests/e2e/snippet_rendering_wire.py";
const BRACKET_EVIDENCE: &str = "docs/departures/evidence/bracket-query-parameter-call-keyword.py";
const HEADER_EVIDENCE: &str = "docs/departures/evidence/non-string-client-header-example.py";

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
pub(super) const MANIFEST: &str = ".crozier-overlay.json";

/// The literals overlay goldens this module compares, for the inventory of
/// compared goldens (each cause's own `fern-expected/` is found by directory).
pub(super) fn compared_overlays() -> Vec<String> {
    LITERALS
        .iter()
        .map(|cause| format!("{AREA_DIR}/{cause}/expected-literals/fern-expected"))
        .collect()
}

fn cause_dir(cause: &str) -> PathBuf {
    repo_root().join(AREA_DIR).join(cause)
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Every Fern golden comparison — the corpus `*_matches_fern_output` tests, the hand-written, probe and measurement gates — runs in this one binary suite by the project's design (crates/crozier-e2e/AGENTS.md), which drives the binary crozier:build leaves; giving these measurement journeys their own Nx edge is a graph change for that whole family (the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads"), not for these cases.
#[test]
fn every_handed_off_snippet_rendering_measurement_is_complete() {
    let mut directories: Vec<String> = std::fs::read_dir(repo_root().join(AREA_DIR))
        .expect("the measurement directory exists")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .collect();
    directories.sort();
    assert_eq!(
        directories, CAUSES,
        "{AREA_DIR}: every cause directory needs a CAUSES row"
    );
    for cause in CAUSES {
        let dir = cause_dir(cause);
        for part in ["openapi.yml", "README.md", "fern-expected/README.md"] {
            assert!(dir.join(part).is_file(), "{cause}: {part} is missing");
        }
        assert_eq!(
            dir.join("runtime.txt").is_file(),
            RUNTIME.contains(cause),
            "{cause}: a runtime.txt exactly where the verdict rests on behaviour"
        );
        assert_eq!(
            dir.join("expected-literals/fern-expected").is_dir(),
            LITERALS.contains(cause),
            "{cause}: an expected-literals overlay exactly where the enum mode changes the call"
        );
    }
}

#[test]
fn handed_off_snippet_rendering_measurements_match_fern() {
    let mut failures = Vec::new();
    for cause in CAUSES {
        let dir = cause_dir(cause);
        let expected = dir.join("fern-expected");
        failures.extend(tree_failures(
            cause,
            &dir.join("openapi.yml"),
            &[],
            &golden_path(&expected),
            &expected,
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

#[test]
fn handed_off_snippet_rendering_literals_overlays_match_fern() {
    let mut failures = Vec::new();
    for cause in LITERALS {
        let dir = cause_dir(cause);
        let tree = literals_tree_in(&dir);
        failures.extend(ledger_tree_failures(
            &format!("{cause} (literals)"),
            &dir.join("openapi.yml"),
            &["--enum-type", "literals"],
            literals_ledger_in(&dir),
            tree.path(),
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// The certified pair's and crozier's text of `rel` for a cause.
fn file_texts(cause: &str, rel: &str) -> (String, String) {
    let dir = cause_dir(cause);
    let out = generate(&dir.join("openapi.yml"), &[]).unwrap_or_else(|failure| panic!("{failure}"));
    let read = |path: PathBuf| {
        std::fs::read_to_string(&path).unwrap_or_else(|error| panic!("{}: {error}", path.display()))
    };
    (
        read(dir.join("fern-expected").join(rel)),
        read(out.path().join(rel)),
    )
}

/// What crozier writes where a catalogued Fern defect stands, beside the
/// certified pair's line.
#[test]
fn catalogued_snippet_defects_are_what_crozier_writes() {
    for (cause, rel, fern, crozier) in [
        // bracket-query-parameter-call-keyword: the method's own argument.
        (
            "snippet-rendering",
            "reference.md",
            "    codes_array=[",
            "    codes=[",
        ),
        (
            "snippet-rendering",
            "reference.md",
            "    ids_array=[",
            "    ids=[",
        ),
        // non-string-client-header-example: the declared type's placeholder,
        // the string header's `YOUR_*` kept.
        (
            "snippet-rendering",
            "src/fern/client.py",
            "        strict_mode=\"YOUR_STRICT_MODE\",",
            "        strict_mode=True,",
        ),
        (
            "snippet-rendering",
            "src/fern/berths/client.py",
            "            shift_number=\"YOUR_SHIFT_NUMBER\",",
            "            shift_number=1,",
        ),
        (
            "snippet-rendering",
            "src/fern/berths/client.py",
            "            tide_metres=\"YOUR_TIDE_METRES\",",
            "            tide_metres=1.1,",
        ),
        (
            "snippet-rendering",
            "src/fern/client.py",
            "        tenant_code=\"YOUR_TENANT_CODE\",",
            "        tenant_code=\"YOUR_TENANT_CODE\",",
        ),
        // binary-json-body-example: the bytes the method is annotated with.
        (
            "json-binary-body-snippet",
            "reference.md",
            "    request=\"string\",",
            "    request=b\"string\",",
        ),
    ] {
        let (fern_reference, crozier_reference) = file_texts(cause, rel);
        let has = |text: &str, line: &str| text.lines().any(|candidate| candidate == line);
        assert!(
            has(&fern_reference, fern),
            "{cause}: the certified pair's `{fern}`"
        );
        assert!(
            has(&crozier_reference, crozier),
            "{cause}: crozier's `{crozier}`"
        );
        assert!(
            fern == crozier || !has(&crozier_reference, fern),
            "{cause}: crozier still writes `{fern}`"
        );
    }
    // The parameter list keeps the certified spelling, matched byte for byte.
    let (_, reference) = file_texts("snippet-rendering", "reference.md");
    assert!(reference
        .contains("**codes_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]`"));
}

/// A copy of a cause's committed tree with one line changed: a `from` the tree
/// no longer holds fails here, so a regenerated tree cannot leave a negative
/// case silently unperturbed.
#[cfg(unix)]
fn perturbed(cause: &str, rel: &str, from: &str, to: &str) -> tempfile::TempDir {
    let copy = tempfile::tempdir().expect("tree copy tempdir");
    super::copy_dir(&cause_dir(cause).join("fern-expected"), copy.path());
    let path = copy.path().join(rel);
    let text = std::fs::read_to_string(&path).expect("a committed Fern file");
    assert!(text.contains(from), "{cause}/{rel} holds no `{from}`");
    std::fs::write(&path, text.replacen(from, to, 1)).expect("perturb the tree");
    copy
}

/// Each departure explains only its own line, and each repaired line is no
/// longer explained by anything: a different certified spelling beside the
/// departure, or the line crozier wrote before its repair, fails the compare.
// `crozier compare` runs a reference command only on Unix (docs/compare.md).
#[cfg(unix)]
#[test]
fn snippet_departures_and_repairs_hold_only_their_lines() {
    for (cause, rel, from, to) in [
        // bracket-query-parameter-call-keyword: only `<name>_array=`.
        (
            "snippet-rendering",
            "reference.md",
            "    codes_array=[",
            "    codes_list=[",
        ),
        // non-string-client-header-example: only the `YOUR_<NAME>` placeholder.
        (
            "snippet-rendering",
            "src/fern/client.py",
            "        strict_mode=\"YOUR_STRICT_MODE\",",
            "        strict_mode=\"YOUR_MODE\",",
        ),
        // binary-json-body-example: only the plain-string placeholder.
        (
            "json-binary-body-snippet",
            "reference.md",
            "    request=\"string\",",
            "    request=\"strings\",",
        ),
        // The repairs: what crozier wrote before each, now unexplained.
        (
            "snippet-rendering",
            "README.md",
            "    tenant_code=\"<X-Tenant-Code>\",\n",
            "    strict_mode=\"<X-Strict-Mode>\",\n    tenant_code=\"<X-Tenant-Code>\",\n",
        ),
        (
            "example-presence",
            "reference.md",
            "client.darkroom.flash_enlarger(...)",
            "client.darkroom.flash_enlarger(\n    image=\"example_image\",\n)",
        ),
        (
            "example-empty-array-field",
            "reference.md",
            "    criteria=Criteria(),",
            "    criteria=Criteria(\n        any_of=[],\n    ),",
        ),
        (
            "map-body-placeholder-layout",
            "README.md",
            "    request={\"key\": \"value\"},",
            "    request={\n        \"key\": \"value\"\n    },",
        ),
        (
            "request-example-union-variant-fields",
            "reference.md",
            "            window=Window.DAILY,",
            "            window=Window.HOURLY,",
        ),
    ] {
        let tree = perturbed(cause, rel, from, to);
        let differing = super::handed_off_example_values::compare_differing(
            &cause_dir(cause).join("openapi.yml"),
            tree.path(),
        );
        assert!(
            differing.iter().any(|file| file == rel),
            "{cause} {rel}: {differing:?}"
        );
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

fn run_python(python: &Path, script: &Path, args: &[&std::ffi::OsStr]) -> std::process::Output {
    std::process::Command::new(python)
        .arg(script)
        .args(args)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output()
        .expect("run the journey")
}

/// The run `runtime.txt` records under `heading`: the JSON line it printed.
fn recorded_run(cause: &str, heading: &str) -> String {
    let recorded = std::fs::read_to_string(cause_dir(cause).join("runtime.txt"))
        .expect("the cause's runtime record");
    let section = recorded
        .split(&format!("## {heading}\n"))
        .nth(1)
        .unwrap_or_else(|| panic!("{cause}: runtime.txt records no `{heading}` run"));
    section
        .lines()
        .find(|line| line.starts_with('{'))
        .unwrap_or_else(|| panic!("{cause}: the `{heading}` run printed nothing"))
        .to_string()
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These `sdk_env_*` journeys run only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// The behaviour each catalogued defect rests on, driven through both SDKs as
/// `runtime.txt` records it: the certified pair's worked calls fail to bind
/// (`codes_array`, `ids_array`), its request and client-header examples fail
/// the actual `bytes`, `bool` and `int` annotations, and crozier's bind,
/// validate and send the values on the wire. An SDK directory without the
/// package is refused with exit 2.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_snippet_defect_journeys_hold_for_crozier_and_fern() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let root = repo_root();
    let work = tempfile::tempdir().expect("work dir");
    let absent = work.path().join("absent");
    // (cause, the departure the journey proves, its script, whether it reads
    // `reference.md`)
    let journeys = [
        (
            "json-binary-body-snippet",
            "binary-json-body-example",
            root.join(WIRE),
            false,
        ),
        (
            "snippet-rendering",
            "bracket-query-parameter-call-keyword",
            root.join(BRACKET_EVIDENCE),
            true,
        ),
        (
            "snippet-rendering",
            "non-string-client-header-example",
            root.join(HEADER_EVIDENCE),
            false,
        ),
    ];
    for (_, _, script, reads_reference) in &journeys {
        let reference = absent.join("reference.md");
        let mut args = vec![absent.as_os_str(), "--expected".as_ref(), "valid".as_ref()];
        if *reads_reference {
            args.extend(["--reference".as_ref(), reference.as_os_str()]);
        }
        let refused = run_python(&python, script, &args);
        assert_eq!(refused.status.code(), Some(2), "{refused:?}");
        assert!(
            predicate::str::contains("must contain the generated fern package")
                .eval(&String::from_utf8_lossy(&refused.stderr)),
            "{refused:?}"
        );
    }
    for (cause, departure, script, reads_reference) in &journeys {
        let dir = cause_dir(cause);
        let crozier =
            generate(&dir.join("openapi.yml"), &[]).unwrap_or_else(|failure| panic!("{failure}"));
        let certified = work.path().join(departure);
        super::copy_dir(&dir.join("fern-expected"), &certified);
        for (side, tree, expected) in [
            (
                "certified pair (fern-expected/src)",
                certified.as_path(),
                "invalid",
            ),
            ("crozier", crozier.path(), "valid"),
        ] {
            let src = tree.join("src");
            let reference = tree.join("reference.md");
            let mut args = vec![src.as_os_str(), "--expected".as_ref(), expected.as_ref()];
            if *reads_reference {
                args.extend(["--reference".as_ref(), reference.as_os_str()]);
            }
            let run = run_python(&python, script, &args);
            let heading = format!("{departure}: {side}");
            assert!(
                run.status.success(),
                "{cause} {heading}: {}",
                String::from_utf8_lossy(&run.stderr)
            );
            assert_eq!(
                String::from_utf8_lossy(&run.stdout).trim_end(),
                recorded_run(cause, &heading),
                "{cause} {heading}: the run runtime.txt records"
            );
        }
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
