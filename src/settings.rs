//! Layered generation settings: the schema of `crozier.yml`, the pure
//! parse/validate/merge/resolve logic, and the file discovery that reads it.
//!
//! # The model
//!
//! crozier runs one or more **named generator instances**. A config file lists
//! them under `generators:`; each has an optional `type` (only `python` today,
//! the default) and its own generation settings. Top-level fields are *shared
//! defaults* every generator inherits unless it overrides them. A built-in
//! `python` generator always exists, so `crozier generate python` works with no
//! config at all; defining `python` in a config file overrides that built-in.
//!
//! # Precedence
//!
//! For every field, the value is resolved highest-wins:
//!
//! ```text
//! CLI flag  >  CROZIER_* env var  >  generators.<name>.<field>  >  top-level <field>  >  built-in default
//! ```
//!
//! The env layer and the layering are resolved here with no I/O (the env reader
//! is injected), so they are unit-testable; only [`load`]/[`discover`] touch the
//! filesystem.

use std::path::{Path, PathBuf};

use indexmap::IndexMap;
use schemars::JsonSchema;
use serde::Deserialize;

use crate::error::{Error, Result};
use crate::GenerateArgs;

/// The name of the built-in generator that exists with zero config, so
/// `crozier generate python` always resolves. A config file may define a
/// generator with this same name to override the built-in's defaults.
pub const BUILTIN_PYTHON: &str = "python";

/// Config file names auto-discovered in the working directory, in priority
/// order. Discovery is the working directory only — there is no walk up the
/// parent tree (a deliberate simplification over Fern's project layout).
pub const CONFIG_NAMES: &[&str] = &[
    "crozier.yml",
    "crozier.yaml",
    ".crozier.yml",
    ".crozier.yaml",
];

/// The kind of SDK a generator emits. Python is the only target today; the field
/// exists so a config can be explicit and forward-compatible, and so an unknown
/// value (a typo, or a target crozier does not have) fails loudly at parse time.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Deserialize, JsonSchema)]
#[serde(rename_all = "lowercase")]
pub enum GeneratorType {
    /// The Python generator.
    Python,
}

impl GeneratorType {
    /// The canonical lowercase name (`python`), matching the config value and
    /// the built-in generator's name.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            GeneratorType::Python => "python",
        }
    }
}

/// One generator's settings, as written under `generators.<name>` (or as the
/// top-level shared defaults, which share this shape minus `type`). Every field
/// is optional: an absent field falls through to the next layer down. Unknown
/// fields are rejected so a typo fails loudly instead of being ignored.
#[derive(Debug, Clone, Default, PartialEq, Deserialize, JsonSchema)]
#[serde(rename_all = "kebab-case", deny_unknown_fields)]
pub struct GeneratorSettings {
    /// The generator kind. Defaults to [`GeneratorType::Python`] when unset.
    #[serde(rename = "type")]
    pub generator_type: Option<GeneratorType>,
    /// Path to the OpenAPI document to read.
    pub spec: Option<PathBuf>,
    /// Directory to write the generated SDK into.
    pub output: Option<PathBuf>,
    /// Python package (import) name; defaults to a snake_case of the API title.
    pub package_name: Option<String>,
    /// Distribution name recorded in `version.py`; defaults to the package name.
    pub project_name: Option<String>,
    /// Root client class name (Fern's `client_class_name`); defaults to
    /// `{PascalCase(package_name)}Api`.
    pub client_class_name: Option<String>,
    /// `x-crozier-audiences` filter; empty generates the whole API.
    pub audiences: Option<Vec<String>>,
    /// Strict audience subsetting (exclude un-annotated operations).
    pub audience_strict: Option<bool>,
}

/// A parsed `crozier.yml`: the shared top-level defaults plus the named
/// generators. The top-level fields reuse [`GeneratorSettings`]' meaning but are
/// shared across every generator (the `type` there is ignored — it is per
/// generator). `generators` preserves declaration order so `crozier generate`
/// (no name) runs them deterministically in file order.
#[derive(Debug, Clone, Default, PartialEq, Deserialize, JsonSchema)]
#[serde(rename_all = "kebab-case", deny_unknown_fields)]
pub struct FileConfig {
    /// Shared default OpenAPI document for every generator.
    pub spec: Option<PathBuf>,
    /// Shared default output directory.
    pub output: Option<PathBuf>,
    /// Shared default Python package name.
    pub package_name: Option<String>,
    /// Shared default distribution name.
    pub project_name: Option<String>,
    /// Shared default root client class name.
    pub client_class_name: Option<String>,
    /// Shared default audience filter.
    pub audiences: Option<Vec<String>>,
    /// Shared default strict-audience flag.
    pub audience_strict: Option<bool>,
    /// The named generator instances (one SDK each), in declaration order.
    // Described to `schemars` as a plain string-keyed map (same JSON shape) so
    // the schema does not depend on the indexmap feature; serde keeps the
    // `IndexMap` at runtime so declaration order is preserved.
    #[serde(default)]
    #[schemars(with = "std::collections::BTreeMap<String, GeneratorSettings>")]
    pub generators: IndexMap<String, GeneratorSettings>,
}

