//! Error type for crozier. Every fallible boundary returns [`Error`]; the CLI
//! maps it to a non-zero exit and an actionable stderr message.

use std::path::PathBuf;

/// A crozier failure, always carrying enough context to act on.
#[derive(Debug, thiserror::Error)]
pub enum Error {
    /// The spec file could not be read.
    #[error("could not read spec {path}: {source}")]
    ReadSpec {
        /// The path that failed to read.
        path: PathBuf,
        /// The underlying IO error.
        source: std::io::Error,
    },

    /// The spec file has an extension crozier does not recognize.
    #[error("unsupported spec extension for {path}: expected .yml, .yaml, or .json")]
    UnknownSpecFormat {
        /// The offending path.
        path: PathBuf,
    },

    /// The spec could not be parsed as OpenAPI.
    #[error("could not parse OpenAPI document {path}: {message}")]
    ParseSpec {
        /// The path being parsed.
        path: PathBuf,
        /// A human-readable parse error.
        message: String,
    },

    /// The document is syntactically valid but not usable (e.g. wrong version).
    #[error("invalid OpenAPI document {path}: {message}")]
    InvalidSpec {
        /// The path being validated.
        path: PathBuf,
        /// What is wrong and, where possible, how to fix it.
        message: String,
    },

    /// The `--package-name` value is not a usable, safe package name.
    #[error(
        "invalid package name {name:?}: must be a single directory segment \
         (no path separators, no `..`); pass a simple name like `my_api`"
    )]
    InvalidPackageName {
        /// The rejected name.
        name: String,
    },

    /// Writing a generated file failed.
    #[error("could not write {path}: {source}")]
    WriteOutput {
        /// The output path that failed.
        path: PathBuf,
        /// The underlying IO error.
        source: std::io::Error,
    },

    /// A template failed to render — an internal bug, surfaced rather than panicked.
    #[error("template rendering failed for {file}: {message}")]
    Render {
        /// The logical output file being rendered.
        file: String,
        /// The template engine's message.
        message: String,
    },

    /// The `ruff` formatter could not be run, or rejected the generated source.
    /// crozier defers Python line-wrapping to `ruff format`, so a missing or
    /// failing `ruff` is a hard error with an actionable message.
    #[error("formatting {file} with ruff failed: {message}")]
    Format {
        /// The logical output file being formatted.
        file: String,
        /// What went wrong and how to fix it (e.g. install `ruff`).
        message: String,
    },

    /// A config file could not be read (a `--config` / `CROZIER_CONFIG` path, or
    /// a discovered `crozier.yml`).
    #[error("could not read config {path}: {source}")]
    ReadConfig {
        /// The config path that failed to read.
        path: PathBuf,
        /// The underlying IO error.
        source: std::io::Error,
    },

    /// An explicitly named config file (`--config` or `CROZIER_CONFIG`) does not
    /// exist. A *discovered* file that is absent is simply no config, not an
    /// error — only a file the user named is required to be there.
    #[error("config file not found: {path}")]
    ConfigNotFound {
        /// The named path that is missing.
        path: PathBuf,
    },

    /// A config file was read but is not valid (bad YAML, an unknown field, or an
    /// unknown generator type).
    #[error("invalid config {path}: {message}")]
    ParseConfig {
        /// The config path being parsed.
        path: PathBuf,
        /// A human-readable parse/validation error.
        message: String,
    },

    /// A `CROZIER_*` environment override could not be parsed (e.g. a
    /// non-boolean `CROZIER_AUDIENCE_STRICT`).
    #[error("invalid environment override: {message}")]
    InvalidEnvOverride {
        /// What is wrong and which variable it came from.
        message: String,
    },

    /// A generator was requested by name but is neither configured nor a built-in.
    #[error("unknown generator {name:?}; available: {available}")]
    UnknownGenerator {
        /// The requested generator name.
        name: String,
        /// The comma-separated names that could be run instead.
        available: String,
    },

    /// A generator has no OpenAPI spec after layering CLI, environment, and
    /// config — there is nothing to generate from.
    #[error(
        "generator {name:?} has no spec: set `spec` in a config file, \
         `CROZIER_SPEC`, or pass `--spec`"
    )]
    MissingSpec {
        /// The generator that is missing a spec.
        name: String,
    },

    /// A generator has no output directory after layering CLI, environment, and
    /// config — there is nowhere to write.
    #[error(
        "generator {name:?} has no output directory: set `output` in a config \
         file, `CROZIER_OUTPUT`, or pass `--output`"
    )]
    MissingOutput {
        /// The generator that is missing an output directory.
        name: String,
    },

    /// Per-generation CLI overrides (`--spec`/`--output`/…) were passed while
    /// more than one generator would run, so they cannot be attributed to one.
    #[error(
        "per-generation flags (--spec/--output/--package-name/--project-name/\
         --audience/--audience-strict) apply to a single generator, but {count} \
         would run; name one (e.g. `crozier generate <name>`) or set the values \
         in the config file"
    )]
    OverridesWithMultipleGenerators {
        /// How many generators the current selection would run.
        count: usize,
    },
}

/// Convenience alias for crozier results.
pub type Result<T> = std::result::Result<T, Error>;
