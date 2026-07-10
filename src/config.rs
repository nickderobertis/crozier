//! Generation configuration. Deliberately small: the OpenAPI document plus a few
//! naming knobs are the entire input — there is no per-project config file.

use std::path::{Component, Path, PathBuf};

use crate::error::{Error, Result};

/// Everything a generation run needs.
#[derive(Debug, Clone)]
pub struct GenerateConfig {
    /// Path to the OpenAPI document to read.
    pub spec: PathBuf,
    /// Directory to write the generated SDK into.
    pub output: PathBuf,
    /// The Python import package name (the directory under `src/`), e.g. `seed`.
    pub package_name: String,
    /// The distribution (PyPI) name recorded in `version.py`, e.g.
    /// `fern_my-api`. Defaults to the package name when unset.
    pub project_name: String,
}

impl GenerateConfig {
    /// Build a config from raw CLI inputs, filling naming defaults from `title`
    /// when a name was not supplied.
    #[must_use]
    pub fn new(
        spec: PathBuf,
        output: PathBuf,
        package_name: Option<String>,
        project_name: Option<String>,
        title: &str,
    ) -> Self {
        let package_name = package_name.unwrap_or_else(|| default_package_name(title));
        let project_name = project_name.unwrap_or_else(|| package_name.clone());
        Self {
            spec,
            output,
            package_name,
            project_name,
        }
    }
}

/// Validate the effective package name before it is used as a directory under
/// `src/` and — on regeneration — as the target of a destructive `remove_dir_all`
/// (see [`crate::emit::clean_package_tree`]). It must be a single, ordinary path
/// segment: not empty, not `.`/`..`, and free of path separators, so a crafted
/// `--package-name` (e.g. `../..`) cannot escape the generated tree and delete
/// elsewhere. The auto-derived default is snake_case, which never contains a
/// separator, so it always passes.
pub fn validate_package_name(name: &str) -> Result<()> {
    let mut components = Path::new(name).components();
    let single_segment =
        matches!(components.next(), Some(Component::Normal(_))) && components.next().is_none();
    // Also reject `/` and `\` explicitly, so a name that is a traversal on *any*
    // platform is rejected everywhere — not only on the OS whose separator it is.
    if single_segment && !name.contains(['/', '\\']) {
        Ok(())
    } else {
        Err(Error::InvalidPackageName {
            name: name.to_string(),
        })
    }
}

/// Derive a fallback package name from the API title.
fn default_package_name(title: &str) -> String {
    let snake = crate::naming::to_snake_case(title);
    if snake.is_empty() {
        "client".to_string()
    } else {
        snake
    }
}
