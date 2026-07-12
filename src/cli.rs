//! CLI parsing and dispatch. Kept in the library (not `main.rs`) so it is
//! testable in-process and measured by coverage; `src/main.rs` is a thin shell.
//!
//! # Command surface
//!
//! - `crozier` / `crozier generate` — run every configured generator (or the
//!   built-in `python` when nothing is configured).
//! - `crozier generate <name>` — run one generator by name (a config-defined
//!   instance, or the built-in `python`).
//!
//! Configuration layers per field as CLI > `CROZIER_*` env > config file
//! (per-generator over shared top-level) > built-in defaults; see
//! [`crate::settings`]. A `crozier.yml` in the working directory is picked up
//! automatically; `--config <path>` (repeatable) selects files instead, and
//! `--no-config` ignores files entirely.
//!
//! Exit codes: `0` success, `1` any failure (with an actionable message on
//! stderr). Success is quiet: each generator prints a single summary line to
//! stderr.

use std::path::PathBuf;

use clap::{Parser, Subcommand};

use crate::settings::{self, CliOverrides};
use crate::{generate, strip_python_comments, GenerateArgs};

/// Generate SDKs from an OpenAPI document, matching Fern's output.
#[derive(Parser)]
#[command(name = "crozier", version, about)]
pub struct Cli {
    /// The subcommand to run. Omitted, crozier runs every configured generator.
    #[command(subcommand)]
    command: Option<Command>,

    /// Config file to load, overriding auto-discovery of `crozier.yml` in the
    /// working directory. Repeatable; later files win per field. Overrides
    /// `CROZIER_CONFIG`.
    #[arg(long = "config", global = true, value_name = "PATH")]
    config: Vec<PathBuf>,

    /// Ignore all config files (use only CLI flags, `CROZIER_*` env, and
    /// built-in defaults).
    #[arg(long = "no-config", global = true)]
    no_config: bool,
}

/// Top-level subcommands.
#[derive(Subcommand)]
enum Command {
    /// Generate an SDK from an OpenAPI document.
    Generate(GenerateCmd),

    /// Write a starter `crozier.yml` (with a JSON Schema modeline for editor
    /// completion) to the working directory.
    Init(InitCmd),

    /// Show the effective configuration and where each value comes from.
    Config(ConfigCmd),

    /// Internal: strip Python `#` comments from a file to stdout. Used by the
    /// fixture tooling so the committed fixtures and the e2e share one stripper.
    #[command(hide = true)]
    InternalStrip {
        /// The `.py` file to strip.
        file: PathBuf,
    },
}

/// Arguments to `crozier init`.
#[derive(Parser)]
struct InitCmd {
    /// Where to write the config. Defaults to `crozier.yml` in the working
    /// directory.
    #[arg(long, value_name = "PATH")]
    output: Option<PathBuf>,

    /// Overwrite an existing file instead of refusing.
    #[arg(long)]
    force: bool,
}

/// Arguments to `crozier config`.
#[derive(Parser)]
struct ConfigCmd {
    /// Show only this generator. Omit to show every configured generator (or the
    /// built-in `python`).
    generator: Option<String>,
}

/// Arguments to `crozier generate`.
#[derive(Parser)]
struct GenerateCmd {
    /// The generator to run. Omit to run every configured generator (or the
    /// built-in `python` when none are configured).
    generator: Option<String>,

    /// Path to the OpenAPI document (`.yml`, `.yaml`, or `.json`).
    #[arg(long)]
    spec: Option<PathBuf>,

    /// Directory to write the generated SDK into.
    #[arg(long)]
    output: Option<PathBuf>,

    /// Python package (import) name — the directory under `src/`. Defaults to a
    /// snake_case of the API title.
    #[arg(long)]
    package_name: Option<String>,

    /// Distribution name recorded in `version.py`. Defaults to the package name.
    #[arg(long)]
    project_name: Option<String>,

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

impl GenerateCmd {
    /// The per-generation values this invocation supplied, as an override layer.
    /// Repeatable/flag fields map to `None` when absent so they fall through to
    /// the env and config layers rather than clobbering them with an empty value.
    fn overrides(&self) -> CliOverrides {
        CliOverrides {
            spec: self.spec.clone(),
            output: self.output.clone(),
            package_name: self.package_name.clone(),
            project_name: self.project_name.clone(),
            audiences: (!self.audiences.is_empty()).then(|| self.audiences.clone()),
            audience_strict: self.audience_strict.then_some(true),
        }
    }
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
        // Bare `crozier`: run every configured generator with no per-generation
        // overrides.
        None => do_generate(&cli.config, cli.no_config, None, &CliOverrides::default())
            .map_err(|e| e.to_string()),
        Some(Command::Generate(cmd)) => do_generate(
            &cli.config,
            cli.no_config,
            cmd.generator.as_deref(),
            &cmd.overrides(),
        )
        .map_err(|e| e.to_string()),
        Some(Command::Init(cmd)) => do_init(&cmd).map_err(|e| e.to_string()),
        Some(Command::Config(cmd)) => {
            do_config(&cli.config, cli.no_config, cmd.generator.as_deref())
                .map_err(|e| e.to_string())
        }
        Some(Command::InternalStrip { file }) => {
            let source = std::fs::read_to_string(&file)
                .map_err(|e| format!("could not read {}: {e}", file.display()))?;
            print!("{}", strip_python_comments(&source));
            Ok(())
        }
    }
}

