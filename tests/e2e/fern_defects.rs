//! The Fern defect registry, `tests/fixtures/fern-defects.toml`: the line-level
//! account of each Fern defect crozier does not reproduce, and the substitution
//! every comparison with a committed Fern golden applies before it compares a
//! file. This module is the one definition of both, and of the inventory of
//! compared goldens the registry is validated against; the rule and the meaning
//! of each failure are in `docs/matching.md`, "Fern defects crozier does not
//! reproduce".

use std::borrow::Cow;
use std::collections::{BTreeMap, BTreeSet};
use std::path::{Component, Path};

use serde::{Deserialize, Serialize};

/// The registry, relative to the repository root.
pub const REGISTRY: &str = "tests/fixtures/fern-defects.toml";

/// The inventory of compared goldens, relative to the repository root.
pub const INVENTORY: &str = "tests/fixtures/compared-goldens.json";

/// Where every entry's `evidence` note lives, relative to the repository root.
pub const EVIDENCE_DIR: &str = "docs/fern-defects/";

/// The file-level carve-outs a comparison records, each as its inventory slug
/// and the words a failure uses for it.
pub const CARVE_OUT_KINDS: [(&str, &str); 4] = [
    ("crozier-only", "a crozier-only file"),
    ("pinned", "a file pinned to crozier's own bytes"),
    (
        "scaffolding",
        "repository scaffolding crozier does not emit",
    ),
    ("unmatched", "an `unmatched` entry"),
];

/// One `[[defect]]` table: exactly these keys, all strings.
#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Defect {
    pub id: String,
    pub gap: String,
    pub golden: String,
    pub file: String,
    pub fern: String,
    pub crozier: String,
    pub reason: String,
    pub evidence: String,
}

/// The whole file: the `defect` array and nothing else.
#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct Document {
    #[serde(default)]
    defect: Vec<Defect>,
}

/// Every committed Fern golden tree a comparison reads crozier's output
/// against, keyed by its repository-relative path. `tests/e2e.rs` derives it
/// from the comparisons' own registrations and holds the committed copy,
/// [`INVENTORY`], to them, so both test binaries validate against one list.
#[derive(Debug, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Inventory {
    pub goldens: BTreeMap<String, ComparedGolden>,
}

/// What the comparisons of one golden read: every file a walk of the tree
/// yields (the walk already skips the provenance record) except `excluded`,
/// with `carve_outs` — the files they account for at file level, by kind slug.
#[derive(Debug, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ComparedGolden {
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub excluded: Vec<String>,
    #[serde(default, skip_serializing_if = "BTreeMap::is_empty")]
    pub carve_outs: BTreeMap<String, Vec<String>>,
}

impl Inventory {
    /// Read `root`'s committed inventory.
    pub fn read(root: &Path) -> Result<Self, String> {
        let text = std::fs::read_to_string(root.join(INVENTORY))
            .map_err(|error| format!("{INVENTORY}: cannot be read: {error}"))?;
        let inventory: Self = serde_json::from_str(&text)
            .map_err(|error| format!("{INVENTORY}: is not an inventory: {error}"))?;
        for (golden, compared) in &inventory.goldens {
            for slug in compared.carve_outs.keys() {
                if carve_out_kind(slug).is_none() {
                    return Err(format!(
                        "{INVENTORY}: {golden} records an unknown carve-out kind `{slug}`"
                    ));
                }
            }
        }
        Ok(inventory)
    }

    /// The inventory as the committed file spells it.
    pub fn render(&self) -> String {
        let mut text = serde_json::to_string_pretty(self).expect("an inventory serializes");
        text.push('\n');
        text
    }
}

/// The words a failure uses for the carve-out kind `slug`.
fn carve_out_kind(slug: &str) -> Option<&'static str> {
    CARVE_OUT_KINDS
        .iter()
        .find(|(known, _)| *known == slug)
        .map(|(_, kind)| *kind)
}

/// The registry, parsed and validated against the inventory.
#[derive(Debug)]
pub struct Registry {
    defects: Vec<Defect>,
    goldens: BTreeSet<String>,
}

impl Registry {
    /// Read `root`'s inventory and registry and validate every entry, returning
    /// every failure (each naming its entry) rather than the first. Every
    /// comparison in both test binaries loads the registry through this.
    pub fn load(root: &Path) -> Result<Self, Vec<String>> {
        let inventory = Inventory::read(root).map_err(|error| vec![error])?;
        let defects = read(root).map_err(|error| vec![error])?;
        let failures = validation_failures(root, &inventory, &defects);
        if failures.is_empty() {
            Ok(Self {
                defects,
                goldens: inventory.goldens.into_keys().collect(),
            })
        } else {
            Err(failures)
        }
    }

