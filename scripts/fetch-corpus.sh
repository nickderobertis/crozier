#!/usr/bin/env bash
# Fetch URL-backed corpus sources from tests/fixtures/CORPUS.md into the ignored cache.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "$script_dir/corpus-lib.sh"
repo_root="$(cd "$script_dir/.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
dry_run=0
if [ "${1:-}" = "--dry-run" ]; then
  dry_run=1
  shift
fi
dest_root="${1:-$repo_root/.local/corpus}"

[ -f "$manifest" ] || { echo "fetch-corpus: missing $manifest" >&2; exit 1; }
mkdir -p "$dest_root"

corpus_rows "$manifest" |
while IFS=$'\t' read -r name url ref decision; do
  [ -n "$name" ] || continue
  [ "$decision" = link-ok ] || continue
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\t%s\n' "$name" "$url" "$ref"
    continue
  fi
  corpus_fetch_source "$dest_root" "$name" "$url" "$ref" >/dev/null
done

if [ "$dry_run" -eq 0 ]; then
  echo "fetch-corpus: fetched link-ok corpus sources into $dest_root" >&2
fi
