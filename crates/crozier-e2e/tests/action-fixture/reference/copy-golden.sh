#!/usr/bin/env bash
# Write the committed golden for this layout's spec as the reference: exactly
# what crozier generates for it. With `--alter`, one file of it is changed, so
# the comparison finds one differing file.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cp -R "$here/../../../../../tests/fixtures/client-class-name/expected/." "$CROZIER_REFERENCE_OUTPUT"
if [ "${1:-}" = --alter ]; then
  echo "A line the reference has and crozier does not." >>"$CROZIER_REFERENCE_OUTPUT/README.md"
fi
