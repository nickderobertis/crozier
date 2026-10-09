//! The union shapes the hand-written union fixtures prove, driven through the
//! real binary: each fixture's complete certified tree in both enum modes, the
//! two union extensions under both spellings and with conflicting values, the
//! `union-value-wrapper-docs-example` departure's scope, and the refusals
//! beside the shapes that now generate.

use std::path::{Path, PathBuf};

use super::{
    departure_ledger, golden_path, golden_tree_failures, probe_artifact_digest, probe_command,
    refusal_run, refused_failures, repo_root, walk_files, HANDWRITTEN_DIR,
};

/// Every hand-written union fixture, each with a literals overlay under
/// [`LITERALS_DIR`].
const FIXTURES: [&str; 13] = [
    "atlas-untagged-inline-discriminator",
    "bakery-get-body-member",
    "ferry-mapping-outside-schemas",
    "greenhouse-undiscriminated-unions",
    "harbor-nullable-inline-object",
    "kitchen-nested-mapping-target",
    "library-union-shared-fields",
    "museum-titled-array-items",
    "pharmacy-nullable-scalar-unions",
    "quiz-nullable-response-union",
    "survey-map-value-union",
    "telescope-renamed-discriminant",
    "thermostat-nullable-member",
];

/// Where each fixture's literals overlay lives: the files of the tree Fern
/// generated with `enum_type` unset that differ from its `fern-expected/`, and
/// a manifest naming the files it omits and the complete tree's digest.
const LITERALS_DIR: &str = "docs/fern-measurements/union-literals";

/// The overlay manifest.
const MANIFEST: &str = ".crozier-overlay.json";

fn fixture(name: &str) -> PathBuf {
    repo_root().join(HANDWRITTEN_DIR).join(name)
}

/// `fixture`'s literals tree: `fern-expected/` less the files the manifest
/// removes, with the overlay laid over it, held to the manifest's digest of the
/// complete tree Fern generated.
fn literals_tree(name: &str) -> Result<tempfile::TempDir, String> {
    let overlay = repo_root().join(LITERALS_DIR).join(name);
    let text = std::fs::read_to_string(overlay.join(MANIFEST))
        .map_err(|error| format!("{name}: cannot read its literals manifest: {error}"))?;
    let manifest: serde_json::Value = serde_json::from_str(&text)
        .map_err(|error| format!("{name}: invalid literals manifest: {error}"))?;
    for (key, value) in [
        ("enum_type", "literals"),
        ("base", "fern-expected"),
        ("fern_cli_version", "5.67.1"),
        ("fern_python_sdk_version", "5.20.0"),
    ] {
        if manifest[key] != value {
            return Err(format!(
                "{name}: its literals manifest must record {key} `{value}`"
            ));
        }
    }
    let removed: Vec<&str> = manifest["removed"]
        .as_array()
        .ok_or_else(|| format!("{name}: its literals manifest has no `removed` list"))?
        .iter()
        .filter_map(serde_json::Value::as_str)
        .collect();
    let tree = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let copy = |from: &Path, rel: &str| -> Result<(), String> {
        let to = tree.path().join(rel);
        std::fs::create_dir_all(to.parent().expect("a file has a parent"))
            .and_then(|()| std::fs::copy(from.join(rel), &to).map(drop))
            .map_err(|error| format!("{name}: cannot copy {rel}: {error}"))
    };
    let base = fixture(name).join("fern-expected");
    for rel in walk_files(&base) {
        if !removed.contains(&rel.as_str()) {
            copy(&base, &rel)?;
        }
    }
    for rel in walk_files(&overlay) {
        if rel != MANIFEST {
            copy(&overlay, &rel)?;
        }
    }
    let digest = probe_artifact_digest(tree.path())?;
    if manifest["digest"] != digest.as_str() {
        return Err(format!(
            "{name}: the rebuilt literals tree hashes to {digest}, not the {} its manifest \
             records — a committed Fern file changed; restore it",
            manifest["digest"]
        ));
    }
    Ok(tree)
}

