#!/usr/bin/env python3
"""The one rate-limit guard every HTTP call this repository makes to GitHub,
to Postman or to Sourcegraph goes through.

This docstring is the single statement of the rule, the interface and the
scope of the guarantee; every document that mentions the rule links here
rather than carrying a copy.

The rule
--------
No call this repository's code makes may take any GitHub REST rate-limit
bucket past 70% of its limit. Before every call, ``acquire`` reads the bucket
live and admits the call only while ``(used + cost) / limit <= 0.70``;
otherwise it sleeps until the ``reset`` that refusing reading named, reads
again once it has passed, and repeats for as long as that takes. A bucket at
69 of 100 admits a call costing 1 and waits on a call costing 2.

Waiting is the intended behaviour, never a failure. A bucket reaching its cap
is never a reason to stop a search, to mark a key searched, to record a source
``unanswered``, or to conclude anything about the world. The rule is per
bucket, and a Postman or Sourcegraph throttle or refusal is a wait exactly as
a GitHub cap is.

What the 70% is a guarantee about
---------------------------------
The token is shared with everything else on this host. The guard bounds what
*this repository's* code spends on it and leaves the rest of every bucket as
headroom for callers it cannot see and does not control. It is not a claim
about the token's instantaneous total usage: an independent caller can spend
between any two of the guard's readings, and that headroom is the answer to
it.

Why GitHub REST only, and no GraphQL
------------------------------------
The rule needs limit, used and reset read freely and accurately before each
call, and only GitHub publishes them: ``GET /rate_limit`` reports every REST
bucket and GitHub documents it as not counting against any limit. So no
reading the guard takes spends anything, a bucket already at or above the cap
is still readable, and a fresh guard's first reading is safe whatever state
it finds the bucket in.

GraphQL has no such reading. Measured on this host's token on 2026-09-23 at
about 18:55 UTC: a GraphQL ``rateLimit`` query spent a point of the bucket it
reported (``cost: 1``, ``rateLimit(dryRun: true)`` included), while the free
``graphql`` block of REST ``/rate_limit`` reported ``used: 0`` against the
1,274-1,279 that GraphQL's own ``rateLimit`` field and the ``X-Ratelimit-Used``
header on a GraphQL POST reported. A guard covering GraphQL could not take
even its first reading without possibly spending past 70%, so this repository
makes no GitHub GraphQL call: code and repository search are
``/search/code`` and ``/search/repositories``, contents and trees are
``/repos/.../contents`` and ``/repos/.../git/trees``. ``acquire("graphql")``
raises ``UnsupportedBucket`` before reading, waiting or admitting, and
``record`` raises it for a response from the GraphQL endpoint.

Postman and Sourcegraph are paced, not percentage-guarded
---------------------------------------------------------
Postman (``POST https://www.postman.com/_api/ws/proxy``) and Sourcegraph's
public code search publish no quota figures, so this module claims none for
either: no limit, no used, no reset, no percentage. Each runs in a paced lane
of its own: a fixed minimum spacing between the guard's requests, ``429`` and
``Retry-After`` honoured, exponential backoff on repeated refusals, and never
a retry into a refusal. A wait on one lane never delays the other.

Interface
---------
``RateLimitGuard(host, *, evidence_dir=None)``
    ``host`` is ``"github"``, ``"postman"`` or ``"sourcegraph"``. Share one
    guard per host across a process's threads.
``guard.acquire(bucket, *, cost=1)``
    Call immediately before every call. For GitHub, ``cost`` is the units the
    call spends in ``bucket`` (1 for every call this repository makes).
    Admission is a reservation: a per-bucket lock is held across the live
    reading, the decision and the caller's call, and released by ``record``,
    so a second caller decides on a reading taken after the first's call.
    For a paced host ``bucket`` is the lane, named after the host, and
    ``acquire`` returns once the lane's spacing since the guard's last
    request has elapsed and any refusal backoff has expired.
``guard.record(response)``
    Call immediately after every call, with the response (an
    ``urllib.error.HTTPError`` is one) or, when the call produced none, the
    exception it raised. For GitHub it folds in the response's
    ``x-ratelimit-*`` headers for the log, closes the reservation and honours
    any ``Retry-After``; those figures never decide a later admission. A
    rate-limit refusal the live reading disagrees with is GitHub's secondary
    limiter: it opens an exponential backoff honouring ``Retry-After``, and
    after ``SECONDARY_ATTEMPT_BUDGET`` consecutive refusals ``SecondaryLimit``
    is raised, here and by every later ``acquire`` on that bucket. For a paced
    host it starts the lane's next interval, and a refusal opens the same
    backoff with the same budget.
``guard.waits()``
    Every wait the guard made, and every reading it took while waiting (as a
    ``probe``), as dicts. With ``evidence_dir`` each is also appended to
    ``rate-limit-waits.jsonl`` there as it happens; recorded calls go to
    ``rate-limit-calls.jsonl``. No record carries a credential.
``SecondaryLimit``
    Report the refused call and stop making it; never retry it tightly, and
    never treat it as a searched or answered source.
``UnsupportedBucket``
    A programming error: make the REST call instead.

The token is read from ``GITHUB_TOKEN`` (then ``GH_TOKEN``) and never
written anywhere. ``CROZIER_GITHUB_API_URL`` overrides the API root, which is
how the offline tests point the guard at a local server.

``python3 scripts/rate_limit_guard.py status`` (``just quota-status``) prints
each GitHub bucket's live figures from one free ``/rate_limit`` read and the
pacing in force for Postman and Sourcegraph. It never waits. It exits 0 after
printing, 1 when ``/rate_limit`` is unreadable or malformed, and 2 on a usage
error.
"""