    /// Whether the inventory records `golden` as a tree a comparison reads.
    pub fn compares(&self, golden: &str) -> bool {
        self.goldens.contains(golden)
    }

    /// The entries naming `golden`, refused when one of them names a file the
    /// comparison carves out at file level: each `(slug, files)` pair is one
    /// such carve-out, of a kind in [`CARVE_OUT_KINDS`].
    pub fn tree(
        &self,
        golden: &str,
        carve_outs: &[(&str, &[&str])],
    ) -> Result<TreeDefects<'_>, Vec<String>> {
        let defects: Vec<&Defect> = self
            .defects
            .iter()
            .filter(|defect| defect.golden == golden)
            .collect();
        let failures: Vec<String> = defects
            .iter()
            .flat_map(|defect| {
                carve_outs
                    .iter()
                    .filter(|(_, files)| files.contains(&defect.file.as_str()))
                    .map(|(slug, _)| carve_out_failure(defect, slug))
            })
            .collect();
        if failures.is_empty() {
            Ok(TreeDefects { defects })
        } else {
            Err(failures)
        }
    }
}

/// The failure for `defect` naming a file also carved out as `slug`.
fn carve_out_failure(defect: &Defect, slug: &str) -> String {
    format!(
        "fern defect `{}`: {} in {} is also {}; a file is accounted for at line level or at \
         file level, never both — remove one",
        defect.id,
        defect.file,
        defect.golden,
        carve_out_kind(slug).unwrap_or(slug)
    )
}

/// The entries one comparison applies to the golden it reads.
#[derive(Debug)]
pub struct TreeDefects<'r> {
    defects: Vec<&'r Defect>,
}

impl<'r> TreeDefects<'r> {
    /// Add `base`'s entries for every file this tree takes from its base golden
    /// unchanged: every file neither in `own`, the files the tree carries
    /// itself, nor in `removed`, the base files the tree leaves out.
    pub fn inherit(
        mut self,
        base: TreeDefects<'r>,
        own: &BTreeSet<String>,
        removed: &[String],
    ) -> Self {
        self.defects.extend(
            base.defects
                .into_iter()
                .filter(|defect| !own.contains(&defect.file) && !removed.contains(&defect.file)),
        );
        self
    }

    /// The files an entry applies to.
    pub fn files(&self) -> BTreeSet<&'r str> {
        self.defects
            .iter()
            .map(|defect| defect.file.as_str())
            .collect()
    }

    /// The failure for the entries naming `rel` when they cannot apply because
    /// `side` (`crozier wrote no`, `Fern's golden holds no`) lacks the file.
    pub fn cannot_apply(&self, rel: &str, side: &str) -> String {
        format!(
            "fern defect {}: {side} {rel}, so the entry cannot apply",
            ids(self.named(rel).as_slice())
        )
    }

    /// The failure for the entries naming `rel` when crozier's file still
    /// differs from Fern's once they are substituted; `diff` is the normalized
    /// difference that remains.
    pub fn still_differs(&self, rel: &str, diff: &str) -> String {
        format!(
            "fern defect {}: crozier's {rel} still differs from Fern's golden after the \
             substitution — fix the generator or the entry\n{diff}",
            ids(self.named(rel).as_slice())
        )
    }

    /// One failure per file an entry names that crozier's tree `out` lacks.
    pub fn unwritten(&self, out: &Path) -> Vec<String> {
        self.files()
            .into_iter()
            .filter(|rel| !out.join(rel).is_file())
            .map(|rel| self.cannot_apply(rel, "crozier wrote no"))
            .collect()
    }

    /// The entries naming `rel`.
    fn named(&self, rel: &str) -> Vec<&'r Defect> {
        self.defects
            .iter()
            .copied()
            .filter(|defect| defect.file == rel)
            .collect()
    }

    /// The Fern text a comparison holds crozier's `generated` file `rel` to:
    /// `fern` itself when no entry names `rel`, otherwise `fern` with every
    /// entry's lines replaced by crozier's at once. `matches` is the
    /// comparison's own equality. Fails, naming the entries, when crozier
    /// already matches the unsubstituted file (the entries are stale), when an
    /// entry's `fern` lines do not start exactly one line of the original file,
    /// or when two entries' lines overlap.
    pub fn expected<'t>(
        &self,
        rel: &str,
        generated: &str,
        fern: &'t str,
        matches: impl Fn(&str, &str, &str) -> bool,
    ) -> Result<Cow<'t, str>, String> {
        let applied = self.named(rel);
        if applied.is_empty() {
            return Ok(Cow::Borrowed(fern));
        }
        if matches(rel, generated, fern) {
            return Err(format!(
                "fern defect {}: crozier's {rel} already equals Fern's golden without the \
                 substitution — the entry is stale; remove it",
                ids(&applied)
            ));
        }
        substitute(fern, &applied).map(Cow::Owned)
    }
}