/// Load config, resolve the selected generator(s), and run each. Per-generation
/// CLI overrides only make sense for a single generator, so passing them while
/// more than one would run is a hard error rather than an ambiguous broadcast.
fn do_generate(
    config_paths: &[PathBuf],
    no_config: bool,
    selected: Option<&str>,
    overrides: &CliOverrides,
) -> crate::Result<()> {
    let cwd = std::env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
    // `--config` beats `CROZIER_CONFIG`; either names files explicitly and
    // disables auto-discovery.
    let explicit = resolve_config_paths(config_paths, std::env::var("CROZIER_CONFIG").ok());
    let loaded = settings::load(&explicit, no_config, &cwd)?;
    let env = if no_config {
        crate::settings::GeneratorSettings::default()
    } else {
        settings::env_overrides(|name| std::env::var(name).ok())?
    };

    let names = settings::run_set(&loaded.config, selected)?;
    if names.len() > 1 && !overrides.is_empty() {
        return Err(crate::Error::OverridesWithMultipleGenerators { count: names.len() });
    }

    let multiple = names.len() > 1;
    for name in &names {
        let args: GenerateArgs = settings::resolve(name, &loaded.config, &env, overrides)?;
        let output = args.output.clone();
        let files = generate(args)?;
        if multiple {
            eprintln!(
                "{name}: generated {} files into {}",
                files.len(),
                output.display()
            );
        } else {
            eprintln!("generated {} files into {}", files.len(), output.display());
        }
    }
    Ok(())
}

/// The body written by `crozier init`, after the schema modeline. A minimal
/// config: one shared default and one generator of each canonical type (only
/// `python` today).
const STARTER_CONFIG: &str = "\
# crozier configuration.
# Docs: https://github.com/nickderobertis/crozier/blob/main/docs/configuration.md
#
# Settings resolve per field as:
#   CLI flag > CROZIER_* env > this file (generator over shared) > built-in default
#
# Top-level keys are shared defaults inherited by every generator.
spec: ./openapi.yml

generators:
  # The built-in Python generator. `crozier generate python` runs this;
  # `crozier` (or `crozier generate`) runs every generator listed here.
  python:
    type: python
    output: ./sdk/python
    # package-name: my_api    # defaults to a snake_case of the API title
    # project-name: my-api    # defaults to the package name
";

/// Write a starter `crozier.yml`, refusing to clobber an existing file unless
/// `--force` was given. The file leads with a `$schema` modeline so editors give
/// completion/validation against the published schema.
fn do_init(cmd: &InitCmd) -> crate::Result<()> {
    let path = cmd
        .output
        .clone()
        .unwrap_or_else(|| PathBuf::from("crozier.yml"));
    if path.exists() && !cmd.force {
        return Err(crate::Error::ConfigExists { path });
    }
    let contents = format!("{}{STARTER_CONFIG}", crate::schema::modeline());
    std::fs::write(&path, contents).map_err(|source| crate::Error::WriteConfig {
        path: path.clone(),
        source,
    })?;
    eprintln!("wrote {}", path.display());
    Ok(())
}

/// Print the effective configuration for the selected generator(s): the config
/// files consulted, then each field's resolved value and the layer it came from.
/// Never requires `spec`/`output` — this is for inspecting a config before a run.
fn do_config(
    config_paths: &[PathBuf],
    no_config: bool,
    selected: Option<&str>,
) -> crate::Result<()> {
    let cwd = std::env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
    let explicit = resolve_config_paths(config_paths, std::env::var("CROZIER_CONFIG").ok());
    let loaded = settings::load(&explicit, no_config, &cwd)?;
    let env = if no_config {
        crate::settings::GeneratorSettings::default()
    } else {
        settings::env_overrides(|name| std::env::var(name).ok())?
    };

    if loaded.files.is_empty() {
        println!("config files: none (built-in defaults)");
    } else {
        let files: Vec<String> = loaded
            .files
            .iter()
            .map(|p| p.display().to_string())
            .collect();
        println!("config files: {}", files.join(", "));
    }

    let names = settings::run_set(&loaded.config, selected)?;
    let empty_cli = CliOverrides::default();
    for name in &names {
        println!("\ngenerator `{name}`");
        for f in settings::explain(name, &loaded.config, &env, &empty_cli) {
            let value = f.value.as_deref().unwrap_or("(unset)");
            println!("  {:<16} {:<28} ({})", f.field, value, f.source.label());
        }
    }
    Ok(())
}

/// The explicit config paths for this run: `--config` if given, else a single
/// `CROZIER_CONFIG` if set and non-empty, else none (auto-discovery). Pure over
/// its inputs so the precedence is unit-testable without touching the process
/// environment.
fn resolve_config_paths(config_paths: &[PathBuf], env_config: Option<String>) -> Vec<PathBuf> {
    if !config_paths.is_empty() {
        return config_paths.to_vec();
    }
    match env_config {
        Some(v) if !v.is_empty() => vec![PathBuf::from(v)],
        _ => Vec::new(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn config_flag_beats_env_which_beats_discovery() {
        let flag = [PathBuf::from("a.yml"), PathBuf::from("b.yml")];
        // `--config` wins outright, ignoring the environment.
        assert_eq!(
            resolve_config_paths(&flag, Some("env.yml".to_string())),
            flag
        );
        // No flag: a non-empty `CROZIER_CONFIG` is used.
        assert_eq!(
            resolve_config_paths(&[], Some("env.yml".to_string())),
            [PathBuf::from("env.yml")]
        );
        // No flag, empty or absent env: nothing (auto-discovery).
        assert!(resolve_config_paths(&[], Some(String::new())).is_empty());
        assert!(resolve_config_paths(&[], None).is_empty());
    }
}
