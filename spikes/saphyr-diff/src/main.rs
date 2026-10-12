//! SPIKE (serde-yaml-replacement): differential harness, never landed.
//!
//! Reads this repository's real YAML (and the JSON that reaches the YAML
//! reader) with the crate crozier uses today (`serde_yaml_ng` 0.10) and with
//! `serde-saphyr` 1.3 / `saphyr` 0.2, and prints every difference per document
//! kind: what is read (crozier's own types, the schema-less trees, the whole
//! generation pipeline), what is written (refusal key labels), and what errors
//! say. Run it with `spikes/saphyr-diff/run.sh`; every occurrence goes to the
//! details file it names.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::sync::Mutex;
use std::time::{Duration, Instant};

use crozier::spike_yaml::{options_from_flags, saphyr_tree, set_thread_mode};
use serde_yaml_ng::Value as Ng;

const STACK: usize = 64 * 1024 * 1024;
const SHOWN: usize = 6;

// ---------------------------------------------------------------- reporting

#[derive(Default)]
struct Section {
    documents: usize,
    notes: Vec<String>,
    diffs: BTreeMap<String, Vec<String>>,
}

#[derive(Default)]
struct Report {
    sections: BTreeMap<String, Section>,
}

impl Report {
    fn section(&mut self, kind: &str) -> &mut Section {
        self.sections.entry(kind.to_owned()).or_default()
    }
    fn diff(&mut self, kind: &str, signature: impl Into<String>, occurrence: impl Into<String>) {
        self.section(kind)
            .diffs
            .entry(signature.into())
            .or_default()
            .push(occurrence.into());
    }
    fn note(&mut self, kind: &str, note: impl Into<String>) {
        self.section(kind).notes.push(note.into());
    }
    fn print(&self, details: &Path) {
        let mut full = String::new();
        for (kind, section) in &self.sections {
            println!("\n== {kind} ({} documents/cases) ==", section.documents);
            full.push_str(&format!("\n== {kind} ({} documents/cases) ==\n", section.documents));
            for note in &section.notes {
                println!("  note: {note}");
                full.push_str(&format!("  note: {note}\n"));
            }
            if section.diffs.is_empty() {
                println!("  no differences");
                full.push_str("  no differences\n");
            }
            for (signature, occurrences) in &section.diffs {
                println!("  - [{}x] {signature}", occurrences.len());
                full.push_str(&format!("  - [{}x] {signature}\n", occurrences.len()));
                for (i, occurrence) in occurrences.iter().enumerate() {
                    if i < SHOWN {
                        println!("      {occurrence}");
                    }
                    full.push_str(&format!("      {occurrence}\n"));
                }
                if occurrences.len() > SHOWN {
                    println!("      … {} more in the details file", occurrences.len() - SHOWN);
                }
            }
        }
        std::fs::write(details, full).expect("write details");
        println!("\nevery occurrence: {}", details.display());
    }
}

// ---------------------------------------------------------------- tree diffs

fn kind(v: &Ng) -> &'static str {
    match v {
        Ng::Null => "null",
        Ng::Bool(_) => "bool",
        Ng::Number(n) if n.is_i64() => "int",
        Ng::Number(n) if n.is_u64() => "uint",
        Ng::Number(_) => "float",
        Ng::String(_) => "str",
        Ng::Sequence(_) => "seq",
        Ng::Mapping(_) => "map",
        Ng::Tagged(_) => "tagged",
    }
}

fn short(v: &Ng) -> String {
    let s = match v {
        Ng::Null => "null".to_owned(),
        Ng::Bool(b) => b.to_string(),
        Ng::Number(n) => n.to_string(),
        Ng::String(s) => format!("{s:?}"),
        Ng::Sequence(items) => format!("[{} items]", items.len()),
        Ng::Mapping(map) => format!("{{{} entries}}", map.len()),
        Ng::Tagged(t) => format!("{} {}", t.tag, short(&t.value)),
    };
    if s.chars().count() > 70 {
        format!("{}…", s.chars().take(70).collect::<String>())
    } else {
        s
    }
}

fn path_join(path: &str, key: &Ng) -> String {
    match key {
        Ng::String(s) => format!("{path}/{}", s.replace('~', "~0").replace('/', "~1")),
        other => format!("{path}/<{} {}>", kind(other), short(other)),
    }
}

/// Every leaf difference between `a` (today) and `b`, as (signature, occurrence).
fn diff_tree(a: &Ng, b: &Ng, path: &str, out: &mut Vec<(String, String)>) {
    match (a, b) {
        (Ng::Mapping(ma), Ng::Mapping(mb)) => {
            if ma.len() != mb.len() {
                let ka: Vec<String> = ma.keys().map(short).collect();
                let kb: Vec<String> = mb.keys().map(short).collect();
                let only_a: Vec<&String> = ka.iter().filter(|k| !kb.contains(k)).collect();
                let only_b: Vec<&String> = kb.iter().filter(|k| !ka.contains(k)).collect();
                out.push((
                    "mapping entry count differs".to_owned(),
                    format!(
                        "{path}: {} → {} entries (only before: {only_a:?}; only after: {only_b:?})",
                        ma.len(),
                        mb.len()
                    ),
                ));
            }
            for ((ka, va), (kb, vb)) in ma.iter().zip(mb.iter()) {
                if ka != kb {
                    out.push((
                        format!("key: {} → {}", kind(ka), kind(kb)),
                        format!("{path}: key {} → {}", short(ka), short(kb)),
                    ));
                }
                diff_tree(va, vb, &path_join(path, ka), out);
            }
        }
        (Ng::Sequence(sa), Ng::Sequence(sb)) => {
            if sa.len() != sb.len() {
                out.push((
                    "sequence length differs".to_owned(),
                    format!("{path}: {} → {}", sa.len(), sb.len()),
                ));
            }
            for (i, (va, vb)) in sa.iter().zip(sb.iter()).enumerate() {
                diff_tree(va, vb, &format!("{path}/{i}"), out);
            }
        }
        (Ng::Tagged(ta), Ng::Tagged(tb)) if ta.tag == tb.tag => {
            diff_tree(&ta.value, &tb.value, path, out);
        }
        _ if a == b => {}
        _ => {
            // NaN != NaN: identical spellings are not a difference.
            if let (Ng::Number(x), Ng::Number(y)) = (a, b) {
                if x.as_f64().is_some_and(f64::is_nan) && y.as_f64().is_some_and(f64::is_nan) {
                    return;
                }
            }
            let shown = match (a, b) {
                (Ng::String(x), Ng::String(y)) => string_diff(x, y),
                _ => format!("{} → {}", short(a), short(b)),
            };
            out.push((format!("value: {} → {}", kind(a), kind(b)), format!("{path}: {shown}")));
        }
    }
}

/// Where two strings first part, with a little context on each side.
fn string_diff(x: &str, y: &str) -> String {
    let (cx, cy): (Vec<char>, Vec<char>) = (x.chars().collect(), y.chars().collect());
    let i = cx.iter().zip(cy.iter()).take_while(|(p, q)| p == q).count();
    let window = |c: &[char]| c[i.saturating_sub(12)..(i + 12).min(c.len())].iter().collect::<String>();
    format!(
        "strings part at char {i} of {}/{}: {:?} → {:?}",
        cx.len(),
        cy.len(),
        window(&cx),
        window(&cy)
    )
}

// ---------------------------------------------------------------- readers

fn ng_tree(text: &str) -> Result<Ng, String> {
    serde_yaml_ng::from_str(text).map_err(|e| e.to_string())
}

fn saphyr_direct(text: &str, flags: &[&str]) -> Result<Ng, String> {
    serde_saphyr::from_str_with_options(text, options_from_flags(flags)).map_err(|e| e.to_string())
}

fn saphyr_json(text: &str, flags: &[&str]) -> Result<serde_json::Value, String> {
    serde_saphyr::from_str_with_options(text, options_from_flags(flags)).map_err(|e| e.to_string())
}

