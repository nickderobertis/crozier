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
case "$installed" in
    *"$expected"*) ;;
    *) echo "error: '$bin --version' reported '$installed', which does not contain the expected '$expected'; confirm the release tag matches the crate version in Cargo.toml and that the artifact for this tag was published" >&2; exit 1 ;;
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

# Capture the generator's output so success stays quiet (a single final line);
# on failure, surface the captured diagnostics plus a concrete next step.
if ! gen_out="$("$bin" generate \
    --spec "$work/openapi.yml" \
    --output "$work/out" \
    --package-name smoke \
    --project-name smoke 2>&1)"; then
    echo "error: 'crozier generate' failed on the smoke spec — reproduce with 'crozier generate --spec <spec> --output <dir> --package-name smoke' and inspect the output below:" >&2
    echo "$gen_out" >&2
    exit 1
fi

# The type layer crozier always emits for this spec: the version module, the
# PEP 561 marker, and the generated model. If any is missing the published
# binary is broken even though it started and reported a version.
for f in src/smoke/version.py src/smoke/py.typed src/smoke/types/widget.py; do
    if [ ! -f "$work/out/$f" ]; then
        echo "error: crozier ran but did not emit '$f' for the smoke spec; this build's type-layer generation (src/emit.rs) is broken — do not ship it" >&2
        exit 1
    fi
done

echo "smoke test passed: crozier $expected generated a working Python SDK"
