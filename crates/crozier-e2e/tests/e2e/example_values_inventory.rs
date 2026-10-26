//! The committed inventory of worked-example values Fern writes that their own
//! schema rejects, `docs/departures/evidence/invalid-example-values/inventory.tsv`.
//!
//! Every golden comparison holds its golden's rows to what it observes, as it
//! holds the departure ledger's: a recording `crozier generate` writes each
//! rejected value at crozier's line ([`crozier::example_values::RECORD_ENV`]),
//! the comparison pairs that line with Fern's through the engine's alignment,
//! and under [`RECORD_ENV`] records the rows for `just departures-ledger` to
//! merge instead of checking them. No second pass over the corpus is made.

use std::collections::{BTreeMap, BTreeSet};
use std::path::Path;

use crozier::departures::Context;
use crozier::example_values::{mechanism, Disposition, ExampleValue};

use super::departures_ledger::{GoldenLedger, Observed};

/// The inventory, relative to the repository root.
pub const INVENTORY: &str = "docs/departures/evidence/invalid-example-values/inventory.tsv";

/// The inventory's first line.
pub const HEADER: &str =
    "golden\tfile\tline\targument\tfern_value\tconstraint\tmechanism\tdisposition";

/// The recipe that regenerates it, in the same pass as the departure ledger.
pub const REGENERATE: &str = "just departures-ledger";

/// The directory a recording run's comparisons write their rows under.
pub const RECORD_ENV: &str = "CROZIER_RECORD_EXAMPLE_INVENTORY";

/// One inventory row; rows sort by golden, file, line and argument.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
pub struct Row {
    pub golden: String,
    pub file: String,
    pub line: usize,
    pub argument: String,
    pub fern_value: String,
    pub constraint: String,
    pub mechanism: String,
    pub disposition: String,
}

impl Row {
    /// The row as the inventory writes it.
    pub fn render(&self) -> String {
        [
            self.golden.as_str(),
            &self.file,
            &self.line.to_string(),
            &self.argument,
            &self.fern_value,
            &self.constraint,
            &self.mechanism,
            &self.disposition,
        ]
        .join("\t")
    }

    fn parse(line: &str) -> Option<Self> {
        let [golden, file, number, argument, fern_value, constraint, mechanism, disposition] =
            line.split('\t').collect::<Vec<_>>()[..]
        else {
            return None;
        };
        Some(Self {
            golden: golden.to_string(),
            file: file.to_string(),
            line: number.parse().ok().filter(|line| *line > 0)?,
            argument: argument.to_string(),
            fern_value: fern_value.to_string(),
            constraint: constraint.to_string(),
            mechanism: mechanism.to_string(),
            disposition: disposition.to_string(),
        })
    }
}

/// The inventory's rows, or every way its text breaks the format: the header,
/// eight fields per row, a disposition from the vocabulary, a mechanism that is
/// a catalog id or `-`, and rows sorted and unique.
pub fn parse(text: &str) -> Result<Vec<Row>, Vec<String>> {
    let mut lines = text.lines();
    if lines.next() != Some(HEADER) {
        return Err(vec![format!(
            "{INVENTORY}: the first line is not `{HEADER}`"
        )]);
    }
    let mut failures = Vec::new();
    let mut rows: Vec<Row> = Vec::new();
    for line in lines {
        let Some(row) = Row::parse(line) else {
            failures.push(format!(
                "{INVENTORY}: `{line}` is not eight tab-separated fields"
            ));
            continue;
        };
        if Disposition::parse(&row.disposition).is_none() {
            failures.push(format!(
                "{INVENTORY}: `{line}` has no disposition of the vocabulary"
            ));
        }
        if row.mechanism != "-" && !mechanism::NAMED.contains(&row.mechanism.as_str()) {
            failures.push(format!(
                "{INVENTORY}: `{line}` names no mechanism's departure"
            ));
        }
        if rows.last().is_some_and(|last| *last >= row) {
            failures.push(format!("{INVENTORY}: `{line}` is out of order or repeated"));
        }
        rows.push(row);
    }
    if failures.is_empty() {
        Ok(rows)
    } else {
        Err(failures)
    }
}

/// The text of `rows`.
pub fn render(rows: &BTreeSet<Row>) -> String {
    let mut text = format!("{HEADER}\n");
    for row in rows {
        text.push_str(&row.render());
        text.push('\n');
    }
    text
}

