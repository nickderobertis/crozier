# Configuration

crozier's input is an OpenAPI document plus a small set of generation settings.
Those settings can come from the command line, the environment, or a
`crozier.yml` config file — layered so a project can commit its defaults once and
override them per invocation.

## The model: named generators

A run emits one or more **named generator instances**. Each instance has a
`type` (only `python` today, and the default) and its own generation settings.
A built-in `python` generator always exists, so `crozier generate python` works
with **zero config**. Defining a `python` entry in a config file overrides that
built-in's defaults.

## Commands

| Command | What it does |
| --- | --- |
| `crozier` | Generate with every configured generator (the built-in `python` when none are configured). |
| `crozier generate` | Same as bare `crozier`. |
| `crozier generate <name>` | Generate with the one generator named `<name>` (a config entry, or the built-in `python`). |
| `crozier init` | Write a starter `crozier.yml` (`--output <path>`, `--force`). |
| `crozier config [<name>]` | Print the effective config and the layer each value came from. |
| `crozier schema` | Print the config JSON Schema to stdout. |

## Precedence

Every field is resolved highest-wins:

```text
CLI flag  >  CROZIER_* env var  >  generators.<name>.<field>  >  top-level <field>  >  built-in default
```

- **CLI flags** — `--spec`, `--output`, `--package-name`, `--project-name`,
  `--client-class-name`, `--audience` (repeatable), `--audience-strict`,
  `--extra-fields`, `--layout`. These apply to a *single* generator; passing them while more
  than one would run is an error (name one, or move the values into the config
  file).
- **Environment** — `CROZIER_SPEC`, `CROZIER_OUTPUT`, `CROZIER_PACKAGE_NAME`,
  `CROZIER_PROJECT_NAME`, `CROZIER_CLIENT_CLASS_NAME`, `CROZIER_AUDIENCES`
  (comma-separated), `CROZIER_AUDIENCE_STRICT`, `CROZIER_EXTRA_FIELDS`,
  `CROZIER_LAYOUT`. Empty values count as unset; a value outside a field's set
  (`CROZIER_LAYOUT=nested`) is an error naming the variable. These are a global
  override layer applied to every selected generator.
- **Config file** — a `generators.<name>` value beats the shared top-level value
  of the same field. `extra-fields` is **Python-generator-specific**: it lives
  only under a generator, never at the shared top level (a top-level
  `extra-fields` is a parse error).
- **Built-in defaults** — `package-name` defaults to a `snake_case` of the API
  title; `project-name` defaults to the package name; `client-class-name`
  defaults to `{PascalCase(package-name)}Api`; audiences default to empty (the
  whole API); `extra-fields` defaults to `allow`; `layout` defaults to
  `packaged`. `spec` and `output` have no default — a generator resolved without
  either is an actionable error.

So `layout` resolves as `--layout` > `CROZIER_LAYOUT` > `generators.<name>.layout`
> top-level `layout` > `packaged`, and any other value from any layer is refused
with an error naming the value and where it came from.

## Output layout

Fern writes one of two trees depending on how it is run, and `layout` picks the
one crozier writes, so a team migrating from Fern sets the value that matches its
Fern setup and gets the same files:

| `layout` | crozier writes | Matches Fern's |
| --- | --- | --- |
| `packaged` (default) | A pip-installable package: `pyproject.toml`, `requirements.txt`, `README.md`, `CONTRIBUTING.md`, `reference.md`, `.fern/metadata.json`, `tests/`, and the modules under `src/<package-name>/` (with `py.typed` and `version.py`). | `fern generate --preview --output <dir>` |
| `flat` | The package's modules directly under `output`, beside `README.md`, `CONTRIBUTING.md`, `reference.md`, `.fern/metadata.json` and `tests/`. No `pyproject.toml`, `requirements.txt`, `py.typed` or `version.py`. | a generator whose `output` is `location: local-file-system` with a `path` |

