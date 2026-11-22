//! The invalid-example repairs through `crozier compare`, the interface a
//! migrating user checks crozier against their own Fern SDK with: the compiled
//! binary over a real temporary repository whose reference command writes a
//! reference tree. The reference is crozier's own tree with each repaired value
//! put back to what Fern writes there — the declared `42` beneath `maximum: 1`,
//! an empty tuple, an empty list of a recursive model and the import that does
//! not name it — or to a value the schema accepts, which is no defect.
//! `compare` must match the defect through the catalogued departures and
//! mismatch every non-defect, the boundary the departure rules hold.

use std::path::Path;

use super::crozier;

/// One operation whose body declares an example its schema rejects, a tuple
/// Fern has no item for, and a recursive list Fern stops at.
const SPEC: &str = "\
openapi: 3.1.0
info: {title: Plans, version: \"1\"}
paths:
  /plans:
    post:
      operationId: file_plan
      requestBody:
        required: true
        content:
          application/json:
            schema: {$ref: '#/components/schemas/Plan'}
      responses:
        '204': {description: Filed}
components:
  schemas:
    Plan:
      type: object
      required: [share, bounds, filter]
      properties:
        share: {type: number, maximum: 1, example: 42}
        bounds:
          type: array
          items: false
          minItems: 2
          maxItems: 2
          prefixItems: [{type: number}, {type: number}]
        filter: {$ref: '#/components/schemas/Filter'}
    Filter:
      type: object
      required: [all]
      properties:
        all:
          type: array
          minItems: 1
          items:
            anyOf:
              - {$ref: '#/components/schemas/Filter'}
              - type: object
                required: [field]
                properties:
                  field: {type: string}
";

/// `reference.sh MODE`: generate the tree with the crozier under test, then
/// write back what MODE says Fern writes in each worked example.
const REFERENCE: &str = r#"#!/bin/sh
set -eu
"$CROZIER_UNDER_TEST" generate python --spec openapi.yml --output "$CROZIER_REFERENCE_OUTPUT" \
  --package-name fern --project-name plans --no-config >/dev/null
python3 - "$CROZIER_REFERENCE_OUTPUT" "$1" <<'PY'
import pathlib, re, sys
root, mode = pathlib.Path(sys.argv[1]), sys.argv[2]
share = {"defect": "42", "valid-share": "0.5"}.get(mode)
bounds = {"defect": "[]", "valid-bounds": "[2.5, 3.5]"}.get(mode)
empty_filter = mode == "defect"
lose_import = mode in ("defect", "import-only")
for name in ("README.md", "reference.md", "src/fern/client.py"):
    path = root / name
    text = path.read_text()
    if share is not None:
        text = re.sub(r"share=1(\.0)?,", lambda m: f"share={share}{'.0' if m.group(1) and share == '42' else ''},", text)
    if bounds is not None:
        text = re.sub(r"bounds=\[[^\]]*\]", f"bounds={bounds}", text)
    if empty_filter:
        text = re.sub(r"all_=\[\s*FilterAllItemField\(\s*field=\"string\",\s*\)\s*\]", "all_=[]", text)
    if lose_import:
        text = text.replace(", Filter, FilterAllItemField", ", Filter")
    path.write_text(text)
PY
"#;

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().expect("a parent")).expect("mkdir");
    std::fs::write(path, text).expect("write");
}

#[cfg(unix)]
#[test]
fn compare_matches_fern_s_invalid_examples_through_their_departures_and_nothing_else() {
    use std::os::unix::fs::PermissionsExt;
    let repo = tempfile::tempdir().expect("repo tempdir");
    let root = repo.path();
    write(root, "openapi.yml", SPEC);
    write(root, "reference.sh", REFERENCE);
    std::fs::set_permissions(
        root.join("reference.sh"),
        std::fs::Permissions::from_mode(0o755),
    )
    .expect("chmod");
    let generators: String = ["defect", "valid-share", "valid-bounds", "import-only"]
        .iter()
        .map(|mode| format!("  {mode}:\n    reference:\n      command: ./reference.sh {mode}\n"))
        .collect();
    write(
        root,
        "crozier.yml",
        &format!(
            "spec: ./openapi.yml\noutput: ./sdk\npackage-name: fern\nproject-name: plans\n\
             generators:\n{generators}"
        ),
    );
    let output = crozier()
        .current_dir(root)
        .env("CROZIER_UNDER_TEST", super::crozier_bin())
        .env_remove("NO_COLOR")
        .env_remove("CLICOLOR_FORCE")
        .args(["compare", "--json", "-"])
        .output()
        .expect("compare runs");
    let report: serde_json::Value =
        serde_json::from_slice(&output.stdout).unwrap_or_else(|error| {
            panic!(
                "{error}: {}\n{}",
                String::from_utf8_lossy(&output.stdout),
                String::from_utf8_lossy(&output.stderr)
            )
        });
    assert_eq!(output.status.code(), Some(3), "{report:#}");
    let result = |generator: &str| {
        report["results"]
            .as_array()
            .expect("results")
            .iter()
            .find(|result| result["generator"] == generator)
            .unwrap_or_else(|| panic!("no result for {generator}: {report:#}"))
            .clone()
    };
    // Fern's defects are crozier's departures, each where it stands.
    let defect = result("defect");
    assert_eq!(defect["status"], "matched", "{defect:#}");
    let applied: Vec<(String, String)> = defect["comparison"]["departures"]
        .as_array()
        .expect("departures")
        .iter()
        .map(|found| {
            (
                found["id"].as_str().expect("an id").to_string(),
                found["file"].as_str().expect("a file").to_string(),
            )
        })
        .collect();
    for (id, file) in [
        ("schema-rejected-declared-example", "src/fern/client.py"),
        ("schema-rejected-declared-example", "README.md"),
        ("schema-rejected-array-length-example", "src/fern/client.py"),
        ("schema-rejected-array-length-example", "reference.md"),
    ] {
        assert!(
            applied.iter().any(|found| found.0 == id && found.1 == file),
            "{id} in {file}: {applied:?}"
        );
    }
    // A value the schema accepts in Fern's place is no defect to depart
    // from, and an import naming a model no seeded list builds is no repair.
    for (generator, differs) in [
        ("valid-share", "src/fern/client.py"),
        ("valid-bounds", "src/fern/client.py"),
        ("import-only", "src/fern/client.py"),
    ] {
        let found = result(generator);
        assert_eq!(found["status"], "mismatched", "{generator}: {found:#}");
        assert!(
            found["comparison"]["differing"]
                .as_array()
                .expect("differing")
                .iter()
                .any(|path| path == differs),
            "{generator}: {found:#}"
        );
    }
}
