//! crozier: generate SDKs from an OpenAPI document, matching Fern's output.
//!
//! The library is a small pipeline: [`openapi::load`] parses the document,
//! [`ir::build`] resolves it into a generation-ready [`ir::Ir`], and
//! [`emit::generate`] renders that IR to Python files with minijinja. The CLI
//! (`src/main.rs`) is a thin shell over [`generate`].

pub mod config;
pub mod emit;
pub mod error;
pub mod ir;
pub mod naming;
pub mod normalize;
pub mod openapi;

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
}

/// Run the full pipeline: parse the spec, build the IR, render, and write files.
/// Returns the files written so the caller can report a count.
pub fn generate(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    let doc = openapi::load(&args.spec)?;
    let config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        &doc.info.title,
    );
    let ir = ir::build(&doc, &config);
    let files = emit::generate(&ir)?;
    emit::write_files(&config.output, &files)?;
    Ok(files)
}

/// Render the files for a spec without writing them — used by tests to compare
/// generated contents against fixtures in-process.
pub fn render_files(args: GenerateArgs) -> Result<Vec<GeneratedFile>> {
    let doc = openapi::load(&args.spec)?;
    let config = GenerateConfig::new(
        args.spec.clone(),
        args.output.clone(),
        args.package_name,
        args.project_name,
        &doc.info.title,
    );
    let ir = ir::build(&doc, &config);
    emit::generate(&ir)
}
