//! `crozier compare`: for every generator a repository's crozier configs declare,
//! produce a reference SDK by running the user's `reference.command`, produce
//! crozier's SDK, compare the two whole trees under the byte-match rules in
//! [`crate::parity`], and time both sides. See `docs/compare.md` for the contract
//! this implements (the flags, the reference-command environment, the JSON report
//! and the exit statuses).
//!
//! Every generator is checked before the run ends: a config that cannot be read,
//! a generator that cannot be resolved, a missing or failing reference command —
//! each becomes a `could_not_check` result and the run goes on. Only a failure of
//! the command itself (a missing path argument, an unwritable `--json` or
//! `--diff-dir`) is an `Err`, which the binary turns into exit 1.

pub mod color;
pub mod discover;
pub mod reference;
pub mod report;

use std::io::Write;
use std::path::{Component, Path, PathBuf};
use std::time::Instant;

use crate::parity::{self, Difference};
use crate::settings::{self, CliOverrides, FileConfig, GeneratorSettings};
use crate::GenerateArgs;

use color::Painter;
use discover::FoundConfig;
use report::{ComparedLayout, Comparison, GeneratorResult, ReferenceRun, Report, Status, Timing};

/// The reason a generator with no reference command resolved is not checked.
pub const NO_REFERENCE_COMMAND: &str = "no reference command configured: set \
     `reference.command` in crozier.yml or pass `--reference-command`";

/// The reason every generator is not checked where `sh` is unavailable.
pub const NO_SHELL: &str = "reference commands run under `sh -c`, which crozier \
     does not support on Windows";

/// What `crozier compare` was asked to do.
#[derive(Debug, Clone, Default)]
pub struct Options {
    /// Files and directories to search; empty searches the working directory.
    pub paths: Vec<PathBuf>,
    /// `--reference-command`: overrides every generator's `reference.command`.
    pub reference_command: Option<String>,
    /// `--json`: where to write the JSON report (`-` is stdout).
    pub json: Option<PathBuf>,
    /// `--diff-dir`: where to write one diff file per mismatched generator.
    pub diff_dir: Option<PathBuf>,
}

/// Where a run writes, and the facts about its host it depends on.
pub struct Io<'a> {
    /// Progress and the human report.
    pub stderr: &'a mut dyn Write,
    /// The JSON report under `--json -`.
    pub stdout: &'a mut dyn Write,
    /// Whether to colour the human output (see [`color::color_enabled`]).
    pub color: bool,
    /// Whether reference commands can run (`sh` exists: not Windows).
    pub shell_supported: bool,
}

/// Run `crozier compare` from `cwd`, returning the exit status (0, 3 or 4).
///
/// # Errors
///
/// When the command itself fails — a path argument that does not exist, an
/// unwritable `--json` or `--diff-dir` — with a message naming the problem. No
/// report is written then.
pub fn run(options: &Options, cwd: &Path, io: &mut Io<'_>) -> Result<u8, String> {
    let painter = Painter::new(io.color);
    let configs = discover::discover(&options.paths, cwd)?;
    let json_target = options
        .json
        .as_ref()
        .map(|path| JsonTarget::new(path, cwd))
        .transpose()?;
    let diff_dir = options
        .diff_dir
        .as_ref()
        .map(|dir| {
            let absolute = cwd.join(dir);
            std::fs::create_dir_all(&absolute)
                .map(|()| (dir.clone(), absolute))
                .map_err(|error| format!("could not create --diff-dir {}: {error}", dir.display()))
        })
        .transpose()?;

    let mut checker = Checker {
        options,
        painter,
        shell_supported: io.shell_supported,
        diff_dir,
        results: Vec::new(),
    };
    for config in &configs {
        progress(io.stderr, &format!("found config {}", config.display));
        checker.check_config(config, io.stderr)?;
    }

    let searched = if options.paths.is_empty() {
        vec![cwd.display().to_string()]
    } else {
        options
            .paths
            .iter()
            .map(|p| p.display().to_string())
            .collect()
    };
    let report = Report::new(searched, checker.results);
    if let Some(target) = json_target {
        target.write(&report, io.stdout)?;
    }
    let _ = io.stderr.write_all(report.render(painter).as_bytes());
    Ok(report.exit_code.into())
}

