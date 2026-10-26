//! The two generated-model defects measured against the certified pair under
//! `docs/fern-measurements/output-defects/`, each driven through the real
//! binary over the from-scratch document Fern generated `fern-expected/` from.
//! Both were parity gaps, repaired in `src/`: crozier's complete SDK must equal
//! Fern's, the line the defect decides must fail the comparison when written the
//! way crozier used to write it, and the generated SDK must behave the way the
//! measurement's `runtime.txt` records Fern's behaving.
//!
//! - `615-empty-composition-member-reference`: an `allOf` of `$ref Kiln` and a
//!   bare `{}` is `Kiln` itself, not a copied model
//!   (<https://github.com/nickderobertis/crozier/issues/615>).
//! - `617-annotated-inherited-union`: an annotated `$ref` to a union spelled
//!   through inheritance keeps its variant wrappers in the annotated copy
//!   (<https://github.com/nickderobertis/crozier/issues/617>).

use std::path::{Path, PathBuf};

use assert_cmd::Command;
use predicates::prelude::*;

use super::{
    crozier_clean_env, departure_ledger, golden_tree_failures, probe_command, repo_root,
    runtime_python_env,
};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const OUTPUT_DEFECTS_DIR: &str = "docs/fern-measurements/output-defects";
const EMPTY_MEMBER: &str = "615-empty-composition-member-reference";
const INHERITED_UNION: &str = "617-annotated-inherited-union";
/// The cases these journeys hold whole, which the directory-wide comparison skips.
pub(crate) const OWN_JOURNEYS: [&str; 2] = [EMPTY_MEMBER, INHERITED_UNION];
const RUNTIME: &str = "crates/crozier-e2e/tests/e2e/output_defects_runtime.py";

fn case_dir(case: &str) -> PathBuf {
    repo_root().join(OUTPUT_DEFECTS_DIR).join(case)
}

