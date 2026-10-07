#!/usr/bin/env bash
# The arm search's YAML fallback against the census's stdlib loader, under the
# pinned full YAML 1.2 parser (ruamel.yaml) each script declares in its own
# inline metadata, installed through uv:
#   samples  identical counts on every registered YAML source, and each refused
#            form's committed sample (tools/surface-census/tests/data/
#            census-fallback-sample/) read as what it declares;
#   parsers  the arm search and the witness-search re-census CLI over temporary
#            ledgers, a loopback GitHub and Sourcegraph, and the same parser.
# Fetches no specification. The `census-fallback` project's targets run it; CI
# runs both in its live-e2e leg, and corpus-match's offline proof runs the
# samples with sockets denied.
set -euo pipefail
cd "$(dirname "$0")/../.."

# The parser pin, read from a script's PEP 723 `dependencies` line: exactly one
# non-empty pin, or the run stops naming the script, since an empty `--with`
# would run the fallback against whatever parser uv happens to hold.
pinned() {
  local pin
  pin="$(sed -n 's/^# dependencies = \["\(.*\)"\]$/\1/p' "$1")"
  if [ -z "$pin" ] || [ "$(printf '%s\n' "$pin" | wc -l)" -ne 1 ]; then
    echo "census-fallback: $1 declares no single pinned dependency in its PEP 723 header —" \
         "restore its '# dependencies = [\"<package>==<version>\"]' line (git checkout -- $1), then re-run" >&2
    return 1
  fi
  printf '%s\n' "$pin"
}

case "${1:-}" in
  samples)
    search_pin="$(pinned tools/surface-census/golden-reach-search.py)"
    python3 tools/corpus/corpus_sources.py check
    CROZIER_REQUIRE_CORPUS=1 uv run --no-project --with "$search_pin" \
      python3 tests/census_fallback/golden_reach_census_fallback_test.py
    ;;
  parsers)
    search_pin="$(pinned tools/surface-census/golden-reach-search.py)"
    recensus_pin="$(pinned tools/witness-search/witness-search-recensus.py)"
    CROZIER_REQUIRE_CORPUS=1 uv run --no-project --with "$search_pin" \
      python3 tools/surface-census/tests/golden_reach_test.py
    uv run --no-project --with "$recensus_pin" \
      python3 tools/witness-search/tests/witness_search_recensus_test.py
    ;;
  *)
    echo "usage: tests/census_fallback/run.sh samples|parsers" >&2
    exit 2
    ;;
esac