fn json_to_ng(v: &serde_json::Value) -> Ng {
    serde_yaml_ng::to_value(v).expect("json converts")
}

fn saphyr_node(text: &str) -> Result<Ng, String> {
    saphyr_tree::load(text).map_err(|e| e.0)
}

fn one_line(s: &str) -> String {
    let s = s.replace('\n', "⏎");
    let width = std::env::var("SAPHYR_DIFF_WIDTH").ok().and_then(|w| w.parse().ok()).unwrap_or(240);
    if s.chars().count() > width {
        format!("{}…", s.chars().take(width).collect::<String>())
    } else {
        s
    }
}

// ---------------------------------------------------------------- inventory

fn repo_root() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../..").canonicalize().unwrap()
}

fn walk(dir: &Path, out: &mut Vec<PathBuf>, skip: &dyn Fn(&Path) -> bool) {
    let Ok(entries) = std::fs::read_dir(dir) else { return };
    let mut entries: Vec<_> = entries.flatten().map(|e| e.path()).collect();
    entries.sort();
    for path in entries {
        if skip(&path) {
            continue;
        }
        if path.is_dir() {
            walk(&path, out, skip);
        } else {
            out.push(path);
        }
    }
}

fn is_doc(path: &Path) -> bool {
    matches!(
        path.extension().and_then(|e| e.to_str()).map(str::to_ascii_lowercase).as_deref(),
        Some("yml" | "yaml" | "json")
    )
}

fn is_yaml(path: &Path) -> bool {
    matches!(
        path.extension().and_then(|e| e.to_str()).map(str::to_ascii_lowercase).as_deref(),
        Some("yml" | "yaml")
    )
}

struct Doc {
    path: PathBuf,
    group: &'static str,
    text: String,
}

fn rel(root: &Path, path: &Path) -> String {
    path.strip_prefix(root).unwrap_or(path).display().to_string()
}

/// Every OpenAPI document (and every other YAML/JSON file) the corpus,
/// feature fixtures and refusal registry commit.
fn inventory(root: &Path) -> (Vec<Doc>, usize) {
    let mut files = Vec::new();
    let mut skipped = 0;
    walk(&root.join("tests/fixtures/corpus-sources"), &mut files, &|_| false);
    let corpus = files.len();
    walk(&root.join("tests/fixtures"), &mut files, &|p| {
        p.ends_with("corpus-sources")
            || p.file_name()
                .and_then(|n| n.to_str())
                .is_some_and(|n| n.starts_with("expected") || n == ".fern")
    });
    walk(&root.join("docs/fern-refusals"), &mut files, &|p| p.ends_with("evaluation-logs"));
    let mut docs = Vec::new();
    for (i, path) in files.into_iter().enumerate() {
        if !is_doc(&path) {
            continue;
        }
        let Ok(text) = std::fs::read_to_string(&path) else {
            skipped += 1;
            continue;
        };
        let group = if i < corpus {
            "corpus-sources"
        } else if path.starts_with(root.join("docs/fern-refusals")) {
            "fern-refusals"
        } else {
            "tests/fixtures"
        };
        docs.push(Doc { path, group, text });
    }
    (docs, skipped)
}

fn looks_openapi(text: &str, path: &Path) -> bool {
    let value = if is_yaml(path) {
        serde_yaml_ng::from_str::<Ng>(text).ok()
    } else {
        serde_json::from_str::<serde_json::Value>(text).ok().map(|v| json_to_ng(&v)).or_else(|| serde_yaml_ng::from_str::<Ng>(text).ok())
    };
    value.is_some_and(|v| v.get("openapi").is_some() || v.get("swagger").is_some())
}

// ---------------------------------------------------------------- parallel map

fn par_map<T: Sync, R: Send>(items: &[T], f: impl Fn(&T) -> R + Sync) -> Vec<R> {
    let next = Mutex::new(0usize);
    let results: Mutex<Vec<Option<R>>> = Mutex::new((0..items.len()).map(|_| None).collect());
    let threads = std::thread::available_parallelism().map_or(4, |n| n.get()).min(12);
    std::thread::scope(|scope| {
        for _ in 0..threads {
            std::thread::Builder::new()
                .stack_size(STACK)
                .spawn_scoped(scope, || loop {
                    let i = {
                        let mut n = next.lock().unwrap();
                        let i = *n;
                        *n += 1;
                        i
                    };
                    if i >= items.len() {
                        break;
                    }
                    let r = f(&items[i]);
                    results.lock().unwrap()[i] = Some(r);
                })
                .unwrap();
        }
    });
    results.into_inner().unwrap().into_iter().map(Option::unwrap).collect()
}

fn on_big_stack<R: Send>(f: impl FnOnce() -> R + Send) -> R {
    std::thread::scope(|s| std::thread::Builder::new().stack_size(STACK).spawn_scoped(s, f).unwrap().join().unwrap())
}

// ---------------------------------------------------------------- kinds

/// The serde-saphyr Options that reproduce today's reads on every real document.
const CANDIDATE: [&str; 4] = ["strict_booleans", "budget=none", "nonfinite=string", "merge=ordinary"];

const TREES: [&str; 3] = ["serde-saphyr→serde_yaml_ng::Value", "serde-saphyr→serde_json::Value", "saphyr::Yaml"];

/// The schema-less trees: today's `serde_yaml_ng::Value` against each candidate.
fn compare_trees(report: &mut Report, kind: &str, root: &Path, docs: &[&Doc], flags: &[&str]) {
    for tree in TREES {
        report.section(&format!("{kind} · tree {tree}")).documents = docs.len();
    }
    let results = par_map(docs, |doc| {
        let mut out: Vec<(String, String, String)> = Vec::new();
        let name = rel(root, &doc.path);
        let before = ng_tree(&doc.text);
        let afters = [
            saphyr_direct(&doc.text, flags),
            saphyr_json(&doc.text, flags).map(|v| json_to_ng(&v)),
            saphyr_node(&doc.text),
        ];
        for (tree, after) in TREES.iter().zip(afters) {
            let section = format!("{kind} · tree {tree}");
            match (&before, after) {
                (Ok(a), Ok(b)) => {
                    let mut d = Vec::new();
                    diff_tree(a, &b, "", &mut d);
                    for (sig, occ) in d {
                        out.push((section.clone(), sig, format!("{name}: {occ}")));
                    }
                }
                (Ok(_), Err(e)) => out.push((section.clone(), "read today, refused after".into(), format!("{name}: {}", one_line(&e)))),
                (Err(e), Ok(_)) => out.push((section.clone(), "refused today, read after".into(), format!("{name}: {}", one_line(e)))),
                (Err(a), Err(b)) => out.push((section.clone(), "refused by both (messages)".into(), format!("{name}: before: {} | after: {}", one_line(a), one_line(&b)))),
            }
        }
        out
    });
    for (section, sig, occ) in results.into_iter().flatten() {
        report.diff(&section, sig, occ);
    }
}

/// `crozier::openapi::load` — the typed read into crozier's own `OpenApi`.
fn compare_load(report: &mut Report, root: &Path, docs: &[&Doc], modes: &[String]) {
    let results = par_map(docs, |doc| {
        let run = |m: &str| {
            set_thread_mode(Some(m));
            let r = crozier::openapi::load(&doc.path).map(|d| format!("{d:#?}")).map_err(|e| e.to_string());
            set_thread_mode(None);
            r
        };
        let before = run("off");
        let afters: Vec<_> = modes.iter().map(|m| (m.clone(), run(m))).collect();
        (rel(root, &doc.path), before, afters)
    });
    for mode in modes {
        report.section(&format!("openapi::load (typed OpenApi) · mode `{mode}`")).documents = docs.len();
    }
    for (name, before, afters) in results {
        for (mode, after) in afters {
            let section = format!("openapi::load (typed OpenApi) · mode `{mode}`");
            record_outcome(report, &section, &name, before.clone(), after, first_line_diff);
        }
    }
}

