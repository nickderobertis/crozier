//! The nested-discriminator golden, through the real CLI and parity engine.

use std::collections::BTreeSet;
use std::path::{Path, PathBuf};

use assert_cmd::Command;
use crozier::departures::Context;
use crozier::parity;

#[allow(
    dead_code,
    reason = "this binary uses scoped ledger loading and recording; aggregate inventory and overlay helpers belong to their existing suites"
)]
#[path = "../../support/departures_ledger.rs"]
mod ledger;

const FIXTURE: &str = "docs/fern-measurements/examples/nested-discriminator-wire";
const GOLDEN: &str = "docs/fern-measurements/examples/nested-discriminator-wire/fern-expected";

fn root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("../../..")
        .canonicalize()
        .unwrap()
}

fn binary() -> PathBuf {
    if let Some(path) = std::env::var_os("CARGO_BIN_EXE_crozier") {
        return PathBuf::from(path);
    }
    std::env::current_exe()
        .unwrap()
        .parent()
        .unwrap()
        .parent()
        .unwrap()
        .join(format!("crozier{}", std::env::consts::EXE_SUFFIX))
}

#[test]
fn nested_discriminator_golden_diff_is_only_the_flat_wire_departure() {
    let root = root();
    let source = root.join(FIXTURE).join("openapi.yml");
    let reference = root.join(GOLDEN);
    // Only this fixture exists in the isolated ledger root. A whole-inventory
    // walk must fail here; the scoped loader must succeed and retain its rows.
    let isolated = tempfile::tempdir().unwrap();
    for path in [ledger::LEDGER, ledger::INVENTORY] {
        let destination = isolated.path().join(path);
        std::fs::create_dir_all(destination.parent().unwrap()).unwrap();
        std::fs::copy(root.join(path), destination).unwrap();
    }
    let expected: BTreeSet<_> = parity::walk_files(&reference)
        .unwrap()
        .into_iter()
        .collect();
    for path in &expected {
        let destination = isolated.path().join(GOLDEN).join(path);
        std::fs::create_dir_all(destination.parent().unwrap()).unwrap();
        std::fs::copy(reference.join(path), destination).unwrap();
    }
    assert!(ledger::Ledger::load(isolated.path()).is_err());
    assert!(ledger::Ledger::load_filtered(isolated.path(), Some("unregistered")).is_err());
    let ledger = ledger::Ledger::load_filtered(isolated.path(), Some(GOLDEN))
        .unwrap()
        .golden(GOLDEN, &[])
        .unwrap();
    for strict in [false, true] {
        let generated = tempfile::tempdir().unwrap();
        let mut command = Command::new(binary());
        for (key, _) in
            std::env::vars_os().filter(|(key, _)| key.to_string_lossy().starts_with("CROZIER_"))
        {
            command.env_remove(key);
        }
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&source)
            .arg("--output")
            .arg(generated.path())
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
            ]);
        if strict {
            command.arg("--fern-strict");
        }
        command.assert().success();
        let actual: BTreeSet<_> = parity::walk_files(generated.path())
            .unwrap()
            .into_iter()
            .collect();
        assert_eq!(actual, expected, "generated file set differs");
        let context = Context::from_trees(&reference, generated.path())
            .with_source_document(crozier::openapi::load(&source).unwrap());
        let mut observed = Vec::new();
        for path in &expected {
            let emitted = std::fs::read_to_string(generated.path().join(path)).unwrap();
            let fern = std::fs::read_to_string(reference.join(path)).unwrap();
            let comparison = parity::compare_file(&context, path, &emitted, &fern).unwrap();
            assert!(
                comparison.matches(),
                "{path}: {}",
                comparison.diff().unwrap_or_default()
            );
            observed.extend(
                comparison
                    .departures
                    .iter()
                    .map(|departure| (path.clone(), departure.line.get(), departure.id.to_owned())),
            );
        }
        let failures = ledger.check(&observed, &|_| true);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    }
}
