//! crozier's non-default generator settings against Fern's own output under the
//! same setting.
//!
//! A setting that changes only a few generated files is proven on a targeted set
//! of registered corpora ([`KINDS`]), not on a copy of the whole corpus. Each
//! listed corpus carries an overlay golden beside `expected/`: Fern's output for
//! the same spec and settings with that one setting changed, produced by
//! `scripts/fern-overlay-goldens.sh` exactly as `expected/` is and committed as an
//! overlay of it — only the files whose bytes differ, plus a manifest naming the
//! files Fern does not emit under the setting. The gate rebuilds the full tree
//! and byte-compares crozier's output under the matching flag to it with the
//! corpus's own residuals, the same comparison `assert_corpus_matches` makes
//! against `expected/`.

use std::path::Path;

use super::{
    assert_generated_tree_matches, corpus_golden_ledger, corpus_has_comparable_golden,
    departure_ledger, fixture_dir, generate_corpus_with, registered_diff_corpora, walk_files,
    Corpus,
};

/// The test that byte-compares every overlay golden, listed in
/// `just test-corpus-match` like each corpus's own test.
pub(super) const CORPUS_TEST: &str = "overlay_goldens_match_fern_output";

/// The overlay manifest: provenance plus the `expected/` files Fern omits.
const MANIFEST: &str = ".crozier-overlay.json";

/// One setting proven by overlay goldens.
struct Kind {
    /// The overlay directory beside `expected/`.
    dir: &'static str,
    /// The Fern setting the manifest must record, as `(key, JSON value)`.
    fern_setting: (&'static str, &'static str),
    /// The crozier flags that reproduce it.
    flags: &'static [&'static str],
    /// `scripts/fern-overlay-goldens.sh`'s arguments that regenerate it.
    script_args: &'static str,
    /// The corpora held to it.
    fixtures: &'static [&'static str],
}

/// Every overlay-golden setting, each with the corpora it is proven on.
const KINDS: &[Kind] = &[
    // `enum-type: literals` against Fern with `pydantic_config.enum_type` unset
    // (fern-python-sdk's `literals` default). The corpora together reach every
    // enum shape crozier generates:
    // - `enum-name-sanitization`: values that need sanitizing into member names
    //   (`"0: Active"`) and an inline query-parameter enum of numeric strings;
    // - `groupe-psa`: inline enum variants in composed properties;
    // - `enum-query-param`: an inline query-parameter enum on a nested resource;
    // - `enum-receiver-collision`: members whose names collide with `visit`'s
    //   receiver;
    // - `openfigi.com`: inline property enums, optional and `nullable` ones, and
    //   a path-parameter enum, in a real corpus document.
    Kind {
        dir: "expected-literals",
        fern_setting: ("enum_type", "\"literals\""),
        flags: &["--enum-type", "literals"],
        script_args: "--enum-type literals",
        fixtures: &[
            "enum-name-sanitization",
            "groupe-psa",
            "enum-query-param",
            "enum-receiver-collision",
            "openfigi.com",
            "aws-mobileanalytics",
        ],
    },
    // `default-max-retries: 0` against Fern's `default_max_retries: 0`, which
    // reaches only the root client and the client wrapper: a vendored fixture
    // and a real corpus document.
    Kind {
        dir: "expected-default-max-retries",
        fern_setting: ("default_max_retries", "0"),
        flags: &["--default-max-retries", "0"],
        script_args: "--default-max-retries 0",
        fixtures: &["enum-query-param", "openfigi.com"],
    },
];

/// A validated overlay manifest.
#[derive(Debug)]
struct Overlay {
    /// `expected/` files Fern does not emit under the setting.
    removed: Vec<String>,
}

