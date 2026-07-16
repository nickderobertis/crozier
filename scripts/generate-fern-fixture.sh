#!/usr/bin/env bash
# Generate Fern's Python SDK output for a fixture's OpenAPI spec, strip comments,
# and install it as that fixture's golden `expected/` tree.
#
# Produces the *packaged* SDK (a pip package: `src/<pkg>/…` + pyproject.toml +
# README.md/reference.md + .fern/) via `fern generate --preview`, which is the form
# the committed corpus vendors and needs no publishing credentials. String enums
# render as real `enum.Enum` classes (`pydantic_config.enum_type: python_enums`) to
# match crozier — see docs/matching.md.
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
# Usage:  scripts/generate-fern-fixture.sh [FIXTURE] [FERN_PYTHON_VERSION] [SPEC_PATH] [DEST_PATH]
#   FIXTURE             fixture dir under tests/fixtures/ (default: exhaustive).
#                       e.g. auth-schemes, inline-request-response, integer-enums.
#   FERN_PYTHON_VERSION defaults to the latest stable tag resolved by the same
#                       Docker Hub distribution lookup as `fern-goldens`.
#   SPEC_PATH           optional OpenAPI file to generate from instead of
#                       tests/fixtures/<fixture>/openapi.yml; useful for fetched,
#                       unvendored source specs.
#   DEST_PATH           optional automation-only destination. It must be an
#                       `expected` directory below this fixture; the default is
#                       tests/fixtures/<fixture>/expected.
set -euo pipefail

. "$(cd "$(dirname "$0")" && pwd)/lib.sh"

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

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
  echo "generate-fern-fixture: invalid Fern version '$FERN_PYTHON_VERSION' — use an exact semantic version such as 4.35.0" >&2
  exit 1
}
SPEC_OVERRIDE="${3:-}"
# The Fern CLI version, pinned via fern.config.json's `version` (the `fern` npm
# package is only a launcher; this field selects the actual CLI it runs). Matches
# the corpus's `.fern/metadata.json` cliVersion so regenerated output stays
# consistent; a `*` here would float to the latest CLI and can drift the output.
FERN_CLI_VERSION="${FERN_CLI_VERSION:-5.67.1}"

spec="${SPEC_OVERRIDE:-$repo_root/tests/fixtures/$FIXTURE/openapi.yml}"
fixture_dir="$repo_root/tests/fixtures/$FIXTURE"
dest="${4:-$fixture_dir/expected}"
[ "$(basename "$dest")" = expected ] || {
  echo "generate-fern-fixture: invalid destination '$dest' — its final path segment must be expected" >&2
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
  "$fixture_dir" | "$fixture_dir"/*) dest="$dest_parent/expected" ;;
  *)
    echo "generate-fern-fixture: invalid destination '$dest' — it must stay below $fixture_dir" >&2
    exit 1
    ;;
esac

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
cp "$spec" "$workdir/fern/openapi/openapi.yml"
cat > "$workdir/fern/fern.config.json" <<JSON
{ "organization": "fern", "version": "${FERN_CLI_VERSION}" }
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
cat > "$workdir/fern/generators.yml" <<YAML
api:
  path: openapi/openapi.yml
groups:
  python-sdk:
${audiences_block}    generators:
      - name: fernapi/fern-python-sdk
        version: ${FERN_PYTHON_VERSION}
        config:
${client_class_name_block}          # crozier renders string enums as real \`enum.Enum\` classes (issue #41
          # gap 2b), which is Fern's opt-in \`python_enums\` mode rather than its
          # out-of-the-box open-\`Literal\`-union default. The whole golden corpus
          # therefore targets \`python_enums\`; keep this in lockstep with the
          # generator so a regeneration does not silently flip the enum shape.
          pydantic_config:
            enum_type: python_enums
${extra_fields_block}
        output:
          location: local-file-system
          path: ../generated/python
YAML

echo "generate-fern-fixture: running Fern (python-sdk@${FERN_PYTHON_VERSION}) locally..." >&2
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
# a dummy is sufficient and carries no credential.
export FERN_TOKEN="${FERN_TOKEN:-preview-only-no-publish}"

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

mkdir -p "$workdir/preview"
( cd "$workdir/fern" && fern generate --group python-sdk --local --preview --output "$workdir/preview" --force )

# The packaged tree lands under `<output>/fern-python-sdk/`; it is already the
# `src/…` + `.fern/` layout the committed corpus uses, so no path remapping.
src="$workdir/preview/fern-python-sdk"
prefix=""
if [ ! -d "$src/src" ]; then
  echo "generate-fern-fixture: Fern produced no packaged SDK under $src" >&2
  exit 1
fi

# Strip comments from every generated .py, mirroring the offline corpus, into a
# same-filesystem staging directory. Only a complete tree is renamed into place;
# a failed strip/copy therefore cannot damage the prior valid golden.
mkdir -p "$(dirname "$dest")"
publish_stage="$(mktemp -d "$(dirname "$dest")/.fern-output.XXXXXX")"
staged_dest="$publish_stage/expected"
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

backup="$(dirname "$dest")/.expected.backup.$$"
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