fn first_line_diff(a: &str, b: &str) -> String {
    let (la, lb): (Vec<&str>, Vec<&str>) = (a.lines().collect(), b.lines().collect());
    let mut shown = Vec::new();
    for i in 0..la.len().max(lb.len()) {
        let (x, y) = (la.get(i).copied().unwrap_or(""), lb.get(i).copied().unwrap_or(""));
        if x != y {
            let context = la[..i.min(la.len())]
                .iter()
                .rev()
                .find(|l| l.trim_end().ends_with('{') && l.contains(':'))
                .map(|l| l.trim())
                .unwrap_or("");
            shown.push(format!("line {} (in `{context}`): {:?} → {:?}", i + 1, x.trim(), y.trim()));
            if shown.len() >= 3 {
                break;
            }
        }
    }
    shown.join("; ")
}

fn record_outcome(
    report: &mut Report,
    section: &str,
    name: &str,
    before: Result<String, String>,
    after: Result<String, String>,
    show: impl Fn(&str, &str) -> String,
) {
    match (before, after) {
        (Ok(a), Ok(b)) if a == b => {}
        (Ok(a), Ok(b)) => report.diff(section, "read differently", format!("{name}: {}", show(&a, &b))),
        (Ok(_), Err(e)) => report.diff(section, "read today, refused after", format!("{name}: after: {}", one_line(&e))),
        (Err(e), Ok(_)) => report.diff(section, "refused today, read after", format!("{name}: before: {}", one_line(&e))),
        (Err(a), Err(b)) if a == b => {}
        (Err(a), Err(b)) => report.diff(section, "error message differs", format!("{name}: before: {} | after: {}", one_line(&a), one_line(&b))),
    }
}

/// A corpus row's staged entry point, exactly as the e2e gate stages it.
fn stage_corpus(root: &Path, name: &str, scratch: &Path) -> Result<PathBuf, String> {
    let out = scratch.join(name);
    let _ = std::fs::remove_dir_all(&out);
    std::fs::create_dir_all(&out).map_err(|e| e.to_string())?;
    let o = std::process::Command::new("python3")
        .arg(root.join("tools/corpus/corpus_sources.py"))
        .args(["prepare", "--fixture", name, "--output"])
        .arg(&out)
        .current_dir(root)
        .output()
        .map_err(|e| e.to_string())?;
    if !o.status.success() {
        return Err(String::from_utf8_lossy(&o.stderr).trim().to_owned());
    }
    Ok(PathBuf::from(String::from_utf8_lossy(&o.stdout).trim()))
}

fn args(spec: &Path, strict: bool) -> crozier::GenerateArgs {
    crozier::GenerateArgs {
        spec: spec.to_path_buf(),
        output: PathBuf::from("/nonexistent/spike-out"),
        package_name: None,
        project_name: None,
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: Default::default(),
        enum_type: Default::default(),
        default_max_retries: 2,
        fern_strict: strict,
        layout: Default::default(),
    }
}

fn render(spec: &Path, strict: bool, mode: &str) -> Result<BTreeMap<PathBuf, String>, String> {
    set_thread_mode(Some(mode));
    let r = crozier::render_files(args(spec, strict))
        .map(|files| files.into_iter().map(|f| (f.path, f.contents)).collect())
        .map_err(|e| e.to_string());
    set_thread_mode(None);
    r
}

fn files_diff(a: &BTreeMap<PathBuf, String>, b: &BTreeMap<PathBuf, String>) -> String {
    let mut parts = Vec::new();
    for path in a.keys().filter(|k| !b.contains_key(*k)) {
        parts.push(format!("only before: {}", path.display()));
    }
    for path in b.keys().filter(|k| !a.contains_key(*k)) {
        parts.push(format!("only after: {}", path.display()));
    }
    for (path, x) in a {
        if let Some(y) = b.get(path) {
            if x != y {
                parts.push(format!("{}: {}", path.display(), first_line_diff(x, y)));
            }
        }
    }
    parts.truncate(4);
    parts.join(" || ")
}

/// End to end: `crozier::render_files` (every refusal, the `$ref` resolver,
/// the IR, the emitter and its `ruff format`) per entry point, plain and
/// `--fern-strict`; the `off` baseline renders once and every mode compares
/// against it.
fn compare_generate(report: &mut Report, entries: &[(String, PathBuf)], modes: &[String]) {
    for mode in modes {
        report.section(&format!("generate (render_files, plain + --fern-strict) · mode `{mode}`")).documents = entries.len();
    }
    let done = std::sync::atomic::AtomicUsize::new(0);
    let results = par_map(entries, |(name, spec)| {
        let mut out = Vec::new();
        for strict in [false, true] {
            let label = format!("{name}{}", if strict { " [strict]" } else { "" });
            let before = render(spec, strict, "off");
            for mode in modes {
                out.push((mode.clone(), label.clone(), before.clone(), render(spec, strict, mode)));
            }
        }
        let n = done.fetch_add(1, std::sync::atomic::Ordering::Relaxed) + 1;
        if n % 25 == 0 || n == entries.len() {
            eprintln!("saphyr-diff: generate {n}/{}", entries.len());
        }
        out
    });
    for (mode, name, before, after) in results.into_iter().flatten() {
        let section = format!("generate (render_files, plain + --fern-strict) · mode `{mode}`");
        match (before, after) {
            (Ok(a), Ok(b)) if a == b => {}
            (Ok(a), Ok(b)) => report.diff(&section, "SDK bytes differ", format!("{name}: {}", files_diff(&a, &b))),
            (Ok(a), Err(e)) => report.diff(&section, "generated today, refused/failed after", format!("{name}: today {} files; after: {}", a.len(), one_line(&e))),
            (Err(e), Ok(b)) => report.diff(&section, "refused/failed today, generated after", format!("{name}: after {} files; today: {}", b.len(), one_line(&e))),
            (Err(a), Err(b)) if a == b => {}
            (Err(a), Err(b)) => report.diff(&section, "refusal/error message differs", format!("{name}: before: {} | after: {}", one_line(&a), one_line(&b))),
        }
    }
}