/// Write one progress line to stderr.
fn progress(stderr: &mut dyn Write, line: &str) {
    let _ = writeln!(stderr, "compare: {line}");
}

/// Where `--json` goes, checked before any generator runs so an unwritable path
/// fails fast.
enum JsonTarget {
    Stdout,
    File { given: PathBuf, absolute: PathBuf },
}

impl JsonTarget {
    fn new(given: &Path, cwd: &Path) -> Result<Self, String> {
        if given == Path::new("-") {
            return Ok(JsonTarget::Stdout);
        }
        let absolute = cwd.join(given);
        let parent = absolute.parent().unwrap_or(cwd);
        if !parent.is_dir() || absolute.is_dir() {
            return Err(format!(
                "cannot write --json {}: its directory does not exist or it is a directory",
                given.display()
            ));
        }
        Ok(JsonTarget::File {
            given: given.to_path_buf(),
            absolute,
        })
    }

    fn write(&self, report: &Report, stdout: &mut dyn Write) -> Result<(), String> {
        let mut body = serde_json::to_string_pretty(report).expect("the report serializes");
        body.push('\n');
        match self {
            JsonTarget::Stdout => stdout
                .write_all(body.as_bytes())
                .and_then(|()| stdout.flush())
                .map_err(|error| format!("could not write the JSON report to stdout: {error}")),
            JsonTarget::File { given, absolute } => std::fs::write(absolute, body)
                .map_err(|error| format!("could not write --json {}: {error}", given.display())),
        }
    }
}

/// The state of one run across its configs.
struct Checker<'a> {
    options: &'a Options,
    painter: Painter,
    shell_supported: bool,
    /// `--diff-dir` as given, and absolute.
    diff_dir: Option<(PathBuf, PathBuf)>,
    results: Vec<GeneratorResult>,
}

/// One generator, resolved from its config file alone.
struct Resolved {
    args: GenerateArgs,
    names: crate::ResolvedNames,
    config_path: PathBuf,
}

