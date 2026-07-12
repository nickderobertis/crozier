//! Generation configuration. Deliberately small: the OpenAPI document plus a few
//! naming knobs are the entire input — there is no per-project config file.

use std::path::{Component, Path, PathBuf};

use crate::error::{Error, Result};

/// A validated Python package (import) name — a single, safe path segment.
///
/// The name becomes a directory under `src/` *and*, on regeneration, the target
/// of a destructive `remove_dir_all` (see [`crate::emit::clean_package_tree`]).
/// The only way to obtain a `PackageName` is [`PackageName::new`], which rejects
/// path separators and `.`/`..`, so a traversal value like `../..` can never
/// reach that delete: the invalid state is unrepresentable, not merely guarded
/// by a check a caller must remember to run.
#[derive(Debug, Clone)]
pub struct PackageName(String);

impl PackageName {
    /// Validate and wrap a package name. Errors on an empty name, `.`/`..`, or
    /// any path separator (`/` or `\`, on every platform).
    pub fn new(name: String) -> Result<Self> {
        let mut components = Path::new(&name).components();
        let single_segment =
            matches!(components.next(), Some(Component::Normal(_))) && components.next().is_none();
        if single_segment && !name.contains(['/', '\\']) {
            Ok(Self(name))
        } else {
            Err(Error::InvalidPackageName { name })
        }
    }

    /// The validated name as a string slice.
    #[must_use]
    pub fn as_str(&self) -> &str {
        &self.0
    }
}

impl std::fmt::Display for PackageName {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(&self.0)
    }
}

/// Everything a generation run needs.
#[derive(Debug, Clone)]
pub struct GenerateConfig {
    /// Path to the OpenAPI document to read.
    pub spec: PathBuf,
    /// Directory to write the generated SDK into.
    pub output: PathBuf,
    /// The Python import package name (the directory under `src/`), e.g. `seed`.
    pub package_name: PackageName,
    /// The distribution (PyPI) name recorded in `version.py`, e.g.
    /// `fern_my-api`. Defaults to the package name when unset.
    pub project_name: String,
    /// Override for the generated root client class name (Fern's
    /// `client_class_name`). `None` derives it from the package name as
    /// `{PascalCase(package_name)}Api` — see [`crate::ir::build`].
    pub client_class_name: Option<String>,
}

impl GenerateConfig {
    /// Build a config from raw CLI inputs, filling naming defaults from `title`
    /// when a name was not supplied. Fails if the effective package name is not a
    /// single safe path segment (see [`PackageName::new`]) — including when a
    /// pathological title derives one — so the invariant holds before any
    /// filesystem work, and never by panicking.
    pub fn new(
        spec: PathBuf,
        output: PathBuf,
        package_name: Option<String>,
        project_name: Option<String>,
        client_class_name: Option<String>,
        title: &str,
    ) -> Result<Self> {
        let package_name = match package_name {
            Some(name) => PackageName::new(name)?,
            None => PackageName::new(default_package_name(title))?,
        };
        let project_name = project_name.unwrap_or_else(|| package_name.as_str().to_string());
        Ok(Self {
            spec,
            output,
            package_name,
            project_name,
            client_class_name,
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
