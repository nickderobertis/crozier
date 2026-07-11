#!/usr/bin/env bash
# Idempotent setup for the GENERATED fixture path (scripts/generate-fern-fixture.sh):
# make Fern runnable end-to-end from a spec. Each step runs ONLY when its target is
# not already available, so re-running is cheap and running where things already
# exist is a no-op.
#
# Wired into the Claude Code SessionStart hook (.claude/settings.json) so web/cloud
# sessions can regenerate a fixture's golden tree with no manual steps; also safe to
# run by hand (`just setup-fern`). Every step tolerates failure and the script always
# exits 0 — a flaky install must never break session startup; the generate script
# still gates each prerequisite with an actionable error when the time comes.
#
# The OFFLINE path (`just fixtures-refresh`, `just fixtures-candidates`) needs NONE
# of this and is unaffected whether this succeeds or not.
#
# What it does, and why — each guarded by "is it already here?":
#   1. fern CLI — Fern's orchestrator (installed from npm; the pinned *generator
#      image* in generate-fern-fixture.sh, not this CLI version, controls output).
#   2. Docker daemon — Fern runs its Python generator as a local container, so a
#      runtime must be reachable. Started only if nothing answers and we are root.
#   3. Release binary — the comment stripper (`crozier internal-strip`) the pipeline
#      pipes every generated .py through; built only if absent.
# The web container's filesystem is cached after the hook completes, so the npm
# global install and the compiled target/ persist — only the first session pays.
#
# llmlint: ignore-file[robust_shell, tool_output_is_signal, cli_output_contract]
# deliberate for a session-startup installer, matching scripts/setup-llmlint.sh:
# `set -e` is omitted and the script ALWAYS exits 0 on purpose — a non-zero exit
# would fail the SessionStart hook and block the whole session over an optional,
# best-effort setup. Failure is not hidden: it is surfaced on stderr (log-and-
# continue) and re-gated by generate-fern-fixture.sh's actionable prerequisite
# checks when a fixture is actually generated. So exit 0 here is "nothing to block
# startup for", not "everything succeeded".
set -uo pipefail

# Run asynchronously: the SessionStart hook reads this directive off stdout's first
# line and lets the rest run in the background, so a cold `cargo build --release`
# never delays session startup. The tradeoff is a race — work that needs a
# generated fixture right at startup may arrive before this finishes; the generate
# script gates each prerequisite with an actionable error if so. asyncTimeout is
# generous enough for a cold release build. Nothing else writes stdout (log() and
# the installers below go to stderr), so this stays the sole stdout line.
echo '{"async": true, "asyncTimeout": 900000}'

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

log() { printf 'setup-fern: %s\n' "$*" >&2; }

# 1. fern CLI (needs npm; lands on PATH under the node prefix, no PATH persist).
ensure_fern() {
  if command -v fern >/dev/null 2>&1; then
    log "fern present ($(fern --version 2>/dev/null | head -1)) — skipping"
  elif command -v npm >/dev/null 2>&1; then
    log "installing fern CLI (npm i -g fern-api)"
    npm i -g fern-api >&2 2>&1 && log "fern installed" \
      || log "fern install failed; run 'npm i -g fern-api' by hand (continuing)"
  else
    log "npm not found; cannot install fern — generated fixtures unavailable (continuing)"
  fi
}

# 2. Docker daemon. Reachable already → nothing to do. Otherwise start dockerd, but
#    only as root (a non-root or local session leaves the daemon to the host).
ensure_docker() {
  if docker info >/dev/null 2>&1; then
    log "docker daemon reachable — skipping"
    return 0
  fi
  if ! command -v dockerd >/dev/null 2>&1 || [ "$(id -u)" != "0" ]; then
    log "no reachable docker daemon and cannot start one — generated fixtures unavailable (continuing)"
    return 0
  fi
  # A dockerd may already be starting (socket not up yet) — wait for it rather than
  # spawning a second. Otherwise clear a stale pidfile a prior daemon left on an
  # unclean exit (dockerd refuses to start while one exists) and launch fresh.
  if pgrep -x dockerd >/dev/null 2>&1; then
    log "docker daemon already starting — waiting"
  else
    rm -f /var/run/docker.pid
    log "starting docker daemon"
    nohup dockerd >/tmp/dockerd.log 2>&1 &
  fi
  # Bounded wait for the socket; never hang the session on a daemon that won't come up.
  for _ in $(seq 1 20); do
    docker info >/dev/null 2>&1 && break
    sleep 1
  done
  docker info >/dev/null 2>&1 && log "docker daemon up" \
    || log "docker daemon did not start (see /tmp/dockerd.log) (continuing)"
}

# 3. Release binary — only if absent (the cached container keeps the built target/).
ensure_release_binary() {
  if [ -x "$repo_root/target/release/crozier" ]; then
    log "release binary present — skipping build"
  elif command -v cargo >/dev/null 2>&1; then
    log "building release binary (cargo build --release)"
    ( cd "$repo_root" && cargo build --release >&2 2>&1 ) && log "release binary built" \
      || log "release build failed; run 'cargo build --release' (continuing)"
  else
    log "cargo not found; cannot build release binary (continuing)"
  fi
}

ensure_fern
ensure_docker
ensure_release_binary
log "done (the offline fixture path needs none of this; see tests/fixtures/AGENTS.md)"
exit 0
