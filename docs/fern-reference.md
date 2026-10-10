# A Fern reference for `crozier compare`

`crozier compare` checks crozier's output against a reference SDK
that a command you configure produces. For a team moving from Fern, that
reference is Fern's own output for the same OpenAPI document. This page is a
copy-paste script that produces it: crozier does not ship or run it, and nothing
in crozier knows about Fern beyond the byte-match rules its output is compared
under.

## What you need

- the [`fern`](https://www.npmjs.com/package/fern-api) CLI launcher on `PATH`
  (`npm install -g fern-api`); it fetches the CLI version the script pins;
- Docker, running: Fern runs its Python generator as the
  `fernapi/fern-python-sdk` container image.

## Certified versions

crozier certifies one pair: **Fern CLI 5.67.1** with **`fernapi/fern-python-sdk`
5.20.0** (the pair recorded in crozier's
[`assets/scaffolding/metadata.json`](../assets/scaffolding/metadata.json)). The
script defaults to it. Each version can be overridden through the script's own
environment variables, `FERN_REFERENCE_CLI_VERSION` and
`FERN_REFERENCE_PYTHON_SDK_VERSION`, but only the certified pair is known to
match: another pair differs at least in `.fern/metadata.json`, which records the
versions, and may differ anywhere else Fern changed its output.

Under that pair both of crozier's enum forms are certified, each against the
Fern configuration it names: `enum-type: python-enums` against
`pydantic_config.enum_type: python_enums`, and `enum-type: literals` against
`enum_type` unset, fern-python-sdk's `literals` default. crozier's corpus gate
holds every corpus document to the `python_enums` output (`expected/`) and a
targeted set reaching every enum shape to the `literals` output
(`expected-literals/`), and the script
writes whichever one the generator is configured with (see `ENUM_TYPE` below).
`default-max-retries` is certified the same way against Fern's
`default_max_retries` (at `0`, on a targeted pair of corpora); the script
writes it whenever it is not the shared default of `2` (see
`DEFAULT_MAX_RETRIES` below).

## Use it

Save the script as `scripts/fern-reference.sh` in your repository, make it
executable (`chmod +x`), and name it in `crozier.yml`:

```yaml
reference:
  command: ./scripts/fern-reference.sh   # relative to this config file's directory
```

Then run `crozier compare`. Pull the generator image first so a one-time
download is not counted in the first generator's reference time:

```sh
docker pull fernapi/fern-python-sdk:5.20.0
crozier compare
```

## How each setting maps

The script builds a temporary Fern workspace from the `CROZIER_REFERENCE_*`
environment `crozier compare` passes, runs Fern, and leaves the reference SDK in
`$CROZIER_REFERENCE_OUTPUT`. Every value it reads, and what it does with it:

| `CROZIER_REFERENCE_*` | What the script does |
| --- | --- |
| `SPEC` | Copied into the workspace's `openapi/` directory (file name kept) and named as `api.path` in `generators.yml`. |
| `PACKAGE_NAME` | Becomes the `organization` in `fern.config.json`: Fern names the module, the `{Organization}Api` default client class and the README heading after it. A value Fern cannot reproduce makes the script exit non-zero naming it (see [Names](#names)). |
| `PROJECT_NAME` | Not written. Under `packaged` it must be `default_package_name`, Fern's fixed distribution name, or the script exits non-zero naming it; under `flat` it is not read further, since a flat tree has no distribution (see [Names](#names)). |
| `CLIENT_CLASS_NAME` | The generator's `config.client_class_name`. |
| `AUDIENCES` | The group's `audiences:` list (comma-separated values, one entry each); no `audiences:` key when empty. |
| `AUDIENCE_STRICT` | Not written: Fern has no such setting. Its group `audiences:` filter always drops operations that carry no audience, which is crozier's `audience-strict: true`. With `false`, crozier keeps those operations and a document that has any reports `mismatched`. |
| `EXTRA_FIELDS` | The generator's `config.pydantic_config.extra_fields`. |
| `ENUM_TYPE` | `python-enums` sets the generator's `config.pydantic_config.enum_type: python_enums`; `literals` leaves `enum_type` unset, Fern's `literals` default; any other value exits non-zero naming it, without running `fern`. |
| `DEFAULT_MAX_RETRIES` | The generator's `config.default_max_retries` when it is not `2`, Fern's default; at `2` no key is written. A value that is not a non-negative integer exits non-zero naming it, without running `fern`. |
| `LAYOUT` | Fern's output mode: `packaged` runs `fern generate --local --preview --output "$CROZIER_REFERENCE_OUTPUT"`, `flat` writes the tree to a `local-file-system` output whose `path` is `$CROZIER_REFERENCE_OUTPUT`; any other value exits non-zero naming it, without running `fern`. |
| `OUTPUT` | Where Fern writes, as `LAYOUT` describes. |

It also sets `CI` and `GITHUB_ACTIONS` to `true` only when
they are unset (Fern records how it was invoked in `.fern/metadata.json`, and
crozier emits the form a CI run records).

Each value is written into the workspace quoted, exactly as given; a value
holding a control character (a line break, say) is refused before `fern` runs.

### Layouts

| `layout` | Fern run |
| --- | --- |
| `packaged` | `fern generate --group crozier-reference --local --preview --output "$CROZIER_REFERENCE_OUTPUT" --force`, with `FERN_TOKEN` set to a placeholder only when unset (`--preview` emits the packaged tree only with a non-empty token; nothing is published). Fern writes the package into one subdirectory, which `compare` takes as the reference. The group still carries a `local-file-system` output, pointed at a scratch directory: without one, Fern emits a publishable repository instead (CI workflow, `poetry.lock`, version `0.0.1`). |
| `flat` | `fern generate --group crozier-reference --local --force`, with the group's `local-file-system` output `path` set to `$CROZIER_REFERENCE_OUTPUT`, an absolute path, which Fern accepts. No `--preview`, and `FERN_TOKEN` unset for the run: the flat tree was measured from a token-less run. |

### Names

Measured with Fern CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0:

- **Packaged.** Fern emits its packaged tree with a placeholder token only for
  the organization `fern`: with `acme` it falls back to the flat module tree. Its
  packaged distribution is then `default_package_name`. So under `packaged` the
  script reproduces only package `fern` with project `default_package_name`, the
  names crozier's own Fern goldens are produced under, and exits non-zero naming
  any other package or project name. Fern's `package_name` option is no way out:
  it renames the module and distribution but leaves the client class and the
  README heading on the organization, which crozier cannot express.
- **Flat.** Any organization made of lowercase letters, digits and underscores,
  starting with a letter, names the module as given (`acme`, `acme2` and
  `my_api` all matched crozier). `my-api` did not: Fern renamed the module
  `my_api`. The script exits non-zero naming a package name outside that shape.
  The flat tree has no distribution, so any project name is accepted.

A team whose generators use their own package names can therefore compare them
under `layout: flat`, whatever layout it ships.

## Vendor extensions

The document both tools read may carry Fern's `x-fern-*` extensions. crozier
reads each one below in Fern's spelling and in its own `x-crozier-*` alias; when
a node carries both, the alias wins
([dual-header policy](matching.md#fern-compatible-extension-policy)). An
extension not listed here does not change crozier's output.

| Fern | crozier alias | On | Effect |
| --- | --- | --- | --- |
| `x-fern-audiences` | `x-crozier-audiences` | operation | The audience labels the `audiences` setting filters on. |
| `x-fern-ignore` | `x-crozier-ignore` | operation, component schema, parameter | Leaves the node out of the SDK. |
| `x-fern-sdk-group-name` | `x-crozier-sdk-group-name` | operation, component schema | On an operation, the sub-client the method belongs to (a list nests it), honoured only beside a method name; on a component, the package its type is written into. |
| `x-fern-sdk-method-name` | `x-crozier-sdk-method-name` | operation | The method's name. A sequence of strings is read joined by `,`, as Fern reads it (`[fetch]` is `fetch`). |
| `x-fern-sdk-method-name` | `x-crozier-sdk-method-name` | request-body media | Each named representation generates its own method; the crozier spelling wins on that media node. |
| `x-fern-pagination` | `x-crozier-pagination` | operation | Returns a pager over the response's items. |
| `x-fern-streaming` | `x-crozier-streaming` | operation | Streams the response: `format: sse` as Server-Sent Events, which a `terminator` ends; `true` or `format: json` as JSON lines; `false`, like no extension, leaves the response's media types to decide. A `stream-condition` splits the method in two. |
| `x-fern-enum` | `x-crozier-enum` | string enum schema | The member name for each value. |
| `x-fern-property-name` | `x-crozier-property-name` | object property | The property's Python name, both the model field and the request keyword argument. Its JSON key on the wire stays the property's key. |
| `x-fern-header` | `x-crozier-header` | header `apiKey` security scheme | The credential's constructor parameter (`name`), the text its value is sent behind (`prefix`), and the environment variable it defaults to (`env`). On a second header scheme, whose credential is a promoted header, `name` and `env` apply but Fern sends no `prefix`. |
| `x-fern-bearer` | `x-crozier-bearer` | http `bearer` security scheme | The credential's constructor parameter (`name`) and the environment variable it defaults to (`env`). |
| `x-fern-token-variable-name` | `x-crozier-token-variable-name` | http `bearer` security scheme | The credential's constructor parameter, when the bearer extension names none. |
| `x-fern-basic` | `x-crozier-basic` | http `basic` security scheme | The `username` and `password` parameters' `name` and `env`. For this and the three rows above, a credential name that is a Python keyword is escaped as Fern escapes it (`class` is `class_`); one naming a client constructor parameter (`timeout`, `headers`, …) is refused, exit 1, asking for another name. |
| `x-fern-server-name` | `x-crozier-server-name` | server | The environment member's name (`primary` is `PRIMARY`); every server naming itself is a member, the first the default. On an operation's own server, a field of the environment object beside `base` that the operation's requests read. A keyword field is escaped (`class_`); a name making a digit-led member, or an operation server named `base`, is refused, exit 1. |
| `x-fern-default-url` | `x-crozier-default-url` | server | The environment member's value, in place of the expanded `url`. |
| `x-fern-idempotency-headers` | `x-crozier-idempotency-headers` | document | The headers (`[{header: X-Dedupe-Token}]`) an idempotent operation takes. |
| `x-fern-idempotent` | `x-crozier-idempotent` | operation | Gives the method an optional argument per idempotency header after its body fields (`dedupe_token`), sent as that header. |
| `x-fern-retries` | `x-crozier-retries` | operation | `{disabled: true}` sends the request with `max_retries` 0, whatever the caller's options say. |
| `x-fern-webhook` | `x-crozier-webhook` | path operation | `true` leaves the operation out of the client; the schemas it names stay ordinary types. |
| `x-fern-base-path` | `x-crozier-base-path` | document | A path every route sits under: a string, or an object with `path`, `paths-include-base-path` and `parameters`. Each `{placeholder}` in the object form's `path` leaves every method and becomes a client constructor argument, `Optional[str]` with the `default` a `parameters` map entry gives it, else a required `str`. |
| `x-fern-parameter-name` | `x-crozier-parameter-name` | parameter | Names the SDK argument while retaining the parameter wire name. |
| `x-fern-default` | `x-crozier-default` | query parameter | Supplies the generated argument default. |
| `x-fern-sdk-variables` | `x-crozier-sdk-variables` | document | Declares client constructor variables. |
| `x-fern-sdk-variable` | `x-crozier-sdk-variable` | path parameter | Reads a declared client variable instead of taking a method argument. |
| `x-fern-global-headers` | `x-crozier-global-headers` | document | Declares client constructor arguments sent as headers. |
| `x-fern-version` | `x-crozier-version` | document | Refuses a version header also declared as a required operation parameter. |

The parameter-extension alias gate reads these spellings and placements from
this table, then checks their complete generated output. Its header refusal
control does the same for the version extension.

## The script

```bash
#!/usr/bin/env bash
# Write a Fern reference SDK for `crozier compare` into $CROZIER_REFERENCE_OUTPUT,
# from the generator settings crozier passes as CROZIER_REFERENCE_*.
# See https://github.com/nickderobertis/crozier/blob/main/docs/fern-reference.md
set -euo pipefail

# The Fern CLI and generator versions crozier certifies; override either here.
FERN_CLI_VERSION="${FERN_REFERENCE_CLI_VERSION:-5.67.1}"
FERN_PYTHON_SDK_VERSION="${FERN_REFERENCE_PYTHON_SDK_VERSION:-5.20.0}"

fail() {
  echo "fern-reference: $*" >&2
  exit 1
}

# A value as a double-quoted YAML (and JSON) string, so characters YAML gives a
# meaning to (`:`, `#`, `{`, quotes) reach Fern as written. A control character
# cannot be carried that way, so it is refused.
quote() {
  if [[ "$1" =~ [[:cntrl:]] ]]; then
    fail "value '$1' holds a control character, which the Fern workspace cannot carry"
  fi
  printf '"%s"' "$(printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"
}

for name in OUTPUT SPEC PACKAGE_NAME PROJECT_NAME CLIENT_CLASS_NAME \
  AUDIENCE_STRICT EXTRA_FIELDS ENUM_TYPE DEFAULT_MAX_RETRIES LAYOUT; do
  var="CROZIER_REFERENCE_$name"
  [ -n "${!var:-}" ] || fail "$var is not set; run this as a crozier compare reference command"
done
out="$CROZIER_REFERENCE_OUTPUT"
package="$CROZIER_REFERENCE_PACKAGE_NAME"
project="$CROZIER_REFERENCE_PROJECT_NAME"
layout="$CROZIER_REFERENCE_LAYOUT"

# Fern names the module, the `{Organization}Api` client class and the README
# heading after the workspace organization, so the package name becomes it.
case "$layout" in
  packaged)
    # Fern emits the packaged tree only for the `fern` organization, whose
    # distribution is always `default_package_name`.
    [ "$package" = fern ] || fail "package name '$package' cannot be reproduced under the packaged layout: Fern emits its packaged form only for the organization 'fern'; set package-name: fern, or compare under layout: flat"
    [ "$project" = default_package_name ] || fail "project name '$project' cannot be reproduced under the packaged layout: Fern's packaged distribution is always 'default_package_name'"
    ;;
  flat)
    # Measured: `acme`, `acme2` and `my_api` name Fern's module as given;
    # `my-api` does not (Fern renames it `my_api`), so only this shape is passed.
    [[ "$package" =~ ^[a-z][a-z0-9_]*$ ]] || fail "package name '$package' cannot be reproduced: Fern names the module after the organization, which reproduces only lowercase letters, digits and underscores, starting with a letter"
    # A flat tree has no distribution, so the project name reaches none of its files.
    ;;
  *)
    fail "unknown layout '$layout': expected packaged or flat"
    ;;
esac

# crozier's `python-enums` is Fern's `enum_type: python_enums`; its `literals` is
# Fern with `enum_type` unset, which is fern-python-sdk's `literals` default.
case "$CROZIER_REFERENCE_ENUM_TYPE" in
  python-enums) enum_type="            enum_type: python_enums"$'\n' ;;
  literals) enum_type="" ;;
  *)
    fail "unknown enum type '$CROZIER_REFERENCE_ENUM_TYPE': expected python-enums or literals"
    ;;
