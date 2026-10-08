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

/// The version Cargo built this crate as — what `crozier --version` prints.
pub const VERSION: &str = env!("CARGO_PKG_VERSION");

pub mod cli;
pub mod compare;
pub mod config;
pub mod departures;
pub mod document_refusals;
pub mod emit;
pub mod error;
pub mod ir;
mod name_refusals;
pub mod naming;
pub mod normalize;
pub mod openapi;
pub mod parity;
pub mod pyfmt;
pub mod refs;
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
    /// How string enums are generated (Fern's `pydantic_config.enum_type`):
    /// `enum.StrEnum` classes or open `typing.Literal` unions.
    pub enum_type: settings::EnumType,
    /// The client's default maximum number of retries for a failed request
    /// (Fern's `default_max_retries`); Fern's default is 2.
    pub default_max_retries: u32,
    /// Strict Fern compatibility (`--fern-strict`): refuse, as Fern does, a
    /// document crozier would otherwise generate from. It only ever decides
    /// whether an SDK is written, never a byte of one that is. The classes it
    /// refuses and their evaluated generation policies are registered in
    /// `docs/fern-refusals/`.
    pub fern_strict: bool,
    /// Which tree to write: Fern's packaged SDK (the default) or its flat module
    /// tree (see [`settings::Layout`]).
    pub layout: settings::Layout,
}

/// Run the full pipeline: parse the spec, build the IR, render, and write files.
/// Returns the files written so the caller can report a count.
pub fn generate(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    document_refusals::check_version_file(&args.spec, args.fern_strict)?;
    document_refusals::check_structure_file(&args.spec, args.fern_strict)?;
    let mut doc = name_refusals::load(&args)?;
    openapi::filter_ignored(&mut doc);
    openapi::filter_by_audience(&mut doc, &args.audiences, args.audience_strict);
    document_refusals::check(&doc, &args.spec, args.fern_strict)?;
    // The config constructor validates the package name (a `PackageName`), so an
    // invalid, traversal-prone value can never reach the filesystem below.
    let mut config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        args.client_class_name,
        args.extra_fields,
        &doc.info.title,
    )?;
    config.layout = args.layout;
    config.enum_type = args.enum_type;
    config.default_max_retries = args.default_max_retries;
    let ir = ir::build(&doc, &config);
    document_refusals::check_sdk(&mut doc, &ir, &config, &args.spec, args.fern_strict)?;
    name_refusals::validate(&doc, &args.spec, args.fern_strict, &ir)?;
    name_refusals::validate_ir(&ir, &doc, &args.spec, args.fern_strict)?;
    let files = emit::generate(&ir)?;
    // Regeneration is idempotent: clear the crozier-owned package tree first so a
    // schema or endpoint dropped from the spec does not leave an orphaned module.
    // In the flat layout that tree is the output root itself.
    match config.layout {
        settings::Layout::Packaged => {
            emit::clean_package_tree(&config.output, config.package_name.as_str())?;
        }
        settings::Layout::Flat => emit::clean_flat_tree(&config.output)?,
    }
    emit::write_files(&config.output, &files)?;
    Ok(files)
}

/// The names a generation run would use once crozier's defaults are filled in:
/// what [`generate`] derives from the API title when a name is not configured.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ResolvedNames {
    /// The Python package (import) name.
    pub package_name: String,
    /// The distribution name.
    pub project_name: String,
    /// The root client class name.
    pub client_class_name: String,
}

/// Resolve the names `args` would generate with, reading the document's title
/// for the defaults exactly as [`generate`] does.
pub fn resolved_names(args: &GenerateArgs) -> Result<ResolvedNames> {
    let doc = openapi::load(&args.spec)?;
    let config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name.clone(),
        args.project_name.clone(),
        args.client_class_name.clone(),
        args.extra_fields,
        &doc.info.title,
    )?;
    let client_class_name = config
        .client_class_name
        .clone()
        .unwrap_or_else(|| config::default_client_class_name(config.package_name.as_str()));
    Ok(ResolvedNames {
        package_name: config.package_name.as_str().to_string(),
        project_name: config.project_name,
        client_class_name,
    })
}

/// Render the files for a spec without writing them — used by tests to compare
/// generated contents against fixtures in-process.
pub fn render_files(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    document_refusals::check_version_file(&args.spec, args.fern_strict)?;
    document_refusals::check_structure_file(&args.spec, args.fern_strict)?;
    let mut doc = name_refusals::load(&args)?;
    openapi::filter_ignored(&mut doc);
    openapi::filter_by_audience(&mut doc, &args.audiences, args.audience_strict);
    document_refusals::check(&doc, &args.spec, args.fern_strict)?;
    let mut config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        args.client_class_name,
        args.extra_fields,
        &doc.info.title,
    )?;
    config.layout = args.layout;
    config.enum_type = args.enum_type;
    config.default_max_retries = args.default_max_retries;
    let ir = ir::build(&doc, &config);
    document_refusals::check_sdk(&mut doc, &ir, &config, &args.spec, args.fern_strict)?;
    name_refusals::validate(&doc, &args.spec, args.fern_strict, &ir)?;
    name_refusals::validate_ir(&ir, &doc, &args.spec, args.fern_strict)?;
    emit::generate(&ir)
}
