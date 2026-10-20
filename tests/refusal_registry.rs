//! In-process sweep of the Fern refusal registry (`docs/fern-refusals/`). The
//! binary e2e (`fern_refusal_classes_hold` and the per-class journeys in
//! `crates/crozier-e2e/tests/e2e.rs`) proves the CLI contract; this drives the same committed
//! documents through the library so the refusal detectors are measured by the
//! fast tier's coverage, and holds the contract every one of them shares:
//!
//! - each class's `probe.yml` is refused as its row's `status` says, naming the
//!   class id and its `crozier_diagnostic` element;
//! - every refusal on any committed registry document names a registered,
//!   evaluated class;
//! - `fern-strict` adds refusals only under `generate` classes, marks every
//!   strict refusal as its cause, and changes no byte of an SDK it allows.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

use crozier::{render_files, GenerateArgs};

const REGISTRY: &str = "docs/fern-refusals";

/// A refusal crozier issued before the refusal classes existed, kept for a
/// document Fern accepts and recorded in its class evaluation (the array header
/// parameter under `list-default-not-array`).
const PRE_CLASS_REFUSALS: &[&str] = &["has an unsupported array schema in Fern's Python generator"];

type Rendered = Result<BTreeMap<String, String>, String>;

fn render(spec: &Path, fern_strict: bool) -> Rendered {
    render_files(GenerateArgs {
        spec: spec.to_path_buf(),
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        fern_strict,
        extra_fields: crozier::settings::ExtraFields::Allow,
        enum_type: crozier::settings::EnumType::PythonEnums,
        default_max_retries: crozier::settings::DEFAULT_MAX_RETRIES,
        layout: crozier::settings::Layout::Packaged,
    })
    .map(|files| {
        files
            .into_iter()
            .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
            .collect()
    })
    .map_err(|error| error.to_string())
}

/// The refusal's own line: what follows the document path in the error.
fn diagnostic<'a>(error: &'a str, spec: &Path) -> &'a str {
    let prefix = format!("{}: ", spec.display());
    error
        .split_once(&prefix)
        .map_or(error, |(_, rest)| rest)
        .trim()
}

struct Class {
    status: String,
    element: String,
}

fn classes(root: &Path) -> BTreeMap<String, Class> {
    let text = std::fs::read_to_string(root.join("classes.tsv")).expect("classes.tsv");
    let mut lines = text.lines();
    let header: Vec<&str> = lines.next().expect("header").split('\t').collect();
    let column = |name: &str| header.iter().position(|h| *h == name).expect(name);
    let (class, status, element) = (
        column("class"),
        column("status"),
        column("crozier_diagnostic"),
    );
    lines
        .map(|line| line.split('\t').collect::<Vec<_>>())
        .map(|row| {
            (
                row[class].to_string(),
                Class {
                    status: row[status].to_string(),
                    element: row[element].to_string(),
                },
            )
        })
        .collect()
}

/// Every committed document under each class directory: the class probe and
/// the side probes and controls its evaluation measured against Fern.
fn documents(root: &Path) -> Vec<(String, PathBuf)> {
    let mut out = Vec::new();
    for entry in std::fs::read_dir(root).expect("registry").flatten() {
        let dir = entry.path();
        if !dir.is_dir() {
            continue;
        }
        let class = entry.file_name().to_string_lossy().into_owned();
        for file in std::fs::read_dir(&dir).expect("class dir").flatten() {
            let path = file.path();
            if path.is_file()
                && matches!(
                    path.extension().and_then(|e| e.to_str()),
                    Some("yml" | "yaml" | "json")
                )
            {
                out.push((class.clone(), path));
            }
        }
    }
    out.sort();
    out
}

/// The registered class a refusal names, or why it names none.
fn refusing_class<'a>(
    line: &str,
    registry: &'a BTreeMap<String, Class>,
) -> Result<Option<(&'a str, &'a Class)>, String> {
    if PRE_CLASS_REFUSALS.iter().any(|known| line.contains(known)) {
        return Ok(None);
    }
    let id = line.split(':').next().unwrap_or_default();
    match registry.get_key_value(id) {
        Some((id, class)) if matches!(class.status.as_str(), "generate" | "refuse") => {
            Ok(Some((id.as_str(), class)))
        }
        Some((_, class)) => Err(format!(
            "names class `{id}`, whose status is `{}`",
            class.status
        )),
        None => Err(format!("names no registered class: {line}")),
    }
}

