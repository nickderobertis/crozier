#!/usr/bin/env bash
# Fetch (when needed) and generate Fern golden `expected/` trees for the issue #77
# corpus. Existing committed fixture specs are reused; link-only rows are cloned
# from their source URL, an OpenAPI document is discovered, vendored as
# tests/fixtures/<name>/openapi.yml, and then Fern generation runs.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "$script_dir/corpus-lib.sh"
repo_root="$(cd "$script_dir/.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
mode=all
dry_run=0
fetch_root="$repo_root/.local/corpus"

usage() {
  cat >&2 <<'USAGE'
Usage: scripts/generate-corpus-fixtures.sh [--all|--committed] [--dry-run] [--fetch-root DIR]

  --all        Fetch/use every issue #77 manifest row and generate its Fern fixture.
               This is the default.
  --committed  Generate only rows already marked `committed` in CORPUS.md.
  --dry-run    Print the generation plan, including source/discovered spec, without
               copying specs or running Fern.
  --fetch-root DIR
               Clone link-only source repositories under DIR (default .local/corpus).
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --all) mode=all ;;
    --committed) mode=committed ;;
    --dry-run) dry_run=1 ;;
    --fetch-root) shift; fetch_root="${1:?--fetch-root needs a directory}" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "generate-corpus-fixtures: unknown argument '$1'" >&2; usage; exit 1 ;;
  esac
  shift
done

[ -f "$manifest" ] || { echo "generate-corpus-fixtures: missing $manifest" >&2; exit 1; }


discover_openapi() {
  local root="$1" candidates count
  candidates="$({
    find "$root" \
      \( -path '*/.git' -o -path '*/node_modules' -o -path '*/target' -o -path '*/dist' -o -path '*/build' -o -path '*/vendor' \) -prune \
      -o -type f \( -name '*.yml' -o -name '*.yaml' -o -name '*.json' \) -size -20M -print0 |
    while IFS= read -r -d '' f; do
      if LC_ALL=C rg -q "(^|[\"'[:space:]])openapi([\"'[:space:]]*:|:)" "$f"; then
        printf '%s\n' "$f"
      fi
    done
  })"
  count="$(printf '%s\n' "$candidates" | sed '/^$/d' | wc -l | tr -d ' ')"
  case "$count" in
    0) return 1 ;;
    1) printf '%s\n' "$candidates" ;;
    *)
      echo "generate-corpus-fixtures: found multiple OpenAPI candidates under $root; set one up as tests/fixtures/<name>/openapi.yml before generating:" >&2
      printf '%s\n' "$candidates" >&2
      return 2
      ;;
  esac
}

plan=()
while IFS=$'\t' read -r name url ref decision; do
  [ -n "$name" ] || continue
  fixture="$(corpus_fixture_for "$name")"
  fixture_dir="$repo_root/tests/fixtures/$fixture"
  spec="$fixture_dir/openapi.yml"

  if [ "$mode" = committed ] && [ "$decision" != committed ]; then
    continue
  fi

  source_desc="committed"
  if [ ! -f "$spec" ]; then
    if [ "$decision" = committed ]; then
      echo "generate-corpus-fixtures: committed row $name points at missing $spec" >&2
      exit 1
    fi
    repo_dir="$(corpus_fetch_repo "$fetch_root" "$name" "$url" "$ref")"
    discovered="$(discover_openapi "$repo_dir")" || {
      echo "generate-corpus-fixtures: could not discover exactly one OpenAPI spec for $name from $url" >&2
      exit 1
    }
    source_desc="$discovered"
    if [ "$dry_run" -eq 0 ]; then
      mkdir -p "$fixture_dir"
      cp "$discovered" "$spec"
    fi
  fi

  plan+=("$fixture|$source_desc")
done < <(corpus_rows "$manifest")

if [ "${#plan[@]}" -eq 0 ]; then
  echo "generate-corpus-fixtures: no corpus rows selected" >&2
  exit 1
fi

for item in "${plan[@]}"; do
  fixture="${item%%|*}"
  source_desc="${item#*|}"
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\n' "$fixture" "$source_desc"
  else
    echo "generate-corpus-fixtures: generating $fixture (spec source: $source_desc)" >&2
    "$repo_root/scripts/generate-fern-fixture.sh" "$fixture"
  fi
done
