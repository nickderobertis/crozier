#!/usr/bin/env bash
# Install crozier for the GitHub Action (action.yml), and `ruff`, crozier's own
# generation-time dependency, when it is absent. Nothing here installs,
# configures or pins the reference tool: that is the calling workflow's.
#
# Reads VERSION (the action's `version` input), GITHUB_ACTION_PATH (the action's
# own checkout), RUNNER_TEMP and GITHUB_OUTPUT; writes `bin=<path to crozier>`.
#
#   VERSION=""       the release the action's own ref names: `v` + the
#                    `[package] version` of the action's own Cargo.toml. At a
#                    release tag that version IS the released one (release-plz
#                    is its only writer), so `@vX.Y.Z` installs vX.Y.Z and `@v0`
#                    the release `v0` points at. Unreadable, this fails rather
#                    than guess: falling back to `latest` would quietly unpin
#                    every caller relying on the default.
#   VERSION=latest   the newest release.
#   VERSION=local    build the action's own source with `cargo install`.
#   anything else    that exact release tag.
set -euo pipefail

# shellcheck source=tools/github-action/lib.sh
. "$(dirname "$0")/lib.sh"

[ -n "${GITHUB_ACTION_PATH:-}" ] || die "GITHUB_ACTION_PATH is not set" \
  "run this as a step of the crozier action, which GitHub Actions gives its own path"
[ -n "${RUNNER_TEMP:-}" ] || die "RUNNER_TEMP is not set" \
  "run this inside GitHub Actions, or set RUNNER_TEMP to a scratch directory"
[ -n "${GITHUB_OUTPUT:-}" ] || die "GITHUB_OUTPUT is not set" \
  "run this inside GitHub Actions, or set GITHUB_OUTPUT to a writable file"
case "${RUNNER_OS:-}" in
  Windows) die "the crozier action runs on Linux and macOS runners only" \
    "run the job on ubuntu-latest or macos-latest" ;;
esac

root="$RUNNER_TEMP/crozier-action"
mkdir -p "$root/bin" || die "could not create the install directory $root/bin" \
  "check that RUNNER_TEMP ($RUNNER_TEMP) is a writable directory on a disk with free space, then re-run"
installer="$GITHUB_ACTION_PATH/scripts/install.sh"
version="${VERSION:-}"

case "$version" in
  local)
    cargo install --path "$GITHUB_ACTION_PATH" --locked --root "$root" --quiet
    ;;
  latest)
    sh "$installer" --to "$root/bin"
    ;;
  "")
    manifest="$GITHUB_ACTION_PATH/Cargo.toml"
    own=""
    if [ -r "$manifest" ]; then
      own="$(awk '
        /^\[/ { section = $0 }
        section == "[package]" && /^version[ \t]*=/ {
          # The whole assignment, or nothing: a line TOML would reject names
          # no version.
          if ($0 ~ /^version[ \t]*=[ \t]*"[^"]*"[ \t]*(#.*)?$/) {
            sub(/^version[ \t]*=[ \t]*"/, ""); sub(/".*$/, ""); print
          }
          exit
        }' "$manifest" || true)"
    fi
    # Held to the X.Y.Z shape a release tag has before it names one.
    if ! [[ "$own" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
      echo "::error::cannot read the release this action's ref names from the [package] version in $manifest; set the version input (a tag such as v0.1.0, latest, or local)" >&2
      exit 1
    fi
    sh "$installer" --to "$root/bin" --version "v$own"
    ;;
  *)
    sh "$installer" --to "$root/bin" --version "$version"
    ;;
esac

bin="$root/bin/crozier"
[ -x "$bin" ] || die "no crozier binary at $bin after installing '${version:-the action ref}'" \
  "check the install output above; set the version input to a published tag"

if ! command -v ruff >/dev/null 2>&1; then
  bash "$GITHUB_ACTION_PATH/scripts/install-ruff.sh"
fi

echo "bin=$bin" >>"$GITHUB_OUTPUT" || die "could not write the bin output to GITHUB_OUTPUT ($GITHUB_OUTPUT)" \
  "check that GITHUB_OUTPUT names a writable file (GitHub Actions sets it for each step), then re-run"