from __future__ import annotations

import dataclasses
import datetime
import email.utils
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

CAP = 0.70
"""The share of any GitHub REST bucket this repository's calls may reach."""

GITHUB_API_URL = "https://api.github.com"

GITHUB_BUCKETS = frozenset({"core", "search", "code_search"})
"""The REST buckets this repository's calls spend in; ``graphql`` is deliberately absent.

A call that spends in any other bucket is caught by ``record``, which raises
``UnsupportedBucket`` when a response's ``x-ratelimit-resource`` names a bucket
other than the one acquired: add that bucket here, once a call needs it."""

RESET_MARGIN_S = 1.0
"""Slept past a bucket's reset before reading again, to absorb clock skew."""

SECONDARY_BACKOFF_BASE_S = 60.0
"""First secondary-limit backoff when no ``Retry-After`` asks for longer."""

SECONDARY_ATTEMPT_BUDGET = 5
"""Consecutive refusals of one bucket or lane before ``SecondaryLimit``."""


@dataclasses.dataclass(frozen=True)
class PacedLane:
    """The pacing discipline of a host that publishes no quota figures."""

    spacing_s: float
    backoff_base_s: float
    attempt_budget: int


PACED_LANES = {
    "postman": PacedLane(spacing_s=2.0, backoff_base_s=10.0, attempt_budget=5),
    "sourcegraph": PacedLane(spacing_s=2.0, backoff_base_s=10.0, attempt_budget=5),
}

REFUSAL_STATUSES = frozenset({429, 503})
"""Paced-host statuses that are a refusal to wait out, never a result."""

HOSTS = ("github", *PACED_LANES)

WAITS_FILE = "rate-limit-waits.jsonl"
CALLS_FILE = "rate-limit-calls.jsonl"


class UnsupportedBucket(ValueError):
    """A bucket the guard cannot read for free, ``graphql`` above all."""


class SecondaryLimit(RuntimeError):
    """Refusals persisted past the attempt budget: stop making this call.

    Named for GitHub's secondary limiter, and raised on the same terms when a
    paced lane exhausts its budget, because the contract handles a Postman or
    Sourcegraph refusal the way it handles a secondary one."""


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")


def _token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or None


def github_api_url() -> str:
    """The GitHub REST API root the guard reads and callers should call."""
    return os.environ.get("CROZIER_GITHUB_API_URL", GITHUB_API_URL).rstrip("/")


def read_rate_limit() -> dict[str, dict[str, int]]:
    """One free ``GET /rate_limit`` read: every REST bucket's figures."""
    request = urllib.request.Request(
        f"{github_api_url()}/rate_limit",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "crozier-rate-limit-guard",
        },
    )
    token = _token()
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        body = json.load(response)
    resources = body.get("resources") if isinstance(body, dict) else None
    if not isinstance(resources, dict):
        raise RuntimeError("GET /rate_limit returned no `resources` object")
    return resources


