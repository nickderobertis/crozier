//! Text rendering is deferred until the ledger accepts the comparison, and
//! consumed one file at a time. The verdict never depends on these limits.
use super::*;

// At most 128 KiB of normalized input and 1,000,000 u32 LCS cells (4 MiB).
// Both limits matter: long lines bound output bytes, short lines bound alignment.
const MAX_TEXT_BYTES: usize = 128 * 1024;
const MAX_CELLS: usize = 1_000_000;

pub(super) fn print(
    differences: &[(String, Difference)],
    unmatched: &std::collections::HashSet<&str>,
    reference: &Path,
    generated: &Path,
    source: Option<&Path>,
    text: bool,
) {
    if !text || differences.is_empty() {
        print_fixture_differences(differences, unmatched);
        return;
    }
    let context = Context::from_trees(reference, generated);
    let context = match source {
        Some(source) => {
            context.with_source_document(crozier::openapi::load(source).expect("validated source"))
        }
        None => context,
    };
    for (rel, difference) in differences {
        let rendered = if matches!(difference, Difference::Text(None)) {
            render(&context, rel, reference, generated)
                .map(|diff| Difference::Text(Some(diff)))
                .unwrap_or_else(Difference::Processing)
        } else {
            difference.clone()
        };
        print_fixture_differences(&[(rel.clone(), rendered)], unmatched);
    }
}

fn render(
    context: &Context,
    rel: &str,
    reference: &Path,
    generated: &Path,
) -> Result<String, String> {
    let read =
        |root: &Path| std::fs::read_to_string(root.join(rel)).map_err(|error| error.to_string());
    let compared =
        parity::compare_file_with_origins(context, rel, &read(generated)?, &read(reference)?)?;
    let Some((reference, generated)) = &compared.comparison.residual else {
        return Ok(String::new());
    };
    let (left, right) = (reference.lines().count(), generated.lines().count());
    if reference.len().saturating_add(generated.len()) > MAX_TEXT_BYTES
        || left
            .saturating_add(1)
            .saturating_mul(right.saturating_add(1))
            > MAX_CELLS
    {
        return Ok(format!(
            "  Unified diff omitted: {} normalized input line(s) (Fern: {left}; crozier: {right}); limit {MAX_TEXT_BYTES} input bytes / {MAX_CELLS} alignment cells.\n",
            left.saturating_add(right),
        ));
    }
    Ok(compared.diff().unwrap_or_default())
}

/// A tree input seam on the reporter's own subprocess entry point: no generator
/// can predictably produce arbitrarily large, unrelated synthetic text files.
/// It uses the same comparison engine and rendering path as generated corpora.
// llmlint: ignore[tests_mirror_real_usage] The task explicitly requires synthetic corpora through report_fixture_diffs's own subprocess entry point: a real generator cannot emit arbitrarily large unrelated text corpora. This seam uses the real filesystem, parity engine, ledger check and renderer; source_aware_report_generates_and_recovers also generates a real SDK against a committed Fern golden. The optional removal models a file disappearing between verdict and rendering.
pub(super) fn synthetic_report(text: bool) -> bool {
    let Some(root) = std::env::var_os("CROZIER_TEST_DIFF_TREES") else {
        return false;
    };
    let root = PathBuf::from(root);
    let reference = root.join("reference");
    let generated = root.join("generated");
    let source = root.join("openapi.yml");
    let source = source.is_file().then_some(source);
    if !generated.exists() {
        probe_command(
            source.as_deref().expect("generation needs a spec"),
            &generated,
        )
        .assert()
        .success();
    }
    let golden = std::fs::read_to_string(root.join("golden.txt"))
        .unwrap_or_else(|_| "synthetic".to_string());
    let differences = golden_differences(
        &reference,
        &generated,
        None,
        false,
        departure_ledger().golden(golden.trim(), &[]),
        source.as_deref(),
    )
    .expect("ledger-validated comparison");
    if let Ok(rel) = std::fs::read_to_string(root.join("remove-before-render")) {
        std::fs::remove_file(generated.join(rel.trim())).unwrap();
    }
    println!("\n=== synthetic ===");
    print(
        &differences,
        &std::collections::HashSet::new(),
        &reference,
        &generated,
        source.as_deref(),
        text,
    );
    println!("\n{} {DIFFS_SUMMARY}.", differences.len());
    true
}

