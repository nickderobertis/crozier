#!/usr/bin/env bash
# End the GitHub Action with `crozier compare`'s own exit status, so the step
# passes on 0 and fails on 1, 3 and 4 (docs/compare.md#exit-statuses), after one
# result line in that status's colour: a pass green, a failure red, and
# could-not-check yellow.
#
# Reads EXIT_CODE (compare.sh's `exit-code` output).
set -euo pipefail

# shellcheck source=scripts/action/lib.sh
. "$(dirname "$0")/lib.sh"

code="${EXIT_CODE:-}"
[[ "$code" =~ ^[0-9]+$ ]] || die "EXIT_CODE '$code' is not an exit status" \
  "pass the compare step's exit-code output; an empty one means that step did not finish"

case "$code" in
  0) line="$(paint green "crozier compare: every checked generator matched (exit 0)")" ;;
  3) line="$(paint red "crozier compare: a generator mismatched its reference (exit 3)")" ;;
  4) line="$(paint yellow "crozier compare: no mismatch, but a generator could not be checked (exit 4)")" ;;
  *) line="$(paint red "crozier compare: the command failed (exit $code); see its error above")" ;;
esac
printf '%s\n' "$line" >&2
exit "$code"
