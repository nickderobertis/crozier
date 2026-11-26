//! Formatting generated Python by delegating to `ruff format`.
//!
//! Fern runs `ruff format` (line length 120) over its output, so crozier must
//! wrap identically to match byte-for-byte. Rather than reproduce ruff's line
//! layout in Rust, crozier emits content-correct Python and hands the final
//! wrapping to `ruff` itself — the same tool Fern uses. `ruff format` is
//! deterministic and its style has been verified byte-identical, on the shapes
//! crozier emits, to the version Fern pins (see `.ruff-version` and
//! `docs/matching.md`).
//!
//! `ruff` is invoked as an external process (not the unstable `0.0.x` library
//! crates), so it is a runtime prerequisite of `crozier generate`; a missing or
//! failing `ruff` surfaces as [`Error::Format`] with an actionable message.

use std::io::Write;
use std::process::{Command, Stdio};

use crate::error::{Error, Result};

/// ruff's line length for the generated SDK files (Fern's `[tool.ruff]`
/// `line-length = 120`). The worked example snippets embedded in docstrings are
/// pre-wrapped at ruff's default 88 before emission and are opaque string
/// content here, so a single file-level width is correct.
pub const LINE_LENGTH: usize = 120;

/// Format one Python source string with `ruff format`, returning the formatted
/// text. `file` names the logical output for error messages. `width` is the
/// target line length. Runs `ruff format --stdin-filename <file> -`, piping the
/// source through stdin so nothing touches disk.
pub fn format_source(file: &str, source: &str, width: usize) -> Result<String> {
    let _format = crate::profile::phase("format");
    let done = crate::profile::spawn_timer("ruff");
    let result = format_source_inner(file, source, width);
    done();
    result
}

fn format_source_inner(file: &str, source: &str, width: usize) -> Result<String> {
    let mut child = Command::new("ruff")
        .arg("format")
        .arg("--line-length")
        .arg(width.to_string())
        // A filename lets ruff apply the right syntax rules and appear in its
        // diagnostics; `-` reads the actual source from stdin.
        .arg("--stdin-filename")
        .arg(file)
        .arg("-")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|source| Error::Format {
            file: file.to_string(),
            message: match source.kind() {
                std::io::ErrorKind::NotFound => {
                    "`ruff` was not found on PATH; install it (e.g. `pip install ruff` \
                     or see https://docs.astral.sh/ruff/installation/) — crozier defers \
                     Python formatting to ruff"
                        .to_string()
                }
                _ => format!("could not run `ruff`: {source}"),
            },
        })?;

    child
        .stdin
        .take()
        .expect("stdin was piped")
        .write_all(source.as_bytes())
        .map_err(|source| Error::Format {
            file: file.to_string(),
            message: format!("could not write source to ruff: {source}"),
        })?;

    let output = child.wait_with_output().map_err(|source| Error::Format {
        file: file.to_string(),
        message: format!("waiting on ruff failed: {source}"),
    })?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Err(Error::Format {
            file: file.to_string(),
            message: format!("ruff exited with {}: {}", output.status, stderr.trim()),
        });
    }

    String::from_utf8(output.stdout).map_err(|source| Error::Format {
        file: file.to_string(),
        message: format!("ruff produced non-UTF-8 output: {source}"),
    })
}

/// SPIKE ONLY (`spike-windows-lane-breakdown`): how a generation's files are
/// formatted, from `CROZIER_SPIKE_RUFF_BATCH`.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum FormatMode {
    /// Unset or empty: one `ruff format` per file, as on `main`.
    PerFile,
    /// `1`: one `ruff format` over the whole generation.
    Batch,
    /// `verify`: both, failing the generation on any byte of difference.
    Verify,
}

impl FormatMode {
    /// Read the mode, refusing any value it does not name.
    ///
    /// # Errors
    ///
    /// When the variable holds anything but empty, `1` or `verify`.
    pub fn from_env() -> Result<Self> {
        match std::env::var_os("CROZIER_SPIKE_RUFF_BATCH") {
            None => Ok(Self::PerFile),
            Some(value) => match value.to_str() {
                Some("") => Ok(Self::PerFile),
                Some("1") => Ok(Self::Batch),
                Some("verify") => Ok(Self::Verify),
                _ => Err(Error::Format {
                    file: "(every file)".to_string(),
                    message: format!(
                        "CROZIER_SPIKE_RUFF_BATCH must be empty, `1` or `verify`, not {value:?}"
                    ),
                }),
            },
        }
    }
}

