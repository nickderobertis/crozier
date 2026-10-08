#!/usr/bin/env bash
# The fixture-match loop's two reports, off the e2e suite's ignored reporters:
#   gaps   the exact expected files crozier still does not reproduce — the
#          ready-to-paste `unmatched` task lists (CROZIER_GAPS_CORPUS scopes it);
#   diff   the normalized diff of every committed fixture file crozier does not
#          reproduce, as the gate's comparison engine decides it (`-` Fern golden,
#          `+` crozier; CROZIER_DIFF_CORPUS / CROZIER_DIFF_FILE scope it).
# Run through `just fixtures-gaps` / `just fixtures-diff` (the crozier-e2e
# project's targets, which build crozier first). Neither gates.
#
# The summary-line grep is a drift gate: `cargo test <name>` exits 0 even when
# the exact-name filter matches nothing, so a renamed or removed reporter would
# otherwise no-op silently.
set -euo pipefail

fail() { echo "fixtures-report: $1" >&2; echo "fixtures-report: $2" >&2; exit 1; }

cd "$(dirname "$0")/../.." || fail "cannot enter the repository root above $0" "run it from a readable checkout"

[ "$#" -eq 1 ] || fail "takes exactly one report, got $#" "usage: crates/crozier-e2e/fixtures-report.sh gaps|diff"

case "${1:-}" in
  gaps) reporter=report_fixture_gaps summary='file(s) still unmatched across all corpora'
        restore="restore report_fixture_gaps in crates/crozier-e2e/tests/e2e.rs, or fix the self-check failure above" ;;
  diff) reporter=report_fixture_diffs summary='differing file(s) across the reported corpora'
        restore="restore report_fixture_diffs in crates/crozier-e2e/tests/e2e.rs, or pass a corpus that exists (just fixtures-diff <corpus>)" ;;
  *) fail "unknown report '${1:-}'" "usage: crates/crozier-e2e/fixtures-report.sh gaps|diff" ;;
esac

out=$(mktemp "${TMPDIR:-/tmp}/crozier-fixtures-$1.XXXXXX") \
  || fail "cannot create a temporary file under ${TMPDIR:-/tmp}" "point TMPDIR at a writable directory and rerun"
trap 'rm -f "$out" || echo "fixtures-report: could not remove $out; delete it by hand" >&2' EXIT

# llmlint: ignore[changed_behavior_has_e2e] this path runs the ignored whole-corpus reporters, so running it inside crozier-e2e's own tests would rebuild and rerun that suite inside itself; crates/crozier-e2e/tests/e2e/report_scripts.rs runs this real script with only the `cargo` boundary stood in, covering extraction, a missing summary, a failing reporter and temp-file cleanup. The real path is `just fixtures-gaps` / `just fixtures-diff`.
if cargo test --locked -p crozier-e2e --test e2e -- --ignored --nocapture "$reporter" >"$out" 2>&1 \
  && grep -qF "$summary" "$out"; then
  # Only the report, from the first corpus header through the summary, never
  # cargo's build/test scaffolding.
  # llmlint: ignore[tool_output_is_signal] Printing this report is the documented behaviour of `just fixtures-gaps` / `just fixtures-diff` (tests/fixtures/AGENTS.md, "prints the normalized diff"); everything else cargo printed is dropped, and a failure prints the whole log plus the fix.
  awk -v summary="$summary" '/^=== /{p=1} p; index($0, summary){p=0}' "$out" \
    || fail "could not print the report from $out" "check that ${TMPDIR:-/tmp} is readable, then rerun"
else
  cat "$out" >&2 || echo "fixtures-report: could not read the run log $out" >&2
  fail "no report from $reporter (output above)" "$restore"
fi
