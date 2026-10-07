//! The "Migrating from Fern" workflow, driven from the guide's own code blocks:
//! the README's step blocks and `docs/migrating-from-fern.md`'s, each found by
//! the `<!-- migration-e2e: NAME -->` comment before it. The config is written as
//! shown, its `reference.command` names a committed stand-in for the team's copy
//! of the Fern recipe that writes a committed Fern golden, and every command runs
//! under `sh -c` with the compiled `crozier` first on `PATH`. So a key or command
//! the guide shows and crozier rejects fails here.

use std::path::{Path, PathBuf};
use std::process::{Command, Output};

fn root() -> &'static Path {
    crate::repo_root()
}

/// The body of the code block marked `<!-- migration-e2e: name -->` in `page`.
fn block(page: &str, name: &str) -> String {
    let text = std::fs::read_to_string(root().join(page)).unwrap();
    let marker = format!("<!-- migration-e2e: {name} -->\n```");
    let mut found = text.split(&marker).skip(1);
    let rest = found
        .next()
        .unwrap_or_else(|| panic!("{page} marks no `{name}` code block"));
    assert!(found.next().is_none(), "{page} marks `{name}` twice");
    let (_, body) = rest.split_once('\n').unwrap();
    let (body, _) = body
        .split_once("\n```\n")
        .unwrap_or_else(|| panic!("{page}: the `{name}` block is not closed"));
    format!("{body}\n")
}

/// The `crozier` binary's directory, prepended to `PATH`.
fn path_with_crozier() -> String {
    let bin = crate::crozier_bin();
    let dir = bin.parent().unwrap();
    format!(
        "{}:{}",
        dir.display(),
        std::env::var("PATH").unwrap_or_default()
    )
}

/// Run a command the guide shows, from `repo`, with `golden` as the stand-in
/// recipe's reference.
fn run(repo: &Path, command: &str, golden: &Path) -> Output {
    Command::new("sh")
        .arg("-c")
        .arg(command)
        .current_dir(repo)
        .env("PATH", path_with_crozier())
        .env("MIGRATION_E2E_GOLDEN", golden)
        .env("NO_COLOR", "1")
        .output()
        .expect("run the guide's command")
}

fn text(bytes: &[u8]) -> String {
    String::from_utf8_lossy(bytes).into_owned()
}

fn write(path: &Path, contents: &str) {
    std::fs::create_dir_all(path.parent().unwrap()).unwrap();
    std::fs::write(path, contents).unwrap();
}

/// Copy one file (its mode included), creating the target's directory.
fn copy_file(from: &Path, to: &Path) {
    std::fs::create_dir_all(to.parent().unwrap()).unwrap();
    std::fs::copy(from, to).unwrap();
}

fn copy_tree(from: &Path, to: &Path) {
    std::fs::create_dir_all(to).unwrap();
    for entry in std::fs::read_dir(from).unwrap() {
        let entry = entry.unwrap();
        let target = to.join(entry.file_name());
        if entry.file_type().unwrap().is_dir() {
            copy_tree(&entry.path(), &target);
        } else {
            std::fs::copy(entry.path(), target).unwrap();
        }
    }
}

/// A repository path the config names (`./x` or `x`).
fn in_repo(repo: &Path, configured: &str) -> PathBuf {
    repo.join(configured.trim_start_matches("./"))
}

/// A Fern `generators.yml` with the Python generator still on Fern beside a
/// TypeScript one; `with_python: false` is it after step 4.
fn generators_yml(with_python: bool) -> String {
    let python = "  python-sdk:\n    generators:\n      - name: fernapi/fern-python-sdk\n        version: 5.20.0\n        output:\n          location: local-file-system\n          path: ../sdks/python\n";
    let typescript = "  ts-sdk:\n    generators:\n      - name: fernapi/fern-typescript-sdk\n        version: 3.0.0\n        output:\n          location: local-file-system\n          path: ../sdks/ts\n";
    format!(
        "api:\n  path: openapi/openapi.yml\ngroups:\n{}{typescript}",
        if with_python { python } else { "" }
    )
}

