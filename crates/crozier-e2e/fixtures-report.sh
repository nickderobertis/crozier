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
set -uo pipefail
cd "$(dirname "$0")/../.."

case "${1:-}" in
  gaps) reporter=report_fixture_gaps summary='file(s) still unmatched across all corpora'
        drift="its self-check failed" ;;
  diff) reporter=report_fixture_diffs summary='differing file(s) across the reported corpora'
        drift="the corpus filter matched nothing" ;;
  *) echo "usage: crates/crozier-e2e/fixtures-report.sh gaps|diff" >&2; exit 2 ;;
esac

out=$(mktemp "${TMPDIR:-/tmp}/crozier-fixtures-$1.XXXXXX")
trap 'rm -f "$out"' EXIT
status=0
cargo test --locked -p crozier-e2e --test e2e -- --ignored --nocapture "$reporter" >"$out" 2>&1 || status=$?
if [ "$status" -eq 0 ] && grep -qF "$summary" "$out"; then
  # Quiet on success: only the report, from the first corpus header through the
  # summary, not cargo's build/test scaffolding.
  awk -v summary="$summary" '/^=== /{p=1} p; index($0, summary){p=0}' "$out"
else
  cat "$out" >&2
  echo "fixtures-$1: no report from $reporter — renamed/removed in crates/crozier-e2e/tests/e2e.rs, or $drift" >&2
  exit 1
fi