/// Per-generation values supplied on the command line — the highest-precedence
/// layer. Every field is optional (absent means "not passed", which falls
/// through to the env/config layers).
#[derive(Debug, Clone, Default, PartialEq)]
pub struct CliOverrides {
    /// `--spec`.
    pub spec: Option<PathBuf>,
    /// `--output`.
    pub output: Option<PathBuf>,
    /// `--package-name`.
    pub package_name: Option<String>,
    /// `--project-name`.
    pub project_name: Option<String>,
    /// `--client-class-name`.
    pub client_class_name: Option<String>,
    /// `--audience` (repeatable); `None` when none were passed.
    pub audiences: Option<Vec<String>>,
    /// `--audience-strict`; `None` when the flag was absent.
    pub audience_strict: Option<bool>,
}

impl CliOverrides {
    /// Whether any per-generation override was supplied. Used to reject
    /// single-generator flags when more than one generator would run.
    #[must_use]
    pub fn is_empty(&self) -> bool {
        self.spec.is_none()
            && self.output.is_none()
            && self.package_name.is_none()
            && self.project_name.is_none()
            && self.client_class_name.is_none()
            && self.audiences.is_none()
            && self.audience_strict.is_none()
    }
}

/// The result of loading config files: the merged config plus the paths that
/// shaped it (for reporting which files a run consulted).
#[derive(Debug, Default)]
pub struct LoadedConfig {
    /// The layered configuration.
    pub config: FileConfig,
    /// The files loaded, in layering order (later wins).
    pub files: Vec<PathBuf>,
}

/// Parse one config file's text into a [`FileConfig`]. Pure: the caller attaches
/// the path to any error. Rejects unknown fields and unknown generator types.
pub fn parse(text: &str) -> std::result::Result<FileConfig, String> {
    let config: FileConfig = serde_yaml_ng::from_str(text).map_err(|e| e.to_string())?;
    validate(&config)?;
    Ok(config)
}

/// Validate a parsed config beyond what serde enforces structurally.
fn validate(config: &FileConfig) -> std::result::Result<(), String> {
    for name in config.generators.keys() {
        if name.trim().is_empty() {
            return Err("a generator name must be non-empty".to_string());
        }
    }
    Ok(())
}

/// Layer `over` on top of `base`: a field set in `over` wins; an absent one
/// falls through. Generators merge by name, then per field, so a later layer can
/// override a single field of a generator the earlier layer declared.
#[must_use]
pub fn merge(base: FileConfig, over: FileConfig) -> FileConfig {
    let mut generators = base.generators;
    for (name, o) in over.generators {
        let entry = generators.entry(name).or_default();
        *entry = merge_generator(std::mem::take(entry), o);
    }
    FileConfig {
        spec: over.spec.or(base.spec),
        output: over.output.or(base.output),
        package_name: over.package_name.or(base.package_name),
        project_name: over.project_name.or(base.project_name),
        client_class_name: over.client_class_name.or(base.client_class_name),
        audiences: over.audiences.or(base.audiences),
        audience_strict: over.audience_strict.or(base.audience_strict),
        generators,
    }
}

/// Per-field merge of one generator's settings (`over` wins per field).
fn merge_generator(base: GeneratorSettings, over: GeneratorSettings) -> GeneratorSettings {
    GeneratorSettings {
        generator_type: over.generator_type.or(base.generator_type),
        spec: over.spec.or(base.spec),
        output: over.output.or(base.output),
        package_name: over.package_name.or(base.package_name),
        project_name: over.project_name.or(base.project_name),
        client_class_name: over.client_class_name.or(base.client_class_name),
        audiences: over.audiences.or(base.audiences),
        audience_strict: over.audience_strict.or(base.audience_strict),
    }
}