/// The committed rows, loaded once per test process.
fn committed() -> &'static [Row] {
    static ROWS: std::sync::OnceLock<Vec<Row>> = std::sync::OnceLock::new();
    ROWS.get_or_init(|| {
        let text = std::fs::read_to_string(crate::repo_root().join(INVENTORY))
            .unwrap_or_else(|error| panic!("{INVENTORY}: {error}"));
        parse(&text).unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
    })
}

/// The directory every `crozier` this process runs records its example
/// values under, one file per output directory.
pub fn records_dir() -> &'static Path {
    static DIR: std::sync::OnceLock<tempfile::TempDir> = std::sync::OnceLock::new();
    DIR.get_or_init(|| tempfile::tempdir().expect("example-value records directory"))
        .path()
}

/// The values a recording `crozier generate` wrote into `out`; empty when it
/// recorded none.
fn recorded(out: &Path) -> Result<Vec<ExampleValue>, String> {
    let path = records_dir().join(crozier::example_values::record_file_name(out));
    let Ok(text) = std::fs::read_to_string(&path) else {
        return Ok(Vec::new());
    };
    text.lines()
        .map(|line| {
            ExampleValue::parse(line, &mechanism::NAMED)
                .ok_or_else(|| format!("{}: `{line}` is not a record", path.display()))
        })
        .collect()
}

/// The inventory rows of crozier's tree `out` against the Fern tree
/// `expected_root`: each recorded value in a file `compared` admits, at Fern's
/// line. Fern's line must hold Fern's value; a repaired value must be one
/// `departures` shows its mechanism's rule applied at, which validated it
/// against the source document.
pub fn observed_rows(
    ledger: &GoldenLedger,
    context: &Context,
    expected_root: &Path,
    out: &Path,
    departures: &[Observed],
    compared: &dyn Fn(&str) -> bool,
) -> Result<BTreeSet<Row>, Vec<String>> {
    let values = recorded(out).map_err(|error| vec![error])?;
    let mut by_file: BTreeMap<&str, Vec<&ExampleValue>> = BTreeMap::new();
    for value in &values {
        if compared(&value.file) {
            by_file.entry(&value.file).or_default().push(value);
        }
    }
    let mut rows = BTreeSet::new();
    let mut failures = Vec::new();
    for (rel, values) in by_file {
        let (Ok(generated), Ok(reference)) = (
            std::fs::read_to_string(out.join(rel)),
            std::fs::read_to_string(expected_root.join(rel)),
        ) else {
            continue;
        };
        let mapped = match crozier::parity::compare_file_with_origins(
            context, rel, &generated, &reference,
        ) {
            Ok(mapped) => mapped.reference_lines,
            Err(error) => {
                failures.push(format!("{rel}: {error}"));
                continue;
            }
        };
        let fern_lines: Vec<&str> = reference.split('\n').collect();
        let crozier_lines: Vec<&str> = generated.split('\n').collect();
        for value in values {
            let Some(fern_line) = mapped.get(value.line - 1).copied().flatten() else {
                failures.push(format!(
                    "{rel}:{}: the comparison pairs crozier's line holding {} with no Fern line",
                    value.line, value.argument
                ));
                continue;
            };
            if !fern_lines[fern_line].contains(&value.fern)
                && !compact(&fern_lines[fern_line..=list_end(&fern_lines, fern_line)].join("\n"))
                    .contains(&compact(&value.fern))
            {
                failures.push(format!(
                    "{rel}:{}: Fern's line {} does not hold {} for {}",
                    value.line,
                    fern_line + 1,
                    value.fern,
                    value.argument
                ));
                continue;
            }
            // A list's departure stands on the line its added items begin, and
            // a one-line list's covers the items it holds, so a repaired value
            // is accounted for by a rejected-example departure on its line or,
            // for a list, anywhere in its lines.
            let end = if value.mechanism == Some(mechanism::ARRAY) {
                list_end(&crozier_lines, value.line - 1) + 1
            } else {
                value.line
            };
            if value.disposition == Disposition::Repaired
                && !departures.iter().any(|(file, line, id)| {
                    file == rel
                        && (value.line..=end).contains(line)
                        && mechanism::NAMED.contains(&id.as_str())
                })
            {
                failures.push(format!(
                    "{rel}:{}: crozier writes {} for {}, but no `{}` departure accounts for it \
                     against the source document",
                    value.line,
                    value.crozier,
                    value.argument,
                    value.mechanism.unwrap_or("-")
                ));
                continue;
            }
            rows.insert(Row {
                golden: ledger.owner_of(rel).0.to_string(),
                file: rel.to_string(),
                line: fern_line + 1,
                argument: value.argument.clone(),
                fern_value: value.fern.clone(),
                constraint: value.constraint.clone(),
                mechanism: value.mechanism.unwrap_or("-").to_string(),
                disposition: value.disposition.as_str().to_string(),
            });
        }
    }
    // And every line a rejected-example departure accounts for holds a
    // repaired value of the inventory: the departure is applied nowhere else.
    for (file, line, id) in departures {
        if !mechanism::ALL.contains(&id.as_str()) || !compared(file) {
            continue;
        }
        let backed = values.iter().any(|value| {
            value.file == *file
                && value.disposition == Disposition::Repaired
                && (value.line == *line
                    || value.mechanism == Some(mechanism::ARRAY)
                        && value.line <= *line
                        && *line <= value.line + 400)
        });
        if !backed {
            failures.push(format!(
                "{file}:{line}: `{id}` is applied where no repaired value of the inventory stands"
            ));
        }
    }
    if failures.is_empty() {
        Ok(rows)
    } else {
        Err(failures)
    }
}