/// `defects`' ids, each in backticks.
fn ids(defects: &[&Defect]) -> String {
    defects
        .iter()
        .map(|defect| format!("`{}`", defect.id))
        .collect::<Vec<_>>()
        .join(", ")
}

/// Read and parse `root`'s registry, without validating it.
pub fn read(root: &Path) -> Result<Vec<Defect>, String> {
    let text = std::fs::read_to_string(root.join(REGISTRY))
        .map_err(|error| format!("{REGISTRY}: cannot be read: {error}"))?;
    parse(&text)
}

/// Parse the registry's text: the `defect` array of tables, each holding
/// exactly the eight string keys.
pub fn parse(text: &str) -> Result<Vec<Defect>, String> {
    toml::from_str::<Document>(text)
        .map(|document| document.defect)
        .map_err(|error| {
            format!(
                "{REGISTRY}: every [[defect]] holds exactly the keys {}, all strings: {error}",
                keys().join(", ")
            )
        })
}

/// The keys a `[[defect]]` table holds, in declaration order, read from the
/// loader itself — the deserializer's refusal of an unknown key lists them — so
/// the documentation of the keys is checked against [`Defect`], not a copy.
pub fn keys() -> Vec<String> {
    let refusal = toml::from_str::<Document>("[[defect]]\n_ = \"\"\n")
        .expect_err("an unknown key is refused")
        .to_string();
    let listed = refusal
        .split_once("expected one of ")
        .map_or("", |(_, listed)| listed);
    listed
        .split('`')
        .skip(1)
        .step_by(2)
        .map(str::to_string)
        .collect()
}

/// Whether `path` is a non-empty, `/`-separated relative path of plain names:
/// no root, drive prefix, backslash, or empty, `.` or `..` part, so it can only
/// name something inside the tree it is relative to.
fn is_plain_relative(path: &str) -> bool {
    !path.contains('\\')
        && path
            .split('/')
            .all(|part| !part.is_empty() && part != "." && part != "..")
        && Path::new(path)
            .components()
            .all(|part| matches!(part, Component::Normal(_)))
}

