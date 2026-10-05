//! The Fern defect registry, `tests/fixtures/fern-defects.toml`: the line-level
//! account of each Fern defect crozier does not reproduce, and the substitution
//! every comparison with a committed Fern golden applies before it compares a
//! file. This module is the one definition of both; the rule and the meaning of
//! each failure are in `docs/matching.md`, "Fern defects crozier does not
//! reproduce".

use std::borrow::Cow;
use std::collections::{BTreeMap, BTreeSet};
use std::path::{Path, PathBuf};

use serde::Deserialize;

/// The registry, relative to the repository root.
pub const REGISTRY: &str = "tests/fixtures/fern-defects.toml";

/// Where every entry's `evidence` note lives, relative to the repository root.
pub const EVIDENCE_DIR: &str = "docs/fern-defects/";

/// Every committed Fern golden tree some comparison reads, keyed by its
/// repository-relative path, each with the directories its files are found in.
pub type Goldens = BTreeMap<String, Vec<PathBuf>>;

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

/// The registry, parsed and validated against the goldens comparisons read.
#[derive(Debug)]
pub struct Registry {
    defects: Vec<Defect>,
}

impl Registry {
    /// Read `root`'s registry and validate every entry, returning every failure
    /// (each naming its entry) rather than the first.
    pub fn load(root: &Path, goldens: &Goldens) -> Result<Self, Vec<String>> {
        let defects = read(root).map_err(|error| vec![error])?;
        let failures = validation_failures(root, goldens, &defects);
        if failures.is_empty() {
            Ok(Self { defects })
        } else {
            Err(failures)
        }
    }

    /// The entries naming `golden`, refused when one of them names a file the
    /// comparison already carves out at file level: each `(kind, files)` pair is
    /// one such carve-out, described by `kind` in the failure.
    pub fn tree(
        &self,
        golden: &str,
        carve_outs: &[(&str, &[&str])],
    ) -> Result<TreeDefects<'_>, Vec<String>> {
        let defects = TreeDefects::of(&self.defects, golden);
        let failures: Vec<String> = defects
            .defects
            .iter()
            .flat_map(|defect| {
                carve_outs
                    .iter()
                    .filter(|(_, files)| files.contains(&defect.file.as_str()))
                    .map(|(kind, _)| {
                        format!(
                            "fern defect `{}`: {} in {golden} is also {kind}; a file is accounted \
                             for at line level or at file level, never both — remove one",
                            defect.id, defect.file
                        )
                    })
            })
            .collect();
        if failures.is_empty() {
            Ok(defects)
        } else {
            Err(failures)
        }
    }
}

/// The entries one comparison applies to the golden it reads.
#[derive(Debug)]
pub struct TreeDefects<'r> {
    defects: Vec<&'r Defect>,
}

impl<'r> TreeDefects<'r> {
    /// The entries of `defects` naming `golden`, unvalidated: a comparison
    /// that holds no file to equality reads these straight from [`read`].
    pub fn of(defects: &'r [Defect], golden: &str) -> Self {
        Self {
            defects: defects
                .iter()
                .filter(|defect| defect.golden == golden)
                .collect(),
        }
    }

    /// Add `base`'s entries for every file this tree takes from its base golden
    /// unchanged — every file not in `own`, the files the tree carries itself.
    pub fn inherit(mut self, base: TreeDefects<'r>, own: &BTreeSet<String>) -> Self {
        self.defects.extend(
            base.defects
                .into_iter()
                .filter(|defect| !own.contains(&defect.file)),
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

    /// The Fern text a comparison holds crozier's `generated` file `rel` to:
    /// `fern` itself when no entry names `rel`, otherwise `fern` with each
    /// entry's lines replaced by crozier's. `matches` is the comparison's own
    /// equality. Fails, naming the entries, when crozier already matches the
    /// unsubstituted file (the entries are stale), or naming one entry, when its
    /// `fern` text does not occur in the file exactly once.
    pub fn expected<'t>(
        &self,
        rel: &str,
        generated: &str,
        fern: &'t str,
        matches: impl Fn(&str, &str, &str) -> bool,
    ) -> Result<Cow<'t, str>, String> {
        let applied: Vec<&Defect> = self
            .defects
            .iter()
            .copied()
            .filter(|defect| defect.file == rel)
            .collect();
        if applied.is_empty() {
            return Ok(Cow::Borrowed(fern));
        }
        if matches(rel, generated, fern) {
            let ids: Vec<String> = applied
                .iter()
                .map(|defect| format!("`{}`", defect.id))
                .collect();
            return Err(format!(
                "fern defect {}: crozier's {rel} already equals Fern's golden without the \
                 substitution — the entry is stale; remove it",
                ids.join(", ")
            ));
        }
        let mut text = fern.to_string();
        for defect in applied {
            text = substitute(&text, defect)?;
        }
        Ok(Cow::Owned(text))
    }
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

/// Every way `defects` breaks the contract on its own, before any comparison.
fn validation_failures(root: &Path, goldens: &Goldens, defects: &[Defect]) -> Vec<String> {
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
        let evidence = Path::new(&defect.evidence);
        if !defect.evidence.starts_with(EVIDENCE_DIR)
            || evidence
                .components()
                .any(|part| part == std::path::Component::ParentDir)
            || !root.join(evidence).is_file()
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
        match goldens.get(&defect.golden) {
            None => failures.push(format!(
                "fern defect `{id}`: golden `{}` is not a tree any comparison reads",
                defect.golden
            )),
            Some(dirs) if !dirs.iter().any(|dir| dir.join(&defect.file).is_file()) => {
                failures.push(format!(
                    "fern defect `{id}`: file `{}` is not in golden `{}`, so no comparison reads it",
                    defect.file, defect.golden
                ));
            }
            Some(_) => {}
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

/// `text` with `defect`'s `fern` lines, which must start a line and occur once,
/// replaced by its `crozier` lines.
fn substitute(text: &str, defect: &Defect) -> Result<String, String> {
    let fern = whole_lines(&defect.fern);
    let crozier = whole_lines(&defect.crozier);
    // A file whose last line has no newline still ends a line there.
    let padded = !text.is_empty() && !text.ends_with('\n');
    let haystack = whole_lines(text);
    let hits: Vec<usize> = haystack
        .match_indices(fern.as_ref())
        .map(|(index, _)| index)
        .filter(|index| *index == 0 || haystack.as_bytes()[index - 1] == b'\n')
        .collect();
    let [hit] = hits[..] else {
        return Err(format!(
            "fern defect `{}`: its `fern` lines occur {} times in {}/{}; they must occur exactly \
             once",
            defect.id,
            hits.len(),
            defect.golden,
            defect.file
        ));
    };
    let mut replaced = format!(
        "{}{crozier}{}",
        &haystack[..hit],
        &haystack[hit + fern.len()..]
    );
    if padded && replaced.ends_with('\n') {
        replaced.pop();
    }
    Ok(replaced)
}