The flat modules also differ slightly from their packaged form, as Fern's do: no
`__version__` export, an aiohttp install hint naming the package rather than the
project, and no `X-Fern-SDK-Name`/`X-Fern-SDK-Version` headers. A flat tree has
no distribution, so `project-name` reaches none of its files.
[`matching.md`](matching.md#the-flat-layout) lists every difference.

Regenerating is idempotent in both layouts. `packaged` clears
`<output>/src/<package-name>/` first; `flat` clears `output` itself, but only
when it holds a previous generation (it has a `.fern/metadata.json`). It always
keeps dot-entries such as `.git`. A directory without that file is written into
and nothing in it is deleted.

## The config file

### Discovery

A config file in the **working directory** is picked up automatically, by this
priority: `crozier.yml`, `crozier.yaml`, `.crozier.yml`, `.crozier.yaml`. There
is no walk up the parent tree — discovery is the working directory only.

- `--config <path>` (repeatable) loads exactly those files instead of
  discovering one; later files win per field. A named-but-missing file is an
  error.
- `CROZIER_CONFIG=<path>` names a single file via the environment (`--config`
  beats it).
- `--no-config` ignores config files and `CROZIER_*` overrides entirely — only
  CLI flags and built-in defaults shape the run (useful for hermetic runs).

### Schema

```yaml
# Top-level keys are shared defaults inherited by every generator.
spec: ./openapi.yml
output: ./sdks            # usually set per-generator instead
package-name: my_api
project-name: my-api
audiences: [public]
audience-strict: false
layout: packaged          # packaged|flat — see "Output layout"

generators:
  python:
    type: python          # optional; `python` is the only type today (and the default)
    spec: ./openapi.yml    # any shared field can be overridden per generator
    output: ./sdks/python
    package-name: my_api
    project-name: my-api
    client-class-name: MyApi   # defaults to {PascalCase(package-name)}Api
    audiences: [public]
    audience-strict: false
    extra-fields: allow        # allow|ignore|forbid — pydantic behavior for unknown
                               # response fields (Python-generator-specific; not a
                               # shared top-level field)
    layout: flat               # packaged (Fern's --preview --output) | flat
                               # (Fern's local-file-system output)
  admin:
    spec: ./admin-openapi.yml
    output: ./sdks/admin
    package-name: admin_api
```

Unknown fields and unknown generator types are rejected at parse time, with the
offending file's path in the error. Generators run in declaration order.

### Editor support (JSON Schema)

`crozier init` writes the config with a modeline on the first line:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/nickderobertis/crozier/main/assets/crozier.schema.json
```

Editors with the [YAML language server](https://github.com/redhat-developer/yaml-language-server)
(VS Code, Neovim, …) then offer field completion, hover docs, and validation
against the published schema. The schema is **derived from crozier's own config
types** (`schemars`), so it never drifts from what the tool accepts; the
committed `assets/crozier.schema.json` is pinned to the generator by a test
(regenerate with `CROZIER_UPDATE_SCHEMA=1 cargo test --lib schema`).

### Inspecting the effective config

`crozier config` loads the config exactly as a run would and prints, per
generator, each field's resolved value and the layer it came from (`cli`, `env`,
`generator`, `shared`, or `default`) — without running generation, so an
incomplete config is fine to inspect:

```text
$ crozier config
config files: crozier.yml

generator `python`
  type             python                       (generator)
  spec             ./openapi.yml                (shared)
  output           ./sdk/python                 (generator)
  package-name     (unset)                      (default)
  ...
  layout           packaged                     (default)
```

`layout` always shows the value a run would use, `packaged` when no layer sets it.

## Examples

Pure CLI, no config file:

```sh
crozier generate python --spec ./openapi.yml --output ./sdks/python --package-name my_api
```

One config, run everything:

```sh
crozier            # or `crozier generate`
```

Select one generator, override its output for this run:

```sh
crozier generate admin --output ./tmp/admin-preview
```

Point at an explicit config and override the package name via the environment:

```sh
CROZIER_PACKAGE_NAME=preview crozier --config ./ci/crozier.yml generate python
```