/// Build the environment-override layer from the `CROZIER_*` variables, read
/// through `get` (injected so this stays pure and unit-testable). Empty values
/// count as unset. A malformed value (a non-boolean `CROZIER_AUDIENCE_STRICT`)
/// fails loudly, exactly like a malformed file. The overrides are shared across
/// every selected generator — there is no per-generator env form by design.
///
/// Names mirror the config fields and CLI flags: `CROZIER_SPEC`,
/// `CROZIER_OUTPUT`, `CROZIER_PACKAGE_NAME`, `CROZIER_PROJECT_NAME`,
/// `CROZIER_CLIENT_CLASS_NAME`, `CROZIER_AUDIENCES` (comma-separated),
/// `CROZIER_AUDIENCE_STRICT`.
pub fn env_overrides(get: impl Fn(&str) -> Option<String>) -> Result<GeneratorSettings> {
    let read = |name: &str| get(name).filter(|v| !v.is_empty());

    let audience_strict = match read("CROZIER_AUDIENCE_STRICT") {
        None => None,
        Some(v) => Some(parse_bool(&v).ok_or_else(|| Error::InvalidEnvOverride {
            message: format!("`CROZIER_AUDIENCE_STRICT` must be `true` or `false`, got `{v}`"),
        })?),
    };
    let audiences = read("CROZIER_AUDIENCES").map(|v| split_list(&v));

    Ok(GeneratorSettings {
        generator_type: None,
        spec: read("CROZIER_SPEC").map(PathBuf::from),
        output: read("CROZIER_OUTPUT").map(PathBuf::from),
        package_name: read("CROZIER_PACKAGE_NAME"),
        project_name: read("CROZIER_PROJECT_NAME"),
        client_class_name: read("CROZIER_CLIENT_CLASS_NAME"),
        audiences,
        audience_strict,
    })
}

/// Parse a permissive boolean (`true`/`false`/`1`/`0`, case-insensitive).
fn parse_bool(v: &str) -> Option<bool> {
    match v.to_ascii_lowercase().as_str() {
        "true" | "1" => Some(true),
        "false" | "0" => Some(false),
        _ => None,
    }
}

/// Split a comma-separated list, trimming each entry and dropping empties.
fn split_list(v: &str) -> Vec<String> {
    v.split(',')
        .map(str::trim)
        .filter(|s| !s.is_empty())
        .map(str::to_string)
        .collect()
}

/// The generators to run for a selection. `Some(name)` runs exactly that one
/// (a config-defined generator, or the built-in `python`); `None` runs every
/// configured generator, or the built-in `python` when none are configured — so
/// bare `crozier` / `crozier generate` always has something to do.
pub fn run_set(config: &FileConfig, selected: Option<&str>) -> Result<Vec<String>> {
    match selected {
        Some(name) => {
            if config.generators.contains_key(name) || name == BUILTIN_PYTHON {
                Ok(vec![name.to_string()])
            } else {
                Err(Error::UnknownGenerator {
                    name: name.to_string(),
                    available: available_names(config),
                })
            }
        }
        None => {
            if config.generators.is_empty() {
                Ok(vec![BUILTIN_PYTHON.to_string()])
            } else {
                Ok(config.generators.keys().cloned().collect())
            }
        }
    }
}

/// The names a user could select, for the "unknown generator" error: every
/// configured generator plus the built-in `python` (unless overridden).
fn available_names(config: &FileConfig) -> String {
    let mut names: Vec<&str> = config.generators.keys().map(String::as_str).collect();
    if !config.generators.contains_key(BUILTIN_PYTHON) {
        names.push(BUILTIN_PYTHON);
    }
    names.join(", ")
}

/// Resolve one generator's effective [`GenerateArgs`] by layering CLI over env
/// over per-generator config over the shared top-level over the built-in
/// defaults. `spec` and `output` are required — a generator resolved without
/// either is an actionable error, not a silent no-op.
pub fn resolve(
    name: &str,
    config: &FileConfig,
    env: &GeneratorSettings,
    cli: &CliOverrides,
) -> Result<GenerateArgs> {
    let per = config.generators.get(name);

    let spec = cli
        .spec
        .clone()
        .or_else(|| env.spec.clone())
        .or_else(|| per.and_then(|p| p.spec.clone()))
        .or_else(|| config.spec.clone())
        .ok_or_else(|| Error::MissingSpec {
            name: name.to_string(),
        })?;
    let output = cli
        .output
        .clone()
        .or_else(|| env.output.clone())
        .or_else(|| per.and_then(|p| p.output.clone()))
        .or_else(|| config.output.clone())
        .ok_or_else(|| Error::MissingOutput {
            name: name.to_string(),
        })?;
    let package_name = cli
        .package_name
        .clone()
        .or_else(|| env.package_name.clone())
        .or_else(|| per.and_then(|p| p.package_name.clone()))
        .or_else(|| config.package_name.clone());
    let project_name = cli
        .project_name
        .clone()
        .or_else(|| env.project_name.clone())
        .or_else(|| per.and_then(|p| p.project_name.clone()))
        .or_else(|| config.project_name.clone());
    let client_class_name = cli
        .client_class_name
        .clone()
        .or_else(|| env.client_class_name.clone())
        .or_else(|| per.and_then(|p| p.client_class_name.clone()))
        .or_else(|| config.client_class_name.clone());
    let audiences = cli
        .audiences
        .clone()
        .or_else(|| env.audiences.clone())
        .or_else(|| per.and_then(|p| p.audiences.clone()))
        .or_else(|| config.audiences.clone())
        .unwrap_or_default();
    let audience_strict = cli
        .audience_strict
        .or(env.audience_strict)
        .or(per.and_then(|p| p.audience_strict))
        .or(config.audience_strict)
        .unwrap_or(false);

    Ok(GenerateArgs {
        spec,
        output,
        package_name,
        project_name,
        client_class_name,
        audiences,
        audience_strict,
    })
}

