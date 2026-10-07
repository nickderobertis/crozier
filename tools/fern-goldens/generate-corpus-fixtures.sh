#!/usr/bin/env bash
# Fetch (when needed) and generate Fern golden `expected/` trees for the issue #77
# corpus. Existing committed fixture specs are reused. URL-only rows are fetched
# into the ignored cache under .local/corpus and passed directly to Fern so source
# specs do not need to be vendored just to refresh generated output.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "$script_dir/../corpus/corpus-lib.sh"
repo_root="$(cd "$script_dir/../.." && pwd)"
manifest="$repo_root/tests/fixtures/CORPUS.md"
mode=all
dry_run=0
fetch_root="$repo_root/.local/corpus"
only=""

usage() {
  cat >&2 <<'USAGE'
Usage: tools/fern-goldens/generate-corpus-fixtures.sh [--all|--committed] [--only NAME] [--dry-run] [--fetch-root DIR]

  --all        Fetch/use every issue #77 manifest row and generate its Fern fixture.
               This is the default.
  --committed  Generate only rows already marked `committed` in CORPUS.md.
  --only NAME  Generate one manifest row, matching either its CORPUS.md name or
               its fixture directory name.
  --dry-run    Print the generation plan, including source/discovered spec, without
               running Fern or writing fixture output.
  --fetch-root DIR
               Cache direct specs and source repositories under DIR (default .local/corpus).
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --all) mode=all ;;
    --committed) mode=committed ;;
    --only) shift; only="${1:?--only needs a corpus name or fixture directory}" ;;
    --dry-run) dry_run=1 ;;
    --fetch-root) shift; fetch_root="${1:?--fetch-root needs a directory}" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "generate-corpus-fixtures: unknown argument '$1'" >&2; usage; exit 1 ;;
  esac
  shift
done

[ -f "$manifest" ] || {
  echo "generate-corpus-fixtures: missing $manifest — it is committed; restore it with" \
       "git checkout -- tests/fixtures/CORPUS.md, then re-run" >&2
  exit 1
}


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

# Read the rows before the loop: a failure inside `< <(...)` would reach neither
# `set -e` nor pipefail, and the loop would run over a partial plan.
rows="$(corpus_rows "$manifest")" || {
  echo "generate-corpus-fixtures: could not read the numbered rows of $manifest — make it readable" \
       "(restore it with git checkout -- tests/fixtures/CORPUS.md), then re-run" >&2
  exit 1
}
plan=()
while IFS=$'\t' read -r name url ref decision; do
  [ -n "$name" ] || continue
  fixture="$(corpus_fixture_for "$name")"
  fixture_dir="$repo_root/tests/fixtures/$fixture"
  spec="$fixture_dir/openapi.yml"

  if [ -n "$only" ] && [ "$only" != "$name" ] && [ "$only" != "$fixture" ]; then
    continue
  fi

  if [ "$mode" = committed ] && [ "$decision" != committed ]; then
    continue
  fi

  source_desc="$spec"
  if [ ! -f "$spec" ]; then
    if [ "$decision" = committed ]; then
      echo "generate-corpus-fixtures: committed row $name points at missing $spec — restore" \
           "it (git checkout -- tests/fixtures/$fixture/openapi.yml), or stage the row's" \
           "source there (tools/corpus/fetch-corpus.sh --fixture $fixture prints the fetched" \
           "document's path; copy it to $spec), then re-run" >&2
      exit 1
    fi
    source_path="$(corpus_fetch_source "$fetch_root" "$name" "$url" "$ref")"
    if [ -f "$source_path" ]; then
      discovered="$source_path"
    else
      discovered="$(discover_openapi "$source_path")" || {
        echo "generate-corpus-fixtures: could not discover exactly one OpenAPI spec for $name" \
             "from $url — copy the intended document under $source_path to $spec (this" \
             "script then generates from it), then re-run" >&2
        exit 1
      }
    fi
    source_desc="$discovered"
  fi

  plan+=("$fixture|$source_desc")
done <<<"$rows"

if [ "${#plan[@]}" -eq 0 ]; then
  if [ -n "$only" ]; then
    echo "generate-corpus-fixtures: no corpus rows selected — --only '$only' names no" \
         "numbered link-ok or committed row ($mode mode) of tests/fixtures/CORPUS.md; pass" \
         "one of its row names or fixture directories (--dry-run without --only lists" \
         "them), then re-run" >&2
  else
    echo "generate-corpus-fixtures: no corpus rows selected — tests/fixtures/CORPUS.md has" \
         "no numbered row that $mode mode selects (--committed takes committed rows, --all" \
         "link-ok or committed ones); register a row there, or use --all when none is" \
         "marked committed, then re-run" >&2
  fi
  exit 1
fi

for item in "${plan[@]}"; do
  fixture="${item%%|*}"
  source_desc="${item#*|}"
  if [ "$dry_run" -eq 1 ]; then
    printf '%s\t%s\n' "$fixture" "$source_desc"
  else
    # The generator prints its own one-line summary; the fixture and its source
    # are named here only when it fails.
    status=0
    "$repo_root/tools/fern-goldens/generate-fern-fixture.sh" "$fixture" "${FERN_PYTHON_VERSION-}" "$source_desc" ||
      status=$?
    if [ "$status" -ne 0 ]; then
      echo "generate-corpus-fixtures: generating $fixture (spec source: $source_desc) exited" \
           "$status — fix the error above, then re-run with --only $fixture" >&2
      exit "$status"
    fi
  fi
done
