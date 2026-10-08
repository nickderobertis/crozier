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
# Fern repo). The exhaustive spec is NOT committed as OpenAPI-derived output, so
# passing `exhaustive` ALSO runs Fern's container generator for it via
# tools/fern-goldens/generate-fern-fixture.sh (needs Docker + the fern CLI).
#
# Usage:  tools/fern-goldens/fixtures-refresh.sh [exhaustive]
set -euo pipefail

# Pin the Fern commit the fixtures were generated from — reproducibility and a
# clear provenance record. Bump deliberately, then re-run and review the diff.
FERN_REPO="https://github.com/fern-api/fern.git"
FERN_COMMIT="4d07e6aeeed1d88917ce59dfc9b4cf9e6008e553"

# APIs whose Fern Python output is genuinely OpenAPI-derived (flat structure that
# crozier can reproduce from openapi.yml alone). Each entry:
#   <api-name>:<source-spec-path>:<seed-output-path>
CORPUS=(
  "query-parameters-openapi:test-definitions/fern/apis/query-parameters-openapi/openapi.yml:seed/python-sdk/query-parameters-openapi/no-custom-config"
)

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
crozier_bin="$repo_root/target/release/crozier"
[ -x "$crozier_bin" ] || { echo "fixtures-refresh: build crozier first (cargo build --release)" >&2; exit 1; }

workdir="$(mktemp -d)" || {
  echo "fixtures-refresh: could not create a scratch directory — point TMPDIR at a writable" \
       "directory with free space, then re-run" >&2
  exit 1
}
# Quiet on success (one summary line); the step that failed is named on exit.
step=""
on_exit() {
  local status=$?
  # A cleanup that fails names what is left; it never replaces the run's own status.
  rm -rf "$workdir" 2>/dev/null ||
    echo "fixtures-refresh: could not remove the scratch directory $workdir — delete it (rm -rf $workdir)" >&2
  [ "$status" -eq 0 ] || [ -z "$step" ] ||
    echo "fixtures-refresh: stopped while $step (exit $status) — fix the error above, then" \
         "re-run; restore any partly refreshed fixture with git checkout -- tests/fixtures/" >&2
}
trap on_exit EXIT

# A failed sparse-checkout setup is fatal: the checkout below would otherwise
# write nothing (or the whole Fern tree) instead of the corpus paths.
sparse_checkout() {
  local output
  output="$(git -C "$workdir" sparse-checkout "$@" 2>&1)" || {
    echo "fixtures-refresh: git sparse-checkout $1 failed: ${output:-no output} — it needs" \
         "git 2.26 or newer (git --version); upgrade git, then re-run" >&2
    step=""
    exit 1
  }
}

step="fetching Fern @ ${FERN_COMMIT:0:9} from $FERN_REPO"
git -C "$workdir" init -q
git -C "$workdir" remote add origin "$FERN_REPO"
git -C "$workdir" config core.sparseCheckout true
sparse_checkout init --cone
for entry in "${CORPUS[@]}"; do
  IFS=':' read -r _ spec seed <<<"$entry"
  sparse_checkout add "$(dirname "$spec")" "$seed"
done
git -C "$workdir" fetch -q --depth 1 origin "$FERN_COMMIT"
git -C "$workdir" checkout -q FETCH_HEAD

refreshed=0
for entry in "${CORPUS[@]}"; do
  IFS=':' read -r name spec seed <<<"$entry"
  step="refreshing tests/fixtures/$name"
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
  refreshed=$((refreshed + 1))
done

# The exhaustive fixture is not committed by Fern as OpenAPI-derived output, so
# it is regenerated on demand behind an explicit arg (it needs Docker + fern,
# which the offline corpus does not).
also=""
for arg in "$@"; do
  if [ "$arg" = "exhaustive" ]; then
    step="regenerating tests/fixtures/exhaustive with Fern's container generator"
    # Its output is shown only when it fails; this script's line is the summary.
    "$repo_root/tools/fern-goldens/generate-fern-fixture.sh" >"$workdir/exhaustive.log" 2>&1 || {
      status=$?
      cat "$workdir/exhaustive.log" >&2 || echo "fixtures-refresh: could not read the generator's log" >&2
      exit "$status"
    }
    also=" and exhaustive"
  fi
done
step=""

echo "fixtures-refresh: refreshed $refreshed fixture(s) from Fern @ ${FERN_COMMIT:0:9}$also —" \
     "review the diff; update the e2e manifest for any new matched files." >&2
