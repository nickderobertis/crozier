//! Formatting generated Python by delegating to `ruff format`.
//!
//! Fern runs `ruff format` (line length 120) over its output, so crozier must
//! wrap identically to match byte-for-byte. Rather than reproduce ruff's line
//! layout in Rust, crozier emits content-correct Python and hands the final
//! wrapping to `ruff` itself — the same tool Fern uses. `ruff format` is
//! deterministic and its style has been verified byte-identical, on the shapes
//! crozier emits, to the `0.11.5` Fern pins (see `docs/matching.md`).
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