impl Checker<'_> {
    /// Check every generator `config` declares, appending one result each (or one
    /// for the config when it cannot be read).
    fn check_config(&mut self, config: &FoundConfig, stderr: &mut dyn Write) -> Result<(), String> {
        let config_path =
            std::fs::canonicalize(&config.path).unwrap_or_else(|_| config.path.clone());
        let config_dir = config_path
            .parent()
            .map_or_else(|| PathBuf::from("."), Path::to_path_buf);
        let loaded = match settings::load(std::slice::from_ref(&config_path), false, &config_dir) {
            Ok(loaded) => loaded,
            Err(error) => {
                self.finish(
                    stderr,
                    &config.display,
                    None,
                    could_not_check(config, None, None, None, error.to_string()),
                );
                return Ok(());
            }
        };
        let names = settings::run_set(&loaded.config, None)
            .expect("the whole configured set always resolves");
        for name in names {
            let result = self.check_generator(
                config,
                &config_path,
                &config_dir,
                &loaded.config,
                &name,
                stderr,
            )?;
            self.finish(stderr, &config.display, Some(&name), result);
        }
        Ok(())
    }

    /// Record a result and print its progress line.
    fn finish(
        &mut self,
        stderr: &mut dyn Write,
        config: &str,
        generator: Option<&str>,
        result: GeneratorResult,
    ) {
        let label = generator.map_or_else(|| config.to_string(), |g| format!("{config} {g}"));
        let mut line = format!(
            "{label}: {}",
            self.painter.status(result.status, result.status.as_str())
        );
        if let Some(reason) = &result.reason {
            let first = reason.lines().next().unwrap_or_default();
            line.push_str(&format!(" ({})", first.trim_end_matches(':')));
        }
        progress(stderr, &line);
        self.results.push(result);
    }

    fn check_generator(
        &mut self,
        config: &FoundConfig,
        config_path: &Path,
        config_dir: &Path,
        file: &FileConfig,
        name: &str,
        stderr: &mut dyn Write,
    ) -> Result<GeneratorResult, String> {
        let label = format!("{} {name}", config.display);
        let crozier_dir = tempfile::tempdir()
            .map_err(|error| format!("could not create a temporary directory: {error}"))?;
        let resolved = match resolve(file, name, config_path, config_dir, crozier_dir.path()) {
            Ok(resolved) => resolved,
            Err((spec, reason)) => {
                return Ok(could_not_check(config, Some(name), spec, None, reason));
            }
        };
        let spec = Some(resolved.args.spec.display().to_string());

        let Some((command, _)) = settings::resolve_reference_command(
            name,
            file,
            self.options.reference_command.as_deref(),
        ) else {
            return Ok(could_not_check(
                config,
                Some(name),
                spec,
                None,
                NO_REFERENCE_COMMAND.to_string(),
            ));
        };
        if !self.shell_supported {
            let run = ReferenceRun {
                command,
                exit_code: None,
                diagnostic: None,
            };
            return Ok(could_not_check(
                config,
                Some(name),
                spec,
                Some(run),
                NO_SHELL.to_string(),
            ));
        }

        // The reference side: the user's command, timed as one invocation.
        let reference_dir = tempfile::tempdir()
            .map_err(|error| format!("could not create a temporary directory: {error}"))?;
        progress(
            stderr,
            &format!("{label}: reference command starting: {command}"),
        );
        let env = reference_env(&resolved, name, reference_dir.path());
        let outcome = reference::run(&command, config_dir, &env);
        let reference_seconds = outcome.seconds;
        progress(
            stderr,
            &format!(
                "{label}: reference command finished in {reference_seconds:.2}s ({})",
                outcome.status_text()
            ),
        );
        let mut run = ReferenceRun {
            command,
            exit_code: outcome.exit_code(),
            diagnostic: None,
        };
        let located = if outcome.succeeded() {
            reference::locate(reference_dir.path())
        } else {
            Err(outcome.failure_reason())
        };
        let reference_root = match located {
            Ok(root) => root,
            Err(reason) => {
                run.diagnostic = outcome.diagnostic();
                let mut result = could_not_check(config, Some(name), spec, Some(run), reason);
                result.timing = Some(Timing::from_measurements(Some(reference_seconds), None));
                return Ok(result);
            }
        };

        // crozier's side, into its own temporary directory, timed alone.
        progress(stderr, &format!("{label}: crozier generation starting"));
        let layout = resolved.args.layout;
        let crozier_root = resolved.args.output.clone();
        let started = Instant::now();
        let generated = crate::generate(resolved.args);
        let crozier_seconds = started.elapsed().as_secs_f64();
        let timing = Some(Timing::from_measurements(
            Some(reference_seconds),
            Some(crozier_seconds),
        ));
        if let Err(error) = generated {
            progress(
                stderr,
                &format!("{label}: crozier generation failed in {crozier_seconds:.2}s"),
            );
            let mut result = could_not_check(
                config,
                Some(name),
                spec,
                Some(run),
                format!("crozier could not generate: {error}"),
            );
            result.timing = Some(Timing::from_measurements(Some(reference_seconds), None));
            return Ok(result);
        }
        progress(
            stderr,
            &format!("{label}: crozier generation finished in {crozier_seconds:.2}s"),
        );

        let differences = match parity::tree_differences(
            &reference_root,
            &crozier_root,
            None,
            self.diff_dir.is_some(),
        ) {
            Ok(differences) => differences,
            Err(error) => {
                let mut result = could_not_check(
                    config,
                    Some(name),
                    spec,
                    Some(run),
                    format!("the trees could not be compared: {error}"),
                );
                result.timing = timing;
                return Ok(result);
            }
        };
        let files_compared = count_paths(&reference_root, &crozier_root);
        let mut comparison = Comparison {
            layout: ComparedLayout::from(layout),
            files_compared,
            differing: Vec::new(),
            only_in_reference: Vec::new(),
            only_in_crozier: Vec::new(),
            diff_file: None,
        };
        for (rel, difference) in &differences {
            match difference {
                Difference::OnlyInReference => comparison.only_in_reference.push(rel.clone()),
                Difference::OnlyInCrozier => comparison.only_in_crozier.push(rel.clone()),
                _ => comparison.differing.push(rel.clone()),
            }
        }
        let status = if differences.is_empty() {
            Status::Matched
        } else {
            Status::Mismatched
        };
        if status == Status::Mismatched {
            if let Some((given, absolute)) = &self.diff_dir {
                let file_name = diff_file_name(self.results.len() + 1, &config.display, name);
                let body = render_diff(&config.display, name, &differences);
                std::fs::write(absolute.join(&file_name), body).map_err(|error| {
                    format!(
                        "could not write --diff-dir file {}: {error}",
                        given.join(&file_name).display()
                    )
                })?;
                comparison.diff_file = Some(given.join(&file_name).display().to_string());
            }
        }
        Ok(GeneratorResult {
            status,
            config_file: config.display.clone(),
            generator: Some(name.to_string()),
            spec,
            reference: Some(run),
            comparison: Some(comparison),
            timing,
            reason: None,
        })
    }
}