/// Unevaluated classes promise only a pinned, measured input record.
fn unevaluated_record_failures(root: &Path, id: &str) -> Vec<String> {
    let dir = root.join(id);
    let mut failures = Vec::new();
    if !dir.join("probe.yml").is_file() {
        failures.push(format!("{id}: probe.yml is missing"));
    }
    match std::fs::read_to_string(dir.join("fern-refusal.txt")) {
        Ok(record) => {
            let pair = crozier::emit::certified_fern_pair();
            for field in [
                format!("fern_cli_version: {}", pair.cli),
                format!("fern_python_sdk_version: {}", pair.python_sdk),
            ] {
                if !record.lines().any(|line| line == field) {
                    failures.push(format!("{id}: fern-refusal.txt lacks `{field}`"));
                }
            }
            if !record.lines().any(|line| {
                line.strip_prefix("diagnostic:")
                    .is_some_and(|value| !value.trim().is_empty())
            }) {
                failures.push(format!("{id}: fern-refusal.txt has no diagnostic"));
            }
        }
        Err(error) => failures.push(format!("{id}: fern-refusal.txt: {error}")),
    }
    failures
}

#[test]
fn unevaluated_records_require_the_probe_and_pinned_diagnostic() {
    let root = tempfile::tempdir().unwrap();
    let dir = root.path().join("pending-shape");
    std::fs::create_dir(&dir).unwrap();
    std::fs::write(
        dir.join("fern-refusal.txt"),
        format!(
            "fern_cli_version: {}\nfern_python_sdk_version: {}\ndiagnostic: measured refusal\n",
            crozier::emit::certified_fern_pair().cli,
            crozier::emit::certified_fern_pair().python_sdk
        ),
    )
    .unwrap();
    assert_eq!(
        unevaluated_record_failures(root.path(), "pending-shape"),
        ["pending-shape: probe.yml is missing"]
    );
    std::fs::write(dir.join("probe.yml"), "not yet evaluated").unwrap();
    assert!(unevaluated_record_failures(root.path(), "pending-shape").is_empty());
    std::fs::write(dir.join("fern-refusal.txt"), "diagnostic: \n").unwrap();
    assert_eq!(
        unevaluated_record_failures(root.path(), "pending-shape").len(),
        3
    );
}

/// The classes the registry is retiring: each whose own `probe.yml` a
/// `generates` or `check-only` row of `findings.tsv` names, because Fern at the
/// pin generates from it. Their rows stay until the population is measured
/// again; meanwhile crozier generates their probes in both modes.
fn retiring(root: &Path) -> std::collections::BTreeSet<String> {
    let Ok(text) = std::fs::read_to_string(root.join("findings.tsv")) else {
        return std::collections::BTreeSet::new();
    };
    let mut lines = text.lines();
    let header: Vec<&str> = lines.next().unwrap_or_default().split('\t').collect();
    let column = |name: &str| header.iter().position(|h| *h == name).expect(name);
    let (kind, probe) = (column("kind"), column("probe"));
    lines
        .map(|line| line.split('\t').collect::<Vec<_>>())
        .filter(|row| matches!(row.get(kind), Some(&"generates" | &"check-only")))
        .filter_map(|row| {
            row.get(probe)?
                .strip_prefix(&format!("{REGISTRY}/"))?
                .strip_suffix("/probe.yml")
                .map(str::to_owned)
        })
        .collect()
}