/// Read and validate `api`'s `kind` overlay manifest; `None` when it has none.
/// The overlay is only meaningful over the golden it was reduced against, so its
/// recorded Fern versions must be the ones `expected/`'s provenance records.
fn read_overlay(kind: &Kind, api: &str) -> Result<Option<Overlay>, String> {
    let root = fixture_dir(api);
    let overlay = root.join(kind.dir);
    if !overlay.exists() {
        return Ok(None);
    }
    let path = overlay.join(MANIFEST);
    let text = std::fs::read_to_string(&path)
        .map_err(|error| format!("{api}: cannot read {}: {error}", path.display()))?;
    let manifest: serde_json::Value = serde_json::from_str(&text)
        .map_err(|error| format!("{api}: invalid {}/{MANIFEST}: {error}", kind.dir))?;
    let (key, value) = kind.fern_setting;
    let value: serde_json::Value = serde_json::from_str(value).expect("a JSON setting value");
    if manifest[key] != value || manifest["base"] != "expected" {
        return Err(format!(
            "{api}: {}/{MANIFEST} must record {key} {value} over base `expected`",
            kind.dir
        ));
    }
    let base_provenance = root.join("expected/.crozier-fern-golden.json");
    if let Ok(text) = std::fs::read_to_string(&base_provenance) {
        let base: serde_json::Value = serde_json::from_str(&text)
            .map_err(|error| format!("{api}: invalid expected/ provenance: {error}"))?;
        if manifest["fern_python_sdk_version"] != base["fern_python_sdk_version"] {
            return Err(format!(
                "{api}: {} was generated by fern-python-sdk {} but expected/ by {}; \
                 regenerate it with scripts/fern-overlay-goldens.sh {} {api}",
                kind.dir,
                manifest["fern_python_sdk_version"],
                base["fern_python_sdk_version"],
                kind.script_args
            ));
        }
    }
    let removed: Vec<String> = manifest["removed"]
        .as_array()
        .ok_or_else(|| format!("{api}: {MANIFEST} has no `removed` list"))?
        .iter()
        .map(|entry| {
            entry
                .as_str()
                .map(str::to_string)
                .ok_or_else(|| format!("{api}: {MANIFEST} `removed` holds a non-string"))
        })
        .collect::<Result<_, _>>()?;
    for rel in &removed {
        if !root.join("expected").join(rel).is_file() {
            return Err(format!(
                "{api}: {MANIFEST} removes {rel}, which expected/ does not have"
            ));
        }
    }
    Ok(Some(Overlay { removed }))
}

/// The full golden of `api` under `kind`: `expected/` minus the removed files,
/// with every overlay file laid over it.
fn materialize(kind: &Kind, api: &str, overlay: &Overlay) -> tempfile::TempDir {
    let tree = tempfile::tempdir().expect("overlay golden tempdir");
    let copy = |from: &Path, rel: &str| {
        let to = tree.path().join(rel);
        std::fs::create_dir_all(to.parent().expect("a file has a parent")).expect("mkdir");
        std::fs::copy(from.join(rel), &to).expect("copy golden file");
    };
    let base = fixture_dir(api).join("expected");
    for rel in walk_files(&base) {
        if !overlay.removed.contains(&rel) {
            copy(&base, &rel);
        }
    }
    let layer = fixture_dir(api).join(kind.dir);
    for rel in walk_files(&layer) {
        if rel != MANIFEST {
            copy(&layer, &rel);
        }
    }
    tree
}

/// Every overlay golden the gate compares: its repository-relative path, the
/// corpus whose residuals it is compared under, and the files in it no
/// comparison reads (its manifest).
pub(super) fn compared() -> Vec<(String, &'static Corpus, Vec<String>)> {
    overlay_corpora()
        .into_iter()
        .map(|(kind, corpus, _)| {
            (
                format!("tests/fixtures/{}/{}", corpus.api, kind.dir),
                corpus,
                vec![MANIFEST.to_string()],
            )
        })
        .collect()
}

