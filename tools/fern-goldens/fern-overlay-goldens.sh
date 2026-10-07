#!/usr/bin/env bash
# Generate each named fixture's overlay golden under one non-default Fern setting
# (tools/fern-goldens/golden_overlay.py):
#   --enum-type literals     `expected-literals/`, Fern with
#                            `pydantic_config.enum_type` unset (fern-python-sdk's
#                            `literals` default), for crozier's `enum-type: literals`;
#   --default-max-retries N  `expected-default-max-retries/`, Fern with
#                            `default_max_retries: N`, for crozier's
#                            `default-max-retries`.
# Every fixture must already have its python-enums `expected/` golden, because
# the overlay is reduced against it. The spec, the Fern pins and the fixture's
# other generator settings are the ones its `expected/` golden used:
#   - the spec is the fixture's vendored openapi.yml, else its committed corpus
#     source, else (a row with pinned remote refs or a pinned tree) what
#     `just fetch-corpus` stages for Fern, as the Fern goldens workflow does;
#   - the version is the one the fixture's provenance records (else the corpus
#     pin every managed golden agrees on);
#   - audiences, client class name, extra fields come from
#     tests/fixtures/fern-generator-config.txt inside generate-fern-fixture.sh.
#
# Needs what generate-fern-fixture.sh needs (Docker, fern, a release crozier).
# Usage: tools/fern-goldens/fern-overlay-goldens.sh [--jobs N] (--enum-type literals | --default-max-retries N) FIXTURE...
# One summary line on success; logs under .local/fern-overlay/<fixture>.log.
set -euo pipefail

. "$(cd "$(dirname "$0")/../../scripts" && pwd)/lib.sh"
repo_root="$(cd "$(dirname "$0")/../.." && pwd)"

usage="usage: tools/fern-goldens/fern-overlay-goldens.sh [--jobs N] (--enum-type literals | --default-max-retries N) FIXTURE..."
jobs=1
setting=()
golden=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --jobs)
      [[ "${2:-}" =~ ^[1-9][0-9]*$ ]] || {
        echo "fern-overlay-goldens: --jobs needs a positive integer" >&2
        exit 1
      }
      jobs="$2"
      ;;
    --enum-type)
      [ "${2:-}" = literals ] || {
        echo "fern-overlay-goldens: --enum-type overlay is literals only" >&2
        exit 1
      }
      setting=(--enum-type literals)
      golden=expected-literals
      ;;
    --default-max-retries)
      [[ "${2:-}" =~ ^(0|[1-9][0-9]*)$ ]] || {
        echo "fern-overlay-goldens: --default-max-retries needs a non-negative integer" >&2
        exit 1
      }
      setting=(--default-max-retries "$2")
      golden=expected-default-max-retries
      ;;
    *) break ;;
  esac
  shift 2
done
[ -n "$golden" ] && [ "$#" -gt 0 ] || {
  echo "$usage" >&2
  exit 1
}

report_failures fern-overlay-goldens "check that tests/fixtures/ and .local/fern-overlay/ are \
writable on a disk with free space and that the expected/ provenance it read is intact, then re-run \
this script for the fixtures that failed"

pin_of() {
  python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["fern_python_sdk_version"])' "$1"
}
corpus_pin="$(pin_of "$repo_root/tests/fixtures/eos.local/expected/.crozier-fern-golden.json")"
logs="$repo_root/.local/fern-overlay"
mkdir -p "$logs"
# Each worker records the version it generated at here, so the run reports one
# summary line rather than one line per parallel worker.
results="$(mktemp -d)"
trap 'rm -rf "$results"' EXIT