def _header(response: Any, name: str) -> str | None:
    headers = getattr(response, "headers", None)
    if headers is None:
        return None
    value = headers.get(name)
    return None if value is None else str(value)


def _status(response: Any) -> int | None:
    for attribute in ("status", "code", "status_code"):
        value = getattr(response, attribute, None)
        if isinstance(value, int):
            return value
    return None


def _url(response: Any) -> str:
    for attribute in ("url", "geturl"):
        value = getattr(response, attribute, None)
        if callable(value):
            value = value()
        if isinstance(value, str):
            return value
    return ""


def _retry_after(response: Any) -> float | None:
    value = _header(response, "Retry-After")
    if value is None:
        return None
    try:
        return max(float(value), 0.0)
    except ValueError:
        pass
    try:
        moment = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    return max(moment.timestamp() - time.time(), 0.0)


def _is_graphql(response: Any) -> bool:
    path = urllib.parse.urlsplit(_url(response)).path.rstrip("/")
    return path.endswith("/graphql") or _header(response, "x-ratelimit-resource") == "graphql"


@dataclasses.dataclass
class _Reservation:
    bucket: str
    cost: int
    reading: dict[str, int] | None
    lock: threading.Lock


@dataclasses.dataclass
class _Backoff:
    until: float = 0.0
    refusals: int = 0
    exhausted: bool = False
    last_request: float | None = None


