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
# difference. Each invocation's crozier profiles land in <out-dir>/<mode>-<round>/,
# its output in <out-dir>/<mode>-<round>.log, and its wall seconds and exit
# status in <out-dir>/runs.tsv (header: mode, round, seconds, exit).
# Exits 1, naming each failed invocation and its log, when any test run failed.
# llmlint: ignore[changed_behavior_has_e2e] SPIKE ONLY: one execution runs three of the largest golden e2e tests five times (about 4 minutes on Linux, 11 on Windows); it ran in run 45840622476 on both platforms and its runs.tsv and profiles are the report's A/B. ci-profile-journeys proves its refusal path and the reader proves its output columns.
set -euo pipefail
out=${1:?usage: ruff-batch-experiment.sh <out-dir> [rounds]}
rounds=${2:-2}
if ! [[ $rounds =~ ^[1-9][0-9]*$ ]]; then
  echo "ruff-batch-experiment: rounds must be a positive integer, not '$rounds'" >&2
  exit 2
fi
unwritable() {
  echo "ruff-batch-experiment: cannot write $1; pass an <out-dir> you can create files in" >&2
  exit 1
}
mkdir -p "$out" || unwritable "$out"
filter='test(=zulip_matches_fern_output) | test(=webflow_v2_matches_fern_output) | test(=embedpdf_cloudpdf_matches_fern_output)'
printf 'mode\tround\tseconds\texit\n' > "$out/runs.tsv" || unwritable "$out/runs.tsv"
failed=()
run() {
  local mode=$1 round=$2 value=$3
  local dir="$out/$mode-$round"
  mkdir -p "$dir" || unwritable "$dir"
  local start=$SECONDS status=0
  CROZIER_PROFILE="$dir" CROZIER_SPIKE_RUFF_BATCH="$value" NEXTEST_HIDE_PROGRESS_BAR=1 \
    cargo nextest run --locked --cargo-profile e2e -p crozier-e2e --test-threads 1 --no-fail-fast -E "$filter" \
    > "$dir.log" 2>&1 || status=$?
  printf '%s\t%s\t%s\t%s\n' "$mode" "$round" "$((SECONDS - start))" "$status" >> "$out/runs.tsv" || unwritable "$out/runs.tsv"
  if [ "$status" -ne 0 ]; then
    failed+=("$mode round $round (exit $status; output in $dir.log)")
    echo "ruff-batch-experiment: $mode round $round failed; the end of its output:" >&2
    tail -n 25 "$dir.log" >&2 || echo "ruff-batch-experiment: (could not read $dir.log)" >&2
  fi
}
for ((round = 1; round <= rounds; round++)); do
  run per-file "$round" ""
  run batch "$round" 1
done
run verify 1 verify
if [ "${#failed[@]}" -gt 0 ]; then
  printf 'ruff-batch-experiment: failed: %s\n' "${failed[@]}" >&2
  echo "ruff-batch-experiment: a verify failure names the file the batched ruff changed; rerun one mode with the same cargo nextest filter to reproduce it" >&2
  exit 1
fi
echo "ruff-batch-experiment: wrote $out/runs.tsv"
