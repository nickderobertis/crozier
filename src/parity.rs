//! The byte-match rules: how crozier's output tree is compared with a
//! **reference** tree that has the shape of Fern's Python SDK output.
//!
//! crozier's contract is that its output equals the reference once both sides
//! are normalized here, and nowhere else. The corpus gate (`tests/e2e.rs`), its
//! `just fixtures-gaps` / `just fixtures-diff` reporters, and `crozier compare`
//! all decide a match with these functions, so "matches" has one definition.
//!
//! The per-file rules ([`normalized_pair`]), applied to both sides alike:
//!
//! - every file: the SDK-identity headers are normalized
//!   ([`normalize_sdk_headers`]);
//! - `.py`: Python comments are stripped ([`crate::strip_python_comments`]);
//! - `__init__.py`: additionally, leading blank lines are dropped and the imports
//!   are sorted with `ruff check --select I --fix` ([`normalize_init`]);
//! - exactly `.fern/metadata.json` (Fern's own provenance record, at the SDK
//!   root — [`FERN_METADATA`]): the `generatorConfig` block is dropped
//!   ([`normalize_metadata`]). Any other file whose name ends in
//!   `metadata.json` (say `types/user_metadata.json`) is SDK content, so it
//!   gets no such rule;
//! - anything else is compared as-is.
//!
//! The tree rules ([`tree_differences`]): the comparison is bidirectional (a file
//! on only one side is a difference), a symbolic link on either side is refused
//! rather than followed, and the `.crozier-fern-golden.json` provenance record a
//! committed golden carries is not part of either tree.
//!
//! A committed golden is already comment-stripped; a live reference is not. The
//! comment strip is idempotent over every committed golden (pinned by this
//! module's tests), so stripping both sides serves both inputs with one rule.

use std::collections::BTreeSet;
use std::io::Write;
use std::path::Path;
use std::process::{Command, Stdio};

use crate::strip_python_comments;

/// The provenance record a committed golden tree carries beside the reference
/// output. It is not reference output, so neither side's walk includes it.
pub const PROVENANCE_FILE: &str = ".crozier-fern-golden.json";

/// The SDK-relative path of Fern's own metadata record — the one file
/// [`normalize_metadata`] applies to. `rel` is always `/`-separated (see
/// [`walk_files`]), so this exact match holds on Windows too.
pub const FERN_METADATA: &str = ".fern/metadata.json";

/// Normalize the SDK-identity headers out of the comparison. crozier brands its
/// own `X-Crozier-*` headers rather than impersonating the reference, and —
/// because it reproduces the reference's *packaged* wrapper — always emits the
/// `SDK-Name`/`SDK-Version` headers that publishing metadata supplies, which a
/// credential-free local reference omits. Both are deliberate, non-behavioral
/// differences in tool branding/packaging, so drop the `SDK-Name`/`SDK-Version`
/// lines and canonicalize the remaining `X-Crozier-` prefix (the `Language`
/// header) to `X-Fern-`. Applied to both sides; a no-op on lines a tree doesn't
/// contain.
#[must_use]
pub fn normalize_sdk_headers(content: &str) -> String {
    let is_sdk_identity_line = |line: &str| {
        let t = line.trim_start();
        [
            "X-Fern-SDK-Name",
            "X-Crozier-SDK-Name",
            "X-Fern-SDK-Version",
            "X-Crozier-SDK-Version",
        ]
        .iter()
        .any(|h| t.starts_with(&format!("\"{h}\"")))
    };
    content
        .split_inclusive('\n')
        .filter(|line| !is_sdk_identity_line(line))
        .collect::<String>()
        .replace("X-Crozier-", "X-Fern-")
}

/// Normalize a lazy-loader `__init__.py` for comparison: drop leading blank lines
/// (a comment-strip artifact) and canonicalize the import order with `ruff` isort,
/// so the semantically-irrelevant `TYPE_CHECKING` ordering does not gate the match.
///
/// # Errors
///
/// When `ruff` cannot be run or rejects the input.
pub fn normalize_init(content: &str) -> Result<String, String> {
    let trimmed: String = content
        .split_inclusive('\n')
        .skip_while(|line| line.trim().is_empty())
        .collect();
    ruff_isort(&trimmed)
}

