//! Generation configuration. Deliberately small: the OpenAPI document plus a few
//! naming knobs are the entire input — there is no per-project config file.

use std::path::PathBuf;

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

/// Derive a fallback package name from the API title.
fn default_package_name(title: &str) -> String {
    let snake = crate::naming::to_snake_case(title);
    if snake.is_empty() {
        "client".to_string()
    } else {
        snake
    }
}
