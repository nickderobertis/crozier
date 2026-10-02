//! CLI parsing and dispatch. Kept in the library (not `main.rs`) so it is
//! testable in-process and measured by coverage; `src/main.rs` is a thin shell.
//!
//! # Command surface
//!
//! - `crozier` / `crozier generate` — run every configured generator (or the
//!   built-in `python` when nothing is configured).
//! - `crozier generate <name>` — run one generator by name (a config-defined
//!   instance, or the built-in `python`).
//! - `crozier compare [PATHS...]` — check every configured generator against a
//!   reference SDK (see [`crate::compare`]).
//!
//! Configuration layers per field as CLI > `CROZIER_*` env > config file
//! (per-generator over shared top-level) > built-in defaults; see
//! [`crate::settings`]. A `crozier.yml` in the working directory is picked up
//! automatically; `--config <path>` (repeatable) selects files instead, and
//! `--no-config` ignores files entirely.
//!
//! Exit codes: `0` success, `1` any failure (with an actionable message on
//! stderr); `compare` adds `3` (a mismatch) and `4` (no mismatch, but a
//! generator could not be checked). Success is quiet: each generator prints a
//! single summary line to stderr.

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

    /// Check every configured generator's output against a reference SDK that
    /// a command you configure produces, and time both sides. See
    /// docs/compare.md.
    Compare(CompareCmd),

    /// Print the JSON Schema for `crozier.yml` to stdout (the same schema editors
    /// use via the `$schema` modeline `crozier init` writes).
    Schema,

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

/// Arguments to `crozier compare`.
#[derive(Parser)]
struct CompareCmd {
    /// Crozier config files to check, or directories to search for them (`.git`
    /// and git-ignored paths are skipped). Omit to search the whole repository
    /// the working directory is in (its git top-level).
    paths: Vec<PathBuf>,

    /// The command that writes each generator's reference SDK (run under
    /// `sh -c`; see docs/compare.md), overriding every `reference.command`.
    #[arg(long = "reference-command", value_name = "CMD")]
    reference_command: Option<String>,

    /// Write the JSON report to this path (`-` for stdout; the human report stays
    /// on stderr).
    #[arg(long = "json", value_name = "PATH")]
    json: Option<PathBuf>,

    /// Write one normalized unified diff per mismatched generator into this
    /// directory.
    #[arg(long = "diff-dir", value_name = "DIR")]
    diff_dir: Option<PathBuf>,
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

    /// Strict Fern compatibility: refuse to generate from a document Fern
    /// refuses, even where crozier's own output would be valid. Never changes a
    /// byte of an SDK that is written.
    #[arg(long = "fern-strict")]
    fern_strict: bool,

    /// How generated pydantic models treat unknown fields on a response (Fern's
    /// `pydantic_config.extra_fields`). `allow` (default) keeps them, `ignore`
    /// drops them silently, `forbid` rejects them.
    #[arg(long = "extra-fields", value_name = "MODE")]
    extra_fields: Option<crate::settings::ExtraFields>,

    /// How string enums are generated (Fern's `pydantic_config.enum_type`).
    /// `python-enums` (default) emits an `enum.StrEnum` class per enum;
    /// `literals` emits an open `typing.Literal` union that also accepts values
    /// the spec does not list (Fern with `enum_type` unset).
    #[arg(long = "enum-type", value_name = "TYPE")]
    enum_type: Option<crate::settings::EnumType>,

    /// Which tree to write, matching how Fern was run: `packaged` (default) is a
    /// pip-installable package with the modules under `src/<package>/` (Fern's
    /// `--preview --output`); `flat` is the bare module tree at the output root
    /// (Fern's `local-file-system` output).
    #[arg(long = "layout", value_name = "LAYOUT")]
    layout: Option<crate::settings::Layout>,
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
            client_class_name: self.client_class_name.clone(),
            audiences: (!self.audiences.is_empty()).then(|| self.audiences.clone()),
            audience_strict: self.audience_strict.then_some(true),
            fern_strict: self.fern_strict.then_some(true),
            extra_fields: self.extra_fields,
            enum_type: self.enum_type,
            layout: self.layout,
        }
    }
}

/// Parse an argument list, refusing every usage error as clap does — including
/// `compare` combined with the global `--config`/`--no-config`, which clap's
/// derive cannot express — so each one exits 2 with clap's usage text.
///
/// # Errors
///
/// The usage error, ready for [`clap::Error::exit`].
pub fn parse_args<I, T>(args: I) -> std::result::Result<Cli, clap::Error>
where
    I: IntoIterator<Item = T>,
    T: Into<std::ffi::OsString> + Clone,
{
    let cli = Cli::try_parse_from(args)?;
    if matches!(cli.command, Some(Command::Compare(_))) && (!cli.config.is_empty() || cli.no_config)
    {
        let mut command = <Cli as clap::CommandFactory>::command();
        command.build();
        let compare = command
            .find_subcommand_mut("compare")
            .expect("compare is a subcommand");
        return Err(compare.error(
            clap::error::ErrorKind::ArgumentConflict,
            "`compare` finds its configs from its PATHS; pass a config file as a PATH \
             instead of --config/--no-config",
        ));
    }
    Ok(cli)
}