/// Every way `defects` breaks the contract, judged against `inventory`.
fn validation_failures(root: &Path, inventory: &Inventory, defects: &[Defect]) -> Vec<String> {
    let mut failures = Vec::new();
    for pair in defects.windows(2) {
        let (previous, defect) = (&pair[0], &pair[1]);
        if previous.id == defect.id {
            failures.push(format!(
                "fern defect `{}`: the id appears twice; ids are unique",
                defect.id
            ));
        } else if previous.id > defect.id {
            failures.push(format!(
                "fern defect `{}`: follows `{}`; entries are sorted by id",
                defect.id, previous.id
            ));
        }
    }
    let mut compared: BTreeMap<&str, Result<BTreeSet<String>, String>> = BTreeMap::new();
    for defect in defects {
        let id = &defect.id;
        let slug = !id.is_empty()
            && !id.starts_with('-')
            && !id.ends_with('-')
            && !id.contains("--")
            && id
                .bytes()
                .all(|byte| byte.is_ascii_lowercase() || byte.is_ascii_digit() || byte == b'-');
        if !slug {
            failures.push(format!(
                "fern defect `{id}`: the id is not a lower-kebab slug"
            ));
        }
        for (key, value) in [
            ("gap", &defect.gap),
            ("golden", &defect.golden),
            ("file", &defect.file),
            ("fern", &defect.fern),
        ] {
            if value.trim().is_empty() {
                failures.push(format!("fern defect `{id}`: `{key}` is empty"));
            }
        }
        if defect.reason.trim().is_empty() || defect.reason.contains('\n') {
            failures.push(format!(
                "fern defect `{id}`: `reason` is empty or more than one line; say in one line why \
                 Fern's lines are wrong on their own terms"
            ));
        }
        if !is_plain_relative(&defect.evidence)
            || !defect.evidence.starts_with(EVIDENCE_DIR)
            || !root.join(&defect.evidence).is_file()
        {
            failures.push(format!(
                "fern defect `{id}`: `evidence` `{}` is no committed note under {EVIDENCE_DIR}",
                defect.evidence
            ));
        }
        if whole_lines(&defect.fern) == whole_lines(&defect.crozier) {
            failures.push(format!(
                "fern defect `{id}`: `fern` equals `crozier`, so it accounts for no difference"
            ));
        }
        let Some(golden) = inventory.goldens.get(&defect.golden) else {
            failures.push(format!(
                "fern defect `{id}`: golden `{}` is not a tree any comparison reads",
                defect.golden
            ));
            continue;
        };
        if !is_plain_relative(&defect.file) {
            failures.push(format!(
                "fern defect `{id}`: file `{}` is not a relative path inside its golden",
                defect.file
            ));
            continue;
        }
        let carved: Vec<String> = golden
            .carve_outs
            .iter()
            .filter(|(_, files)| files.contains(&defect.file))
            .map(|(slug, _)| carve_out_failure(defect, slug))
            .collect();
        if !carved.is_empty() {
            failures.extend(carved);
            continue;
        }
        let files = compared.entry(defect.golden.as_str()).or_insert_with(|| {
            crozier::parity::walk_files(&root.join(&defect.golden)).map(|files| {
                files
                    .into_iter()
                    .filter(|file| !golden.excluded.contains(file))
                    .collect()
            })
        });
        match files {
            Ok(files) if files.contains(&defect.file) => {}
            Ok(_) => failures.push(format!(
                "fern defect `{id}`: file `{}` is not a file any comparison of golden `{}` reads",
                defect.file, defect.golden
            )),
            Err(error) => failures.push(format!(
                "fern defect `{id}`: golden `{}` cannot be read: {error}",
                defect.golden
            )),
        }
    }
    failures
}

/// `text` as whole lines: newline-terminated unless empty.
fn whole_lines(text: &str) -> Cow<'_, str> {
    if text.is_empty() || text.ends_with('\n') {
        Cow::Borrowed(text)
    } else {
        Cow::Owned(format!("{text}\n"))
    }
}

/// `text` with every one of `defects`' `fern` lines replaced by its `crozier`
/// lines at once. Each entry's lines must start exactly one line of the
/// original `text` — every line start is tried, so overlapping occurrences
/// count — and no two entries' lines may overlap, so no substitution can make
/// or unmake another's occurrence.
fn substitute(text: &str, defects: &[&Defect]) -> Result<String, String> {
    // A file whose last line has no newline still ends a line there.
    let padded = !text.is_empty() && !text.ends_with('\n');
    let haystack = whole_lines(text);
    let starts: Vec<usize> = std::iter::once(0)
        .chain(haystack.match_indices('\n').map(|(index, _)| index + 1))
        .filter(|start| *start < haystack.len())
        .collect();
    let mut spans = Vec::new();
    let mut failures = Vec::new();
    for defect in defects {
        let fern = whole_lines(&defect.fern);
        let hits: Vec<usize> = starts
            .iter()
            .copied()
            .filter(|start| haystack[*start..].starts_with(fern.as_ref()))
            .collect();
        if let [hit] = hits[..] {
            spans.push((hit, hit + fern.len(), *defect));
        } else {
            failures.push(format!(
                "fern defect `{}`: its `fern` lines occur {} times in {}/{}; they must occur \
                 exactly once",
                defect.id,
                hits.len(),
                defect.golden,
                defect.file
            ));
        }
    }
    spans.sort_by_key(|(start, _, _)| *start);
    for pair in spans.windows(2) {
        let ((_, end, first), (start, _, second)) = (pair[0], pair[1]);
        if start < end {
            failures.push(format!(
                "fern defect {}: their `fern` lines overlap in {}/{}; each entry names lines no \
                 other entry names",
                ids(&[first, second]),
                first.golden,
                first.file
            ));
        }
    }
    if !failures.is_empty() {
        return Err(failures.join("\n"));
    }
    let mut replaced = String::with_capacity(haystack.len());
    let mut at = 0;
    for (start, end, defect) in spans {
        replaced.push_str(&haystack[at..start]);
        replaced.push_str(&whole_lines(&defect.crozier));
        at = end;
    }
    replaced.push_str(&haystack[at..]);
    if padded && replaced.ends_with('\n') {
        replaced.pop();
    }
    Ok(replaced)
}