/// Drop the `generatorConfig` block from `.fern/metadata.json`. A reference
/// generated with `pydantic_config.enum_type: python_enums` (so enums render as
/// real classes — see docs/matching.md) records that config in its provenance
/// file. crozier's output carries no generator config whichever `enum-type` it
/// was generated with, so — like the SDK-identity headers — this reference-only provenance is
/// normalized out of both sides rather than faked by crozier. A no-op on content
/// without the block. The block is the object's last key, so removing it plus the
/// preceding comma restores the shorter form.
#[must_use]
pub fn normalize_metadata(content: &str) -> String {
    let Some(start) = content.find("\"generatorConfig\"") else {
        return content.to_string();
    };
    let before = content[..start].trim_end();
    let before = before.strip_suffix(',').unwrap_or(before);
    // Skip past the balanced `{ ... }` value that follows `"generatorConfig":`.
    let rest = &content[start..];
    let (mut depth, mut started, mut end) = (0i32, false, rest.len());
    for (i, ch) in rest.char_indices() {
        match ch {
            '{' => {
                depth += 1;
                started = true;
            }
            '}' if started => {
                depth -= 1;
                if depth == 0 {
                    end = i + 1;
                    break;
                }
            }
            _ => {}
        }
    }
    format!("{before}{}", &rest[end..])
}

/// Run `ruff check --select I --fix` over a source string, returning the
/// import-sorted result. Uses the same `ruff` the generator depends on.
fn ruff_isort(source: &str) -> Result<String, String> {
    let mut child = Command::new("ruff")
        .args([
            "check",
            "--select",
            "I",
            "--fix",
            "--stdin-filename",
            "x.py",
            "-",
        ])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|error| format!("could not run ruff (see docs/matching.md): {error}"))?;
    child
        .stdin
        .take()
        .ok_or_else(|| "ruff stdin was not piped".to_string())?
        .write_all(source.as_bytes())
        .map_err(|error| format!("could not write to ruff: {error}"))?;
    let out = child
        .wait_with_output()
        .map_err(|error| format!("could not wait for ruff: {error}"))?;
    // Trust ruff's stdout only when it exited cleanly — a non-zero exit (e.g. a
    // syntax error in the input) must surface, not silently yield wrong text.
    if !out.status.success() {
        return Err(format!(
            "ruff isort failed ({}): {}",
            out.status,
            String::from_utf8_lossy(&out.stderr).trim()
        ));
    }
    String::from_utf8(out.stdout).map_err(|error| format!("ruff output is not UTF-8: {error}"))
}

/// The exact `(crozier, reference)` strings the comparison decides on for the
/// file at relative path `rel`, after the per-file rules in the module docs.
/// Shared by the match check and the diff writers, so a printed diff is precisely
/// what the comparison sees.
///
/// # Errors
///
/// When an `__init__.py` cannot be normalized (see [`normalize_init`]).
pub fn normalized_pair(
    rel: &str,
    crozier: &str,
    reference: &str,
) -> Result<(String, String), String> {
    let crozier = normalize_sdk_headers(crozier);
    let reference = normalize_sdk_headers(reference);
    if rel.ends_with("__init__.py") {
        Ok((
            normalize_init(&strip_python_comments(&crozier))?,
            normalize_init(&strip_python_comments(&reference))?,
        ))
    } else if rel.ends_with(".py") {
        Ok((
            strip_python_comments(&crozier),
            strip_python_comments(&reference),
        ))
    } else if rel == FERN_METADATA {
        Ok((normalize_metadata(&crozier), normalize_metadata(&reference)))
    } else {
        Ok((crozier, reference))
    }
}