/// The ledger rows the `kind` golden of `corpus` is held to: those naming the
/// overlay for a file it carries, and those naming `expected/` for every file
/// it takes from there unchanged — never one `overlay` removes.
fn overlay_golden_ledger(
    kind: &Kind,
    corpus: &Corpus,
    overlay: &Overlay,
) -> Result<super::GoldenLedger, Vec<String>> {
    let base = format!("tests/fixtures/{}/expected", corpus.api);
    let own = walk_files(&fixture_dir(corpus.api).join(kind.dir))
        .into_iter()
        .collect();
    let golden = format!("tests/fixtures/{}/{}", corpus.api, kind.dir);
    Ok(
        corpus_golden_ledger(departure_ledger(), &golden, corpus)?.inherit(
            corpus_golden_ledger(departure_ledger(), &base, corpus)?,
            own,
            &overlay.removed,
        ),
    )
}

/// Every `(kind, corpus, overlay)` the gate compares, validated: each listed
/// corpus is registered with a comparable `expected/` and carries a valid overlay.
fn overlay_corpora() -> Vec<(&'static Kind, &'static Corpus, Overlay)> {
    let corpora: Vec<&'static Corpus> = registered_diff_corpora()
        .into_iter()
        .filter(|corpus| {
            corpus_has_comparable_golden(corpus, &fixture_dir(corpus.api).join("expected"))
                .unwrap_or_else(|error| panic!("{}: {error}", corpus.api))
        })
        .collect();
    let mut all = Vec::new();
    for kind in KINDS {
        for api in kind.fixtures {
            let corpus = corpora
                .iter()
                .find(|corpus| corpus.api == *api)
                .unwrap_or_else(|| {
                    panic!(
                        "{api}: listed for {} but no registered corpus with a golden",
                        kind.dir
                    )
                });
            let overlay = read_overlay(kind, api)
                .unwrap_or_else(|error| panic!("{error}"))
                .unwrap_or_else(|| {
                    panic!(
                        "{api}: has no {}/; run scripts/fern-overlay-goldens.sh {} {api}",
                        kind.dir, kind.script_args
                    )
                });
            all.push((kind, *corpus, overlay));
        }
    }
    all
}

/// Each overlay kind covers exactly its listed corpora: each is a registered
/// corpus with a valid overlay, and no overlay sits outside its list, where no
/// test would read it.
#[test]
fn overlay_goldens_are_exactly_the_targeted_sets() {
    let listed_total: usize = KINDS.iter().map(|kind| kind.fixtures.len()).sum();
    assert_eq!(overlay_corpora().len(), listed_total);
    let fixtures = Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures");
    let names: Vec<String> = std::fs::read_dir(&fixtures)
        .expect("read tests/fixtures")
        .map(|entry| {
            entry
                .expect("fixture entry")
                .file_name()
                .to_string_lossy()
                .into_owned()
        })
        .collect();
    for kind in KINDS {
        let mut on_disk: Vec<&String> = names
            .iter()
            .filter(|name| fixtures.join(name).join(kind.dir).exists())
            .collect();
        on_disk.sort();
        let mut listed: Vec<String> = kind.fixtures.iter().map(|api| (*api).to_string()).collect();
        listed.sort();
        assert_eq!(
            on_disk,
            listed.iter().collect::<Vec<_>>(),
            "a fixture's {}/ is not listed in KINDS, or a listed one is missing",
            kind.dir
        );
    }
}

// llmlint: ignore-block[tests_mirror_real_usage] `read_overlay` and `materialize` are this e2e binary's overlay-golden gate, not crozier code: the CLI and src/ expose no entry point to them, so the test calls them directly to hold the rebuilt tree to its rule.
/// An overlay golden is `expected/` minus the manifest's removed files, with the
/// overlay laid over it: Fern's literal enum modules replace the classes, and
/// every file the overlay does not carry is `expected/`'s own.
#[test]
fn the_literals_golden_is_expected_minus_removed_plus_overlay() {
    let (kind, api) = (&KINDS[0], "openfigi.com");
    assert_eq!(kind.dir, "expected-literals");
    let overlay = read_overlay(kind, api)
        .expect("valid publisher overlay")
        .expect("publisher has an overlay");
    assert_eq!(overlay.removed, ["src/fern/core/enum.py"]);
    let tree = materialize(kind, api, &overlay);
    assert!(!tree.path().join("src/fern/core/enum.py").exists());
    assert!(!tree.path().join(MANIFEST).exists());
    let state =
        std::fs::read_to_string(tree.path().join("src/fern/types/mapping_job_state_code.py"))
            .expect("overlaid enum module");
    assert!(
        state.contains("typing.Literal[")
            && state.contains("\"AB\"")
            && state.contains("\"AC\"")
            && state.contains("typing.Any"),
        "{state}"
    );
    // Unchanged files come from expected/ untouched.
    assert_eq!(
        std::fs::read(tree.path().join("pyproject.toml")).unwrap(),
        std::fs::read(fixture_dir(api).join("expected/pyproject.toml")).unwrap()
    );
}
// llmlint: ignore-end[tests_mirror_real_usage]