#[test]
fn every_class_probe_has_the_outcome_its_registry_row_states() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR")).join(REGISTRY);
    assert!(!classes(&root).is_empty());
    let failures = class_probe_failures(&root);
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// A retiring class whose probe crozier still refuses fails, naming it; one
/// whose probe crozier generates holds; a `refuse` class no finding names is
/// still held to refusing.
#[test]
fn a_retiring_class_probe_must_generate_in_both_modes() {
    let committed = Path::new(env!("CARGO_MANIFEST_DIR")).join(REGISTRY);
    let root = tempfile::tempdir().unwrap();
    let header = "class\tstatus\tcrozier_diagnostic\n";
    let mut rows = String::new();
    for (id, source) in [
        ("retiring-generated", "object-property-name-collision"),
        ("retiring-still-refused", "type-name-collision"),
        ("type-name-collision", "type-name-collision"),
    ] {
        let dir = root.path().join(id);
        std::fs::create_dir(&dir).unwrap();
        std::fs::copy(
            committed.join(source).join("probe.yml"),
            dir.join("probe.yml"),
        )
        .unwrap();
        rows.push_str(&format!("{id}\trefuse\ttype GetThingResponse\n"));
    }
    std::fs::write(root.path().join("classes.tsv"), format!("{header}{rows}")).unwrap();
    std::fs::write(
        root.path().join("findings.tsv"),
        format!(
            "finding\tkind\tprobe\n\
             retiring-generated-generates\tgenerates\t{REGISTRY}/retiring-generated/probe.yml\n\
             retiring-still-refused-generates\tgenerates\t{REGISTRY}/retiring-still-refused/probe.yml\n"
        ),
    )
    .unwrap();
    let failures = class_probe_failures(root.path());
    let refused = "retiring, but crozier refused: type-name-collision: type GetThingResponse";
    assert_eq!(failures.len(), 2, "{failures:#?}");
    for mode in ["default", "strict"] {
        assert!(
            failures.iter().any(
                |line| line.starts_with(&format!("retiring-still-refused ({mode}): {refused}"))
            ),
            "{failures:#?}"
        );
    }
}

/// Every class probe's outcome against its row: refused or generated as its
/// `status` says, or — for a retiring class — generated in both modes with the
/// same bytes.
fn class_probe_failures(root: &Path) -> Vec<String> {
    let registry = classes(root);
    let retiring = retiring(root);
    let mut failures = Vec::new();
    for (id, class) in &registry {
        let probe = root.join(id).join("probe.yml");
        if class.status == "unevaluated" {
            failures.extend(unevaluated_record_failures(root, id));
            continue;
        }
        if retiring.contains(id) {
            let mut generated = Vec::new();
            for strict in [false, true] {
                let mode = if strict { "strict" } else { "default" };
                match render(&probe, strict) {
                    Ok(files) if !files.is_empty() => generated.push(files),
                    Ok(_) => failures.push(format!("{id} ({mode}): generated no files")),
                    Err(error) => failures.push(format!(
                        "{id} ({mode}): retiring, but crozier refused: {}",
                        diagnostic(&error, &probe)
                    )),
                }
            }
            if let [default, strict] = &generated[..] {
                if default != strict {
                    failures.push(format!("{id}: fern-strict changed the generated SDK"));
                }
            }
            continue;
        }
        if !matches!(class.status.as_str(), "generate" | "refuse") {
            failures.push(format!("{id}: unknown status `{}`", class.status));
            continue;
        }
        for strict in [false, true] {
            let mode = if strict { "strict" } else { "default" };
            match (class.status.as_str(), render(&probe, strict)) {
                ("generate", Ok(files)) if !strict => {
                    if files.is_empty() {
                        failures.push(format!("{id} ({mode}): generated no files"));
                    }
                }
                ("generate" | "refuse", Err(error)) if strict || class.status == "refuse" => {
                    let line = diagnostic(&error, &probe);
                    if !line.starts_with(&format!("{id}: ")) || !line.contains(&class.element) {
                        failures.push(format!(
                            "{id} ({mode}): refusal does not name the class and `{}`: {line}",
                            class.element
                        ));
                    }
                    if strict && !line.contains("fern-strict") {
                        failures.push(format!(
                            "{id} ({mode}): refusal does not name fern-strict: {line}"
                        ));
                    }
                }
                (status, outcome) => failures.push(format!(
                    "{id} ({mode}): status `{status}` but crozier {}",
                    match outcome {
                        Ok(_) => "generated".to_string(),
                        Err(error) => format!("refused: {}", diagnostic(&error, &probe)),
                    }
                )),
            }
        }
    }
    failures
}

