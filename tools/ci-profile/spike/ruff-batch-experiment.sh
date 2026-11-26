#!/usr/bin/env bash
# SPIKE ONLY (spike-windows-lane-breakdown): what one `ruff format` process per
# generation saves against one per file, on a few large goldens, with the
# output proved byte-identical.
#
#   bash tools/ci-profile/spike/ruff-batch-experiment.sh <out-dir> [rounds]
#
# Runs the goldens' own e2e tests (which byte-compare crozier's tree with the
# committed golden) one at a time, alternating per-file and batched formatting
# for `rounds` rounds (default 2), then once with CROZIER_SPIKE_RUFF_BATCH=verify,
# under which crozier formats every file both ways and fails on any byte of
# difference. Each invocation's crozier profiles land in <out-dir>/<mode>-<round>/
# and its wall seconds and exit status in <out-dir>/runs.tsv.
set -uo pipefail
out=${1:?usage: ruff-batch-experiment.sh <out-dir> [rounds]}
rounds=${2:-2}
mkdir -p "$out"
filter='test(=zulip_matches_fern_output) | test(=webflow_v2_matches_fern_output) | test(=embedpdf_cloudpdf_matches_fern_output)'
printf 'mode\tround\tseconds\texit\n' > "$out/runs.tsv"
run() {
  local mode=$1 round=$2 value=$3
  local dir="$out/$mode-$round"
  mkdir -p "$dir"
  local start end status
  start=$(date +%s.%N)
  CROZIER_PROFILE="$dir" CROZIER_SPIKE_RUFF_BATCH="$value" NEXTEST_HIDE_PROGRESS_BAR=1 \
    cargo nextest run --locked --cargo-profile e2e -p crozier-e2e --test-threads 1 --no-fail-fast -E "$filter" \
    > "$dir.log" 2>&1
  status=$?
  end=$(date +%s.%N)
  printf '%s\t%s\t%s\t%s\n' "$mode" "$round" "$(awk "BEGIN{print $end-$start}")" "$status" >> "$out/runs.tsv"
}
for round in $(seq 1 "$rounds"); do
  run per-file "$round" ""
  run batch "$round" 1
done
run verify 1 verify
echo "ruff-batch-experiment: wrote $out/runs.tsv"
