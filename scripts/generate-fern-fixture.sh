#!/usr/bin/env bash
# Generate Fern's Python SDK output for a fixture's OpenAPI spec, strip comments,
# and install it as that fixture's golden `expected/` tree.
#
# By default produces the *packaged* SDK (a pip package: `src/<pkg>/…` +
# pyproject.toml + README.md/reference.md + .fern/) via `fern generate --preview`,
# which is the form the committed corpus vendors and needs no publishing
# credentials. `--layout flat` instead produces Fern's *flat* module tree — what
# `fern generate --local` writes to a `local-file-system` output path without
# `--preview` — and installs it as the fixture's `expected-flat/` golden. A flat
# golden must be declared in tests/fixtures/flat-goldens.txt. String enums
# render as real `enum.Enum` classes (`pydantic_config.enum_type: python_enums`) to
# match crozier's default — see docs/matching.md. `--enum-type literals` instead
# leaves `enum_type` unset (Fern's open `Literal`-union default, crozier's
# `enum-type: literals`) and installs `expected-literals/`: only the files that
# differ from the fixture's committed `expected/`, plus a manifest naming the
# files Fern omits (scripts/golden_overlay.py). `--default-max-retries N` sets
# Fern's `default_max_retries: N` and installs `expected-default-max-retries/`,
# the same kind of overlay, for crozier's `default-max-retries`.
#
# Fern's generator only runs under a container runtime (Docker/Podman), which is
# not available in every environment — so this is a SEPARATE, opt-in script, not
# part of `just fixtures-refresh`'s default offline path. Run it on a machine
# with Docker; it produces tests/fixtures/<fixture>/expected/.
#
# Requirements:
#   - Docker running (Fern runs the generator image locally)
#   - fern CLI:  npm i -g fern-api    (invoked as `fern`)
#   - crozier built (for the comment stripper):  cargo build --release
#
# Usage:  scripts/generate-fern-fixture.sh [--layout packaged|flat] [--enum-type python-enums|literals] [--default-max-retries N] [FIXTURE] [FERN_PYTHON_VERSION] [SPEC_PATH] [DEST_PATH]
#   --layout            `packaged` (default) installs expected/; `flat` installs
#                       expected-flat/ from Fern's local-file-system output.
#   --enum-type         `python-enums` (default) or `literals`, which installs
#                       the packaged expected-literals/ overlay of expected/.
#   --default-max-retries  a non-negative integer for Fern's default_max_retries;
#                       installs the packaged expected-default-max-retries/
#                       overlay of expected/.
#   FIXTURE             fixture dir under tests/fixtures/ (default: exhaustive).
#                       e.g. auth-schemes, inline-request-response, integer-enums.
#   FERN_PYTHON_VERSION defaults to the latest stable tag resolved by the same
#                       Docker Hub distribution lookup as `fern-goldens`.
#   SPEC_PATH           optional OpenAPI file to generate from instead of
#                       tests/fixtures/<fixture>/openapi.yml (or, for a flat
#                       golden, the spec its flat-goldens.txt row names); useful
#                       for fetched, unvendored source specs.
#   DEST_PATH           optional automation-only destination. It must be an
#                       `expected` (packaged) or `expected-flat` (flat) directory
#                       below this fixture; the default is
#                       tests/fixtures/<fixture>/expected[-flat].
set -euo pipefail

. "$(cd "$(dirname "$0")" && pwd)/lib.sh"

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

LAYOUT=packaged
ENUM_TYPE=python-enums
DEFAULT_MAX_RETRIES=""
while [ "${1:-}" = "--layout" ] || [ "${1:-}" = "--enum-type" ] || [ "${1:-}" = "--default-max-retries" ]; do
  [ "$#" -ge 2 ] || {
    echo "generate-fern-fixture: $1 needs a value" >&2
    exit 1
  }
  case "$1" in
    --layout) LAYOUT="$2" ;;
    --enum-type) ENUM_TYPE="$2" ;;
    --default-max-retries) DEFAULT_MAX_RETRIES="$2" ;;
  esac
  shift 2
