//! Running a generator's reference command and finding the reference SDK it
//! wrote.
//!
//! The command is the user's: crozier runs it as `sh -c <command>` from the config
//! file's directory, adds the `CROZIER_REFERENCE_*` variables to the environment
//! it inherits, and times the one invocation. It does not isolate the command.

use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::time::Instant;

/// How many trailing lines of the command's output a diagnostic keeps.
const TAIL_LINES: usize = 20;

/// How one reference-command invocation ended.
#[derive(Debug, Clone, PartialEq)]
pub struct Outcome {
    /// The exit status; `None` when it could not start or ended without one.
    pub exit_code: Option<i32>,
    /// Why it could not start, when it could not.
    pub spawn_error: Option<String>,
    /// The command's stderr.
    pub stderr: String,
    /// Its stdout, kept only as a fallback diagnostic when stderr is empty.
    pub stdout: String,
    /// Wall time of the invocation, in seconds.
    pub seconds: f64,
}

/// Run `command` under `sh -c` from `cwd`, adding `env` to the inherited
/// environment. Its stdin is empty and its output is captured, never passed
/// through, so `--json -` keeps stdout to the report alone.
#[must_use]
pub fn run(command: &str, cwd: &Path, env: &[(String, String)]) -> Outcome {
    let started = Instant::now();
    let output = Command::new("sh")
        .arg("-c")
        .arg(command)
        .current_dir(cwd)
        .envs(env.iter().map(|(k, v)| (k, v)))
        .stdin(Stdio::null())
        .output();
    let seconds = started.elapsed().as_secs_f64();
    match output {
        Ok(output) => Outcome {
            exit_code: output.status.code(),
            spawn_error: None,
            stderr: String::from_utf8_lossy(&output.stderr).into_owned(),
            stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
            seconds,
        },
        Err(error) => Outcome {
            exit_code: None,
            spawn_error: Some(error.to_string()),
            stderr: String::new(),
            stdout: String::new(),
            seconds,
        },
    }
}

impl Outcome {
    /// Whether the command ran and exited 0.
    #[must_use]
    pub fn succeeded(&self) -> bool {
        self.exit_code == Some(0)
    }

    /// The exit status as a progress line shows it.
    #[must_use]
    pub fn status_text(&self) -> String {
        match (&self.spawn_error, self.exit_code) {
            (Some(_), _) => "could not start".to_string(),
            (None, Some(code)) => format!("exit {code}"),
            (None, None) => "ended without an exit status".to_string(),
        }
    }

    /// The command's own diagnostic: the tail of its stderr (of its stdout when
    /// stderr is empty), or why it could not start. `None` when there is none.
    #[must_use]
    pub fn diagnostic(&self) -> Option<String> {
        if let Some(error) = &self.spawn_error {
            return Some(format!("could not run `sh`: {error}"));
        }
        let source = if self.stderr.trim().is_empty() {
            &self.stdout
        } else {
            &self.stderr
        };
        let tail = tail(source);
        (!tail.is_empty()).then_some(tail)
    }

    /// The `could_not_check` reason for a command that did not exit 0, carrying
    /// its exit status and diagnostic.
    #[must_use]
    pub fn failure_reason(&self) -> String {
        let what = match (&self.spawn_error, self.exit_code) {
            (Some(_), _) => "the reference command could not be started".to_string(),
            (None, Some(code)) => format!("the reference command exited with status {code}"),
            (None, None) => "the reference command was terminated by a signal".to_string(),
        };
        match self.diagnostic() {
            Some(diagnostic) => format!("{what}:\n{diagnostic}"),
            None => format!("{what} and printed nothing"),
        }
    }
}

/// The last [`TAIL_LINES`] non-blank-trailing lines of `text`.
fn tail(text: &str) -> String {
    let lines: Vec<&str> = text.trim_end().lines().collect();
    lines[lines.len().saturating_sub(TAIL_LINES)..].join("\n")
}