#[test]
fn the_migration_guide_workflow_runs_as_written() {
    let repo_dir = tempfile::tempdir().unwrap();
    let repo = repo_dir.path();
    assert!(Command::new("git")
        .args(["init", "-q"])
        .current_dir(repo)
        .env_remove("GIT_DIR")
        .env_remove("GIT_WORK_TREE")
        .status()
        .unwrap()
        .success());

    // Step 1: the config exactly as the README shows it, and what it names.
    let config = block("README.md", "config");
    write(&repo.join("crozier.yml"), &config);
    let parsed: serde_yaml_ng::Value = serde_yaml_ng::from_str(&config).unwrap();
    let python = &parsed["generators"]["python"];
    let spec = python["spec"].as_str().expect("step 1 names a spec");
    let output = python["output"].as_str().expect("step 1 names an output");
    let command = python["reference"]["command"]
        .as_str()
        .expect("step 1 names a reference command");
    assert_eq!(python["layout"].as_str(), Some("flat"));
    // The Fern golden for this API under organization `acme`, written flat.
    let fixture = root().join("tests/fixtures");
    copy_file(
        &fixture.join("exhaustive/openapi.yml"),
        &in_repo(repo, spec),
    );
    copy_file(
        &root().join("crates/crozier-e2e/tests/e2e/migration/fern-reference.sh"),
        &in_repo(repo, command),
    );
    write(&repo.join("fern/generators.yml"), &generators_yml(true));
    let golden_dir = tempfile::tempdir().unwrap();
    let golden = golden_dir.path().join("reference");
    copy_tree(
        &fixture.join("exhaustive-package-name/expected-flat"),
        &golden,
    );

    // Step 2: the comparison matches the reference.
    let compare = block("README.md", "compare");
    let matched = run(repo, &compare, &golden);
    assert_eq!(matched.status.code(), Some(0), "{}", text(&matched.stderr));
    assert!(
        text(&matched.stderr).contains("python: matched (layout flat"),
        "{}",
        text(&matched.stderr)
    );

    // A reference that differs is reported, with exit 3.
    let readme = golden.join("README.md");
    let mut edited = std::fs::read_to_string(&readme).unwrap();
    edited.push_str("A line Fern did not write.\n");
    std::fs::write(&readme, edited).unwrap();
    let mismatched = run(repo, &compare, &golden);
    assert_eq!(
        mismatched.status.code(),
        Some(3),
        "{}",
        text(&mismatched.stderr)
    );
    let report = text(&mismatched.stderr);
    assert!(report.contains("python: mismatched"), "{report}");
    assert!(report.contains("README.md"), "{report}");

    // Tracking what remains: the Python generator still in generators.yml is
    // listed, and the TypeScript one is not.
    let remaining = block("README.md", "remaining");
    let listed = run(repo, &remaining, &golden);
    assert_eq!(listed.status.code(), Some(0), "{}", text(&listed.stderr));
    let stdout = text(&listed.stdout);
    assert!(
        stdout.contains("fern/generators.yml") && stdout.contains("fernapi/fern-python-sdk"),
        "{stdout}"
    );
    assert!(!stdout.contains("typescript"), "{stdout}");

    // Step 3: the build generates the flat tree where the config points.
    let generate = block("README.md", "generate");
    let generated = run(repo, &generate, &golden);
    assert!(generated.status.success(), "{}", text(&generated.stderr));
    let sdk = in_repo(repo, output);
    assert!(sdk.join("client.py").is_file());
    assert!(sdk.join(".fern/metadata.json").is_file());
    assert!(!sdk.join("src").exists() && !sdk.join("pyproject.toml").exists());

    // Step 4: with the Python generator removed, nothing is left to list.
    write(&repo.join("fern/generators.yml"), &generators_yml(false));
    let none_left = run(repo, &remaining, &golden);
    assert_eq!(none_left.status.code(), Some(1));
    assert_eq!(text(&none_left.stdout), "");
}

#[test]
fn the_scripted_fern_search_finds_scripts_and_skips_the_recipe() {
    let repo_dir = tempfile::tempdir().unwrap();
    let repo = repo_dir.path();
    let search = block("docs/migrating-from-fern.md", "scripted-fern");
    // The recipe itself runs `fern generate`, and is left out.
    write(
        &repo.join("scripts/fern-reference.sh"),
        "fern generate --group crozier-reference --local --force\n",
    );
    let none = run(repo, &search, repo);
    assert_eq!(none.status.code(), Some(1), "{}", text(&none.stderr));
    assert_eq!(text(&none.stdout), "");

    write(
        &repo.join("tools/regen.sh"),
        "cd \"$(mktemp -d)\" && fern init --openapi \"$SPEC\"\n",
    );
    let found = run(repo, &search, repo);
    assert_eq!(found.status.code(), Some(0), "{}", text(&found.stderr));
    let stdout = text(&found.stdout);
    assert!(stdout.contains("tools/regen.sh"), "{stdout}");
    assert!(!stdout.contains("fern-reference.sh"), "{stdout}");
}

/// The guide restates the certified Fern pair (prose, `generators.yml`,
/// `fern.config.json`, `docker pull`); every version it names is that pair from
/// `assets/scaffolding/metadata.json` or one of the pinned tool and history
/// versions listed here, so moving the pair fails until the guide moves too.
#[test]
fn the_migration_guide_names_the_certified_fern_pair() {
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(root().join("assets/scaffolding/metadata.json")).unwrap(),
    )
    .unwrap();
    let cli = metadata["cliVersion"].as_str().unwrap();
    let generator = metadata["generatorVersion"].as_str().unwrap();
    // swagger2openapi and openapi-format pins, and the crozier release that
    // fixed bracketed property names.
    let others = ["7.0.8", "1.33.5", "0.0.22"];
    let page = std::fs::read_to_string(root().join("docs/migrating-from-fern.md")).unwrap();
    let versions = versions_in(&page);
    assert!(
        versions.iter().any(|v| v == cli),
        "the guide never names CLI {cli}"
    );
    assert!(
        versions.iter().any(|v| v == generator),
        "the guide never names generator {generator}"
    );
    for version in &versions {
        assert!(
            version == cli || version == generator || others.contains(&version.as_str()),
            "docs/migrating-from-fern.md names version {version}, which is neither the certified \
             pair ({cli} / {generator}) nor a listed pin; update the guide or the list"
        );
    }
    // The check can fail: an uncertified version is caught.
    assert!(versions_in("version: 5.19.3").contains(&"5.19.3".to_string()));
}

/// Every `N.N.N` in `text`.
fn versions_in(text: &str) -> Vec<String> {
    let mut found = Vec::new();
    let chars: Vec<char> = text.chars().collect();
    let mut i = 0;
    while i < chars.len() {
        if chars[i].is_ascii_digit() && (i == 0 || !chars[i - 1].is_ascii_alphanumeric()) {
            let start = i;
            while i < chars.len() && (chars[i].is_ascii_digit() || chars[i] == '.') {
                i += 1;
            }
            let token: String = chars[start..i].iter().collect::<String>();
            let token = token.trim_end_matches('.');
            if token.split('.').count() == 3 && token.split('.').all(|p| !p.is_empty()) {
                found.push(token.to_string());
            }
        } else {
            i += 1;
        }
    }
    found
}
