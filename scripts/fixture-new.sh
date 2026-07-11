#!/usr/bin/env bash
# Scaffold a new feature-coverage fixture: create tests/fixtures/<name>/ with a
# minimal placeholder openapi.yml and print the Corpus snippet to paste into
# tests/e2e.rs. It does NOT author the spec or touch e2e.rs — those are judgment
# (which shapes to exercise) and a source edit, kept in your hands on purpose.
#
# After this: replace openapi.yml with the spec you want to match, generate Fern's
# golden output with scripts/generate-fern-fixture.sh <name> (Docker + fern CLI),
# add the printed Corpus to FEATURE_TARGETS, then grow `matched` with
# `just fixtures-candidates`. See tests/fixtures/AGENTS.md.
#
# Usage:  scripts/fixture-new.sh <name>
set -euo pipefail

name="${1:-}"
[ -n "$name" ] || { echo "fixture-new: usage: scripts/fixture-new.sh <name>" >&2; exit 1; }

# Hold the name to a single safe path segment (same invariant as
# generate-fern-fixture.sh and crozier's --package-name): no slashes, no `..`, no
# leading `.`/`-`. Rejects traversal and keeps it a valid dir under tests/fixtures/.
case "$name" in
  *[!A-Za-z0-9._-]* | [.-]* | *..*)
    echo "fixture-new: invalid name '$name' — must match [A-Za-z0-9][A-Za-z0-9._-]*" >&2
    exit 1 ;;
esac

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$repo_root/tests/fixtures/$name"
[ -e "$dir" ] && { echo "fixture-new: $dir already exists — refusing to overwrite" >&2; exit 1; }

mkdir -p "$dir"
cat > "$dir/openapi.yml" <<'YAML'
# PLACEHOLDER — replace with the OpenAPI document this fixture should match.
# crozier consumes only this file; author the shapes you want to exercise, then
# regenerate Fern's golden output with scripts/generate-fern-fixture.sh <name>.
openapi: 3.0.0
info:
  title: fern
  version: 0.0.0
paths: {}
components:
  schemas: {}
YAML

echo "fixture-new: created tests/fixtures/$name/openapi.yml (placeholder)" >&2
cat >&2 <<EOF
fixture-new: next steps —
  1. Replace tests/fixtures/$name/openapi.yml with the real spec.
  2. Generate Fern's golden tree:  scripts/generate-fern-fixture.sh $name
  3. Add this to FEATURE_TARGETS in tests/e2e.rs:

    Corpus {
        api: "$name",
        package_name: "fern",
        project_name: "default_package_name",
        matched: &[],
    },

  4. Grow \`matched\` as generation lands:  just fixtures-candidates
EOF