class RateLimitGuard:
    """See the module docstring: it is the one statement of this contract."""

    def __init__(self, host: str, *, evidence_dir: str | os.PathLike[str] | None = None) -> None:
        if host not in HOSTS:
            raise ValueError(f"unknown host {host!r}: expected one of {', '.join(HOSTS)}")
        self.host = host
        self.evidence_dir = None if evidence_dir is None else Path(evidence_dir)
        if self.evidence_dir is not None:
            self.evidence_dir.mkdir(parents=True, exist_ok=True)
        self._locks: dict[str, threading.Lock] = {}
        self._state: dict[str, _Backoff] = {}
        self._pending: dict[int, _Reservation] = {}
        self._meta = threading.Lock()
        self._waits: list[dict[str, Any]] = []

    def acquire(self, bucket: str, *, cost: int = 1) -> None:
        """Block until ``bucket`` admits a call of ``cost``; see the module docstring."""
        bucket = self._covered(bucket)
        if cost < 1:
            raise ValueError(f"cost must be a positive integer, got {cost!r}")
        with self._meta:
            if threading.get_ident() in self._pending:
                raise RuntimeError("acquire called again before record closed this thread's reservation")
            lock = self._locks.setdefault(bucket, threading.Lock())
            state = self._state.setdefault(bucket, _Backoff())
        if state.exhausted:
            raise SecondaryLimit(self._exhausted_message(bucket))
        lock.acquire()
        try:
            if state.exhausted:
                raise SecondaryLimit(self._exhausted_message(bucket))
            if self.host == "github":
                self._wait_backoff(bucket, state)
                reading = self._admit(bucket, cost)
            else:
                self._wait_lane(bucket, state)
                reading = None
        except BaseException:
            lock.release()
            raise
        with self._meta:
            self._pending[threading.get_ident()] = _Reservation(bucket, cost, reading, lock)

    def record(self, response: Any) -> None:
        """Close this thread's reservation with the call's response; see the module docstring."""
        if self.host == "github" and _is_graphql(response):
            raise UnsupportedBucket(
                "a GitHub GraphQL response reached the guard: this repository makes no GraphQL "
                "call (see scripts/rate_limit_guard.py); make the REST call instead"
            )
        with self._meta:
            reservation = self._pending.pop(threading.get_ident(), None)
        if reservation is None:
            raise RuntimeError("record called without a matching acquire on this thread")
        try:
            if self.host == "github":
                exhausted = self._record_github(reservation, response)
            else:
                exhausted = self._record_lane(reservation, response)
        finally:
            reservation.lock.release()
        if exhausted:
            raise SecondaryLimit(self._exhausted_message(reservation.bucket))

    def waits(self) -> list[dict[str, Any]]:
        """Every wait made and every reading taken while waiting, oldest first."""
        with self._meta:
            return [dict(entry) for entry in self._waits]

    def _covered(self, bucket: str) -> str:
        if self.host == "github":
            if bucket not in GITHUB_BUCKETS:
                raise UnsupportedBucket(
                    f"the guard does not cover GitHub bucket {bucket!r}: it reads only the REST "
                    "buckets GET /rate_limit reports for free, and this repository makes no "
                    "GraphQL call — make the REST call instead"
                )
            return bucket
        if bucket != self.host:
            raise UnsupportedBucket(f"{self.host} has one paced lane, named {self.host!r}; got {bucket!r}")
        return self.host

    def _read(self, bucket: str) -> dict[str, int]:
        resources = read_rate_limit()
        figures = resources.get(bucket)
        if not isinstance(figures, dict) or not {"limit", "used", "reset"} <= figures.keys():
            raise UnsupportedBucket(f"GET /rate_limit reports no figures for bucket {bucket!r}")
        return {key: int(figures[key]) for key in ("limit", "used", "remaining", "reset") if key in figures}

    def _admit(self, bucket: str, cost: int) -> dict[str, int]:
        waiting = False
        while True:
            reading = self._read(bucket)
            limit = reading["limit"]
            admitted = limit > 0 and (reading["used"] + cost) / limit <= CAP
            if waiting or not admitted:
                self._log_wait(
                    {"host": "github", "bucket": bucket, "kind": "probe", "reading": reading,
                     "cost": cost, "admitted": admitted}
                )
            if admitted:
                return reading
            waiting = True
            duration = max(reading["reset"] - time.time(), 0.0) + RESET_MARGIN_S
            self._sleep(
                duration,
                {"host": "github", "bucket": bucket, "kind": "wait", "cause": "cap",
                 "reading": reading, "cost": cost},
            )

    def _wait_backoff(self, bucket: str, state: _Backoff) -> None:
        duration = state.until - time.time()
        if duration > 0:
            self._sleep(
                duration,
                {"host": "github", "bucket": bucket, "kind": "wait", "cause": "backoff",
                 "refusals": state.refusals},
            )

    def _record_github(self, reservation: _Reservation, response: Any) -> bool:
        bucket = reservation.bucket
        state = self._state[bucket]
        status = _status(response)
        retry_after = _retry_after(response)
        spent: dict[str, Any] = {
            "host": "github", "bucket": bucket, "at": _now_iso(), "status": status,
            "reserved": reservation.cost,
        }
        for key in ("limit", "used", "remaining", "reset", "resource"):
            value = _header(response, f"x-ratelimit-{key}")
            if value is not None:
                spent[key] = int(value) if value.isdigit() else value
        reading = reservation.reading or {}
        if isinstance(spent.get("used"), int) and "used" in reading and spent.get("reset") == reading.get("reset"):
            spent["cost"] = spent["used"] - reading["used"]
        self._log_call(spent)
        resource = spent.get("resource")
        if resource is not None and resource != bucket:
            raise UnsupportedBucket(
                f"a call acquired on {bucket!r} spent in {resource!r}: acquire the bucket the call "
                "spends in, adding it to GITHUB_BUCKETS if the guard does not cover it yet"
            )
        refused = status == 429 or (
            status == 403 and (retry_after is not None or _header(response, "x-ratelimit-remaining") == "0")
        )
        if not refused:
            state.refusals = 0
            if retry_after:
                state.until = max(state.until, time.time() + retry_after)
            return False
        live = self._read(bucket)
        primary = live["used"] >= live["limit"]
        self._log_wait(
            {"host": "github", "bucket": bucket, "kind": "probe", "reading": live,
             "classifying": "primary" if primary else "secondary", "status": status}
        )
        if primary:
            # The bucket really is spent (by another holder of the token): the
            # next acquire's live reading waits for its reset.
            if retry_after:
                state.until = max(state.until, time.time() + retry_after)
            return False
        return self._refused(state, retry_after, SECONDARY_BACKOFF_BASE_S, SECONDARY_ATTEMPT_BUDGET)

    def _wait_lane(self, lane: str, state: _Backoff) -> None:
        pacing = PACED_LANES[lane]
        now = time.time()
        if state.until > now:
            self._sleep(
                state.until - now,
                {"host": lane, "lane": lane, "kind": "wait", "cause": "backoff",
                 "refusals": state.refusals},
            )
        if state.last_request is not None:
            duration = state.last_request + pacing.spacing_s - time.time()
            if duration > 0:
                self._sleep(
                    duration,
                    {"host": lane, "lane": lane, "kind": "wait", "cause": "spacing",
                     "spacing_s": pacing.spacing_s},
                )

    def _record_lane(self, reservation: _Reservation, response: Any) -> bool:
        lane = reservation.bucket
        pacing = PACED_LANES[lane]
        state = self._state[lane]
        state.last_request = time.time()
        status = _status(response)
        retry_after = _retry_after(response)
        self._log_call({"host": lane, "lane": lane, "at": _now_iso(), "status": status})
        if status not in REFUSAL_STATUSES:
            state.refusals = 0
            if retry_after:
                state.until = max(state.until, time.time() + retry_after)
            return False
        return self._refused(state, retry_after, pacing.backoff_base_s, pacing.attempt_budget)

    def _refused(self, state: _Backoff, retry_after: float | None, base: float, budget: int) -> bool:
        state.refusals += 1
        backoff = max(retry_after or 0.0, base * 2 ** (state.refusals - 1))
        state.until = time.time() + backoff
        if state.refusals >= budget:
            state.exhausted = True
        return state.exhausted

    def _exhausted_message(self, bucket: str) -> str:
        return (
            f"{self.host} {bucket!r} refused {self._state[bucket].refusals} consecutive calls "
            "while its budget remained: report the refused call and stop making it — it is not "
            "a searched or answered source"
        )

    def _sleep(self, duration: float, entry: dict[str, Any]) -> None:
        started = time.monotonic()
        entry = {**entry, "started_at": _now_iso(), "planned_s": round(duration, 3)}
        time.sleep(duration)
        entry["duration_s"] = round(time.monotonic() - started, 3)
        self._log_wait(entry)

    def _log_wait(self, entry: dict[str, Any]) -> None:
        entry.setdefault("at", _now_iso())
        with self._meta:
            self._waits.append(entry)
            self._append(WAITS_FILE, entry)

    def _log_call(self, entry: dict[str, Any]) -> None:
        with self._meta:
            self._append(CALLS_FILE, entry)

    def _append(self, name: str, entry: dict[str, Any]) -> None:
        if self.evidence_dir is None:
            return
        with (self.evidence_dir / name).open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, sort_keys=True) + "\n")