/// `text` with whitespace outside string literals and a comma before a
/// closing bracket dropped: a list spread over lines and its one-line
/// spelling read alike.
fn compact(text: &str) -> String {
    let mut out = String::new();
    let mut quote = None;
    let mut escaped = false;
    for character in text.chars() {
        if let Some(delimiter) = quote {
            out.push(character);
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
        } else if matches!(character, '"' | '\'') {
            quote = Some(character);
            out.push(character);
        } else if matches!(character, ')' | ']' | '}') && out.ends_with(',') {
            out.pop();
            out.push(character);
        } else if !character.is_whitespace() {
            out.push(character);
        }
    }
    out
}

/// The 0-based line the bracket the line `start` first opens closes on, or
/// `start` when it opens none or never closes.
fn list_end(lines: &[&str], start: usize) -> usize {
    let (mut depth, mut quote, mut escaped, mut opened) = (0usize, None, false, false);
    for (index, line) in lines.iter().enumerate().skip(start) {
        for character in line.chars() {
            if let Some(delimiter) = quote {
                if escaped {
                    escaped = false;
                } else if character == '\\' {
                    escaped = true;
                } else if character == delimiter {
                    quote = None;
                }
                continue;
            }
            match character {
                '"' | '\'' => quote = Some(character),
                '[' | '(' | '{' => {
                    depth += 1;
                    opened = true;
                }
                ']' | ')' | '}' => {
                    depth = depth.saturating_sub(1);
                    if opened && depth == 0 {
                        return index;
                    }
                }
                _ => {}
            }
        }
    }
    start
}

/// Hold `observed`, a comparison's rows over the files `compared` admits, to
/// the committed rows of its goldens: one failure per stale and per
/// unrecorded row. Under [`RECORD_ENV`], record them there instead and pass.
pub fn check(
    ledger: &GoldenLedger,
    observed: &BTreeSet<Row>,
    compared: &dyn Fn(&str) -> bool,
) -> Vec<String> {
    let goldens = ledger.goldens();
    if let Some(dir) = std::env::var_os(RECORD_ENV) {
        return match record_to(Path::new(&dir), &goldens, observed) {
            Ok(()) => Vec::new(),
            Err(error) => vec![error],
        };
    }
    let expected: BTreeSet<Row> = committed()
        .iter()
        .filter(|row| {
            goldens.iter().any(|(golden, _)| *golden == row.golden)
                && ledger.owner_of(&row.file).0 == row.golden
                && compared(&row.file)
        })
        .cloned()
        .collect();
    let stale = expected.difference(observed).map(|row| {
        format!(
            "{INVENTORY}: `{}` is stale: the comparison no longer finds that value there — \
             regenerate the inventory with `{REGENERATE}` if that is intended",
            row.render()
        )
    });
    let unrecorded = observed.difference(&expected).map(|row| {
        format!(
            "{INVENTORY}: `{}` is unrecorded: the comparison finds that value, but the \
             inventory has no such row — regenerate it with `{REGENERATE}`",
            row.render()
        )
    });
    stale.chain(unrecorded).collect()
}

