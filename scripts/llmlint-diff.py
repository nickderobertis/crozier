#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace; this wrapper sits in scripts/ beside the other llmlint tooling and is the `lint-llm-diff` recipe's body.
"""Judge a branch's diff with llmlint, in batches the judge can hold.

`llmlint --diff` hands one rule batch every changed file it targets, whole and
with its diff. It batches by rule and never by file, so a branch whose changed
files outgrow the judge's input gets back no parseable verdict at all ("no JSON
value could be extracted from the response"), however clean the change is.

So this wrapper measures what the judge would receive: each changed file's size
plus the size of its diff against the merge base, for every file llmlint.yml
does not exclude. When that fits `--budget` bytes, it runs the one invocation
the recipe always ran. When it does not, it splits the files, in path order so
neighbouring files stay together, into batches under the budget. It runs
`llmlint --diff` on each with the files named and fails if any batch fails.
A file larger than the budget on its own is a batch of one.

Exit status is the worst batch's: 2 (a judge errored) over 1 (a rule failed)
over 0. Any other nonzero status, a batch killed by a signal included, is read
as 2: a batch that returned no verdict fails the run, never passes it.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# The largest judged input measured to come back with a verdict was 3.8 MB (a
# 22-file code batch); an 8 MB one never did. The default leaves headroom below
# the first.
DEFAULT_BUDGET = 3_000_000


def fail(message: str) -> None:
    raise SystemExit(f"llmlint-diff: {message}")


def git(*args: str) -> str:
    run = subprocess.run(["git", *args], capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"`git {' '.join(args)}` exited {run.returncode}: {run.stderr.strip()} — "
             "fetch the base (`git fetch origin main`) and run from inside the checkout")
    return run.stdout


def glob_regex(pattern: str) -> re.Pattern[str]:
    """A cwd-rooted gitignore-style glob (`**`, `*`, `?`) as a whole-path regex."""
    out, index = "", 0
    while index < len(pattern):
        if pattern.startswith("**/", index):
            out, index = out + "(?:.*/)?", index + 3
        elif pattern.startswith("**", index):
            out, index = out + ".*", index + 2
        elif pattern[index] == "*":
            out, index = out + "[^/]*", index + 1
        elif pattern[index] == "?":
            out, index = out + "[^/]", index + 1
        else:
            out, index = out + re.escape(pattern[index]), index + 1
    return re.compile(out + r"\Z")


def excludes() -> list[re.Pattern[str]]:
    """llmlint's own effective `files.exclude`, read from `llmlint config`."""
    run = subprocess.run(["llmlint", "config"], capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"`llmlint config` exited {run.returncode}: {run.stderr.strip()[-400:]} — "
             "fix llmlint.yml (`just lint-llm-validate`) and retry")
    try:
        globs = json.loads(run.stdout)["config"]["files"]["exclude"]
    except (ValueError, KeyError, TypeError) as error:
        fail(f"`llmlint config` printed no `config.files.exclude` list ({error!r}); "
             "check the installed llmlint with `just setup-llmlint`")
    if not isinstance(globs, list) or not all(isinstance(g, str) for g in globs):
        fail("`llmlint config`'s `config.files.exclude` is not a list of globs; check the installed llmlint")
    return [glob_regex(g) for g in globs]


def changed(base: str) -> dict[str, int]:
    """Each changed, still-present file against the merge base, with what the judge reads of it."""
    merge_base = git("merge-base", base, "HEAD").strip()
    skip = excludes()
    sizes: dict[str, int] = {}
    for path in git("diff", "--name-only", "--diff-filter=d", merge_base).splitlines():
        if not path or any(pattern.match(path) for pattern in skip) or not Path(path).is_file():
            continue
        diff = subprocess.run(["git", "diff", merge_base, "--", path], capture_output=True).stdout
        sizes[path] = Path(path).stat().st_size + len(diff)
    return sizes


def batches(sizes: dict[str, int], budget: int) -> list[list[str]]:
    """Files in path order, cut into runs whose summed size stays under `budget`."""
    out: list[list[str]] = []
    current: list[str] = []
    total = 0
    for path in sorted(sizes):
        if current and total + sizes[path] > budget:
            out.append(current)
            current, total = [], 0
        current.append(path)
        total += sizes[path]
    if current:
        out.append(current)
    return out


def severity(code: int) -> int:
    """A batch's status on llmlint's 0/1/2 scale; anything else is an error."""
    return code if code in (0, 1, 2) else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("base", nargs="?", default="origin/main")
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET,
                        help="bytes of file plus diff one judge batch may receive")
    args, extra = parser.parse_known_args(argv)
    if args.budget <= 0:
        fail(f"--budget must be a positive byte count, not {args.budget}")
    if shutil.which("llmlint") is None:
        fail("llmlint is not on PATH — run `just setup-llmlint`")
    command = ["llmlint", "--diff", "git", "--diff-base", args.base, *extra]
    sizes = changed(args.base)
    if sum(sizes.values()) <= args.budget:
        return severity(subprocess.run(command).returncode)
    groups = batches(sizes, args.budget)
    worst = 0
    for number, group in enumerate(groups, start=1):
        size = sum(sizes[path] for path in group)
        print(f"llmlint-diff: batch {number}/{len(groups)}: {len(group)} file(s), {size:,} bytes", flush=True)
        code = subprocess.run([*command, *group]).returncode
        worst = max(worst, severity(code))
    return worst


if __name__ == "__main__":
    sys.exit(main())
