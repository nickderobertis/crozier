//! Which crozier configs a `crozier compare` run checks.
//!
//! - No path: search the whole repository the working directory is in — its git
//!   top-level — or the working directory itself when it is not in one.
//! - A directory: search its tree. `.git` and anything git ignores are skipped
//!   (when the directory is inside a git work tree), but hidden config names such
//!   as `.crozier.yml` are still found. In each directory the config is the first
//!   of [`settings::CONFIG_NAMES`] present — the rule `crozier generate` applies.
//! - A file: checked directly as a crozier config, whatever its name.
//! - A path that does not exist is an error naming it.

use std::collections::{BTreeMap, HashSet};
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};

use crate::settings;

/// One config to check: how the report names it, and where it is.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct FoundConfig {
    /// The path as the report shows it (relative to the searched path as given).
    pub display: String,
    /// The config file's absolute path.
    pub path: PathBuf,
}

/// The configs under `paths` (the [`default_root`] of `cwd` when empty), in
/// argument order and then path order, each once.
///
/// # Errors
///
/// When a path does not exist, naming it.
pub fn discover(paths: &[PathBuf], cwd: &Path) -> Result<Vec<FoundConfig>, String> {
    let mut found = Vec::new();
    let mut seen = HashSet::new();
    let implicit = [default_root(cwd)];
    let roots = if paths.is_empty() {
        &implicit[..]
    } else {
        paths
    };
    for given in roots {
        let absolute = cwd.join(given);
        // The implicit root is named by its configs' paths relative to it.
        let given = if paths.is_empty() {
            Path::new(".")
        } else {
            given.as_path()
        };
        if std::fs::metadata(&absolute).is_err() {
            return Err(format!("path not found: {}", given.display()));
        }
        let candidates: Vec<(String, PathBuf)> = if absolute.is_dir() {
            configs_in_tree(&absolute)
                .into_iter()
                .map(|rel| {
                    let display = if given == Path::new(".") {
                        rel.clone()
                    } else {
                        format!(
                            "{}/{rel}",
                            given.display().to_string().trim_end_matches('/')
                        )
                    };
                    (display, absolute.join(&rel))
                })
                .collect()
        } else {
            vec![(given.display().to_string(), absolute)]
        };
        for (display, path) in candidates {
            let key = std::fs::canonicalize(&path).unwrap_or_else(|_| path.clone());
            if seen.insert(key) {
                found.push(FoundConfig { display, path });
            }
        }
    }
    Ok(found)
}

/// Where a run with no paths searches: the top-level of the git work tree `cwd`
/// is in, or `cwd` itself when it is in none (or git is unavailable).
#[must_use]
pub fn default_root(cwd: &Path) -> PathBuf {
    git(cwd, &["rev-parse", "--show-toplevel"])
        .map(|out| {
            String::from_utf8_lossy(&out)
                .trim_end_matches(['\n', '\r'])
                .to_string()
        })
        .filter(|top| !top.is_empty())
        .map_or_else(|| cwd.to_path_buf(), PathBuf::from)
}

/// `git -C dir <args>`'s stdout when it exits 0. The directory decides, not a
/// repository a calling hook points at, so git's location variables are dropped.
fn git(dir: &Path, args: &[&str]) -> Option<Vec<u8>> {
    let output = Command::new("git")
        .arg("-C")
        .arg(dir)
        .args(args)
        .env_remove("GIT_DIR")
        .env_remove("GIT_WORK_TREE")
        .env_remove("GIT_INDEX_FILE")
        .stdin(Stdio::null())
        .stderr(Stdio::null())
        .output()
        .ok()?;
    output.status.success().then_some(output.stdout)
}

/// Every config under `root`, as `/`-separated paths relative to it, sorted:
/// at most one per directory, chosen by [`settings::CONFIG_NAMES`] priority.
fn configs_in_tree(root: &Path) -> Vec<String> {
    let files = git_visible_files(root).unwrap_or_else(|| walk_without_git(root));
    let mut by_dir: BTreeMap<String, Vec<String>> = BTreeMap::new();
    for rel in files {
        let (dir, name) = match rel.rsplit_once('/') {
            Some((dir, name)) => (dir.to_string(), name.to_string()),
            None => (String::new(), rel.clone()),
        };
        if settings::CONFIG_NAMES.contains(&name.as_str()) && root.join(&rel).is_file() {
            by_dir.entry(dir).or_default().push(name);
        }
    }
    by_dir
        .into_iter()
        .filter_map(|(dir, names)| {
            let name = settings::CONFIG_NAMES
                .iter()
                .find(|candidate| names.iter().any(|n| n == *candidate))?;
            Some(if dir.is_empty() {
                (*name).to_string()
            } else {
                format!("{dir}/{name}")
            })
        })
        .collect()
}

/// The files git does not ignore under `root` (tracked or not), relative to it,
/// when `root` is inside a git work tree and git is available; `None` otherwise.
fn git_visible_files(root: &Path) -> Option<Vec<String>> {
    let stdout = git(
        root,
        &[
            "ls-files",
            "-z",
            "--cached",
            "--others",
            "--exclude-standard",
        ],
    )?;
    let text = String::from_utf8_lossy(&stdout);
    Some(
        text.split('\0')
            .filter(|rel| !rel.is_empty())
            .map(str::to_string)
            .collect(),
    )
}