#[test]
fn small_report_preserves_text_and_names_missing_files() {
    let root = tempfile::tempdir().unwrap();
    for (side, text) in [("reference", "old\n"), ("generated", "new\n")] {
        std::fs::create_dir(root.path().join(side)).unwrap();
        std::fs::write(root.path().join(side).join("changed.txt"), text).unwrap();
    }
    std::fs::write(root.path().join("reference/missing.txt"), "missing").unwrap();
    let output = reporter(root.path()).output().unwrap();
    assert!(output.status.success());
    let report = String::from_utf8(output.stdout).unwrap();
    assert!(
        report.contains("- old\n+ new\n\nUnexplained original crozier line(s): 1\n"),
        "{report}"
    );
    assert!(report.contains("--- missing.txt [REGRESSION"), "{report}");
    assert!(
        report.contains("Crozier did not emit this Fern file."),
        "{report}"
    );
    assert!(!report.contains("omitted"), "{report}");
}

#[test]
fn byte_limit_reports_omitted_long_lines() {
    let root = tempfile::tempdir().unwrap();
    for (side, character) in [("reference", "r"), ("generated", "g")] {
        std::fs::create_dir(root.path().join(side)).unwrap();
        std::fs::write(
            root.path().join(side).join("long.txt"),
            character.repeat(MAX_TEXT_BYTES),
        )
        .unwrap();
    }
    let output = reporter(root.path()).output().unwrap();
    assert!(output.status.success());
    let report = String::from_utf8(output.stdout).unwrap();
    assert!(report.contains("--- long.txt [REGRESSION"), "{report}");
    assert!(
        report.contains("Unified diff omitted: 2 normalized input line(s) (Fern: 1; crozier: 1)"),
        "{report}"
    );
    assert!(report.len() < 2048, "long lines escaped the byte limit");
}

#[test]
fn source_aware_report_generates_and_recovers() {
    let root = tempfile::tempdir().unwrap();
    let golden = "docs/fern-measurements/examples-docs/marina-dock-refs/fern-expected";
    copy_dir(&repo_root().join(golden), &root.path().join("reference"));
    std::fs::copy(
        repo_root().join("docs/fern-measurements/examples-docs/marina-dock-refs/openapi.yml"),
        root.path().join("openapi.yml"),
    )
    .unwrap();
    std::fs::write(root.path().join("golden.txt"), golden).unwrap();
    let md = root.path().join("reference/reference.md");
    let original = std::fs::read_to_string(&md).unwrap();
    std::fs::write(
        &md,
        original.replace("**dock_id_or_code:** `str`", "**dock_id_or_code:** `int`"),
    )
    .unwrap();
    let run = |summary| {
        // Regenerate in the reporter process, including its example records.
        let generated = root.path().join("generated");
        if generated.exists() {
            std::fs::remove_dir_all(generated).unwrap();
        }
        let mut command = reporter(root.path());
        if summary {
            command.env("CROZIER_DIFF_SUMMARY_ONLY", "1");
        }
        let output = command.output().unwrap();
        let report = String::from_utf8(output.stdout).unwrap();
        assert!(output.status.success(), "{report}");
        report
    };
    let report = run(false);
    assert!(report.contains("--- reference.md [REGRESSION"), "{report}");
    assert!(report.contains("- **dock_id_or_code:** `int`"), "{report}");
    assert!(report.contains("+ **dock_id_or_code:** `str`"), "{report}");
    assert!(
        !report.contains("northbasin"),
        "source-dependent example departure leaked: {report}"
    );
    assert!(
        report.contains("Unexplained original crozier line(s):"),
        "{report}"
    );
    assert!(report.contains(&format!("1 {DIFFS_SUMMARY}")), "{report}");
    let summary = run(true);
    assert!(
        summary.contains("--- reference.md [REGRESSION"),
        "{summary}"
    );
    assert!(
        summary.contains("unified diff omitted in summary mode"),
        "{summary}"
    );
    assert!(!summary.contains("- **dock_id_or_code:"), "{summary}");
    assert!(summary.contains(&format!("1 {DIFFS_SUMMARY}")), "{summary}");
    std::fs::write(md, original).unwrap();
    let recovered = run(false);
    assert!(recovered.contains("no differences."), "{recovered}");
    assert!(
        recovered.contains(&format!("0 {DIFFS_SUMMARY}")),
        "{recovered}"
    );
}