# one FIXTURE SETTING... — generate FIXTURE's overlay golden under SETTING.
one() {
  local fixture="$1" dir spec="" version staging log
  shift
  valid_fixture_name "$fixture" || {
    echo "$fixture: invalid fixture name — pass the name of one directory under" \
         "tests/fixtures/, matching [A-Za-z0-9][A-Za-z0-9._-]* with no '..'" >&2
    return 1
  }
  dir="$repo_root/tests/fixtures/$fixture"
  log="$logs/$fixture.log"
  : >"$log"
  [ -d "$dir/expected" ] || {
    echo "$fixture: no expected/ golden to overlay — restore it" \
         "(git checkout -- tests/fixtures/$fixture/expected) or generate it first" \
         "(tools/fern-goldens/generate-fern-fixture.sh $fixture; a CORPUS.md row via the" \
         "Fern goldens workflow), then re-run" >&2
    return 1
  }
  version="$corpus_pin"
  [ ! -f "$dir/expected/.crozier-fern-golden.json" ] \
    || version="$(pin_of "$dir/expected/.crozier-fern-golden.json")" \
    || {
      echo "$fixture: unreadable expected/.crozier-fern-golden.json — restore it" \
           "(git checkout -- tests/fixtures/$fixture/expected/.crozier-fern-golden.json) or" \
           "regenerate expected/ with its record (tools/fern-goldens/generate-fern-fixture.sh" \
           "$fixture; a CORPUS.md row via the Fern goldens workflow), then re-run" >&2
      return 1
    }
  if [ ! -f "$dir/openapi.yml" ]; then
    if cut -f1 "$repo_root/tests/fixtures/corpus-remote-ref-pins.tsv" | grep -qx -- "$fixture" \
      || cut -f2 "$repo_root/tests/fixtures/corpus-remote-ref-pins.tsv" | grep -qx -- "$fixture"; then
      spec="$(just --justfile "$repo_root/justfile" fetch-corpus --fixture "$fixture" 2>>"$log" | tail -1)" \
        || {
          echo "$fixture: just fetch-corpus failed: $(tail -n 1 "$log" 2>/dev/null || echo 'no output')" >&2
          echo "$fixture: fix what it reports (the whole run is in $log), then re-run" \
               "tools/fern-goldens/fern-overlay-goldens.sh $* $fixture" >&2
          return 1
        }
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
  staging="$(mktemp -d "$dir/.fern-overlay-stage.XXXXXX")"
  if "$repo_root/tools/fern-goldens/generate-fern-fixture.sh" "$@" "$fixture" "$version" \
    "$spec" "$staging/$golden" >>"$log" 2>&1; then
    rm -rf "${dir:?}/$golden"
    mv "$staging/$golden" "$dir/$golden" || {
      echo "$fixture: could not install $golden; the overlay is left in $staging — make" \
           "tests/fixtures/$fixture writable, then move it into place" \
           "(mv $staging/$golden $dir/$golden) or discard it (rm -rf $staging) and re-run" \
           "this script for $fixture" >&2
      return 1
    }
    rm -rf "$staging"
    printf '%s\n' "$version" >"$results/$fixture"
  else
    rm -rf "$staging"
    echo "$fixture: Fern generation failed: $(tail -n 1 "$log" 2>/dev/null || echo 'no output')" >&2
    echo "$fixture: the whole run is in $log — fix the cause it records" \
         "(generate-fern-fixture.sh names its own next action there), then re-run" \
         "tools/fern-goldens/fern-overlay-goldens.sh $* $fixture" >&2
    return 1
  fi
}
export -f one pin_of valid_fixture_name arm_failure_report _report_failure
export repo_root corpus_pin logs golden results _failure_tool _failure_action

# The worker shell xargs starts does not inherit this script's `set -euo
# pipefail`, so it sets its own: a failed step fails that fixture's worker. The
# setting reaches it as separate arguments, never re-split from a string.
status=0
printf '%s\n' "$@" | xargs -P "$jobs" -I{} bash -c 'set -euo pipefail; arm_failure_report; one "$@"' _ {} "${setting[@]}" ||
  status=$?

# One line naming every installed overlay, in argument order, with its Fern pin
# (stated once when every fixture shares it). A failed fixture is absent here and
# has already named its own fix on stderr.
names="" pinned="" versions=""
for fixture in "$@"; do
  [ -f "$results/$fixture" ] || continue
  version="$(cat "$results/$fixture")"
  names+="${names:+, }$fixture/$golden"
  pinned+="${pinned:+, }$fixture/$golden at fernapi/fern-python-sdk:$version"
  versions+="$version"$'\n'
done
if [ -n "$names" ]; then
  if [ "$(printf '%s' "$versions" | sort -u | wc -l)" -eq 1 ]; then
    echo "generated $names at fernapi/fern-python-sdk:${versions%%$'\n'*}"
  else
    echo "generated $pinned"
  fi
fi
exit "$status"
