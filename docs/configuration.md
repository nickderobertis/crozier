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

| Command | What it runs |
| --- | --- |
| `crozier` | Every configured generator (the built-in `python` when none are configured). |
| `crozier generate` | Same as bare `crozier`. |
| `crozier generate <name>` | The one generator named `<name>` (a config entry, or the built-in `python`). |

## Precedence

Every field is resolved highest-wins:

```text
CLI flag  >  CROZIER_* env var  >  generators.<name>.<field>  >  top-level <field>  >  built-in default
```

- **CLI flags** — `--spec`, `--output`, `--package-name`, `--project-name`,
  `--audience` (repeatable), `--audience-strict`. These apply to a *single*
  generator; passing them while more than one would run is an error (name one,
  or move the values into the config file).
- **Environment** — `CROZIER_SPEC`, `CROZIER_OUTPUT`, `CROZIER_PACKAGE_NAME`,
  `CROZIER_PROJECT_NAME`, `CROZIER_AUDIENCES` (comma-separated),
  `CROZIER_AUDIENCE_STRICT`. Empty values count as unset. These are a global
  override layer applied to every selected generator.
- **Config file** — a `generators.<name>` value beats the shared top-level value
  of the same field.
- **Built-in defaults** — `package-name` defaults to a `snake_case` of the API
  title; `project-name` defaults to the package name; audiences default to empty
  (the whole API). `spec` and `output` have no default — a generator resolved
  without either is an actionable error.

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

generators:
  python:
    type: python          # optional; `python` is the only type today (and the default)
    spec: ./openapi.yml    # any shared field can be overridden per generator
    output: ./sdks/python
    package-name: my_api
    project-name: my-api
    audiences: [public]
    audience-strict: false
  admin:
    spec: ./admin-openapi.yml
    output: ./sdks/admin
    package-name: admin_api
```

Unknown fields and unknown generator types are rejected at parse time, with the
offending file's path in the error. Generators run in declaration order.

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