/// Which layer supplied a resolved value, for `crozier config`.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Source {
    /// A command-line flag.
    Cli,
    /// A `CROZIER_*` environment variable.
    Env,
    /// The generator's own `generators.<name>` entry.
    Generator,
    /// The shared top-level config value.
    Shared,
    /// The built-in default (no layer supplied a value).
    Default,
}

impl Source {
    /// A short label for display (`cli`, `env`, `generator`, `shared`,
    /// `default`).
    #[must_use]
    pub fn label(self) -> &'static str {
        match self {
            Source::Cli => "cli",
            Source::Env => "env",
            Source::Generator => "generator",
            Source::Shared => "shared",
            Source::Default => "default",
        }
    }
}

/// One resolved field for `crozier config`: its display value (or `None` when
/// unset everywhere) and the layer that supplied it.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct FieldSource {
    /// The field name as written in a config file (kebab-case).
    pub field: &'static str,
    /// The effective value rendered for display, or `None` when unset.
    pub value: Option<String>,
    /// Where the value came from.
    pub source: Source,
}

/// The first layer to supply a value wins; record which one did. Falls to
/// [`Source::Default`] when every layer is empty.
fn pick(layers: &[(Source, Option<String>)]) -> (Option<String>, Source) {
    for (src, val) in layers {
        if let Some(v) = val {
            return (Some(v.clone()), *src);
        }
    }
    (None, Source::Default)
}

/// One field's precedence chain, as display strings, from a value-extractor.
fn field(
    name: &'static str,
    cli: Option<String>,
    env: Option<String>,
    gen_val: Option<String>,
    shared: Option<String>,
) -> FieldSource {
    let (value, source) = pick(&[
        (Source::Cli, cli),
        (Source::Env, env),
        (Source::Generator, gen_val),
        (Source::Shared, shared),
    ]);
    FieldSource {
        field: name,
        value,
        source,
    }
}

/// Explain how each field of one generator resolves, without requiring `spec`
/// or `output` — the inspection counterpart of [`resolve`], used by
/// `crozier config`. `type` always resolves (defaulting to `python`).
pub fn explain(
    name: &str,
    config: &FileConfig,
    env: &GeneratorSettings,
    cli: &CliOverrides,
) -> Vec<FieldSource> {
    let per = config.generators.get(name);
    let path = |p: &PathBuf| p.display().to_string();
    let list = |v: &[String]| {
        if v.is_empty() {
            "[]".to_string()
        } else {
            v.join(", ")
        }
    };

    // `type` has no CLI/env form and defaults to `python`.
    let type_field = {
        let (value, source) = pick(&[(
            Source::Generator,
            per.and_then(|p| p.generator_type)
                .map(|t| t.as_str().to_string()),
        )]);
        match value {
            Some(v) => FieldSource {
                field: "type",
                value: Some(v),
                source,
            },
            None => FieldSource {
                field: "type",
                value: Some(BUILTIN_PYTHON.to_string()),
                source: Source::Default,
            },
        }
    };

    vec![
        type_field,
        field(
            "spec",
            cli.spec.as_ref().map(path),
            env.spec.as_ref().map(path),
            per.and_then(|p| p.spec.as_ref()).map(path),
            config.spec.as_ref().map(path),
        ),
        field(
            "output",
            cli.output.as_ref().map(path),
            env.output.as_ref().map(path),
            per.and_then(|p| p.output.as_ref()).map(path),
            config.output.as_ref().map(path),
        ),
        field(
            "package-name",
            cli.package_name.clone(),
            env.package_name.clone(),
            per.and_then(|p| p.package_name.clone()),
            config.package_name.clone(),
        ),
        field(
            "project-name",
            cli.project_name.clone(),
            env.project_name.clone(),
            per.and_then(|p| p.project_name.clone()),
            config.project_name.clone(),
        ),
        field(
            "client-class-name",
            cli.client_class_name.clone(),
            env.client_class_name.clone(),
            per.and_then(|p| p.client_class_name.clone()),
            config.client_class_name.clone(),
        ),
        field(
            "audiences",
            cli.audiences.as_deref().map(list),
            env.audiences.as_deref().map(list),
            per.and_then(|p| p.audiences.as_deref()).map(list),
            config.audiences.as_deref().map(list),
        ),
        field(
            "audience-strict",
            cli.audience_strict.map(|b| b.to_string()),
            env.audience_strict.map(|b| b.to_string()),
            per.and_then(|p| p.audience_strict).map(|b| b.to_string()),
            config.audience_strict.map(|b| b.to_string()),
        ),
    ]
}

