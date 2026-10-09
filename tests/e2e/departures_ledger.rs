//! The per-golden ledger of intended departures,
//! `tests/fixtures/departures-ledger.tsv`: for each committed Fern golden, every
//! `(file, line, catalog id)` the comparison engine reports applying when it
//! compares crozier's output with that golden. Every golden comparison in both
//! test binaries holds the departures it observes to the golden's rows, so a
//! departure that stops applying fails as stale and one that newly applies
//! fails as unrecorded. The catalog itself is `assets/departures.yml`; the
//! contract and the regeneration command are in `docs/departures/README.md`.

use std::collections::{BTreeMap, BTreeSet};
use std::path::{Component, Path};

use serde::{Deserialize, Serialize};

/// The ledger, relative to the repository root.
pub const LEDGER: &str = "tests/fixtures/departures-ledger.tsv";

/// The ledger's first line.
pub const HEADER: &str = "golden\tfile\tline\tdeparture";

/// The inventory of compared goldens, relative to the repository root.
pub const INVENTORY: &str = "tests/fixtures/compared-goldens.json";

/// The command that regenerates the ledger.
pub const REGENERATE: &str = "just departures-ledger";

/// Set to a directory, every golden comparison records the departures it
/// observes there instead of holding them to the ledger; `just
/// departures-ledger` then merges the records into it.
pub const RECORD_ENV: &str = "CROZIER_RECORD_DEPARTURES";

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

/// One ledger row.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
pub struct Row {
    pub golden: String,
    pub file: String,
    pub line: usize,
    pub departure: String,
}

impl Row {
    /// The row as the ledger spells it.
    pub fn render(&self) -> String {
        format!(
            "{}\t{}\t{}\t{}",
            self.golden, self.file, self.line, self.departure
        )
    }
}

/// One departure a comparison observed: the file, crozier's line and the
/// catalog id.
pub type Observed = (String, usize, String);

/// The ledger, parsed and validated against the inventory and the catalog.
#[derive(Debug)]
pub struct Ledger {
    rows: Vec<Row>,
    goldens: BTreeMap<String, ComparedGolden>,
}

impl Ledger {
    /// Read `root`'s inventory and ledger and validate every row, returning
    /// every failure (each naming its row) rather than the first. Every
    /// comparison in both test binaries loads the ledger through this.
    pub fn load(root: &Path) -> Result<Self, Vec<String>> {
        let inventory = Inventory::read(root).map_err(|error| vec![error])?;
        let text = std::fs::read_to_string(root.join(LEDGER))
            .map_err(|error| vec![format!("{LEDGER}: cannot be read: {error}")])?;
        let rows = parse(&text)?;
        let failures = validation_failures(root, &inventory, &rows);
        if failures.is_empty() {
            Ok(Self {
                rows,
                goldens: inventory.goldens,
            })
        } else {
            Err(failures)
        }
    }

    /// Whether the inventory records `golden` as a tree a comparison reads.
    pub fn compares(&self, golden: &str) -> bool {
        self.goldens.contains_key(golden)
    }

    /// Every file the inventory records `golden`'s comparisons carving out at
    /// file level, whatever the kind.
    #[allow(
        dead_code,
        reason = "only tests/generation.rs's in-process comparison asks; the e2e gates know \
                  their corpora's carve-outs directly"
    )]
    pub fn carved_out(&self, golden: &str) -> BTreeSet<String> {
        self.goldens
            .get(golden)
            .map(|compared| compared.carve_outs.values().flatten().cloned().collect())
            .unwrap_or_default()
    }

    /// The rows for `golden`, refused when one names a file the comparison
    /// carves out at file level: each `(slug, files)` pair is one such
    /// carve-out, of a kind in [`CARVE_OUT_KINDS`].
    pub fn golden(
        &self,
        golden: &str,
        carve_outs: &[(&str, &[&str])],
    ) -> Result<GoldenLedger, Vec<String>> {
        let rows: Vec<Row> = self
            .rows
            .iter()
            .filter(|row| row.golden == golden)
            .cloned()
            .collect();
        let failures: Vec<String> = rows
            .iter()
            .flat_map(|row| {
                carve_outs
                    .iter()
                    .filter(|(_, files)| files.contains(&row.file.as_str()))
                    .map(|(slug, _)| carve_out_failure(row, slug))
            })
            .collect();
        if failures.is_empty() {
            Ok(GoldenLedger {
                golden: golden.to_string(),
                known: self.compares(golden),
                rows,
                base: None,
                removed: BTreeSet::new(),
            })
        } else {
            Err(failures)
        }
    }
}

