//! `docs/migrating-from-fern.md`'s generator-option tables, held to the option
//! names of the pinned `fernapi/fern-python-sdk` image. Fern no longer publishes
//! the generator's source, so the image is the only authority. This reads its
//! `SDKCustomConfig` and `PydanticModelCustomConfig` field names with the
//! image's own Python, and copies none of its source into the repository.

use std::collections::BTreeSet;
use std::process::Command;

use super::repo_root;

const GUIDE: &str = "docs/migrating-from-fern.md";

/// Prints `{"name": [nested names]}` for every field of `SDKCustomConfig`,
/// nested names spelled `parent.child` as the guide spells them.
const PROBE: &str = r#"
import json, typing, pydantic
from fern_python.generators.sdk.custom_config import SDKCustomConfig

def model_of(annotation):
    for arg in typing.get_args(annotation) or (annotation,):
        if isinstance(arg, type) and issubclass(arg, pydantic.BaseModel):
            return arg

print(json.dumps({
    name: [f"{name}.{child}" for child in model.model_fields] if (model := model_of(info.annotation)) else []
    for name, info in SDKCustomConfig.model_fields.items()
}))
"#;

/// The option column of the guide's `Generator config` and `pydantic_config` tables.
fn guide_options(guide: &str) -> BTreeSet<String> {
    let mut options = BTreeSet::new();
    for heading in ["### Generator `config`", "### `pydantic_config`"] {
        let section = guide
            .split_once(heading)
            .unwrap_or_else(|| panic!("{GUIDE} has no `{heading}` table"))
            .1;
        let section = section.split("\n### ").next().unwrap_or(section);
        for line in section.lines() {
            if let Some(name) = line
                .strip_prefix("| `")
                .and_then(|rest| rest.split_once('`'))
                .map(|(name, _)| name)
            {
                options.insert(name.to_string());
            }
        }
    }
    options
}

/// The option names the image's model accepts. A nested model's fields count
/// one by one where the guide spells them `parent.child`, else as one option.
fn model_options(fields: &serde_json::Value, guide: &BTreeSet<String>) -> BTreeSet<String> {
    let expanded: BTreeSet<&str> = guide
        .iter()
        .filter_map(|option| option.split_once('.').map(|(parent, _)| parent))
        .collect();
    let mut options = BTreeSet::new();
    for (name, nested) in fields.as_object().expect("the probe prints an object") {
        let nested: Vec<&str> = nested
            .as_array()
            .unwrap_or_else(|| {
                panic!("the probe's `{name}` is not a list of nested names: {nested}")
            })
            .iter()
            .map(|child| {
                child.as_str().unwrap_or_else(|| {
                    panic!("the probe's `{name}` lists a nested name that is not a string: {child}")
                })
            })
            .collect();
        if expanded.contains(name.as_str()) && !nested.is_empty() {
            options.extend(nested.iter().map(|child| (*child).to_string()));
        } else {
            options.insert(name.clone());
        }
    }
    options
}

#[test]
#[ignore = "opt-in Docker tier (reads the pinned fernapi/fern-python-sdk image); run via `just test-sdk-env`"]
fn sdk_env_the_migration_guide_lists_every_option_the_pinned_generator_accepts() {
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(repo_root().join("assets/scaffolding/metadata.json")).unwrap(),
    )
    .unwrap();
    let image = format!(
        "fernapi/fern-python-sdk:{}",
        metadata["generatorVersion"]
            .as_str()
            .expect("a generator version")
    );
    let present = Command::new("docker")
        .args(["image", "inspect", &image])
        .output()
        .is_ok_and(|output| output.status.success());
    if !present {
        eprintln!(
            "skipped: Docker or the image {image} is unavailable; `docker pull {image}` and rerun to check {GUIDE}"
        );
        return;
    }
    let output = Command::new("docker")
        .args(["run", "--rm", "--entrypoint", "python", &image, "-c", PROBE])
        .output()
        .expect("docker runs");
    assert!(
        output.status.success(),
        "{image}'s Python could not read its config models: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    let fields: serde_json::Value =
        serde_json::from_slice(&output.stdout).expect("the probe prints JSON");
    let guide = guide_options(&std::fs::read_to_string(repo_root().join(GUIDE)).unwrap());
    let model = model_options(&fields, &guide);
    let missing: Vec<&String> = model.difference(&guide).collect();
    let extra: Vec<&String> = guide.difference(&model).collect();
    assert!(
        missing.is_empty() && extra.is_empty(),
        "{GUIDE} and {image} disagree on the generator's options.\n\
         Options the image accepts that the guide does not list: {missing:?}\n\
         Options the guide lists that the image does not accept: {extra:?}"
    );
}

/// The comparison itself, on a fixed model and guide: a missing and an extra
/// option are each named, and a nested model is read as the guide spells it.
#[test]
fn the_option_comparison_names_each_disagreement() {
    let guide = "### Generator `config`\n\n| Option | Default | crozier |\n| --- | --- | --- |\n\
                 | `timeout` | unset | Default only. |\n| `client.class_name` | unset | x |\n\
                 | `retired` | unset | x |\n\n### `pydantic_config`\n\n| Option | Default | crozier |\n\
                 | --- | --- | --- |\n| `pydantic_config.frozen` | `true` | x |\n";
    let fields = serde_json::json!({
        "timeout": [],
        "client": ["client.class_name", "client.filename"],
        "pydantic_config": ["pydantic_config.frozen"],
        "lazy_imports": [],
    });
    let guide = guide_options(guide);
    let model = model_options(&fields, &guide);
    assert_eq!(
        model.difference(&guide).collect::<Vec<_>>(),
        ["client.filename", "lazy_imports"]
    );
    assert_eq!(guide.difference(&model).collect::<Vec<_>>(), ["retired"]);
}

/// A probe that lists anything but strings is refused, not read as fewer options.
#[test]
#[should_panic(expected = "lists a nested name that is not a string")]
fn a_malformed_probe_is_refused() {
    let guide = guide_options("### Generator `config`\n\n| `client.class_name` | x |\n\n### `pydantic_config`\n\n| `pydantic_config.frozen` | x |\n");
    model_options(
        &serde_json::json!({"client": ["client.class_name", 7]}),
        &guide,
    );
}
