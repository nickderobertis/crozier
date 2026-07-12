#!/usr/bin/env bash
# Fetch link-only corpus source repositories from tests/fixtures/CORPUS.md.
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
dry_run=0
if [ "${1:-}" = "--dry-run" ]; then
  dry_run=1
  shift
fi
dest_root="${1:-$repo_root/.local/corpus}"

[ -f "$manifest" ] || { echo "fetch-corpus: missing $manifest" >&2; exit 1; }
mkdir -p "$dest_root"

awk -F '|' '
  NR > 6 && $8 ~ /link-only/ {
    name=$3; url=$5; ref=$6;
    gsub(/^[ `]+|[ `]+$/, "", name);
    gsub(/^[ ]+|[ ]+$/, "", url);
    gsub(/^[ `]+|[ `]+$/, "", ref);
    print name "\t" url "\t" ref;
  }
' "$manifest" |
while IFS=$'\t' read -r name url ref; do
  [ -n "$name" ] || continue
  target="$dest_root/$name"
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\t%s\n' "$name" "$url" "$ref"
    continue
  fi
  if [ -d "$target/.git" ]; then
    git -C "$target" fetch --quiet --tags origin
  else
    git clone --quiet --filter=blob:none "$url" "$target"
  fi
  if [ "$ref" != "HEAD" ]; then
    git -C "$target" checkout --quiet "$ref"
  fi
done

if [ "$dry_run" -eq 0 ]; then
  echo "fetch-corpus: fetched link-only corpus repos into $dest_root" >&2
fi
