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

/// Generate the patisserie SDK through the built CLI, isolated from the
/// caller's `CROZIER_*` environment.
fn generate(source: &Path, strict: bool) -> tempfile::TempDir {
    let generated = tempfile::tempdir().unwrap();
    let mut command = Command::new(binary());
    for (key, _) in
        std::env::vars_os().filter(|(key, _)| key.to_string_lossy().starts_with("CROZIER_"))
    {
        command.env_remove(key);
    }
    command
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(source)
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
    generated
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
        let generated = generate(&source, strict);
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

/// The departure admits only the measured adapters and example arguments. A
/// tampered adapter, an edited example or import, a source whose inner union
/// carries no discriminator, or a comparison without the source document must
/// each stay a mismatch.
#[test]
fn nested_discriminator_departure_rejects_what_it_was_not_measured_on() {
    let root = root();
    let source = root.join(FIXTURE).join("openapi.yml");
    let reference = root.join(GOLDEN);
    let generated = generate(&source, false);
    let document = std::fs::read_to_string(&source).unwrap();
    let compare = |document: Option<&str>, path: &str, emitted: &str| {
        let mut context = Context::from_trees(&reference, generated.path());
        if let Some(document) = document {
            let spec = tempfile::Builder::new().suffix(".yml").tempfile().unwrap();
            std::fs::write(spec.path(), document).unwrap();
            context = context.with_source_document(crozier::openapi::load(spec.path()).unwrap());
        }
        let fern = std::fs::read_to_string(reference.join(path)).unwrap();
        parity::compare_file(&context, path, emitted, &fern)
            .unwrap()
            .matches()
    };
    let model = "src/fern/types/pastry.py";
    let readme = "README.md";
    let emitted = |path: &str| std::fs::read_to_string(generated.path().join(path)).unwrap();
    // The unaltered output is the control: each case below differs from it by
    // one edit, so its mismatch is that edit's.
    for path in [model, readme] {
        assert!(
            compare(Some(&document), path, &emitted(path)),
            "{path} must match unaltered"
        );
    }
    let edit = |path: &str, from: &str, to: &str| {
        let text = emitted(path);
        assert!(text.contains(from), "{path} no longer contains {from:?}");
        text.replacen(from, to, 1)
    };
    let tampered = [
        (
            "adapter merge order",
            model,
            edit(
                model,
                r#"return {**value, **data, "kind": self.kind}"#,
                r#"return {**data, **value, "kind": self.kind}"#,
            ),
        ),
        (
            "adapter unflatten probe",
            model,
            edit(model, r#"("crust" in data or"#, r#"("fruit" in data or"#),
        ),
        (
            "wrapper field beside the adapter",
            model,
            edit(
                model,
                "    kind: typing.Literal[\"tart\"] = \"tart\"\n",
                "    kind: typing.Literal[\"tart\"] = \"tart\"\n    note: str\n",
            ),
        ),
        (
            "example value",
            readme,
            edit(readme, r#"fruit="fruit","#, r#"fruit="pear","#),
        ),
        (
            "example import",
            readme,
            edit(
                readme,
                "from fern import FernApi, Pastry_Tart, TartOrder_Shortcrust",
                "from fern import FernApi, Pastry_Tart, TartOrder_Shortcrust, Croissant",
            ),
        ),
        (
            "documentation prose",
            readme,
            edit(
                readme,
                "Instantiate and use the client with the following:",
                "Use the client:",
            ),
        ),
    ];
    for (case, path, text) in &tampered {
        assert!(
            !compare(Some(&document), path, text),
            "{case}: {path} must not match"
        );
    }
    let inner_discriminator = "      discriminator:\n        propertyName: crust\n        mapping:\n          shortcrust: '#/components/schemas/FruitTart'\n          puff: '#/components/schemas/CreamTart'\n";
    assert!(document.contains(inner_discriminator));
    let plain_inner = document.replacen(inner_discriminator, "", 1);
    for path in [model, readme] {
        assert!(
            !compare(Some(&plain_inner), path, &emitted(path)),
            "{path} must not match when the inner union has no discriminator"
        );
        assert!(
            !compare(None, path, &emitted(path)),
            "{path} must not match without the source document"
        );
    }
}
