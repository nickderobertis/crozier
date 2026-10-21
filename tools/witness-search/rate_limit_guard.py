#!/usr/bin/env python3
"""The one rate-limit guard every HTTP call this repository makes to GitHub,
to Postman or to Sourcegraph goes through.

This docstring is the single statement of the rule, the interface and the
scope of the guarantee; every document that mentions the rule links here
rather than carrying a copy.

The rule
--------
No call this repository's code makes may leave any GitHub REST rate-limit
bucket with less than 40% of its limit remaining, unless that bucket's reset
arrives before its remaining quota would run out. Before every call,
``acquire`` reads the bucket live and admits the call while
``(limit - used - cost) / limit >= 0.40``. A bucket at 59 used of 100 admits a
call costing 1 (exactly 40 remain after it) and refuses one costing 2.

Below that floor the burn-rate exception decides. The guard keeps every
bucket's readings within the current window (one ``reset``): the first and the
latest give the burn rate, ``(used_latest - used_first) / elapsed``, the units
spent per second by every holder of the token. The call is admitted below the
floor when ``remaining_after / rate`` exceeds the seconds until ``reset``, so the
window resets before the quota left after the call would be spent at the rate
measured. The rate needs two readings in the window over a positive elapsed
time; with one reading there is no rate and the call waits. A measured rate of
zero (or a ``used`` that fell) means nothing is burning, so the quota never runs
out and the call is admitted. No call is ever admitted that would take
``remaining`` below zero, exception or not. A call admitted by the exception is
logged as a ``probe`` with ``"admitted_by": "burn-rate"`` and, under ``burn``,
the rate and seconds to reset it decided on (with the projected seconds to
exhaustion when the rate is positive).

Otherwise the guard waits: it sleeps until the ``reset`` the refusing reading
named, reads again once it has passed, and repeats for as long as that takes.

Waiting is the intended behaviour, never a failure. A bucket reaching its
floor is never a reason to stop a search, to mark a key searched, to record a
source ``unanswered``, or to conclude anything about the world. The rule is
per bucket, and a Postman or Sourcegraph throttle or refusal is a wait exactly
as a GitHub floor is.

What the 40% floor is a guarantee about
---------------------------------------
The token is shared with everything else on this host. The floor bounds what
*this repository's* code spends on it and leaves at least 40% of every bucket
as headroom for callers it cannot see and does not control, except where the
measured burn shows the window resetting before that headroom would be needed.
It is not a claim about the token's instantaneous total usage: an independent
caller can spend between any two of the guard's readings, and that headroom is
the answer to it. The burn-rate projection is likewise a projection from the
guard's own readings, never a promise about callers it cannot see.

Why GitHub REST only, and no GraphQL
------------------------------------
The rule needs limit, used and reset read freely and accurately before each
call, and only GitHub publishes them: ``GET /rate_limit`` reports every REST
bucket and GitHub documents it as not counting against any limit. So no
reading the guard takes spends anything, a bucket already at or below the floor
is still readable, and a fresh guard's first reading is safe whatever state
it finds the bucket in.

GraphQL has no such reading. Measured on this host's token on 2026-09-23 at
about 18:55 UTC: a GraphQL ``rateLimit`` query spent a point of the bucket it
reported (``cost: 1``, ``rateLimit(dryRun: true)`` included), while the free
``graphql`` block of REST ``/rate_limit`` reported ``used: 0`` against the
1,274-1,279 that GraphQL's own ``rateLimit`` field and the ``X-Ratelimit-Used``
header on a GraphQL POST reported. A guard covering GraphQL could not take
even its first reading without possibly spending below its floor, so this repository
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
``cache_lookup(method, url, headers)`` / ``cache_store(...)``
    The one shared GitHub response cache; see below.

The shared GitHub response cache
--------------------------------
Every GitHub response a witness search, acquisition, screen or refusal fetch
receives (the REST API, the exact-commit raw lane on raw.githubusercontent.com,
and the tree downloads of ``witness-acquire-github.py``) is stored once, in one
cache on the host, outside every worktree:
``${XDG_CACHE_HOME:-$HOME/.cache}/crozier/github-responses/`` (an
``XDG_CACHE_HOME`` that is not absolute is ignored, as the XDG spec asks).
Each caller consults it *before* ``acquire`` or any pacing, so a later request
for a key already stored, from any node or worktree, is answered from the
cache: no call, no reading, no wait, no quota spent. Callers log such a hit to
``github-cache-hits.jsonl`` in their evidence directory, never to the call
ledgers, which count only calls made.

The key is the SHA-256 of a canonical JSON of the request: its method, its
full URL, and the request headers that change the answer (``CACHE_KEY_HEADERS``:
``Accept``, ``X-GitHub-Api-Version``, ``Range``). ``Authorization`` is never part
of the key and the token is never stored. Each entry is two files under
``<key[:2]>/``: ``<key>.<sha256>.body`` (the response body's bytes, named by
their own digest) and ``<key>.json`` (the status, the response headers callers
read, the body's size and SHA-256). Both are written to a temporary file and
published with ``os.replace``, body first, so a reader in another process sees
a whole entry or none. A body file is never overwritten with other bytes, and
one already holding its bytes is left in place, so
a hit's headers and body stay one answer while another writer stores a
different one for the same key; an entry whose body does not match its
recorded digest is a miss.

Only answers are stored. A rate-limit refusal (``429``, or a ``403`` carrying
``Retry-After``, ``x-ratelimit-remaining: 0`` or a rate-limit message), a
server-side or transient failure (any ``5xx``, ``408``), an authentication
failure (``401``, ``407``) and a transport error with no response are not
answers about the world, so none is stored or served. Entries never expire:
delete the directory to have every request asked again.

``CROZIER_GITHUB_CACHE_DIR`` overrides the cache root; the offline tests set it
to a temporary directory so they never write the host's cache. Without it, a
request to a loopback server (the offline tier standing in for GitHub) bypasses
the cache entirely.

The token is read from ``GITHUB_TOKEN`` (then ``GH_TOKEN``) and never
written anywhere. ``CROZIER_GITHUB_API_URL`` overrides the API root, which is
how the offline tests point the guard at a local server; it must name
``https://api.github.com`` or a loopback HTTP server, so the credential never
leaves for another host or crosses the network in clear.

``python3 tools/witness-search/rate_limit_guard.py status`` (``just quota-status``) prints
each GitHub bucket's live figures from one free ``/rate_limit`` read and the
pacing in force for Postman and Sourcegraph. It never waits. It exits 0 after
printing, 1 when ``/rate_limit`` is unreadable or malformed, and 2 on a usage
error.
"""

