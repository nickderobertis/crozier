//! The public JSON Schema for a `crozier.yml` config file.
//!
//! The schema is **derived from the config model** in [`crate::settings`] via
//! `schemars`, so field names and their doc comments come straight from the Rust
//! types — add a field and it appears in the schema automatically. It is
//! published at [`SCHEMA_URL`] (the bundled copy ships as
//! `assets/crozier.schema.json`), and [`crate::cli`]'s `init` writes a
//! `# yaml-language-server: $schema=…` modeline pointing at it, so editors with
//! the YAML language server give completion and validation for free.
//!
//! The committed asset is pinned to this generator by a test
//! (`committed_asset_matches_generated_schema`), so it can never drift: change
//! the model, regenerate the asset
//! (`CROZIER_UPDATE_SCHEMA=1 cargo test --lib schema`), and the test goes green.

use serde_json::Value;

use crate::settings::FileConfig;

/// Canonical public URL of the config JSON Schema, served from the repo's
/// `assets/` over raw.githubusercontent. Used as the schema's `$id` and as the
/// `$schema=` target written into configs by `crozier init`.
pub const SCHEMA_URL: &str =
    "https://raw.githubusercontent.com/nickderobertis/crozier/main/assets/crozier.schema.json";

/// The bundled JSON Schema, embedded at compile time so it ships in the crate
/// and is pinned to [`build`] by the drift test.
pub const BUNDLED: &str = include_str!("../assets/crozier.schema.json");

/// Canonical public URL of the `crozier compare --json` report's JSON Schema.
pub const COMPARE_REPORT_SCHEMA_URL: &str =
    "https://raw.githubusercontent.com/nickderobertis/crozier/main/assets/compare-report.schema.json";

/// The committed compare-report schema, pinned to [`compare_report`] by the drift
/// test.
pub const COMPARE_REPORT_BUNDLED: &str = include_str!("../assets/compare-report.schema.json");

/// Build the JSON Schema (2020-12) of the `crozier compare --json` report,
/// derived from [`crate::compare::report::Report`] and published with
/// [`COMPARE_REPORT_SCHEMA_URL`] as its `$id`.
#[must_use]
pub fn compare_report() -> Value {
    let mut schema = serde_json::to_value(schemars::schema_for!(crate::compare::report::Report))
        .expect("report schema serializes");
    if let Value::Object(map) = &mut schema {
        map.insert(
            "$id".to_string(),
            Value::String(COMPARE_REPORT_SCHEMA_URL.to_string()),
        );
        map.insert(
            "title".to_string(),
            Value::String("crozier compare report".to_string()),
        );
    }
    schema
}

/// Compare `generated` with the committed asset at `relative` (under the crate
/// root), rewriting the asset when `CROZIER_UPDATE_SCHEMA` is set and failing
/// otherwise.
#[cfg(test)]
fn assert_asset_matches(relative: &str, committed: &str, generated: &Value) {
    let committed: Value = serde_json::from_str(committed).expect("bundled schema is valid JSON");
    if &committed != generated {
        if std::env::var_os("CROZIER_UPDATE_SCHEMA").is_some() {
            let path = format!("{}/{relative}", env!("CARGO_MANIFEST_DIR"));
            let mut body = serde_json::to_string_pretty(generated).unwrap();
            body.push('\n');
            std::fs::write(path, body).unwrap();
            return;
        }
        panic!(
            "{relative} is out of sync with its Rust types; \
             regenerate with `CROZIER_UPDATE_SCHEMA=1 cargo test --lib schema`"
        );
    }
}

/// The `# yaml-language-server` modeline that points an editor at the published
/// schema. `crozier init` writes this as the first line of a generated config.
#[must_use]
pub fn modeline() -> String {
    format!("# yaml-language-server: $schema={SCHEMA_URL}\n")
}

/// Build the JSON Schema (2020-12) for a `crozier.yml`, derived from the
/// [`FileConfig`] model and published with [`SCHEMA_URL`] as its `$id`.
#[must_use]
pub fn build() -> Value {
    let mut schema =
        serde_json::to_value(schemars::schema_for!(FileConfig)).expect("config schema serializes");
    // schemars doesn't assign an `$id`; set it to the canonical published URL so
    // the schema is self-describing and tools can dereference it.
    if let Value::Object(map) = &mut schema {
        map.insert("$id".to_string(), Value::String(SCHEMA_URL.to_string()));
        map.insert(
            "title".to_string(),
            Value::String("crozier configuration".to_string()),
        );
    }
    schema
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn schema_describes_the_config_shape() {
        let s = build();
        assert_eq!(s["$id"], SCHEMA_URL);
        assert_eq!(s["type"], "object");
        let props = s["properties"].as_object().unwrap();
        for key in [
            "spec",
            "output",
            "package-name",
            "audiences",
            "layout",
            "generators",
        ] {
            assert!(props.contains_key(key), "missing property {key}");
        }
        // `generators` is an object whose values follow the generator schema, and
        // a generator's `type` enumerates the known kinds.
        assert_eq!(s["properties"]["generators"]["type"], "object");
    }

    #[test]
    fn modeline_targets_the_published_schema() {
        let line = modeline();
        assert!(line.starts_with("# yaml-language-server: $schema="));
        assert!(line.contains(SCHEMA_URL));
        assert!(line.ends_with('\n'));
    }

    /// The committed `assets/crozier.schema.json` is what gets published and
    /// referenced by `crozier init`; pin it to the generator so the two never
    /// drift. Set `CROZIER_UPDATE_SCHEMA=1` to rewrite the asset from the
    /// generator.
    #[test]
    fn committed_asset_matches_generated_schema() {
        assert_asset_matches("assets/crozier.schema.json", BUNDLED, &build());
    }

    /// The compare report is the contract CI consumers parse; its committed
    /// schema is pinned to the Rust types the same way.
    #[test]
    fn committed_compare_report_schema_matches_its_types() {
        assert_asset_matches(
            "assets/compare-report.schema.json",
            COMPARE_REPORT_BUNDLED,
            &compare_report(),
        );
    }

    #[test]
    fn compare_report_schema_states_the_contract() {
        let s = compare_report();
        assert_eq!(s["$id"], COMPARE_REPORT_SCHEMA_URL);
        let required: Vec<&str> = s["required"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_str().unwrap())
            .collect();
        for key in [
            "schema_version",
            "crozier_version",
            "searched_paths",
            "exit_code",
            "counts",
            "timing_totals",
            "results",
        ] {
            assert!(required.contains(&key), "{key} not required: {required:?}");
        }
        assert_eq!(s["properties"]["schema_version"]["const"], 2);
        assert_eq!(
            s["properties"]["exit_code"]["enum"],
            serde_json::json!([0, 3, 4])
        );
        let text = s.to_string();
        assert!(!text.to_lowercase().contains("fern"), "{text}");
    }
}
