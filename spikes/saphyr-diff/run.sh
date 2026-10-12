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
# SAPHYR_DIFF_MODES (`;`-separated CROZIER_SPIKE_YAML values) picks the modes;
# see src/spike_yaml.rs for the flags.
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
modes=${SAPHYR_DIFF_MODES:-tree=direct;tree=json;tree=saphyr}
export SAPHYR_DIFF_MODES=$modes

cargo build --locked --quiet --profile spike -p saphyr-diff
cargo build --locked --quiet --profile spike -p crozier --features spike-saphyr --bin crozier
target/spike/saphyr-diff "$@" | tee "$OUT/report.txt"

[ "$e2e" = 1 ] || exit 0

echo
echo "== end to end: crates/crozier-e2e --test e2e against target/spike/crozier, per reader mode =="
failing() {
  # nextest's final summary names every failing test once per line.
  grep -E '^\s+(FAIL|SIGSEGV|SIGABRT|TIMEOUT|LEAK-FAIL)\b' "$1" | awk '{print $NF}' | sort -u
}
IFS=';' read -r -a all <<<"off;$modes"
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
    # The first assertion line of that test's output, for the before/after text.
    awk -v t="$t" '$0 ~ "--- STDERR: .*"t"( |$)" {on=1; n=0; next} on && /panicked at|assertion|left:|right:|error|refus/ {print "      " substr($0,1,300); if (++n>=4) on=0}' "$log" | head -4
  done
  for t in $fixed; do echo "   newly passing: $t"; done
done
echo
echo "e2e logs: $OUT/e2e-*.log"
