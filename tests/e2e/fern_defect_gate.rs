//! The Fern defect registry's contract, driven through the entry points the
//! gates use — [`load_fern_defects`], then the tree comparisons — over a
//! registry, goldens and crozier outputs each test authors itself in a scratch
//! repository. The real registry's own test is the drift check.

use std::path::Path;

use super::fern_defects::{self, Registry};
use super::{
    assert_generated_tree_matches, compared_goldens, corpus_tree_defects, golden_differences,
    golden_tree_failures, load_fern_defects, Corpus, CORPORA, EXHAUSTIVE, QUERY_PARAMETERS,
    WEBFLOW_V2, WEBFLOW_V2_CROZIER_ONLY,
};

/// The authored golden every test compares against, as an entry names it.
const GOLDEN: &str = "docs/openapi-surface/authored-probes/demo/fern-expected";

/// The note every valid entry cites.
const EVIDENCE: &str = "docs/fern-defects/demo-readme.md";

/// Fern's README: the snippet imports a client class the package does not define.
const FERN_README: &str = "# Demo\n\nfrom demo import DemoClient\nclient = DemoClient()\n";

/// crozier's README: the snippet names the class the package defines.
const CROZIER_README: &str = "# Demo\n\nfrom demo import Demo\nclient = Demo()\n";

/// A module both sides write identically.
const CLIENT: &str = "class Demo:\n    pass\n";

/// One `[[defect]]` table over `README.md` in [`GOLDEN`], with `fern` and
/// `crozier` replacing the lines that differ.
fn entry(id: &str, fern: &str, crozier: &str) -> String {
    entry_with(
        id,
        GOLDEN,
        "README.md",
        fern,
        crozier,
        "the snippet imports DemoClient, which the package does not define",
        EVIDENCE,
    )
}

/// One `[[defect]]` table with every key given.
fn entry_with(
    id: &str,
    golden: &str,
    file: &str,
    fern: &str,
    crozier: &str,
    reason: &str,
    evidence: &str,
) -> String {
    format!(
        "[[defect]]\nid = {id:?}\ngap = \"demo-gap\"\ngolden = {golden:?}\nfile = {file:?}\n\
         fern = {fern:?}\ncrozier = {crozier:?}\nreason = {reason:?}\nevidence = {evidence:?}\n\n"
    )
}

/// The entry that accounts for the README difference.
fn valid_entry() -> String {
    entry(
        "readme-imports-undefined-client",
        "from demo import DemoClient\nclient = DemoClient()\n",
        "from demo import Demo\nclient = Demo()\n",
    )
}

/// A scratch repository holding `registry`, the evidence note, and [`GOLDEN`]
/// with Fern's README `fern_readme`.
fn repository(registry: &str, fern_readme: &str) -> tempfile::TempDir {
    let root = tempfile::tempdir().expect("scratch repository");
    write(root.path(), fern_defects::REGISTRY, registry);
    write(
        root.path(),
        EVIDENCE,
        "`python -c 'from demo import DemoClient'` exits 1: ImportError\n",
    );
    write(root.path(), &format!("{GOLDEN}/README.md"), fern_readme);
    write(root.path(), &format!("{GOLDEN}/src/demo/client.py"), CLIENT);
    write(root.path(), fern_defects::INVENTORY, SCRATCH_INVENTORY);
    root
}

/// The scratch repository's inventory: [`GOLDEN`] and the corpus and overlay
/// goldens the corpus-gate tests author, with no carve-out recorded.
const SCRATCH_INVENTORY: &str = r#"{
  "goldens": {
    "docs/openapi-surface/authored-probes/demo/fern-expected": {},
    "tests/fixtures/exhaustive/expected": {},
    "tests/fixtures/exhaustive/expected-literals": {
      "excluded": [".crozier-overlay.json"]
    },
    "tests/fixtures/query-parameters-openapi/expected": {},
    "tests/fixtures/webflow-v2/expected": {}
  }
}
"#;

/// crozier's authored output tree, with its README `readme`.
fn output(readme: &str) -> tempfile::TempDir {
    let out = tempfile::tempdir().expect("authored crozier output");
    write(out.path(), "README.md", readme);
    write(out.path(), "src/demo/client.py", CLIENT);
    out
}

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().expect("a file has a parent")).expect("mkdir");
    std::fs::write(path, text).expect("write authored file");
}

