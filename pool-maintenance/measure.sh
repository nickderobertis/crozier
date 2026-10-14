#!/usr/bin/env bash
# The `crozier-pool-maintenance-seconds` budget's command (budgets.yaml): time one
# steady-state `just pool-maintenance` pass, the one a regular post-run
# maintenance faces, never a first pass over accumulated history.
#
#   (a) run the declared maintenance once, untimed, to clear any backlog;
#   (b) build the test targets under an alternative profile that gives this
#       repository's own crates new metadata hashes, then backdate exactly the
#       entries that build created past the 2-day window (to 2000-01-01, older
#       than any build the backlog pass kept, so none of them is a unit's
#       newest) — a run's builds that have since been superseded;
#   (c) run the ordinary build, so each unit's newest build is the ordinary one;
#   (d) time one declared pass, which removes the alternative builds.
#
# The figure is (d)'s, as the pruner reports it to ONEBUDGETSPEC_RESULT; (a)'s own
# report is appended to the detail as separate evidence. The script fails, with
# the entries named, if (d) removes anything (b) did not create or removes nothing.
# With POOL_MAINTENANCE_EVIDENCE naming a directory, the entry lists it compared
# (before-alt, alt, before-pass, after-pass, removed) are copied there.
# It really prunes this checkout and builds it twice: run it only in a clone you own.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
scratch="$(mktemp -d)"
finish() {
  if [ -n "${POOL_MAINTENANCE_EVIDENCE:-}" ]; then
    mkdir -p "$POOL_MAINTENANCE_EVIDENCE"
    cp "$scratch"/before-alt "$scratch"/alt "$scratch"/before-pass "$scratch"/after-pass "$scratch"/removed \
      "$POOL_MAINTENANCE_EVIDENCE"/ 2>/dev/null || true
  fi
  rm -rf "$scratch"
}
trap finish EXIT

die() {
  printf 'measure: %s\n' "$1" >&2
  exit 1
}

read -r -a targets <<<"$(just --evaluate pool_maintenance_targets)"

# Every top-level entry of every profile directory's build containers: what the
# pruner groups into builds, one unit and metadata hash per name.
entries() {
  local target profile container entry
  for target in "${targets[@]}"; do
    [ -d "$target" ] || continue
    find "$target" -type d -name .fingerprint -print | while IFS= read -r profile; do
      profile="${profile%/.fingerprint}"
      for container in deps .fingerprint build incremental; do
        for entry in "$profile/$container"/*; do
          [ -e "$entry" ] || [ -L "$entry" ] || continue
          printf '%s\n' "$entry"
        done
      done
    done
  done | LC_ALL=C sort
}

# The gate's test build: every workspace member's test targets.
build() {
  cargo test --workspace --no-run --locked --quiet "$@" >"$scratch/build.log" 2>&1 || {
    cat "$scratch/build.log" >&2
    die "the test build failed (above); fix it, then rerun"
  }
}

# (a) The backlog, cleared untimed; its own report kept as evidence.
ONEBUDGETSPEC_RESULT="$scratch/backlog.json" just pool-maintenance >&2

# (b) Overflow checks off for the workspace members only (`"*"` restores them for
# every dependency), so only this repository's own crates get new hashes.
entries >"$scratch/before-alt"
build --config 'profile.dev.overflow-checks=false' --config 'profile.dev.package."*".overflow-checks=true'
entries >"$scratch/after-alt"
LC_ALL=C comm -13 "$scratch/before-alt" "$scratch/after-alt" >"$scratch/alt"
[ -s "$scratch/alt" ] || die "the alternative build created no new entries, so there is nothing superseded to time"
while IFS= read -r entry; do
  find "$entry" -exec touch -h -t 200001010000 {} +
done <"$scratch/alt"

# (c) The ordinary build: each unit's newest.
build

# (d) The timed pass.
entries >"$scratch/before-pass"
just pool-maintenance >&2
entries >"$scratch/after-pass"
LC_ALL=C comm -23 "$scratch/before-pass" "$scratch/after-pass" >"$scratch/removed"
LC_ALL=C comm -23 "$scratch/removed" "$scratch/alt" >"$scratch/unexpected"
if [ -s "$scratch/unexpected" ]; then
  cat "$scratch/unexpected" >&2
  die "the timed pass removed the entries above, which the alternative build did not create"
fi
[ -s "$scratch/removed" ] || die "the timed pass removed none of the alternative build's entries"
kept="$(LC_ALL=C comm -23 "$scratch/before-pass" "$scratch/alt" | wc -l | tr -d ' ')"
printf 'measure: removed %s of the alternative build'"'"'s %s entries; all %s other entries kept\n' \
  "$(wc -l <"$scratch/removed" | tr -d ' ')" "$(wc -l <"$scratch/alt" | tr -d ' ')" "$kept" >&2

# The backlog pass's report, appended to the timed pass's detail.
if [ -n "${ONEBUDGETSPEC_RESULT:-}" ] && [ -f "$ONEBUDGETSPEC_RESULT" ]; then
  python3 -I - "$ONEBUDGETSPEC_RESULT" "$scratch/backlog.json" <<'PY'
import json
import sys

result_path, backlog_path = sys.argv[1:]
with open(result_path, encoding="utf-8") as f:
    result = json.load(f)
with open(backlog_path, encoding="utf-8") as f:
    backlog = json.load(f)
result["detail"] = (
    f"{result.get('detail', '')}; untimed backlog pass, not in the figure: "
    f"{backlog['value']} seconds ({backlog.get('detail', '')})"
)
with open(result_path, "w", encoding="utf-8") as f:
    json.dump(result, f)
PY
fi
