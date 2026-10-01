#!/usr/bin/env bash
# Stands in for a team's copy of the Fern reference recipe (docs/fern-reference.md)
# in the migration journey (tests/e2e/migration.rs): instead of running Fern, it
# writes the committed Fern golden the test names in $MIGRATION_E2E_GOLDEN into
# $CROZIER_REFERENCE_OUTPUT, as the recipe writes Fern's output there.
set -euo pipefail
: "${MIGRATION_E2E_GOLDEN:?set by the migration e2e to the golden to copy}"
: "${CROZIER_REFERENCE_OUTPUT:?run this as a crozier compare reference command}"
cp -R "$MIGRATION_E2E_GOLDEN"/. "$CROZIER_REFERENCE_OUTPUT"
