//! The comparison engine: how crozier's output tree is compared with a
//! **reference** tree that has the shape of Fern's Python SDK output.
//!
//! crozier's contract is that its output equals the reference once the
//! comparison's mechanics have run and the departures in
//! [`crate::departures`]' catalog are applied — here, and nowhere else.
//! `crozier compare` and every golden comparison in crozier's own test suite
//! call this engine with that one catalog, so "matches" has one definition.
//!
//! A file present on both sides ([`compare_file`]) is compared in four steps:
//!
//! 1. **Mechanics** that keep every line where it is: a `.py` file's Python
//!    comments are stripped ([`crate::strip_python_comments`]), leaving a
//!    comment-only line blank. Comments are outside the compared output — the
//!    committed goldens hold none — so this records no departure.
//! 2. **A region rule**: a catalog rule that recognises a whole construct (the
//!    `generatorConfig` block of `.fern/metadata.json`, an `__init__.py`'s
//!    `TYPE_CHECKING` imports in another order) replaces crozier's region with
//!    Fern's. The region rules read disjoint paths, so at most one applies.
//! 3. **Line rules**: the two sides' lines are aligned (a longest common
//!    subsequence), and inside each run of differing lines a catalog rule may
//!    pair one Fern line with the crozier line aligned to it, or account for a
//!    line only crozier writes. Each line it accounts for is replaced with
//!    Fern's.
//! 4. **The verdict**: crozier's text with every applied departure replaced is
//!    compared with the reference's, an `__init__.py` without its leading blank
//!    lines on both sides (the lines its differing header comments leave). Any
//!    difference no rule explained remains, so the file fails — even on a line
//!    or in a file where a departure applied.
//!
//! Every departure applied is reported by catalog id, file and crozier's
//! 1-based line: the first line of crozier's replacement, or, where crozier
//! writes no line, the line before which Fern's stand.
//!
//! The tree rules ([`compare_trees`]): the comparison is bidirectional (a file
//! on only one side is a difference), a symbolic link on either side is refused
//! rather than followed, and the `.crozier-fern-golden.json` provenance record a
//! committed golden carries is not part of either tree. A rule that reads the
//! trees (which classes each defines) sees them whole.
//!
//! A committed golden is already comment-stripped; a live reference is not. The
//! comment strip is idempotent over every committed golden (pinned by this
//! module's tests), so stripping both sides serves both inputs with one rule.

use std::collections::BTreeSet;
use std::path::Path;

use crate::departures::{self, Context, Pair};
use crate::strip_python_comments;

pub use crate::departures::FERN_METADATA;

/// The provenance record a committed golden tree carries beside the reference
/// output. It is not reference output, so neither side's walk includes it.
pub const PROVENANCE_FILE: &str = ".crozier-fern-golden.json";

/// One departure the engine applied in a file: crozier's 1-based line and the
/// catalog id.
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub struct FileDeparture {
    /// crozier's line where the departure starts.
    pub line: usize,
    /// The catalog entry's id.
    pub id: &'static str,
}

/// How one file pair compared.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct FileComparison {
    /// Every departure applied, in line order.
    pub departures: Vec<FileDeparture>,
    /// `None` when the pair matches; otherwise the `(reference, crozier)` texts
    /// the verdict compared, with every departure applied.
    pub residual: Option<(String, String)>,
}

impl FileComparison {
    /// Whether the pair matches once its departures are applied.
    #[must_use]
    pub fn matches(&self) -> bool {
        self.residual.is_none()
    }

    /// The unified diff of what still differs (`-` reference, `+` crozier), or
    /// `None` when the pair matches.
    #[must_use]
    pub fn diff(&self) -> Option<String> {
        self.residual
            .as_ref()
            .and_then(|(reference, crozier)| unified_diff(reference, crozier))
    }
}

/// `text` after the line-preserving mechanics for `rel`: a `.py` file's
/// comments stripped.
fn mechanics(rel: &str, text: &str) -> String {
    if rel.ends_with(".py") {
        strip_python_comments(text)
    } else {
        text.to_string()
    }
}

