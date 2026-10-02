//! `crozier compare`: for every generator a repository's crozier configs declare,
//! produce a reference SDK by running the user's `reference.command`, produce
//! crozier's SDK, compare the two whole trees under the byte-match rules in
//! [`crate::parity`], and time both sides. See `docs/compare.md` for the contract
//! this implements (the flags, the reference-command environment, the JSON report
//! and the exit statuses).
//!
//! Every generator is checked before the run ends: a config that cannot be read,
//! a generator that cannot be resolved, a missing or failing reference command —
//! each becomes a `could_not_check` result, and a reference crozier cannot
//! generate a counterpart for becomes a `mismatched` one; the run goes on. Only a
//! failure of the command itself (a missing path argument, a `--json` target or
//! `--diff-dir` that cannot be created, a `--diff-dir` file that cannot be
//! written) makes the binary exit 1.

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
    /// Files and directories to search; empty searches the
    /// repository the working directory is in ([`discover::default_root`]).
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

/// Run `crozier compare` from `cwd`, returning the exit status: 0, 3 or 4, or 1
/// when a `--diff-dir` file could not be written — every generator is still
/// checked and both reports still written, and the human one states the failure.
///
/// # Errors
///
/// When the command itself fails before any reference command runs — a path
/// argument that does not exist, a `--json` target that cannot be created, a
/// `--diff-dir` that cannot be created — or when the JSON report cannot be
/// written at the end, with a message naming the problem.
pub fn run(options: &Options, cwd: &Path, io: &mut Io<'_>) -> Result<u8, String> {
    let painter = Painter::new(io.color);
    let configs = discover::discover(&options.paths, cwd)?;
    let json_target = options
        .json
        .as_ref()
        .map(|path| JsonTarget::create(path, cwd))
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
        diff_failures: Vec::new(),
    };
    for config in &configs {
        progress(io.stderr, &format!("found config {}", config.display));
        checker.check_config(config, io.stderr)?;
    }

    let searched = if options.paths.is_empty() {
        vec![discover::default_root(cwd).display().to_string()]
    } else {
        options
            .paths
            .iter()
            .map(|p| p.display().to_string())
            .collect()
    };
    let report = Report::new(searched, std::mem::take(&mut checker.results));
    if let Some(target) = json_target {
        target.write(&report, io.stdout)?;
    }
    let _ = io.stderr.write_all(report.render(painter).as_bytes());
    if checker.diff_failures.is_empty() {
        return Ok(report.exit_code.into());
    }
    let mut failure = format!(
        "{} --diff-dir file(s) could not be written, so the command exits 1:",
        checker.diff_failures.len()
    );
    for message in &checker.diff_failures {
        failure.push_str(&format!("\n  {message}"));
    }
    let _ = writeln!(io.stderr, "{}", painter.failure(&failure));
    Ok(1)
}

/// Write one progress line to stderr.
fn progress(stderr: &mut dyn Write, line: &str) {
    let _ = writeln!(stderr, "compare: {line}");
}

/// Where `--json` goes. A file target is created before any reference command
/// runs, so a target that cannot be written fails the run before it spends
/// anything, rather than after every reference has run.
enum JsonTarget {
    Stdout,
    File { given: PathBuf, absolute: PathBuf },
}

