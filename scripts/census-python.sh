#!/usr/bin/env bash
# Print the Python interpreter the census tooling must run under, or fail saying
# why there is none. `just surface-census` and `just test-surface-census` both
# call this instead of spelling `python3`, so neither can silently borrow another
# project's environment. Given arguments, it runs them under that interpreter
# instead (`sh scripts/census-python.sh SCRIPT ARGS...`): the form an Nx target
# can spell on every OS, since Windows runs a target's command under cmd.exe.
#
# Why this exists: a bare `python3` is whatever PATH happens to offer first, and
# an activated virtualenv from an unrelated checkout wins that race. The census
# scripts are stdlib-only, so a foreign interpreter does not fail — it produces a
# clean, wrong-provenance answer, and the census is an instrument whose whole
# value is that its numbers are about *this* repository. A missing environment
# has to be an error, not a fall-through.
#
# crozier is a Rust project: it has no committed virtualenv and needs none. So
# the interpreter it wants is a plain system Python 3, and a repo-local `.venv`
# is honoured only if someone has deliberately made one here.
# Started as `sh` (a POSIX shell, or bash in POSIX mode — macOS's /bin/sh), the
# selection below needs bash proper.
if [ -z "${BASH_VERSION:-}" ]; then exec bash "$0" "$@"; fi
case ":${SHELLOPTS:-}:" in *:posix:*) exec bash "$0" "$@" ;; esac
set -euo pipefail

found() { # found INTERPRETER [ARGS...]: print it, or run ARGS under it
  local interpreter="$1"
  shift
  if [ "$#" -gt 0 ]; then exec "$interpreter" "$@"; fi
  printf '%s\n' "$interpreter"
  exit 0
}

script_dir="${0%/*}"
[ "$script_dir" != "$0" ] || script_dir=.
repo_root="$(cd "$script_dir/.." && pwd)"

for local_python in \
  "$repo_root/.venv/bin/python3" \
  "$repo_root/.venv/Scripts/python.exe"
do
  if [ -x "$local_python" ]; then
    found "$local_python" "$@"
  fi
done

# Ask each candidate whether it is a virtualenv, rather than guessing from its
# path: `sys.prefix` parting from `sys.base_prefix` is what a virtualenv IS.
foreign=""
while IFS= read -r candidate; do
  [ -x "$candidate" ] || continue
  prefix="$("$candidate" -c 'import sys; print(sys.prefix)' 2>/dev/null)" || continue
  base="$("$candidate" -c 'import sys; print(sys.base_prefix)' 2>/dev/null)" || continue
  if [ "$prefix" = "$base" ]; then
    found "$candidate" "$@"
  fi
  [ -n "$foreign" ] || foreign="$candidate"
done < <(type -a -p python3 2>/dev/null || true)

if [ -n "$foreign" ]; then
  echo "census-python: the only python3 on PATH is another project's virtualenv" >&2
  echo "  $foreign" >&2
  echo "census-python: run outside that virtualenv (deactivate), or create one here" >&2
  echo "  python3 -m venv $repo_root/.venv" >&2
  exit 1
fi

echo "census-python: no python3 on PATH — the census tooling needs Python 3" >&2
exit 1
