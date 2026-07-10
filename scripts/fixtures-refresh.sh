#!/usr/bin/env bash
# Re-vendor the OFFLINE Fern reference corpus into tests/fixtures/.
#
# For each API in the corpus, this fetches (at a pinned Fern commit) the source
# OpenAPI document and Fern's committed Python SDK output, strips comments from
# the .py files with crozier's own stripper, and writes:
#     tests/fixtures/<api>/openapi.yml      (source spec, vendored verbatim)
#     tests/fixtures/<api>/expected/**      (Fern output, comment-stripped)
#
# These fixtures are Fern's output (Apache-2.0). Attribution lives in NOTICE and
# licenses/fern-APACHE-2.0.txt — this script preserves them; do not remove them.
#
# The offline corpus needs NO Docker (Fern's output is already committed in the
# Fern repo). For the exhaustive spec, which is NOT committed as OpenAPI-derived
# output, use scripts/generate-fern-fixture.sh (needs Docker) instead.
#
# Usage:  scripts/fixtures-refresh.sh
set -euo pipefail

# Pin the Fern commit the fixtures were generated from — reproducibility and a
# clear provenance record. Bump deliberately, then re-run and review the diff.
FERN_REPO="https://github.com/fern-api/fern.git"
FERN_COMMIT="3a471b03d4778f291849adc03bacfcd40340fc26"

# APIs whose Fern Python output is genuinely OpenAPI-derived (flat structure that
# crozier can reproduce from openapi.yml alone). Each entry:
#   <api-name>:<source-spec-path>:<seed-output-path>
CORPUS=(
  "query-parameters-openapi:test-definitions/fern/apis/query-parameters-openapi/openapi.yml:seed/python-sdk/query-parameters-openapi/no-custom-config"
)

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
crozier_bin="$repo_root/target/release/crozier"
[ -x "$crozier_bin" ] || { echo "fixtures-refresh: build crozier first (cargo build --release)" >&2; exit 1; }

workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

echo "fixtures-refresh: fetching Fern @ ${FERN_COMMIT:0:9}..." >&2
git -C "$workdir" init -q
git -C "$workdir" remote add origin "$FERN_REPO"
git -C "$workdir" config core.sparseCheckout true
git -C "$workdir" sparse-checkout init --cone >/dev/null 2>&1 || true
for entry in "${CORPUS[@]}"; do
  IFS=':' read -r _ spec seed <<<"$entry"
  git -C "$workdir" sparse-checkout add "$(dirname "$spec")" "$seed" >/dev/null 2>&1 || true
done
git -C "$workdir" fetch -q --depth 1 origin "$FERN_COMMIT"
git -C "$workdir" checkout -q FETCH_HEAD

for entry in "${CORPUS[@]}"; do
  IFS=':' read -r name spec seed <<<"$entry"
  echo "fixtures-refresh: $name" >&2
  api_dir="$repo_root/tests/fixtures/$name"
  rm -rf "$api_dir/expected"
  mkdir -p "$api_dir/expected"
  cp "$workdir/$spec" "$api_dir/openapi.yml"

  ( cd "$workdir/$seed" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    mkdir -p "$api_dir/expected/$(dirname "$rel")"
    case "$rel" in
      *.py) "$crozier_bin" internal-strip "$workdir/$seed/$rel" > "$api_dir/expected/$rel" ;;
      *)    cp "$workdir/$seed/$rel" "$api_dir/expected/$rel" ;;
    esac
  done
done

echo "fixtures-refresh: done. Review the diff; update the e2e manifest for any new matched files." >&2