/// Every file under `root` outside a git work tree, skipping `.git` directories
/// and never following a symbolic link.
fn walk_without_git(root: &Path) -> Vec<String> {
    fn rec(base: &Path, dir: &Path, out: &mut Vec<String>) {
        let Ok(entries) = std::fs::read_dir(dir) else {
            return;
        };
        for entry in entries.flatten() {
            let path = entry.path();
            let Ok(kind) = entry.file_type() else {
                continue;
            };
            if kind.is_dir() {
                if entry.file_name() != ".git" {
                    rec(base, &path, out);
                }
            } else if kind.is_file() {
                if let Ok(rel) = path.strip_prefix(base) {
                    out.push(rel.to_string_lossy().replace('\\', "/"));
                }
            }
        }
    }
    let mut out = Vec::new();
    rec(root, root, &mut out);
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn touch(root: &Path, rel: &str) {
        let path = root.join(rel);
        std::fs::create_dir_all(path.parent().unwrap()).unwrap();
        std::fs::write(path, "spec: ./a.yml\n").unwrap();
    }

    fn displays(found: &[FoundConfig]) -> Vec<&str> {
        found.iter().map(|f| f.display.as_str()).collect()
    }

    #[test]
    fn no_paths_search_the_git_top_level_or_else_the_working_directory() {
        let dir = tempfile::tempdir().unwrap();
        let root = std::fs::canonicalize(dir.path()).unwrap();
        // Outside any repository: the working directory itself.
        assert_eq!(default_root(&root), root);

        let status = Command::new("git")
            .args(["init", "-q"])
            .current_dir(&root)
            .env_remove("GIT_DIR")
            .env_remove("GIT_WORK_TREE")
            .env_remove("GIT_INDEX_FILE")
            .status()
            .unwrap();
        assert!(status.success());
        touch(&root, "other/crozier.yml");
        std::fs::create_dir_all(root.join("sub")).unwrap();
        let sub = root.join("sub");
        assert_eq!(
            std::fs::canonicalize(default_root(&sub)).unwrap(),
            root,
            "a subdirectory searches its repository's top level"
        );
        assert_eq!(
            displays(&discover(&[], &sub).unwrap()),
            ["other/crozier.yml"]
        );
        // An explicit path still narrows.
        assert!(discover(&[PathBuf::from(".")], &sub).unwrap().is_empty());
    }

    #[test]
    fn a_plain_tree_finds_one_config_per_directory_by_priority() {
        let dir = tempfile::tempdir().unwrap();
        let root = dir.path();
        touch(root, "crozier.yml");
        touch(root, ".crozier.yml");
        touch(root, "a/.crozier.yaml");
        touch(root, "b/c/crozier.yaml");
        touch(root, "b/c/.crozier.yml");
        touch(root, ".git/crozier.yml");
        touch(root, "d/not-a-config.yml");
        let found = discover(&[], root).unwrap();
        assert_eq!(
            displays(&found),
            ["crozier.yml", "a/.crozier.yaml", "b/c/crozier.yaml"]
        );
        assert_eq!(found[1].path, root.join("a/.crozier.yaml"));
    }

    #[test]
    fn a_git_tree_skips_ignored_paths_but_finds_hidden_configs() {
        let dir = tempfile::tempdir().unwrap();
        let root = dir.path();
        let git = |args: &[&str]| {
            let status = Command::new("git")
                .env_remove("GIT_DIR")
                .env_remove("GIT_WORK_TREE")
                .env_remove("GIT_INDEX_FILE")
                .arg("-C")
                .arg(root)
                .args(args)
                .stdout(Stdio::null())
                .status()
                .unwrap();
            assert!(status.success());
        };
        git(&["init", "-q"]);
        std::fs::write(root.join(".gitignore"), "ignored/\n").unwrap();
        std::fs::create_dir_all(root.join(".git/info")).unwrap();
        std::fs::write(root.join(".git/info/exclude"), "excluded/\n").unwrap();
        touch(root, "ignored/crozier.yml");
        touch(root, "excluded/crozier.yml");
        touch(root, "svc/.crozier.yml");
        touch(root, "tracked/crozier.yml");
        git(&["add", "tracked/crozier.yml"]);
        let found = discover(&[PathBuf::from(".")], root).unwrap();
        assert_eq!(
            displays(&found),
            ["svc/.crozier.yml", "tracked/crozier.yml"]
        );

        // A directory argument searches only its own tree.
        let found = discover(&[PathBuf::from("svc/")], root).unwrap();
        assert_eq!(displays(&found), ["svc/.crozier.yml"]);
    }

    #[test]
    fn a_file_argument_is_a_config_whatever_its_name_and_duplicates_collapse() {
        let dir = tempfile::tempdir().unwrap();
        let root = dir.path();
        touch(root, "configs/team.yaml");
        touch(root, "crozier.yml");
        let found = discover(
            &[
                PathBuf::from("configs/team.yaml"),
                PathBuf::from("."),
                PathBuf::from("crozier.yml"),
            ],
            root,
        )
        .unwrap();
        assert_eq!(displays(&found), ["configs/team.yaml", "crozier.yml"]);
    }

    #[test]
    fn a_missing_path_is_an_error_naming_it() {
        let dir = tempfile::tempdir().unwrap();
        let error = discover(&[PathBuf::from("nope")], dir.path()).unwrap_err();
        assert_eq!(error, "path not found: nope");
        assert!(discover(&[], dir.path()).unwrap().is_empty());
    }

    #[cfg(unix)]
    #[test]
    fn the_plain_walk_does_not_follow_symbolic_links() {
        let dir = tempfile::tempdir().unwrap();
        let outside = tempfile::tempdir().unwrap();
        touch(outside.path(), "crozier.yml");
        std::os::unix::fs::symlink(outside.path(), dir.path().join("link")).unwrap();
        assert!(walk_without_git(dir.path()).is_empty());
        assert!(walk_without_git(&dir.path().join("absent")).is_empty());
    }
}
