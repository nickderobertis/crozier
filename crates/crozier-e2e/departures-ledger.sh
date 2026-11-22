#!/usr/bin/env bash
# Regenerate the per-golden departure ledger, tests/fixtures/departures-ledger.tsv,
# and the inventory of example values Fern writes that their own schema rejects,
# docs/departures/evidence/invalid-example-values/inventory.tsv: run the golden
# comparisons with CROZIER_RECORD_DEPARTURES and CROZIER_RECORD_EXAMPLE_INVENTORY
# set, so each records the departures the engine applies and the rejected values
# it finds instead of holding them to the committed files, then merge the records
# (`write_departures_ledger`, `write_example_values_inventory`). Run it (`just
# departures-ledger`, the crozier-e2e project's target, which builds crozier
# first) after a change that adds, moves or removes a departure, and review the
# diff before committing; see docs/departures/README.md. CROZIER_REQUIRE_CORPUS
# makes a missing committed source fail rather than skip, so no golden's rows
# are lost.
#
# Only the tests tests/fixtures/departures-contributors.tsv lists run, and the
# run must record exactly the goldens it lists for them before anything merges
# (`verify_departure_contributors`). Optional arguments:
#   GOLDEN...                 record only these goldens (closed over every test
#                             recording them); every other golden keeps its rows
#   --rename OLD=NEW          a golden tree moved unchanged: verify its bytes and
#                             source document against HEAD, then rename it in the
#                             committed ledgers before recording (repeatable)
#   --discover-contributors   run the whole suite, as before the inventory
#                             existed, and rederive the inventory from it
# With no arguments the recipe passes them in CROZIER_DEPARTURES_LEDGER_ARGS.
set -euo pipefail

fail() { echo "departures-ledger: $1" >&2; echo "departures-ledger: $2" >&2; exit 1; }
usage="usage: crates/crozier-e2e/departures-ledger.sh [--discover-contributors] [--rename OLD=NEW]... [GOLDEN]..."

cd "$(dirname "$0")/../.." || fail "cannot enter the repository root above $0" "run it from a readable checkout"

if [ "$#" -eq 0 ] && [ -n "${CROZIER_DEPARTURES_LEDGER_ARGS:-}" ]; then
  read -ra forwarded <<< "$CROZIER_DEPARTURES_LEDGER_ARGS"
  set -- "${forwarded[@]}"
fi
goldens=() renames=() discover=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --discover-contributors) discover=1 ;;
    --rename) [ "$#" -ge 2 ] || fail "--rename needs OLD=NEW" "$usage"; renames+=("$2"); shift ;;
    --rename=*) renames+=("${1#--rename=}") ;;
    -*) fail "unknown option '$1'" "$usage" ;;
    *) goldens+=("$1") ;;
  esac
  shift
done
[ "$discover" = 0 ] || [ "${#goldens[@]}" -eq 0 ] \
  || fail "--discover-contributors runs the whole suite, so it takes no GOLDEN" "$usage"

