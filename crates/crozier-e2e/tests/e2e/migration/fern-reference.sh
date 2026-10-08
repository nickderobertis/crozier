#!/usr/bin/env bash
# Stands in for a team's copy of the Fern reference recipe (docs/fern-reference.md)
# in the migration journey (crates/crozier-e2e/tests/e2e/migration.rs): instead
# of running Fern, it writes the committed Fern golden the test names in
# $MIGRATION_E2E_GOLDEN into $CROZIER_REFERENCE_OUTPUT, as the recipe writes
# Fern's output there.
set -euo pipefail
: "${MIGRATION_E2E_GOLDEN:?is unset — run this through the migration e2e (cargo nextest run -p crozier-e2e -E 'test(/migration/)'), or set it to a committed golden directory}"
: "${CROZIER_REFERENCE_OUTPUT:?run this as a crozier compare reference command}"
cp -R "$MIGRATION_E2E_GOLDEN"/. "$CROZIER_REFERENCE_OUTPUT" || {
  echo "fern-reference: could not copy the golden $MIGRATION_E2E_GOLDEN into" \
       "$CROZIER_REFERENCE_OUTPUT — check that the golden directory exists and the" \
       "output directory is writable, then re-run" >&2
  exit 1
}
