#!/usr/bin/env bash
# Fetch (when needed) and generate Fern golden `expected/` trees for the issue #77
# corpus. Existing committed fixture specs are reused. URL-only rows are fetched
# into the ignored cache under .local/corpus and passed directly to Fern so source
# specs do not need to be vendored just to refresh generated output.
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)" && repo_root="$(cd "$script_dir/../.." && pwd)" || {
  echo "generate-corpus-fixtures: cannot resolve the checkout from $0 — run it by its path from a readable" \
       "checkout, then re-run" >&2
  exit 1
}
# shellcheck source=../corpus/corpus-lib.sh
. "$script_dir/../corpus/corpus-lib.sh" || {
  echo "generate-corpus-fixtures: cannot load $script_dir/../corpus/corpus-lib.sh — restore it with" \
       "git checkout -- tools/corpus/corpus-lib.sh, then re-run" >&2
  exit 1
}
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
               running Fern or writing fixture output. A row with no committed
               spec is still fetched into the --fetch-root cache: its spec is
               found by searching what was fetched.
  --fetch-root DIR
               Cache direct specs and source repositories under DIR (default .local/corpus).

Exit status: 0 when every selected row generated (or, with --dry-run, was
planned); 2 for an invalid invocation; the failing step's own status, or 1,
when a row cannot be read, fetched, discovered or generated.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --all) mode=all ;;
    --committed) mode=committed ;;
    --only) shift; [ -n "${1:-}" ] || { echo "generate-corpus-fixtures: --only needs a corpus name or fixture directory" >&2; usage; exit 2; }; only="$1" ;;
    --dry-run) dry_run=1 ;;
    --fetch-root) shift; [ -n "${1:-}" ] || { echo "generate-corpus-fixtures: --fetch-root needs a directory" >&2; usage; exit 2; }; fetch_root="$1" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "generate-corpus-fixtures: unknown argument '$1'" >&2; usage; exit 2 ;;
  esac
  shift
done

[ -f "$manifest" ] || {
  echo "generate-corpus-fixtures: missing $manifest — it is committed; restore it with" \
       "git checkout -- tests/fixtures/CORPUS.md, then re-run" >&2
  exit 1
}


# discover_openapi ROOT — the one OpenAPI document under ROOT: exit 1 when there
# is none, 2 when there are several, 3 when the search itself failed. Callers
# test it in an `||`, which turns off errexit inside, so each failure is
# returned explicitly rather than left to `set -e`.
discover_openapi() {
  local root="$1" candidates count
  candidates="$({
    find "$root" \
      \( -path '*/.git' -o -path '*/node_modules' -o -path '*/target' -o -path '*/dist' -o -path '*/build' -o -path '*/vendor' \) -prune \
      -o -type f \( -name '*.yml' -o -name '*.yaml' -o -name '*.json' \) -size -20M -print0 |
    while IFS= read -r -d '' f; do
      matched=0
      LC_ALL=C rg -q "(^|[\"'[:space:]])openapi([\"'[:space:]]*:|:)" "$f" || matched=$?
      case "$matched" in
        0) printf '%s\n' "$f" ;;
        1) ;;
        *) echo "generate-corpus-fixtures: could not read $f while looking for the OpenAPI document" \
                "(rg exit $matched)" >&2
           exit 3 ;;
      esac
    done
  })" || {
    echo "generate-corpus-fixtures: the search for the OpenAPI document under $root failed — make it" \
         "readable (or remove the unreadable file named above), then re-run" >&2
    return 3
  }
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
       "(restore it with git checkout -- tests/fixtures/CORPUS.md) or fix the row named" \
       "above, then re-run" >&2
  exit 1
}
# Two parallel lists, not one delimited string: a source path may hold any
# character, so none is free to split it on.
plan=()
plan_sources=()
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

  plan+=("$fixture")
  plan_sources+=("$source_desc")
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

# Each generation's output is kept, and shown only when it fails: one fixture
# reports the generator's own summary, a batch one line for all of them.
generated=()
log=""
if [ "$dry_run" -eq 0 ]; then
  log="$(mktemp "${TMPDIR:-/tmp}/generate-corpus-fixtures.XXXXXX")" || {
    echo "generate-corpus-fixtures: cannot create a temporary log under ${TMPDIR:-/tmp} — point" \
         "TMPDIR at a writable directory, then re-run" >&2
    exit 1
  }
  trap 'rm -f "$log" || echo "generate-corpus-fixtures: could not remove $log; delete it by hand" >&2' EXIT
fi
for index in "${!plan[@]}"; do
  fixture="${plan[$index]}"
  source_desc="${plan_sources[$index]}"
  if [ "$dry_run" -eq 1 ]; then
    # The plan is what --dry-run was asked for: one `fixture<TAB>source` row per
    # selected fixture on stdout, the data its caller reads, not progress chatter.
    printf '%s\t%s\n' "$fixture" "$source_desc"
  else
    status=0
    "$repo_root/tools/fern-goldens/generate-fern-fixture.sh" "$fixture" "${FERN_PYTHON_VERSION-}" "$source_desc" \
      >"$log" 2>&1 || status=$?
    if [ "$status" -ne 0 ]; then
      cat "$log" >&2 || echo "generate-corpus-fixtures: could not read the generator's log $log" >&2
      echo "generate-corpus-fixtures: generating $fixture (spec source: $source_desc) exited" \
           "$status — fix the error above, then re-run with --only $fixture" >&2
      exit "$status"
    fi
    generated+=("$fixture")
  fi
done
if [ "${#generated[@]}" -eq 1 ]; then
  tail -n 1 "$log" >&2 || {
    echo "generate-corpus-fixtures: generated ${generated[0]}, but could not read the generator's summary" \
         "from $log — review tests/fixtures/${generated[0]}/expected, then wire it into the e2e manifest" >&2
    exit 1
  }
elif [ "${#generated[@]}" -gt 1 ]; then
  echo "generate-corpus-fixtures: generated ${#generated[@]} fixtures (${generated[*]}) — review," \
       "then wire them into the e2e manifest (see docs/matching.md)" >&2
fi