/// Every way crozier's output over `spec` under `enum_type` fails to match the
/// Fern tree `expected` that `fixture`'s ledger rows belong to.
fn tree_failures(name: &str, spec: &Path, expected: &Path, enum_type: &str) -> Vec<String> {
    let out = tempfile::tempdir().expect("tempdir");
    let result = probe_command(spec, out.path())
        .args(["--enum-type", enum_type])
        .output()
        .expect("crozier runs");
    if !result.status.success() {
        return vec![format!(
            "{name}, enum-type={enum_type}: crozier failed: {}",
            String::from_utf8_lossy(&result.stderr)
        )];
    }
    let golden = golden_path(&fixture(name).join("fern-expected"));
    let ledger = match departure_ledger().golden(&golden, &[]) {
        Ok(ledger) => ledger,
        Err(failures) => return failures,
    };
    golden_tree_failures(
        name,
        &format!("{}, enum-type={enum_type}", spec.display()),
        &ledger,
        expected,
        out.path(),
    )
}

/// Each fixture's complete certified tree, Python enums and literals, byte-equal
/// to crozier's under the same setting through `src/parity.rs` and the
/// catalogued departures alone.
#[test]
fn union_shapes_match_complete_goldens_in_both_enum_modes() {
    let mut failures = Vec::new();
    for name in FIXTURES {
        let spec = fixture(name).join("openapi.yml");
        failures.extend(tree_failures(
            name,
            &spec,
            &fixture(name).join("fern-expected"),
            "python-enums",
        ));
        match literals_tree(name) {
            Ok(tree) => failures.extend(tree_failures(name, &spec, tree.path(), "literals")),
            Err(error) => failures.push(error),
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// The literals overlays are exactly the fixtures': one per fixture, and none
/// beside them where no test would read it.
#[test]
fn union_literals_overlays_are_exactly_the_fixtures() {
    let mut found: Vec<String> = std::fs::read_dir(repo_root().join(LITERALS_DIR))
        .expect("the literals overlays are committed")
        .map(|entry| {
            entry
                .expect("entry")
                .file_name()
                .to_string_lossy()
                .into_owned()
        })
        .filter(|name| name != "README.md")
        .collect();
    found.sort();
    assert_eq!(found, FIXTURES);
}

/// `fixture`'s document with `edit` applied, written to a scratch file.
fn edited(name: &str, edit: impl Fn(&str) -> String) -> (tempfile::TempDir, PathBuf) {
    let text = std::fs::read_to_string(fixture(name).join("openapi.yml")).expect("fixture");
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("openapi.yml");
    std::fs::write(&path, edit(&text)).expect("write the edited document");
    (dir, path)
}

/// Each `x-fern-<stem>: <value>` line of `text` respelled by `with`, which is
/// handed the line's indentation and value.
fn respell(text: &str, stem: &str, with: impl Fn(&str, &str) -> String) -> String {
    let key = format!("x-fern-{stem}: ");
    let mut seen = 0;
    let lines: Vec<String> = text
        .lines()
        .map(|line| match line.trim_start().strip_prefix(&key) {
            Some(value) => {
                seen += 1;
                with(&line[..line.len() - line.trim_start().len()], value)
            }
            None => line.to_string(),
        })
        .collect();
    assert!(seen > 0, "the fixture writes no {key}");
    lines.join("\n") + "\n"
}

/// The fixture's certified tree against crozier over `spec`, Python enums.
fn matches_golden(name: &str, spec: &Path) -> Vec<String> {
    tree_failures(
        name,
        spec,
        &fixture(name).join("fern-expected"),
        "python-enums",
    )
}

/// `x-crozier-discriminated` and the discriminator's `x-crozier-property-name`
/// are read exactly as their Fern spellings, and the crozier spelling wins when
/// a node carries both with different values: each edit below must still match
/// the tree Fern generated from the `x-fern-*` document, while the losing value
/// alone is shown to change the output.
#[test]
fn union_extension_aliases_match_and_win() {
    for (name, stem, losing) in [
        ("greenhouse-undiscriminated-unions", "discriminated", "true"),
        (
            "telescope-renamed-discriminant",
            "property-name",
            "signalKind",
        ),
    ] {
        let (_alias_dir, alias) = edited(name, |text| {
            respell(text, stem, |indent, value| {
                format!("{indent}x-crozier-{stem}: {value}")
            })
        });
        let failures = matches_golden(name, &alias);
        assert!(
            failures.is_empty(),
            "{name}, x-crozier-{stem}: {}",
            failures.join("\n")
        );

        let (_conflict_dir, conflict) = edited(name, |text| {
            respell(text, stem, |indent, value| {
                format!("{indent}x-fern-{stem}: {losing}\n{indent}x-crozier-{stem}: {value}")
            })
        });
        let failures = matches_golden(name, &conflict);
        assert!(
            failures.is_empty(),
            "{name}, both spellings: {}",
            failures.join("\n")
        );

        let (_losing_dir, losing_only) = edited(name, |text| {
            respell(text, stem, |indent, _| {
                format!("{indent}x-fern-{stem}: {losing}")
            })
        });
        assert!(
            !matches_golden(name, &losing_only).is_empty(),
            "{name}: x-fern-{stem}: {losing} alone generates the same tree, so the conflict \
             above proves nothing"
        );
    }
}

/// Both extensions are documented in the reference's vendor-extension table
/// under both spellings.
#[test]
fn union_extensions_are_documented_under_both_spellings() {
    let reference = std::fs::read_to_string(repo_root().join("docs/fern-reference.md"))
        .expect("docs/fern-reference.md");
    for stem in ["discriminated", "property-name"] {
        assert!(
            reference.lines().any(|row| row.starts_with('|')
                && row.contains(&format!("`x-fern-{stem}`"))
                && row.contains(&format!("`x-crozier-{stem}`"))
                && row.contains("iscriminat")),
            "docs/fern-reference.md has no vendor-extension row naming x-fern-{stem} and \
             x-crozier-{stem} for a discriminated union"
        );
    }
}

/// `union-value-wrapper-docs-example` accounts for the wrapper call alone: the
/// fixture's README matches Fern's under it, and the same README with one
/// adjacent line of the snippet changed (an argument of the method call the
/// wrapper sits in) still fails.
#[test]
fn union_value_wrapper_departure_is_scoped_to_the_wrapper_call() {
    let name = "kitchen-nested-mapping-target";
    let expected = fixture(name).join("fern-expected");
    let out = tempfile::tempdir().expect("tempdir");
    probe_command(&fixture(name).join("openapi.yml"), out.path())
        .assert()
        .success();
    let context = crozier::departures::Context::from_trees(&expected, out.path());
    let fern = std::fs::read_to_string(expected.join("README.md")).expect("README");
    let generated = std::fs::read_to_string(out.path().join("README.md")).expect("README");
    let compared = crozier::parity::compare_file(&context, "README.md", &generated, &fern)
        .expect("comparable");
    assert!(
        compared.matches(),
        "{}",
        compared.diff().unwrap_or_default()
    );
    assert!(
        generated.contains("value=SteakOrder(") && fern.contains("grill=,"),
        "the departure no longer has a wrapper call to account for"
    );
    let perturbed = generated.replacen(
        "client.fire_ticket(\n    request=Course_Grill(",
        "client.fire_ticket(\n    request_options=None,\n    request=Course_Grill(",
        1,
    );
    assert_ne!(
        perturbed, generated,
        "the perturbation must change the README"
    );
    let compared = crozier::parity::compare_file(&context, "README.md", &perturbed, &fern)
        .expect("comparable");
    assert!(
        !compared.matches(),
        "an unexplained line beside the wrapper call was accounted for"
    );
}

/// The refusals beside the shapes that now generate: a non-identifier
/// discriminant with no declared Python name is still refused, and the
/// union-member body is still refused when the operation is a POST, in both
/// modes, while the fixtures' own documents generate.
#[test]
fn union_refusal_controls_hold_beside_the_generating_shapes() {
    let crozier = super::crozier;
    let (_bare_dir, bare) = edited("telescope-renamed-discriminant", |text| {
        text.lines()
            .filter(|line| {
                !line
                    .trim_start()
                    .starts_with("x-fern-property-name: targetClass")
            })
            .collect::<Vec<_>>()
            .join("\n")
            + "\n"
    });
    let (_post_dir, post) = edited("bakery-get-body-member", |text| {
        text.replacen(
            "  /loaves/preview:\n    get:",
            "  /loaves/preview:\n    post:",
            1,
        )
    });
    for (spec, class, element) in [
        (
            &bare,
            "discriminant-value-unsuitable",
            "#/components/schemas/Target discriminant \"$class\"",
        ),
        (&post, "type-not-defined", "components/schemas/Loaf/oneOf/0"),
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, spec, strict).expect("crozier runs");
            let failures = refused_failures(class, &run, element, strict);
            assert!(failures.is_empty(), "{class}: {}", failures.join("\n"));
        }
    }
    for name in ["telescope-renamed-discriminant", "bakery-get-body-member"] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &fixture(name).join("openapi.yml"), strict)
                .expect("crozier runs");
            assert_eq!(run.code, Some(0), "{name}: {}", run.stderr);
            assert!(!run.files.is_empty(), "{name} wrote nothing");
        }
    }
}