/// `text` as the verdict compares it: an `__init__.py` without its leading
/// blank lines, which are where its header comments stood.
fn verdict_text<'t>(rel: &str, text: &'t str) -> &'t str {
    if rel != "__init__.py" && !rel.ends_with("/__init__.py") {
        return text;
    }
    let mut rest = text;
    while let Some((line, after)) = rest.split_once('\n') {
        if !line.trim().is_empty() {
            break;
        }
        rest = after;
    }
    rest
}

/// Compare crozier's file `rel` with the reference's under the steps in the
/// module docs, with `context` describing the trees they belong to.
///
/// # Errors
///
/// When a rule cannot be applied: `ruff` cannot be run, or rejects the input.
pub fn compare_file(
    context: &Context,
    rel: &str,
    crozier: &str,
    reference: &str,
) -> Result<FileComparison, String> {
    let (crozier, reference) = (mechanics(rel, crozier), mechanics(rel, reference));
    if verdict_text(rel, &crozier) == verdict_text(rel, &reference) {
        return Ok(FileComparison {
            departures: Vec::new(),
            residual: None,
        });
    }
    let fern: Vec<&str> = reference.split('\n').collect();
    let original: Vec<&str> = crozier.split('\n').collect();
    let pair = Pair {
        rel,
        fern: &fern,
        crozier: &original,
        context,
    };
    let mut departures = Vec::new();

    // crozier's lines, with the region a region rule accounts for replaced by
    // Fern's; every other line keeps its original index.
    let mut lines: Vec<(&str, Option<usize>)> = original
        .iter()
        .enumerate()
        .map(|(j, line)| (*line, Some(j)))
        .collect();
    for (id, rule) in rules_of(|rule| rule.region) {
        if let Some(region) = rule(&pair)? {
            lines.splice(
                region.crozier.clone(),
                region.fern.clone().map(|i| (fern[i], None)),
            );
            departures.push(FileDeparture {
                line: region.crozier.start + 1,
                id,
            });
            break;
        }
    }

    // Line rules, inside each run of lines the alignment leaves unpaired.
    let line_rules = rules_of(|rule| rule.line);
    let added_rules = rules_of(|rule| rule.added);
    let current: Vec<&str> = lines.iter().map(|(line, _)| *line).collect();
    let line_rule = |i: usize, j: usize| -> Option<(&'static str, usize)> {
        let origin = lines[j].1?;
        line_rules
            .iter()
            .find(|(_, holds)| holds(&pair, fern[i], current[j]))
            .map(|(id, _)| (*id, origin))
    };
    let added_rule = |j: usize| -> Option<(&'static str, usize)> {
        let origin = lines[j].1?;
        added_rules
            .iter()
            .find(|(_, holds)| holds(&pair, current[j]))
            .map(|(id, _)| (*id, origin))
    };
    let mut result: Vec<&str> = Vec::with_capacity(current.len());
    let ops = align(fern.len(), current.len(), |i, j| fern[i] == current[j]);
    let mut index = 0;
    while index < ops.len() {
        if let Op::Equal(_, j) = ops[index] {
            result.push(current[j]);
            index += 1;
            continue;
        }
        let (mut removed, mut added) = (Vec::new(), Vec::new());
        while let Some(op) = ops.get(index) {
            match *op {
                Op::Delete(i) => removed.push(i),
                Op::Insert(j) => added.push(j),
                Op::Equal(..) => break,
            }
            index += 1;
        }
        let inner = align(removed.len(), added.len(), |a, b| {
            line_rule(removed[a], added[b]).is_some()
        });
        for op in inner {
            let (claimed, kept) = match op {
                Op::Equal(a, b) => (line_rule(removed[a], added[b]), Some(fern[removed[a]])),
                Op::Delete(_) => (None, None),
                Op::Insert(b) => match added_rule(added[b]) {
                    Some(claimed) => (Some(claimed), None),
                    None => (None, Some(current[added[b]])),
                },
            };
            if let Some((id, origin)) = claimed {
                departures.push(FileDeparture {
                    line: origin + 1,
                    id,
                });
            }
            result.extend(kept);
        }
    }
    departures.sort();
    let applied = result.join("\n");
    let (reference, applied) = (verdict_text(rel, &reference), verdict_text(rel, &applied));
    Ok(FileComparison {
        departures,
        residual: (reference != applied).then(|| (reference.to_string(), applied.to_string())),
    })
}