/// The reference SDK a successful command left in `output`: `output` itself, or
/// its single subdirectory when it holds exactly one entry and that entry is a
/// directory.
///
/// # Errors
///
/// When the reference is empty, or ambiguous (several directories and no file,
/// so no one of them is evidently the SDK) — each with a reason naming the
/// problem.
pub fn locate(output: &Path) -> Result<PathBuf, String> {
    let mut entries: Vec<PathBuf> = std::fs::read_dir(output)
        .map_err(|error| format!("could not read $CROZIER_REFERENCE_OUTPUT: {error}"))?
        .filter_map(|entry| entry.ok().map(|entry| entry.path()))
        .collect();
    entries.sort();
    let is_dir = |path: &PathBuf| {
        std::fs::symlink_metadata(path).is_ok_and(|metadata| metadata.file_type().is_dir())
    };
    match entries.as_slice() {
        [] => Err(
            "the reference command exited 0 but left $CROZIER_REFERENCE_OUTPUT empty".to_string(),
        ),
        [only] if is_dir(only) => {
            let empty = std::fs::read_dir(only).map_or(true, |mut dir| dir.next().is_none());
            if empty {
                Err(format!(
                    "the reference command exited 0 but its single subdirectory `{}` of \
                     $CROZIER_REFERENCE_OUTPUT is empty",
                    only.file_name().unwrap_or_default().to_string_lossy()
                ))
            } else {
                Ok(only.clone())
            }
        }
        many if many.len() > 1 && many.iter().all(is_dir) => Err(format!(
            "the reference is ambiguous: $CROZIER_REFERENCE_OUTPUT holds {} directories and \
             no file; write the reference SDK into it directly or into exactly one subdirectory",
            many.len()
        )),
        _ => Ok(output.to_path_buf()),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn run_passes_the_environment_and_working_directory_and_captures_output() {
        let dir = tempfile::tempdir().unwrap();
        let env = [(
            "CROZIER_REFERENCE_GENERATOR".to_string(),
            "python".to_string(),
        )];
        let outcome = run(
            "printf '%s %s' \"$CROZIER_REFERENCE_GENERATOR\" \"$(pwd)\"; echo oops >&2",
            dir.path(),
            &env,
        );
        assert!(outcome.succeeded(), "{outcome:?}");
        let cwd = std::fs::canonicalize(dir.path()).unwrap();
        assert_eq!(outcome.stdout, format!("python {}", cwd.display()));
        assert_eq!(outcome.status_text(), "exit 0");
        assert_eq!(outcome.diagnostic().as_deref(), Some("oops"));
        assert!(outcome.seconds >= 0.0);
    }

    #[test]
    fn a_failure_reason_carries_the_status_and_the_stderr_tail() {
        let dir = tempfile::tempdir().unwrap();
        let outcome = run(
            "for i in $(seq 1 30); do echo line$i >&2; done; exit 7",
            dir.path(),
            &[],
        );
        assert_eq!(outcome.exit_code, Some(7));
        let reason = outcome.failure_reason();
        assert!(
            reason.starts_with("the reference command exited with status 7:\n"),
            "{reason}"
        );
        assert!(
            reason.contains("line30") && reason.contains("line11"),
            "{reason}"
        );
        assert!(!reason.contains("line10\n"), "{reason}");

        // stdout stands in when stderr is empty; silence says so.
        let outcome = run("echo only-stdout; exit 2", dir.path(), &[]);
        assert!(outcome.failure_reason().ends_with("only-stdout"));
        let outcome = run("exit 3", dir.path(), &[]);
        assert_eq!(
            outcome.failure_reason(),
            "the reference command exited with status 3 and printed nothing"
        );
    }

    #[cfg(unix)]
    #[test]
    fn a_signal_and_a_failed_start_are_reported() {
        let dir = tempfile::tempdir().unwrap();
        let outcome = run("kill -9 $$", dir.path(), &[]);
        assert_eq!(outcome.exit_code, None);
        assert_eq!(outcome.status_text(), "ended without an exit status");
        assert!(outcome.failure_reason().contains("terminated by a signal"));

        let outcome = run("true", &dir.path().join("missing-dir"), &[]);
        assert!(outcome.spawn_error.is_some());
        assert_eq!(outcome.status_text(), "could not start");
        assert!(outcome.failure_reason().contains("could not be started"));
        assert!(outcome.diagnostic().unwrap().contains("could not run `sh`"));
    }

    #[test]
    fn locate_takes_the_directory_or_its_single_subdirectory() {
        let dir = tempfile::tempdir().unwrap();
        let out = dir.path();
        assert!(locate(out).unwrap_err().contains("empty"));

        std::fs::create_dir(out.join("sdk")).unwrap();
        assert!(locate(out)
            .unwrap_err()
            .contains("single subdirectory `sdk`"));
        std::fs::write(out.join("sdk/README.md"), "x").unwrap();
        assert_eq!(locate(out).unwrap(), out.join("sdk"));

        std::fs::create_dir(out.join("other")).unwrap();
        assert!(locate(out).unwrap_err().contains("ambiguous"));

        std::fs::write(out.join("__init__.py"), "").unwrap();
        assert_eq!(locate(out).unwrap(), out);

        let error = locate(&out.join("absent")).unwrap_err();
        assert!(error.contains("could not read"), "{error}");
    }
}