/// The first config file present in `dir`, by [`CONFIG_NAMES`] priority. No walk
/// up the parent tree — discovery is the working directory only.
#[must_use]
pub fn discover(dir: &Path) -> Option<PathBuf> {
    CONFIG_NAMES
        .iter()
        .map(|name| dir.join(name))
        .find(|path| path.is_file())
}

/// Load the effective config for a run.
///
/// - `no_config` loads nothing — only CLI flags, env overrides, and built-in
///   defaults shape the run.
/// - A non-empty `explicit` (from `--config`, repeatable, or a single
///   `CROZIER_CONFIG`) loads exactly those files in order (later wins), and a
///   missing one is an error since the user named it.
/// - Otherwise the single discovered file in `dir` is loaded, if any; a missing
///   discovered file is simply no config, not an error.
pub fn load(explicit: &[PathBuf], no_config: bool, dir: &Path) -> Result<LoadedConfig> {
    let mut loaded = LoadedConfig::default();
    if no_config {
        return Ok(loaded);
    }
    if explicit.is_empty() {
        if let Some(path) = discover(dir) {
            loaded.config = read_config(&path)?;
            loaded.files.push(path);
        }
    } else {
        for path in explicit {
            loaded.config = merge(loaded.config, read_config(path)?);
            loaded.files.push(path.clone());
        }
    }
    Ok(loaded)
}

