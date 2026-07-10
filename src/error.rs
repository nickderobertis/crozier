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
}

/// Convenience alias for crozier results.
pub type Result<T> = std::result::Result<T, Error>;
