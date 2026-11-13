#!/usr/bin/env python3
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

A batch that returns no verdict (llmlint's exit 2: the judge errored or could
not be reached) is retried on the same tree, twice, after
`LLMLINT_DIFF_RETRY_DELAY` seconds (default 30) and then twice that. Only the
unanswered batch is re-sent: an answered one is never replayed, and a rule
failure (exit 1) is a verdict, so it is never retried.

Exit status: 1 when any batch's rule failed, since a rejection stands whatever
else happened; otherwise 2 when a batch still has no verdict after its retries,
announced by a `verification unavailable` line naming no rule; otherwise 0. Any
other nonzero status, a batch killed by a signal included, is read as 2: a
batch that returned no verdict never passes the run. A run it cannot make at
all (no llmlint, an invalid budget, a git or config failure) exits 2 as well,
never 1, which only a failed rule earns.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import NoReturn

# The largest judged input measured to come back with a verdict was 3.8 MB (a
# 22-file code batch); an 8 MB one never did. The default leaves headroom below
# the first.
DEFAULT_BUDGET = 3_000_000

# A judge outage seen in CI lasted minutes, not seconds; two retries, the second
# after twice the first delay, bound the wait at three times it.
RETRIES = 2
DEFAULT_RETRY_DELAY = 30.0


def fail(message: str) -> NoReturn:
    """Stop with exit 2, the status a judge error takes: the run could not be made,
    which is never the same answer as a rule failing (exit 1)."""
    print(f"llmlint-diff: {message}", file=sys.stderr)
    raise SystemExit(2)


def git(*args: str) -> str:
    run = subprocess.run(["git", *args], capture_output=True, text=True)
    if run.returncode != 0:
        fail(
            f"`git {' '.join(args)}` exited {run.returncode}: {run.stderr.strip()} — "
            "fetch the base (`git fetch origin main`) and run from inside the checkout"
        )
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


def excludes(llmlint: str) -> list[re.Pattern[str]]:
    """llmlint's own effective `files.exclude`, read from `llmlint config`."""
    run = subprocess.run([llmlint, "config"], capture_output=True, text=True)
    if run.returncode != 0:
        fail(
            f"`llmlint config` exited {run.returncode}: {run.stderr.strip()[-400:]} — "
            "fix llmlint.yml (`just lint-llm-validate`) and retry"
        )
    try:
        globs = json.loads(run.stdout)["config"]["files"]["exclude"]
    except (ValueError, KeyError, TypeError) as error:
        fail(
            f"`llmlint config` printed no `config.files.exclude` list ({error!r}); "
            "check the installed llmlint with `just setup-llmlint`"
        )
    if not isinstance(globs, list) or not all(isinstance(g, str) for g in globs):
        fail("`llmlint config`'s `config.files.exclude` is not a list of globs; check the installed llmlint")
    return [glob_regex(g) for g in globs]


def changed(base: str, llmlint: str) -> dict[str, int]:
    """Each changed, still-present file against the merge base, with what the judge reads of it."""
    merge_base = git("merge-base", base, "HEAD").strip()
    skip = excludes(llmlint)
    sizes: dict[str, int] = {}
    # NUL-delimited: git quotes a name holding a space, a quote or a non-ASCII
    # byte in its line-per-path form, which no such file is literally called.
    for path in git("diff", "--name-only", "-z", "--diff-filter=d", merge_base).split("\0"):
        if not path or any(pattern.match(path) for pattern in skip) or not Path(path).is_file():
            continue
        diff = subprocess.run(["git", "diff", merge_base, "--", path], capture_output=True)
        if diff.returncode != 0:
            fail(
                f"`git diff {merge_base} -- {path}` exited {diff.returncode}: "
                f"{diff.stderr.decode(errors='replace').strip()} — run from inside the checkout, then retry"
            )
        sizes[path] = Path(path).stat().st_size + len(diff.stdout)
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


def retry_delay() -> float:
    """Seconds before the first retry of an unanswered batch, from `LLMLINT_DIFF_RETRY_DELAY`."""
    raw = os.environ.get("LLMLINT_DIFF_RETRY_DELAY", "")
    if not raw:
        return DEFAULT_RETRY_DELAY
    try:
        delay = float(raw)
    except ValueError:
        delay = -1.0
    if not 0 <= delay <= 600:
        fail(f"LLMLINT_DIFF_RETRY_DELAY must be a number of seconds from 0 to 600, not {raw!r}")
    return delay


def judge(command: list[str], label: str, delay: float) -> int:
    """One batch's status, re-sending it while the judge gives no verdict, up to `RETRIES` times."""
    status = severity(subprocess.run(command).returncode)
    for attempt in range(1, RETRIES + 1):
        if status != 2:
            break
        wait = delay * attempt
        print(
            f"llmlint-diff: {label}: no verdict from the judge; retry {attempt}/{RETRIES} "
            f"on the same tree in {wait:g}s",
            flush=True,
        )
        time.sleep(wait)
        status = severity(subprocess.run(command).returncode)
    return status


def verdict(statuses: list[int]) -> int:
    """The run's status: a failed rule over an unanswered batch over a pass."""
    unanswered = statuses.count(2)
    if unanswered:
        print(
            f"llmlint-diff: verification unavailable: {unanswered} of {len(statuses)} batch(es) got no "
            f"verdict after {RETRIES} retries, so the judge never decided them; re-run the judged lint "
            "on this head once the judge answers",
            file=sys.stderr,
            flush=True,
        )
    if 1 in statuses:
        return 1
    return 2 if unanswered else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("base", nargs="?", default="origin/main")
    parser.add_argument(
        "--budget", type=int, default=DEFAULT_BUDGET, help="bytes of file plus diff one judge batch may receive"
    )
    args, extra = parser.parse_known_args(argv)
    if args.budget <= 0:
        fail(f"--budget must be a positive byte count, not {args.budget}")
    # The resolved path, not the bare name: on Windows an installed CLI is a
    # `.cmd` shim, which `which` finds through PATHEXT and a process spawn does not.
    llmlint = shutil.which("llmlint")
    if llmlint is None:
        fail("llmlint is not on PATH — run `just setup-llmlint`")
    delay = retry_delay()
    command = [llmlint, "--diff", "git", "--diff-base", args.base, *extra]
    sizes = changed(args.base, llmlint)
    if sum(sizes.values()) <= args.budget:
        return verdict([judge(command, "the diff", delay)])
    groups = batches(sizes, args.budget)
    statuses = []
    for number, group in enumerate(groups, start=1):
        size = sum(sizes[path] for path in group)
        label = f"batch {number}/{len(groups)}"
        print(f"llmlint-diff: {label}: {len(group)} file(s), {size:,} bytes", flush=True)
        statuses.append(judge([*command, *group], label, delay))
    return verdict(statuses)


if __name__ == "__main__":
    sys.exit(main())