/// Whether crozier's `rel` matches the reference's under [`normalized_pair`].
///
/// # Errors
///
/// When the pair cannot be normalized.
pub fn files_match(rel: &str, crozier: &str, reference: &str) -> Result<bool, String> {
    let (crozier, reference) = normalized_pair(rel, crozier, reference)?;
    Ok(crozier == reference)
}

/// A minimal unified-style line diff of two already-normalized texts,
/// dependency-free. Lines only in `reference` are prefixed `-`, only in `crozier`
/// `+`, shared lines a space; runs of unchanged lines beyond `CONTEXT` around each
/// change collapse to a `⋮ (N unchanged line(s))` marker so a one-line drift in a
/// large file prints a few lines, not the whole file. Returns `None` when the two
/// are byte-identical.
#[must_use]
pub fn unified_diff(reference: &str, crozier: &str) -> Option<String> {
    if reference == crozier {
        return None;
    }
    const CONTEXT: usize = 3;
    let a: Vec<&str> = reference.lines().collect();
    let b: Vec<&str> = crozier.lines().collect();
    let (n, m) = (a.len(), b.len());

    // Longest-common-subsequence lengths, filled from the bottom-right.
    let mut lcs = vec![vec![0u32; m + 1]; n + 1];
    for i in (0..n).rev() {
        for j in (0..m).rev() {
            lcs[i][j] = if a[i] == b[j] {
                lcs[i + 1][j + 1] + 1
            } else {
                lcs[i + 1][j].max(lcs[i][j + 1])
            };
        }
    }

    // Backtrack into an edit script of (sign, line) ops.
    let mut ops: Vec<(char, &str)> = Vec::new();
    let (mut i, mut j) = (0usize, 0usize);
    while i < n && j < m {
        if a[i] == b[j] {
            ops.push((' ', a[i]));
            i += 1;
            j += 1;
        } else if lcs[i + 1][j] >= lcs[i][j + 1] {
            ops.push(('-', a[i]));
            i += 1;
        } else {
            ops.push(('+', b[j]));
            j += 1;
        }
    }
    while i < n {
        ops.push(('-', a[i]));
        i += 1;
    }
    while j < m {
        ops.push(('+', b[j]));
        j += 1;
    }

    // Keep every change, plus CONTEXT unchanged lines on each side; collapse the rest.
    let keep: Vec<bool> = (0..ops.len())
        .map(|k| {
            let lo = k.saturating_sub(CONTEXT);
            let hi = (k + CONTEXT).min(ops.len() - 1);
            (lo..=hi).any(|x| ops[x].0 != ' ')
        })
        .collect();

    let mut out = String::new();
    let mut elided = 0usize;
    for (k, (sign, line)) in ops.iter().enumerate() {
        if keep[k] {
            if elided > 0 {
                out.push_str(&format!("      ⋮ ({elided} unchanged line(s))\n"));
                elided = 0;
            }
            out.push(*sign);
            out.push(' ');
            out.push_str(line);
            out.push('\n');
        } else {
            elided += 1;
        }
    }
    if elided > 0 {
        out.push_str(&format!("      ⋮ ({elided} unchanged line(s))\n"));
    }
    Some(out)
}

