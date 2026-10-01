# A Fern reference for `crozier compare`

[`crozier compare`](compare.md) checks crozier's output against a reference SDK
that a command you configure produces. For a team moving from Fern, that
reference is Fern's own output for the same OpenAPI document. This page is a
copy-paste script that produces it: crozier does not ship or run it, and nothing
in crozier knows about Fern beyond the byte-match rules its output is compared
under ([`matching.md`](matching.md#how-the-comparison-works)).

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
| `LAYOUT` | Fern's output mode: `packaged` runs `fern generate --local --preview --output "$CROZIER_REFERENCE_OUTPUT"`, `flat` writes the tree to a `local-file-system` output whose `path` is `$CROZIER_REFERENCE_OUTPUT`; any other value exits non-zero naming it, without running `fern`. |
| `OUTPUT` | Where Fern writes, as `LAYOUT` describes. |

It also always sets `config.pydantic_config.enum_type: python_enums`, the enum
form crozier always emits, and sets `CI` and `GITHUB_ACTIONS` to `true` only when
they are unset (Fern records how it was invoked in `.fern/metadata.json`, and
crozier emits the form a CI run records).

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

for name in OUTPUT SPEC PACKAGE_NAME PROJECT_NAME CLIENT_CLASS_NAME \
  AUDIENCE_STRICT EXTRA_FIELDS LAYOUT; do
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

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/fern/openapi"
spec_name="$(basename "$CROZIER_REFERENCE_SPEC")"
cp "$CROZIER_REFERENCE_SPEC" "$work/fern/openapi/$spec_name"

cat > "$work/fern/fern.config.json" <<JSON
{ "organization": "$package", "version": "$FERN_CLI_VERSION" }
JSON

audiences=""
if [ -n "${CROZIER_REFERENCE_AUDIENCES:-}" ]; then
  audiences="    audiences:"$'\n'
  IFS=',' read -ra names <<<"$CROZIER_REFERENCE_AUDIENCES"
  for audience in "${names[@]}"; do
    audiences+="      - $audience"$'\n'
  done
fi

# A local-file-system output: the flat tree is written to its path. Under
# `--preview --output` the packaged tree goes to the --output directory instead,
# and Fern still needs this output to emit the plain package (without one it
# emits a publishable repository: CI workflow, poetry.lock, version 0.0.1).
output_path="$work/unused"
[ "$layout" = packaged ] || output_path="$out"

cat > "$work/fern/generators.yml" <<YAML
api:
  path: openapi/$spec_name
groups:
  crozier-reference:
${audiences}    generators:
      - name: fernapi/fern-python-sdk
        version: $FERN_PYTHON_SDK_VERSION
        config:
          client_class_name: $CROZIER_REFERENCE_CLIENT_CLASS_NAME
          pydantic_config:
            enum_type: python_enums
            extra_fields: $CROZIER_REFERENCE_EXTRA_FIELDS
        output:
          location: local-file-system
          path: $output_path
YAML

# Fern stamps how it was invoked into .fern/metadata.json; crozier emits the
# form a CI run records.
export CI="${CI:-true}"
export GITHUB_ACTIONS="${GITHUB_ACTIONS:-true}"

cd "$work/fern"
if [ "$layout" = packaged ]; then
  # `--preview` emits the packaged tree only with a non-empty token; nothing is
  # published, so a placeholder serves.
  export FERN_TOKEN="${FERN_TOKEN:-preview-only-no-publish}"
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
