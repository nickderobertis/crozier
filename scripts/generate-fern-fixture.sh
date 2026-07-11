#!/usr/bin/env bash
# Generate Fern's Python SDK output for a fixture's OpenAPI spec, strip comments,
# and install it as that fixture's golden `expected/` tree.
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
# Usage:  scripts/generate-fern-fixture.sh [FIXTURE] [FERN_PYTHON_VERSION]
#   FIXTURE             fixture dir under tests/fixtures/ (default: exhaustive).
#                       e.g. auth-schemes, inline-request-response, integer-enums.
#   FERN_PYTHON_VERSION defaults to the pin below (matches the vendored specs).
set -euo pipefail

. "$(cd "$(dirname "$0")" && pwd)/lib.sh"

FIXTURE="${1:-exhaustive}"
# FIXTURE is spliced into paths that are later `rm -rf`'d, so hold it to a single
# safe path segment (shared valid_fixture_name; rejects traversal/option injection).
valid_fixture_name "$FIXTURE" || {
  echo "generate-fern-fixture: invalid fixture name '$FIXTURE' — must be a single" \
       "path segment matching [A-Za-z0-9][A-Za-z0-9._-]* (a dir under tests/fixtures/)" >&2
  exit 1
}
# The fern-python-sdk generator version whose output we target. Bump together
# with the vendored spec + fixtures so the corpus stays internally consistent.
FERN_PYTHON_VERSION="${2:-4.34.0}"
# The Fern CLI version, pinned via fern.config.json's `version` (the `fern` npm
# package is only a launcher; this field selects the actual CLI it runs). Matches
# the corpus's `.fern/metadata.json` cliVersion so regenerated output stays
# consistent; a `*` here would float to the latest CLI and can drift the output.
FERN_CLI_VERSION="${FERN_CLI_VERSION:-5.67.1}"

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
spec="$repo_root/tests/fixtures/$FIXTURE/openapi.yml"
dest="$repo_root/tests/fixtures/$FIXTURE/expected"

need() { command -v "$1" >/dev/null 2>&1 || { echo "generate-fern-fixture: '$1' not found — $2" >&2; exit 1; }; }
need fern "install it: npm i -g fern-api"
need docker "start Docker; Fern runs its generator as a local container"
[ -f "$spec" ] || { echo "generate-fern-fixture: missing spec $spec" >&2; exit 1; }

crozier_bin="$repo_root/target/release/crozier"
[ -x "$crozier_bin" ] || { echo "generate-fern-fixture: build crozier first (cargo build --release)" >&2; exit 1; }

workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

# Scaffold a minimal Fern workspace around the vendored OpenAPI spec. We ignore
# Fern's definition files by construction: only the OpenAPI document is wired in.
mkdir -p "$workdir/fern/openapi" "$workdir/generated"
cp "$spec" "$workdir/fern/openapi/openapi.yml"
cat > "$workdir/fern/fern.config.json" <<JSON
{ "organization": "fern", "version": "${FERN_CLI_VERSION}" }
JSON
cat > "$workdir/fern/generators.yml" <<YAML
api:
  path: openapi/openapi.yml
groups:
  python-sdk:
    generators:
      - name: fernapi/fern-python-sdk
        version: ${FERN_PYTHON_VERSION}
        output:
          location: local-file-system
          path: ../generated/python
YAML

echo "generate-fern-fixture: running Fern (python-sdk@${FERN_PYTHON_VERSION}) locally..." >&2
( cd "$workdir/fern" && fern generate --group python-sdk --local --force )

out="$workdir/generated/python"
# Fern emits one of two layouts depending on the CLI version: a full pip package
# (`python/src/<pkg>/...` alongside pyproject.toml — install verbatim) or a flat
# module tree (`python/<pkg-contents>` with no `src/` — relocate under
# `src/fern/`, the layout crozier and the committed corpus use). Detect which.
if [ -d "$out/src" ]; then
  src="$out"; prefix=""
elif [ -f "$out/__init__.py" ]; then
  src="$out"; prefix="src/fern/"
else
  echo "generate-fern-fixture: Fern produced no recognizable package under $out" >&2
  exit 1
fi

# Strip comments from every generated .py, mirroring the offline corpus, and
# install into the fixture tree (under $prefix). Non-.py files are copied verbatim.
# In the flat layout the package root and the output root are conflated, so the
# `.fern/` metadata dir stays at the fixture root rather than moving under src/.
rm -rf "$dest"
mkdir -p "$dest"
( cd "$src" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
  rel="${rel#./}"
  case "$rel" in
    .fern/*) target="$dest/$rel" ;;
    *)       target="$dest/$prefix$rel" ;;
  esac
  mkdir -p "$(dirname "$target")"
  case "$rel" in
    *.py) "$crozier_bin" internal-strip "$src/$rel" > "$target" ;;
    *)    cp "$src/$rel" "$target" ;;
  esac
done

echo "generate-fern-fixture: wrote $(find "$dest" -type f | wc -l | tr -d ' ') files to $dest" >&2
echo "generate-fern-fixture: review, then wire files into the e2e manifest (see docs/matching.md)." >&2