from __future__ import annotations

import dataclasses
import datetime
import email.utils
import fractions
import hashlib
import http.client
import json
import os
import re
import shutil
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path
from typing import Any, Literal, NamedTuple, NotRequired, Protocol, TypeAlias, TypedDict

FLOOR = fractions.Fraction(2, 5)
"""The share of any GitHub REST bucket that must remain after a call (40%), outside the burn-rate exception.

A ``Fraction`` so the boundary is exact: 40 remaining of 100 admits, 12 of 30
admits, with no float rounding either side."""

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

SECONDARY_ATTEMPT_BUDGET: int = 5
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
CACHE_HITS_FILE = "github-cache-hits.jsonl"
"""Where a caller logs a request the shared cache answered: never a call ledger."""

CACHE_DIR_ENV = "CROZIER_GITHUB_CACHE_DIR"
CACHE_KEY_HEADERS = ("accept", "range", "x-github-api-version")
"""The request headers that change a GitHub answer, and so are part of its cache key."""

UNCACHED_RESPONSE_HEADERS = frozenset({"set-cookie", "retry-after", "date", "connection", "transfer-encoding"})
"""Response headers never stored: stale or per-connection once the response is replayed.

Every ``x-ratelimit-*`` header is dropped too: a replayed quota figure is not
a reading."""


class UnsupportedBucket(ValueError):
    """A bucket the guard cannot read for free, ``graphql`` above all."""


class SecondaryLimit(RuntimeError):
    """Refusals persisted past the attempt budget: stop making this call.

    Named for GitHub's secondary limiter, and raised on the same terms when a
    paced lane exhausts its budget, because the contract handles a Postman or
    Sourcegraph refusal the way it handles a secondary one."""


def _now_iso() -> str:
    return datetime.datetime.now(datetime.UTC).isoformat(timespec="milliseconds")


def _token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or None