#[test]
fn disappearing_file_reports_error_and_continues() {
    let root = tempfile::tempdir().unwrap();
    for (side, content) in [("reference", "old\n"), ("generated", "new\n")] {
        std::fs::create_dir(root.path().join(side)).unwrap();
        for file in ["a.txt", "b.txt"] {
            std::fs::write(root.path().join(side).join(file), content).unwrap();
        }
    }
    std::fs::write(root.path().join("remove-before-render"), "a.txt").unwrap();
    let output = reporter(root.path()).output().unwrap();
    let report = String::from_utf8(output.stdout).unwrap();
    assert!(output.status.success(), "{report}");
    assert!(report.contains("--- a.txt [REGRESSION"), "{report}");
    assert!(
        report.contains("Could not normalize/compare this file:"),
        "{report}"
    );
    assert!(report.contains("--- b.txt [REGRESSION"), "{report}");
    assert!(report.contains("- old\n+ new"), "{report}");
    assert!(report.contains(&format!("2 {DIFFS_SUMMARY}")), "{report}");
}

fn reporter(root: &Path) -> std::process::Command {
    let mut command = std::process::Command::new(std::env::current_exe().unwrap());
    command
        .args([
            "report_fixture_diffs",
            "--exact",
            "--ignored",
            "--nocapture",
        ])
        .env("CROZIER_TEST_DIFF_TREES", root)
        .env_remove("CROZIER_DIFF_SUMMARY_ONLY");
    command
}

#[cfg(target_os = "linux")]
#[test]
fn growing_reports_keep_peak_memory_bounded() {
    // GNU time measures the separate reporter, not this test's fixture builder.
    // Run measurements serially under the host's shared measurement lock.
    const PEAK_KIB: u64 = 256 * 1024;
    let cache = std::env::var_os("XDG_CACHE_HOME")
        .map(PathBuf::from)
        .unwrap_or_else(|| PathBuf::from(std::env::var_os("HOME").unwrap()).join(".cache"));
    let lock = cache.join("crozier/instrumented-measurement.lock");
    std::fs::create_dir_all(lock.parent().unwrap()).unwrap();
    let mut peaks = Vec::new();
    for (files, lines) in [(2, 5_000), (8, 20_000), (20, 50_000)] {
        let root = tempfile::tempdir().unwrap();
        for side in ["reference", "generated"] {
            std::fs::create_dir(root.path().join(side)).unwrap();
            // Unique shared anchors keep normalization's working set small;
            // changes throughout the file still defeat the old diff's common
            // prefix/suffix optimization and require a quadratic text table.
            let content: String = (0..lines / 2)
                .map(|line| format!("anchor-{line}\n{side}\n"))
                .collect();
            for file in 0..files {
                std::fs::write(
                    root.path().join(side).join(format!("file-{file}.txt")),
                    &content,
                )
                .unwrap();
            }
        }
        let peak = root.path().join("peak");
        let mut command = std::process::Command::new("flock");
        command
            .arg(&lock)
            .args(["/usr/bin/time", "-f", "%M", "-o"])
            .arg(&peak)
            .arg(std::env::current_exe().unwrap())
            .args([
                "report_fixture_diffs",
                "--exact",
                "--ignored",
                "--nocapture",
            ])
            .env("CROZIER_TEST_DIFF_TREES", root.path());
        let output = command.output().unwrap();
        let report = String::from_utf8(output.stdout).unwrap();
        assert!(output.status.success(), "{report}");
        let rss: u64 = std::fs::read_to_string(peak)
            .unwrap()
            .trim()
            .parse()
            .unwrap();
        assert!(
            rss < PEAK_KIB,
            "{files} files x {lines} lines: {rss} KiB >= {PEAK_KIB}"
        );
        peaks.push(rss);
        for file in 0..files {
            assert!(
                report.contains(&format!("--- file-{file}.txt [REGRESSION")),
                "{report}"
            );
        }
        let marker = format!(
            "Unified diff omitted: {} normalized input line(s) (Fern: {lines}; crozier: {lines})",
            lines * 2
        );
        assert_eq!(report.matches(&marker).count(), files, "{report}");
        assert!(
            report.contains(&format!("{files} {DIFFS_SUMMARY}")),
            "{report}"
        );
    }
    // Total differing lines grew 100x; RSS must grow by less than 3x (with
    // 32 MiB allocator/startup slack), as well as obeying the absolute ceiling.
    assert!(peaks[2] < peaks[0] * 3 + 32 * 1024, "{peaks:?}");
    eprintln!("reporter peak RSS (KiB), 2x5000 / 8x20000 / 20x50000: {peaks:?}");
}