done
case "$LAYOUT" in
  packaged) golden_name=expected ;;
  flat) golden_name=expected-flat ;;
  *)
    echo "generate-fern-fixture: invalid layout '$LAYOUT' — use packaged or flat" >&2
    exit 1
    ;;
esac
case "$ENUM_TYPE" in
  python-enums) ;;
  literals)
    [ "$LAYOUT" = packaged ] || {
      echo "generate-fern-fixture: --enum-type literals only produces a packaged golden" >&2
      exit 1
    }
    golden_name=expected-literals
    ;;
  *)
    echo "generate-fern-fixture: invalid enum type '$ENUM_TYPE' — use python-enums or literals" >&2
    exit 1
    ;;
esac
if [ -n "$DEFAULT_MAX_RETRIES" ]; then
  [[ "$DEFAULT_MAX_RETRIES" =~ ^(0|[1-9][0-9]*)$ ]] || {
    echo "generate-fern-fixture: invalid default max retries '$DEFAULT_MAX_RETRIES' — use a non-negative integer" >&2
    exit 1
  }
  [ "$LAYOUT" = packaged ] && [ "$ENUM_TYPE" = python-enums ] || {
    echo "generate-fern-fixture: --default-max-retries only produces a packaged python-enums golden" >&2
    exit 1
  }
  golden_name=expected-default-max-retries
fi

FIXTURE="${1:-exhaustive}"
# FIXTURE is spliced into paths that are later `rm -rf`'d, so hold it to a single
# safe path segment (shared valid_fixture_name; rejects traversal/option injection).
valid_fixture_name "$FIXTURE" || {
  echo "generate-fern-fixture: invalid fixture name '$FIXTURE' — must be a single" \
       "path segment matching [A-Za-z0-9][A-Za-z0-9._-]* (a dir under tests/fixtures/)" >&2
  exit 1
}
# fern-goldens always supplies its already-resolved exact version. Direct local
# calls use that tool's identical Docker Hub resolver instead of a second pin.
FERN_PYTHON_VERSION="${2:-}"
[ -z "$FERN_PYTHON_VERSION" ] || valid_fern_version "$FERN_PYTHON_VERSION" || {
  echo "generate-fern-fixture: invalid Fern version '$FERN_PYTHON_VERSION' — use an exact semantic version such as 5.20.0" >&2
  exit 1
}
SPEC_OVERRIDE="${3:-}"
# The Fern CLI version, pinned via fern.config.json's `version` (the `fern` npm
# package is only a launcher; this field selects the actual CLI it runs). Matches
# the corpus's `.fern/metadata.json` cliVersion so regenerated output stays
# consistent; a `*` here would float to the latest CLI and can drift the output.
FERN_CLI_VERSION="${FERN_CLI_VERSION:-5.67.1}"

# A flat golden is declared in one table, which also names the fixture whose
# vendored spec it generates from when the golden's own directory has none (a
# second flat golden over an already-vendored document, differing by a setting).
spec_fixture="$FIXTURE"
if [ "$LAYOUT" = flat ]; then
  flat_table="$repo_root/tests/fixtures/flat-goldens.txt"
  declared=""
  if [ -f "$flat_table" ]; then
    while IFS='|' read -r flat_fixture flat_spec; do
      case "$flat_fixture" in ""|\#*) continue ;; esac
      [ "$flat_fixture" = "$FIXTURE" ] || continue
      declared=1
      [ -z "$flat_spec" ] || spec_fixture="$flat_spec"
    done < "$flat_table"
  fi
  [ -n "$declared" ] || {
    echo "generate-fern-fixture: '$FIXTURE' is not a declared flat golden — add it to" \
         "tests/fixtures/flat-goldens.txt first" >&2
    exit 1
  }
  valid_fixture_name "$spec_fixture" || {
    echo "generate-fern-fixture: invalid spec fixture '$spec_fixture' for '$FIXTURE' in $flat_table" >&2
    exit 1
  }
fi