def status() -> int:
    """Print every bucket's live figures from one free read; never wait."""
    try:
        resources = read_rate_limit()
    except (OSError, RuntimeError, ValueError) as error:
        print(f"quota-status: could not read {github_api_url()}/rate_limit: {error}", file=sys.stderr)
        print("quota-status: check network access, and set GITHUB_TOKEN to read the token's own buckets", file=sys.stderr)
        return 1
    lines = []
    for bucket in sorted(set(resources) - {"graphql"}):
        figures = resources[bucket]
        try:
            limit, used, reset = (int(figures[key]) for key in ("limit", "used", "reset"))
        except (KeyError, TypeError, ValueError):
            print(f"quota-status: GET /rate_limit reported malformed figures for {bucket!r}: {figures!r}", file=sys.stderr)
            print("quota-status: check CROZIER_GITHUB_API_URL points at the GitHub REST API", file=sys.stderr)
            return 1
        share = used / limit if limit else 0.0
        when = datetime.datetime.fromtimestamp(reset, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        guarded = "guarded" if bucket in GITHUB_BUCKETS else "not called here"
        over = "  OVER CAP" if share > CAP else ""
        lines.append(f"  {bucket:<28} limit {limit:>6}  used {used:>6}  {share:>6.1%}  reset {when}  {guarded}{over}")
    print(f"github ({'authenticated' if _token() else 'unauthenticated: set GITHUB_TOKEN'}; cap {CAP:.0%})")
    print("\n".join(lines))
    print("  graphql: not covered; this repository makes no GraphQL call")
    for lane, pacing in PACED_LANES.items():
        print(
            f"{lane}: no published quota; paced (1 request / {pacing.spacing_s:g}s, "
            f"backoff from {pacing.backoff_base_s:g}s doubling, "
            f"SecondaryLimit after {pacing.attempt_budget} refusals)"
        )
    return 0


def main(argv: list[str]) -> int:
    if argv != ["status"]:
        print("usage: rate_limit_guard.py status", file=sys.stderr)
        return 2
    return status()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
