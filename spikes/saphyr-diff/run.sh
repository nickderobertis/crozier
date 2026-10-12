#!/usr/bin/env bash
# SPIKE (serde-yaml-replacement): the one command for the differential harness.
#
#   spikes/saphyr-diff/run.sh [--no-e2e] [trees|writes|load|generate|errors|settings|workflows|timing ...]
#
# 1. Builds the harness and a `spike-saphyr` crozier binary (profile `spike`).
# 2. Runs the harness: every difference per document kind between
#    serde_yaml_ng 0.10 (today) and serde-saphyr 1.3 / saphyr 0.2, in what is
#    read, written and what errors say. Report: $OUT/report.txt; every
#    occurrence: $OUT/details.txt.
# 3. Unless --no-e2e: runs the whole binary e2e suite (crates/crozier-e2e,
#    `--test e2e`: every committed Fern golden byte-compare and every refusal
#    journey) against the spike binary once per reader mode, and prints the
#    tests whose outcome differs from the `off` (serde_yaml_ng) baseline.
#
# SAPHYR_DIFF_MODES / SAPHYR_DIFF_E2E_MODES (`;`-separated CROZIER_SPIKE_YAML
# values) pick the harness's and the e2e suite's modes; SAPHYR_DIFF_FILTER keeps
# only documents whose path holds it. Flags: src/spike_yaml.rs.
set -euo pipefail
cd "$(dirname "$0")/../.."

OUT=${SAPHYR_DIFF_SCRATCH:-$PWD/target/saphyr-diff}
export SAPHYR_DIFF_SCRATCH=$OUT
mkdir -p "$OUT"
e2e=1
if [ "${1:-}" = "--no-e2e" ]; then
  e2e=0
  shift
fi
modes=${SAPHYR_DIFF_MODES:-tree=json;tree=saphyr;tree=json,strict_booleans,budget=none,nonfinite=string,merge=ordinary;tree=saphyr,strict_booleans,budget=none,nonfinite=string,merge=ordinary}
export SAPHYR_DIFF_MODES=$modes
# The e2e suite is slow (every golden runs `ruff format`), so it runs the raw
# default-Options reader once and the two candidate configurations. The
# today-wording adapter is not measured by default: errors need only say what
# failed and where (the user's ruling); SAPHYR_DIFF_TODAY_WORDING=1 shows it.
e2e_modes=${SAPHYR_DIFF_E2E_MODES:-tree=json;tree=json,strict_booleans,budget=none,nonfinite=string,merge=ordinary;tree=saphyr,strict_booleans,budget=none,nonfinite=string,merge=ordinary}

cargo build --locked --quiet --profile spike -p saphyr-diff
cargo build --locked --quiet --profile spike -p crozier --features spike-saphyr --bin crozier
target/spike/saphyr-diff "$@" | tee "$OUT/report.txt"

echo
echo "== supply chain: what serde-saphyr 1.3.0 and saphyr 0.2.1 bring in, against deny.toml =="
banned='^(serde_yaml|serde_yaml_ng|serde_norway|serde_yml|unsafe-libyaml|unsafe-libyaml-norway|libyml) '
for crate in serde-saphyr@1.3.0 saphyr@0.2.1; do
  deps=$(cargo tree --locked -p "$crate" -e normal,build --prefix none | sort -u)
  hits=$(printf '%s\n' "$deps" | grep -E "$banned" || true)
  echo "$crate: $(printf '%s\n' "$deps" | grep -c .) crates in its tree; YAML crates to replace in it: ${hits:-none}"
done
echo "cargo deny (licenses bans sources, whole workspace with the spike feature):"
cargo deny --all-features check licenses bans sources 2>&1 \
  | grep -E '^(error|warning)\[|rejected|license = |├ [a-z0-9_-]+ v[0-9]|└──|├──|(bans|licenses|sources) (ok|FAILED)' \
  | grep -v 'license-not-encountered' | head -30 || true
echo "which feature pulls a refused crate in:"
cargo tree --locked --all-features -i foldhash@0.2.0 -e features 2>/dev/null | grep -A3 'default-hasher' | head -4 || true

[ "$e2e" = 1 ] || exit 0

echo
echo "== end to end: crates/crozier-e2e --test e2e against target/spike/crozier, per reader mode =="
failing() {
  # nextest's final summary names every failing test once per line.
  # No failures is a grep miss, not an error.
  { grep -E '^\s+(FAIL|SIGSEGV|SIGABRT|TIMEOUT|LEAK-FAIL)\b' "$1" || true; } | awk '{print $NF}' | sort -u
}
IFS=';' read -r -a all <<<"off;$e2e_modes"
for mode in "${all[@]}"; do
  log="$OUT/e2e-${mode//[^a-z0-9]/_}.log"
  set +e
  CROZIER_SPIKE_YAML=$mode CARGO_BIN_EXE_crozier=$PWD/target/spike/crozier CROZIER_REQUIRE_CORPUS=1 \
    cargo nextest run --locked -p crozier-e2e --test e2e --no-fail-fast --test-threads 8 \
    --status-level fail --final-status-level fail --color never >"$log" 2>&1
  set -e
  summary=$(grep -E '^\s+Summary' "$log" | tail -1)
  echo "mode \`$mode\`: ${summary:-no nextest summary; see $log}"
  failing "$log" >"$log.failing"
done
base="$OUT/e2e-off.log.failing"
for mode in "${all[@]:1}"; do
  log="$OUT/e2e-${mode//[^a-z0-9]/_}.log"
  newly=$(comm -13 "$base" "$log.failing")
  fixed=$(comm -23 "$base" "$log.failing")
  echo
  echo "-- mode \`$mode\` vs \`off\`: $(printf '%s' "$newly" | grep -c . || true) newly failing, $(printf '%s' "$fixed" | grep -c . || true) newly passing"
  for t in $newly; do
    echo "   newly failing: $t"
    # The test's panic and its first assertion lines: the before/after text.
    grep -A3 "thread '$t' .* panicked at" "$log" | tail -n +2 | cut -c1-400 | sed 's/^ */      /' || true
  done
  for t in $fixed; do echo "   newly passing: $t"; done
done
echo
echo "e2e logs: $OUT/e2e-*.log"
