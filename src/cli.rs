//! CLI parsing and dispatch. Kept in the library (not `main.rs`) so it is
//! testable in-process and measured by coverage; `src/main.rs` is a thin shell.
//!
//! Exit codes: `0` success, `1` any failure (with an actionable message on
//! stderr). Success is quiet: `generate` prints a single summary line to stderr.

use std::path::PathBuf;

use clap::{Parser, Subcommand};

use crate::{generate, strip_python_comments, GenerateArgs};

/// Generate SDKs from an OpenAPI document, matching Fern's output.
#[derive(Parser)]
#[command(name = "crozier", version, about)]
pub struct Cli {
    /// The subcommand to run.
    #[command(subcommand)]
    command: Command,
}

/// Top-level subcommands.
#[derive(Subcommand)]
enum Command {
    /// Generate an SDK from an OpenAPI document.
    Generate(GenerateCmd),

    /// Internal: strip Python `#` comments from a file to stdout. Used by the
    /// fixture tooling so the committed fixtures and the e2e share one stripper.
    #[command(hide = true)]
    InternalStrip {
        /// The `.py` file to strip.
        file: PathBuf,
    },
}

/// Arguments to `crozier generate`.
#[derive(Parser)]
struct GenerateCmd {
    /// Path to the OpenAPI document (`.yml`, `.yaml`, or `.json`).
    #[arg(long)]
    spec: PathBuf,

    /// Directory to write the generated SDK into.
    #[arg(long)]
    output: PathBuf,

    /// Python package (import) name — the directory under `src/`. Defaults to a
    /// snake_case of the API title.
    #[arg(long)]
    package_name: Option<String>,

    /// Distribution name recorded in `version.py`. Defaults to the package name.
    #[arg(long)]
    project_name: Option<String>,

    /// Name of the generated root client class (Fern's `client_class_name`).
    /// Defaults to `{PascalCase(package_name)}Api`.
    #[arg(long)]
    client_class_name: Option<String>,

    /// `x-crozier-audiences` filter (repeatable). When given, only operations
    /// carrying a matching audience — or none at all — are generated, along with
    /// the transitive closure of schemas they reference. Omit to generate the
    /// whole API.
    #[arg(long = "audience")]
    audiences: Vec<String>,

    /// Restrict `--audience` to a *strict* subset: generate only operations that
    /// carry a matching audience, excluding un-annotated ones. Matches Fern's
    /// exclusive filtering — the way to carve a minimal, self-contained SDK out of
    /// a mostly-un-annotated API. No effect without `--audience`.
    #[arg(long = "audience-strict")]
    audience_strict: bool,
}

/// Parse an explicit argument list and run — the in-process entry point used by
/// tests. Returns `Ok` on success or a human-readable error string.
pub fn run_from<I, T>(args: I) -> std::result::Result<(), String>
where
    I: IntoIterator<Item = T>,
    T: Into<std::ffi::OsString> + Clone,
{
    let cli = Cli::try_parse_from(args).map_err(|e| e.to_string())?;
    run(cli)
}

/// Dispatch a parsed CLI, returning a human-readable error string on failure.
pub fn run(cli: Cli) -> std::result::Result<(), String> {
    match cli.command {
        Command::Generate(cmd) => {
            let files = generate(GenerateArgs {
                spec: cmd.spec,
                output: cmd.output.clone(),
                package_name: cmd.package_name,
                project_name: cmd.project_name,
                client_class_name: cmd.client_class_name,
                audiences: cmd.audiences,
                audience_strict: cmd.audience_strict,
            })
            .map_err(|e| e.to_string())?;
            eprintln!(
                "generated {} files into {}",
                files.len(),
                cmd.output.display()
            );
            Ok(())
        }
        Command::InternalStrip { file } => {
            let source = std::fs::read_to_string(&file)
                .map_err(|e| format!("could not read {}: {e}", file.display()))?;
            print!("{}", strip_python_comments(&source));
            Ok(())
        }
    }
}