/// Parse an explicit argument list and run — the in-process entry point used by
/// tests. Returns `Ok` on success or a human-readable error string.
pub fn run_from<I, T>(args: I) -> std::result::Result<(), String>
where
    I: IntoIterator<Item = T>,
    T: Into<std::ffi::OsString> + Clone,
{
    let cli = parse_args(args).map_err(|e| e.to_string())?;
    run(cli)
}

/// Dispatch a parsed CLI, returning a human-readable error string on failure.
/// A command that finishes with a non-zero status of its own (`compare`'s 3 or
/// 4) is reported as an error here; [`execute`] returns the status itself.
pub fn run(cli: Cli) -> std::result::Result<(), String> {
    match execute(cli)? {
        0 => Ok(()),
        code => Err(format!("exited with status {code}")),
    }
}

/// Dispatch a parsed CLI, returning the process exit status on success (`0`,
/// or `compare`'s `3`/`4`, or its `1` when a `--diff-dir` file could not be
/// written) or a human-readable error string, which the binary reports with
/// exit `1`. Parse with [`parse_args`], which refuses every usage error.
pub fn execute(cli: Cli) -> std::result::Result<u8, String> {
    if let Some(Command::Compare(cmd)) = &cli.command {
        return do_compare(cmd);
    }
    run_other(cli).map(|()| 0)
}

/// Run `crozier compare` against the real process: its working directory,
/// environment, and standard streams.
/// (`--config`/`--no-config` were refused by [`parse_args`].)
fn do_compare(cmd: &CompareCmd) -> std::result::Result<u8, String> {
    use std::io::IsTerminal;
    let cwd = std::env::current_dir()
        .map_err(|e| format!("could not read the working directory: {e}"))?;
    let options = crate::compare::Options {
        paths: cmd.paths.clone(),
        reference_command: cmd.reference_command.clone(),
        json: cmd.json.clone(),
        diff_dir: cmd.diff_dir.clone(),
    };
    let stderr = std::io::stderr();
    let color =
        crate::compare::color::color_enabled(|name| std::env::var(name).ok(), stderr.is_terminal());
    let mut io = crate::compare::Io {
        stderr: &mut stderr.lock(),
        stdout: &mut std::io::stdout().lock(),
        color,
        shell_supported: !cfg!(windows),
    };
    crate::compare::run(&options, &cwd, &mut io)
}

/// Dispatch every command but `compare`.
fn run_other(cli: Cli) -> std::result::Result<(), String> {
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
        Some(Command::Compare(_)) => unreachable!("dispatched by `execute`"),
        Some(Command::Schema) => {
            let json =
                serde_json::to_string_pretty(&crate::schema::build()).map_err(|e| e.to_string())?;
            println!("{json}");
            Ok(())
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
# fern-strict: false  # true refuses, as Fern does, documents Fern cannot generate from

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
            println!("  {:<17} {:<28} ({})", f.field, value, f.source.label());
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
    fn compare_with_config_or_no_config_is_a_usage_error() {
        for args in [
            ["crozier", "--config", "a.yml", "compare"].as_slice(),
            ["crozier", "--no-config", "compare"].as_slice(),
        ] {
            let error = parse_args(args).err().unwrap();
            assert_eq!(error.exit_code(), 2);
            assert_eq!(error.kind(), clap::error::ErrorKind::ArgumentConflict);
            assert!(error.to_string().contains("pass a config file as a PATH"));
        }
        assert!(parse_args(["crozier", "compare"]).is_ok());
        assert!(parse_args(["crozier", "--no-config", "generate"]).is_ok());
    }

    #[test]
    fn docs_compare_flag_table_is_compares_own_flags() {
        use clap::CommandFactory;
        let cli = Cli::command();
        let compare = cli.find_subcommand("compare").unwrap();
        let flags: Vec<String> = compare
            .get_arguments()
            .filter(|arg| !arg.is_global_set())
            .filter_map(|arg| {
                let long = arg.get_long()?;
                let value = arg.get_value_names()?.first()?.to_string();
                Some(format!("--{long} <{value}>"))
            })
            .collect();
        let page = std::fs::read_to_string(
            std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/compare.md"),
        )
        .unwrap();
        let documented: Vec<&str> = page
            .lines()
            .filter_map(|line| line.strip_prefix("| `--"))
            .map(|rest| &rest[..rest.find('`').unwrap()])
            .collect();
        let flags: Vec<&str> = flags.iter().map(|f| &f[2..]).collect();
        assert_eq!(
            documented, flags,
            "docs/compare.md's flag table must list `crozier compare`'s flags, in order"
        );
    }

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
