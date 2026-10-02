//! `enum-type: literals` through the binary: its resolution through every
//! settings layer, its schema entry, and the SDK shape it writes. Its Fern
//! parity is proven by the overlay goldens in `overlay_goldens.rs`.

use std::path::Path;

/// One string enum, reached through a model field and an operation header.
pub(super) const ENUM_SPEC: &str = "openapi: 3.0.0
info:
  title: Pets
paths:
  /pets:
    get:
      operationId: getPet
      tags: [Pets]
      parameters:
        - name: X-Mode
          in: header
          required: true
          schema: { type: string, enum: [fast, slow] }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Pet' }
components:
  schemas:
    Status:
      type: string
      enum: [active, inactive]
    Pet:
      type: object
      required: [status]
      properties:
        status: { $ref: '#/components/schemas/Status' }
";

/// `crozier config`'s `enum-type` row for the python generator in `dir`:
/// `(value, source)`.
fn enum_type_row(dir: &Path, env: &[(&str, &str)]) -> (String, String) {
    let mut command = super::crozier_clean_env();
    command.current_dir(dir).arg("config");
    for (name, value) in env {
        command.env(name, value);
    }
    let out = command.output().expect("run crozier config");
    let stdout = String::from_utf8(out.stdout).expect("utf-8 stdout");
    assert!(out.status.success(), "{stdout}");
    super::config_rows(&stdout, "python")
        .into_iter()
        .find(|(field, _, _)| field == "enum-type")
        .map(|(_, value, source)| (value, source))
        .unwrap_or_else(|| panic!("`crozier config` printed no enum-type row:\n{stdout}"))
}

/// Which enum shape the SDK generated under `out` has, asserting every file the
/// setting decides agrees on it: the enum module, the `core/enum.py` runtime the
/// classes need, the header's serialization and the worked example.
fn written_enum_type(out: &Path) -> &'static str {
    let pkg = out.join("src/pets");
    let read = |rel: &str| std::fs::read_to_string(pkg.join(rel)).expect(rel);
    let status = read("types/status.py");
    let raw = read("pets/raw_client.py");
    let reference = std::fs::read_to_string(out.join("reference.md")).expect("reference.md");
    if status
        .contains("Status = typing.Union[typing.Literal[\"active\", \"inactive\"], typing.Any]")
    {
        assert!(
            !pkg.join("core/enum.py").exists(),
            "literals ship no StrEnum base"
        );
        assert!(
            raw.contains("\"X-Mode\": str(mode) if mode is not None else None"),
            "{raw}"
        );
        assert!(reference.contains("mode=\"fast\""), "{reference}");
        "literals"
    } else {
        assert!(status.contains("class Status(enum.StrEnum):"), "{status}");
        assert!(pkg.join("core/enum.py").is_file());
        assert!(
            raw.contains("\"X-Mode\": mode.value if mode is not None else None"),
            "{raw}"
        );
        assert!(
            reference.contains("mode=GetPetRequestXMode.FAST"),
            "{reference}"
        );
        "python-enums"
    }
}

/// `enum-type` resolves CLI > `CROZIER_ENUM_TYPE` > `generators.<name>` > the
/// built-in `python-enums`, like every Python-generator setting; `crozier config`
/// names the layer that won; it has no shared top-level form; and a bad value is
/// refused before anything is written.
#[test]
fn enum_type_resolves_through_every_layer_through_the_binary() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), ENUM_SPEC).unwrap();
    let config = dir.path().join("crozier.yml");
    let pair = |value: &str, source: &str| (value.to_string(), source.to_string());
    let generate = |env: &[(&str, &str)], args: &[&str], output: &str| {
        let mut command = super::crozier_clean_env();
        command.current_dir(dir.path());
        for (name, value) in env {
            command.env(name, value);
        }
        command
            .args(["generate", "python", "--output", output])
            .args(args)
            .assert()
            .success();
        written_enum_type(&dir.path().join(output))
    };

    // No layer: the built-in python-enums, unchanged.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n",
    )
    .unwrap();
    assert_eq!(
        enum_type_row(dir.path(), &[]),
        pair("python-enums", "default")
    );
    assert_eq!(generate(&[], &[], "default"), "python-enums");

    // The generator's own entry.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n    enum-type: literals\n",
    )
    .unwrap();
    assert_eq!(
        enum_type_row(dir.path(), &[]),
        pair("literals", "generator")
    );
    assert_eq!(generate(&[], &[], "generator"), "literals");

    // The environment beats the config file; the flag beats the environment.
    let env = [("CROZIER_ENUM_TYPE", "python-enums")];
    assert_eq!(enum_type_row(dir.path(), &env), pair("python-enums", "env"));
    assert_eq!(generate(&env, &[], "env"), "python-enums");
    assert_eq!(
        generate(&env, &["--enum-type", "literals"], "flag"),
        "literals"
    );

    // Python-generator-specific: a shared top-level value is a config error.
    std::fs::write(&config, "spec: ./api.yml\nenum-type: literals\n").unwrap();
    super::crozier_clean_env()
        .current_dir(dir.path())
        .arg("config")
        .assert()
        .failure()
        .stderr(predicates::str::contains("enum-type"));

    // A bad value is refused, from either layer, and writes nothing.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n",
    )
    .unwrap();
    super::crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_ENUM_TYPE", "python_enums")
        .args(["generate", "python", "--output", "bad-env"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicates::str::contains(
            "`CROZIER_ENUM_TYPE` must be `python-enums` or `literals`, got `python_enums`",
        ));
    super::crozier_clean_env()
        .current_dir(dir.path())
        .args([
            "generate",
            "python",
            "--output",
            "bad-flag",
            "--enum-type",
            "strict",
        ])
        .assert()
        .failure()
        .code(2)
        .stderr(predicates::str::contains("python-enums"));
    assert!(!dir.path().join("bad-env").exists());
    assert!(!dir.path().join("bad-flag").exists());
}

/// The published JSON Schema documents `enum-type` on a generator, with exactly
/// its two values.
#[test]
fn the_schema_documents_enum_type() {
    let out = super::crozier_clean_env()
        .arg("schema")
        .output()
        .expect("run crozier schema");
    assert!(out.status.success());
    let schema: serde_json::Value = serde_json::from_slice(&out.stdout).expect("schema JSON");
    let field = &schema["$defs"]["GeneratorSettings"]["properties"]["enum-type"];
    assert_eq!(field["anyOf"][0]["$ref"], "#/$defs/EnumType", "{field}");
    let values: Vec<&str> = schema["$defs"]["EnumType"]["oneOf"]
        .as_array()
        .expect("EnumType's values")
        .iter()
        .map(|value| value["const"].as_str().expect("a string value"))
        .collect();
    assert_eq!(values, ["python-enums", "literals"]);
    // Python-generator-specific: not a shared top-level field.
    assert!(schema["properties"].get("enum-type").is_none());
}
