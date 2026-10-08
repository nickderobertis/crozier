#!/usr/bin/env bash
# Scaffold a new feature-coverage fixture: create tests/fixtures/<name>/ with a
# minimal placeholder openapi.yml and print the steps that wire it into
# crates/crozier-e2e/tests/e2e.rs. It does NOT author the spec or touch e2e.rs — those are judgment
# (which shapes to exercise) and a source edit, kept in your hands on purpose.
#
# After this: replace openapi.yml with the spec you want to match, generate Fern's
# golden output with tools/fern-goldens/generate-fern-fixture.sh <name> (Docker + fern CLI),
# copy an existing FEATURE_TARGETS entry for it as the printed steps say, then
# shrink its `unmatched` list with `just fixtures-gaps`. See tests/fixtures/AGENTS.md.
#
# Usage:  tools/fern-goldens/fixture-new.sh <name>
# Exit status: 0 once the placeholder is written; 2 for a missing or invalid
# name; 1 when the fixture exists already or cannot be created.
#
# llmlint: ignore-file[tool_output_is_signal] this is a scaffolder: its success
# output — the created path plus the wiring steps — IS the deliverable, the way
# `cargo new` / `git init` print next steps, not incidental chatter. The steps
# mirror tests/fixtures/AGENTS.md.
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd)" || {
  echo "fixture-new: cannot resolve the checkout from $0 — run it by its path from a readable checkout, then re-run" >&2
  exit 1
}
# shellcheck source=../../scripts/lib.sh
. "$repo_root/scripts/lib.sh" || {
  echo "fixture-new: cannot load $repo_root/scripts/lib.sh — restore it with git checkout -- scripts/lib.sh, then re-run" >&2
  exit 1
}

name="${1:-}"
[ "$#" -eq 1 ] && [ -n "$name" ] || { echo "fixture-new: usage: tools/fern-goldens/fixture-new.sh <name>" >&2; exit 2; }

# Hold the name to a single safe path segment (shared valid_fixture_name): rejects
# traversal and keeps it a valid dir under tests/fixtures/.
valid_fixture_name "$name" || {
  echo "fixture-new: invalid name '$name' — must match [A-Za-z0-9][A-Za-z0-9._-]*" >&2
  exit 2
}

dir="$repo_root/tests/fixtures/$name"
# A symlink counts as existing even when it dangles, which `-e` alone misses.
if [ -e "$dir" ] || [ -L "$dir" ]; then
  echo "fixture-new: $dir already exists — refusing to overwrite" >&2
  exit 1
fi

# A fixture directory is created whole or not at all, and the cleanup removes
# only a directory this run made.
made=""
undo_partial_fixture() {
  echo "fixture-new: could not create $dir/openapi.yml — check that tests/fixtures/ is writable and" \
       "the disk has free space, then re-run" >&2
  if [ -n "$made" ] && ! rm -rf "$dir"; then
    echo "fixture-new: could not remove the partial $dir either — delete it by hand (rm -rf $dir)" \
         "before re-running" >&2
  fi
  exit 1
}
mkdir -p "$dir" || undo_partial_fixture
made=1
cat > "$dir/openapi.yml" <<'YAML' || undo_partial_fixture
# PLACEHOLDER — replace with the OpenAPI document this fixture should match.
# crozier consumes only this file; author the shapes you want to exercise, then
# regenerate Fern's golden output with tools/fern-goldens/generate-fern-fixture.sh <name>.
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
  2. Generate Fern's golden tree:  tools/fern-goldens/generate-fern-fixture.sh $name
  3. Wire it into crates/crozier-e2e/tests/e2e.rs: copy an existing FEATURE_TARGETS entry, set
     api: "$name" and unmatched: &[] (empty is the target). Copying a real entry keeps
     the Corpus shape single-sourced — no hand-mirrored struct to drift.
  4. Add its #[test] and its tests/corpus_match/match.sh line; the gate fails without both.
  5. While crozier still diverges, list the files that differ:  just fixtures-gaps
EOF