esac

# Fern's `default_max_retries` defaults to 2, as crozier's does; only another
# value is written.
retries="$CROZIER_REFERENCE_DEFAULT_MAX_RETRIES"
[[ "$retries" =~ ^(0|[1-9][0-9]*)$ ]] || fail "default max retries '$retries' is not a non-negative integer"
default_max_retries=""
[ "$retries" = 2 ] || default_max_retries="          default_max_retries: $retries"$'\n'

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/fern/openapi"
spec_name="$(basename "$CROZIER_REFERENCE_SPEC")"
cp "$CROZIER_REFERENCE_SPEC" "$work/fern/openapi/$spec_name"

# Every value written into the workspace, quoted first: a refusal inside a
# here-document would not stop the script.
q_package="$(quote "$package")"
q_cli_version="$(quote "$FERN_CLI_VERSION")"
q_spec_path="$(quote "openapi/$spec_name")"
q_sdk_version="$(quote "$FERN_PYTHON_SDK_VERSION")"
q_client="$(quote "$CROZIER_REFERENCE_CLIENT_CLASS_NAME")"
q_extra_fields="$(quote "$CROZIER_REFERENCE_EXTRA_FIELDS")"

cat > "$work/fern/fern.config.json" <<JSON
{ "organization": $q_package, "version": $q_cli_version }
JSON

