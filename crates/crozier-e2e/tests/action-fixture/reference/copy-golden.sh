#!/usr/bin/env bash
# Write the committed golden for this layout's spec as the reference: exactly
# what crozier generates for it. With `--alter`, one file of it is changed, so
# the comparison finds one differing file.
set -euo pipefail
case "$#:${1:-}" in
  0: | 1:--alter) ;;
  *) echo "copy-golden: usage: copy-golden.sh [--alter], not '$*'; fix the reference command in crozier.yml" >&2; exit 2 ;;
esac
here="$(cd "$(dirname "$0")" && pwd)" || { echo "copy-golden: cannot resolve this script's directory; run it by its path from a readable checkout" >&2; exit 1; }
if [ -z "${CROZIER_REFERENCE_OUTPUT:-}" ]; then
  echo "copy-golden: CROZIER_REFERENCE_OUTPUT is unset; crozier compare sets it — run this as the generator's reference command (crozier compare)" >&2
  exit 1
fi
golden="$here/../../../../../tests/fixtures/client-class-name/expected"
cp -R "$golden/." "$CROZIER_REFERENCE_OUTPUT" || {
  echo "copy-golden: cannot copy $golden into \$CROZIER_REFERENCE_OUTPUT; restore the golden with git checkout -- tests/fixtures/client-class-name" >&2
  exit 1
}
if [ "$#" -eq 1 ]; then
  echo "A line the reference has and crozier does not." >>"$CROZIER_REFERENCE_OUTPUT/README.md" || {
    echo "copy-golden: cannot alter $CROZIER_REFERENCE_OUTPUT/README.md; check the reference output directory is writable" >&2
    exit 1
  }
fi
