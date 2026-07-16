#!/usr/bin/env bash
# Fetch URL-backed corpus sources from tests/fixtures/CORPUS.md into the ignored cache.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "$script_dir/corpus-lib.sh"
. "$script_dir/lib.sh"
repo_root="$(cd "$script_dir/.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
dry_run=0
selector=""
if_missing=0
dest_root="$repo_root/.local/corpus"

usage() {
  cat >&2 <<'USAGE'
Usage: scripts/fetch-corpus.sh [--dry-run] [--fixture NAME] [--if-missing] [DEST_ROOT]

  --fixture NAME  Fetch one canonical CORPUS.md row and print its local path.
  --if-missing    With --fixture, reuse a nonempty canonical cached spec.
  --dry-run       Print matching link-ok rows without fetching them.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run) dry_run=1 ;;
    --fixture)
      shift
      [ "$#" -gt 0 ] || { echo "fetch-corpus: --fixture needs a name" >&2; exit 1; }
      selector="$1"
      ;;
    --if-missing) if_missing=1 ;;
    -h|--help) usage; exit 0 ;;
    --*) echo "fetch-corpus: unknown argument '$1'" >&2; usage; exit 1 ;;
    *)
      [ "$dest_root" = "$repo_root/.local/corpus" ] || {
        echo "fetch-corpus: more than one destination root was provided" >&2
        exit 1
      }
      dest_root="$1"
      ;;
  esac
  shift
done

[ -z "$selector" ] || valid_fixture_name "$selector" || {
  echo "fetch-corpus: invalid fixture name '$selector'" >&2
  exit 1
}
[ "$if_missing" -eq 0 ] || [ -n "$selector" ] || {
  echo "fetch-corpus: --if-missing requires --fixture" >&2
  exit 1
}

[ -f "$manifest" ] || { echo "fetch-corpus: missing $manifest" >&2; exit 1; }
mkdir -p "$dest_root"

found=0
while IFS=$'\t' read -r name url ref decision; do
  [ -n "$name" ] || continue
  fixture="$(corpus_fixture_for "$name")"
  if [ -n "$selector" ] && [ "$selector" != "$name" ] && [ "$selector" != "$fixture" ]; then
    continue
  fi
  if [ -z "$selector" ] && [ "$decision" != link-ok ]; then
    continue
  fi
  found=1
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\t%s\n' "$name" "$url" "$ref"
    continue
  fi
  cached=""
  if corpus_is_direct_spec_url "$url"; then
    cached="$dest_root/$name/$(corpus_spec_cache_filename "$url")"
  fi
  if [ "$if_missing" -eq 1 ] && [ -n "$cached" ] && [ -s "$cached" ]; then
    source_path="$cached"
  else
    source_path="$(corpus_fetch_source "$dest_root" "$name" "$url" "$ref")"
  fi
  if [ -n "$selector" ]; then
    printf '%s\n' "$source_path"
    break
  fi
done < <(corpus_rows "$manifest")

[ "$found" -eq 1 ] || {
  echo "fetch-corpus: fixture '$selector' is not a canonical CORPUS.md row" >&2
  exit 1
}

if [ "$dry_run" -eq 0 ] && [ -z "$selector" ]; then
  echo "fetch-corpus: fetched link-ok corpus sources into $dest_root" >&2
fi