audiences=""
if [ -n "${CROZIER_REFERENCE_AUDIENCES:-}" ]; then
  audiences="    audiences:"$'\n'
  IFS=',' read -ra names <<<"$CROZIER_REFERENCE_AUDIENCES"
  for audience in "${names[@]}"; do
    audiences+="      - $(quote "$audience")"$'\n'
  done
fi

# A local-file-system output: the flat tree is written to its path. Under
# `--preview --output` the packaged tree goes to the --output directory instead,
# and Fern still needs this output to emit the plain package (without one it
# emits a publishable repository: CI workflow, poetry.lock, version 0.0.1).
output_path="$work/unused"
[ "$layout" = packaged ] || output_path="$out"
q_output_path="$(quote "$output_path")"

cat > "$work/fern/generators.yml" <<YAML
api:
  path: $q_spec_path
groups:
  crozier-reference:
${audiences}    generators:
      - name: fernapi/fern-python-sdk
        version: $q_sdk_version
        config:
          client_class_name: $q_client
${default_max_retries}          pydantic_config:
${enum_type}            extra_fields: $q_extra_fields
        output:
          location: local-file-system
          path: $q_output_path
YAML

# Fern stamps how it was invoked into .fern/metadata.json; crozier emits the
# form a CI run records.
export CI="${CI-true}"
export GITHUB_ACTIONS="${GITHUB_ACTIONS-true}"

cd "$work/fern"
if [ "$layout" = packaged ]; then
  # `--preview` emits the packaged tree only with a non-empty token; nothing is
  # published, so a placeholder serves.
  export FERN_TOKEN="${FERN_TOKEN-preview-only-no-publish}"
  fern generate --group crozier-reference --local --preview --output "$out" --force >&2
else
  # The flat tree is what a token-less local run writes, as measured.
  unset FERN_TOKEN
  fern generate --group crozier-reference --local --force >&2
fi
```

The script writes only to `$CROZIER_REFERENCE_OUTPUT` and a temporary directory
it removes. What `fern` and Docker do beyond that (caches, pulled images) is
theirs.
