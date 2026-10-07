#!/usr/bin/env bash
# Fetch registered corpus sources from their pinned tests/fixtures/CORPUS.md URLs
# into the ignored cache. Rebuild tooling only: every gate reads the committed
# copies under tests/fixtures/corpus-sources/ (tools/corpus/corpus_sources.py).
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "$script_dir/corpus-lib.sh"
. "$script_dir/../../scripts/lib.sh"
repo_root="$(cd "$script_dir/../.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
dry_run=0
selector=""
if_missing=0
dest_root="$repo_root/.local/corpus"

usage() {
  cat >&2 <<'USAGE'
Usage: tools/corpus/fetch-corpus.sh [--dry-run] [--fixture NAME] [--if-missing] [DEST_ROOT]

  --fixture NAME  Fetch one canonical CORPUS.md row and print its local path.
  --if-missing    With --fixture, reuse a nonempty canonical cached spec.
  --dry-run       Print the matching registered rows without fetching them.
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
        echo "fetch-corpus: more than one destination root was provided — supply exactly one" \
             "DEST_ROOT (or none, for .local/corpus), then re-run" >&2
        exit 1
      }
      dest_root="$1"
      ;;
  esac
  shift
done

[ -z "$selector" ] || valid_fixture_name "$selector" || {
  echo "fetch-corpus: invalid fixture name '$selector' — pass one CORPUS.md row name or" \
       "fixture directory (letters, digits, '.', '_' and '-'; not starting with '.' or '-';" \
       "no '..'), then re-run" >&2
  exit 1
}
[ "$if_missing" -eq 0 ] || [ -n "$selector" ] || {
  echo "fetch-corpus: --if-missing requires --fixture" >&2
  exit 1
}

[ -f "$manifest" ] || {
  echo "fetch-corpus: missing $manifest — it is committed; restore it with" \
       "git checkout -- tests/fixtures/CORPUS.md, then re-run" >&2
  exit 1
}
mkdir -p "$dest_root"

# Read the rows before the loop: a failure inside `< <(...)` would reach neither
# `set -e` nor pipefail, and the loop would run over a partial plan.
rows="$(corpus_rows "$manifest")" || {
  echo "fetch-corpus: could not read the numbered rows of $manifest — make it readable" \
       "(restore it with git checkout -- tests/fixtures/CORPUS.md), then re-run" >&2
  exit 1
}
found=0
while IFS=$'\t' read -r name url ref _; do
  [ -n "$name" ] || continue
  fixture="$(corpus_fixture_for "$name")"
  if [ -n "$selector" ] && [ "$selector" != "$name" ] && [ "$selector" != "$fixture" ]; then
    continue
  fi
  found=1
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\t%s\n' "$name" "$url" "$ref"
    continue
  fi
  cached=""
  tree_root="$(corpus_tree_root "$name")"
  if [ -n "$tree_root" ]; then
    cached="$dest_root/$name/$tree_root"
  elif corpus_is_direct_spec_url "$url"; then
    cached="$dest_root/$name/$(corpus_spec_cache_filename "$url")"
  fi
  # A cached spec is only reusable when it already carries this row's recorded
  # remote-`$ref` pins. Neither a pre-change unpinned cache nor one written under
  # a superseded pin may mask the current manifest, so either falls through to a
  # real fetch. Routine CI uses committed copies; Fern rebuilds fetch explicitly.
  if [ "$if_missing" -eq 1 ] && [ -n "$tree_root" ] && [ -s "$cached" ] &&
    corpus_tree_verify "$name" "$dest_root/$name"; then
    source_path="$cached"
  elif [ "$if_missing" -eq 1 ] && [ -z "$tree_root" ] && [ -n "$cached" ] && [ -s "$cached" ] &&
    corpus_pin_verify "$name" "$cached"; then
    source_path="$cached"
  else
    source_path="$(corpus_fetch_source "$dest_root" "$name" "$url" "$ref")"
  fi
  if [ -n "$selector" ]; then
    printf '%s\n' "$source_path"
    break
  fi
done <<<"$rows"

[ "$found" -eq 1 ] || {
  echo "fetch-corpus: fixture '$selector' is not a canonical CORPUS.md row — choose a" \
       "numbered link-ok or committed row of tests/fixtures/CORPUS.md (list them with" \
       "tools/corpus/fetch-corpus.sh --dry-run), then re-run" >&2
  exit 1
}

if [ "$dry_run" -eq 0 ] && [ -z "$selector" ]; then
  echo "fetch-corpus: fetched registered corpus sources into $dest_root" >&2
fi