/// A `could_not_check` result with nothing measured.
fn could_not_check(
    config: &FoundConfig,
    generator: Option<&str>,
    spec: Option<String>,
    reference: Option<ReferenceRun>,
    reason: String,
) -> GeneratorResult {
    GeneratorResult {
        status: Status::CouldNotCheck,
        config_file: config.display.clone(),
        generator: generator.map(str::to_string),
        spec,
        reference,
        comparison: None,
        timing: None,
        reason: Some(reason),
    }
}

/// Resolve one generator's generation settings from its config file alone — no
/// `CROZIER_*` environment layer and no per-generation flags — with relative
/// paths against the config file's directory, and crozier's output redirected to
/// `output` (never the configured `output`). On failure, the resolved spec (if
/// any) and the reason.
fn resolve(
    file: &FileConfig,
    name: &str,
    config_path: &Path,
    config_dir: &Path,
    output: &Path,
) -> Result<Resolved, (Option<String>, String)> {
    let only_output = CliOverrides {
        output: Some(output.join("sdk")),
        ..CliOverrides::default()
    };
    let mut args = settings::resolve(name, file, &GeneratorSettings::default(), &only_output)
        .map_err(|error| (None, error.to_string()))?;
    args.spec = clean_join(config_dir, &args.spec);
    let names = crate::resolved_names(&args).map_err(|error| {
        (
            Some(args.spec.display().to_string()),
            format!("crozier could not read the generator's settings: {error}"),
        )
    })?;
    Ok(Resolved {
        args,
        names,
        config_path: config_path.to_path_buf(),
    })
}

/// `base.join(path)` as an absolute path that reads cleanly for a reference
/// command: its directory resolved (so `..` and `.` are gone), its file name kept
/// as written. Falls back to dropping `.` components when the directory does not
/// exist.
fn clean_join(base: &Path, path: &Path) -> PathBuf {
    let joined = base.join(path);
    if let (Some(parent), Some(name)) = (joined.parent(), joined.file_name()) {
        if let Ok(parent) = std::fs::canonicalize(parent) {
            return parent.join(name);
        }
    }
    joined
        .components()
        .filter(|c| !matches!(c, Component::CurDir))
        .collect()
}