fn document_contract_failures(root: &Path) -> Vec<String> {
    let registry = classes(root);
    let documents = documents(root);
    let mut failures = Vec::new();
    for (dir, spec) in &documents {
        if registry
            .get(dir)
            .is_some_and(|class| class.status == "unevaluated")
        {
            failures.extend(unevaluated_record_failures(root, dir));
            continue;
        }
        let name = format!("{dir}/{}", spec.file_name().unwrap().to_string_lossy());
        let default = render(spec, false);
        let strict = render(spec, true);
        for (mode, outcome) in [("default", &default), ("strict", &strict)] {
            if let Err(error) = outcome {
                let line = diagnostic(error, spec);
                match refusing_class(line, &registry) {
                    Err(why) => failures.push(format!("{name} ({mode}): {why}")),
                    Ok(Some((id, class))) if mode == "default" && class.status == "generate" => {
                        failures.push(format!("{name}: `generate` class {id} refused by default"));
                    }
                    Ok(Some((id, _))) if mode == "strict" && !line.contains("fern-strict") => {
                        failures.push(format!(
                            "{name}: strict refusal under {id} omits fern-strict: {line}"
                        ));
                    }
                    Ok(_) => {}
                }
            }
        }
        match (&default, &strict) {
            (Ok(normal), Ok(strict)) if normal != strict => {
                failures.push(format!("{name}: fern-strict changed the generated SDK"));
            }
            (Ok(_), Err(error)) => {
                let line = diagnostic(error, spec);
                if !matches!(refusing_class(line, &registry), Ok(Some((_, class))) if class.status == "generate")
                {
                    failures.push(format!(
                        "{name}: strict-only refusal outside a `generate` class: {line}"
                    ));
                }
            }
            (Err(normal), Err(strict)) => {
                let normal = diagnostic(normal, spec);
                let class = normal.split(':').next().unwrap_or_default();
                if !diagnostic(strict, spec).starts_with(&format!("{class}:")) {
                    failures.push(format!(
                        "{name}: strict refuses under another class than `{normal}`"
                    ));
                }
            }
            (Err(normal), Ok(_)) => {
                failures.push(format!(
                    "{name}: strict generated what default refused: {}",
                    diagnostic(normal, spec)
                ));
            }
            (Ok(_), Ok(_)) => {}
        }
    }
    failures
}

#[test]
fn unevaluated_documents_are_checked_without_rendering() {
    let root = tempfile::tempdir().unwrap();
    let dir = root.path().join("pending-shape");
    std::fs::create_dir(&dir).unwrap();
    let header = "class\tstatus\tcrozier_diagnostic\n";
    let row = "pending-shape\tunevaluated\t—\n";
    std::fs::write(root.path().join("classes.tsv"), format!("{header}{row}")).unwrap();
    std::fs::write(dir.join("probe.yml"), "not yet evaluated\n").unwrap();
    std::fs::copy(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/head-request-body/fern-refusal.txt"),
        dir.join("fern-refusal.txt"),
    )
    .unwrap();
    assert!(document_contract_failures(root.path()).is_empty());
    std::fs::write(
        root.path().join("classes.tsv"),
        format!("{header}{}", row.replace("unevaluated", "refuse")),
    )
    .unwrap();
    assert!(!document_contract_failures(root.path()).is_empty());
    std::fs::write(root.path().join("classes.tsv"), format!("{header}{row}")).unwrap();
    std::fs::remove_file(dir.join("probe.yml")).unwrap();
    assert_eq!(
        unevaluated_record_failures(root.path(), "pending-shape"),
        ["pending-shape: probe.yml is missing"]
    );
}

#[test]
fn every_registry_document_obeys_the_strict_mode_contract() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR")).join(REGISTRY);
    let registry = classes(&root);
    let documents = documents(&root);
    // Side probes and controls measure the detectors beyond their main probes.
    assert!(
        documents.len() > registry.len(),
        "{} documents",
        documents.len()
    );
    let failures = document_contract_failures(&root);
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}
