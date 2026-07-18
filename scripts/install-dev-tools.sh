#!/usr/bin/env bash
# Install the cargo subcommands the gate needs, if missing. Idempotent and quiet
# on success. Prefers prebuilt binaries (cargo-binstall) over source builds.
#
# In CI these come from taiki-e/install-action (see .github/workflows/ci.yml);
# this script is the clean-clone local path invoked by `just bootstrap`. `ruff`
# (the other generation-time dependency) is installed by scripts/install-ruff.sh,
# which `just bootstrap` calls alongside this.
set -euo pipefail

tools=(cargo-nextest cargo-llvm-cov cargo-deny cargo-machete sccache)

missing=()
for t in "${tools[@]}"; do
  if [ "$t" = "sccache" ]; then
    command -v sccache >/dev/null 2>&1 || missing+=("$t")
  else
    sub="${t#cargo-}"
    cargo "$sub" --version >/dev/null 2>&1 || missing+=("$t")
  fi
done

if [ "${#missing[@]}" -eq 0 ]; then
  exit 0
fi

echo "install-dev-tools: installing ${missing[*]}" >&2
if command -v cargo-binstall >/dev/null 2>&1; then
  cargo binstall --no-confirm --locked "${missing[@]}"
else
  echo "install-dev-tools: cargo-binstall not found; building from source (slow)." \
       "Install it for faster setup: https://github.com/cargo-bins/cargo-binstall" >&2
  cargo install --locked "${missing[@]}"
fi