LOOPBACK_HOSTS = frozenset({"localhost", "127.0.0.1", "::1"})


def valid_port(parsed: urllib.parse.SplitResult) -> bool:
    """Whether a URL's port, when it names one, is a TCP port (urllib reads it only on use)."""
    try:
        port = parsed.port
    except ValueError:
        return False
    return port is None or port > 0


def checked_service_url(value: str, name: str, expected_host: str) -> str:
    """Allow the intended HTTPS host and local HTTP servers used by the offline tier."""
    parsed = urllib.parse.urlsplit(value)
    if (
        not valid_port(parsed)
        or not parsed.hostname
        or (
            not (parsed.scheme == "https" and parsed.hostname == expected_host)
            and not (parsed.scheme == "http" and parsed.hostname in LOOPBACK_HOSTS)
        )
    ):
        raise ValueError(f"{name} must use https://{expected_host} or a loopback HTTP URL")
    return value


class _CheckedRedirects(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to a URL `allowed` accepts, and never carry the
    request's `Authorization` to another host: urllib's own handler follows any
    redirect and copies every header but the body's."""

    def __init__(self, allowed: Callable[[str], bool]) -> None:
        super().__init__()
        self.allowed = allowed

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not self.allowed(newurl):
            raise urllib.error.URLError(f"redirect to {newurl} refused: it is not a URL this request may follow")
        followed = super().redirect_request(req, fp, code, msg, headers, newurl)
        if followed is not None and urllib.parse.urlsplit(newurl).netloc != urllib.parse.urlsplit(req.full_url).netloc:
            followed.remove_header("Authorization")
        return followed


def open_checked(request: urllib.request.Request, allowed: Callable[[str], bool], timeout: float):
    """`urlopen(request)`, following only redirects to URLs `allowed(url)` accepts."""
    return urllib.request.build_opener(_CheckedRedirects(allowed)).open(request, timeout=timeout)


def is_github_api_url(url: str) -> bool:
    """Whether `url` is on the GitHub API root the guard calls (or the loopback one standing in)."""
    root, target = urllib.parse.urlsplit(github_api_url()), urllib.parse.urlsplit(url)
    return (target.scheme, target.netloc) == (root.scheme, root.netloc)


def github_api_url() -> str:
    """The GitHub REST API root the guard reads and callers should call.

    Raises ``ValueError`` for an override that is neither the GitHub API over
    HTTPS nor a loopback HTTP server, before any credential is attached."""
    return checked_service_url(
        os.environ.get("CROZIER_GITHUB_API_URL", GITHUB_API_URL),
        "CROZIER_GITHUB_API_URL",
        urllib.parse.urlsplit(GITHUB_API_URL).hostname or "",
    ).rstrip("/")


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
    with open_checked(request, is_github_api_url, timeout=30) as response:
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


class ResponseHeaders(Protocol):
    """What the cache reads of a response's headers: a live ``HTTPMessage`` or a stored mapping."""

    def get(self, name: str, /) -> str | None: ...

    def items(self) -> Iterable[tuple[str, str]]: ...


class QuotaReading(TypedDict):
    """One bucket's figures as ``GET /rate_limit`` reports them."""

    limit: int
    used: int
    reset: int
    remaining: NotRequired[int]


class BurnFigures(TypedDict):
    """A burn-rate measurement as the ledger records it; ``projected_s`` only when the bucket was spending."""

    rate_per_s: float
    elapsed_s: float
    until_reset_s: float
    projected_s: NotRequired[float]


class AdmissionProbe(TypedDict, total=False):
    """One ``probe`` row of the wait ledger: a reading taken to admit a call, and the decision."""

    host: Literal["github"]
    bucket: str
    kind: Literal["probe"]
    reading: QuotaReading
    cost: int
    admitted: bool
    admitted_by: Literal["floor", "burn-rate"]
    burn: BurnFigures


# A response cache entry's name: the SHA-256 of its canonical request (see ``cache_key``).
CacheKey: TypeAlias = str
# The lower-hex SHA-256 of a stored body's bytes.
Sha256: TypeAlias = str


class CacheHit(TypedDict):
    """The fields a ``github-cache-hits.jsonl`` row records of the answer it was served."""

    cache_key: CacheKey
    status: int
    sha256: Sha256
    bytes: int


class CacheMeta(TypedDict):
    """A cache entry's stored record beside its body: the answer's status, kept headers and body digest."""

    status: int
    headers: list[list[str]]
    sha256: Sha256
    bytes: int


class Burn(NamedTuple):
    """The burn-rate exception's measurement of a bucket: the units spent per
    second over the guard's readings, the seconds they span and until the reset,
    and, when the call is admitted while spending, the seconds the remaining
    quota would last at that rate."""

    rate_per_s: float
    elapsed_s: float
    until_reset_s: float
    projected_s: float | None = None

    def logged(self) -> BurnFigures:
        """The figures a ``probe`` record carries under ``burn``."""
        figures: BurnFigures = {
            "rate_per_s": self.rate_per_s,
            "elapsed_s": self.elapsed_s,
            "until_reset_s": self.until_reset_s,
        }
        if self.projected_s is not None:
            figures["projected_s"] = self.projected_s
        return figures


@dataclasses.dataclass(frozen=True)
class _Reading:
    """One live reading of a bucket, on the monotonic clock for its elapsed time."""

    at: float
    used: int
    reset: int


@dataclasses.dataclass
class _Reservation:
    bucket: str
    cost: int
    reading: QuotaReading | None
    lock: threading.Lock


@dataclasses.dataclass
class _Backoff:
    # Both instants are on the monotonic clock: a wall clock the host steps
    # (time sync moves it by a tenth of a second at a time) would otherwise
    # shorten a wait. A `Retry-After` date or a reset epoch is turned into a
    # delay when it arrives, so it never enters these.
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
        # Per bucket, the first and latest reading in the current reset window.
        self._window: dict[str, tuple[_Reading, _Reading]] = {}

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
        with self._meta:
            reservation = self._pending.pop(threading.get_ident(), None)
        if self.host == "github" and _is_graphql(response):
            if reservation is not None:
                reservation.lock.release()
            raise UnsupportedBucket(
                "a GitHub GraphQL response reached the guard: this repository makes no GraphQL "
                "call (see tools/witness-search/rate_limit_guard.py); make the REST call instead"
            )
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

    def _read(self, bucket: str) -> QuotaReading:
        resources = read_rate_limit()
        figures = resources.get(bucket)
        if not isinstance(figures, dict) or not {"limit", "used", "reset"} <= figures.keys():
            raise UnsupportedBucket(f"GET /rate_limit reports no figures for bucket {bucket!r}")
        values = {key: figures[key] for key in ("limit", "used", "remaining", "reset") if key in figures}
        if not all(isinstance(value, int) and not isinstance(value, bool) and value >= 0 for value in values.values()):
            raise RuntimeError(
                f"GET /rate_limit reported malformed figures for bucket {bucket!r}: {figures!r} — "
                "each must be a nonnegative integer; check CROZIER_GITHUB_API_URL points at the GitHub REST API"
            )
        reading: QuotaReading = {"limit": values["limit"], "used": values["used"], "reset": values["reset"]}
        if "remaining" in values:
            reading["remaining"] = values["remaining"]
        latest = _Reading(time.monotonic(), reading["used"], reading["reset"])
        with self._meta:
            window = self._window.get(bucket)
            first = window[0] if window is not None and window[0].reset == latest.reset else latest
            self._window[bucket] = (first, latest)
        return reading

    def _burn(self, bucket: str, reading: QuotaReading, remaining_after: int) -> Burn | None:
        """The burn-rate exception's figures when it admits the call, else ``None``.

        Admits when the bucket's window resets before ``remaining_after`` would
        be spent at the rate measured between the window's first and latest
        reading; see the module docstring."""
        with self._meta:
            window = self._window.get(bucket)
        if window is None or remaining_after < 0:
            return None
        first, latest = window
        elapsed = latest.at - first.at
        if latest.reset != reading["reset"] or elapsed <= 0:
            return None
        rate = max(latest.used - first.used, 0) / elapsed
        until_reset = reading["reset"] - time.time()
        burn = Burn(round(rate, 6), round(elapsed, 3), round(until_reset, 3))
        if rate == 0:
            return burn
        projected = remaining_after / rate
        if projected <= until_reset:
            return None
        return burn._replace(projected_s=round(projected, 3))

    def _admit(self, bucket: str, cost: int) -> QuotaReading:
        waiting = False
        while True:
            reading = self._read(bucket)
            limit = reading["limit"]
            remaining_after = limit - reading["used"] - cost
            burn = None
            if limit > 0 and remaining_after >= 0 and fractions.Fraction(remaining_after, limit) >= FLOOR:
                admitted_by = "floor"
            elif limit > 0 and (burn := self._burn(bucket, reading, remaining_after)) is not None:
                admitted_by = "burn-rate"
            else:
                admitted_by = None
            admitted = admitted_by is not None
            if waiting or admitted_by != "floor":
                probe: AdmissionProbe = {
                    "host": "github",
                    "bucket": bucket,
                    "kind": "probe",
                    "reading": reading,
                    "cost": cost,
                    "admitted": admitted,
                }
                if admitted_by is not None:
                    probe["admitted_by"] = admitted_by
                if burn is not None:
                    probe["burn"] = burn.logged()
                self._log_wait(dict(probe))
            if admitted:
                return reading
            waiting = True
            duration = max(reading["reset"] - time.time(), 0.0) + RESET_MARGIN_S
            self._sleep(
                duration,
                {
                    "host": "github",
                    "bucket": bucket,
                    "kind": "wait",
                    "cause": "floor",
                    "reading": reading,
                    "cost": cost,
                },
            )

    def _wait_backoff(self, bucket: str, state: _Backoff) -> None:
        duration = state.until - time.monotonic()
        if duration > 0:
            self._sleep(
                duration,
                {"host": "github", "bucket": bucket, "kind": "wait", "cause": "backoff", "refusals": state.refusals},
            )

    def _record_github(self, reservation: _Reservation, response: Any) -> bool:
        bucket = reservation.bucket
        state = self._state[bucket]
        status = _status(response)
        retry_after = _retry_after(response)
        spent: dict[str, Any] = {
            "host": "github",
            "bucket": bucket,
            "at": _now_iso(),
            "status": status,
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
                state.until = max(state.until, time.monotonic() + retry_after)
            return False
        live = self._read(bucket)
        primary = live["used"] >= live["limit"]
        self._log_wait(
            {
                "host": "github",
                "bucket": bucket,
                "kind": "probe",
                "reading": live,
                "classifying": "primary" if primary else "secondary",
                "status": status,
            }
        )
        if primary:
            # The bucket really is spent (by another holder of the token): the
            # next acquire's live reading waits for its reset.
            if retry_after:
                state.until = max(state.until, time.monotonic() + retry_after)
            return False
        return self._refused(state, retry_after, SECONDARY_BACKOFF_BASE_S, SECONDARY_ATTEMPT_BUDGET)

    def _wait_lane(self, lane: str, state: _Backoff) -> None:
        pacing = PACED_LANES[lane]
        now = time.monotonic()
        if state.until > now:
            self._sleep(
                state.until - now,
                {"host": lane, "lane": lane, "kind": "wait", "cause": "backoff", "refusals": state.refusals},
            )
        if state.last_request is not None:
            duration = state.last_request + pacing.spacing_s - time.monotonic()
            if duration > 0:
                self._sleep(
                    duration,
                    {"host": lane, "lane": lane, "kind": "wait", "cause": "spacing", "spacing_s": pacing.spacing_s},
                )

    def _record_lane(self, reservation: _Reservation, response: Any) -> bool:
        lane = reservation.bucket
        pacing = PACED_LANES[lane]
        state = self._state[lane]
        state.last_request = time.monotonic()
        status = _status(response)
        retry_after = _retry_after(response)
        self._log_call({"host": lane, "lane": lane, "at": _now_iso(), "status": status})
        if status not in REFUSAL_STATUSES:
            state.refusals = 0
            if retry_after:
                state.until = max(state.until, time.monotonic() + retry_after)
            return False
        return self._refused(state, retry_after, pacing.backoff_base_s, pacing.attempt_budget)

    def _refused(self, state: _Backoff, retry_after: float | None, base: float, budget: int) -> bool:
        state.refusals += 1
        backoff = max(retry_after or 0.0, base * 2 ** (state.refusals - 1))
        state.until = time.monotonic() + backoff
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
        # Every deadline is set on the monotonic clock, so the wait ends when that
        # clock reaches it: a coarse one (about 16 ms on Windows) can still read
        # short of the deadline after `time.sleep` returns.
        deadline = started + duration
        while (remaining := deadline - time.monotonic()) > 0:
            time.sleep(remaining)
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


def github_cache_root(url: str) -> Path | None:
    """The shared response cache's root for a request to `url`, or ``None`` when it bypasses the cache."""
    override = os.environ.get(CACHE_DIR_ENV)
    if override:
        return Path(override)
    if urllib.parse.urlsplit(url).hostname in LOOPBACK_HOSTS:
        return None
    base = os.environ.get("XDG_CACHE_HOME") or ""
    root = Path(base) if os.path.isabs(base) else Path.home() / ".cache"
    return root / "crozier" / "github-responses"


def cache_key(method: str, url: str, headers: Mapping[str, str]) -> CacheKey:
    """SHA-256 of the request's method, URL and answer-changing headers; never the credential."""
    kept = {name.lower(): str(value) for name, value in dict(headers).items() if name.lower() in CACHE_KEY_HEADERS}
    canonical = json.dumps(
        {"method": method.upper(), "url": url, "headers": kept}, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def is_answer(status: int | None, headers: ResponseHeaders | None, body: bytes = b"") -> bool:
    """Whether a GitHub response is an answer to store, not a refusal or transient failure."""
    if status is None or status >= 500 or status in (401, 407, 408, 429):
        return False
    if status == 403:
        get = getattr(headers, "get", None)
        if get is not None and (get("Retry-After") is not None or get("x-ratelimit-remaining") == "0"):
            return False
        if b"rate limit" in body[:4096].lower():
            return False
    return True


@dataclasses.dataclass(frozen=True)
class CachedResponse:
    """One stored GitHub answer; ``body_path`` holds its bytes."""

    key: CacheKey
    status: int
    headers: tuple[tuple[str, str], ...]
    body_path: Path
    sha256: Sha256
    size: int

    def body(self) -> bytes:
        return self.body_path.read_bytes()

    def message(self) -> http.client.HTTPMessage:
        """The stored headers as the ``HTTPMessage`` a live response carries."""
        message = http.client.HTTPMessage()
        for name, value in self.headers:
            message[name] = value
        return message

    def ledger(self) -> CacheHit:
        """The fields a caller's ``github-cache-hits.jsonl`` row records."""
        return {"cache_key": self.key, "status": self.status, "sha256": self.sha256, "bytes": self.size}


def _meta_path(root: Path, key: str) -> Path:
    return root / key[:2] / f"{key}.json"


def _body_path(root: Path, key: str, sha256: str) -> Path:
    """A body's file, named by its own digest so no writer ever replaces it with other bytes."""
    return root / key[:2] / f"{key}.{sha256}.body"


def _file_digest(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def cache_lookup(method: str, url: str, headers: Mapping[str, str]) -> CachedResponse | None:
    """The stored answer for this request, or ``None`` on a miss (or a torn or unreadable entry)."""
    root = github_cache_root(url)
    if root is None:
        return None
    key = cache_key(method, url, headers)
    meta_path = _meta_path(root, key)
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if not isinstance(meta, dict):
            return None
        status, stored, sha256, size = meta.get("status"), meta.get("headers"), meta.get("sha256"), meta.get("bytes")
        # Only a record `cache_store` could have written is replayed: an HTTP
        # status, string header pairs, a SHA-256 and a byte count.
        if (
            type(status) is not int
            or not 100 <= status <= 599
            or not isinstance(stored, list)
            or not all(
                isinstance(pair, list) and len(pair) == 2 and all(isinstance(part, str) for part in pair)
                for pair in stored
            )
            or not isinstance(sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", sha256) is None
            or type(size) is not int
            or size < 0
            or _file_digest(body_path := _body_path(root, key, sha256)) != (sha256, size)
        ):
            return None
        cached = CachedResponse(key, status, tuple((name, value) for name, value in stored), body_path, sha256, size)
        with body_path.open("rb") as handle:
            head = handle.read(4096)
        # A refusal is never an answer, however it was stored.
        return cached if is_answer(status, cached.message(), head) else None
    except (OSError, ValueError):
        return None


def _publish(path: Path, write: Callable[[Path], object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")
    try:
        write(temporary)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def cache_store(
    method: str,
    url: str,
    headers: Mapping[str, str],
    status: int | None,
    response_headers: ResponseHeaders | None,
    body: bytes | Path,
) -> CachedResponse | None:
    """Store an answer (see ``is_answer``) for later requests; ``None`` when it is not one or cannot be stored.

    ``body`` is the bytes, or a file holding them (a large download). A cache
    that cannot be written is reported on stderr and costs the caller nothing."""
    root = github_cache_root(url)
    if isinstance(body, bytes):
        probe = body[:4096]
    else:
        # A file-backed body is judged on the same head a refusal's message sits in.
        try:
            with body.open("rb") as handle:
                probe = handle.read(4096)
        except OSError:
            return None
    if root is None or status is None or not is_answer(status, response_headers, probe):
        return None
    key = cache_key(method, url, headers)
    meta_path = _meta_path(root, key)
    kept = tuple(
        (str(name), str(value))
        for name, value in (response_headers.items() if response_headers is not None else ())
        if name.lower() not in UNCACHED_RESPONSE_HEADERS and not name.lower().startswith("x-ratelimit-")
    )
    try:
        staged = meta_path.with_name(f".{key}.{os.getpid()}.{threading.get_ident()}.body.tmp")
        staged.parent.mkdir(parents=True, exist_ok=True)
        try:
            if isinstance(body, bytes):
                staged.write_bytes(body)
            else:
                shutil.copyfile(body, staged)
            sha256, size = _file_digest(staged)
            body_path = _body_path(root, key, sha256)
            # A body already holding these bytes is left in place: replacing a
            # file another process has open fails on Windows, and a reader
            # there would see it vanish mid-replace.
            try:
                published = _file_digest(body_path) == (sha256, size)
            except OSError:
                published = False
            if not published:
                os.replace(staged, body_path)
        finally:
            staged.unlink(missing_ok=True)
        meta: CacheMeta = {"status": status, "headers": [list(pair) for pair in kept], "sha256": sha256, "bytes": size}
        _publish(meta_path, lambda path: path.write_text(json.dumps(meta, sort_keys=True), encoding="utf-8"))
    except OSError as error:
        print(
            f"rate_limit_guard: could not store a GitHub response in {root}: {error}; "
            f"the request will be asked again — check {CACHE_DIR_ENV} or that directory's permissions",
            file=sys.stderr,
        )
        return None
    return CachedResponse(key, status, kept, body_path, sha256, size)


def status() -> int:
    """Print every bucket's live figures from one free read; never wait."""
    try:
        api_url = github_api_url()
    except ValueError as error:
        print(f"quota-status: {error} — unset it or point it at the GitHub REST API", file=sys.stderr)
        return 1
    try:
        resources = read_rate_limit()
    except (OSError, RuntimeError, ValueError) as error:
        print(f"quota-status: could not read {api_url}/rate_limit: {error}", file=sys.stderr)
        print(
            "quota-status: check network access, and set GITHUB_TOKEN to read the token's own buckets", file=sys.stderr
        )
        return 1
    lines = []
    for bucket in sorted(set(resources) - {"graphql"}):
        figures = resources[bucket]
        try:
            limit, used, reset = (int(figures[key]) for key in ("limit", "used", "reset"))
        except (KeyError, TypeError, ValueError):
            print(
                f"quota-status: GET /rate_limit reported malformed figures for {bucket!r}: {figures!r}", file=sys.stderr
            )
            print("quota-status: check CROZIER_GITHUB_API_URL points at the GitHub REST API", file=sys.stderr)
            return 1
        share = used / limit if limit else 0.0
        below = limit > 0 and fractions.Fraction(limit - used, limit) < FLOOR
        when = datetime.datetime.fromtimestamp(reset, datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        guarded = "guarded" if bucket in GITHUB_BUCKETS else "not called here"
        flag = "  BELOW FLOOR" if below else ""
        lines.append(f"  {bucket:<28} limit {limit:>6}  used {used:>6}  {share:>6.1%}  reset {when}  {guarded}{flag}")
    auth = "authenticated" if _token() else "unauthenticated: set GITHUB_TOKEN"
    print(f"github ({auth}; floor {float(FLOOR):.0%} remaining, burn-rate exception)")
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