/// `crozier.yml`: the committed configs plus every field shape and the
/// malformed cases the e2e names.
fn compare_settings(report: &mut Report, root: &Path, mode: &str) {
    let section = format!("crozier.yml (settings::parse) · mode `{mode}`");
    let mut cases: Vec<(String, String)> = Vec::new();
    for p in ["screenshots/crozier.yml", "crates/crozier-e2e/tests/action-fixture/crozier.yml"] {
        cases.push((p.to_owned(), std::fs::read_to_string(root.join(p)).unwrap()));
    }
    let synthetic: &[(&str, &str)] = &[
        ("every field, block style", "spec: ./api.yml\nfern-strict: true\npackage-name: acme\nproject-name: acme-sdk\nclient-class-name: AcmeClient\naudiences: [public, beta]\naudience-strict: false\nlayout: flat\ngenerators:\n  python:\n    output: ./out\n    package-name: acme\n    extra-fields: forbid\n    enum-type: literals\n    default-max-retries: 3\n  extra:\n    type: python\n    output: ./extra\n"),
        ("YAML 1.1 boolean `yes`", "fern-strict: yes\n"),
        ("YAML 1.1 boolean `on`", "audience-strict: on\n"),
        ("boolean `True`", "fern-strict: True\n"),
        ("quoted boolean", "fern-strict: \"true\"\n"),
        ("number as package-name", "package-name: 123\n"),
        ("float as project-name", "project-name: 1.10\n"),
        ("YAML 1.1 bool as package-name", "package-name: no\n"),
        ("enum spelled as bool-ish", "generators:\n  python:\n    extra-fields: allow\n    enum-type: on\n"),
        ("float retries", "generators:\n  python:\n    default-max-retries: 3.0\n"),
        ("octal-looking retries", "generators:\n  python:\n    default-max-retries: 010\n"),
        ("hex retries", "generators:\n  python:\n    default-max-retries: 0x3\n"),
        ("null spec", "spec: ~\n"),
        ("empty document", ""),
        ("comment only", "# nothing\n"),
        ("anchors and aliases", "generators:\n  a: &c\n    output: ./o\n  python: *c\n"),
        ("merge key", "generators:\n  python:\n    <<: {output: ./o}\n    package-name: p\n"),
        ("duplicate key", "spec: a.yml\nspec: b.yml\n"),
        ("tagged scalar", "spec: !!str 123\n"),
        ("broken YAML (e2e)", "generators:\n  python:\n   - not: a map\n"),
        ("unknown field (e2e)", "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    packge-name: oops\n"),
        ("unknown top-level field", "spek: ./api.yml\n"),
        ("bad enum (e2e)", "layout: nested\n"),
        ("bad nested enum (e2e)", "generators:\n  python:\n    layout: nested\n"),
        ("expected a boolean", "fern-strict: maybe\n"),
        ("wrong type: list for string", "spec: [a, b]\n"),
        ("negative retries", "generators:\n  python:\n    default-max-retries: -1\n"),
        ("tab indentation", "generators:\n\tpython: {}\n"),
        ("unterminated quote", "spec: \"abc\n"),
        ("root is a list", "- spec: a\n"),
        ("multi-document", "spec: a\n---\nspec: b\n"),
    ];
    for (n, t) in synthetic {
        cases.push(((*n).to_owned(), (*t).to_owned()));
    }
    report.section(&section).documents = cases.len();
    for (name, text) in cases {
        let run = |m: &str| {
            set_thread_mode(Some(m));
            let r = crozier::settings::parse(&text).map(|c| format!("{c:#?}"));
            set_thread_mode(None);
            r
        };
        let (before, after) = (run("off"), run(mode));
        record_outcome(report, &section, &name, before, after, first_line_diff);
    }
}

fn compare_departures(report: &mut Report, root: &Path, mode: &str) {
    let section = format!("assets/departures.yml (departures::parse) · mode `{mode}`");
    let catalog = std::fs::read_to_string(root.join("assets/departures.yml")).unwrap();
    let first = catalog.find("\n- ").map_or(catalog.clone(), |i| catalog[..i + 1].to_owned());
    let mut cases = vec![("assets/departures.yml".to_owned(), catalog.clone())];
    cases.push(("first entry + unknown key".into(), format!("{first}  extra: x\n")));
    cases.push(("first entry minus `fern`".into(), first.lines().filter(|l| !l.trim_start().starts_with("fern:")).collect::<Vec<_>>().join("\n") + "\n"));
    cases.push(("not a list".into(), "id: x\n".into()));
    cases.push(("broken YAML".into(), "- id: [\n".into()));
    report.section(&section).documents = cases.len();
    for (name, text) in cases {
        let run = |m: &str| {
            set_thread_mode(Some(m));
            let r = crozier::departures::parse(&text).map(|c| format!("{c:#?}")).map_err(|e| e.join(" / "));
            set_thread_mode(None);
            r
        };
        let (before, after) = (run("off"), run(mode));
        record_outcome(report, &section, &name, before, after, first_line_diff);
    }
}

/// Malformed OpenAPI documents through `openapi::load` and `render_files`.
fn compare_errors(report: &mut Report, scratch: &Path, mode: &str) {
    let section = format!("malformed OpenAPI (load + render_files errors) · mode `{mode}`");
    let base = "openapi: 3.0.3\ninfo: {title: probe, version: '1'}\n";
    let ok_tail = "paths:\n  /p:\n    get:\n      operationId: p\n      responses:\n        '200': {description: ok}\n";
    let cases: Vec<(&str, String)> = vec![
        ("broken flow sequence", format!("{base}paths: [unclosed\n")),
        ("tab indentation", format!("{base}paths:\n\t/p: {{}}\n")),
        ("duplicate key", format!("{base}{ok_tail}info: {{title: again, version: '2'}}\n")),
        ("paths is a number", format!("{base}paths: 5\n")),
        ("root is a sequence", "- openapi: 3.0.3\n".into()),
        ("empty file", String::new()),
        ("unterminated quote", format!("{base}paths:\n  \"/p: {{}}\n")),
        ("nullable: 1 (expected a boolean)", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: string, nullable: 1}}\n")),
        ("nullable: yes (YAML 1.1 boolean)", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: string, nullable: yes}}\n")),
        ("nullable: on (YAML 1.1 boolean)", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: string, nullable: on}}\n")),
        ("required: True", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: object, properties: {{a: {{type: string}}}}, required: [a], readOnly: True}}\n")),
        ("openapi unquoted float", "openapi: 3.0\ninfo: {title: probe, version: '1'}\npaths: {}\n".into()),
        ("version is a number", "openapi: 3.0.3\ninfo: {title: probe, version: 1.0}\npaths: {}\n".into()),
        ("missing openapi", "info: {title: probe, version: '1'}\npaths: {}\n".into()),
        ("unknown alias", format!("{base}paths: *nope\n")),
        ("deep nesting (70 levels)", format!("{base}paths: {{}}\nx-deep: {}{}\n", "[".repeat(70), "]".repeat(70))),
        ("deep nesting (130 levels)", format!("{base}paths: {{}}\nx-deep: {}{}\n", "[".repeat(130), "]".repeat(130))),
        ("integer past u64 in maximum", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: integer, maximum: 99999999999999999999999}}\n")),
        ("float past f64::MAX in maximum", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: number, maximum: 1.8e308}}\n")),
        ("merge key in a schema", format!("{base}{ok_tail}components:\n  schemas:\n    B: &b {{type: object, properties: {{a: {{type: string}}}}}}\n    M:\n      <<: *b\n      description: merged\n")),
        ("non-string response code key", format!("{base}paths:\n  /p:\n    get:\n      operationId: p\n      responses:\n        200: {{description: ok}}\n")),
        ("multi-document", format!("{base}{ok_tail}---\nopenapi: 3.1.0\n")),
    ];
    report.section(&section).documents = cases.len();
    for (name, text) in cases {
        let spec = scratch.join(format!("err-{}.yml", name.replace(|c: char| !c.is_ascii_alphanumeric(), "_")));
        std::fs::write(&spec, &text).unwrap();
        for strict in [false, true] {
            let label = format!("{name}{}", if strict { " [strict]" } else { "" });
            let (before, after) = on_big_stack(|| (render(&spec, strict, "off"), render(&spec, strict, mode)));
            // Both generate: compare the SDKs byte for byte, not just their file counts.
            let (before, after) = match (before, after) {
                (Ok(b), Ok(a)) if b != a => (Ok(String::new()), Ok(files_diff(&b, &a))),
                (b, a) => (b.map(|_| String::new()), a.map(|_| String::new())),
            };
            record_outcome(report, &section, &label, before, after, |_, b| format!("SDK bytes differ: {b}"));
        }
    }
}

