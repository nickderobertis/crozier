#!/usr/bin/env bash
# Render a `crozier compare` JSON report (assets/compare-report.schema.json) as
# the Markdown step summary the GitHub Action writes, on stdout.
#
# Every figure comes from the report; nothing is measured here. Markdown cannot
# colour text, so the marks beside each status are the summary's signal:
# ✅ matched, ❌ mismatched, ⚠️ could not check.
#
# Reads REPORT (the report's path) and EXIT_CODE (the CLI's exit status, which
# differs from the report's `exit_code` only when the command itself failed).
set -euo pipefail

# shellcheck source=tools/github-action/lib.sh
. "$(dirname "$0")/lib.sh"

exit_code="${EXIT_CODE:-}"
is_exit_status "$exit_code" || die "EXIT_CODE '$exit_code' is not an exit status (0-255, no leading zero)" \
  "pass the status crozier compare exited with"

if [ -z "${REPORT:-}" ] || ! jq -e '.schema_version == 1 or .schema_version == 2' "$REPORT" >/dev/null 2>&1; then
  # Exit 1 before any reference ran (a path that does not exist, an unwritable
  # --json target) leaves no report; anything else without one is a broken run.
  printf '## crozier compare\n\n'
  printf '❌ **crozier compare failed (exit %s) before writing a report.** See the step log for its error.\n' "$exit_code"
  exit 0
fi

jq -r --argjson cli_exit "$exit_code" '
  def fixed2:
    (. * 100 | round) as $c
    | ($c | if . < 0 then -. else . end) as $a
    | (if $c < 0 then "-" else "" end)
      + (($a / 100 | floor) | tostring) + "."
      + (($a % 100) | tostring | if length < 2 then "0" + . else . end);
  def secs: if . == null then "—" else (fixed2 + " s") end;
  def times: if . == null then "—" else (fixed2 + "×") end;
  # Text from the report is data: escaped for HTML, and kept on one table row.
  def esc: gsub("&"; "&amp;") | gsub("<"; "&lt;") | gsub(">"; "&gt;")
    | gsub("\\|"; "&#124;") | gsub("\r?\n"; "<br>");
  def code: "<code>" + (. | esc) + "</code>";
  def mark:
    if . == "matched" then "✅ matched"
    elif . == "mismatched" then "❌ mismatched"
    else "⚠️ could not check" end;
  def paths($label; $list):
    if ($list | length) == 0 then empty
    else $label + ": " + ([$list[] | code] | join(", ")) end;
  def details:
    if .status == "matched" then
      "\(.comparison.files_compared) file(s) compared, layout <code>\(.comparison.layout)</code>"
    elif .status == "mismatched" and .comparison != null then
      ([.comparison.differing[], .comparison.only_in_reference[], .comparison.only_in_crozier[]] | length) as $n
      | ([.comparison.differing[:20][], .comparison.only_in_reference[:20][], .comparison.only_in_crozier[:20][]] | length) as $shown
      | [paths("differ"; .comparison.differing[:20]),
         paths("only in reference"; .comparison.only_in_reference[:20]),
         paths("only in crozier"; .comparison.only_in_crozier[:20])]
      | join("<br>")
      + (if $n > $shown then "<br>(\($n - $shown) more; see the diff artifact)" else "" end)
    else (.reason // "no reason given" | esc) end;

  .counts as $c
  | .timing_totals as $t
  | "## crozier compare",
    "",
    (if .exit_code == 3 then "❌ **\($c.mismatched) generator(s) mismatched the reference.**"
     elif .exit_code == 4 then "⚠️ **No mismatch, but \($c.could_not_check) generator(s) could not be checked.**"
     elif ($c.matched + $c.mismatched + $c.could_not_check) == 0 then "✅ **Nothing to check:** no crozier config was found."
     else "✅ **Every checked generator matched.**" end),
    (if $cli_exit != .exit_code then
       "", "❌ **crozier compare exited \($cli_exit)**, not \(.exit_code): see the step log for its error."
     else empty end),
    "",
    "| ✅ Matched | ❌ Mismatched | ⚠️ Could not check |",
    "| ---: | ---: | ---: |",
    "| \($c.matched) | \($c.mismatched) | \($c.could_not_check) |",
    (if (.results | length) == 0 then empty else
      "",
      "| Status | Config | Generator | Reference command | Details | Reference time | crozier time | Speed-up | Time saved |",
      "| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
      (.results[]
        | "| \(.status | mark) | \(.config_file | code) | \(if .generator == null then "—" else (.generator | code) end) | \(if .reference == null then "—" else (.reference.command | code) end) | \(details) | \(.timing.reference_seconds | secs) | \(.timing.crozier_seconds | secs) | \(.timing.speedup | times) | \(.timing.saved_seconds | secs) |"),
      "| **Total** (\($t.generators_timed) generator(s) where both sides ran) | | | | | **\($t.reference_seconds | secs)** | **\($t.crozier_seconds | secs)** | **\($t.speedup | times)** | **\($t.saved_seconds | secs)** |"
    end),
    "",
    "_Reference time_ is the wall time of that generator'"'"'s one reference-command invocation; a first invocation may include one-time costs such as an image pull. _crozier time_ is its generation only. _Speed-up_ is reference ÷ crozier and _time saved_ is reference − crozier; the totals sum the generators where both sides ran."
' "$REPORT"
