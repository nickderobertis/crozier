//! The `crozier` command-line interface — a thin shell over the library.
//!
//! Exit codes: `0` success, `1` any failure (with an actionable message on
//! stderr). Success is quiet: `generate` prints a single summary line to stderr.

use std::path::PathBuf;
use std::process::ExitCode;

use clap::{Parser, Subcommand};

use crozier::{generate, strip_python_comments, GenerateArgs};

/// Generate SDKs from an OpenAPI document, matching Fern's output.
#[derive(Parser)]
#[command(name = "crozier", version, about)]
struct Cli {
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
}

fn main() -> ExitCode {
    let cli = Cli::parse();
    match run(cli) {
        Ok(()) => ExitCode::SUCCESS,
        Err(message) => {
            eprintln!("crozier: {message}");
            ExitCode::FAILURE
        }
    }
}

/// Dispatch a parsed CLI, returning a human-readable error string on failure.
fn run(cli: Cli) -> std::result::Result<(), String> {
    match cli.command {
        Command::Generate(cmd) => {
            let files = generate(GenerateArgs {
                spec: cmd.spec,
                output: cmd.output.clone(),
                package_name: cmd.package_name,
                project_name: cmd.project_name,
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