/// Write `rows` under `dir`, one directory per golden, with an empty record
/// for each of `goldens` the inventory of compared goldens records, so a
/// golden whose values all went away loses its rows at the merge.
fn record_to(dir: &Path, goldens: &[(&str, bool)], rows: &BTreeSet<Row>) -> Result<(), String> {
    let mut by_golden: BTreeMap<&str, String> = goldens
        .iter()
        .filter(|(_, known)| *known)
        .map(|(golden, _)| (*golden, String::new()))
        .collect();
    for row in rows {
        if let Some(text) = by_golden.get_mut(row.golden.as_str()) {
            text.push_str(&row.render());
            text.push('\n');
        }
    }
    for (golden, text) in by_golden {
        let target = dir.join(golden.replace('/', "%"));
        std::fs::create_dir_all(&target)
            .map_err(|error| format!("{RECORD_ENV}: {}: {error}", target.display()))?;
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

/// Merge the records under `dir` into `root`'s inventory: each recorded
/// golden's rows become exactly what its comparisons recorded; every other
/// golden keeps its rows. Returns the merged text.
pub fn merge_records(root: &Path, dir: &Path) -> Result<String, String> {
    let text =
        std::fs::read_to_string(root.join(INVENTORY)).unwrap_or_else(|_| format!("{HEADER}\n"));
    let current = parse(&text).map_err(|failures| failures.join("\n"))?;
    let mut recorded: BTreeMap<String, BTreeSet<Row>> = BTreeMap::new();
    let entries = std::fs::read_dir(dir).map_err(|error| format!("{}: {error}", dir.display()))?;
    for entry in entries {
        let entry = entry.map_err(|error| format!("{}: {error}", dir.display()))?;
        let golden = entry.file_name().to_string_lossy().replace('%', "/");
        let rows = recorded.entry(golden).or_default();
        let files = std::fs::read_dir(entry.path())
            .map_err(|error| format!("{}: {error}", entry.path().display()))?;
        for file in files {
            let path = file
                .map_err(|error| format!("{}: {error}", entry.path().display()))?
                .path();
            let text = std::fs::read_to_string(&path)
                .map_err(|error| format!("{}: {error}", path.display()))?;
            for line in text.lines() {
                rows.insert(
                    Row::parse(line)
                        .ok_or_else(|| format!("{}: `{line}` is not a row", path.display()))?,
                );
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

/// `just departures-ledger`'s merge of the inventory: what its recording pass
/// wrote under [`RECORD_ENV`], into the committed inventory.
#[test]
#[ignore = "the inventory's regeneration step; run via `just departures-ledger`"]
fn write_example_values_inventory() {
    let root = crate::repo_root();
    let records =
        std::env::var_os(RECORD_ENV).unwrap_or_else(|| panic!("set {RECORD_ENV} to the records"));
    let merged = merge_records(root, Path::new(&records)).unwrap_or_else(|error| panic!("{error}"));
    parse(&merged).unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    std::fs::write(root.join(INVENTORY), merged).expect("write the inventory");
}

/// The committed inventory holds to its format, and every golden it names is
/// one the comparisons read: the rows of a golden no comparison reads could
/// never be checked.
#[test]
fn the_inventory_holds_to_its_format_and_names_only_compared_goldens() {
    let root = crate::repo_root();
    let text = std::fs::read_to_string(root.join(INVENTORY)).expect("the inventory");
    let rows = parse(&text).unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let ledger = crate::departure_ledger();
    let unread: BTreeSet<&str> = rows
        .iter()
        .map(|row| row.golden.as_str())
        .filter(|golden| !ledger.compares(golden))
        .collect();
    assert!(
        unread.is_empty(),
        "{INVENTORY} names goldens no comparison reads: {unread:?}"
    );
    for row in &rows {
        let named = match Disposition::parse(&row.disposition).expect("parsed") {
            Disposition::Repaired => row.mechanism != "-",
            Disposition::DeclaredInSpec | Disposition::OutOfScopeKeyword => row.mechanism == "-",
            Disposition::ResidualUndecidable | Disposition::ResidualUnconstructible => true,
        };
        assert!(
            named,
            "a repaired row names its mechanism's departure, and a value Fern did not \
             construct names none: `{}`",
            row.render()
        );
    }
}

#[test]
fn the_inventory_format_refuses_broken_rows() {
    let row = "g\tREADME.md\t3\tid\t\"id\"\tformat=uuid\tschema-rejected-name-example\trepaired";
    assert_eq!(
        parse(&format!("{HEADER}\n{row}\n")).map(|rows| rows.len()),
        Ok(1)
    );
    for (broken, says) in [
        (format!("{row}\textra"), "eight tab-separated fields"),
        (row.replace("\trepaired", "\tfixed"), "no disposition"),
        (
            row.replace("schema-rejected-name-example", "made-up"),
            "names no mechanism",
        ),
        (format!("{row}\n{row}"), "out of order or repeated"),
    ] {
        let failures = parse(&format!("{HEADER}\n{broken}\n")).unwrap_err();
        assert!(
            failures.iter().any(|failure| failure.contains(says)),
            "{failures:?}"
        );
    }
    assert!(parse("golden\tfile\n").is_err());
}