/// Every file under `root`, as `/`-separated paths relative to `root`, sorted.
/// A symbolic link anywhere (the root included) is refused rather than followed,
/// and the [`PROVENANCE_FILE`] at the root is skipped. A missing root is empty.
///
/// # Errors
///
/// On a symbolic link or an unreadable directory.
pub fn walk_files(root: &Path) -> Result<Vec<String>, String> {
    fn rec(base: &Path, dir: &Path, out: &mut Vec<String>) -> Result<(), String> {
        let mut entries = Vec::new();
        let directory = std::fs::read_dir(dir)
            .map_err(|error| format!("read_dir {}: {error}", dir.display()))?;
        for entry in directory {
            entries.push(
                entry
                    .map_err(|error| format!("read_dir entry in {}: {error}", dir.display()))?
                    .path(),
            );
        }
        entries.sort();
        for path in entries {
            let metadata = std::fs::symlink_metadata(&path)
                .map_err(|error| format!("metadata {}: {error}", path.display()))?;
            if metadata.file_type().is_symlink() {
                return Err(format!(
                    "refusing to follow symbolic link while walking {}",
                    path.display()
                ));
            }
            if metadata.is_dir() {
                rec(base, &path, out)?;
            } else {
                let rel = path.strip_prefix(base).map_err(|error| {
                    format!(
                        "{} is not below {}: {error}",
                        path.display(),
                        base.display()
                    )
                })?;
                let rel = rel.to_string_lossy().replace('\\', "/");
                // Automation provenance is committed atomically inside a golden
                // directory, but it is not reference output and crozier must not
                // be expected to emit it.
                if rel != PROVENANCE_FILE {
                    out.push(rel);
                }
            }
        }
        Ok(())
    }
    let mut out = Vec::new();
    if root.is_symlink() {
        return Err(format!(
            "refusing to follow symbolic link while walking {}",
            root.display()
        ));
    }
    if root.is_dir() {
        rec(root, root, &mut out)?;
    }
    Ok(out)
}

/// How one path differs between the reference and crozier's tree.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Difference {
    /// The reference has the file; crozier did not emit it.
    OnlyInReference,
    /// crozier emitted the file; the reference has none.
    OnlyInCrozier,
    /// Both are text and differ after normalization; the unified diff
    /// (`-` reference, `+` crozier) when it was asked for.
    Text(Option<String>),
    /// At least one side is not UTF-8 and the raw bytes differ.
    Binary {
        /// The reference file's length in bytes.
        reference: usize,
        /// crozier's file's length in bytes.
        crozier: usize,
    },
    /// The pair could not be read or normalized.
    Processing(String),
}

/// Compare the whole `reference_root` tree with the whole `crozier_root` tree
/// under the per-file rules, returning every differing path (sorted) with how it
/// differs. An empty result is a match. `file_filter` keeps only paths containing
/// it; `include_text_diffs` attaches each text difference's unified diff.
///
/// # Errors
///
/// When either walk fails (a symbolic link, an unreadable directory), or when
/// the reference holds no files and no filter was given — an empty reference
/// never counts as a match.
pub fn tree_differences(
    reference_root: &Path,
    crozier_root: &Path,
    file_filter: Option<&str>,
    include_text_diffs: bool,
) -> Result<Vec<(String, Difference)>, String> {
    let reference_files: BTreeSet<String> = walk_files(reference_root)?.into_iter().collect();
    if reference_files.is_empty() && file_filter.is_none() {
        return Err(format!(
            "no reference files under {} — the tree walk is broken",
            reference_root.display()
        ));
    }
    let crozier_files: BTreeSet<String> = walk_files(crozier_root)?.into_iter().collect();
    let paths: BTreeSet<&String> = reference_files.union(&crozier_files).collect();
    let mut differences = Vec::new();

    for rel in paths {
        if file_filter.is_some_and(|filter| !rel.contains(filter)) {
            continue;
        }
        let difference = match (reference_files.contains(rel), crozier_files.contains(rel)) {
            (true, false) => Some(Difference::OnlyInReference),
            (false, true) => Some(Difference::OnlyInCrozier),
            _ => file_difference(
                rel,
                &reference_root.join(rel),
                &crozier_root.join(rel),
                include_text_diffs,
            ),
        };
        if let Some(difference) = difference {
            differences.push((rel.clone(), difference));
        }
    }
    Ok(differences)
}