/// Load `root`'s registry as every gate does and compare `out` to [`GOLDEN`]
/// through the probe, authored-probe and hand-written gates' comparison.
fn compare(root: &Path, out: &Path) -> Vec<String> {
    let registry = load_fern_defects(root).unwrap_or_else(|failures| panic!("{failures:?}"));
    let defects = registry
        .tree(GOLDEN, &[])
        .unwrap_or_else(|failures| panic!("{failures:?}"));
    golden_tree_failures(
        "demo",
        "the authored document",
        &defects,
        &root.join(GOLDEN),
        out,
    )
}

/// The load's failures for `registry`, which must refuse it.
fn load_failures(root: &Path) -> Vec<String> {
    load_fern_defects(root).expect_err("the registry must be refused")
}

/// Assert exactly one failure, naming `id` and saying `says`.
fn assert_names(failures: &[String], id: &str, says: &str) {
    assert!(
        failures.len() == 1
            && failures[0].contains(&format!("`{id}`"))
            && failures[0].contains(says),
        "expected one failure naming `{id}` and saying {says:?}: {failures:#?}"
    );
}

/// The repository's own registry holds to its contract against every golden
/// this suite compares.
#[test]
fn fern_defect_registry_holds_to_its_contract() {
    if let Err(failures) = load_fern_defects(Path::new(env!("CARGO_MANIFEST_DIR"))) {
        panic!(
            "{} breaks its contract:\n{}",
            fern_defects::REGISTRY,
            failures.join("\n")
        );
    }
}

#[test]
fn a_valid_entry_makes_the_substituted_golden_match() {
    let root = repository(&valid_entry(), FERN_README);
    let out = output(CROZIER_README);
    assert_eq!(compare(root.path(), out.path()), Vec::<String>::new());
    // Without the entry the same pair is a difference: the substitution is what
    // matches it, and it touches nothing outside the lines it names.
    let bare = repository("", FERN_README);
    let failures = compare(bare.path(), out.path());
    assert!(
        failures.len() == 1 && failures[0].contains("generated README.md differs"),
        "{failures:#?}"
    );
    let drifted = output(&CROZIER_README.replace("# Demo", "# Demo SDK"));
    let failures = compare(root.path(), drifted.path());
    assert!(
        failures.len() == 1 && failures[0].contains("+ # Demo SDK"),
        "{failures:#?}"
    );
}

#[test]
fn a_file_without_a_final_newline_still_ends_a_line() {
    let fern = FERN_README.trim_end();
    let root = repository(&valid_entry(), fern);
    let out = output(CROZIER_README.trim_end());
    assert_eq!(compare(root.path(), out.path()), Vec::<String>::new());
}

#[test]
fn fern_text_absent_from_the_file_fails_naming_the_entry() {
    let root = repository(
        &entry(
            "absent-lines",
            "from demo import Missing\n",
            "from demo import Demo\n",
        ),
        FERN_README,
    );
    let out = output(CROZIER_README);
    assert_names(
        &compare(root.path(), out.path()),
        "absent-lines",
        "occur 0 times",
    );
    // Part of a line is not a line: `import DemoClient` occurs only mid-line.
    let partial = repository(
        &entry("partial-line", "import DemoClient\n", "import Demo\n"),
        FERN_README,
    );
    assert_names(
        &compare(partial.path(), out.path()),
        "partial-line",
        "occur 0 times",
    );
}

#[test]
fn fern_text_occurring_twice_fails_naming_the_entry() {
    let twice = format!("{FERN_README}client = DemoClient()\n");
    let root = repository(
        &entry(
            "repeated-lines",
            "client = DemoClient()\n",
            "client = Demo()\n",
        ),
        &twice,
    );
    let out = output(&format!("{CROZIER_README}client = Demo()\n"));
    assert_names(
        &compare(root.path(), out.path()),
        "repeated-lines",
        "occur 2 times",
    );
}

