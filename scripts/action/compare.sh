#!/usr/bin/env bash
# Run `crozier compare` for the GitHub Action (action.yml) and report what it
# found: the step outputs, the Markdown step summary, and one coloured result
# line. It adds no comparison logic: every count and figure is the CLI's own,
# read from its JSON report (assets/compare-report.schema.json).
#
# The CLI's exit status is captured, not acted on, so the diff artifact can be
# uploaded after a mismatch; finish.sh ends the action with it.
#
# Reads CROZIER (the binary; default `crozier` on PATH), COMPARE_PATHS
# (separated by any whitespace, newlines included; empty searches the
# repository), REFERENCE_COMMAND
# (empty uses each config's `reference.command`), RUNNER_TEMP, GITHUB_OUTPUT and
# GITHUB_STEP_SUMMARY.
set -euo pipefail

here="$(dirname "$0")"
# shellcheck source=scripts/action/lib.sh
. "$here/lib.sh"

[ -n "${RUNNER_TEMP:-}" ] || die "RUNNER_TEMP is not set" \
  "run this inside GitHub Actions, or set RUNNER_TEMP to a scratch directory"
[ -n "${GITHUB_OUTPUT:-}" ] || die "GITHUB_OUTPUT is not set" \
  "run this inside GitHub Actions, or set GITHUB_OUTPUT to a writable file"
command -v jq >/dev/null 2>&1 || die "jq is not on PATH" \
  "install jq (GitHub's Linux and macOS runners ship it)"

crozier="${CROZIER:-crozier}"
work="$RUNNER_TEMP/crozier-compare"
report="$work/report.json"
diffs="$work/diffs"
rm -rf "$work"
mkdir -p "$work"

# `-d ''` reads to the end rather than the first line, so a YAML block scalar
# (`paths: |`, one path per line) names every path it lists; read returns 1 at
# that end, which is not a failure.
read -r -d '' -a paths <<<"${COMPARE_PATHS:-}" || true
args=(compare --json "$report" --diff-dir "$diffs")
if [ -n "${REFERENCE_COMMAND:-}" ]; then
  args+=(--reference-command "$REFERENCE_COMMAND")
fi
# `--` keeps a path starting with `-` a path. bash 3.2 (macOS) rejects an empty
# "${paths[@]}" under `set -u`; the `+` form expands to nothing instead.
args+=(-- ${paths[@]+"${paths[@]}"})

# lib.sh exported CLICOLOR_FORCE=1, so the CLI colours the log too.
status=0
"$crozier" "${args[@]}" || status=$?

# Exit 1 before any reference ran (a path that does not exist, an unwritable
# --json target) leaves no report, and then no counts or figures either.
report_path=""
if jq -e '.schema_version == 1 or .schema_version == 2' "$report" >/dev/null 2>&1; then
  report_path="$report"
fi

field() {
  if [ -n "$report_path" ]; then
    jq -r "$1 | if . == null then \"\" else tostring end" "$report"
  fi
}
matched="$(field .counts.matched)"
mismatched="$(field .counts.mismatched)"
could_not_check="$(field .counts.could_not_check)"

{
  echo "exit-code=$status"
  echo "report-path=$report_path"
  echo "diff-dir=$diffs"
  echo "matched=$matched"
  echo "mismatched=$mismatched"
  echo "could-not-check=$could_not_check"
  echo "total-reference-seconds=$(field .timing_totals.reference_seconds)"
  echo "total-crozier-seconds=$(field .timing_totals.crozier_seconds)"
  echo "total-speedup=$(field .timing_totals.speedup)"
  echo "total-saved-seconds=$(field .timing_totals.saved_seconds)"
} >>"$GITHUB_OUTPUT"

if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  REPORT="$report_path" EXIT_CODE="$status" bash "$here/summary.sh" >>"$GITHUB_STEP_SUMMARY"
fi

if [ -n "$report_path" ]; then
  printf 'crozier-action: %s, %s, %s\n' \
    "$(paint green "$matched matched")" \
    "$(paint red "$mismatched mismatched")" \
    "$(paint yellow "$could_not_check could not check")" >&2
fi