/// The failure for `row` naming a file also carved out as `slug`.
fn carve_out_failure(row: &Row, slug: &str) -> String {
    format!(
        "{LEDGER}: `{}` names a file that is also {}; a file is accounted for at line level or \
         at file level, never both — remove one",
        row.render(),
        carve_out_kind(slug).unwrap_or(slug)
    )
}

/// The rows one comparison holds its observed departures to.
#[derive(Debug, Clone)]
pub struct GoldenLedger {
    golden: String,
    /// Whether the inventory records the golden; only such a golden's
    /// departures are recorded, never a scratch tree's.
    known: bool,
    rows: Vec<Row>,
    /// For an overlay golden: its base golden's rows, and the files the
    /// overlay carries itself (every other file is the base's).
    base: Option<(Box<GoldenLedger>, BTreeSet<String>)>,
    /// For an overlay golden: the base files it leaves out.
    removed: BTreeSet<String>,
}

impl GoldenLedger {
    /// Take `base`'s rows for every file this tree takes from its base golden
    /// unchanged: every file neither in `own`, the files the tree carries
    /// itself, nor in `removed`, the base files the tree leaves out.
    pub fn inherit(
        mut self,
        base: GoldenLedger,
        own: BTreeSet<String>,
        removed: &[String],
    ) -> Self {
        self.base = Some((Box::new(base), own));
        self.removed = removed.iter().cloned().collect();
        self
    }

    /// The golden whose rows account for `file`.
    fn owner(&self, file: &str) -> &GoldenLedger {
        match &self.base {
            Some((base, own)) if !own.contains(file) => base,
            _ => self,
        }
    }

    /// The `(file, line, departure)` rows that account for the files `scope`
    /// admits.
    fn expected(&self, scope: &dyn Fn(&str) -> bool) -> BTreeSet<Observed> {
        let own = self
            .rows
            .iter()
            .filter(|row| self.owner(&row.file).golden == self.golden);
        let inherited = self.base.iter().flat_map(|(base, own)| {
            base.rows
                .iter()
                .filter(move |row| !own.contains(&row.file) && !self.removed.contains(&row.file))
        });
        own.chain(inherited)
            .filter(|row| scope(&row.file))
            .map(|row| (row.file.clone(), row.line, row.departure.clone()))
            .collect()
    }