#[test]
fn an_entry_naming_a_golden_or_file_no_comparison_reads_is_refused() {
    let unread_golden = repository(
        &entry_with(
            "unread-golden",
            "docs/elsewhere/fern-expected",
            "README.md",
            "from demo import DemoClient\n",
            "from demo import Demo\n",
            "the snippet imports DemoClient, which the package does not define",
            EVIDENCE,
        ),
        FERN_README,
    );
    write(
        unread_golden.path(),
        "docs/elsewhere/fern-expected/README.md",
        FERN_README,
    );
    assert_names(
        &load_failures(unread_golden.path()),
        "unread-golden",
        "not a tree any comparison reads",
    );
    let unread_file = repository(
        &entry_with(
            "unread-file",
            GOLDEN,
            "docs/README.md",
            "from demo import DemoClient\n",
            "from demo import Demo\n",
            "the snippet imports DemoClient, which the package does not define",
            EVIDENCE,
        ),
        FERN_README,
    );
    assert_names(
        &load_failures(unread_file.path()),
        "unread-file",
        "is not a file any comparison of",
    );
}

#[test]
fn fern_equal_to_crozier_is_refused() {
    let root = repository(
        &entry(
            "no-difference",
            "from demo import DemoClient\n",
            "from demo import DemoClient",
        ),
        FERN_README,
    );
    assert_names(
        &load_failures(root.path()),
        "no-difference",
        "`fern` equals `crozier`",
    );
}

#[test]
fn an_entry_crozier_no_longer_needs_is_stale() {
    let root = repository(&valid_entry(), FERN_README);
    let out = output(FERN_README);
    assert_names(
        &compare(root.path(), out.path()),
        "readme-imports-undefined-client",
        "the entry is stale",
    );
}

#[test]
fn an_empty_reason_is_refused() {
    for reason in ["", "  ", "two\nlines"] {
        let root = repository(
            &entry_with(
                "no-reason",
                GOLDEN,
                "README.md",
                "from demo import DemoClient\n",
                "from demo import Demo\n",
                reason,
                EVIDENCE,
            ),
            FERN_README,
        );
        assert_names(
            &load_failures(root.path()),
            "no-reason",
            "`reason` is empty",
        );
    }
}

#[test]
fn missing_evidence_is_refused() {
    for evidence in [
        "docs/fern-defects/absent.md",
        "docs/elsewhere.md",
        "docs/fern-defects/../fern-defects/demo-readme.md",
    ] {
        let root = repository(
            &entry_with(
                "no-evidence",
                GOLDEN,
                "README.md",
                "from demo import DemoClient\n",
                "from demo import Demo\n",
                "the snippet imports DemoClient, which the package does not define",
                evidence,
            ),
            FERN_README,
        );
        write(
            root.path(),
            "docs/elsewhere.md",
            "a note outside the directory\n",
        );
        assert_names(&load_failures(root.path()), "no-evidence", "`evidence`");
    }
}

#[test]
fn duplicate_or_unsorted_ids_are_refused() {
    let first = valid_entry();
    let root = repository(&format!("{first}{first}"), FERN_README);
    assert_names(
        &load_failures(root.path()),
        "readme-imports-undefined-client",
        "appears twice",
    );
    let earlier = entry(
        "absent-lines",
        "from demo import Missing\n",
        "from demo import Demo\n",
    );
    let root = repository(&format!("{first}{earlier}"), FERN_README);
    assert_names(&load_failures(root.path()), "absent-lines", "sorted by id");
    let root = repository(
        &entry(
            "Not_A_Slug",
            "from demo import DemoClient\n",
            "from demo import Demo\n",
        ),
        FERN_README,
    );
    assert_names(
        &load_failures(root.path()),
        "Not_A_Slug",
        "lower-kebab slug",
    );
}

#[test]
fn the_loader_admits_exactly_the_eight_string_keys() {
    let valid = valid_entry();
    assert_eq!(fern_defects::parse(&valid).expect("a valid entry").len(), 1);
    assert!(fern_defects::parse("# no entry\n")
        .expect("an empty registry")
        .is_empty());
    for (broken, says) in [
        (
            valid.replace("gap = \"demo-gap\"\n", ""),
            "missing field `gap`",
        ),
        (format!("{valid}owner = \"me\"\n"), "unknown field `owner`"),
        (
            valid.replace("gap = \"demo-gap\"", "gap = 3"),
            "invalid type",
        ),
        (
            valid.replace("[[defect]]", "[[defects]]"),
            "unknown field `defects`",
        ),
    ] {
        let error = fern_defects::parse(&broken).expect_err("a broken entry");
        assert!(error.contains(says), "{says:?} not in {error}");
    }
}

