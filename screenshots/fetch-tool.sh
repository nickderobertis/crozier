#!/usr/bin/env bash
# fetch-tool.sh URL OUT: download one pinned tool archive for the visual-docs capture,
# recovering a transient transfer failure. The capture's container runs it for each tool.
#
# A failure curl reports as transient (name or connection failure, a partial or reset
# transfer, a timeout, a TLS handshake, an empty reply, or an HTTP 408, 429 or 5xx answer)
# is retried after FETCH_TOOL_DELAY seconds (default 2), then twice and three times that,
# for at most FETCH_TOOL_ATTEMPTS attempts (default 4). Anything else, a 404 for a version
# that was never released included, fails at once. Either way it fails naming the URL and
# curl's last error, and OUT is written only by a complete download.
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "fetch-tool: usage: screenshots/fetch-tool.sh URL OUT" >&2
  exit 2
fi
url=$1
out=$2
case $url in
  https://* | http://*) ;;
  *)
    echo "fetch-tool: '$url' is not an http(s) URL; pass the pinned release's https:// address" >&2
    exit 2
    ;;
esac
if [ -d "$out" ]; then
  echo "fetch-tool: $out is a directory, so the archive from $url cannot be written there; remove it or name a file, then re-run" >&2
  exit 2
fi
# A whole number from MIN to MAX, read as decimal whatever its leading zeros.
bounded() {
  local name=$1 value=$2 min=$3 max=$4
  case $value in
    "" | *[!0-9]*)
      echo "fetch-tool: $name must be a whole number from $min to $max, not '$value'; set it within that range, or unset it for the default" >&2
      exit 2
      ;;
  esac
  # Leading zeros off as text, so a long or zero-padded value never reaches arithmetic.
  value=${value#"${value%%[!0]*}"}
  value=${value:-0}
  if [ "${#value}" -gt 3 ] || [ "$value" -lt "$min" ] || [ "$value" -gt "$max" ]; then
    echo "fetch-tool: $name must be a whole number from $min to $max, not '$2'; set it within that range, or unset it for the default" >&2
    exit 2
  fi
  echo "$value"
}
attempts=$(bounded FETCH_TOOL_ATTEMPTS "${FETCH_TOOL_ATTEMPTS:-4}" 1 10)
delay=$(bounded FETCH_TOOL_DELAY "${FETCH_TOOL_DELAY:-2}" 0 60)

attempt=0
retried=""
while :; do
  attempt=$((attempt + 1))
  status=0
  error=$(curl -fsSL --connect-timeout 30 -o "$out.part" --url "$url" 2>&1) || status=$?
  if [ "$status" -eq 0 ]; then
    if ! mv -f "$out.part" "$out"; then
      echo "fetch-tool: downloaded $url but could not move it to $out; check that its directory is writable, then re-run" >&2
      exit 1
    fi
    [ -z "$retried" ] || echo "fetch-tool: $url: downloaded on attempt $attempt after transient failures ($retried)" >&2
    exit 0
  fi
  if ! rm -f "$out.part"; then
    echo "fetch-tool: could not remove the partial download $out.part (curl exit $status: $error); remove it, then re-run" >&2
    exit 1
  fi
  transient=false
  case $status in
    5 | 6 | 7 | 16 | 18 | 28 | 35 | 52 | 55 | 56 | 92) transient=true ;;
    22) case $error in *"error: 408"* | *"error: 429"* | *"error: 5"[0-9][0-9]*) transient=true ;; esac ;;
  esac
  if [ "$transient" != true ] || [ "$attempt" -ge "$attempts" ]; then
    break
  fi
  wait=$((delay * attempt))
  retried="${retried:+$retried; }attempt $attempt/$attempts: curl exit $status, then ${wait}s"
  sleep "$wait"
done
echo "fetch-tool: could not download $url after $attempt attempt(s): curl exit $status: $error${retried:+ (earlier: $retried)} — check the pinned version file and the network, then re-run" >&2
exit 1