impl JsonTarget {
    fn create(given: &Path, cwd: &Path) -> Result<Self, String> {
        if given == Path::new("-") {
            return Ok(JsonTarget::Stdout);
        }
        let absolute = cwd.join(given);
        std::fs::OpenOptions::new()
            .write(true)
            .create(true)
            .truncate(false)
            .open(&absolute)
            .map_err(|error| format!("cannot write --json {}: {error}", given.display()))?;
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
    /// `--diff-dir` files that could not be written, each with its error.
    diff_failures: Vec<String>,
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
        let config_path = canonicalize(&config.path).unwrap_or_else(|_| config.path.clone());
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
                    result_with_reason(
                        Status::CouldNotCheck,
                        config,
                        None,
                        None,
                        None,
                        error.to_string(),
                    ),
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
                return Ok(result_with_reason(
                    Status::CouldNotCheck,
                    config,
                    Some(name),
                    spec,
                    None,
                    reason,
                ));
            }
        };
        let spec = Some(resolved.args.spec.display().to_string());

        let Some((command, _)) = settings::resolve_reference_command(
            name,
            file,
            self.options.reference_command.as_deref(),
        ) else {
            return Ok(result_with_reason(
                Status::CouldNotCheck,
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
            return Ok(result_with_reason(
                Status::CouldNotCheck,
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
                let mut result = result_with_reason(
                    Status::CouldNotCheck,
                    config,
                    Some(name),
                    spec,
                    Some(run),
                    reason,
                );
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
            // The reference produced output and crozier did not: a mismatch.
            let mut result = result_with_reason(
                Status::Mismatched,
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
                let mut result = result_with_reason(
                    Status::CouldNotCheck,
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
                let shown = given.join(&file_name).display().to_string();
                match std::fs::write(absolute.join(&file_name), body) {
                    Ok(()) => comparison.diff_file = Some(shown),
                    Err(error) => {
                        let message = format!("could not write --diff-dir file {shown}: {error}");
                        progress(stderr, &format!("{label}: {message}"));
                        self.diff_failures.push(message);
                    }
                }
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

/// A result with `status` that carries only a reason: no comparison, nothing measured.
fn result_with_reason(
    status: Status,
    config: &FoundConfig,
    generator: Option<&str>,
    spec: Option<String>,
    reference: Option<ReferenceRun>,
    reason: String,
) -> GeneratorResult {
    GeneratorResult {
        status,
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

/// `std::fs::canonicalize`, as a path a user reads: on Windows, without the
/// `\\?\` verbatim prefix it puts on a drive path, which the report and the
/// reference command's environment would otherwise carry.
fn canonicalize(path: &Path) -> std::io::Result<PathBuf> {
    std::fs::canonicalize(path).map(without_verbatim_prefix)
}

/// `path` with a verbatim drive prefix (`\\?\C:\…`) rewritten to the plain
/// drive form (`C:\…`) when the plain form names the same file: short enough
/// for the classic path limit. Any other path, and every path off Windows, is
/// returned as it is.
#[cfg(windows)]
fn without_verbatim_prefix(path: PathBuf) -> PathBuf {
    use std::path::Prefix;
    let mut components = path.components();
    let Some(Component::Prefix(prefix)) = components.next() else {
        return path;
    };
    let Prefix::VerbatimDisk(disk) = prefix.kind() else {
        return path;
    };
    if components.next() != Some(Component::RootDir) {
        return path;
    }
    let plain = PathBuf::from(format!("{}:\\", char::from(disk))).join(components.as_path());
    if plain.as_os_str().len() < 260 {
        plain
    } else {
        path
    }
}

#[cfg(not(windows))]
fn without_verbatim_prefix(path: PathBuf) -> PathBuf {
    path
}

/// `base.join(path)` as an absolute path that reads cleanly for a reference
/// command: its directory resolved (so `..` and `.` are gone), its file name kept
/// as written. Falls back to dropping `.` components when the directory does not
/// exist.
fn clean_join(base: &Path, path: &Path) -> PathBuf {
    let joined = base.join(path);
    if let (Some(parent), Some(name)) = (joined.parent(), joined.file_name()) {
        if let Ok(parent) = canonicalize(parent) {
            return parent.join(name);
        }
    }
    joined
        .components()
        .filter(|c| !matches!(c, Component::CurDir))
        .collect()
}

/// The variables a reference command receives on top of the inherited
/// environment, in the order `reference_env` gives their values: where to
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
mod tests {
    //! In-process tests of `crozier compare` over real temporary repositories, the
    //! committed fixture specs and goldens, and real `sh` reference commands.

    use std::collections::BTreeSet;
    use std::path::{Path, PathBuf};

    use super::*;

    /// The `client-class-name` fixture: a small spec with a packaged and a flat
    /// golden, generated with package `fern`, project `default_package_name` and
    /// client class `AcmeClient`.
    fn fixture(rel: &str) -> PathBuf {
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("tests/fixtures/client-class-name")
            .join(rel)
    }

    /// The generator settings the fixture's goldens were produced with.
    fn golden_settings(layout: &str) -> String {
        format!(
        "    spec: {}\n    package-name: fern\n    project-name: default_package_name\n    client-class-name: AcmeClient\n    layout: {layout}\n",
        fixture("openapi.yml").display()
    )
    }

    /// A reference command copying a committed golden into place.
    fn copy_golden(golden: &str) -> String {
        format!(
            "cp -R '{}/.' \"$CROZIER_REFERENCE_OUTPUT\"",
            fixture(golden).display()
        )
    }

    struct Run {
        code: Result<u8, String>,
        stderr: String,
        stdout: String,
    }

    fn compare(options: &Options, cwd: &Path, color: bool, shell_supported: bool) -> Run {
        let mut stderr = Vec::new();
        let mut stdout = Vec::new();
        let code = {
            let mut io = Io {
                stderr: &mut stderr,
                stdout: &mut stdout,
                color,
                shell_supported,
            };
            run(options, cwd, &mut io)
        };
        Run {
            code,
            stderr: String::from_utf8(stderr).unwrap(),
            stdout: String::from_utf8(stdout).unwrap(),
        }
    }

    fn write(root: &Path, rel: &str, text: &str) {
        let path = root.join(rel);
        std::fs::create_dir_all(path.parent().unwrap()).unwrap();
        std::fs::write(path, text).unwrap();
    }

    fn read_report(path: &Path) -> Report {
        serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
    }

    fn result_for<'a>(
        report: &'a Report,
        config: &str,
        generator: Option<&str>,
    ) -> &'a GeneratorResult {
        report
            .results
            .iter()
            .find(|r| r.config_file == config && r.generator.as_deref() == generator)
            .unwrap_or_else(|| panic!("no result for {config} {generator:?}: {report:#?}"))
    }

    #[test]
    fn every_status_in_one_run_with_json_and_diffs() {
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        write(
        root,
        "crozier.yml",
        &format!(
            "generators:\n  packaged:\n{}    reference:\n      command: {}\n  flat:\n{}    reference:\n      command: {}\n  edited:\n{}    reference:\n      command: {} && echo changed >> \"$CROZIER_REFERENCE_OUTPUT/README.md\" && rm \"$CROZIER_REFERENCE_OUTPUT/reference.md\" && touch \"$CROZIER_REFERENCE_OUTPUT/extra.txt\"\n  failing:\n{}    reference:\n      command: echo the reference tool refused the spec >&2; exit 5\n  silent:\n{}    reference:\n      command: 'true'\n  unconfigured:\n{}",
            golden_settings("packaged"),
            copy_golden("expected"),
            golden_settings("flat"),
            copy_golden("expected-flat"),
            golden_settings("packaged"),
            copy_golden("expected"),
            golden_settings("packaged"),
            golden_settings("packaged"),
            golden_settings("packaged"),
        ),
    );
        write(root, "broken/crozier.yml", "generators: [not, a, map]\n");
        write(
            root,
            "nospec/.crozier.yml",
            "generators:\n  python:\n    reference:\n      command: 'true'\n",
        );

        let options = Options {
            paths: vec![],
            reference_command: None,
            json: Some(PathBuf::from("report.json")),
            diff_dir: Some(PathBuf::from("diffs")),
        };
        let run = compare(&options, root, false, true);
        assert_eq!(run.code, Ok(3), "{}", run.stderr);
        assert!(run.stdout.is_empty());
        let report = read_report(&root.join("report.json"));
        assert_eq!(report.exit_code, report::ExitStatus::Mismatched);
        assert_eq!(report.searched_paths, [root.display().to_string()]);
        assert_eq!(
            (
                report.counts.matched,
                report.counts.mismatched,
                report.counts.could_not_check
            ),
            (2, 1, 5)
        );

        let packaged = result_for(&report, "crozier.yml", Some("packaged"));
        assert_eq!(packaged.status, Status::Matched);
        let comparison = packaged.comparison.as_ref().unwrap();
        assert_eq!(comparison.layout, ComparedLayout::Packaged);
        assert!(comparison.files_compared >= 40, "{comparison:?}");
        assert_eq!(comparison.diff_file, None);
        let timing = packaged.timing.unwrap();
        let (r, c) = (
            timing.reference_seconds.unwrap(),
            timing.crozier_seconds.unwrap(),
        );
        // Read back from JSON, each figure can sit one ulp from the value derived
        // from the read-back measurements (serde_json parses without exact round-trip).
        assert!((timing.speedup.unwrap() - r / c).abs() < 1e-9, "{timing:?}");
        assert!(
            (timing.saved_seconds.unwrap() - (r - c)).abs() < 1e-9,
            "{timing:?}"
        );
        // The spec is reported as the code resolves it: its directory
        // canonicalized, with no Windows verbatim prefix.
        let spec_dir = canonicalize(&fixture("")).unwrap();
        assert_eq!(
            packaged.spec,
            Some(spec_dir.join("openapi.yml").display().to_string())
        );
        assert!(!packaged.spec.as_deref().unwrap().starts_with(r"\\?\"));

        let flat = result_for(&report, "crozier.yml", Some("flat"));
        assert_eq!(flat.status, Status::Matched);
        assert_eq!(
            flat.comparison.as_ref().unwrap().layout,
            ComparedLayout::Flat
        );

        let edited = result_for(&report, "crozier.yml", Some("edited"));
        assert_eq!(edited.status, Status::Mismatched);
        let comparison = edited.comparison.as_ref().unwrap();
        assert_eq!(comparison.differing, ["README.md"]);
        assert_eq!(comparison.only_in_reference, ["extra.txt"]);
        assert_eq!(comparison.only_in_crozier, ["reference.md"]);
        let diff_file = comparison.diff_file.as_ref().unwrap();
        assert_eq!(
            diff_file,
            &Path::new("diffs")
                .join("003-crozier.yml-edited.diff")
                .display()
                .to_string()
        );
        let diff = std::fs::read_to_string(root.join(diff_file)).unwrap();
        assert!(
            diff.contains("--- reference/README.md\n+++ crozier/README.md\n"),
            "{diff}"
        );
        assert!(diff.contains("- changed"), "{diff}");
        assert!(diff.contains("Only in reference: extra.txt"), "{diff}");
        assert!(diff.contains("Only in crozier: reference.md"), "{diff}");
        assert!(!diff.contains('\u{1b}'));

        let failing = result_for(&report, "crozier.yml", Some("failing"));
        assert_eq!(failing.status, Status::CouldNotCheck);
        let reference = failing.reference.as_ref().unwrap();
        assert_eq!(reference.exit_code, Some(5));
        assert_eq!(
            reference.diagnostic.as_deref(),
            Some("the reference tool refused the spec")
        );
        assert!(failing
            .reason
            .as_deref()
            .unwrap()
            .starts_with("the reference command exited with status 5"));
        let timing = failing.timing.unwrap();
        assert!(timing.reference_seconds.is_some());
        assert_eq!((timing.crozier_seconds, timing.speedup), (None, None));

        let silent = result_for(&report, "crozier.yml", Some("silent"));
        assert_eq!(silent.status, Status::CouldNotCheck);
        assert!(
            silent.reason.as_deref().unwrap().contains("empty"),
            "{silent:?}"
        );
        assert_eq!(silent.reference.as_ref().unwrap().exit_code, Some(0));

        let unconfigured = result_for(&report, "crozier.yml", Some("unconfigured"));
        assert_eq!(unconfigured.reason.as_deref(), Some(NO_REFERENCE_COMMAND));
        assert_eq!(
            (&unconfigured.reference, &unconfigured.timing),
            (&None, &None)
        );

        let broken = result_for(&report, "broken/crozier.yml", None);
        assert_eq!(broken.status, Status::CouldNotCheck);
        assert!(broken.reason.as_deref().unwrap().contains("invalid config"));

        let nospec = result_for(&report, "nospec/.crozier.yml", Some("python"));
        assert!(
            nospec.reason.as_deref().unwrap().contains("has no spec"),
            "{nospec:?}"
        );
        assert_eq!(nospec.spec, None);

        // Progress names each config and each side of each generator as it goes.
        for want in [
        "compare: found config crozier.yml",
        "compare: found config broken/crozier.yml",
        "compare: crozier.yml packaged: reference command starting: cp -R",
        "compare: crozier.yml packaged: reference command finished in ",
        "compare: crozier.yml packaged: crozier generation starting",
        "compare: crozier.yml packaged: crozier generation finished in ",
        "compare: crozier.yml packaged: matched",
        "compare: crozier.yml edited: mismatched",
        "compare: crozier.yml failing: could_not_check (the reference command exited with status 5)",
        "crozier compare report",
        "Result: 1 generator(s) mismatched the reference (exit 3)",
    ] {
        assert!(run.stderr.contains(want), "missing {want:?} in:\n{}", run.stderr);
    }
        assert!(!run.stderr.contains('\u{1b}'));
    }

    // Unix only: the `sh` contract this pins (`pwd`, the exported variables) is
    // one crozier offers only on Linux and macOS; on Windows every generator is
    // could-not-check (`NO_SHELL`), and an MSYS `sh` there prints `pwd` in its own
    // `/d/...` form.
    #[cfg(unix)]
    #[test]
    fn the_reference_command_receives_resolved_settings_with_defaults() {
        let repo = tempfile::tempdir().unwrap();
        let dump = tempfile::tempdir().unwrap();
        let root = repo.path();
        write(
            root,
            "svc/openapi.yml",
            &std::fs::read_to_string(fixture("openapi.yml")).unwrap(),
        );
        write(
        root,
        "svc/crozier.yml",
        "spec: ./openapi.yml\naudiences: [public, internal]\ngenerators:\n  python:\n    extra-fields: forbid\n",
    );
        let dump_file = dump.path().join("env");
        let options = Options {
            paths: vec![PathBuf::from("svc")],
            reference_command: Some(format!(
                "pwd > '{0}'; env | grep '^CROZIER_REFERENCE_' >> '{0}'; exit 1",
                dump_file.display()
            )),
            ..Options::default()
        };
        let run = compare(&options, root, false, true);
        assert_eq!(run.code, Ok(4), "{}", run.stderr);
        let dumped = std::fs::read_to_string(&dump_file).unwrap();
        let svc = canonicalize(&root.join("svc")).unwrap();
        let mut lines = dumped.lines();
        assert_eq!(lines.next(), Some(svc.display().to_string().as_str()));
        // Sorted here, by byte order: `sort`'s collation varies with the locale.
        let mut vars: Vec<&str> = lines.collect();
        vars.sort_unstable();
        let output = vars
            .iter()
            .find_map(|l| l.strip_prefix("CROZIER_REFERENCE_OUTPUT="))
            .unwrap();
        let mut expected = [
            "CROZIER_REFERENCE_AUDIENCES=public,internal".to_string(),
            "CROZIER_REFERENCE_AUDIENCE_STRICT=false".to_string(),
            "CROZIER_REFERENCE_CLIENT_CLASS_NAME=WidgetApiApi".to_string(),
            format!(
                "CROZIER_REFERENCE_CONFIG_FILE={}",
                svc.join("crozier.yml").display()
            ),
            "CROZIER_REFERENCE_EXTRA_FIELDS=forbid".to_string(),
            "CROZIER_REFERENCE_GENERATOR=python".to_string(),
            "CROZIER_REFERENCE_LAYOUT=packaged".to_string(),
            format!("CROZIER_REFERENCE_OUTPUT={output}"),
            "CROZIER_REFERENCE_PACKAGE_NAME=widget_api".to_string(),
            "CROZIER_REFERENCE_PROJECT_NAME=widget_api".to_string(),
            format!(
                "CROZIER_REFERENCE_SPEC={}",
                svc.join("openapi.yml").display()
            ),
        ];
        expected.sort_unstable();
        assert_eq!(vars, expected);
        // The output directory was a fresh temporary one, gone after the run.
        assert!(!Path::new(output).exists());
    }

    #[test]
    fn the_documented_missing_command_reason_is_the_one_crozier_reports() {
        let page =
            std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/compare.md"))
                .unwrap();
        let flat = page.split_whitespace().collect::<Vec<_>>().join(" ");
        assert!(
            flat.contains(&format!("the reason \"{NO_REFERENCE_COMMAND}\"")),
            "docs/compare.md must quote NO_REFERENCE_COMMAND verbatim"
        );
    }

    #[test]
    fn the_documented_reference_variables_are_the_ones_crozier_exports() {
        let page =
            std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/compare.md"))
                .unwrap();
        let documented: Vec<&str> = page
            .lines()
            .filter_map(|line| line.trim_start().strip_prefix("| `CROZIER_REFERENCE_"))
            .map(|rest| &rest[..rest.find('`').unwrap()])
            .collect();
        let exported: Vec<&str> = REFERENCE_VARIABLES
            .iter()
            .map(|name| name.strip_prefix("CROZIER_REFERENCE_").unwrap())
            .collect();
        assert_eq!(
            documented, exported,
            "docs/compare.md's variable table must list REFERENCE_VARIABLES, in order"
        );
    }

    /// Every property name and string `enum`/`const` value in `schema`, at any depth.
    fn schema_words(
        schema: &serde_json::Value,
        names: &mut BTreeSet<String>,
        values: &mut BTreeSet<String>,
    ) {
        match schema {
            serde_json::Value::Object(map) => {
                if let Some(serde_json::Value::Object(properties)) = map.get("properties") {
                    names.extend(properties.keys().cloned());
                }
                if let Some(serde_json::Value::String(value)) = map.get("const") {
                    values.insert(value.clone());
                }
                if let Some(serde_json::Value::Array(options)) = map.get("enum") {
                    values.extend(
                        options
                            .iter()
                            .filter_map(|v| v.as_str().map(str::to_string)),
                    );
                }
                for value in map.values() {
                    schema_words(value, names, values);
                }
            }
            serde_json::Value::Array(items) => {
                for item in items {
                    schema_words(item, names, values);
                }
            }
            _ => {}
        }
    }

    #[test]
    fn the_documented_report_shape_names_the_schemas_fields_and_values() {
        let page =
            std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/compare.md"))
                .unwrap();
        let block = page
            .split("\n```text\nschema_version:")
            .nth(1)
            .and_then(|rest| rest.split("\n```\n").next())
            .map(|rest| format!("schema_version:{rest}"))
            .expect("docs/compare.md holds the report shape");
        let (mut names, mut values) = (BTreeSet::new(), BTreeSet::new());
        schema_words(&crate::schema::compare_report(), &mut names, &mut values);
        // Quoted words are enum values; bare words, apart from the type names, are
        // field names.
        let (mut documented_names, mut documented_values) = (BTreeSet::new(), BTreeSet::new());
        for (index, part) in block.split('"').enumerate() {
            if index % 2 == 1 {
                documented_values.insert(part.to_string());
                continue;
            }
            documented_names.extend(
                part.split(|c: char| !(c.is_ascii_lowercase() || c == '_'))
                    .filter(|word| !word.is_empty())
                    .filter(|word| !["string", "integer", "number", "null"].contains(word))
                    .map(str::to_string),
            );
        }
        assert_eq!(documented_names, names, "field names");
        assert_eq!(documented_values, values, "enum values");
    }

    /// A generator whose reference holds a symbolic link, which the byte-match
    /// walk refuses. Unix only: creating a link on Windows needs a privilege CI
    /// runners lack, and an MSYS `ln -s` there copies instead of linking.
    fn linked_generator() -> String {
        if cfg!(unix) {
            format!(
                "  linked:\n{}    reference:\n      command: ln -s /etc/hostname \"$CROZIER_REFERENCE_OUTPUT/link\"\n",
                golden_settings("packaged")
            )
        } else {
            String::new()
        }
    }

    #[test]
    fn a_refused_spec_a_bad_reference_tree_and_no_shell_are_could_not_check() {
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        let refused = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/openapi-surface/probes/header-array.yml");
        write(
        root,
        "crozier.yml",
        &format!(
            "generators:\n  refused:\n    spec: {}\n    reference:\n      command: touch \"$CROZIER_REFERENCE_OUTPUT/x\"\n{}  badpackage:\n    spec: {}\n    package-name: ../escape\n",
            refused.display(),
            linked_generator(),
            fixture("openapi.yml").display(),
        ),
    );
        let run = compare(&Options::default(), root, false, true);
        assert_eq!(run.code, Ok(4), "{}", run.stderr);
        let lines: Vec<&str> = run.stderr.lines().collect();
        let reason_of = |generator: &str| {
            lines
                .iter()
                .find(|l| {
                    l.starts_with(&format!(
                        "compare: crozier.yml {generator}: could_not_check"
                    ))
                })
                .unwrap_or_else(|| panic!("{generator}: {}", run.stderr))
                .to_string()
        };
        // A document crozier refuses is reported with crozier's own diagnostic.
        assert!(reason_of("refused").contains("unsupported array schema"));
        #[cfg(unix)]
        assert!(reason_of("linked").contains("the trees could not be compared"));
        assert!(reason_of("badpackage").contains("could not read the generator's settings"));

        // Without `sh`, every generator with a command is could-not-check, unrun.
        // Its own repository, with a generator whose settings resolve on every
        // platform: the one above whose do (`linked`) exists only on unix.
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        write(
            root,
            "crozier.yml",
            &format!(
                "generators:\n  unrun:\n{}    reference:\n      command: exit 0\n",
                golden_settings("packaged")
            ),
        );
        let run = compare(&Options::default(), root, false, false);
        assert_eq!(run.code, Ok(4));
        assert!(run.stderr.contains(NO_SHELL), "{}", run.stderr);
        assert!(!run.stderr.contains("reference command starting"));
    }

    /// A read-only directory under `parent`, or `None` when this process writes
    /// through one anyway (it runs as root), which would prove nothing.
    #[cfg(unix)]
    fn read_only_dir(parent: &Path, name: &str) -> Option<PathBuf> {
        use std::os::unix::fs::PermissionsExt;
        let dir = parent.join(name);
        std::fs::create_dir_all(&dir).unwrap();
        std::fs::set_permissions(&dir, std::fs::Permissions::from_mode(0o555)).unwrap();
        let probe = dir.join(".probe");
        if std::fs::write(&probe, "").is_ok() {
            let _ = std::fs::remove_file(probe);
            return None;
        }
        Some(dir)
    }

    #[cfg(unix)]
    #[test]
    fn an_unwritable_json_target_is_refused_before_any_reference_runs() {
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        let marker = root.join("reference-ran");
        write(
            root,
            "crozier.yml",
            &format!(
                "generators:\n  packaged:\n{}    reference:\n      command: touch '{}'\n",
                golden_settings("packaged"),
                marker.display()
            ),
        );
        let Some(locked) = read_only_dir(root, "locked") else {
            return;
        };
        let options = Options {
            json: Some(locked.join("report.json")),
            ..Options::default()
        };
        let run = compare(&options, root, false, true);
        let error = run.code.unwrap_err();
        assert!(error.starts_with("cannot write --json "), "{error}");
        assert!(!marker.exists(), "a reference ran before the refusal");
        assert!(run.stderr.is_empty(), "{}", run.stderr);
    }

    #[cfg(unix)]
    #[test]
    fn a_diff_file_that_cannot_be_written_still_checks_and_reports_everything() {
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        write(
            root,
            "crozier.yml",
            &format!(
                "generators:\n  edited:\n{}    reference:\n      command: {} && echo changed >> \"$CROZIER_REFERENCE_OUTPUT/README.md\"\n  matched:\n{}    reference:\n      command: {}\n",
                golden_settings("packaged"),
                copy_golden("expected"),
                golden_settings("packaged"),
                copy_golden("expected"),
            ),
        );
        let Some(diffs) = read_only_dir(root, "diffs") else {
            return;
        };
        let options = Options {
            json: Some(PathBuf::from("report.json")),
            diff_dir: Some(diffs),
            ..Options::default()
        };
        let run = compare(&options, root, true, true);
        assert_eq!(run.code, Ok(1), "{}", run.stderr);
        assert!(
            run.stderr.contains("crozier compare report"),
            "{}",
            run.stderr
        );
        assert!(
            run.stderr.contains(
                "\u{1b}[31m1 --diff-dir file(s) could not be written, so the command exits 1:\n  could not write --diff-dir file "
            ),
            "{}",
            run.stderr
        );
        let report = read_report(&root.join("report.json"));
        assert_eq!(report.exit_code, report::ExitStatus::Mismatched);
        let edited = result_for(&report, "crozier.yml", Some("edited"));
        assert_eq!(edited.status, Status::Mismatched);
        assert_eq!(edited.comparison.as_ref().unwrap().diff_file, None);
        assert_eq!(
            result_for(&report, "crozier.yml", Some("matched")).status,
            Status::Matched
        );
    }

    #[test]
    fn a_crozier_failure_after_a_good_reference_is_a_mismatch() {
        let repo = tempfile::tempdir().unwrap();
        let root = repo.path();
        write(
            root,
            "openapi.yml",
            &std::fs::read_to_string(fixture("openapi.yml")).unwrap(),
        );
        // The reference succeeds, then leaves the spec unreadable, so crozier's
        // own generation of the same generator fails after it.
        write(
            root,
            "crozier.yml",
            &format!(
                "spec: ./openapi.yml\npackage-name: fern\ngenerators:\n  python:\n    reference:\n      command: {} && echo garbage > openapi.yml\n",
                copy_golden("expected")
            ),
        );
        let run = compare(&Options::default(), root, true, true);
        assert_eq!(run.code, Ok(3), "{}", run.stderr);
        assert!(
            run.stderr.contains(
                "compare: crozier.yml python: \u{1b}[31mmismatched\u{1b}[0m (crozier could not generate"
            ),
            "{}",
            run.stderr
        );
        assert!(run
            .stderr
            .contains("crozier produced no SDK, so no speed-up"));
    }

    #[test]
    fn json_to_stdout_nothing_found_and_colour() {
        let empty = tempfile::tempdir().unwrap();
        let options = Options {
            json: Some(PathBuf::from("-")),
            ..Options::default()
        };
        let run = compare(&options, empty.path(), true, true);
        assert_eq!(run.code, Ok(0));
        let report: Report = serde_json::from_str(&run.stdout).unwrap();
        assert!(report.results.is_empty());
        assert!(!run.stdout.contains('\u{1b}'));
        assert!(run
            .stderr
            .contains("No crozier config was found under the searched paths"));
        assert!(run
            .stderr
            .contains("\u{1b}[32mResult: nothing to check (exit 0)\u{1b}[0m"));

        let repo = tempfile::tempdir().unwrap();
        write(
            repo.path(),
            "crozier.yml",
            &format!(
                "reference:\n  command: {}\ngenerators:\n  python:\n{}",
                copy_golden("expected"),
                golden_settings("packaged")
            ),
        );
        let run = compare(&options, repo.path(), true, true);
        assert_eq!(run.code, Ok(0), "{}", run.stderr);
        assert!(
            run.stderr.contains("\u{1b}[32mmatched\u{1b}[0m"),
            "{}",
            run.stderr
        );
        assert!(!run.stdout.contains('\u{1b}'));
        let report: Report = serde_json::from_str(&run.stdout).unwrap();
        assert_eq!(report.timing_totals.generators_timed, 1);
    }

    #[test]
    fn the_command_itself_failing_writes_no_report() {
        let repo = tempfile::tempdir().unwrap();
        write(repo.path(), "file", "");
        let missing = compare(
            &Options {
                paths: vec![PathBuf::from("absent")],
                ..Options::default()
            },
            repo.path(),
            false,
            true,
        );
        assert_eq!(missing.code, Err("path not found: absent".to_string()));

        let bad_json = compare(
            &Options {
                json: Some(PathBuf::from("no/such/dir/report.json")),
                ..Options::default()
            },
            repo.path(),
            false,
            true,
        );
        assert!(bad_json.code.unwrap_err().contains("cannot write --json"));

        let bad_diffs = compare(
            &Options {
                diff_dir: Some(PathBuf::from("file/diffs")),
                ..Options::default()
            },
            repo.path(),
            false,
            true,
        );
        assert!(bad_diffs
            .code
            .unwrap_err()
            .contains("could not create --diff-dir"));
        assert!(bad_diffs.stderr.is_empty());
    }

    #[test]
    fn a_diff_file_name_is_numbered_and_filesystem_safe() {
        assert_eq!(
            diff_file_name(7, "a b/crozier.yml", "py:thon"),
            "007-a_b_crozier.yml-py_thon.diff"
        );
    }

    #[test]
    fn a_rendered_diff_describes_each_kind_of_difference() {
        let body = render_diff(
            "c.yml",
            "g",
            &[
                (
                    "bin".into(),
                    Difference::Binary {
                        reference: 1,
                        crozier: 2,
                    },
                ),
                ("x".into(), Difference::Processing("boom".into())),
                ("t".into(), Difference::Text(None)),
            ],
        );
        assert!(body.contains("Binary files differ: bin (reference 1 bytes, crozier 2 bytes)"));
        assert!(body.contains("Could not compare x: boom"));
        assert!(body.contains("--- reference/t\n+++ crozier/t\n"));
    }

    #[test]
    fn canonicalize_resolves_without_a_verbatim_prefix() {
        let dir = tempfile::tempdir().unwrap();
        std::fs::create_dir(dir.path().join("sub")).unwrap();
        let resolved = canonicalize(&dir.path().join("sub/../sub")).unwrap();
        assert!(!resolved.display().to_string().starts_with(r"\\?\"));
        assert_eq!(
            std::fs::canonicalize(&resolved).unwrap(),
            std::fs::canonicalize(dir.path().join("sub")).unwrap()
        );
        assert!(canonicalize(&dir.path().join("absent")).is_err());
    }

    #[cfg(windows)]
    #[test]
    fn a_verbatim_drive_path_reads_as_a_plain_one() {
        assert_eq!(
            without_verbatim_prefix(PathBuf::from(r"\\?\D:\a\crozier\openapi.yml")),
            PathBuf::from(r"D:\a\crozier\openapi.yml")
        );
        // A share, or a plain form past the classic length limit, stays verbatim.
        let share = PathBuf::from(r"\\?\UNC\server\share\api.yml");
        assert_eq!(without_verbatim_prefix(share.clone()), share);
        let long = PathBuf::from(format!(r"\\?\C:\{}", "a".repeat(300)));
        assert_eq!(without_verbatim_prefix(long.clone()), long);
        let plain = PathBuf::from(r"C:\already\plain");
        assert_eq!(without_verbatim_prefix(plain.clone()), plain);
    }

    #[test]
    fn clean_join_resolves_the_directory_and_drops_dot_segments() {
        assert_eq!(
            clean_join(Path::new("/no/such"), Path::new("./b/./c.yml")),
            PathBuf::from("/no/such/b/c.yml")
        );
        let dir = tempfile::tempdir().unwrap();
        let real = canonicalize(dir.path()).unwrap();
        std::fs::create_dir(real.join("sub")).unwrap();
        assert_eq!(
            clean_join(&real.join("sub"), Path::new("../api.yml")),
            real.join("api.yml")
        );
    }
}