/// The workflow YAML the tests in `tools/` and `crates/crozier-e2e` walk,
/// keyed on `"on"`.
fn compare_workflows(report: &mut Report, root: &Path) {
    let mut files = Vec::new();
    walk(&root.join(".github"), &mut files, &|_| false);
    files.push(root.join("action.yml"));
    let docs: Vec<Doc> = files
        .into_iter()
        .filter(|p| is_yaml(p))
        .map(|p| Doc { text: std::fs::read_to_string(&p).unwrap(), path: p, group: "workflows" })
        .collect();
    let refs: Vec<&Doc> = docs.iter().collect();
    compare_trees(report, "workflow/action YAML [Options: default]", root, &refs, &[]);
    compare_trees(report, &format!("workflow/action YAML [Options: {}]", CANDIDATE.join(",")), root, &refs, &CANDIDATE);
    let section = "workflow/action YAML · the `on` key";
    report.section(section).documents = docs.len();
    for doc in &docs {
        let name = rel(root, &doc.path);
        // The key at the position today's tree holds `on`, as each reader keys it.
        let Some(position) = ng_tree(&doc.text).ok().and_then(|v| v.as_mapping().and_then(|m| m.keys().position(|k| k.as_str() == Some("on")))) else {
            continue;
        };
        let key_at = |r: Result<Ng, String>| {
            r.ok()
                .and_then(|v| v.as_mapping().and_then(|m| m.keys().nth(position).cloned()))
                .map_or("<unread>".to_owned(), |k| format!("{} {}", kind(&k), short(&k)))
        };
        let json_has_on = |flags: &[&str]| saphyr_json(&doc.text, flags).ok().is_some_and(|v| v.get("on").is_some());
        report.note(
            section,
            format!(
                "{name}: top-level key `on` — today str \"on\"; serde-saphyr→Value {}; serde-saphyr→Value strict_booleans {}; saphyr::Yaml {}; serde-saphyr→serde_json has \"on\": {}",
                key_at(saphyr_direct(&doc.text, &[])),
                key_at(saphyr_direct(&doc.text, &["strict_booleans"])),
                key_at(saphyr_node(&doc.text)),
                json_has_on(&[]),
            ),
        );
    }
}

/// How each reader resolves one scalar spelling, as a value and as a key.
fn scalar_probes(report: &mut Report) {
    let section = "scalar resolution probes (value `x: <s>` and key `<s>: v`)";
    let probes: &[&str] = &[
        "yes", "no", "on", "off", "y", "n", "Yes", "ON", "True", "TRUE", "true", "~", "null", "Null", "",
        "0x1F", "0o17", "017", "1_000", "+1", "1e3", "1.0e+3", ".5", "1:20", "-0",
        "9223372036854775807", "9223372036854775808", "18446744073709551616", "99999999999999999999999",
        "-9223372036854776000", "1.8e308", "-1.8e308", ".inf", ".NaN",
        "2001-12-14t21:59:43.10-05:00", "2024-01-01", "!!str 123", "!!int \"7\"", "!custom foo",
        "'quoted'", "\"200\"", "1.0", "3.0.3",
    ];
    report.section(section).documents = probes.len() * 2;
    let readers: Vec<(&str, Box<dyn Fn(&str) -> Result<Ng, String>>)> = vec![
        ("serde-saphyr→Value", Box::new(|t: &str| saphyr_direct(t, &[]))),
        ("serde-saphyr→Value strict_booleans", Box::new(|t: &str| saphyr_direct(t, &["strict_booleans"]))),
        ("serde-saphyr→serde_json", Box::new(|t: &str| saphyr_json(t, &[]).map(|v| json_to_ng(&v)))),
        ("serde-saphyr→serde_json strict_booleans", Box::new(|t: &str| saphyr_json(t, &["strict_booleans"]).map(|v| json_to_ng(&v)))),
        ("serde-saphyr→serde_json nonfinite=string", Box::new(|t: &str| saphyr_json(t, &["nonfinite=string"]).map(|v| json_to_ng(&v)))),
        ("saphyr::Yaml", Box::new(saphyr_node)),
    ];
    let typed_today = |t: &str| serde_yaml_ng::from_str::<BTreeMap<String, String>>(t).map(|m| format!("{m:?}")).map_err(|e| e.to_string());
    let typed_after = |t: &str| serde_saphyr::from_str::<BTreeMap<String, String>>(t).map(|m| format!("{m:?}")).map_err(|e| one_line(&e.to_string()));
    let show = |r: &Result<Ng, String>, pick: &dyn Fn(&Ng) -> Option<Ng>| match r {
        Ok(v) => pick(v).map_or("<absent>".to_owned(), |x| format!("{} {}", kind(&x), short(&x))),
        Err(e) => format!("<error: {}>", one_line(e).chars().take(90).collect::<String>()),
    };
    for probe in probes {
        for (place, text, pick) in [
            ("value", format!("x: {probe}\n"), Box::new(|v: &Ng| v.get("x").cloned()) as Box<dyn Fn(&Ng) -> Option<Ng>>),
            ("key", format!("{probe}: v\n"), Box::new(|v: &Ng| v.as_mapping().and_then(|m| m.keys().next().cloned()))),
        ] {
            let today = show(&ng_tree(&text), &*pick);
            let mut cells = vec![format!("today {today}")];
            for (name, read) in &readers {
                let after = show(&read(&text), &*pick);
                if after != today {
                    report.diff(section, format!("{name} ({place})"), format!("{probe:?}: {today} → {after}"));
                }
                cells.push(format!("{name} {after}"));
            }
            if place == "value" {
                let (a, b) = (typed_today(&text), typed_after(&text));
                if a != b {
                    report.diff(section, "into a String field (value)", format!("{probe:?}: {a:?} → {b:?}"));
                }
            }
            let _ = cells;
        }
    }
}

/// The one write: `name_label`'s rendering of a non-string mapping key.
fn compare_writes(report: &mut Report, keys: &BTreeMap<String, Ng>) {
    let section = "write · refusal key label (`serde_yaml_ng::to_string` of a non-string key)";
    let mut all = keys.clone();
    for (label, value) in [
        ("synthetic int", Ng::from(200)),
        ("synthetic negative", Ng::from(-1)),
        ("synthetic big uint", Ng::from(u64::MAX)),
        ("synthetic float", Ng::from(1.5)),
        ("synthetic float integral", Ng::from(2.0)),
        ("synthetic float exp", Ng::from(1e300)),
        ("synthetic inf", Ng::from(f64::INFINITY)),
        ("synthetic nan", Ng::from(f64::NAN)),
        ("synthetic true", Ng::Bool(true)),
        ("synthetic null", Ng::Null),
    ] {
        all.insert(label.to_owned(), value);
    }
    report.section(section).documents = all.len();
    for (origin, key) in &all {
        let today = serde_yaml_ng::to_string(key).unwrap_or_default().trim_end().to_owned();
        for (opts_name, opts) in [
            ("default SerializerOptions", serde_saphyr::SerializerOptions::default()),
            ("yaml_12", serde_saphyr::ser_options! { yaml_12: true }),
        ] {
            let after = serde_saphyr::to_string_with_options(key, opts).map(|s| s.trim_end().to_owned()).unwrap_or_else(|e| format!("<error {e}>"));
            if after != today {
                report.diff(section, format!("label differs ({opts_name})"), format!("{origin}: {today:?} → {after:?}"));
            }
        }
    }
}

fn collect_keys(v: &Ng, origin: &str, out: &mut BTreeMap<String, Ng>) {
    match v {
        Ng::Mapping(m) => {
            for (k, val) in m {
                if !k.is_string() {
                    let label = format!("{} {}", kind(k), short(k));
                    out.entry(label).or_insert_with(|| k.clone());
                    let _ = origin;
                }
                collect_keys(val, origin, out);
            }
        }
        Ng::Sequence(s) => s.iter().for_each(|x| collect_keys(x, origin, out)),
        Ng::Tagged(t) => collect_keys(&t.value, origin, out),
        _ => {}
    }
}

const ROUNDS: usize = 15;