contributors=tests/fixtures/departures-contributors.tsv
same_blob() { # same_blob COMMITTED-PATH WORKTREE-PATH: the file holds exactly the bytes HEAD has there
  local committed actual
  committed=$(git rev-parse "HEAD:$1") || fail "cannot read $1 at HEAD" "check the repository is readable"
  actual=$(git hash-object "$2") || fail "cannot hash $2" "check it is readable"
  [ "$committed" = "$actual" ]
}
for pair in ${renames[@]+"${renames[@]}"}; do
  old=${pair%%=*} new=${pair#*=}
  [ "$pair" != "$old" ] && [ -n "$old" ] && [ -n "$new" ] || fail "--rename '$pair' is not OLD=NEW" "$usage"
  for path in "$old" "$new"; do
    case "/$path/" in
      //*|*/../*|*/./*|*//*) fail "--rename '$pair': $path is no repository-relative golden path" "$usage" ;;
    esac
  done
  [ "$(git cat-file -t "HEAD:$old" 2>/dev/null)" = tree ] \
    || fail "$old is no golden tree at HEAD" "name the committed path the tree moved from"
  [ ! -e "$old" ] || fail "$old still exists, so it was copied, not moved" "remove it, or regenerate without --rename"
  [ -d "$new" ] || fail "$new is not a directory" "move the tree there first"
  committed=$(git ls-tree -r --name-only "HEAD:$old" | LC_ALL=C sort) || fail "cannot list $old at HEAD" "check the repository is readable"
  moved=$(cd "$new" && find . -type f | sed 's|^\./||' | LC_ALL=C sort) || fail "cannot list $new" "check it is readable"
  [ "$committed" = "$moved" ] || fail "$new does not hold exactly the files of $old at HEAD" \
    "a rename keeps every file; regenerate a changed golden without --rename"
  while IFS= read -r file; do
    same_blob "$old/$file" "$new/$file" || fail "$new/$file differs from $old/$file at HEAD" \
      "a rename keeps every byte; regenerate a changed golden without --rename"
  done <<< "$committed"
  for document in openapi.yml openapi.yaml openapi.json; do
    source="$(dirname "$old")/$document"
    git cat-file -e "HEAD:$source" 2>/dev/null || continue
    if ! [ -f "$(dirname "$new")/$document" ] || ! same_blob "$source" "$(dirname "$new")/$document"; then
      fail "$(dirname "$new")/$document is not $source at HEAD" "move the golden's source document with it, unchanged"
    fi
  done
done

scratch=$(mktemp -d "${TMPDIR:-/tmp}/crozier-departures.XXXXXX") \
  || fail "cannot create a temporary directory under ${TMPDIR:-/tmp}" "point TMPDIR at a writable directory and rerun"
trap 'rm -rf "$scratch" || echo "departures-ledger: could not remove $scratch; delete it by hand" >&2' EXIT
records="$scratch/records" inventory="$scratch/inventory" noted="$scratch/contributors" log="$scratch/log"
mkdir "$records" "$inventory" "$noted" || fail "cannot create $records, $inventory and $noted" "point TMPDIR at a writable directory and rerun"

if [ "${#renames[@]}" -gt 0 ] && ! CROZIER_RENAME_GOLDENS="${renames[*]:-}" cargo nextest run --locked -p crozier-e2e --run-ignored only \
  -E 'test(=departure_contributors::rename_departure_goldens)' >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "the rename was refused (above)" "fix the named rename, then rerun just departures-ledger"
fi

if [ "$discover" = 1 ]; then
  # The ledger gate's own scratch tests expect ledger failures, and the
  # contributor tests read the inventory this run derives, so neither is run.
  filter='not test(/^(departures_ledger_gate|departure_contributors)::/)'
else
  [ -f "$contributors" ] || fail "$contributors is missing" "derive it with just departures-ledger --discover-contributors"
  # The tests recording the selected goldens (every listed one with none),
  # closed over the other goldens those tests record.
  filter=$(awk -F'\t' -v selected="${goldens[*]:-}" '
    # The inventory becomes a nextest filter, so every cell is checked first:
    # its header, three non-empty cells, and ids nextest names tests by.
    NR == 1 { if ($0 != "golden\tbinary\ttest") { print "invalid " NR ": its header is not golden/binary/test"; bad = 1; exit } next }
    NF != 3 || $1 == "" || $2 !~ /^[A-Za-z0-9_:.-]+$/ || $3 !~ /^[A-Za-z0-9_:.-]+$/ {
      print "invalid " NR ": `" $0 "` is not golden, binary id and test name"; bad = 1; exit
    }
    { golden[NR] = $1; test[NR] = $2 "\t" $3; listed[$1] = 1 }
    END {
      if (bad) exit
      n = split(selected, wanted, " ")
      for (i = 1; i <= n; i++) {
        if (!(wanted[i] in listed)) { print "unknown " wanted[i]; exit }
        mark[wanted[i]] = 1
      }
      do {
        changed = 0
        for (r in golden) if ((n == 0 || (golden[r] in mark)) && !(test[r] in run)) { run[test[r]] = 1; changed = 1 }
        for (r in golden) if ((test[r] in run) && !(golden[r] in mark)) { mark[golden[r]] = 1; changed = 1 }
      } while (changed)
      for (t in run) { split(t, id, "\t"); print "binary_id(=" id[1] ") & test(=" id[2] ")" }
    }' "$contributors" | LC_ALL=C sort) || fail "cannot read $contributors" "restore it with git checkout -- $contributors"
  case "$filter" in
    invalid\ *) fail "$contributors line ${filter#invalid }" \
      "rederive it with just departures-ledger --discover-contributors, or restore it with git checkout -- $contributors" ;;
    unknown\ *) fail "$contributors names no test recording ${filter#unknown }" \
      "name a golden of tests/fixtures/compared-goldens.json, or rederive it with just departures-ledger --discover-contributors" ;;
    "") fail "$contributors lists no test" "derive it with just departures-ledger --discover-contributors" ;;
  esac
  filter=$(paste -sd'|' - <<< "$filter") \
    || fail "cannot join the selected tests into one nextest filter" "check that paste(1) is installed, then rerun"