/// A corpus golden in the scratch repository: `api`'s `expected/` holding
/// `file`, with one entry naming it.
fn corpus_repository(api: &str, file: &str) -> (tempfile::TempDir, String) {
    let golden = format!("tests/fixtures/{api}/expected");
    let root = repository(
        &entry_with(
            "carved-out-file",
            &golden,
            file,
            "from demo import DemoClient\nclient = DemoClient()\n",
            "from demo import Demo\nclient = Demo()\n",
            "the snippet imports DemoClient, which the package does not define",
            EVIDENCE,
        ),
        FERN_README,
    );
    write(root.path(), &format!("{golden}/{file}"), FERN_README);
    (root, golden)
}

/// The failures the corpus gate's preflight reports for `c` over `registry`.
fn carve_out_failures(registry: &Registry, golden: &str, c: &Corpus) -> Vec<String> {
    corpus_tree_defects(registry, golden, c).expect_err("the carve-out must be refused")
}

#[test]
fn a_file_also_carved_out_at_file_level_is_refused() {
    // An `unmatched` entry.
    static UNMATCHED: Corpus = Corpus {
        unmatched: &["README.md"],
        ..EXHAUSTIVE
    };
    let (root, golden) = corpus_repository(EXHAUSTIVE.api, "README.md");
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    assert_names(
        &carve_out_failures(&registry, &golden, &UNMATCHED),
        "carved-out-file",
        "also an `unmatched` entry",
    );
    // A crozier-only file.
    let file = WEBFLOW_V2_CROZIER_ONLY[0];
    let (root, golden) = corpus_repository(WEBFLOW_V2.api, file);
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    assert_names(
        &carve_out_failures(&registry, &golden, &WEBFLOW_V2),
        "carved-out-file",
        "also a crozier-only file",
    );
    // A file pinned to crozier's own bytes.
    let (root, golden) = corpus_repository(QUERY_PARAMETERS.api, "README.md");
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    assert_names(
        &carve_out_failures(&registry, &golden, &QUERY_PARAMETERS),
        "carved-out-file",
        "also a file pinned to crozier's own bytes",
    );
    // The same entry over a corpus that carves nothing out is admitted.
    assert!(corpus_tree_defects(&registry, &golden, &EXHAUSTIVE).is_ok());
}

#[test]
fn the_corpus_gate_applies_an_entry_to_its_golden() {
    let (root, golden) = corpus_repository(EXHAUSTIVE.api, "README.md");
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    assert!(CORPORA.iter().any(|corpus| corpus.api == EXHAUSTIVE.api));
    let expected = root.path().join(&golden);
    let out = output(CROZIER_README);
    std::fs::remove_file(out.path().join("src/demo/client.py")).unwrap();
    let defects = corpus_tree_defects(&registry, &golden, &EXHAUSTIVE).expect("no carve-out");
    assert_generated_tree_matches(&EXHAUSTIVE, &defects, &expected, out.path());
    // Without the entry the corpus gate reports the README.
    let bare = corpus_tree_defects(&registry, "tests/fixtures/other/expected", &EXHAUSTIVE)
        .expect("no entry");
    let panic = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
        assert_generated_tree_matches(&EXHAUSTIVE, &bare, &expected, out.path());
    }))
    .expect_err("an unaccounted difference fails the corpus gate");
    let message = panic.downcast_ref::<String>().cloned().unwrap_or_default();
    assert!(
        message.contains("generated README.md does not match"),
        "{message}"
    );
}

#[test]
fn the_flat_and_reporter_comparison_applies_an_entry() {
    let root = repository(&valid_entry(), FERN_README);
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    let expected = root.path().join(GOLDEN);
    let out = output(CROZIER_README);
    let differences = golden_differences(
        &expected,
        out.path(),
        None,
        true,
        registry.tree(GOLDEN, &[]),
    )
    .expect("the entry applies");
    assert!(differences.is_empty(), "{differences:?}");
    let stale = output(FERN_README);
    let error = golden_differences(
        &expected,
        stale.path(),
        None,
        true,
        registry.tree(GOLDEN, &[]),
    )
    .expect_err("a stale entry fails");
    assert!(
        error.contains("`readme-imports-undefined-client`") && error.contains("stale"),
        "{error}"
    );
    let drifted = output(&CROZIER_README.replace("Demo()", "Demo(x=1)"));
    let differences = golden_differences(
        &expected,
        drifted.path(),
        None,
        true,
        registry.tree(GOLDEN, &[]),
    )
    .expect("the entry applies");
    assert!(
        matches!(&differences[..], [(rel, crozier::parity::Difference::Text(Some(diff)))]
            if rel == "README.md" && diff.contains("- client = Demo()\n+ client = Demo(x=1)")),
        "{differences:?}"
    );
}

