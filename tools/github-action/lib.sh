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

# The report contract (assets/compare-report.schema.json, in the Action's own
# checkout): the one statement of the enums and nullability checked below.
REPORT_SCHEMA="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/assets/compare-report.schema.json"

# `report_is_whole FILE`: FILE is a `crozier compare` report carrying every
# field the Action reads, typed as the schema types it — statuses, exit codes
# and layouts read off the schema's own enums, each timing figure null only
# where the schema allows null — so no count, figure or path reaches an output
# or the summary unchecked.
report_is_whole() {
  jq -e --slurpfile schema "$REPORT_SCHEMA" '
    $schema[0] as $s
    | ($s["$defs"].Status.oneOf | map(.const)) as $statuses
    | ($s.properties.exit_code.enum) as $exits
    | ($s["$defs"].ComparedLayout.oneOf | map(.const)) as $layouts
    | def count: type == "number" and . >= 0 and . == floor;
      def figure($definition): if . == null then ($definition.type | type == "array" and index("null") != null)
                               else type == "number" end;
      def figures($definitions): . as $value
        | all($definitions | to_entries[] | select(.value.format == "double");
              (.value) as $definition | $value[.key] | figure($definition));
      def paths: type == "array" and all(.[]; type == "string");
    (.schema_version == 1 or .schema_version == 2)
    and (.exit_code as $code | $exits | index($code) != null)
    and (.counts | type == "object"
         and (.matched | count) and (.mismatched | count) and (.could_not_check | count))
    and (.timing_totals | type == "object" and (.generators_timed | count)
         and figures($s["$defs"].TimingTotals.properties))
    and (.results | type == "array" and all(.[];
      type == "object"
      and (.status as $status | $statuses | index($status) != null)
      and (.config_file | type == "string")
      and (.generator | . == null or type == "string")
      and (.reason | . == null or type == "string")
      and (.reference | . == null or (type == "object" and (.command | type == "string")))
      and (.timing | . == null or (type == "object"
           and figures($s["$defs"].GeneratorResult.properties.timing.properties)))
      and (.comparison | . == null or (type == "object"
           and (.files_compared | count) and (.layout as $layout | $layouts | index($layout) != null)
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
