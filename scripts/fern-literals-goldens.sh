#!/usr/bin/env bash
# Generate each named fixture's `expected-literals/` golden: Fern's output with
# `pydantic_config.enum_type` unset (fern-python-sdk's `literals` default), the
# reference for crozier's `enum-type: literals`. Every fixture must already have
# its python-enums `expected/` golden, because the literals golden is committed as
# an overlay of it (scripts/literals_overlay.py). The spec, the Fern pins and the
# fixture's other generator settings are the ones its `expected/` golden used:
#   - the spec is the fixture's vendored openapi.yml, else its committed corpus
#     source, else (a row with pinned remote refs or a pinned tree) what
#     `just fetch-corpus` stages for Fern, as the Fern goldens workflow does;
#   - the version is the one the fixture's provenance records (else the corpus
#     pin every managed golden agrees on);
#   - audiences, client class name, extra fields come from
#     tests/fixtures/fern-generator-config.txt inside generate-fern-fixture.sh.
#
# Needs what generate-fern-fixture.sh needs (Docker, fern, a release crozier).
# Usage: scripts/fern-literals-goldens.sh [--jobs N] FIXTURE...
# Quiet per fixture on success; logs under .local/fern-literals/<fixture>.log.
set -euo pipefail

. "$(cd "$(dirname "$0")" && pwd)/lib.sh"
repo_root="$(cd "$(dirname "$0")/.." && pwd)"

jobs=1
if [ "${1:-}" = "--jobs" ]; then
  [[ "${2:-}" =~ ^[1-9][0-9]*$ ]] || {
    echo "fern-literals-goldens: --jobs needs a positive integer" >&2
    exit 1
  }
  jobs="$2"
  shift 2
fi
[ "$#" -gt 0 ] || {
  echo "usage: scripts/fern-literals-goldens.sh [--jobs N] FIXTURE..." >&2
  exit 1
}

pin_of() {
  python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["fern_python_sdk_version"])' "$1"
}
corpus_pin="$(pin_of "$repo_root/tests/fixtures/eos.local/expected/.crozier-fern-golden.json")"
logs="$repo_root/.local/fern-literals"
mkdir -p "$logs"

one() {
  local fixture="$1" dir spec="" version staging log
  valid_fixture_name "$fixture" || { echo "$fixture: invalid fixture name" >&2; return 1; }
  dir="$repo_root/tests/fixtures/$fixture"
  log="$logs/$fixture.log"
  : >"$log"
  [ -d "$dir/expected" ] || { echo "$fixture: no expected/ golden to overlay" >&2; return 1; }
  version="$corpus_pin"
  [ ! -f "$dir/expected/.crozier-fern-golden.json" ] || version="$(pin_of "$dir/expected/.crozier-fern-golden.json")"
  if [ ! -f "$dir/openapi.yml" ]; then
    if cut -f1 "$repo_root/tests/fixtures/corpus-remote-ref-pins.tsv" | grep -qx -- "$fixture" \
      || cut -f2 "$repo_root/tests/fixtures/corpus-remote-ref-pins.tsv" | grep -qx -- "$fixture"; then
      spec="$(just --justfile "$repo_root/justfile" fetch-corpus --fixture "$fixture" 2>>"$log" | tail -1)"
    else
      for name in openapi.json openapi.yaml openapi.yml; do
        [ ! -f "$repo_root/tests/fixtures/corpus-sources/$fixture/$name" ] \
          || spec="$repo_root/tests/fixtures/corpus-sources/$fixture/$name"
      done
    fi
    [ -n "$spec" ] || { echo "$fixture: no committed source; run just lint-corpus-sources" >&2; return 1; }
  fi
  # A stage below the fixture keeps the destination guard of
  # generate-fern-fixture.sh satisfied; only a complete overlay is moved in.
  staging="$(mktemp -d "$dir/.fern-literals-stage.XXXXXX")"
  if "$repo_root/scripts/generate-fern-fixture.sh" --enum-type literals "$fixture" "$version" \
    "$spec" "$staging/expected-literals" >>"$log" 2>&1; then
    rm -rf "$dir/expected-literals"
    mv "$staging/expected-literals" "$dir/expected-literals"
    rm -rf "$staging"
    echo "generated $fixture/expected-literals at fernapi/fern-python-sdk:$version"
  else
    rm -rf "$staging"
    echo "$fixture: Fern generation failed; see $log" >&2
    return 1
  fi
}
export -f one pin_of valid_fixture_name
export repo_root corpus_pin logs

printf '%s\n' "$@" | xargs -P "$jobs" -I{} bash -c 'one "$1"' _ {}