/// The catalog's rules of one shape, each with its id, in catalog order.
fn rules_of<F>(shape: impl Fn(departures::Rule) -> Option<F>) -> Vec<(&'static str, F)> {
    departures::RULE_IDS
        .iter()
        .filter(|id| departures::find(id).is_some())
        .filter_map(|id| shape(departures::rule(id)?).map(|found| (*id, found)))
        .collect()
}

/// One step of an alignment of two sequences.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Op {
    /// The left item `.0` pairs with the right item `.1`.
    Equal(usize, usize),
    /// The left item is unpaired.
    Delete(usize),
    /// The right item is unpaired.
    Insert(usize),
}

/// A longest-common-subsequence alignment of a left sequence of `n` items with
/// a right one of `m`, where `pairs(i, j)` says whether left `i` may pair with
/// right `j`. Common leading and trailing runs are paired first, so only the
/// middle pays the quadratic table.
fn align(n: usize, m: usize, pairs: impl Fn(usize, usize) -> bool) -> Vec<Op> {
    let mut prefix = 0;
    while prefix < n && prefix < m && pairs(prefix, prefix) {
        prefix += 1;
    }
    let mut suffix = 0;
    while suffix < n - prefix && suffix < m - prefix && pairs(n - 1 - suffix, m - 1 - suffix) {
        suffix += 1;
    }
    let (rows, cols) = (n - prefix - suffix, m - prefix - suffix);
    let mut ops: Vec<Op> = (0..prefix).map(|k| Op::Equal(k, k)).collect();

    // Longest-common-subsequence lengths, filled from the bottom-right.
    let mut lcs = vec![vec![0u32; cols + 1]; rows + 1];
    for i in (0..rows).rev() {
        for j in (0..cols).rev() {
            lcs[i][j] = if pairs(prefix + i, prefix + j) {
                lcs[i + 1][j + 1] + 1
            } else {
                lcs[i + 1][j].max(lcs[i][j + 1])
            };
        }
    }
    let (mut i, mut j) = (0usize, 0usize);
    while i < rows && j < cols {
        if lcs[i][j] == lcs[i + 1][j + 1] + 1 && pairs(prefix + i, prefix + j) {
            ops.push(Op::Equal(prefix + i, prefix + j));
            i += 1;
            j += 1;
        } else if lcs[i + 1][j] >= lcs[i][j + 1] {
            ops.push(Op::Delete(prefix + i));
            i += 1;
        } else {
            ops.push(Op::Insert(prefix + j));
            j += 1;
        }
    }
    ops.extend((i..rows).map(|i| Op::Delete(prefix + i)));
    ops.extend((j..cols).map(|j| Op::Insert(prefix + j)));
    ops.extend((0..suffix).map(|k| Op::Equal(n - suffix + k, m - suffix + k)));
    ops
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
    let ops: Vec<(char, &str)> = align(a.len(), b.len(), |i, j| a[i] == b[j])
        .into_iter()
        .map(|op| match op {
            Op::Equal(i, _) => (' ', a[i]),
            Op::Delete(i) => ('-', a[i]),
            Op::Insert(j) => ('+', b[j]),
        })
        .collect();

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
    /// Both are text and differ once the departures are applied; the unified
    /// diff (`-` reference, `+` crozier) when it was asked for.
    Text(Option<String>),
    /// At least one side is not UTF-8 and the raw bytes differ.
    Binary {
        /// The reference file's length in bytes.
        reference: usize,
        /// crozier's file's length in bytes.
        crozier: usize,
    },
    /// The pair could not be read or compared.
    Processing(String),
}

/// One departure applied in a tree comparison.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
pub struct AppliedDeparture {
    /// The file's `/`-separated path relative to the tree root.
    pub file: String,
    /// crozier's 1-based line where it starts.
    pub line: usize,
    /// The catalog entry's id.
    pub id: String,
}

/// The comparison of two whole trees.
#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct TreeComparison {
    /// Every differing path (sorted) with how it differs. Empty is a match.
    pub differences: Vec<(String, Difference)>,
    /// Every departure applied, sorted by file, line and id — in files that
    /// still differ too.
    pub departures: Vec<AppliedDeparture>,
}

