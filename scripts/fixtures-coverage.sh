#!/usr/bin/env bash
# Measure what the committed Fern goldens reach in src/, separately from what
# crozier's own tests reach: the golden-only, all-e2e and non-e2e tiers, against
# one instrumented build. What the tiers mean and how to read the split when
# choosing the next fixture is tests/fixtures/AGENTS.md ("Where the goldens are
# BLIND"); what makes the numbers honest is the docstring of
# scripts/fixtures-coverage-report.py. Neither is restated here.
#
# The one thing only this script knows: the golden tier runs first and is
# exported BEFORE the journey tier runs without an intervening clean, so the
# second export is the accumulated union — the all-e2e tier — and the corpus is
# generated once rather than twice.
#
# NOT part of `just check`: needs network, and runs the corpus instrumented.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"

fetch=1
scope=""
out_dir="$repo_root/.local/fixtures-coverage"

usage() {
  cat >&2 <<'USAGE'
Usage: scripts/fixtures-coverage.sh [--no-fetch] [--out DIR] [SCOPE]

  SCOPE      cargo-nextest filter expression ANDed into every tier, to measure
             one corpus quickly, e.g. 'test(/frankfurter/) or test(/wrap/)'.
             Every tier must still select at least one test.
  --no-fetch Reuse the already-fetched .local/corpus instead of re-fetching.
  --out DIR  Where to write the per-tier llvm-cov JSON exports.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-fetch) fetch=0 ;;
    --out)
      shift
      [ "$#" -gt 0 ] || { echo "fixtures-coverage: --out needs a directory" >&2; exit 1; }
      out_dir="$1"
      ;;
    -h | --help) usage; exit 0 ;;
    --*) echo "fixtures-coverage: unknown argument '$1'" >&2; usage; exit 1 ;;
    *)
      [ -z "$scope" ] || {
        echo "fixtures-coverage: more than one SCOPE expression was provided" >&2
        exit 1
      }
      scope="$1"
      ;;
  esac
  shift
done

need() { # need MESSAGE COMMAND...
  local message="$1"
  shift
  if ! "$@" >/dev/null 2>&1; then
    echo "fixtures-coverage: $message" >&2
    exit 1
  fi
}

need "cargo-llvm-cov is not installed — run 'just bootstrap'" \
  cargo llvm-cov --version
need "cargo-nextest is not installed — run 'just bootstrap'" \
  cargo nextest --version
need "python3 is not on PATH — it renders the report (scripts/fixtures-coverage-report.py)" \
  command -v python3
need "ruff is not on PATH — 'crozier generate' shells out to it, so every tier would \
fail to generate. Run 'just bootstrap'" \
  command -v ruff

mkdir -p "$out_dir"
log="$out_dir/run.log"
: >"$log"

step() { # step DESCRIPTION NEXT-ACTION COMMAND...
  local description="$1" next_action="$2"
  shift 2
  if ! "$@" >>"$log" 2>&1; then
    echo "fixtures-coverage: $description failed. $next_action" >&2
    echo "--- last 40 lines of $log ---" >&2
    tail -n 40 "$log" >&2
    exit 1
  fi
}

scoped() { # scoped EXPRESSION
  if [ -n "$scope" ]; then printf '(%s) and (%s)' "$1" "$scope"; else printf '%s' "$1"; fi
}

golden_expr="$(scoped 'binary(e2e) and test(/matches_fern_output/)')"
journey_expr="$(scoped 'binary(e2e) and not test(/matches_fern_output/)')"
unit_expr="$(scoped 'not binary(e2e)')"

count_tests() { # count_tests LABEL EXPRESSION
  local label="$1" expression="$2" listing count
  if ! listing="$(cd "$repo_root" && cargo nextest list --locked -E "$expression" 2>>"$log")"; then
    echo "fixtures-coverage: cargo nextest could not resolve the $label selection" \
         "'$expression'. Fix the filter expression (see 'cargo nextest list --help')" \
         "or the SCOPE argument." >&2
    tail -n 20 "$log" >&2
    exit 1
  fi
  count="$(printf '%s' "$listing" | grep -c . || true)"
  if [ "$count" -eq 0 ]; then
    echo "fixtures-coverage: the $label selection '$expression' matched no tests," \
         "so its coverage figure would be a meaningless 0%. Widen the SCOPE argument." >&2
    exit 1
  fi
  printf '%s' "$count"
}

golden_tests="$(count_tests golden-only "$golden_expr")"
journey_tests="$(count_tests all-e2e "$journey_expr")"
unit_tests="$(count_tests non-e2e "$unit_expr")"
e2e_tests=$((golden_tests + journey_tests))

if [ "$fetch" -eq 1 ]; then
  step "fetching the corpus specs" \
    "The link-ok corpus is fetched over the network (tests/fixtures/CORPUS.md); \
re-run with --no-fetch to reuse .local/corpus offline." \
    "$script_dir/fetch-corpus.sh"
fi

cd "$repo_root"

# CROZIER_REQUIRE_CORPUS turns an unfetched corpus spec from a silent skip into a
# hard failure, so the golden denominator can never quietly shrink.
export CROZIER_REQUIRE_CORPUS=1

corpus_next_action="A byte-match test failed or a corpus spec is unfetched. Run \
'just test-corpus-match' to see which, then 'just fixtures-diff <corpus>' for the diff."

step "clearing stale coverage profiles" \
  "Remove target/llvm-cov-target by hand and retry." \
  cargo llvm-cov clean --profraw-only

step "measuring the non-e2e tier" \
  "Run 'just test' to see the failure on its own." \
  cargo llvm-cov --locked --no-report nextest -E "$unit_expr"
step "exporting the non-e2e tier" "Retry; if it persists, upgrade cargo-llvm-cov." \
  cargo llvm-cov report --locked --json --output-path "$out_dir/non-e2e.json"

step "clearing the non-e2e profiles" \
  "Remove target/llvm-cov-target by hand and retry." \
  cargo llvm-cov clean --profraw-only

step "measuring the golden-only tier" "$corpus_next_action" \
  cargo llvm-cov --locked --no-report nextest -E "$golden_expr"
step "exporting the golden-only tier" "Retry; if it persists, upgrade cargo-llvm-cov." \
  cargo llvm-cov report --locked --json --output-path "$out_dir/golden-only.json"

# No clean here: the journey run accumulates onto the golden profiles, so the
# next export is the union — the all-e2e tier.
step "measuring the e2e journey tests" \
  "Run 'just test-e2e' to see the failure on its own." \
  cargo llvm-cov --locked --no-report nextest -E "$journey_expr"
step "exporting the all-e2e tier" "Retry; if it persists, upgrade cargo-llvm-cov." \
  cargo llvm-cov report --locked --json --output-path "$out_dir/all-e2e.json"

python3 "$script_dir/fixtures-coverage-report.py" \
  --repo-root "$repo_root" \
  --golden-tier golden-only \
  --subprocess-file src/main.rs \
  --subprocess-tier golden-only \
  --subprocess-tier all-e2e \
  --tier "golden-only=$out_dir/golden-only.json=$golden_tests=$golden_expr" \
  --tier "all-e2e=$out_dir/all-e2e.json=$e2e_tests=$(scoped 'binary(e2e)')" \
  --tier "non-e2e=$out_dir/non-e2e.json=$unit_tests=$unit_expr"

echo "fixtures-coverage: per-tier llvm-cov exports in $out_dir" >&2