/// Parse time of one real document per reader. `webflow-v2/openapi.yml` is the
/// largest real YAML; `github.com/openapi.json` is the largest real document,
/// and the refusal engine and `$ref` resolver read it with the YAML reader.
fn timings(report: &mut Report, root: &Path, rel: &str, rounds: usize) {
    let section = format!("parse time · {rel} (interleaved, {rounds} rounds)");
    let section = section.as_str();
    let text = std::fs::read_to_string(root.join(rel)).unwrap();
    report.section(section).documents = 1;
    report.note(section, format!("{} bytes; build profile `{}`", text.len(), if cfg!(debug_assertions) { "dev (debug — rerun with --profile spike)" } else { "spike (release, no LTO)" }));
    let candidate = options_from_flags(&CANDIDATE);
    let depth128 = options_from_flags(&["strict_booleans", "nonfinite=string", "merge=ordinary", "depth=128"]);
    let runs: Vec<(&str, Box<dyn Fn() -> Result<(), String>>)> = vec![
        ("serde_yaml_ng → serde_yaml_ng::Value (today, schema-less)", Box::new(|| serde_yaml_ng::from_str::<Ng>(&text).map(drop).map_err(|e| e.to_string()))),
        ("serde_yaml_ng → OpenApi (today, typed)", Box::new(|| serde_yaml_ng::from_str::<crozier::openapi::OpenApi>(&text).map(drop).map_err(|e| e.to_string()))),
        ("serde-saphyr (default Options) → OpenApi", Box::new(|| serde_saphyr::from_str::<crozier::openapi::OpenApi>(&text).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("serde-saphyr (candidate Options) → OpenApi", Box::new(|| serde_saphyr::from_str_with_options::<crozier::openapi::OpenApi>(&text, candidate.clone()).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("serde-saphyr (candidate Options, Budget max_depth 128 with nodes/events unlimited) → OpenApi", Box::new(|| serde_saphyr::from_str_with_options::<crozier::openapi::OpenApi>(&text, depth128.clone()).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("serde-saphyr (candidate Options, Budget max_depth 128 with nodes/events unlimited) → serde_json::Value", Box::new(|| serde_saphyr::from_str_with_options::<serde_json::Value>(&text, depth128.clone()).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("serde-saphyr (candidate Options) → serde_json::Value", Box::new(|| serde_saphyr::from_str_with_options::<serde_json::Value>(&text, candidate.clone()).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("serde-saphyr (default Options) → serde_json::Value", Box::new(|| serde_saphyr::from_str::<serde_json::Value>(&text).map(drop).map_err(|e| one_line(&e.to_string())))),
        ("saphyr 0.2 → saphyr::Yaml node tree", Box::new(|| {
            use saphyr::LoadableYamlNode;
            saphyr::Yaml::load_from_str(&text).map(drop).map_err(|e| e.to_string())
        })),
        ("saphyr 0.2 → node tree → serde_yaml_ng::Value (the shim's tree=saphyr conversion)", Box::new(|| saphyr_node(&text).map(drop))),
        ("serde_json → serde_json::Value (JSON only; what openapi::load uses for .json)", Box::new(|| serde_json::from_str::<serde_json::Value>(&text).map(drop).map_err(|e| e.to_string()))),
    ];
    // Interleaved rounds, so load from other work on the host spreads across
    // every reader rather than landing on one; min and median per reader.
    let outcomes: Vec<Result<(), String>> = runs.iter().map(|(_, run)| run()).collect();
    let mut samples: Vec<Vec<Duration>> = vec![Vec::new(); runs.len()];
    for _ in 0..rounds {
        for (i, (_, run)) in runs.iter().enumerate() {
            let t = Instant::now();
            let _ = std::hint::black_box(run());
            samples[i].push(t.elapsed());
        }
    }
    for (((name, _), outcome), mut times) in runs.iter().zip(outcomes).zip(samples) {
        times.sort();
        let ms = |d: Duration| d.as_secs_f64() * 1000.0;
        let (min, median) = (ms(times[0]), ms(times[times.len() / 2]));
        match outcome {
            Ok(()) => report.note(section, format!("{name}: min {min:.1} ms, median {median:.1} ms")),
            Err(e) => report.note(section, format!("{name}: FAILS (min {min:.1} ms to fail): {e}")),
        }
    }
}


// ---------------------------------------------------------------- error wording

/// Today's error text against serde-saphyr's (candidate Options) as it renders
/// by default, and as the `today_wording` code change renders it.
fn compare_error_wording(report: &mut Report) {
    let plain = "error wording · serde-saphyr default rendering (candidate Options)";
    let reworded = "error wording · with the today_wording code change (candidate Options)";
    // The user ruled that errors need only carry what failed and where, not
    // today's text, so the wording adapter is measured only on request.
    let adapter = std::env::var_os("SAPHYR_DIFF_TODAY_WORDING").is_some();
    let base = "openapi: 3.0.3\ninfo: {title: probe, version: '1'}\n";
    let ok_tail = "paths:\n  /p:\n    get:\n      operationId: p\n      responses:\n        '200': {description: ok}\n";
    let openapi: Vec<(&str, String)> = vec![
        ("e2e pagination: x-crozier-pagination: 7", "openapi: 3.0.3\ninfo: {title: Beacons, version: '1'}\npaths:\n  /beacons:\n    get:\n      operationId: listBeacons\n      x-crozier-pagination: 7\n      responses: {'204': {description: ok}}\n".into()),
        ("e2e named media: x-fern-sdk-method-name: [invalid]", format!("{base}paths:\n  /p:\n    post:\n      operationId: p\n      requestBody:\n        content:\n          application/json:\n            x-fern-sdk-method-name: [invalid]\n            schema: {{type: object}}\n      responses:\n        '200': {{description: ok}}\n")),
        ("broken flow sequence", format!("{base}paths: [unclosed\n")),
        ("tab indentation", format!("{base}paths:\n\t/p: {{}}\n")),
        ("duplicate key", format!("{base}{ok_tail}info: {{title: again, version: '2'}}\n")),
        ("paths is a number", format!("{base}paths: 5\n")),
        ("root is a sequence", "- openapi: 3.0.3\n".into()),
        ("unterminated quote", format!("{base}paths:\n  \"/p: {{}}\n")),
        ("nullable: 1 (expected a boolean)", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: string, nullable: 1}}\n")),
        ("nullable: yes", format!("{base}{ok_tail}components:\n  schemas:\n    M: {{type: string, nullable: yes}}\n")),
        ("unknown alias", format!("{base}paths: *nope\n")),
        ("multi-document", format!("{base}{ok_tail}---\nopenapi: 3.1.0\n")),
    ];
    let settings: Vec<(&str, &str)> = vec![
        ("e2e crozier.yml: layout: nested", "layout: nested\n"),
        ("e2e crozier.yml: nested layout", "generators:\n  python:\n    layout: nested\n"),
        ("e2e crozier.yml: broken YAML", "generators:\n  python:\n   - not: a map\n"),
        ("e2e crozier.yml: unknown field", "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    packge-name: oops\n"),
        ("crozier.yml: expected a boolean", "fern-strict: maybe\n"),
        ("crozier.yml: duplicate key", "spec: a.yml\nspec: b.yml\n"),
        ("crozier.yml: list for string", "spec: [a, b]\n"),
        ("crozier.yml: root is a list", "- spec: a\n"),
    ];
    let departures: Vec<(&str, &str)> = vec![
        ("departures: missing field", "- id: x\n  kind: branding\n  trigger: t\n  crozier: c\n  reason: r\n  evidence: e\n"),
        ("departures: unknown field", "- id: x\n  kind: branding\n  trigger: t\n  fern: f\n  crozier: c\n  reason: r\n  evidence: e\n  extra: x\n"),
        ("departures: not a list", "id: x\n"),
    ];
    let mut cases: Vec<(String, Result<(), String>, Result<(), String>, Option<Result<(), String>>)> = Vec::new();
    let flags = &CANDIDATE;
    for (name, text) in &openapi {
        cases.push((
            (*name).to_owned(),
            serde_yaml_ng::from_str::<crozier::openapi::OpenApi>(text).map(drop).map_err(|e| e.to_string()),
            serde_saphyr::from_str_with_options::<crozier::openapi::OpenApi>(text, options_from_flags(flags)).map(drop).map_err(|e| e.to_string()),
            adapter.then(|| crozier::spike_yaml::today_wording::read::<crozier::openapi::OpenApi>(text, flags).map(drop)),
        ));
    }
    for (name, text) in &settings {
        cases.push((
            (*name).to_owned(),
            serde_yaml_ng::from_str::<crozier::settings::FileConfig>(text).map(drop).map_err(|e| e.to_string()),
            serde_saphyr::from_str_with_options::<crozier::settings::FileConfig>(text, options_from_flags(flags)).map(drop).map_err(|e| e.to_string()),
            adapter.then(|| crozier::spike_yaml::today_wording::read::<crozier::settings::FileConfig>(text, flags).map(drop)),
        ));
    }
    for (name, text) in &departures {
        cases.push((
            (*name).to_owned(),
            serde_yaml_ng::from_str::<Vec<crozier::departures::Departure>>(text).map(drop).map_err(|e| e.to_string()),
            serde_saphyr::from_str_with_options::<Vec<crozier::departures::Departure>>(text, options_from_flags(flags)).map(drop).map_err(|e| e.to_string()),
            adapter.then(|| crozier::spike_yaml::today_wording::read::<Vec<crozier::departures::Departure>>(text, flags).map(drop)),
        ));
    }
    report.section(plain).documents = cases.len();
    if adapter {
        report.section(reworded).documents = cases.len();
    }
    for (name, today, after, fixed) in cases {
        let show = |r: &Result<(), String>| match r {
            Ok(()) => "<accepted>".to_owned(),
            Err(e) => one_line(e),
        };
        if after != today {
            // Acceptable when it still says what failed and where (a line and column).
            let located = after.as_ref().err().is_some_and(|e| e.contains("line ") && e.contains(" column "));
            let signature = if located { "differs from today (says what failed and where)" } else { "differs from today WITHOUT a location" };
            report.diff(plain, signature, format!("{name}: today: {} | after: {}", show(&today), show(&after)));
        }
        match fixed {
            Some(fixed) if fixed == today => report.diff(reworded, "reproduces today's text exactly", format!("{name}: {}", show(&today))),
            Some(fixed) => report.diff(reworded, "still differs", format!("{name}: today: {} | after: {}", show(&today), show(&fixed))),
            None => {}
        }
    }
}

// ---------------------------------------------------------------- compatibility fixes

/// The candidate Options as `CROZIER_SPIKE_YAML` flags, without a budget flag.
const BASE: &str = "tree=json,strict_booleans,nonfinite=string,merge=ordinary";

/// Read `text` into `T` through crozier's shim under `mode`, on a big stack.
fn typed<T: serde::de::DeserializeOwned + Send>(text: &str, mode: &str) -> Result<T, String> {
    on_big_stack(|| {
        set_thread_mode(Some(mode));
        let r = crozier::spike_yaml::from_str::<T>(text).map_err(|e| e.to_string());
        set_thread_mode(None);
        r
    })
}

/// Today's outcome, plain serde-saphyr's, and the fix's, per case; the fix
/// reproduces today when it reads the same value or refuses where today does.
fn compare_fix(report: &mut Report, section: &str, fix: &str, rows: Vec<(String, Result<String, String>, Result<String, String>, Result<String, String>)>) {
    report.section(section).documents = rows.len();
    let show = |r: &Result<String, String>| match r {
        Ok(v) => format!("reads {v}"),
        Err(e) => format!("refused: {}", one_line(e)),
    };
    let same = |a: &Result<String, String>, b: &Result<String, String>| match (a, b) {
        (Ok(x), Ok(y)) => x == y,
        (Err(_), Err(_)) => true,
        _ => false,
    };
    for (name, today, plain, fixed) in rows {
        let line = format!("{name}: today {} | serde-saphyr {} | with {fix}: {}", show(&today), show(&plain), show(&fixed));
        let signature = match (same(&today, &plain), same(&today, &fixed)) {
            (true, true) => "same as today without and with the fix",
            (false, true) => "serde-saphyr differs; the fix reproduces today",
            (true, false) => "serde-saphyr matches; the fix BREAKS it",
            (false, false) => "serde-saphyr differs; the fix does NOT reproduce today",
        };
        report.diff(section, signature, line);
    }
}

/// A Budget with `max_depth` N and node/event caps lifted, against today's
/// recursion limit, on flow- and block-nested documents around both limits.
fn compare_depth(report: &mut Report, scratch: &Path) {
    let base = "openapi: 3.0.3\ninfo: {title: probe, version: '1'}\npaths: {}\n";
    let mut cases: Vec<(String, String)> = Vec::new();
    for n in [63usize, 64, 65, 70, 126, 127, 128, 129, 130] {
        cases.push((format!("flow, {n} levels"), format!("{base}x-deep: {}{}\n", "[".repeat(n), "]".repeat(n))));
        let mut block = String::from("x-deep:\n");
        for level in 1..n {
            block.push_str(&"  ".repeat(level));
            block.push_str(if level + 1 == n { "a: 1\n" } else { "a:\n" });
        }
        cases.push((format!("block, {n} levels"), format!("{base}{block}")));
    }
    for depth in [127, 128, 129] {
        let section = format!("compat · nesting depth: Budget max_depth {depth}, nodes/events unlimited (render_files)");
        let mode = format!("{BASE},depth={depth}");
        let rows = cases
            .iter()
            .map(|(name, text)| {
                let spec = scratch.join(format!("depth-{}.yml", name.replace(|c: char| !c.is_ascii_alphanumeric(), "_")));
                std::fs::write(&spec, text).unwrap();
                let run = |m: &str| on_big_stack(|| render(&spec, false, m)).map(|f| format!("{} files", f.len()));
                (name.clone(), run("off"), run(&format!("{BASE},budget=none")), run(&mode))
            })
            .collect();
        compare_fix(report, &section, &format!("depth={depth}"), rows);
    }
}

/// The strict `bool` visitor (`code=bool`) on crozier's real `Option<bool>`
/// fields: `crozier.yml`'s `fern-strict`, a schema's `nullable`, a
/// parameter's `required`.
fn compare_bool_fix(report: &mut Report) {
    let values = ["true", "false", "True", "TRUE", "\"true\"", "'true'", "\"false\"", "yes", "on", "No", "1", "0", "~", "", "!!bool true", "!!bool \"true\"", "!!str true", "maybe"];
    let fixed = format!("{BASE},budget=none,code=bool");
    let plain = format!("{BASE},budget=none");
    let mut rows = Vec::new();
    for v in values {
        let text = format!("fern-strict: {v}\n");
        let read = |m: &str| typed::<crozier::settings::FileConfig>(&text, m).map(|c| format!("{:?}", c.fern_strict));
        rows.push((format!("crozier.yml `fern-strict: {v}`"), read("off"), read(&plain), read(&fixed)));
        let text = format!("openapi: 3.0.3\ninfo: {{title: p, version: '1'}}\npaths: {{}}\ncomponents:\n  schemas:\n    M:\n      type: string\n      nullable: {v}\n  parameters:\n    P: {{name: p, in: query, schema: {{type: string}}}}\n");
        let read = |m: &str| typed::<crozier::openapi::OpenApi>(&text, m).map(|d| format!("{:?}", d.components.schemas["M"].nullable));
        rows.push((format!("schema `nullable: {v}`"), read("off"), read(&plain), read(&fixed)));
        let text = format!("openapi: 3.0.3\ninfo: {{title: p, version: '1'}}\npaths: {{}}\ncomponents:\n  parameters:\n    P:\n      name: p\n      in: query\n      required: {v}\n      schema: {{type: string}}\n");
        let read = |m: &str| typed::<crozier::openapi::OpenApi>(&text, m).map(|d| format!("{:?}", d.components.parameters["P"].required));
        rows.push((format!("parameter `required: {v}`"), read("off"), read(&plain), read(&fixed)));
    }
    compare_fix(report, "compat · strict bool visitor (code=bool) on Option<bool> fields", "code=bool", rows);
}

/// The `String` reader (`code=string`) on crozier's real `String` fields:
/// `info.title` and a departure's `reason`.
fn compare_string_fix(report: &mut Report, root: &Path) {
    let values = ["~", "null", "Null", "NULL", "", "\"\"", "'~'", "!!null ~", "!!int \"7\"", "!!str 7", "!custom x", "1.10", "1e3", "0x1F", "true", "yes", "2024-01-01", "plain text"];
    let fixed = format!("{BASE},budget=none,code=string");
    let plain = format!("{BASE},budget=none");
    let catalog = std::fs::read_to_string(root.join("assets/departures.yml")).unwrap();
    let first: String = catalog.lines().skip_while(|l| !l.starts_with("- ")).take_while({
        let mut seen = false;
        move |l| {
            let start = l.starts_with("- ");
            let keep = !(start && seen);
            seen |= start;
            keep
        }
    }).map(|l| format!("{l}\n")).collect();
    let reason_line = first.lines().find(|l| l.trim_start().starts_with("reason:")).map(str::to_owned);
    let mut rows = Vec::new();
    for v in values {
        let text = format!("openapi: 3.0.3\ninfo:\n  title: {v}\n  version: '1'\npaths: {{}}\n");
        let read = |m: &str| typed::<crozier::openapi::OpenApi>(&text, m).map(|d| format!("{:?}", d.info.title));
        rows.push((format!("OpenAPI `info.title: {v}`"), read("off"), read(&plain), read(&fixed)));
        if let Some(line) = &reason_line {
            // Only a one-line `reason:` can be swapped for the probe value.
            if !line.trim_end().ends_with('>') && !line.trim_end().ends_with('|') {
                let text = first.replacen(line.as_str(), &format!("  reason: {v}"), 1);
                let read = |m: &str| typed::<Vec<crozier::departures::Departure>>(&text, m).map(|d| format!("{:?}", d[0].reason));
                rows.push((format!("departure `reason: {v}`"), read("off"), read(&plain), read(&fixed)));
            }
        }
    }
    compare_fix(report, "compat · String reader (code=string) on String fields", "code=string", rows);
}

// ---------------------------------------------------------------- main

fn main() {
    let only: Vec<String> = std::env::args().skip(1).filter(|a| !a.starts_with("--")).collect();
    let want = |k: &str| only.is_empty() || only.iter().any(|o| o == k);
    let modes: Vec<String> = std::env::var("SAPHYR_DIFF_MODES")
        .unwrap_or_else(|_| "tree=json;tree=saphyr;tree=json,strict_booleans,budget=none,nonfinite=string;tree=saphyr,strict_booleans,budget=none,nonfinite=string".to_owned())
        .split(';')
        .map(str::to_owned)
        .collect();
    // Schema-less trees are compared under serde-saphyr's default Options and
    // under the candidate set that reproduces today's reads.
    let tree_flag_sets: Vec<Vec<&str>> = vec![Vec::new(), CANDIDATE.to_vec()];
    let root = repo_root();
    let scratch = PathBuf::from(std::env::var("SAPHYR_DIFF_SCRATCH").unwrap_or_else(|_| root.join("target/saphyr-diff").display().to_string()));
    std::fs::create_dir_all(&scratch).unwrap();
    let mut report = Report::default();

    let (mut docs, unreadable) = inventory(&root);
    // SAPHYR_DIFF_FILTER: keep only documents (and corpus rows) whose path holds it.
    let filter = std::env::var("SAPHYR_DIFF_FILTER").unwrap_or_default();
    docs.retain(|d| d.path.display().to_string().contains(&filter));
    let openapi: Vec<&Doc> = docs.iter().filter(|d| looks_openapi(&d.text, &d.path)).collect();
    let others: Vec<&Doc> = docs.iter().filter(|d| !looks_openapi(&d.text, &d.path)).collect();
    let count = |g: &str, yaml: bool| openapi.iter().filter(|d| d.group == g && is_yaml(&d.path) == yaml).count();
    println!("saphyr-diff: serde_yaml_ng 0.10.0 vs serde-saphyr 1.3.0 / saphyr 0.2.1");
    println!(
        "inventory: {} OpenAPI documents — corpus-sources {} YAML + {} JSON, tests/fixtures {} YAML + {} JSON, fern-refusals {} YAML + {} JSON; {} other YAML/JSON files (non-OpenAPI: referenced fragments, examples); {} unreadable",
        openapi.len(), count("corpus-sources", true), count("corpus-sources", false), count("tests/fixtures", true), count("tests/fixtures", false), count("fern-refusals", true), count("fern-refusals", false), others.len(), unreadable
    );
    println!("modes (end-to-end + typed): {modes:?}; schema-less trees under default Options and [{}]", CANDIDATE.join(","));

    if want("trees") {
        let yaml: Vec<&Doc> = openapi.iter().copied().filter(|d| is_yaml(&d.path)).collect();
        let json: Vec<&Doc> = openapi.iter().copied().filter(|d| !is_yaml(&d.path)).collect();
        for flags in &tree_flag_sets {
            let label = |kind: &str| format!("{kind} [Options: {}]", if flags.is_empty() { "default".to_owned() } else { flags.join(",") });
            compare_trees(&mut report, &label("OpenAPI YAML documents"), &root, &yaml, flags);
            compare_trees(&mut report, &label("OpenAPI JSON documents read by the YAML reader"), &root, &json, flags);
            compare_trees(&mut report, &label("non-OpenAPI YAML/JSON fragments ($ref targets, examples)"), &root, &others, flags);
        }
    }
    if want("writes") {
        let mut keys = BTreeMap::new();
        for d in &openapi {
            if let Ok(v) = ng_tree(&d.text) {
                collect_keys(&v, &rel(&root, &d.path), &mut keys);
            }
        }
        compare_writes(&mut report, &keys);
    }
    if want("load") {
        compare_load(&mut report, &root, &openapi, &modes);
    }
    if want("generate") {
        let mut entries: Vec<(String, PathBuf)> = Vec::new();
        let mut names: Vec<String> = std::fs::read_dir(root.join("tests/fixtures/corpus-sources"))
            .unwrap()
            .flatten()
            .filter(|e| e.path().is_dir())
            .map(|e| e.file_name().to_string_lossy().into_owned())
            .filter(|n| filter.is_empty() || n.contains(&filter) || filter.contains(n.as_str()))
            .collect();
        names.sort();
        let staged = par_map(&names, |n| (n.clone(), stage_corpus(&root, n, &scratch.join("staged"))));
        let mut unstaged = 0;
        for (n, s) in staged {
            match s {
                Ok(p) => entries.push((format!("corpus {n}"), p)),
                Err(e) => {
                    unstaged += 1;
                    report.note("generate inventory", format!("corpus {n} not staged: {}", one_line(&e)));
                }
            }
        }
        let corpus = entries.len();
        for d in openapi.iter().filter(|d| d.group != "corpus-sources") {
            entries.push((rel(&root, &d.path), d.path.clone()));
        }
        report.section("generate inventory").documents = entries.len();
        report.note("generate inventory", format!("{corpus} staged corpus entry points ({unstaged} not staged), {} feature/refusal fixture documents", entries.len() - corpus));
        compare_generate(&mut report, &entries, &modes);
    }
    if want("errors") {
        for mode in &modes {
            compare_errors(&mut report, &scratch, mode);
        }
    }
    if want("settings") {
        for mode in &modes {
            compare_settings(&mut report, &root, mode);
            compare_departures(&mut report, &root, mode);
        }
    }
    if want("workflows") {
        compare_workflows(&mut report, &root);
    }
    if want("wording") {
        compare_error_wording(&mut report);
    }
    if want("probes") {
        scalar_probes(&mut report);
    }
    if want("compat") {
        compare_depth(&mut report, &scratch);
        compare_bool_fix(&mut report);
        compare_string_fix(&mut report, &root);
    }
    if want("timing") {
        timings(&mut report, &root, "tests/fixtures/corpus-sources/webflow-v2/openapi.yml", ROUNDS);
        on_big_stack(|| timings(&mut report, &root, "tests/fixtures/corpus-sources/github.com/openapi.json", 7));
    }
    report.print(&scratch.join("details.txt"));
}
