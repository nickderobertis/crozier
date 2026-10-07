# shellcheck shell=bash
# Shared by the GitHub Action's scripts (sourced, never run): the failure shape
# and the colour rule their log lines follow.
#
# The colour rule is `crozier compare`'s own (docs/compare.md#colour), so a
# result line the Action prints and the CLI's report beside it in the same log
# agree on when colour is on. The scripts print to stderr, as the CLI does.
#
# A GitHub Actions log is not a terminal, so without help neither would print
# colour there: the Action sets CLICOLOR_FORCE=1 for its scripts and the CLI
# they run, and a NO_COLOR the workflow sets still wins.
export CLICOLOR_FORCE=1

die() {
  printf 'crozier-action: %s\n' "$1" >&2
  printf 'ACTION: %s\n' "$2" >&2
  exit 1
}

# `is_exit_status VALUE`: VALUE is a canonical process exit status, 0-255 with no
# leading zero. Bash truncates a larger `exit` modulo 256 (so 256 would pass) and
# jq's --argjson refuses a leading zero, so both checks are needed.
is_exit_status() {
  [[ "$1" =~ ^(0|[1-9][0-9]{0,2})$ ]] && [ "$1" -le 255 ]
}

# `report_is_whole FILE`: FILE is a `crozier compare` report carrying every
# field the Action reads, typed as assets/compare-report.schema.json types it,
# so no count, figure or path reaches an output or the summary unchecked.
report_is_whole() {
  jq -e '
    def count: type == "number" and . >= 0 and . == floor;
    def seconds: . == null or type == "number";
    def paths: type == "array" and all(.[]; type == "string");
    (.schema_version == 1 or .schema_version == 2)
    and (.exit_code | type == "number" and . == floor and . >= 0 and . <= 255)
    and (.counts | type == "object"
         and (.matched | count) and (.mismatched | count) and (.could_not_check | count))
    and (.timing_totals | type == "object" and (.generators_timed | count)
         and all(.reference_seconds, .crozier_seconds, .speedup, .saved_seconds; seconds))
    and (.results | type == "array" and all(.[];
      type == "object"
      and (.status | . == "matched" or . == "mismatched" or . == "could_not_check")
      and (.config_file | type == "string")
      and (.generator | . == null or type == "string")
      and (.reason | . == null or type == "string")
      and (.reference | . == null or (type == "object" and (.command | type == "string")))
      and (.timing | . == null or (type == "object"
           and all(.reference_seconds, .crozier_seconds, .speedup, .saved_seconds; seconds)))
      and (.comparison | . == null or (type == "object"
           and (.files_compared | count) and (.layout | type == "string")
           and all(.differing, .only_in_reference, .only_in_crozier; paths)))))
  ' "$1" >/dev/null 2>&1
}

color_enabled() {
  if [ -n "${NO_COLOR:-}" ]; then
    return 1
  fi
  if [ -n "${CLICOLOR_FORCE:-}" ] && [ "$CLICOLOR_FORCE" != 0 ]; then
    return 0
  fi
  [ -t 2 ]
}

# `paint green|red|yellow TEXT`: TEXT in that colour, or plain when colour is off.
paint() {
  local code
  case "$1" in
    green) code=32 ;;
    red) code=31 ;;
    yellow) code=33 ;;
    *) die "unknown colour '$1'" "use green, red or yellow" ;;
  esac
  if color_enabled; then
    printf '\033[%sm%s\033[0m' "$code" "$2"
  else
    printf '%s' "$2"
  fi
}