/// Compare the whole `reference_root` tree with the whole `crozier_root` tree
/// under the engine, returning every differing path with how it differs and
/// every departure applied. `file_filter` keeps only paths containing it;
/// `include_text_diffs` attaches each text difference's unified diff.
///
/// # Errors
///
/// When either walk fails (a symbolic link, an unreadable directory), or when
/// the reference holds no files and no filter was given — an empty reference
/// never counts as a match.
pub fn compare_trees(
    reference_root: &Path,
    crozier_root: &Path,
    file_filter: Option<&str>,
    include_text_diffs: bool,
) -> Result<TreeComparison, String> {
    let reference_files: BTreeSet<String> = walk_files(reference_root)?.into_iter().collect();
    if reference_files.is_empty() && file_filter.is_none() {
        return Err(format!(
            "no reference files under {} — the tree walk is broken",
            reference_root.display()
        ));
    }
    let crozier_files: BTreeSet<String> = walk_files(crozier_root)?.into_iter().collect();
    let context = Context::from_trees(reference_root, crozier_root);
    let paths: BTreeSet<&String> = reference_files.union(&crozier_files).collect();
    let mut comparison = TreeComparison::default();

    for rel in paths {
        if file_filter.is_some_and(|filter| !rel.contains(filter)) {
            continue;
        }
        let difference = match (reference_files.contains(rel), crozier_files.contains(rel)) {
            (true, false) => Some(Difference::OnlyInReference),
            (false, true) => Some(Difference::OnlyInCrozier),
            _ => {
                let (difference, departures) = file_difference(
                    &context,
                    rel,
                    &reference_root.join(rel),
                    &crozier_root.join(rel),
                    include_text_diffs,
                );
                comparison
                    .departures
                    .extend(departures.into_iter().map(|departure| AppliedDeparture {
                        file: rel.clone(),
                        line: departure.line,
                        id: departure.id.to_string(),
                    }));
                difference
            }
        };
        if let Some(difference) = difference {
            comparison.differences.push((rel.clone(), difference));
        }
    }
    Ok(comparison)
}

