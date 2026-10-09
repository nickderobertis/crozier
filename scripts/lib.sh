#!/usr/bin/env bash
# Shared helpers for the fixture scripts. Source it, don't execute it:
#   . "$(cd "$(dirname "$0")" && pwd)/lib.sh"

# Succeeds iff NAME is a single safe path segment — no slashes, no `..`, no leading
# `.`/`-`, not empty — the same invariant crozier enforces on --package-name. The
# fixture scripts splice the name into paths they later `rm -rf`, so this rejects
# traversal and option injection. One source so the callers can't drift apart.
valid_fixture_name() {
  case "${1:-}" in
    "" | *[!A-Za-z0-9._-]* | [.-]* | *..*) return 1 ;;
    *) return 0 ;;
  esac
}

# Fern generator image tags are exact semantic versions. Keeping this strict
# prevents a version argument from becoming YAML syntax in generators.yml and
# ensures provenance never records a floating tag such as `latest`.
valid_fern_version() {
  [[ "${1:-}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z]+([.-][0-9A-Za-z]+)*)?$ ]]
}

# report_failures TOOL ACTION — under `set -e`, a command that fails unhandled
# ends the script with only its own words (`mkdir: Permission denied`). From
# here on, such a failure also prints the line, the command and the action that
# recovers. A failure the script handles (`if !`, `||`) never reaches the trap.
report_failures() {
  _failure_tool="$1"
  _failure_action="$2"
  arm_failure_report
}

# arm_failure_report — the trap alone, for a child shell that inherits the
# exported `_failure_tool`/`_failure_action` (an `xargs` worker, say).
arm_failure_report() {
  set -o errtrace
  trap '_report_failure "$?" "$LINENO" "$BASH_COMMAND"' ERR
}

_report_failure() {
  printf "%s: line %s: '%s' failed (exit %s) — %s\n" \
    "$_failure_tool" "$2" "$3" "$1" "$_failure_action" >&2
}
