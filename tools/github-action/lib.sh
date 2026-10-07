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
