#!/usr/bin/env bash
# Generate Fern golden `expected/` trees for the issue #77 corpus entries that are
# ready to be committed. By default it targets the whole 50-entry corpus and
# refuses to skip link-only rows, so "generate all" cannot silently produce a
# partial fixture set.
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
mode=all
dry_run=0

usage() {
  cat >&2 <<'USAGE'
Usage: scripts/generate-corpus-fixtures.sh [--all|--committed] [--dry-run]

  --all        Require every issue #77 manifest row to be commit-ready before
               generating. This is the default and fails on link-only rows.
  --committed  Generate only rows already marked `committed` in CORPUS.md.
  --dry-run    Print the fixture generation plan without running Fern.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --all) mode=all ;;
    --committed) mode=committed ;;
    --dry-run) dry_run=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "generate-corpus-fixtures: unknown argument '$1'" >&2; usage; exit 1 ;;
  esac
  shift
done

[ -f "$manifest" ] || { echo "generate-corpus-fixtures: missing $manifest" >&2; exit 1; }

fixture_for() {
  case "$1" in
    fern-seed-query-parameters) printf '%s\n' query-parameters-openapi ;;
    fern-exhaustive) printf '%s\n' exhaustive ;;
    *) printf '%s\n' "$1" ;;
  esac
}

rows="$({
  awk -F '|' '
    NR > 6 {
      name=$3; ref=$6; decision=$8;
      gsub(/^[ `]+|[ `]+$/, "", name);
      gsub(/^[ `]+|[ `]+$/, "", ref);
      gsub(/^[ ]+|[ ]+$/, "", decision);
      if (name != "") print name "\t" ref "\t" decision;
    }
  ' "$manifest"
})"

blocked=0
plan=()
while IFS=$'\t' read -r name ref decision; do
  [ -n "$name" ] || continue
  fixture="$(fixture_for "$name")"
  if [ "$decision" != committed ]; then
    if [ "$mode" = all ]; then
      echo "generate-corpus-fixtures: blocked $name ($decision, ref=$ref) — pin the source, review redistribution rights, vendor tests/fixtures/$fixture/openapi.yml, then mark it committed" >&2
      blocked=1
    fi
    continue
  fi
  if [ ! -f "$repo_root/tests/fixtures/$fixture/openapi.yml" ]; then
    echo "generate-corpus-fixtures: committed row $name points at missing tests/fixtures/$fixture/openapi.yml" >&2
    blocked=1
    continue
  fi
  plan+=("$fixture")
done <<<"$rows"

if [ "$blocked" -ne 0 ]; then
  echo "generate-corpus-fixtures: refusing to generate a partial issue #77 corpus; use --committed only for an explicit subset refresh" >&2
  exit 1
fi

if [ "${#plan[@]}" -eq 0 ]; then
  echo "generate-corpus-fixtures: no committed corpus rows to generate" >&2
  exit 1
fi

for fixture in "${plan[@]}"; do
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\n' "$fixture"
  else
    "$repo_root/scripts/generate-fern-fixture.sh" "$fixture"
  fi
done