    /// Whether a row this comparison is held to names `file`.
    #[allow(
        dead_code,
        reason = "only tests/generation.rs's in-process comparison asks; the module is shared"
    )]
    pub fn names(&self, file: &str) -> bool {
        !self.expected(&|rel| rel == file).is_empty()
    }

    /// Hold `observed`, every departure a comparison applied in the files
    /// `scope` admits, to the rows: one failure per stale row (the engine no
    /// longer applies it) and per unrecorded departure (no row records it).
    /// Under [`RECORD_ENV`], record `observed` there instead and pass.
    pub fn check(&self, observed: &[Observed], scope: &dyn Fn(&str) -> bool) -> Vec<String> {
        if let Some(dir) = std::env::var_os(RECORD_ENV) {
            return match self.record_to(Path::new(&dir), observed) {
                Ok(()) => Vec::new(),
                Err(error) => vec![error],
            };
        }
        let observed: BTreeSet<Observed> = observed.iter().cloned().collect();
        let expected = self.expected(scope);
        let row = |(file, line, departure): &Observed| Row {
            golden: self.owner(file).golden.clone(),
            file: file.clone(),
            line: *line,
            departure: departure.clone(),
        };
        let stale = expected.difference(&observed).map(|found| {
            format!(
                "{LEDGER}: `{}` is stale: the comparison no longer applies that departure there \
                 — if that is intended, regenerate the ledger with `{REGENERATE}`; otherwise fix \
                 the generator",
                row(found).render()
            )
        });
        let unrecorded = observed.difference(&expected).map(|found| {
            format!(
                "{LEDGER}: `{}` is unrecorded: the comparison applies that departure, but the \
                 ledger has no such row — if the departure is intended, regenerate the ledger \
                 with `{REGENERATE}`; otherwise fix the generator",
                row(found).render()
            )
        });
        stale.chain(unrecorded).collect()
    }

    /// Write `observed` under `dir`, one file per golden it belongs to, beside
    /// any other comparison's records of the same golden — this golden's and
    /// its base's even when empty, so a golden whose departures all stopped
    /// applying loses its rows at the merge.
    pub fn record_to(&self, dir: &Path, observed: &[Observed]) -> Result<(), String> {
        let mut by_golden: BTreeMap<&str, Vec<&Observed>> = BTreeMap::new();
        by_golden.entry(&self.golden).or_default();
        if let Some((base, _)) = &self.base {
            by_golden.entry(&base.golden).or_default();
        }
        for found in observed {
            by_golden
                .entry(&self.owner(&found.0).golden)
                .or_default()
                .push(found);
        }
        let known = |golden: &str| match &self.base {
            Some((base, _)) if base.golden == golden => base.known,
            _ => self.known,
        };
        for (golden, found) in by_golden.into_iter().filter(|(golden, _)| known(golden)) {
            let target = dir.join(golden.replace('/', "%"));
            std::fs::create_dir_all(&target)
                .map_err(|error| format!("{RECORD_ENV}: {}: {error}", target.display()))?;
            let text: String = found
                .iter()
                .map(|(file, line, departure)| format!("{file}\t{line}\t{departure}\n"))
                .collect();
            let mut file = tempfile::Builder::new()
                .suffix(".tsv")
                .tempfile_in(&target)
                .map_err(|error| format!("{RECORD_ENV}: {}: {error}", target.display()))?;
            std::io::Write::write_all(&mut file, text.as_bytes())
                .map_err(|error| format!("{RECORD_ENV}: {error}"))?;
            file.keep()
                .map_err(|error| format!("{RECORD_ENV}: {error}"))?;
        }
        Ok(())
    }
}

/// Parse the ledger's text: the header, then four tab-separated fields per row.
pub fn parse(text: &str) -> Result<Vec<Row>, Vec<String>> {
    let mut lines = text.lines();
    if lines.next() != Some(HEADER) {
        return Err(vec![format!(
            "{LEDGER}: the first line is the header `{}`",
            HEADER.replace('\t', "\\t")
        )]);
    }
    let mut rows = Vec::new();
    let mut failures = Vec::new();
    for (index, line) in lines.enumerate() {
        let fields: Vec<&str> = line.split('\t').collect();
        match fields[..] {
            [golden, file, number, departure] => match number.parse::<usize>() {
                // Line 0 is a whole file only one side has, which only a file
                // rule accounts for.
                Ok(number)
                    if number > 0
                        || crozier::departures::rule(departure)
                            .is_some_and(|rule| rule.file.is_some()) =>
                {
                    rows.push(Row {
                        golden: golden.to_string(),
                        file: file.to_string(),
                        line: number,
                        departure: departure.to_string(),
                    })
                }
                _ => failures.push(format!(
                    "{LEDGER}:{}: `{line}`: the line is not a positive number (0, a whole \
                     file, is a file rule's)",
                    index + 2
                )),
            },
            _ => failures.push(format!(
                "{LEDGER}:{}: `{line}` is not four tab-separated fields: golden, file, line, \
                 departure",
                index + 2
            )),
        }
    }
    if failures.is_empty() {
        Ok(rows)
    } else {
        Err(failures)
    }
}