/// Fern's `default_max_retries: 0` changes only the root client's fallback and
/// documented default and the client wrappers' parameter default (plus the
/// provenance `.fern/metadata.json`), and removes nothing.
#[test]
fn the_default_max_retries_golden_changes_only_the_clients() {
    let kind = &KINDS[1];
    assert_eq!(kind.dir, "expected-default-max-retries");
    for api in kind.fixtures {
        let overlay = read_overlay(kind, api)
            .expect("valid overlay")
            .expect("an overlay");
        assert!(overlay.removed.is_empty(), "{api}: {:?}", overlay.removed);
        let mut files = walk_files(&fixture_dir(api).join(kind.dir));
        files.sort();
        assert_eq!(
            files,
            [
                MANIFEST,
                ".fern/metadata.json",
                "src/fern/client.py",
                "src/fern/core/client_wrapper.py"
            ]
            .iter()
            .map(|rel| (*rel).to_string())
            .collect::<Vec<_>>(),
            "{api}"
        );
        let tree = materialize(kind, api, &overlay);
        let client = std::fs::read_to_string(tree.path().join("src/fern/client.py")).unwrap();
        assert!(
            client.contains("max_retries if max_retries is not None else 0"),
            "{client}"
        );
        assert!(client.contains("Defaults to 0."), "{client}");
    }
}

/// crozier's output under each setting reproduces Fern's overlay golden
/// byte-for-byte (under the shared comparison engine) for every listed corpus.
/// Corpora run concurrently, and every failure is reported, not only the first.
#[test]
fn overlay_goldens_match_fern_output() {
    let corpora = overlay_corpora();
    assert!(!corpora.is_empty(), "no corpus carries an overlay golden");
    let workers = std::thread::available_parallelism().map_or(2, |n| n.get().div_ceil(2));
    let next = std::sync::atomic::AtomicUsize::new(0);
    let failures = std::sync::Mutex::new(Vec::new());
    std::thread::scope(|scope| {
        for _ in 0..workers {
            scope.spawn(|| loop {
                let index = next.fetch_add(1, std::sync::atomic::Ordering::Relaxed);
                let Some((kind, corpus, overlay)) = corpora.get(index) else {
                    break;
                };
                let outcome = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
                    let golden = materialize(kind, corpus.api, overlay);
                    let ledger = overlay_golden_ledger(kind, corpus, overlay)
                        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
                    let out = generate_corpus_with(corpus, kind.flags);
                    assert_generated_tree_matches(corpus, &ledger, golden.path(), out.path());
                }));
                if let Err(panic) = outcome {
                    let message = panic
                        .downcast_ref::<String>()
                        .cloned()
                        .or_else(|| panic.downcast_ref::<&str>().map(|s| (*s).to_string()))
                        .unwrap_or_default();
                    failures
                        .lock()
                        .expect("failure list")
                        .push(format!("{} {}: {message}", corpus.api, kind.dir));
                }
            });
        }
    });
    let failures = failures.into_inner().expect("failure list");
    assert!(
        failures.is_empty(),
        "{} of {} overlay goldens diverge from Fern:\n{}",
        failures.len(),
        corpora.len(),
        failures.join("\n\n")
    );
}
