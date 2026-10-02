# example-not-enum-value: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. Its [public-client journey](evaluation-logs/probe.wire.log)
sends `GET /activities` with no body and parses both declared `kind` values
(`FILL`, `ACATC`) into `ActivityKind`. The probe alone would qualify the class.

Two population representatives from different publishers disqualify it:

- [Alpaca's broker description (sourcegraph, `0f91f138…`)](evaluation-logs/population-alpaca.log),
  the document the probe was isolated from, imports but reports **362 mypy
  errors**. Fern's diagnostic there is `TradeActivity.type`'s first value
  `fill` validated against `ActivityType`, the component its inline enum is
  named like once `Activity`'s `allOf`/`oneOf` merges it. The baseline's
  `Activity` declares only `account_id`, `activity_type` and `id`; its
  [journey](evaluation-logs/population-alpaca.wire.log) parses a declared trade
  activity with `type`, `qty` and `symbol` left untyped. Declared fields are
  dropped.
- [General Translation's API (github-code-search, `a43acb95…`)](evaluation-logs/population-general-translation.log)
  imports but reports **486 mypy errors**.

The class is `refuse` in both modes. No generated SDK changes.

## What Fern rejects, and what it lets through

Refused shapes, each a committed `*-probe.yml` with its Fern log, detected by
the shared example-value walker (`src/document_refusals/examples.rs`):

- a string outside a string enum in `x-fern-examples` — a response body (the
  probe), a request body
  ([fern-examples-request](evaluation-logs/fern-fern-examples-request.log)) or a
  query parameter
  ([fern-examples-query](evaluation-logs/fern-fern-examples-query.log));
- a tagged operation answering a `$ref`'d JSON object, whose optional header
  `$ref`s a string enum not listing the header's name: Fern passes the header
  its own name, whatever example or default is declared (Intercom's
  `Intercom-Version`, General Translation's `gt-api-version`;
  [header-name-enum](evaluation-logs/fern-header-name-enum.log));
- an inline enum of a `oneOf` member merged into an `allOf` owner, named like a
  later string enum component that lacks its first value
  ([merged-member-enum](evaluation-logs/fern-merged-member-enum.log)).

Accepted near misses, each a committed `*-control.yml` whose Fern log exits 0
and which the CLI journey generates identically in both modes:
[a written media example's enum value is not checked](evaluation-logs/fern-written-enum.log),
[a query parameter `$ref`ing the enum](evaluation-logs/fern-query-enum-reference.log),
[a tag equal to the `operationId`](evaluation-logs/fern-tag-equals-operation.log),
[a header name the enum lists](evaluation-logs/fern-header-name-in-enum.log),
[an untagged operation](evaluation-logs/fern-untagged-header.log), and
[`x-crozier-examples`, which pinned Fern does not read](evaluation-logs/fern-crozier-examples.log).

The [probe assertion failed with only its predicate disabled](evaluation-logs/refusal-e2e-induced-red.log)
(the probe generated 39 files), and passed again once restored. The corpus
byte-match passes with `fern-strict` off and on (189 tests each).

[All 50 population documents](evaluation-logs/population-refusals.jsonl),
measured with the finished detector, were retrieved at their digests and
refused in both modes: exit 1, no files, one class/element stderr line and the
strict cause when applicable. Four are refused by this class; the rest by
another registered class or example-value rule that fires first.