fn failures(case: &str, out: &Path) -> Vec<String> {
    let golden = format!("{OUTPUT_DEFECTS_DIR}/{case}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let spec = case_dir(case).join("openapi.yml");
    golden_tree_failures(
        case,
        &spec.display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

fn generate(spec: &Path, out: &Path) {
    probe_command(spec, out).assert().success();
}

/// Generate the case's SDK, hold it whole to Fern's, then show that `file`
/// spelling `fern` (as both trees do) is what the comparison turns on: written as
/// crozier wrote it before the repair, the comparison names `file`.
fn holds_line(case: &str, file: &str, fern: &str, crozier: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(&case_dir(case).join("openapi.yml"), &out);
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

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// `kiln` (`[$ref Kiln, {}]`) and `overflowKiln` (`[{}, $ref Kiln]`) are typed
/// with `Kiln` itself, in the model and in the inline body's parameter, while the
/// described and constrained members keep classes of their own.
#[test]
fn an_empty_composition_member_keeps_the_referenced_model() {
    holds_line(
        EMPTY_MEMBER,
        "src/fern/types/load.py",
        "    label: str\n    kiln: Kiln\n    overflow_kiln: typing_extensions.Annotated[\n        typing.Optional[Kiln],",
        "    label: str\n    kiln: LoadKiln\n    overflow_kiln: typing_extensions.Annotated[\n        typing.Optional[Kiln],",
    );
    holds_line(
        EMPTY_MEMBER,
        "src/fern/loads/client.py",
        "        destination: Kiln,\n        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,",
        "        destination: TransferLoadRequestDestination,\n        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,",
    );
}

/// The annotated copies of `Coat` — a component property's and an inline body
/// field's — are discriminated unions of their own variant wrappers, each
/// documented by the annotation, as Fern declares them.
#[test]
fn an_annotated_inherited_union_keeps_its_variant_wrappers() {
    holds_line(
        INHERITED_UNION,
        "src/fern/types/pot_outer_coat.py",
        "class PotOuterCoat_Matte(Base):\n    \"\"\"\n    The coat on the pot's outer wall.\n    \"\"\"\n\n    finish: typing.Literal[\"matte\"] = \"matte\"\n",
        "class PotOuterCoat(UniversalBaseModel):\n    \"\"\"\n    The coat on the pot's outer wall.\n    \"\"\"\n\n    finish: str\n",
    );
    holds_line(
        INHERITED_UNION,
        "src/fern/pots/types/recoat_pot_request_coat.py",
        "RecoatPotRequestCoat = typing_extensions.Annotated[\n    typing.Union[RecoatPotRequestCoat_Matte, RecoatPotRequestCoat_Gloss], pydantic.Field(discriminator=\"finish\")\n]\n",
        "",
    );
}

// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

/// Each measurement document is generated from as committed: removing it is an
/// actionable failure that writes no SDK.
#[test]
fn a_missing_measurement_document_fails_without_writing() {
    let temp = tempfile::tempdir().unwrap();
    let out = temp.path().join("sdk");
    probe_command(&temp.path().join(EMPTY_MEMBER).join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document writes no SDK");
}

fn as_json(spec: &Path, dir: &Path) -> PathBuf {
    let value: serde_json::Value =
        crate::yaml::from_str(&std::fs::read_to_string(spec).unwrap()).expect("a YAML document");
    let path = dir.join("openapi.json");
    std::fs::write(&path, serde_json::to_vec_pretty(&value).unwrap()).unwrap();
    path
}

fn journey(python: &Path, case: &str, src: &Path, spec: &Path) -> Command {
    let mut command = Command::new(python);
    command
        .arg(repo_root().join(RUNTIME))
        .arg(&case[..3])
        .arg(src)
        .arg(spec)
        .env("PYTHONDONTWRITEBYTECODE", "1");
    command
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// Both generated SDKs behave as the measurements record: through crozier's
/// client and through the certified tree's, #615's `kiln` accepts and returns
/// the exported `Kiln` while the controls keep their own classes, and every
/// #617 variant parses through the annotated copies into its own class and is
/// sent in the shape the source schema validates. The same document with the
/// `{}` member written as a description, or with `Coat`'s mapping removed, makes
/// crozier copy the target as an ordinary model, and the journey names that.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_output_defect_journeys_hold_for_crozier_and_fern() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let work = tempfile::tempdir().unwrap();
    let missing = journey(
        &python,
        EMPTY_MEMBER,
        &work.path().join("absent"),
        work.path(),
    )
    .assert()
    .code(2);
    missing.stderr(predicate::str::contains(
        "must contain the generated fern package",
    ));
    let malformed = work.path().join("malformed.json");
    std::fs::write(
        &malformed,
        r##"{"components": {"schemas": {"Load": {"properties": {"kiln": {"$ref": "#/components/schemas/Absent"}}}, "Kiln": {"type": "array"}}}}"##,
    )
    .unwrap();
    journey(
        &python,
        EMPTY_MEMBER,
        &case_dir(EMPTY_MEMBER).join("fern-expected/src"),
        &malformed,
    )
    .assert()
    .code(2)
    .stderr(predicate::str::contains(
        "Load.properties.kiln.$ref '#/components/schemas/Absent' names no component schema",
    ))
    .stderr(predicate::str::contains("Kiln.type 'array' is not one of"));
    let cyclic = work.path().join("cyclic.json");
    std::fs::write(
        &cyclic,
        r##"{"components": {"schemas": {"Load": {"allOf": [{"allOf": [{"$ref": "#/components/schemas/Kiln"}]}]}, "Kiln": {"$ref": "#/components/schemas/Load"}}}}"##,
    )
    .unwrap();
    journey(
        &python,
        EMPTY_MEMBER,
        &case_dir(EMPTY_MEMBER).join("fern-expected/src"),
        &cyclic,
    )
    .assert()
    .code(2)
    .stderr(predicate::str::contains(
        "references cycle through Load -> Kiln -> Load",
    ));
    journey(
        &python,
        INHERITED_UNION,
        &case_dir(EMPTY_MEMBER).join("fern-expected/src"),
        &as_json(&case_dir(INHERITED_UNION).join("openapi.yml"), work.path()),
    )
    .assert()
    .code(2)
    .stderr(predicate::str::contains(
        "exports no PotOuterCoat, RecoatPotRequestCoat",
    ));
    for (case, removed, kept, refused) in [
        (
            EMPTY_MEMBER,
            "            - $ref: '#/components/schemas/Kiln'\n            - {}\n        overflowKiln:",
            "            - $ref: '#/components/schemas/Kiln'\n            - description: Kiln the load fires in.\n        overflowKiln:",
            "Load.kiln is typed <class 'fern.types.load_kiln.LoadKiln'>, not the exported Kiln",
        ),
        (
            INHERITED_UNION,
            "      discriminator:\n        propertyName: finish\n        mapping:\n          matte: '#/components/schemas/MatteCoat'\n          gloss: '#/components/schemas/GlossCoat'\n",
            "",
            "parsed through PotOuterCoat as PotOuterCoat, not PotOuterCoat_Matte",
        ),
    ] {
        let dir = work.path().join(case);
        std::fs::create_dir_all(&dir).unwrap();
        let spec = case_dir(case).join("openapi.yml");
        let json = as_json(&spec, &dir);
        for src in [case_dir(case).join("fern-expected/src"), {
            let out = dir.join("crozier");
            generate(&spec, &out);
            out.join("src")
        }] {
            let run = journey(&python, case, &src, &json).output().unwrap();
            assert!(
                run.status.success(),
                "{case} over {}: {}{}",
                src.display(),
                String::from_utf8_lossy(&run.stdout),
                String::from_utf8_lossy(&run.stderr)
            );
        }

        let text = std::fs::read_to_string(&spec).unwrap();
        assert!(text.contains(removed), "{case}: no {removed:?}");
        let control_dir = dir.join("control");
        std::fs::create_dir_all(&control_dir).unwrap();
        let control = control_dir.join("openapi.yml");
        std::fs::write(&control, text.replacen(removed, kept, 1)).unwrap();
        let out = control_dir.join("sdk");
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&control)
            .arg("--output")
            .arg(&out)
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
            ])
            .assert()
            .success();
        journey(&python, case, &out.join("src"), &as_json(&control, &control_dir))
            .assert()
            .code(1)
            .stderr(predicate::str::contains(refused));
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