fi

# The comparisons record against the committed inventory of compared goldens
# (tests/fixtures/compared-goldens.json), so a stale one is refused before
# anything records: a golden added or narrowed since would otherwise record
# under the old inventory and fail only at the gate.
inventory_test='departures_ledger_gate::compared_goldens_inventory_is_current'
inventory_regenerate="CROZIER_UPDATE_COMPARED_GOLDENS=1 cargo nextest run --locked -p crozier-e2e -E 'binary(e2e) & test(=$inventory_test)'"
if ! cargo nextest run --locked -p crozier-e2e -E "binary(e2e) & test(=$inventory_test)" >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "tests/fixtures/compared-goldens.json is not the inventory the registered comparisons derive (above), so nothing was recorded" \
    "regenerate it from the repository root with $inventory_regenerate, then rerun just departures-ledger"
fi

# llmlint: ignore[changed_behavior_has_e2e] the recording run is proven twice: departure_contributors::the_recipe_runs_only_the_selected_goldens_contributors drives the real recipe and nextest over a two-golden selection (ignored: it runs Nx and nextest from inside a nextest run and rewrites the committed ledger, so it is run by name), and crates/crozier-e2e/tests/e2e/report_scripts.rs drives the failure paths a real run cannot induce with only `cargo` stood in.
if ! CROZIER_REQUIRE_CORPUS=1 CROZIER_RECORD_DEPARTURES="$records" CROZIER_RECORD_EXAMPLE_INVENTORY="$inventory" CROZIER_RECORD_CONTRIBUTORS="$noted" cargo nextest run --locked -p crozier-e2e -p crozier-nested-discriminator-tests \
  --no-fail-fast -E "$filter" >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "a comparison failed while recording (above)" "fix it, then rerun just departures-ledger"
fi
if ! CROZIER_RECORD_DEPARTURES="$records" CROZIER_RECORD_EXAMPLE_INVENTORY="$inventory" CROZIER_RECORD_CONTRIBUTORS="$noted" \
  CROZIER_LEDGER_SELECTION="${goldens[*]:-}" CROZIER_DISCOVER_CONTRIBUTORS="$discover" cargo nextest run --locked -p crozier-e2e --run-ignored only \
  -E 'test(=departure_contributors::verify_departure_contributors)' >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "the recording run does not match $contributors (above)" "follow the named fix, then rerun just departures-ledger"
fi
if ! CROZIER_RECORD_DEPARTURES="$records" CROZIER_RECORD_EXAMPLE_INVENTORY="$inventory" cargo nextest run --locked -p crozier-e2e --run-ignored only \
  -E 'test(=departures_ledger_gate::write_departures_ledger) | test(=example_values_inventory::write_example_values_inventory)' >"$log" 2>&1; then
  cat "$log" >&2 || echo "departures-ledger: could not read the run log $log" >&2
  fail "the merged ledger or inventory was refused (above)" "fix the cause, then rerun just departures-ledger"
fi
ledger=tests/fixtures/departures-ledger.tsv
inventory_file=docs/departures/evidence/invalid-example-values/inventory.tsv
rows=$(wc -l < "$ledger") || fail "cannot read $ledger after writing it" "restore it with git checkout -- $ledger and rerun"
values=$(wc -l < "$inventory_file") || fail "cannot read $inventory_file after writing it" "restore it with git checkout -- $inventory_file and rerun"
echo "departures-ledger: wrote $ledger ($((rows - 1)) rows) and $inventory_file ($((values - 1)) rows)"