/// The variables a reference command receives on top of the inherited
/// environment, in the order [`reference_env`] gives their values: where to
/// write, then the generator's resolved settings. The one source of the names:
/// `docs/compare.md`'s table and the Fern recipe's tests are checked against it.
pub const REFERENCE_VARIABLES: [&str; 11] = [
    "CROZIER_REFERENCE_OUTPUT",
    "CROZIER_REFERENCE_GENERATOR",
    "CROZIER_REFERENCE_CONFIG_FILE",
    "CROZIER_REFERENCE_SPEC",
    "CROZIER_REFERENCE_PACKAGE_NAME",
    "CROZIER_REFERENCE_PROJECT_NAME",
    "CROZIER_REFERENCE_CLIENT_CLASS_NAME",
    "CROZIER_REFERENCE_AUDIENCES",
    "CROZIER_REFERENCE_AUDIENCE_STRICT",
    "CROZIER_REFERENCE_EXTRA_FIELDS",
    "CROZIER_REFERENCE_LAYOUT",
];

/// [`REFERENCE_VARIABLES`] paired with this generator's values.
fn reference_env(resolved: &Resolved, name: &str, output: &Path) -> Vec<(String, String)> {
    let args = &resolved.args;
    let values = [
        output.display().to_string(),
        name.to_string(),
        resolved.config_path.display().to_string(),
        args.spec.display().to_string(),
        resolved.names.package_name.clone(),
        resolved.names.project_name.clone(),
        resolved.names.client_class_name.clone(),
        args.audiences.join(","),
        args.audience_strict.to_string(),
        args.extra_fields.as_str().to_string(),
        args.layout.as_str().to_string(),
    ];
    REFERENCE_VARIABLES
        .into_iter()
        .map(str::to_string)
        .zip(values)
        .collect()
}

/// How many distinct paths the two trees hold between them.
fn count_paths(reference_root: &Path, crozier_root: &Path) -> usize {
    let mut all: std::collections::BTreeSet<String> = parity::walk_files(reference_root)
        .unwrap_or_default()
        .into_iter()
        .collect();
    all.extend(parity::walk_files(crozier_root).unwrap_or_default());
    all.len()
}

/// The `--diff-dir` file name for the `index`th result: unique within the run
/// and readable as the config and generator it belongs to.
fn diff_file_name(index: usize, config: &str, generator: &str) -> String {
    let slug: String = format!("{config}-{generator}")
        .chars()
        .map(|c| {
            if c.is_ascii_alphanumeric() || "._-".contains(c) {
                c
            } else {
                '_'
            }
        })
        .collect();
    format!("{index:03}-{slug}.diff")
}

/// One mismatched generator's normalized diff, `-` reference and `+` crozier.
fn render_diff(config: &str, generator: &str, differences: &[(String, Difference)]) -> String {
    let mut out = format!(
        "# crozier compare: {config} {generator}\n# normalized diff: `-` reference, `+` crozier\n"
    );
    for (rel, difference) in differences {
        match difference {
            Difference::OnlyInReference => out.push_str(&format!("\nOnly in reference: {rel}\n")),
            Difference::OnlyInCrozier => out.push_str(&format!("\nOnly in crozier: {rel}\n")),
            Difference::Text(diff) => out.push_str(&format!(
                "\n--- reference/{rel}\n+++ crozier/{rel}\n{}",
                diff.as_deref().unwrap_or_default()
            )),
            Difference::Binary { reference, crozier } => out.push_str(&format!(
                "\nBinary files differ: {rel} (reference {reference} bytes, crozier {crozier} bytes)\n"
            )),
            Difference::Processing(error) => {
                out.push_str(&format!("\nCould not compare {rel}: {error}\n"));
            }
        }
    }
    out
}

#[cfg(test)]
mod tests;
