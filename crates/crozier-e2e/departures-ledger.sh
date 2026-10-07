#!/usr/bin/env bash
# Regenerate the per-golden departure ledger, tests/fixtures/departures-ledger.tsv:
# run every golden comparison with CROZIER_RECORD_DEPARTURES set, so each records
# the departures the engine applies instead of holding them to the ledger, then
# merge the records into the ledger (`write_departures_ledger`). Run it (`just
# departures-ledger`, the crozier-e2e project's target, which builds crozier
# first) after a change that adds, moves or removes a departure, and review the
# diff before committing; see docs/departures/README.md. CROZIER_REQUIRE_CORPUS
# makes a missing committed source fail rather than skip, so no golden's rows
# are lost. The ledger gate's own scratch tests expect ledger failures, so they
# are not run.
set -uo pipefail
cd "$(dirname "$0")/../.."

records=$(mktemp -d "${TMPDIR:-/tmp}/crozier-departures.XXXXXX")
log=$(mktemp "${TMPDIR:-/tmp}/crozier-departures-log.XXXXXX")
trap 'rm -rf "$records" "$log"' EXIT
if ! CROZIER_REQUIRE_CORPUS=1 CROZIER_RECORD_DEPARTURES="$records" cargo nextest run --locked -p crozier-e2e \
  --no-fail-fast -E 'not test(/^departures_ledger_gate::/)' >"$log" 2>&1; then
  cat "$log" >&2
  echo "departures-ledger: a comparison failed while recording (above); fix it, then rerun" >&2
  exit 1
fi
if ! CROZIER_RECORD_DEPARTURES="$records" cargo nextest run --locked -p crozier-e2e --run-ignored only \
  -E 'test(=departures_ledger_gate::write_departures_ledger)' >"$log" 2>&1; then
  cat "$log" >&2
  echo "departures-ledger: the merged ledger was refused (above); fix the cause, then rerun" >&2
  exit 1
fi
echo "departures-ledger: wrote tests/fixtures/departures-ledger.tsv ($(($(wc -l < tests/fixtures/departures-ledger.tsv) - 1)) rows)"
