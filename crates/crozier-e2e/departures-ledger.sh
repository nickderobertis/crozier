#!/usr/bin/env bash
# Regenerate the per-golden departure ledger, tests/fixtures/departures-ledger.tsv,
# and the inventory of example values Fern writes that their own schema rejects,
# docs/departures/evidence/invalid-example-values/inventory.tsv: run every golden
# comparison with CROZIER_RECORD_DEPARTURES and CROZIER_RECORD_EXAMPLE_INVENTORY
# set, so each records the departures the engine applies and the rejected values
# it finds instead of holding them to the committed files, then merge the records
# (`write_departures_ledger`, `write_example_values_inventory`). Run it (`just
# departures-ledger`, the crozier-e2e project's target, which builds crozier
# first) after a change that adds, moves or removes a departure, and review the
# diff before committing; see docs/departures/README.md. CROZIER_REQUIRE_CORPUS
# makes a missing committed source fail rather than skip, so no golden's rows
# are lost. The ledger gate's own scratch tests expect ledger failures, so they
# are not run.
set -euo pipefail

fail() { echo "departures-ledger: $1" >&2; echo "departures-ledger: $2" >&2; exit 1; }

cd "$(dirname "$0")/../.." || fail "cannot enter the repository root above $0" "run it from a readable checkout"

scratch=$(mktemp -d "${TMPDIR:-/tmp}/crozier-departures.XXXXXX") \
  || fail "cannot create a temporary directory under ${TMPDIR:-/tmp}" "point TMPDIR at a writable directory and rerun"
trap 'rm -rf "$scratch" || echo "departures-ledger: could not remove $scratch; delete it by hand" >&2' EXIT
records="$scratch/records" inventory="$scratch/inventory" log="$scratch/log"
mkdir "$records" "$inventory" || fail "cannot create $records and $inventory" "point TMPDIR at a writable directory and rerun"

# llmlint: ignore[changed_behavior_has_e2e] running the whole crozier-e2e suite from its own tests would recurse; crates/crozier-e2e/tests/e2e/report_scripts.rs drives this script with only `cargo` stood in.
if ! CROZIER_REQUIRE_CORPUS=1 CROZIER_RECORD_DEPARTURES="$records" CROZIER_RECORD_EXAMPLE_INVENTORY="$inventory" cargo nextest run --locked -p crozier-e2e -p crozier-nested-discriminator-tests \
  --no-fail-fast -E 'not test(/^departures_ledger_gate::/)' >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "a comparison failed while recording (above)" "fix it, then rerun just departures-ledger"
fi
if ! CROZIER_RECORD_DEPARTURES="$records" CROZIER_RECORD_EXAMPLE_INVENTORY="$inventory" cargo nextest run --locked -p crozier-e2e --run-ignored only \
  -E 'test(=departures_ledger_gate::write_departures_ledger) | test(=example_values_inventory::write_example_values_inventory)' >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "the merged ledger or inventory was refused (above)" "fix the cause, then rerun just departures-ledger"
fi
ledger=tests/fixtures/departures-ledger.tsv
inventory_file=docs/departures/evidence/invalid-example-values/inventory.tsv
rows=$(wc -l < "$ledger") || fail "cannot read $ledger after writing it" "restore it with git checkout -- $ledger and rerun"
values=$(wc -l < "$inventory_file") || fail "cannot read $inventory_file after writing it" "restore it with git checkout -- $inventory_file and rerun"
echo "departures-ledger: wrote $ledger ($((rows - 1)) rows) and $inventory_file ($((values - 1)) rows)"