/// How the file present on both sides at `rel` differs, if at all.
fn file_difference(
    rel: &str,
    reference_path: &Path,
    crozier_path: &Path,
    include_text_diffs: bool,
) -> Option<Difference> {
    let reference = match std::fs::read(reference_path) {
        Ok(content) => content,
        Err(error) => {
            return Some(Difference::Processing(format!(
                "could not read the reference file: {error}"
            )))
        }
    };
    let crozier = match std::fs::read(crozier_path) {
        Ok(content) => content,
        Err(error) => {
            return Some(Difference::Processing(format!(
                "could not read crozier's file: {error}"
            )))
        }
    };
    if reference == crozier {
        return None;
    }
    let (Ok(reference_text), Ok(crozier_text)) = (
        std::str::from_utf8(&reference),
        std::str::from_utf8(&crozier),
    ) else {
        return Some(Difference::Binary {
            reference: reference.len(),
            crozier: crozier.len(),
        });
    };
    match normalized_pair(rel, crozier_text, reference_text) {
        Ok((crozier, reference)) if crozier == reference => None,
        Ok((crozier, reference)) => {
            Some(Difference::Text(include_text_diffs.then(|| {
                unified_diff(&reference, &crozier).unwrap_or_default()
            })))
        }
        Err(error) => Some(Difference::Processing(error)),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn write(root: &Path, rel: &str, content: &[u8]) {
        let path = root.join(rel);
        std::fs::create_dir_all(path.parent().unwrap()).unwrap();
        std::fs::write(path, content).unwrap();
    }

    #[test]
    fn sdk_identity_headers_are_dropped_and_the_prefix_canonicalized() {
        let crozier = "h = {\n    \"X-Crozier-Language\": \"Python\",\n    \"X-Crozier-SDK-Name\": \"x\",\n    \"X-Crozier-SDK-Version\": \"1\",\n}\n";
        let reference = "h = {\n    \"X-Fern-Language\": \"Python\",\n}\n";
        assert_eq!(normalize_sdk_headers(crozier), reference);
        assert_eq!(normalize_sdk_headers(reference), reference);
        // The reference's own identity lines go too.
        assert_eq!(
            normalize_sdk_headers(
                "\"X-Fern-SDK-Name\": \"a\",\n\"X-Fern-SDK-Version\": \"b\",\nkeep\n"
            ),
            "keep\n"
        );
    }

    #[test]
    fn metadata_drops_only_the_generator_config_block() {
        let with = "{\n  \"cliVersion\": \"5.67.1\",\n  \"generatorConfig\": {\n    \"pydantic_config\": {\n      \"enum_type\": \"python_enums\"\n    }\n  }\n}";
        assert_eq!(
            normalize_metadata(with),
            "{\n  \"cliVersion\": \"5.67.1\"\n}"
        );
        let without = "{\n  \"cliVersion\": \"5.67.1\"\n}";
        assert_eq!(normalize_metadata(without), without);
    }

    #[test]
    fn init_drops_leading_blank_lines_and_sorts_imports() {
        let out = normalize_init("\n\nimport typing\nimport enum\n").unwrap();
        assert_eq!(out, "import enum\nimport typing\n");
        // ruff refusing the input surfaces as an error, never as wrong text.
        let error = normalize_init("def (:\n").unwrap_err();
        assert!(error.contains("ruff isort failed"), "{error}");
    }

    #[test]
    fn normalized_pair_applies_each_per_path_rule_to_both_sides() {
        // `.py`: comments stripped on both sides.
        let (c, r) =
            normalized_pair("a/b.py", "x = 1  # crozier\n", "x = 1  # reference\n").unwrap();
        assert_eq!((c.as_str(), r.as_str()), ("x = 1\n", "x = 1\n"));
        // `__init__.py`: strip, then leading blanks and import order.
        let (c, r) = normalized_pair(
            "pkg/__init__.py",
            "# header\nimport b\nimport a\n",
            "# other header\n\nimport a\nimport b\n",
        )
        .unwrap();
        assert_eq!(c, r);
        // metadata: `generatorConfig` dropped.
        let (c, r) = normalized_pair(
            ".fern/metadata.json",
            "{\n  \"a\": 1\n}",
            "{\n  \"a\": 1,\n  \"generatorConfig\": {}\n}",
        )
        .unwrap();
        assert_eq!(c, r);
        // Any other `…metadata.json` is SDK content: its `generatorConfig`
        // is compared as written, at the root or nested.
        let theirs = "{\n  \"a\": 1,\n  \"generatorConfig\": {\"x\": 1}\n}";
        let ours = "{\n  \"a\": 1,\n  \"generatorConfig\": {\"x\": 2}\n}";
        assert!(files_match(".fern/metadata.json", ours, theirs).unwrap());
        for rel in [
            "types/user_metadata.json",
            "foo/metadata.json",
            "metadata.json",
            "foo/.fern/metadata.json",
        ] {
            assert!(!files_match(rel, ours, theirs).unwrap(), "{rel}");
        }
        // Anything else: headers only, comments kept.
        let (c, r) = normalized_pair("README.md", "# Title\n", "# Other\n").unwrap();
        assert_ne!(c, r);
        assert!(files_match("README.md", "same\n", "same\n").unwrap());
        assert!(!files_match("a.py", "x = 1\n", "x = 2\n").unwrap());
    }

    #[test]
    fn unified_diff_reports_only_real_changes() {
        assert_eq!(unified_diff("a\nb\nc", "a\nb\nc"), None);
        let d = unified_diff("a\nb\nc", "a\nB\nc").expect("differs");
        assert!(d.contains("- b") && d.contains("+ B"), "{d}");
        assert!(d.contains("  a") && d.contains("  c"), "{d}");
        // Trailing additions and removals both surface.
        let d = unified_diff("a", "a\nb").unwrap();
        assert!(d.contains("+ b"), "{d}");
        let d = unified_diff("a\nb", "a").unwrap();
        assert!(d.contains("- b"), "{d}");

        let big = (0..40).map(|n| n.to_string()).collect::<Vec<_>>();
        let mut changed = big.clone();
        changed[0] = "first".into();
        changed[39] = "last".into();
        let d = unified_diff(&big.join("\n"), &changed.join("\n")).unwrap();
        assert!(d.contains("unchanged line(s)"), "{d}");
        assert!(!d.contains("\n  20\n"), "{d}");
        let mut head_only = big.clone();
        head_only[0] = "first".into();
        let d = unified_diff(&big.join("\n"), &head_only.join("\n")).unwrap();
        assert!(d.ends_with("unchanged line(s))\n"), "{d}");
    }

    #[test]
    fn tree_differences_is_bidirectional_and_skips_provenance() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        let (r, c) = (reference.path(), crozier.path());
        write(r, "same.py", b"x = 1  # a\n");
        write(c, "same.py", b"x = 1  # b\n");
        write(r, "changed.txt", b"reference\n");
        write(c, "changed.txt", b"crozier\n");
        write(r, "dir/only-reference.txt", b"r\n");
        write(c, "only-crozier.txt", b"c\n");
        write(r, "bin.dat", &[0xff, 0x00]);
        write(c, "bin.dat", &[0xfe]);
        write(r, "identical.bin", &[0xff]);
        write(c, "identical.bin", &[0xff]);
        write(r, PROVENANCE_FILE, b"{}");

        let found = tree_differences(r, c, None, true).unwrap();
        let paths: Vec<&str> = found.iter().map(|(p, _)| p.as_str()).collect();
        assert_eq!(
            paths,
            [
                "bin.dat",
                "changed.txt",
                "dir/only-reference.txt",
                "only-crozier.txt"
            ]
        );
        assert_eq!(
            found[0].1,
            Difference::Binary {
                reference: 2,
                crozier: 1
            }
        );
        let Difference::Text(Some(diff)) = &found[1].1 else {
            panic!("{found:?}");
        };
        assert!(diff.contains("- reference") && diff.contains("+ crozier"));
        assert_eq!(found[2].1, Difference::OnlyInReference);
        assert_eq!(found[3].1, Difference::OnlyInCrozier);

        let summary = tree_differences(r, c, Some("changed"), false).unwrap();
        assert_eq!(
            summary,
            [("changed.txt".to_string(), Difference::Text(None))]
        );
    }

    #[test]
    fn tree_differences_reports_an_unnormalizable_pair() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        write(reference.path(), "__init__.py", b"def (:\n");
        write(crozier.path(), "__init__.py", b"x = 1\n");
        let found = tree_differences(reference.path(), crozier.path(), None, true).unwrap();
        assert!(
            matches!(&found[0].1, Difference::Processing(e) if e.contains("ruff")),
            "{found:?}"
        );
    }

    #[test]
    fn an_empty_reference_is_never_a_match() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        let error = tree_differences(reference.path(), crozier.path(), None, true).unwrap_err();
        assert!(error.contains("no reference files"), "{error}");
        // A missing root walks as empty.
        assert!(walk_files(&reference.path().join("absent"))
            .unwrap()
            .is_empty());
    }

    #[cfg(unix)]
    #[test]
    fn symbolic_links_are_refused_not_followed() {
        use std::os::unix::fs::symlink;
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        let outside = tempfile::NamedTempFile::new().unwrap();
        symlink(outside.path(), reference.path().join("link")).unwrap();
        let error = tree_differences(reference.path(), crozier.path(), None, true).unwrap_err();
        assert!(
            error.contains("refusing to follow symbolic link"),
            "{error}"
        );

        let root_link = reference.path().join("root-link");
        symlink(crozier.path(), &root_link).unwrap();
        let error = walk_files(&root_link).unwrap_err();
        assert!(
            error.contains("refusing to follow symbolic link"),
            "{error}"
        );
    }

    #[cfg(unix)]
    #[test]
    fn an_unreadable_file_is_a_processing_difference() {
        use std::os::unix::fs::PermissionsExt;
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        write(reference.path(), "a.txt", b"a\n");
        write(crozier.path(), "a.txt", b"a\n");
        let locked = crozier.path().join("a.txt");
        std::fs::set_permissions(&locked, std::fs::Permissions::from_mode(0o000)).unwrap();
        let found = tree_differences(reference.path(), crozier.path(), None, true).unwrap();
        std::fs::set_permissions(&locked, std::fs::Permissions::from_mode(0o644)).unwrap();
        // Root can read anything; only assert when the permission bit held.
        if let Some((_, difference)) = found.first() {
            assert!(
                matches!(difference, Difference::Processing(e) if e.contains("crozier's file")),
                "{found:?}"
            );
        }
        std::fs::set_permissions(
            reference.path().join("a.txt"),
            std::fs::Permissions::from_mode(0o000),
        )
        .unwrap();
        let found = tree_differences(reference.path(), crozier.path(), None, true).unwrap();
        if let Some((_, difference)) = found.first() {
            assert!(
                matches!(difference, Difference::Processing(e) if e.contains("reference file")),
                "{found:?}"
            );
        }
    }

    /// A committed golden is already comment-stripped and a live reference is
    /// not; [`normalized_pair`] strips both. That is safe for the corpus only
    /// because stripping a stripped golden changes nothing, which this pins over
    /// every committed golden and probe-measurement tree.
    #[test]
    fn stripping_a_committed_golden_again_is_a_no_op() {
        let root = Path::new(env!("CARGO_MANIFEST_DIR"));
        let mut trees = Vec::new();
        for fixture in std::fs::read_dir(root.join("tests/fixtures")).unwrap() {
            let fixture = fixture.unwrap().path();
            for golden in ["expected", "expected-flat"] {
                if fixture.join(golden).is_dir() {
                    trees.push(fixture.join(golden));
                }
            }
        }
        trees.push(root.join("docs/openapi-surface/probe-expected"));
        let mut checked = 0usize;
        let mut changed = Vec::new();
        for tree in &trees {
            for rel in walk_files(tree).unwrap() {
                if !rel.ends_with(".py") {
                    continue;
                }
                let text = std::fs::read_to_string(tree.join(&rel)).unwrap();
                if strip_python_comments(&text) != text {
                    changed.push(tree.join(&rel).display().to_string());
                }
                checked += 1;
            }
        }
        assert!(checked > 1000, "only {checked} golden modules found");
        assert!(changed.is_empty(), "stripping changed: {changed:?}");
    }
}