#[test]
fn an_overlay_takes_base_entries_only_for_the_files_it_inherits() {
    let base = format!("tests/fixtures/{}/expected", EXHAUSTIVE.api);
    let overlay = format!("tests/fixtures/{}/expected-literals", EXHAUSTIVE.api);
    let registry = format!(
        "{}{}",
        entry_with(
            "inherited-readme",
            &base,
            "README.md",
            "from demo import DemoClient\n",
            "from demo import Demo\n",
            "the snippet imports DemoClient, which the package does not define",
            EVIDENCE
        ),
        entry_with(
            "overlaid-client",
            &base,
            "src/demo/client.py",
            "    pass\n",
            "    ...\n",
            "the class body is empty of meaning",
            EVIDENCE
        ),
    );
    let root = repository(&registry, FERN_README);
    write(root.path(), &format!("{base}/README.md"), FERN_README);
    write(root.path(), &format!("{base}/src/demo/client.py"), CLIENT);
    write(
        root.path(),
        &format!("{overlay}/src/demo/client.py"),
        CLIENT,
    );
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    let own = ["src/demo/client.py".to_string()].into_iter().collect();
    let defects = registry.tree(&overlay, &[]).unwrap().inherit(
        registry.tree(&base, &[]).unwrap(),
        &own,
        &[],
    );
    assert_eq!(
        defects.files().into_iter().collect::<Vec<_>>(),
        ["README.md"]
    );
}

/// The keys `docs/matching.md`'s table and the registry's header comment
/// document are exactly the keys the loader admits, in its order.
#[test]
fn the_documented_keys_are_the_loaders() {
    let keys = fern_defects::keys();
    assert_eq!(keys.len(), 8, "{keys:?}");
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let matching = std::fs::read_to_string(root.join("docs/matching.md")).unwrap();
    let section = matching
        .split_once("## Fern defects crozier does not reproduce\n")
        .and_then(|(_, rest)| rest.split("\n## ").next())
        .expect("docs/matching.md has the section");
    let table: Vec<String> = section
        .lines()
        .filter_map(|line| line.strip_prefix("| `"))
        .filter_map(|line| line.split_once('`').map(|(key, _)| key.to_string()))
        .collect();
    assert_eq!(table, keys, "docs/matching.md's key table");
    let registry = std::fs::read_to_string(root.join(fern_defects::REGISTRY)).unwrap();
    let header: Vec<String> = registry
        .lines()
        .filter_map(|line| line.strip_prefix("#   "))
        .filter(|line| !line.starts_with(' '))
        .filter_map(|line| line.split_whitespace().next().map(str::to_string))
        .collect();
    assert_eq!(header, keys, "{}'s header comment", fern_defects::REGISTRY);
}

/// One `[[defect]]` table over `README.md` in [`GOLDEN`] with a fixed reason.
fn readme_entry(id: &str, fern: &str, crozier: &str) -> String {
    entry_with(
        id,
        GOLDEN,
        "README.md",
        fern,
        crozier,
        "the README's lines are wrong on their own terms",
        EVIDENCE,
    )
}

#[test]
fn overlapping_occurrences_are_all_counted() {
    // `x\nx\n` starts at the second and the third line of the three.
    let root = repository(
        &readme_entry("overlapping-lines", "x\nx\n", "y\n"),
        "# Demo\nx\nx\nx\n",
    );
    let out = output("# Demo\ny\nx\n");
    assert_names(
        &compare(root.path(), out.path()),
        "overlapping-lines",
        "occur 2 times",
    );
}

#[test]
fn two_entries_in_one_file_are_both_applied() {
    let registry = format!(
        "{}{}",
        readme_entry("a-heading", "# Demo\n", "# Demo SDK\n"),
        readme_entry("b-client", "client = DemoClient()\n", "client = Demo()\n"),
    );
    let root = repository(&registry, FERN_README);
    let out = output("# Demo SDK\n\nfrom demo import DemoClient\nclient = Demo()\n");
    assert_eq!(compare(root.path(), out.path()), Vec::<String>::new());
}

