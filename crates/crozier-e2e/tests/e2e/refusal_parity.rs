//! The `discriminant-value-unsuitable` class narrowed to what the certified
//! pair refuses, driven through the real binary. A discriminator whose mapping
//! names a schema bare is `typing.Any` to Fern, which generates past an
//! unusable discriminant there; one mapped by references only is still
//! refused. The record is `docs/fern-measurements/refusal-parity/README.md`.

use std::path::{Path, PathBuf};

use super::{crozier_clean_env, departure_ledger, golden_tree_failures, repo_root};

/// Where the from-scratch cases live; each case's `fern-expected/` is a
/// compared golden.
pub(crate) const REFUSAL_PARITY_DIR: &str = "docs/fern-measurements/refusal-parity";
const CLASS_DIR: &str = "docs/fern-refusals/discriminant-value-unsuitable";
const ORCHARD: &str = "discriminant-names-orchard";

fn generate(spec: &Path, out: &Path, extra: &[&str]) -> std::process::Output {
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(spec)
        .arg("--output")
        .arg(out)
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ])
        .args(extra)
        .output()
        .expect("run crozier")
}

fn class_shape(name: &str) -> PathBuf {
    repo_root().join(CLASS_DIR).join(name)
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates small SDKs and compares them, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// The orchard document's `Crate` maps `pear` to the bare `PearCrate` and its
/// `Label` maps `sticker` to the bare `StickerLabel`, under the unusable
/// discriminants `@kind` and `$label`. crozier's complete SDK equals Fern's in
/// either enum mode, and rewriting `Crate` as the union crozier used to refuse
/// to write fails the comparison.
#[test]
fn bare_name_mapped_discriminants_match_fern_in_both_enum_modes() {
    let spec = repo_root()
        .join(REFUSAL_PARITY_DIR)
        .join(ORCHARD)
        .join("openapi.yml");
    for (mode, case) in [
        ("python-enums", ORCHARD.to_owned()),
        ("literals", format!("{ORCHARD}-literals")),
    ] {
        let golden = format!("{REFUSAL_PARITY_DIR}/{case}/fern-expected");
        let expected = repo_root().join(&golden);
        let ledger = departure_ledger()
            .golden(&golden, &[])
            .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        let run = generate(&spec, &out, &["--enum-type", mode]);
        assert!(
            run.status.success(),
            "{mode}: {}",
            String::from_utf8_lossy(&run.stderr)
        );
        let failures = golden_tree_failures(mode, ORCHARD, &ledger, &expected, &out);
        assert!(failures.is_empty(), "{mode}: {}", failures.join("\n\n"));
        let crate_module = out.join("src/fern/types/crate.py");
        let text = std::fs::read_to_string(&crate_module).expect("the Crate module");
        assert!(text.contains("Crate = typing.Any"), "{text}");
        std::fs::write(
            &crate_module,
            text.replace(
                "Crate = typing.Any",
                "Crate = typing.Union[AppleCrate, PearCrate]",
            ),
        )
        .unwrap();
        let unexplained = golden_tree_failures(mode, ORCHARD, &ledger, &expected, &out);
        assert!(
            unexplained
                .iter()
                .any(|failure| failure.contains("src/fern/types/crate.py")),
            "{mode}: an unexplained Crate must fail the comparison: {unexplained:?}"
        );
    }
}

/// Every shape the class measures as refused is refused in both modes, before
/// any file is written, beside the bare-name controls Fern generates from: the
/// class probe (`_t` under a `oneOf`), `$_type` and `@odata.type` under a
/// `oneOf`, `_t` and `@odata.type` on an inheritance base, the mapping-only
/// probe and the inferred one.
#[test]
fn pointer_mapped_discriminant_refusals_hold_beside_the_bare_name_controls() {
    let temp = tempfile::tempdir().expect("output tempdir");
    for (probe, discriminant) in [
        ("probe.yml", "\"_t\""),
        ("dollar-oneof-probe.yml", "\"$_type\""),
        ("odata-oneof-probe.yml", "\"@odata.type\""),
        ("underscore-inheritance-probe.yml", "\"_t\""),
        ("odata-inheritance-probe.yml", "\"@odata.type\""),
        ("mapping-only-probe.yml", "\"_t\""),
        ("inferred-probe.yml", "\"_t\""),
    ] {
        for strict in [false, true] {
            let out = temp.path().join(format!("{probe}-{strict}"));
            let flags: &[&str] = if strict { &["--fern-strict"] } else { &[] };
            let run = generate(&class_shape(probe), &out, flags);
            assert_eq!(run.status.code(), Some(1), "{probe} strict={strict}");
            let stderr = String::from_utf8(run.stderr).unwrap();
            assert_eq!(stderr.lines().count(), 1, "{stderr}");
            assert!(
                stderr.contains(&format!(
                    "discriminant-value-unsuitable: #/components/schemas/Asset discriminant {discriminant}"
                )),
                "{probe}: {stderr}"
            );
            assert_eq!(stderr.contains("fern-strict"), strict, "{stderr}");
            assert!(!out.exists(), "{probe} wrote {}", out.display());
        }
    }
    for control in [
        "bare-name-oneof-control.yml",
        "bare-name-inheritance-control.yml",
    ] {
        for strict in [false, true] {
            let out = temp.path().join(format!("{control}-{strict}"));
            let flags: &[&str] = if strict { &["--fern-strict"] } else { &[] };
            let run = generate(&class_shape(control), &out, flags);
            assert!(
                run.status.success(),
                "{control} strict={strict}: {}",
                String::from_utf8_lossy(&run.stderr)
            );
            let asset = std::fs::read_to_string(out.join("src/fern/types/asset.py"))
                .expect("the Asset module");
            assert!(asset.contains("Asset = typing.Any"), "{control}: {asset}");
        }
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