/// Read and parse a config file, mapping IO and parse failures to actionable
/// errors that carry the path. A not-found path is [`Error::ConfigNotFound`] so
/// an explicitly named, missing file reads clearly.
fn read_config(path: &Path) -> Result<FileConfig> {
    let text = std::fs::read_to_string(path).map_err(|source| {
        if source.kind() == std::io::ErrorKind::NotFound {
            Error::ConfigNotFound {
                path: path.to_path_buf(),
            }
        } else {
            Error::ReadConfig {
                path: path.to_path_buf(),
                source,
            }
        }
    })?;
    parse(&text).map_err(|message| Error::ParseConfig {
        path: path.to_path_buf(),
        message,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn parsed(text: &str) -> FileConfig {
        parse(text).expect("config should parse")
    }

    #[test]
    fn empty_config_is_all_defaults() {
        assert_eq!(parsed(""), FileConfig::default());
    }

    #[test]
    fn full_config_round_trips() {
        let c = parsed(
            "spec: ./api.yml\naudiences: [public]\naudience-strict: true\n\ngenerators:\n  python:\n    output: ./sdks/py\n    package-name: my_api\n    project-name: my-api\n  admin:\n    type: python\n    spec: ./admin.yml\n    output: ./sdks/admin\n",
        );
        assert_eq!(c.spec.as_deref(), Some(Path::new("./api.yml")));
        assert_eq!(c.audiences.as_deref().unwrap(), ["public"]);
        assert_eq!(c.audience_strict, Some(true));
        assert_eq!(c.generators.len(), 2);
        // Declaration order is preserved (python before admin).
        let names: Vec<&str> = c.generators.keys().map(String::as_str).collect();
        assert_eq!(names, ["python", "admin"]);
        let py = &c.generators["python"];
        assert_eq!(py.output.as_deref(), Some(Path::new("./sdks/py")));
        assert_eq!(py.package_name.as_deref(), Some("my_api"));
        assert_eq!(
            c.generators["admin"].generator_type,
            Some(GeneratorType::Python)
        );
    }

    #[test]
    fn unknown_top_level_field_is_rejected() {
        let err = parse("spac: ./x.yml").unwrap_err();
        assert!(err.contains("spac"), "{err}");
    }

    #[test]
    fn unknown_generator_field_is_rejected() {
        let err = parse("generators:\n  python:\n    packge-name: x").unwrap_err();
        assert!(err.contains("packge-name"), "{err}");
    }

    #[test]
    fn unknown_generator_type_is_rejected() {
        let err = parse("generators:\n  ts:\n    type: typescript").unwrap_err();
        assert!(
            err.contains("typescript") || err.contains("python"),
            "{err}"
        );
    }

    #[test]
    fn merge_prefers_over_per_field_and_falls_through() {
        let merged = merge(
            parsed("spec: ./base.yml\npackage-name: base"),
            parsed("package-name: over"),
        );
        assert_eq!(merged.spec.as_deref(), Some(Path::new("./base.yml")));
        assert_eq!(merged.package_name.as_deref(), Some("over"));
    }

    #[test]
    fn merge_generators_by_name_then_field() {
        let base = parsed("generators:\n  python:\n    output: ./a\n    package-name: keep");
        let over = parsed("generators:\n  python:\n    output: ./b\n  extra:\n    spec: ./e.yml");
        let merged = merge(base, over);
        let py = &merged.generators["python"];
        assert_eq!(py.output.as_deref(), Some(Path::new("./b")));
        assert_eq!(py.package_name.as_deref(), Some("keep"));
        assert!(merged.generators.contains_key("extra"));
    }

    fn env_get<'a>(pairs: &'a [(&'a str, &'a str)]) -> impl Fn(&str) -> Option<String> + 'a {
        move |name: &str| {
            pairs
                .iter()
                .find(|(k, _)| *k == name)
                .map(|(_, v)| v.to_string())
        }
    }

    #[test]
    fn env_overrides_map_every_field() {
        let e = env_overrides(env_get(&[
            ("CROZIER_SPEC", "./e.yml"),
            ("CROZIER_OUTPUT", "./out"),
            ("CROZIER_PACKAGE_NAME", "pkg"),
            ("CROZIER_PROJECT_NAME", "proj"),
            ("CROZIER_AUDIENCES", "public, internal"),
            ("CROZIER_AUDIENCE_STRICT", "true"),
        ]))
        .unwrap();
        assert_eq!(e.spec.as_deref(), Some(Path::new("./e.yml")));
        assert_eq!(e.output.as_deref(), Some(Path::new("./out")));
        assert_eq!(e.package_name.as_deref(), Some("pkg"));
        assert_eq!(e.project_name.as_deref(), Some("proj"));
        assert_eq!(e.audiences.as_deref().unwrap(), ["public", "internal"]);
        assert_eq!(e.audience_strict, Some(true));
    }

    #[test]
    fn env_empty_values_are_unset() {
        let e = env_overrides(env_get(&[
            ("CROZIER_SPEC", ""),
            ("CROZIER_PACKAGE_NAME", ""),
        ]))
        .unwrap();
        assert_eq!(e, GeneratorSettings::default());
    }

    #[test]
    fn env_bad_boolean_is_rejected() {
        let err = env_overrides(env_get(&[("CROZIER_AUDIENCE_STRICT", "maybe")])).unwrap_err();
        assert!(err.to_string().contains("CROZIER_AUDIENCE_STRICT"), "{err}");
    }

    #[test]
    fn run_set_named_config_generator() {
        let c = parsed("generators:\n  admin:\n    spec: ./a.yml");
        assert_eq!(run_set(&c, Some("admin")).unwrap(), ["admin"]);
    }

    #[test]
    fn run_set_builtin_python_needs_no_config() {
        assert_eq!(
            run_set(&FileConfig::default(), Some("python")).unwrap(),
            ["python"]
        );
    }

    #[test]
    fn run_set_unknown_generator_lists_available() {
        let c = parsed("generators:\n  admin:\n    spec: ./a.yml");
        let err = run_set(&c, Some("nope")).unwrap_err().to_string();
        assert!(err.contains("nope"), "{err}");
        assert!(err.contains("admin") && err.contains("python"), "{err}");
    }

    #[test]
    fn run_set_none_runs_all_configured_in_order() {
        let c = parsed("generators:\n  a:\n    spec: ./a.yml\n  b:\n    spec: ./b.yml");
        assert_eq!(run_set(&c, None).unwrap(), ["a", "b"]);
    }

    #[test]
    fn run_set_none_falls_back_to_builtin_python() {
        assert_eq!(run_set(&FileConfig::default(), None).unwrap(), ["python"]);
    }

    #[test]
    fn resolve_layers_cli_over_env_over_per_gen_over_top() {
        let config = parsed(
            "spec: ./top.yml\npackage-name: top\n\ngenerators:\n  python:\n    spec: ./gen.yml\n    output: ./gen-out\n    package-name: gen",
        );
        let env = env_overrides(env_get(&[("CROZIER_PACKAGE_NAME", "env")])).unwrap();
        let cli = CliOverrides {
            output: Some(PathBuf::from("./cli-out")),
            ..CliOverrides::default()
        };
        let args = resolve("python", &config, &env, &cli).unwrap();
        // spec: per-gen beats top (no cli/env spec).
        assert_eq!(args.spec, PathBuf::from("./gen.yml"));
        // output: cli beats per-gen.
        assert_eq!(args.output, PathBuf::from("./cli-out"));
        // package-name: env beats per-gen and top.
        assert_eq!(args.package_name.as_deref(), Some("env"));
    }

    #[test]
    fn resolve_uses_top_level_for_builtin_python() {
        let config = parsed("spec: ./top.yml\noutput: ./top-out");
        let args = resolve(
            "python",
            &config,
            &GeneratorSettings::default(),
            &CliOverrides::default(),
        )
        .unwrap();
        assert_eq!(args.spec, PathBuf::from("./top.yml"));
        assert_eq!(args.output, PathBuf::from("./top-out"));
        assert_eq!(args.package_name, None);
        assert!(!args.audience_strict);
        assert!(args.audiences.is_empty());
    }

    #[test]
    fn resolve_missing_spec_and_output_error() {
        let empty = FileConfig::default();
        let env = GeneratorSettings::default();
        let cli = CliOverrides::default();
        let err = resolve("python", &empty, &env, &cli)
            .unwrap_err()
            .to_string();
        assert!(err.contains("no spec"), "{err}");

        let with_spec = parsed("spec: ./x.yml");
        let err = resolve("python", &with_spec, &env, &cli)
            .unwrap_err()
            .to_string();
        assert!(err.contains("no output"), "{err}");
    }

    #[test]
    fn cli_overrides_is_empty() {
        assert!(CliOverrides::default().is_empty());
        assert!(!CliOverrides {
            audience_strict: Some(true),
            ..CliOverrides::default()
        }
        .is_empty());
    }

    #[test]
    fn discover_finds_first_by_priority() {
        let dir = tempfile::tempdir().unwrap();
        assert!(discover(dir.path()).is_none());
        std::fs::write(dir.path().join(".crozier.yml"), "spec: ./a.yml").unwrap();
        assert_eq!(
            discover(dir.path()).unwrap(),
            dir.path().join(".crozier.yml")
        );
        // The non-dotted name outranks the dotted one.
        std::fs::write(dir.path().join("crozier.yml"), "spec: ./b.yml").unwrap();
        assert_eq!(
            discover(dir.path()).unwrap(),
            dir.path().join("crozier.yml")
        );
    }

    #[test]
    fn load_no_config_is_empty() {
        let dir = tempfile::tempdir().unwrap();
        std::fs::write(dir.path().join("crozier.yml"), "spec: ./a.yml").unwrap();
        let loaded = load(&[], true, dir.path()).unwrap();
        assert_eq!(loaded.config, FileConfig::default());
        assert!(loaded.files.is_empty());
    }

    #[test]
    fn load_discovers_in_dir() {
        let dir = tempfile::tempdir().unwrap();
        std::fs::write(dir.path().join("crozier.yml"), "spec: ./a.yml").unwrap();
        let loaded = load(&[], false, dir.path()).unwrap();
        assert_eq!(loaded.config.spec.as_deref(), Some(Path::new("./a.yml")));
        assert_eq!(loaded.files, [dir.path().join("crozier.yml")]);
    }

    #[test]
    fn load_explicit_files_layer_in_order() {
        let dir = tempfile::tempdir().unwrap();
        let a = dir.path().join("a.yml");
        let b = dir.path().join("b.yml");
        std::fs::write(&a, "spec: ./a.yml\npackage-name: a").unwrap();
        std::fs::write(&b, "package-name: b").unwrap();
        let loaded = load(&[a.clone(), b.clone()], false, dir.path()).unwrap();
        // Later file wins per field; the earlier's other fields survive.
        assert_eq!(loaded.config.package_name.as_deref(), Some("b"));
        assert_eq!(loaded.config.spec.as_deref(), Some(Path::new("./a.yml")));
        assert_eq!(loaded.files, [a, b]);
    }

    #[test]
    fn load_explicit_missing_file_errors() {
        let dir = tempfile::tempdir().unwrap();
        let missing = dir.path().join("nope.yml");
        let err = load(&[missing], false, dir.path()).unwrap_err().to_string();
        assert!(err.contains("not found"), "{err}");
    }

    #[test]
    fn load_invalid_file_carries_path() {
        let dir = tempfile::tempdir().unwrap();
        let path = dir.path().join("crozier.yml");
        std::fs::write(&path, "spec: [not, a, scalar]\nbogus: 1").unwrap();
        let err = load(&[], false, dir.path()).unwrap_err().to_string();
        assert!(err.contains("crozier.yml"), "{err}");
    }

    #[test]
    fn load_unreadable_file_surfaces_a_read_error() {
        // A directory passed as a config path is not "not found": reading it fails
        // with a different IO kind, which maps to the read (not not-found) error.
        let dir = tempfile::tempdir().unwrap();
        let err = load(&[dir.path().to_path_buf()], false, dir.path())
            .unwrap_err()
            .to_string();
        assert!(err.contains("could not read config"), "{err}");
    }

    #[test]
    fn env_boolean_accepts_permissive_spellings() {
        for (raw, expected) in [("false", false), ("0", false), ("1", true)] {
            let e = env_overrides(env_get(&[("CROZIER_AUDIENCE_STRICT", raw)])).unwrap();
            assert_eq!(e.audience_strict, Some(expected), "{raw}");
        }
    }

    #[test]
    fn available_names_omits_a_configured_python() {
        // When a config defines `python`, it is not appended a second time as the
        // built-in in the "unknown generator" message.
        let c = parsed("generators:\n  python:\n    spec: ./a.yml");
        let err = run_set(&c, Some("nope")).unwrap_err().to_string();
        assert_eq!(err.matches("python").count(), 1, "{err}");
    }

    fn field_of<'a>(report: &'a [FieldSource], name: &str) -> &'a FieldSource {
        report
            .iter()
            .find(|f| f.field == name)
            .expect("field present")
    }

    #[test]
    fn explain_attributes_each_field_to_its_layer() {
        let config = parsed(
            "spec: ./top.yml\npackage-name: top\ngenerators:\n  python:\n    output: ./gen-out\n    package-name: gen",
        );
        let env = env_overrides(env_get(&[("CROZIER_PROJECT_NAME", "envproj")])).unwrap();
        let cli = CliOverrides {
            spec: Some(PathBuf::from("./cli.yml")),
            ..CliOverrides::default()
        };
        let report = explain("python", &config, &env, &cli);

        let spec = field_of(&report, "spec");
        assert_eq!(spec.value.as_deref(), Some("./cli.yml"));
        assert_eq!(spec.source, Source::Cli);

        let output = field_of(&report, "output");
        assert_eq!(output.value.as_deref(), Some("./gen-out"));
        assert_eq!(output.source, Source::Generator);

        // per-generator `package-name` beats the shared top-level.
        let pkg = field_of(&report, "package-name");
        assert_eq!(pkg.value.as_deref(), Some("gen"));
        assert_eq!(pkg.source, Source::Generator);

        let proj = field_of(&report, "project-name");
        assert_eq!(proj.value.as_deref(), Some("envproj"));
        assert_eq!(proj.source, Source::Env);
    }

    #[test]
    fn client_class_name_layers_and_resolves() {
        // Layers like any scalar (per-gen beats shared) and reaches GenerateArgs.
        let config = parsed(
            "client-class-name: SharedApi\ngenerators:\n  python:\n    spec: ./a.yml\n    output: ./o\n    client-class-name: GenApi",
        );
        let args = resolve(
            "python",
            &config,
            &GeneratorSettings::default(),
            &CliOverrides::default(),
        )
        .unwrap();
        assert_eq!(args.client_class_name.as_deref(), Some("GenApi"));

        // CLI and env win over the config, and `explain` attributes the source.
        let env = env_overrides(env_get(&[("CROZIER_CLIENT_CLASS_NAME", "EnvApi")])).unwrap();
        let report = explain("python", &config, &env, &CliOverrides::default());
        let ccn = field_of(&report, "client-class-name");
        assert_eq!(ccn.value.as_deref(), Some("EnvApi"));
        assert_eq!(ccn.source, Source::Env);
    }

    #[test]
    fn explain_defaults_type_and_unset_fields() {
        let report = explain(
            "python",
            &FileConfig::default(),
            &GeneratorSettings::default(),
            &CliOverrides::default(),
        );
        let ty = field_of(&report, "type");
        assert_eq!(ty.value.as_deref(), Some("python"));
        assert_eq!(ty.source, Source::Default);
        // spec/output are unset everywhere → no value, default source.
        let spec = field_of(&report, "spec");
        assert_eq!(spec.value, None);
        assert_eq!(spec.source, Source::Default);
        // audiences render as `[]` only when a layer sets them; unset stays None.
        assert_eq!(field_of(&report, "audiences").value, None);
        assert_eq!(field_of(&report, "audience-strict").source, Source::Default);
        // Every source has a stable label.
        assert_eq!(Source::Cli.label(), "cli");
        assert_eq!(Source::Shared.label(), "shared");
    }
}