// llmlint: ignore[changed_behavior_has_e2e] SPIKE ONLY: this branch never lands (its task: "no tests of its own beyond what keeps its harness honest"); the durable generation-cost node owns this proof, and run 45840622476's A/B exercised the batch path (30 ruff processes over 3 large generations). Its byte identity is proved by verify over all 1,150 crozier-e2e tests, and ci-profile-journeys drives the batch, verify-mismatch and refused-mode paths.
/// SPIKE ONLY (`spike-windows-lane-breakdown`): format every `(path, source)`
/// with as few `ruff format` processes as the platform's command line allows,
/// instead of one process per file, staged at their generated relative paths.
///
/// # Errors
///
/// When the staging tree cannot be written or ruff fails.
pub fn format_batch(items: &[(String, String)], width: usize) -> Result<Vec<String>> {
    let fail = |file: &str, message: String| Error::Format {
        file: file.to_string(),
        message,
    };
    let nanos = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map_or(0, |d| d.as_nanos());
    // Staged outside the caller's tree and formatted `--isolated`: staged under the working
    // directory, ruff applied the repository's own `force-exclude` list (`templates`) and left
    // a generated `templates/` package unformatted (run 45863948064, letta and maif-otoroshi).
    let stage =
        std::env::temp_dir().join(format!("crozier-spike-ruff-{}-{nanos}", std::process::id()));
    if let Some((path, _)) = items.iter().find(|(path, _)| {
        !std::path::Path::new(path)
            .components()
            .all(|c| matches!(c, std::path::Component::Normal(_)))
    }) {
        return Err(fail(
            path,
            "a generated path must stay inside its tree to be staged".to_string(),
        ));
    }
    let result = (|| {
        for (path, source) in items {
            let full = stage.join(path);
            if let Some(parent) = full.parent() {
                std::fs::create_dir_all(parent).map_err(|e| fail(path, format!("stage: {e}")))?;
            }
            std::fs::write(&full, source).map_err(|e| fail(path, format!("stage: {e}")))?;
        }
        let mut chunks: Vec<Vec<std::path::PathBuf>> = vec![Vec::new()];
        let mut length = 0;
        for (path, _) in items {
            let full = stage.join(path);
            let len = full.as_os_str().len() + 3;
            if length + len > 24_000 && !chunks.last().is_some_and(Vec::is_empty) {
                chunks.push(Vec::new());
                length = 0;
            }
            length += len;
            chunks.last_mut().expect("one chunk").push(full);
        }
        for chunk in chunks.iter().filter(|c| !c.is_empty()) {
            let done = crate::profile::spawn_timer("ruff");
            let output = Command::new("ruff")
                .arg("format")
                .arg("--isolated")
                .arg("--no-cache")
                .arg("--line-length")
                .arg(width.to_string())
                .args(chunk)
                .stdin(Stdio::null())
                .output();
            done();
            let output =
                output.map_err(|e| fail("(batch)", format!("could not run `ruff`: {e}")))?;
            if !output.status.success() {
                return Err(fail(
                    "(batch)",
                    format!(
                        "ruff exited with {}: {}",
                        output.status,
                        String::from_utf8_lossy(&output.stderr).trim()
                    ),
                ));
            }
        }
        items
            .iter()
            .map(|(path, _)| {
                std::fs::read_to_string(stage.join(path))
                    .map_err(|e| fail(path, format!("read back: {e}")))
            })
            .collect()
    })();
    let _ = std::fs::remove_dir_all(&stage);
    result
}

#[cfg(test)]
mod tests {
    use super::{format_source, LINE_LENGTH};
    use crate::error::Error;

    #[test]
    fn formats_poorly_spaced_source() {
        // ruff normalizes spacing and adds the trailing newline — proof the real
        // formatter ran over the piped source.
        let out = format_source("x.py", "x={'a':1,'b':2}", LINE_LENGTH).unwrap();
        assert_eq!(out, "x = {\"a\": 1, \"b\": 2}\n");
    }

    #[test]
    fn wraps_at_the_requested_width() {
        // A call that overflows the width is split across lines with a trailing
        // comma; a wide width leaves it flat. Same input, width drives the layout.
        let src = "f(aaaaaaaaaa, bbbbbbbbbb, cccccccccc, dddddddddd, eeeeeeeeee)\n";
        assert_eq!(format_source("x.py", src, 200).unwrap(), src);
        assert!(format_source("x.py", src, 20).unwrap().contains(",\n"));
    }

    #[test]
    fn invalid_python_is_a_format_error() {
        // ruff exits non-zero on a syntax error; that surfaces as Error::Format
        // rather than a panic or silent pass-through.
        let err = format_source("x.py", "def (:\n", LINE_LENGTH).unwrap_err();
        assert!(matches!(err, Error::Format { .. }));
    }
}