#[test]
fn an_entry_whose_lines_only_another_substitution_writes_is_absent() {
    // `b-beta`'s lines occur only in what `a-import` writes, never in Fern's file.
    let registry = format!(
        "{}{}",
        readme_entry(
            "a-import",
            "from demo import DemoClient\n",
            "from demo import Demo\nbeta = Beta()\n",
        ),
        readme_entry("b-beta", "beta = Beta()\n", "beta = Demo()\n"),
    );
    let root = repository(&registry, FERN_README);
    let out = output("# Demo\n\nfrom demo import Demo\nbeta = Demo()\nclient = DemoClient()\n");
    assert_names(&compare(root.path(), out.path()), "b-beta", "occur 0 times");
}

#[test]
fn an_entry_whose_second_occurrence_another_substitution_removes_still_occurs_twice() {
    let fern =
        "# Demo\nfrom demo import DemoClient\nclient = DemoClient()\nclient = DemoClient()\n";
    let registry = format!(
        "{}{}",
        readme_entry(
            "a-import",
            "from demo import DemoClient\nclient = DemoClient()\n",
            "from demo import Demo\n",
        ),
        readme_entry("b-client", "client = DemoClient()\n", "client = Demo()\n"),
    );
    let root = repository(&registry, fern);
    let out = output("# Demo\nfrom demo import Demo\nclient = Demo()\n");
    let failures = compare(root.path(), out.path());
    assert!(
        failures
            .iter()
            .any(|failure| failure.contains("`b-client`") && failure.contains("occur 2 times")),
        "{failures:#?}"
    );
}

#[test]
fn overlapping_spans_of_two_entries_are_refused_naming_both() {
    let registry = format!(
        "{}{}",
        readme_entry("a-first", "p\nq\n", "P\n"),
        readme_entry("b-second", "q\nr\n", "R\n"),
    );
    let root = repository(&registry, "# Demo\np\nq\nr\n");
    let out = output("# Demo\nP\nR\n");
    let failures = compare(root.path(), out.path());
    assert!(
        failures.len() == 1
            && failures[0].contains("`a-first`")
            && failures[0].contains("`b-second`")
            && failures[0].contains("overlap"),
        "{failures:#?}"
    );
}

/// One entry over `file` in [`GOLDEN`], whose README lines it quotes.
fn file_entry(id: &str, file: &str) -> String {
    entry_with(
        id,
        GOLDEN,
        file,
        "from demo import DemoClient\n",
        "from demo import Demo\n",
        "the snippet imports DemoClient, which the package does not define",
        EVIDENCE,
    )
}

#[test]
fn a_file_path_escaping_its_golden_is_refused() {
    let scratch = repository("", FERN_README);
    let absolute = scratch.path().join(GOLDEN).join("README.md");
    let absolute = absolute.to_string_lossy().into_owned();
    for file in [
        absolute.as_str(),
        "../fern-expected/README.md",
        "./README.md",
        "src//demo/client.py",
        "src\\demo\\client.py",
    ] {
        let root = repository(&file_entry("escaping-path", file), FERN_README);
        assert_names(
            &load_failures(root.path()),
            "escaping-path",
            "is not a relative path inside its golden",
        );
    }
}

#[test]
fn a_file_no_comparison_reads_is_refused() {
    // The provenance record sits in the golden, but no comparison reads it.
    let root = repository(
        &file_entry("provenance-record", ".crozier-fern-golden.json"),
        FERN_README,
    );
    write(
        root.path(),
        &format!("{GOLDEN}/.crozier-fern-golden.json"),
        "from demo import DemoClient\n",
    );
    assert_names(
        &load_failures(root.path()),
        "provenance-record",
        "is not a file any comparison of",
    );
    // Nor does any comparison read an overlay's manifest.
    let overlay = format!("tests/fixtures/{}/expected-literals", EXHAUSTIVE.api);
    let root = repository(
        &entry_with(
            "overlay-manifest",
            &overlay,
            ".crozier-overlay.json",
            "from demo import DemoClient\n",
            "from demo import Demo\n",
            "the snippet imports DemoClient, which the package does not define",
            EVIDENCE,
        ),
        FERN_README,
    );
    write(
        root.path(),
        &format!("{overlay}/.crozier-overlay.json"),
        "from demo import DemoClient\n",
    );
    assert_names(
        &load_failures(root.path()),
        "overlay-manifest",
        "is not a file any comparison of",
    );
}

