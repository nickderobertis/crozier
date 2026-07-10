#!/usr/bin/env bash
# Post-install smoke test for a *published* crozier binary.
#
# Given the expected version, assert `crozier --version` matches, then drive a
# real end-to-end generation and assert it wrote the expected Python SDK. This is
# the shared check the release.yml verify-* jobs run against the real artifacts —
# the crates.io crate, the PyPI wheel, and the GitHub-Release binary fetched by
# scripts/install.sh — so "it published" always means "it installs AND runs",
# not merely "the version string is right".
#
# Runnable locally against any crozier on PATH:  scripts/smoke.sh 0.1.0
# Point it at a specific binary with CROZIER_BIN=/path/to/crozier.
set -euo pipefail

expected="${1:?usage: smoke.sh <expected-version>}"
bin="${CROZIER_BIN:-crozier}"

installed="$("$bin" --version)"
echo "installed: $installed"
case "$installed" in
    *"$expected"*) ;;
    *) echo "error: version mismatch: '$installed' does not contain '$expected'" >&2; exit 1 ;;
esac

"$bin" --help >/dev/null

work="$(mktemp -d 2>/dev/null || mktemp -d -t crozier-smoke)"
trap 'rm -rf "$work"' EXIT

cat > "$work/openapi.yml" <<'YAML'
openapi: 3.0.0
info:
  title: Smoke API
  version: 1.0.0
paths: {}
components:
  schemas:
    Widget:
      type: object
      properties:
        id:
          type: string
YAML

"$bin" generate \
    --spec "$work/openapi.yml" \
    --output "$work/out" \
    --package-name smoke \
    --project-name smoke

# The type layer crozier always emits for this spec: the version module, the
# PEP 561 marker, and the generated model. If any is missing the published
# binary is broken even though it started and reported a version.
for f in src/smoke/version.py src/smoke/py.typed src/smoke/types/widget.py; do
    if [ ! -f "$work/out/$f" ]; then
        echo "error: expected generated file missing: $f" >&2
        exit 1
    fi
done

echo "smoke test passed: crozier $expected generated a working Python SDK"
