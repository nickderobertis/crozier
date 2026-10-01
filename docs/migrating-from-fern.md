# Migrating from Fern

The README's [Migrating from Fern](../README.md#migrating-from-fern) section is
the process: crozier config beside the Fern config, `crozier compare` until every
generator matches, switch the build, remove the generator from `generators.yml`.
This page is what a migration may need beyond it, and what crozier now does
itself. The check, its report and the reference-command contract are in
[`compare.md`](compare.md); the script that produces Fern's side is the
[Fern reference recipe](fern-reference.md); the CI workflow is in
[`github-action.md`](github-action.md#migrating-from-fern).

## Steps a migration may still need

### Upgrade the Fern generator first

crozier certifies one pair, **Fern CLI 5.67.1** with **`fernapi/fern-python-sdk`
5.20.0**, under `pydantic_config.enum_type: python_enums` (the pair and setting
recorded in [`assets/scaffolding/metadata.json`](../assets/scaffolding/metadata.json)).
A generator on an older release (4.x, or an older release candidate) differs
from crozier wherever Fern's output changed since. So upgrade first, as its own
change:

```yaml
# fern/generators.yml
      - name: fernapi/fern-python-sdk
        version: 5.20.0
        config:
          pydantic_config:
            enum_type: python_enums
```

and set `"version": "5.67.1"` in `fern.config.json`. Regenerate with Fern and
review that diff on its own; only then compare against crozier, so the
comparison shows crozier's differences and not Fern's. Remove any
`pydantic_config.version` setting at the same time: crozier emits the default,
`both`, which carries both the pydantic v1 and v2 configuration (see the
[options table](#fern-generator-options)).

A team that stays on its own versions sets the recipe's
`FERN_REFERENCE_CLI_VERSION` and `FERN_REFERENCE_PYTHON_SDK_VERSION`, and should
expect differences, at least in `.fern/metadata.json`, which records the versions
([Certified versions](fern-reference.md#certified-versions)).

### Pin the Fern CLI the comparison runs

The `fern` launcher runs the CLI version a workspace's `fern.config.json` names
([What you need](fern-reference.md#what-you-need)), and only the certified pair is
known to match ([Certified versions](fern-reference.md#certified-versions)). The recipe writes the
certified `5.67.1` into the workspace it builds. A team that adapts it to run in
its own Fern workspace pins that file's `version` to the same release, never
`*` or a range, so the reference does not move under it.

### Apply overlays and overrides to the document

Fern applies a spec's `overrides` and then its `overlays`, both set on an
`api.specs[]` entry in `generators.yml` (Fern's
[Overlays](https://buildwithfern.com/learn/api-definitions/openapi/overlays) and
[Overrides](https://buildwithfern.com/learn/api-definitions/overrides) pages; the
keys are in
[`generators-yml.schema.json` at CLI 5.67.1](https://github.com/fern-api/fern/blob/b8414a6f56a875fc828f16af0d49ca93f22fd082/generators-yml.schema.json),
`generators.OpenAPISpecSchema`). crozier reads the document as given (overlay
support is tracked in
[#83](https://github.com/nickderobertis/crozier/issues/83)), so apply them first
and point `spec` at the result. For an overlay:

```sh
npx openapi-format@1.33.5 fern/openapi/openapi.yml \
  --overlayFile fern/openapi/overlay.yml --no-sort -o build/openapi.yml
```

`--no-sort` keeps the document's own order (`openapi-format` sorts by default).
Overrides are Fern's own format; Fern's Overlays page recommends overlays over
them, so rewrite an overrides file as an overlay and apply it the same way.
Apply them in Fern's order, overrides first. Run this before `crozier compare`
and before `crozier generate`.

### Convert Swagger 2.0 to OpenAPI 3

crozier reads OpenAPI 3.x only: given a Swagger 2.0 document it exits 1, naming
the missing `openapi` version field (Swagger support is tracked in
[#60](https://github.com/nickderobertis/crozier/issues/60)). Fern converts one
with `swagger2openapi` 7.0.8 and default options
([`convertOpenAPIV2ToV3.ts`](https://github.com/fern-api/fern/blob/b8414a6f56a875fc828f16af0d49ca93f22fd082/packages/cli/workspace/lazy-fern-workspace/src/utils/convertOpenAPIV2ToV3.ts),
version pinned in
[`pnpm-workspace.yaml`](https://github.com/fern-api/fern/blob/b8414a6f56a875fc828f16af0d49ca93f22fd082/pnpm-workspace.yaml),
both at CLI 5.67.1). Convert with the same release, and without `--patch`, which
Fern does not pass:

```sh
npx swagger2openapi@7.0.8 fern/openapi/swagger.yml -o build/openapi.json
```

### Keep your post-generation patches

Edits a build applies after generation (to `core/http_client.py`,
`core/serialization.py`, a return annotation in `__init__.py`, …) stay the
team's: `crozier compare` checks the generators' output before any patch, so
keep the patch step after `crozier generate` as it was after `fern generate`.
crozier's output equals Fern's apart from comments
([`matching.md`](matching.md)), so a patch that applied to Fern's output applies
to crozier's unless its context lines include a comment.

### Find Fern setups that scripts create

A script that builds a Fern workspace on the fly (`fern init --openapi` in a
temporary directory with a generators file it writes) leaves no
`generators.yml` in the repository, so the step-2 search does not list it. Find
them by the commands they run, leaving out your copy of the recipe:

<!-- migration-e2e: scripted-fern -->
```sh
grep -rnE --exclude=fern-reference.sh 'fern (init|generate)' .
```

Each one gets crozier config like any other generator; the recipe replaces it for
the comparison.

### Keep the comparison fast in CI

The reference time includes everything the command does, so a first `fern` run
counts the generator image download. Pull it before the comparison, as the
[example workflow](github-action.md#migrating-from-fern) does:

```sh
docker pull fernapi/fern-python-sdk:5.20.0
```

The report's per-generator reference and crozier times, speed-up and time saved
([Timings](compare.md#timings)) are what switching that generator saves on every
build.

To check only what a change touched, pass paths: `crozier compare
services/billing` searches one tree, `crozier compare ci/crozier.yml` checks one
config, and the Action's `paths` input does the same.

## What crozier now does itself

- **Output layout.** A generator whose Fern output went to a `local-file-system`
  path is a flat tree with no `src/` or `pyproject.toml`. crozier's
  [`layout` setting](configuration.md#output-layout) writes it directly: set
  `layout: flat` and point `output` where that tree lived. `crozier compare` and
  the Action then generate and compare the flat tree, and `crozier generate`
  writes it in place; nothing is copied. `layout: packaged`, the default, matches
  `fern generate --preview --output`.
- **Bracketed property names.** Properties such as `filter[name]` generate valid
  Python parameter names since crozier 0.0.22
  ([#74](https://github.com/nickderobertis/crozier/issues/74)).

## Fern generator options

The options are those `fernapi/fern-python-sdk` 5.20.0 accepts in a generator's
`config`, read from its `SDKCustomConfig` and `pydantic_config` models, both of
which refuse unknown keys:
[`sdk/custom_config.py`](https://github.com/fern-api/fern/blob/4d07e6aeeed1d88917ce59dfc9b4cf9e6008e553/generators/python/src/fern_python/generators/sdk/custom_config.py)
and
[`pydantic_model/custom_config.py`](https://github.com/fern-api/fern/blob/4d07e6aeeed1d88917ce59dfc9b4cf9e6008e553/generators/python/src/fern_python/generators/pydantic_model/custom_config.py),
at the commit that released 5.20.0. Defaults are Fern's.

**Default only** in the table means crozier has no setting for the option and
its output is Fern's at the default shown, the configuration crozier's goldens
are generated under. Remove the option from the Fern config before comparing.
A generator whose SDK relies on another value keeps a post-generation patch for
the difference, or stays on Fern.

### Naming and grouping

| Fern | Default | crozier |
| --- | --- | --- |
| `organization` (`fern.config.json`) | — | `package-name`: Fern names the module, the default `{Organization}Api` client class and the README heading after it ([Names](fern-reference.md#names)). |
| Distribution name | `default_package_name` under `--preview` | `project-name`. Under `packaged` the recipe reproduces only `default_package_name`; a `flat` tree has no distribution, so any value is accepted ([Names](fern-reference.md#names)). |
| Group `audiences` | none | `audiences`, with `audience-strict: true`: Fern's filter drops operations that carry no audience ([How each setting maps](fern-reference.md#how-each-setting-maps)). |

### Generator `config`

| Option | Default | crozier |
| --- | --- | --- |
| `client_class_name` | unset: `{Organization}Api` | `client-class-name`. |
| `client.class_name` | unset | `client-class-name`, as for `client_class_name`. |
| `client.filename` | `client.py` | Default only. |
| `client.exported_filename` | `client.py` | Default only. |
| `client.exported_class_name` | unset | Default only. |
| `client_filename` | unset | Default only. |
| `package_name` | unset | None: it renames the module and distribution but leaves the client class and README heading on the organization, which crozier cannot express ([Names](fern-reference.md#names)). Remove it and set the organization to the package name. |
| `package_path` | unset | Default only. |
| `use_api_name_in_package` | `false` | Default only. |
| `flat_layout` | `false` | Default only; `layout` matches Fern's two output modes. |
| `output_directory` | unset | Default only; `layout` matches Fern's two output modes. |
| `skip_formatting` | `false` | Default only. |
| `extra_dependencies` | `{}` | Default only. |
| `extra_dev_dependencies` | `{}` | Default only. |
| `extras` | `{}` | Default only. |
| `pyproject_python_version` | `^3.10` | Default only. |
| `pyproject_toml` | unset | Default only. |
| `include_union_utils` | `false` | Default only. |
| `additional_init_exports` | unset | Default only. |
| `exclude_types_from_init_exports` | `false` | Default only. |
| `custom_readme_sections` | unset | Default only. |
| `improved_imports` | `true` | Default only. |
| `lazy_imports` | `true` | Default only. |
| `import_paths` | unset | Default only. |
| `follow_redirects_by_default` | `true` | Default only. |
| `environment_class_name` | unset | Default only. |
| `inline_request_params` | `true` | Default only. |
| `inline_path_params` | `false` | Default only. |
| `flatten_union_request_bodies` | `false` | Default only. |
| `use_typeddict_requests` | `false` | Default only. |
| `use_typeddict_requests_for_file_upload` | `false` | Default only. |
| `use_inheritance_for_extended_models` | `true` | Default only. |
| `should_generate_websocket_clients` | `false` | Default only. |
| `timeout` | unset | Default only. |
| `timeout_in_seconds` | `60` | Default only. |
| `default_max_retries` (or `maxRetries`) | `2` | Default only. |
| `retry_status_codes` (or `retryStatusCodes`) | `legacy` | Default only. |
| `offset_semantics` (or `offsetSemantics`) | `item-index` | Default only. |
| `custom_pager_name` (or `custom-pager-name`) | unset | Default only. |
| `default_bytes_stream_chunk_size` | unset | Default only. |
| `recursion_limit` | unset | Default only. |
| `datetime_milliseconds` | `false` | Default only. |
| `omit_fern_headers` (or `omitFernHeaders`) | `false` | Default only. |
| `include_platform_headers` | `false` | Default only. |
| `use_request_defaults` | unset | Default only. |
| `custom_transport` | `false` | Default only. |
| `tcp_keepalive.enabled` | `false` | Default only. |
| `tcp_keepalive.idle_seconds` | `60` | Default only. |
| `tcp_keepalive.interval_seconds` | `30` | Default only. |
| `tcp_keepalive.count` | `5` | Default only. |
| `wire_tests.enabled` | `false` | Default only. |
| `wire_tests.exclusions` | unset | Default only. |
| `enable_wire_tests` | `false` | Default only. |
| `include_legacy_wire_tests` | `false` | Default only. |
| `mypy_exclude` | unset | Default only. |

### `pydantic_config`

| Option | Default | crozier |
| --- | --- | --- |
| `pydantic_config.enum_type` | `literals` | `python_enums` only: crozier always emits it. Set it in the Fern config when you upgrade. |
| `pydantic_config.use_str_enums` | `true` | None: Fern resets it from `enum_type`, so with `python_enums` it is `false`. Remove it. |
| `pydantic_config.version` | `both` | Default only: crozier emits both the pydantic v1 and v2 configuration. Remove `v1`, `v2` or `v1_on_v2`. |
| `pydantic_config.extra_fields` | `allow` | `extra-fields` (`allow`, `ignore`, `forbid`). |
| `pydantic_config.forbid_extra_fields` | `false` | None; Fern marks it deprecated for `extra_fields`. Replace `true` with `extra_fields: forbid`, which `extra-fields: forbid` matches. |
| `pydantic_config.frozen` | `true` | Default only. |
| `pydantic_config.orm_mode` | `false` | Default only. |
| `pydantic_config.smart_union` | `true` | Default only. |
| `pydantic_config.require_optional_fields` | `false` | Default only. |
| `pydantic_config.coerce_numbers_to_str` | `false` | Default only. |
| `pydantic_config.wrapped_aliases` | `false` | Default only. |
| `pydantic_config.positional_single_property_constructors` | `false` | Default only. |
| `pydantic_config.union_naming` | `v0` | Default only. |
| `pydantic_config.use_inheritance_for_extended_models` | `true` | None: Fern overwrites it with the top-level `use_inheritance_for_extended_models`. Remove it. |
| `pydantic_config.use_pydantic_field_aliases` | `false` | Default only. |
| `pydantic_config.recursion_limit` | unset | Default only. |
| `pydantic_config.include_validators` | `false` | Default only. |
| `pydantic_config.skip_formatting` | `false` | Default only. |
| `pydantic_config.include_union_utils` | `false` | Default only. |
| `pydantic_config.package_name` | unset | Default only. |
| `pydantic_config.skip_validation` | `false` | Default only. |
| `pydantic_config.use_provided_defaults` | `false` | Default only. |
| `pydantic_config.use_typeddict_requests` | `false` | Default only. |