#[test]
fn a_carve_out_the_inventory_records_is_refused_at_load() {
    let (root, _) = corpus_repository(EXHAUSTIVE.api, "README.md");
    write(
        root.path(),
        fern_defects::INVENTORY,
        r#"{"goldens": {"tests/fixtures/exhaustive/expected": {"carve_outs": {"unmatched": ["README.md"]}}}}"#,
    );
    assert_names(
        &load_failures(root.path()),
        "carved-out-file",
        "also an `unmatched` entry",
    );
}

#[test]
fn a_file_crozier_did_not_write_fails_naming_the_entry_on_every_path() {
    let root = repository(&valid_entry(), FERN_README);
    let out = output(CROZIER_README);
    std::fs::remove_file(out.path().join("README.md")).unwrap();
    let id = "`readme-imports-undefined-client`";
    let failures = compare(root.path(), out.path());
    assert!(
        failures
            .iter()
            .any(|failure| failure.contains(id) && failure.contains("crozier wrote no README.md")),
        "{failures:#?}"
    );
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    let error = golden_differences(
        &root.path().join(GOLDEN),
        out.path(),
        None,
        true,
        registry.tree(GOLDEN, &[]),
    )
    .expect_err("an entry crozier wrote no file for fails");
    assert!(
        error.contains(id) && error.contains("crozier wrote no README.md"),
        "{error}"
    );
    let (root, golden) = corpus_repository(EXHAUSTIVE.api, "README.md");
    let registry = load_fern_defects(root.path()).expect("a valid registry");
    let defects = corpus_tree_defects(&registry, &golden, &EXHAUSTIVE).expect("no carve-out");
    let empty = tempfile::tempdir().unwrap();
    let panic = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
        assert_generated_tree_matches(
            &EXHAUSTIVE,
            &defects,
            &root.path().join(&golden),
            empty.path(),
        );
    }))
    .expect_err("the corpus gate fails");
    let message = panic.downcast_ref::<String>().cloned().unwrap_or_default();
    assert!(
        message.contains("`carved-out-file`") && message.contains("crozier wrote no README.md"),
        "{message}"
    );
}

#[test]
fn a_comment_only_registry_leaves_every_comparison_as_it_was() {
    let root = repository("# no entry\n", FERN_README);
    let matching = output(FERN_README);
    assert_eq!(compare(root.path(), matching.path()), Vec::<String>::new());
    let differing = output(CROZIER_README);
    let failures = compare(root.path(), differing.path());
    assert!(
        failures.len() == 1 && failures[0].contains("generated README.md differs"),
        "{failures:#?}"
    );
    let registry = load_fern_defects(root.path()).expect("an empty registry");
    let differences = golden_differences(
        &root.path().join(GOLDEN),
        differing.path(),
        None,
        false,
        registry.tree(GOLDEN, &[]),
    )
    .expect("no entry");
    assert!(
        matches!(&differences[..], [(rel, crozier::parity::Difference::Text(None))] if rel == "README.md"),
        "{differences:?}"
    );
}

/// The committed inventory of compared goldens is exactly the one the
/// comparisons' registrations derive, so the in-process comparison of
/// `tests/generation.rs`, which reads it, validates against the same list.
#[test]
fn compared_goldens_inventory_is_current() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let derived = compared_goldens(root).render();
    let path = root.join(fern_defects::INVENTORY);
    if std::env::var_os("CROZIER_UPDATE_COMPARED_GOLDENS").is_some() {
        std::fs::write(&path, &derived).expect("write the inventory");
        return;
    }
    let committed = std::fs::read_to_string(&path).unwrap_or_default();
    assert!(
        committed == derived,
        "{} is not the inventory the registered comparisons derive; regenerate it with \
         `CROZIER_UPDATE_COMPARED_GOLDENS=1 cargo nextest run --locked -E \
         'binary(e2e) and test(compared_goldens_inventory_is_current)'` and commit it",
        fern_defects::INVENTORY
    );
}