/// The ledger's text holding `rows`, sorted.
pub fn render(rows: &BTreeSet<Row>) -> String {
    let mut text = format!("{HEADER}\n");
    for row in rows {
        text.push_str(&row.render());
        text.push('\n');
    }
    text
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

/// Every way `rows` break the contract, judged against `inventory` and the
/// compiled catalog, each naming its row.
fn validation_failures(root: &Path, inventory: &Inventory, rows: &[Row]) -> Vec<String> {
    let mut failures = Vec::new();
    for pair in rows.windows(2) {
        let (previous, row) = (&pair[0], &pair[1]);
        if previous == row {
            failures.push(format!(
                "{LEDGER}: `{}` appears twice; every row is unique",
                row.render()
            ));
        } else if previous > row {
            failures.push(format!(
                "{LEDGER}: `{}` follows `{}`; rows are sorted by golden, file, line and departure",
                row.render(),
                previous.render()
            ));
        }
    }
    let mut compared: BTreeMap<&str, Result<BTreeSet<String>, String>> = BTreeMap::new();
    for row in rows {
        let shown = row.render();
        if crozier::departures::find(&row.departure).is_none() {
            failures.push(format!(
                "{LEDGER}: `{shown}` names `{}`, which is no entry of the departure catalog",
                row.departure
            ));
        }
        let Some(golden) = inventory.goldens.get(&row.golden) else {
            failures.push(format!(
                "{LEDGER}: `{shown}` names golden `{}`, which no comparison reads",
                row.golden
            ));
            continue;
        };
        if !is_plain_relative(&row.file) {
            failures.push(format!(
                "{LEDGER}: `{shown}` names file `{}`, which is not a relative path inside its \
                 golden",
                row.file
            ));
            continue;
        }
        let carved: Vec<String> = golden
            .carve_outs
            .iter()
            .filter(|(_, files)| files.contains(&row.file))
            .map(|(slug, _)| carve_out_failure(row, slug))
            .collect();
        if !carved.is_empty() {
            failures.extend(carved);
            continue;
        }
        let files = compared.entry(row.golden.as_str()).or_insert_with(|| {
            crozier::parity::walk_files(&root.join(&row.golden)).map(|files| {
                files
                    .into_iter()
                    .filter(|file| !golden.excluded.contains(file))
                    .collect()
            })
        });
        match files {
            Ok(files) if files.contains(&row.file) => {}
            // Line 0 is a whole file only one side has, so it may be one only
            // crozier writes; the comparison holds it like any other row.
            Ok(_) if row.line == 0 => {}
            Ok(_) => failures.push(format!(
                "{LEDGER}: `{shown}` names file `{}`, which no comparison of golden `{}` reads",
                row.file, row.golden
            )),
            Err(error) => failures.push(format!(
                "{LEDGER}: `{shown}`: golden `{}` cannot be read: {error}",
                row.golden
            )),
        }
    }
    failures
}

/// Merge the records under `dir` into `root`'s ledger: each recorded golden's
/// rows become exactly the union of what its comparisons recorded; every other
/// golden keeps its rows. Returns the merged ledger's text.
pub fn merge_records(root: &Path, dir: &Path) -> Result<String, String> {
    let text = std::fs::read_to_string(root.join(LEDGER)).unwrap_or_else(|_| format!("{HEADER}\n"));
    let current = parse(&text).map_err(|failures| failures.join("\n"))?;
    let mut recorded: BTreeMap<String, BTreeSet<Row>> = BTreeMap::new();
    let entries = std::fs::read_dir(dir).map_err(|error| format!("{}: {error}", dir.display()))?;
    for entry in entries {
        let entry = entry.map_err(|error| format!("{}: {error}", dir.display()))?;
        let golden = entry.file_name().to_string_lossy().replace('%', "/");
        let rows = recorded.entry(golden.clone()).or_default();
        let files = std::fs::read_dir(entry.path())
            .map_err(|error| format!("{}: {error}", entry.path().display()))?;
        for file in files {
            let path = file
                .map_err(|error| format!("{}: {error}", entry.path().display()))?
                .path();
            let text = std::fs::read_to_string(&path)
                .map_err(|error| format!("{}: {error}", path.display()))?;
            for line in text.lines() {
                let [file, number, departure] = line.split('\t').collect::<Vec<_>>()[..] else {
                    return Err(format!("{}: `{line}` is not a record", path.display()));
                };
                rows.insert(Row {
                    golden: golden.clone(),
                    file: file.to_string(),
                    line: number
                        .parse()
                        .map_err(|_| format!("{}: `{line}` is not a record", path.display()))?,
                    departure: departure.to_string(),
                });
            }
        }
    }
    let mut merged: BTreeSet<Row> = current
        .into_iter()
        .filter(|row| !recorded.contains_key(&row.golden))
        .collect();
    merged.extend(recorded.into_values().flatten());
    Ok(render(&merged))
}