/// How the file present on both sides at `rel` differs, if at all, and the
/// departures applied in it.
fn file_difference(
    context: &Context,
    rel: &str,
    reference_path: &Path,
    crozier_path: &Path,
    include_text_diffs: bool,
) -> (Option<Difference>, Vec<FileDeparture>) {
    let processing = |message: String| (Some(Difference::Processing(message)), Vec::new());
    let reference = match std::fs::read(reference_path) {
        Ok(content) => content,
        Err(error) => return processing(format!("could not read the reference file: {error}")),
    };
    let crozier = match std::fs::read(crozier_path) {
        Ok(content) => content,
        Err(error) => return processing(format!("could not read crozier's file: {error}")),
    };
    if reference == crozier {
        return (None, Vec::new());
    }
    let (Ok(reference_text), Ok(crozier_text)) = (
        std::str::from_utf8(&reference),
        std::str::from_utf8(&crozier),
    ) else {
        return (
            Some(Difference::Binary {
                reference: reference.len(),
                crozier: crozier.len(),
            }),
            Vec::new(),
        );
    };
    match compare_file(context, rel, crozier_text, reference_text) {
        Ok(compared) => {
            let difference = (!compared.matches()).then(|| {
                Difference::Text(include_text_diffs.then(|| compared.diff().unwrap_or_default()))
            });
            (difference, compared.departures)
        }
        Err(error) => processing(error),
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

    fn compare(rel: &str, crozier: &str, reference: &str) -> FileComparison {
        compare_file(&Context::default(), rel, crozier, reference).unwrap()
    }

    fn ids(compared: &FileComparison) -> Vec<(usize, &'static str)> {
        compared
            .departures
            .iter()
            .map(|departure| (departure.line, departure.id))
            .collect()
    }

    const WRAPPER: &str = "src/acme/core/client_wrapper.py";

    #[test]
    fn identity_headers_are_departures_line_by_line() {
        let crozier = concat!(
            "# crozier\nh = {\n    \"X-Crozier-Language\": \"Python\",\n    ",
            "\"X-Crozier-SDK-Name\": \"x\",\n    \"X-Crozier-SDK-Version\": \"0.0.0\",\n}\n"
        );
        let reference = concat!(
            "\nh = {\n    \"X-Fern-Language\": \"Python\",\n    ",
            "\"X-Fern-SDK-Name\": \"x\",\n    \"X-Fern-SDK-Version\": \"0.0.0\",\n}\n"
        );
        // crozier's tree names its project `x`, which its SDK-Name line carries.
        let context = Context::from_sources([], [("pyproject.toml", "name = \"x\"\n")]);
        let compare = |rel: &str, crozier: &str, reference: &str| {
            compare_file(&context, rel, crozier, reference).unwrap()
        };
        let compared = compare(WRAPPER, crozier, reference);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(
            ids(&compared),
            [
                (3, "sdk-identity-header-prefix"),
                (4, "sdk-identity-header-prefix"),
                (5, "sdk-identity-header-prefix"),
            ]
        );
        // A reference with no SDK pair, or another published version: the pair
        // is crozier's packaging.
        let unpackaged = "\nh = {\n    \"X-Fern-Language\": \"Python\",\n}\n";
        let compared = compare(WRAPPER, crozier, unpackaged);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(
            ids(&compared),
            [
                (3, "sdk-identity-header-prefix"),
                (4, "sdk-name-version-headers"),
                (5, "sdk-name-version-headers"),
            ]
        );
        let released = reference.replace("\"0.0.0\"", "\"2.3.1\"");
        let compared = compare(WRAPPER, crozier, &released);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(
            ids(&compared),
            [
                (3, "sdk-identity-header-prefix"),
                (4, "sdk-identity-header-prefix"),
                (5, "sdk-name-version-headers"),
            ]
        );
        // A crozier version other than its fixed one is no departure: the line
        // fails, naming it.
        let wrong = crozier.replace("\"0.0.0\"", "\"9.9.9\"");
        let compared = compare(WRAPPER, &wrong, &released);
        assert!(!compared.matches());
        assert!(
            compared
                .diff()
                .unwrap()
                .contains("+     \"X-Crozier-SDK-Version\": \"9.9.9\","),
            "{:?}",
            compared.diff()
        );
        assert!(!compare(WRAPPER, &wrong, unpackaged).matches());
    }

    #[test]
    fn a_difference_no_rule_explains_still_fails_beside_a_departure() {
        let crozier = "h = {\n    \"X-Crozier-Language\": \"Python\",\n}\nx = 1\n";
        // On the same line as the departure.
        let same_line = "h = {\n    \"X-Fern-Language\": \"Pythn\",\n}\nx = 1\n";
        let compared = compare(WRAPPER, crozier, same_line);
        assert!(!compared.matches());
        assert!(compared.departures.is_empty());
        let diff = compared.diff().unwrap();
        assert!(
            diff.contains("-     \"X-Fern-Language\": \"Pythn\","),
            "{diff}"
        );
        // Elsewhere in the same file: the departure applies, the rest fails.
        let elsewhere = "h = {\n    \"X-Fern-Language\": \"Python\",\n}\nx = 2\n";
        let compared = compare(WRAPPER, crozier, elsewhere);
        assert!(!compared.matches());
        assert_eq!(ids(&compared), [(2, "sdk-identity-header-prefix")]);
        let diff = compared.diff().unwrap();
        assert!(
            diff.contains("- x = 2") && diff.contains("+ x = 1"),
            "{diff}"
        );
        assert!(!diff.contains("X-Crozier"), "{diff}");
        // The header rule holds only in the client wrapper.
        let compared = compare(
            "src/acme/client.py",
            crozier,
            &crozier.replace("X-Crozier-", "X-Fern-"),
        );
        assert!(!compared.matches() && compared.departures.is_empty());
    }

    #[test]
    fn comments_and_init_leading_blank_lines_are_mechanics_not_departures() {
        let compared = compare("a/b.py", "x = 1  # crozier\n", "x = 1  # reference\n");
        assert!(compared.matches() && compared.departures.is_empty());
        let compared = compare(
            "pkg/__init__.py",
            "# header\nimport a\n",
            "# other header\n\n# isort: skip_file\n\nimport a\n",
        );
        assert!(compared.matches() && compared.departures.is_empty());
        // Only `__init__.py` drops them, and only leading ones.
        assert!(!compare("pkg/client.py", "# h\nimport a\n", "\n\nimport a\n").matches());
        assert!(!compare("__init__.py", "import a\n\nx\n", "import a\nx\n").matches());
        assert!(compare("__init__.py", "\n", "").matches());
        // Other files are compared as written, comments included.
        assert!(!compare("README.md", "# Title\n", "# Other\n").matches());
    }

    #[test]
    fn init_import_order_is_one_departure_at_crozier_s_first_moved_line() {
        let crozier = concat!(
            "# crozier\nimport typing\n\nif typing.TYPE_CHECKING:\n    from .a import A\n    ",
            "from .b import B\n    from .c import C\n_dynamic_imports = {}\n"
        );
        let reference = concat!(
            "\n\n\nimport typing\n\nif typing.TYPE_CHECKING:\n    from .b import B\n    ",
            "from .a import A\n    from .c import C\n_dynamic_imports = {}\n"
        );
        let compared = compare("src/acme/__init__.py", crozier, reference);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(ids(&compared), [(5, "init-type-checking-import-order")]);
        // Another difference outside the block still fails.
        let other = reference.replace("_dynamic_imports = {}", "_dynamic_imports = {1: 2}");
        let compared = compare("src/acme/__init__.py", crozier, &other);
        assert!(!compared.matches());
        // A block importing something else is no reordering.
        let other = reference.replace("from .c import C", "from .c import D");
        let compared = compare("src/acme/__init__.py", crozier, &other);
        assert!(!compared.matches() && compared.departures.is_empty());
    }

    #[test]
    fn metadata_generator_config_is_one_departure_on_that_path_only() {
        let crozier = crate::emit::FERN_METADATA_RECORD;
        let reference = crozier.replace("python_enums", "literals");
        let compared = compare(FERN_METADATA, crozier, &reference);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(ids(&compared), [(7, "fern-metadata-generator-config")]);
        let start = crozier.find("  \"generatorConfig\"").unwrap();
        let end = crozier.find("  \"invokedBy\"").unwrap();
        let absent = format!("{}{}", &crozier[..start], &crozier[end..]);
        let compared = compare(FERN_METADATA, crozier, &absent);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(ids(&compared), [(5, "fern-metadata-generator-config")]);
        // crozier's own member changed is no departure: the file fails.
        let wrong = crozier.replace("python_enums", "literals");
        let compared = compare(FERN_METADATA, &wrong, &absent);
        assert!(!compared.matches() && compared.departures.is_empty());
        // Any other `…metadata.json` is SDK content, compared as written.
        for rel in [
            "types/user_metadata.json",
            "foo/metadata.json",
            "metadata.json",
            "foo/.fern/metadata.json",
        ] {
            let compared = compare(rel, crozier, &reference);
            assert!(
                !compared.matches() && compared.departures.is_empty(),
                "{rel}"
            );
        }
    }

    #[test]
    fn readme_casing_needs_the_trees_classes() {
        let crozier = "# Acme\n\nfrom LanternHarbor import AsyncLanternHarborApi\n";
        let reference = "# Acme\n\nfrom LanternHarbor import AsyncLanternharborApi\n";
        // Compared alone, nothing says which class the code defines.
        assert!(!compare("README.md", crozier, reference).matches());
        let context = Context::from_sources(
            [("client.py", "class AsyncLanternHarborApi:\n")],
            [("client.py", "class AsyncLanternHarborApi:\n")],
        );
        let compared = compare_file(&context, "README.md", crozier, reference).unwrap();
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(ids(&compared), [(3, "readme-client-class-casing")]);
    }

    #[test]
    fn a_rule_that_cannot_run_is_an_error() {
        let error = compare_file(
            &Context::default(),
            "__init__.py",
            "if typing.TYPE_CHECKING:\n    def (:\n    import b\nx\n",
            "if typing.TYPE_CHECKING:\n    import b\n    def (:\nx\n",
        )
        .unwrap_err();
        assert!(error.contains("ruff isort failed"), "{error}");
    }

    #[test]
    fn alignment_pairs_the_longest_common_run() {
        let a = ["a", "b", "c", "d"];
        let b = ["a", "x", "c", "d", "e"];
        let ops = align(a.len(), b.len(), |i, j| a[i] == b[j]);
        assert_eq!(
            ops,
            [
                Op::Equal(0, 0),
                Op::Delete(1),
                Op::Insert(1),
                Op::Equal(2, 2),
                Op::Equal(3, 3),
                Op::Insert(4),
            ]
        );
        assert_eq!(align(0, 1, |_, _| true), [Op::Insert(0)]);
        assert_eq!(align(1, 0, |_, _| true), [Op::Delete(0)]);
        let (a, b) = (["x", "a", "y"], ["a", "x"]);
        assert_eq!(
            align(a.len(), b.len(), |i, j| a[i] == b[j]),
            [Op::Delete(0), Op::Equal(1, 0), Op::Delete(2), Op::Insert(1)]
        );
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
    fn compare_trees_is_bidirectional_skips_provenance_and_reports_departures() {
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
        write(
            r,
            "core/client_wrapper.py",
            b"h = {\n    \"X-Fern-Language\": \"Python\",\n}\n",
        );
        write(
            c,
            "core/client_wrapper.py",
            b"h = {\n    \"X-Crozier-Language\": \"Python\",\n}\n",
        );

        let found = compare_trees(r, c, None, true).unwrap();
        let paths: Vec<&str> = found.differences.iter().map(|(p, _)| p.as_str()).collect();
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
            found.differences[0].1,
            Difference::Binary {
                reference: 2,
                crozier: 1
            }
        );
        let Difference::Text(Some(diff)) = &found.differences[1].1 else {
            panic!("{found:?}");
        };
        assert!(diff.contains("- reference") && diff.contains("+ crozier"));
        assert_eq!(found.differences[2].1, Difference::OnlyInReference);
        assert_eq!(found.differences[3].1, Difference::OnlyInCrozier);
        assert_eq!(
            found.departures,
            [AppliedDeparture {
                file: "core/client_wrapper.py".into(),
                line: 2,
                id: "sdk-identity-header-prefix".into(),
            }]
        );

        let summary = compare_trees(r, c, Some("changed"), false).unwrap();
        assert_eq!(
            summary.differences,
            [("changed.txt".to_string(), Difference::Text(None))]
        );
        assert!(summary.departures.is_empty());
    }

    #[test]
    fn compare_trees_reads_each_tree_s_classes_for_the_casing_rule() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        let (r, c) = (reference.path(), crozier.path());
        for root in [r, c] {
            write(root, "client.py", b"class LanternHarborApi:\n    pass\n");
        }
        write(
            r,
            "README.md",
            b"from LanternHarbor import LanternharborApi\n",
        );
        write(
            c,
            "README.md",
            b"from LanternHarbor import LanternHarborApi\n",
        );
        let found = compare_trees(r, c, None, true).unwrap();
        assert!(found.differences.is_empty(), "{found:?}");
        assert_eq!(
            found.departures,
            [AppliedDeparture {
                file: "README.md".into(),
                line: 1,
                id: "readme-client-class-casing".into(),
            }]
        );
    }

    #[test]
    fn compare_trees_reports_a_pair_a_rule_cannot_run_on() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        write(
            reference.path(),
            "__init__.py",
            b"if typing.TYPE_CHECKING:\n    import b\n    def (:\nx\n",
        );
        write(
            crozier.path(),
            "__init__.py",
            b"if typing.TYPE_CHECKING:\n    def (:\n    import b\nx\n",
        );
        let found = compare_trees(reference.path(), crozier.path(), None, true).unwrap();
        assert!(
            matches!(&found.differences[0].1, Difference::Processing(e) if e.contains("ruff")),
            "{found:?}"
        );
    }

    #[test]
    fn an_empty_reference_is_never_a_match() {
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        let error = compare_trees(reference.path(), crozier.path(), None, true).unwrap_err();
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
        let error = compare_trees(reference.path(), crozier.path(), None, true).unwrap_err();
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
        let found = compare_trees(reference.path(), crozier.path(), None, true).unwrap();
        std::fs::set_permissions(&locked, std::fs::Permissions::from_mode(0o644)).unwrap();
        // Root can read anything; only assert when the permission bit held.
        if let Some((_, difference)) = found.differences.first() {
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
        let found = compare_trees(reference.path(), crozier.path(), None, true).unwrap();
        if let Some((_, difference)) = found.differences.first() {
            assert!(
                matches!(difference, Difference::Processing(e) if e.contains("reference file")),
                "{found:?}"
            );
        }
    }

    /// A committed golden is already comment-stripped and a live reference is
    /// not; the engine strips both. That is safe for the corpus only because
    /// stripping a stripped golden changes nothing, which this pins over every
    /// committed golden and probe-measurement tree.
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
