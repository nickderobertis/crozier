//! crozier: generate SDKs from an OpenAPI document, matching Fern's output.
//!
//! The library is a small pipeline: [`openapi::load`] parses the document,
//! [`ir::build`] resolves it into a generation-ready [`ir::Ir`], and
//! [`emit::generate`] renders that IR to Python files with minijinja. The CLI
//! (`src/main.rs`) is a thin shell over [`generate`].
//!
//! # Stability
//!
//! **The product is the `crozier` binary, not this library.** The crate is
//! published to crates.io so `cargo install crozier` works and so the binary can
//! be built from a registry source; the library surface (including
//! [`strip_python_comments`], which exists to share one comment-stripper between
//! the CLI's hidden `internal-strip` subcommand and the e2e fixtures) is an
//! **internal API with no semver guarantee** — it may change in any release.
//! Depend on the CLI, not on these items.

pub mod cli;
pub mod config;
pub mod emit;
pub mod error;
pub mod ir;
pub mod naming;
pub mod normalize;
pub mod openapi;
pub mod pyfmt;
pub mod schema;
pub mod settings;
pub mod wrap;

pub use emit::GeneratedFile;
pub use error::{Error, Result};
pub use normalize::strip_python_comments;

use std::path::PathBuf;

use config::GenerateConfig;

/// Inputs for a generation run, mirroring the CLI's `generate` flags.
#[derive(Debug, Clone)]
pub struct GenerateArgs {
    /// Path to the OpenAPI document.
    pub spec: PathBuf,
    /// Output directory for the generated SDK.
    pub output: PathBuf,
    /// Override the Python package (import) name; defaults from the API title.
    pub package_name: Option<String>,
    /// Override the distribution name recorded in `version.py`.
    pub project_name: Option<String>,
    /// Override the generated root client class name (Fern's `client_class_name`);
    /// defaults to `{PascalCase(package_name)}Api`.
    pub client_class_name: Option<String>,
    /// `x-crozier-audiences` filter: when non-empty, prune generation to the
    /// operations carrying a matching audience (or none) plus the transitive
    /// schema closure they reference. Empty generates the whole API.
    pub audiences: Vec<String>,
    /// Strict audience subsetting: when `true`, un-annotated operations are
    /// excluded so only operations carrying a matching audience survive (Fern's
    /// exclusive behaviour). No effect when `audiences` is empty.
    pub audience_strict: bool,
    /// How generated pydantic models treat unknown fields (Fern's
    /// `pydantic_config.extra_fields`) — drives every model's `model_config` /
    /// `Config` `extra`.
    pub extra_fields: settings::ExtraFields,
}

/// Run the full pipeline: parse the spec, build the IR, render, and write files.
/// Returns the files written so the caller can report a count.
pub fn generate(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    let mut doc = openapi::load(&args.spec)?;
    openapi::filter_by_audience(&mut doc, &args.audiences, args.audience_strict);
    // The config constructor validates the package name (a `PackageName`), so an
    // invalid, traversal-prone value can never reach the filesystem below.
    let config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        args.client_class_name,
        args.extra_fields,
        &doc.info.title,
    )?;
    let ir = ir::build(&doc, &config);
    let files = emit::generate(&ir)?;
    // Regeneration is idempotent: clear the crozier-owned package tree first so a
    // schema or endpoint dropped from the spec does not leave an orphaned module.
    emit::clean_package_tree(&config.output, config.package_name.as_str())?;
    emit::write_files(&config.output, &files)?;
    Ok(files)
}

/// Render the files for a spec without writing them — used by tests to compare
/// generated contents against fixtures in-process.
pub fn render_files(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    let mut doc = openapi::load(&args.spec)?;
    openapi::filter_by_audience(&mut doc, &args.audiences, args.audience_strict);
    let config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        args.client_class_name,
        args.extra_fields,
        &doc.info.title,
    )?;
    let ir = ir::build(&doc, &config);
    emit::generate(&ir)
}
