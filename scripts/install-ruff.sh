#!/usr/bin/env bash
# Install `ruff`, pinned to the version in `.ruff-version` (the single source of
# truth). crozier defers Python line wrapping to `ruff format` (see src/pyfmt.rs),
# so `ruff` is a generation-time dependency the e2e and every `crozier generate`
# need. Idempotent and quiet on success: an existing `ruff` on PATH is left as-is
# (any recent version formats crozier's shapes identically).
#
# ruff ships as a Python package, not a cargo crate, so it comes from PyPI. This
# is the one place that installs it — `just bootstrap` and the release verify
# jobs both call it rather than re-implementing the install.
set -euo pipefail

command -v ruff >/dev/null 2>&1 && exit 0

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
version="$(cat "$repo_root/.ruff-version")"
echo "install-ruff: installing ruff==$version" >&2

if command -v pipx >/dev/null 2>&1; then
  pipx install "ruff==$version"
elif command -v uv >/dev/null 2>&1; then
  uv tool install "ruff==$version"
else
  python3 -m pip install --user "ruff==$version"
fi

# These installers drop the `ruff` shim in ~/.local/bin, which a fresh CI runner
# does not always have on PATH; expose it to subsequent GitHub Actions steps.
if [ -n "${GITHUB_PATH:-}" ]; then
  printf '%s\n' "$HOME/.local/bin" >>"$GITHUB_PATH"
fi