spec="${SPEC_OVERRIDE:-$repo_root/tests/fixtures/$spec_fixture/openapi.yml}"
# A flat golden over another fixture may name a registered corpus row whose source
# is committed under tests/fixtures/corpus-sources/ rather than vendored beside a
# fixture: the same lookup tests/e2e.rs's `corpus_spec` makes.
if [ -z "$SPEC_OVERRIDE" ] && [ "$spec_fixture" != "$FIXTURE" ] && [ ! -f "$spec" ]; then
  for candidate in openapi.json openapi.yaml openapi.yml; do
    committed="$repo_root/tests/fixtures/corpus-sources/$spec_fixture/$candidate"
    if [ -f "$committed" ]; then
      spec="$committed"
      break
    fi
  done
fi
fixture_dir="$repo_root/tests/fixtures/$FIXTURE"
dest="${4:-$fixture_dir/$golden_name}"
[ "$(basename "$dest")" = "$golden_name" ] || {
  echo "generate-fern-fixture: invalid destination '$dest' — its final path segment must be $golden_name" >&2
  exit 1
}
fixture_dir="$(cd "$fixture_dir" 2>/dev/null && pwd -P)" || {
  echo "generate-fern-fixture: fixture directory does not exist: $fixture_dir" >&2
  exit 1
}
dest_parent="$(cd "$(dirname "$dest")" 2>/dev/null && pwd -P)" || {
  echo "generate-fern-fixture: destination parent does not exist: $(dirname "$dest")" >&2
  exit 1
}
case "$dest_parent" in
  "$fixture_dir" | "$fixture_dir"/*) dest="$dest_parent/$golden_name" ;;
  *)
    echo "generate-fern-fixture: invalid destination '$dest' — it must stay below $fixture_dir" >&2
    exit 1
    ;;
esac

# Fixture-owned non-default settings are declarative so automated and local
# generation cannot silently refresh a golden with Fern's defaults. Explicit
# environment values remain available for diagnostics and take precedence.
fixture_config="$repo_root/tests/fixtures/fern-generator-config.txt"
configured_audiences=""
configured_audience_strict=""
configured_client_class_name=""
configured_extra_fields=""
configured_organization=""
if [ -f "$fixture_config" ]; then
  while IFS='|' read -r configured_fixture audiences strict client extra organization; do
    case "$configured_fixture" in ""|\#*) continue ;; esac
    [ "$configured_fixture" = "$FIXTURE" ] || continue
    [ -z "$configured_audience_strict" ] || {
      echo "generate-fern-fixture: duplicate configuration for '$FIXTURE' in $fixture_config" >&2
      exit 1
    }
    configured_audiences="$audiences"
    configured_audience_strict="$strict"
    configured_client_class_name="$client"
    configured_extra_fields="$extra"
    configured_organization="$organization"
  done < "$fixture_config"
fi
FERN_AUDIENCES="${FERN_AUDIENCES:-$configured_audiences}"
AUDIENCE_STRICT="${AUDIENCE_STRICT:-$configured_audience_strict}"
CLIENT_CLASS_NAME="${CLIENT_CLASS_NAME:-$configured_client_class_name}"
EXTRA_FIELDS="${EXTRA_FIELDS:-$configured_extra_fields}"
ORGANIZATION="${ORGANIZATION:-$configured_organization}"
case "$AUDIENCE_STRICT" in ""|true|false) ;; *)
  echo "generate-fern-fixture: invalid audience_strict '$AUDIENCE_STRICT' for '$FIXTURE'" >&2
  exit 1
esac
case "$EXTRA_FIELDS" in ""|allow|ignore|forbid) ;; *)
  echo "generate-fern-fixture: invalid extra_fields '$EXTRA_FIELDS' for '$FIXTURE'" >&2
  exit 1
esac
# Letters and digits, starting with a letter. Capitals are admitted: an
# organization with an inner capital (`PetStore`) is what names a mixed-case
# module and `{Organization}Api` client, which crozier derives from a mixed-case
# `--package-name`.
[ -z "$ORGANIZATION" ] || [[ "$ORGANIZATION" =~ ^[A-Za-z][A-Za-z0-9]*$ ]] || {
  echo "generate-fern-fixture: invalid organization '$ORGANIZATION' for '$FIXTURE' — use letters and digits, starting with a letter" >&2
  exit 1
}

if [ -z "$FERN_PYTHON_VERSION" ]; then
  FERN_PYTHON_VERSION="$("$repo_root/scripts/fern-goldens" latest-version)"
  valid_fern_version "$FERN_PYTHON_VERSION" || {
    echo "generate-fern-fixture: latest-version returned invalid Fern version '$FERN_PYTHON_VERSION'" >&2
    exit 1
  }
fi

need() { command -v "$1" >/dev/null 2>&1 || { echo "generate-fern-fixture: '$1' not found — $2" >&2; exit 1; }; }
need fern "install it: npm i -g fern-api"
need docker "start Docker; Fern runs its generator as a local container"
[ -f "$spec" ] || { echo "generate-fern-fixture: missing spec $spec" >&2; exit 1; }

crozier_bin="$repo_root/target/release/crozier"
[ -x "$crozier_bin" ] || { echo "generate-fern-fixture: build crozier first (cargo build --release)" >&2; exit 1; }

workdir="$(mktemp -d)"
publish_stage=""
cleanup() {
  rm -rf "$workdir"
  [ -z "$publish_stage" ] || rm -rf "$publish_stage"
}
trap cleanup EXIT

# Scaffold a minimal Fern workspace around the vendored OpenAPI spec. We ignore
# Fern's definition files by construction: only the OpenAPI document is wired in.
mkdir -p "$workdir/fern/openapi"
api_path="openapi/openapi.yml"
if [ -n "$SPEC_OVERRIDE" ]; then
  tree_root="$(python3 "$repo_root/scripts/corpus_remote_ref_pins.py" tree-root "$FIXTURE")"
  if [ -n "$tree_root" ]; then
    tree_dir="${spec%/"$tree_root"}"
    [ "$tree_dir" != "$spec" ] && [ -d "$tree_dir" ] || {
      echo "generate-fern-fixture: $spec is not the pinned tree root $tree_root; fetch the complete tree with scripts/fetch-corpus.sh and pass its root" >&2
      exit 1
    }
    python3 "$repo_root/scripts/corpus_remote_ref_pins.py" verify-tree "$FIXTURE" "$tree_dir" >/dev/null
    cp -R "$tree_dir/." "$workdir/fern/openapi/"
    api_path="openapi/$tree_root"
  else
    cp "$spec" "$workdir/fern/openapi/openapi.yml"
  fi
else
  cp "$spec" "$workdir/fern/openapi/openapi.yml"
fi
# Optional organization: ORGANIZATION=<name> replaces Fern's `fern` organization,
# which is what names the SDK's module, its `{Organization}Api` client class and
# its README heading — the three names crozier derives from `--package-name`
# (see docs/matching.md). Fern's own `package_name` option instead renames the
# module and distribution while the client and README keep the organization,
# which crozier cannot express, so it is deliberately not a knob here. Fern emits
# the packaged form only for the `fern` organization without a real FERN_TOKEN,
# so a non-default organization is for flat goldens.
cat > "$workdir/fern/fern.config.json" <<JSON
{ "organization": "${ORGANIZATION:-fern}", "version": "${FERN_CLI_VERSION}" }
JSON
# Optional audience filter (issue #41 gap 3): FERN_AUDIENCES=public[,internal]
# adds a group-level `audiences:` block so Fern prunes to matching operations plus
# the transitive type closure. Empty → no filter (the whole API is generated).
audiences_block=""
if [ -n "${FERN_AUDIENCES:-}" ]; then
  audiences_block=$'    audiences:\n'
  IFS=',' read -ra _auds <<<"$FERN_AUDIENCES"
  for _a in "${_auds[@]}"; do audiences_block+="      - ${_a}"$'\n'; done
fi
# Optional client class name override (issue #61): CLIENT_CLASS_NAME=<Name> sets
# Fern's `client_class_name`, renaming the generated root client class. Empty →
# Fern derives it from the API title (its default). Kept a single config line so
# it slots under the generator's `config:` block below.
client_class_name_block=""
if [ -n "${CLIENT_CLASS_NAME:-}" ]; then
  client_class_name_block="          client_class_name: ${CLIENT_CLASS_NAME}"$'\n'
fi
# Optional pydantic extra-fields behavior (issue #63): EXTRA_FIELDS=allow|ignore|forbid
# sets Fern's `pydantic_config.extra_fields`, which drives the emitted model_config /
# Config `extra`. Empty → Fern's default (`allow`). Kept a single config line so it
# slots under the generator's `pydantic_config:` block below.
extra_fields_block=""
if [ -n "${EXTRA_FIELDS:-}" ]; then
  extra_fields_block="            extra_fields: ${EXTRA_FIELDS}"$'\n'
fi
# crozier renders string enums as real `enum.Enum` classes by default (issue #41
# gap 2b), which is Fern's opt-in `python_enums` mode rather than its
# out-of-the-box open-`Literal`-union default. Every `expected/` golden therefore
# targets `python_enums`; keep this in lockstep with the generator so a
# regeneration does not silently flip the enum shape. A literals golden leaves
# `enum_type` unset, exactly as crozier's `enum-type: literals` documents.
enum_type_block=""
[ "$ENUM_TYPE" = literals ] || enum_type_block="            enum_type: python_enums"$'\n'
pydantic_config_block=""
if [ -n "$enum_type_block$extra_fields_block" ]; then
  pydantic_config_block="          pydantic_config:"$'\n'"$enum_type_block$extra_fields_block"
fi

# Optional Fern `default_max_retries` (crozier's `default-max-retries`): only an
# overlay golden sets it, so every other golden keeps Fern's default of 2.
default_max_retries_block=""
if [ -n "$DEFAULT_MAX_RETRIES" ]; then
  default_max_retries_block="          default_max_retries: ${DEFAULT_MAX_RETRIES}"$'\n'
fi

cat > "$workdir/fern/generators.yml" <<YAML
api:
  path: ${api_path}
groups:
  python-sdk:
${audiences_block}    generators:
      - name: fernapi/fern-python-sdk
        version: ${FERN_PYTHON_VERSION}
        config:
${client_class_name_block}${default_max_retries_block}${pydantic_config_block}        output:
          location: local-file-system
          path: ../generated/python
YAML

echo "generate-fern-fixture: running Fern (python-sdk@${FERN_PYTHON_VERSION}, $LAYOUT) locally..." >&2
# `--preview --output` writes the full *packaged* SDK (a pip package with
# `src/<pkg>/…` + `pyproject.toml` + `README.md`/`reference.md` + `.fern/`) under
# `<output>/fern-python-sdk/`. A plain `--local` with `location: local-file-system`
# instead emits only the flat module tree (no packaging), so the committed corpus
# — which is the packaged form — is reproduced with `--preview`. It needs no
# publishing credentials (unlike a `pypi`/`github` output location, whose local
# run tries to push and fails).
#
# `--preview` only emits the full package when Fern considers itself authenticated;
# with no FERN_TOKEN it silently falls back to the flat module tree. We never
# publish (local `--preview`), so any non-empty token unlocks the packaged form —
# a dummy is sufficient and carries no credential. The flat layout is exactly
# that token-less `--local` run, so it runs with no token at all, as measured.
if [ "$LAYOUT" = packaged ]; then
  export FERN_TOKEN="${FERN_TOKEN:-preview-only-no-publish}"
else
  unset FERN_TOKEN
fi

# Fern stamps how it was invoked into `.fern/metadata.json` (`invokedBy` +
# `ciProvider`), detected from the environment. Every committed golden is
# published by the **Fern goldens** workflow from GitHub Actions, so the whole
# corpus carries the `ci`/`github` form and crozier emits it. A local run is a
# reproduction aid for that workflow, not a separate flavor of golden, so give
# Fern the same invocation identity instead of stamping a `manual` record that
# only the local path could ever produce. Already set under the workflow (and
# under any real CI), where this is a no-op.
export CI="${CI:-true}"
export GITHUB_ACTIONS="${GITHUB_ACTIONS:-true}"

# Under a TLS-intercepting sandbox, Fern's generator container runs an internal
# `npm install @fern-api/generator-cli` that hangs forever: the container gets
# neither the host's proxy (the proxy listens on 127.0.0.1, unreachable from a
# default bridge network) nor the proxy CA, so its TLS handshakes never complete.
# When a proxy is configured we transparently reroute Fern's `docker run`/`create`
# through a shim that injects host networking, the proxy env, and the CA — so the
# container's npm behaves exactly like the host's. Off outside a sandbox (no proxy)
# or when CROZIER_FERN_NO_DOCKER_SHIM is set; override the CA with
# CROZIER_FERN_DOCKER_CA (defaults to $NODE_EXTRA_CA_CERTS).
setup_docker_shim() {
  [ -z "${CROZIER_FERN_NO_DOCKER_SHIM:-}" ] || return 0
  local proxy="${HTTPS_PROXY:-${https_proxy:-}}"
  [ -n "$proxy" ] || return 0  # no proxy → real docker already works, do nothing

  local real; real="$(command -v docker)" || return 0
  local ca="${CROZIER_FERN_DOCKER_CA:-${NODE_EXTRA_CA_CERTS:-}}"

  # Flags injected right after `run`/`create`: host networking (so 127.0.0.1 reaches
  # the host proxy), pass-through of the proxy env (docker forwards the current value
  # for a bare `-e NAME`), and the proxy CA mounted read-only + trusted by node.
  local inject="--network host -e HTTPS_PROXY -e https_proxy -e HTTP_PROXY"
  inject+=" -e http_proxy -e NO_PROXY -e no_proxy"
  if [ -n "$ca" ] && [ -f "$ca" ]; then
    inject+=" -v $(printf '%q' "$ca"):/ca.crt:ro -e NODE_EXTRA_CA_CERTS=/ca.crt"
  else
    echo "generate-fern-fixture: no proxy CA ($ca) — container TLS through the proxy" \
         "may fail; set CROZIER_FERN_DOCKER_CA to the bundle." >&2
  fi

  local bin="$workdir/shim-bin"
  mkdir -p "$bin"
  cat > "$bin/docker" <<SHIM
#!/usr/bin/env bash
# Auto-generated by generate-fern-fixture.sh — reroutes docker run/create with
# host networking + proxy CA so the Fern generator container can reach the network.
set -euo pipefail
out=(); injected=0
for a in "\$@"; do
  out+=("\$a")
  if [ "\$injected" -eq 0 ] && { [ "\$a" = run ] || [ "\$a" = create ]; }; then
    out+=($inject); injected=1
  fi
done
exec $(printf '%q' "$real") "\${out[@]}"
SHIM
  chmod +x "$bin/docker"
  export PATH="$bin:$PATH"
  echo "generate-fern-fixture: proxy detected — routing Fern's docker through a" \
       "host-network + CA shim (unset with CROZIER_FERN_NO_DOCKER_SHIM=1)." >&2
}
setup_docker_shim

if [ "$LAYOUT" = packaged ]; then
  mkdir -p "$workdir/preview"
  ( cd "$workdir/fern" && fern generate --group python-sdk --local --preview --output "$workdir/preview" --force )

  # The packaged tree lands under `<output>/fern-python-sdk/`; it is already the
  # `src/…` + `.fern/` layout the committed corpus uses, so no path remapping.
  src="$workdir/preview/fern-python-sdk"
  if [ ! -d "$src/src" ]; then
    echo "generate-fern-fixture: Fern produced no packaged SDK under $src" >&2
    exit 1
  fi
else
  # Without `--preview`, Fern writes to the `local-file-system` path the
  # generators.yml above names: the package's modules at its root, no `src/`.
  ( cd "$workdir/fern" && fern generate --group python-sdk --local --force )
  src="$workdir/generated/python"
  if [ ! -f "$src/__init__.py" ] || [ -e "$src/src" ]; then
    echo "generate-fern-fixture: Fern produced no flat module tree under $src" >&2
    exit 1
  fi
fi
prefix=""

# Strip comments from every generated .py, mirroring the offline corpus, into a
# same-filesystem staging directory. Only a complete tree is renamed into place;
# a failed strip/copy therefore cannot damage the prior valid golden.
mkdir -p "$(dirname "$dest")"
publish_stage="$(mktemp -d "$(dirname "$dest")/.fern-output.XXXXXX")"
staged_dest="$publish_stage/$golden_name"
mkdir -p "$staged_dest"
( cd "$src" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
  rel="${rel#./}"
  case "$rel" in
    .fern/*) target="$staged_dest/$rel" ;;
    *)       target="$staged_dest/$prefix$rel" ;;
  esac
  mkdir -p "$(dirname "$target")"
  case "$rel" in
    *.py) "$crozier_bin" internal-strip "$src/$rel" > "$target" ;;
    *)    cp "$src/$rel" "$target" ;;
  esac
done

# Provenance for the vendored-spec path: hand-authored fixtures are not
# CORPUS.md rows, so `fern-goldens` never records their generator version. It
# writes its own corpus-form record (name/ref/URL) whenever it drives this
# script, which is exactly when a spec override is supplied — so only the
# vendored path writes one here. Any non-default generator knob is part of the
# golden's identity and is recorded alongside the versions — the layout too, for
# a flat golden (a packaged record stays exactly the form it always had).
if [ "$ENUM_TYPE" = literals ]; then
  # The overlay's manifest is its provenance whichever route supplied the spec.
  provenance="{\"fern_python_sdk_version\": \"$FERN_PYTHON_VERSION\", \"fern_cli_version\": \"$FERN_CLI_VERSION\", \"enum_type\": \"literals\", \"base\": \"expected\"}"
  python3 "$repo_root/scripts/golden_overlay.py" reduce "$fixture_dir/expected" "$staged_dest" "$provenance"
elif [ -n "$DEFAULT_MAX_RETRIES" ]; then
  provenance="{\"fern_python_sdk_version\": \"$FERN_PYTHON_VERSION\", \"fern_cli_version\": \"$FERN_CLI_VERSION\", \"default_max_retries\": $DEFAULT_MAX_RETRIES, \"base\": \"expected\"}"
  python3 "$repo_root/scripts/golden_overlay.py" reduce "$fixture_dir/expected" "$staged_dest" "$provenance"
elif [ -z "$SPEC_OVERRIDE" ]; then
  settings=""
  flat_layout=""
  [ "$LAYOUT" = packaged ] || flat_layout="$LAYOUT"
  for pair in "audiences=${FERN_AUDIENCES:-}" \
    "audience_strict=${AUDIENCE_STRICT:-}" \
    "client_class_name=${CLIENT_CLASS_NAME:-}" \
    "extra_fields=${EXTRA_FIELDS:-}" \
    "organization=${ORGANIZATION:-}" \
    "layout=$flat_layout"; do
    value="${pair#*=}"
    [ -n "$value" ] || continue
    settings="$settings,
  \"${pair%%=*}\": \"$value\""
  done
  cat > "$staged_dest/.crozier-fern-golden.json" <<JSON
{
  "fern_python_sdk_version": "$FERN_PYTHON_VERSION",
  "fern_cli_version": "$FERN_CLI_VERSION",
  "vendored_spec_path": "${spec#"$repo_root"/}"$settings
}
JSON
fi

backup="$(dirname "$dest")/.$golden_name.backup.$$"
[ ! -e "$backup" ] || {
  echo "generate-fern-fixture: stale backup blocks atomic install: $backup" >&2
  exit 1
}
had_dest=0
if [ -e "$dest" ]; then
  [ ! -L "$dest" ] || {
    echo "generate-fern-fixture: refusing to replace symlinked destination $dest" >&2
    exit 1
  }
  mv "$dest" "$backup"
  had_dest=1
fi
if ! mv "$staged_dest" "$dest"; then
  [ "$had_dest" -eq 0 ] || mv "$backup" "$dest"
  echo "generate-fern-fixture: could not atomically install the staged golden" >&2
  exit 1
fi
[ "$had_dest" -eq 0 ] || rm -rf "$backup"

echo "generate-fern-fixture: wrote $(find "$dest" -type f | wc -l | tr -d ' ') files to $dest" >&2
echo "generate-fern-fixture: review, then wire files into the e2e manifest (see docs/matching.md)." >&2
