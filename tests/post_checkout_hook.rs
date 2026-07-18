#![cfg(unix)]

use std::fs;
use std::path::Path;
use std::process::Command;

use tempfile::TempDir;

fn init_repo(root: &Path) {
    let status = Command::new("git")
        .args(["init", "--quiet"])
        .current_dir(root)
        .status()
        .expect("git should run");
    assert!(status.success());
}

fn git(root: &Path, args: &[&str]) {
    let status = Command::new("git")
        .args(args)
        .current_dir(root)
        .status()
        .expect("git should run");
    assert!(status.success(), "git {args:?} should succeed");
}

#[test]
fn post_checkout_configures_a_shared_sccache_without_sharing_targets() {
    let repo = TempDir::new().expect("temp repo");
    init_repo(repo.path());
    let bin = repo.path().join("bin");
    let cache = repo.path().join("orchestrator-cache");
    fs::create_dir(&bin).expect("fake bin");
    let fake_sccache = bin.join("sccache");
    fs::write(&fake_sccache, "#!/bin/sh\nexit 0\n").expect("fake sccache");
    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;
        fs::set_permissions(&fake_sccache, fs::Permissions::from_mode(0o755))
            .expect("executable fake");
    }

    let path = format!(
        "{}:{}",
        bin.display(),
        std::env::var("PATH").unwrap_or_default()
    );
    let hook = Path::new(env!("CARGO_MANIFEST_DIR")).join(".githooks/post-checkout");
    for _ in 0..2 {
        let status = Command::new(&hook)
            .args(["HEAD", "HEAD", "1"])
            .current_dir(repo.path())
            .env("PATH", &path)
            .env("ORCHESTRATOR_CACHE_DIR", &cache)
            .status()
            .expect("hook should run");
        assert!(status.success());
    }

    let config = fs::read_to_string(repo.path().join(".cargo/config.toml"))
        .expect("hook should configure Cargo");
    assert!(config.contains(&format!("rustc-wrapper = \"{}\"", fake_sccache.display())));
    assert!(config.contains(&format!("{}/sccache", cache.display())));
    assert!(!config.contains("target-dir"));
}

#[test]
fn post_checkout_is_a_no_op_without_sccache() {
    let repo = TempDir::new().expect("temp repo");
    init_repo(repo.path());
    let empty_path = repo.path().join("empty-bin");
    fs::create_dir(&empty_path).expect("empty bin");
    std::os::unix::fs::symlink("/usr/bin/bash", empty_path.join("bash"))
        .expect("bash should be available to the hook");
    let hook = Path::new(env!("CARGO_MANIFEST_DIR")).join(".githooks/post-checkout");
    let status = Command::new(&hook)
        .args(["HEAD", "HEAD", "1"])
        .current_dir(repo.path())
        .env("PATH", empty_path)
        .status()
        .expect("hook should run");
    assert!(status.success());
    assert!(!repo.path().join(".cargo/config.toml").exists());
}

#[test]
fn git_worktree_add_runs_the_hook_with_the_repo_local_default_cache() {
    let repo = TempDir::new().expect("temp repo");
    init_repo(repo.path());
    git(repo.path(), &["config", "user.email", "test@example.com"]);
    git(repo.path(), &["config", "user.name", "Test"]);
    fs::write(repo.path().join("README.md"), "fixture\n").expect("fixture file");
    git(repo.path(), &["add", "README.md"]);
    git(repo.path(), &["commit", "--quiet", "-m", "fixture"]);

    let hooks = repo.path().join(".githooks");
    fs::create_dir(&hooks).expect("hooks dir");
    let source = Path::new(env!("CARGO_MANIFEST_DIR")).join(".githooks/post-checkout");
    let installed_hook = hooks.join("post-checkout");
    fs::copy(source, &installed_hook).expect("install hook");
    git(repo.path(), &["config", "core.hooksPath", ".githooks"]);

    let bin = repo.path().join("bin");
    fs::create_dir(&bin).expect("fake bin");
    let fake_sccache = bin.join("sccache");
    fs::write(&fake_sccache, "#!/bin/sh\nexit 0\n").expect("fake sccache");
    use std::os::unix::fs::PermissionsExt;
    fs::set_permissions(&fake_sccache, fs::Permissions::from_mode(0o755)).expect("executable fake");
    let worktree = repo.path().join("worktree");
    let path = format!(
        "{}:{}",
        bin.display(),
        std::env::var("PATH").unwrap_or_default()
    );
    let status = Command::new("git")
        .args(["worktree", "add", "--quiet", "-b", "fixture-worktree"])
        .arg(&worktree)
        .current_dir(repo.path())
        .env("PATH", path)
        .status()
        .expect("git worktree add should run");
    assert!(status.success());

    let config = fs::read_to_string(worktree.join(".cargo/config.toml"))
        .expect("post-checkout should configure the new worktree");
    let common_dir = repo.path().join(".git/crozier-cache/sccache");
    assert!(config.contains(&common_dir.display().to_string()));
    assert!(!config.contains("target-dir"));
}
