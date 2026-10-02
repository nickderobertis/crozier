# Unsuitable enum names

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**;
no generator repair is made.

The probe generates and imports, and mypy 1.13.0 under the generated
`pyproject.toml` reports zero errors. Through the generated client, `GET /probe`
parses `#0094FF` and serialization preserves it. However, the generated
identifiers `_0094FF` and `_838383` add private-looking leading underscores
absent from the document. That alone fails the acceptance bar. Committed logs:
[generation](evidence/enum-name-unsuitable.generate.log),
[import](evidence/enum-name-unsuitable.import.log),
[mypy](evidence/enum-name-unsuitable.mypy.log),
[wire](evidence/enum-name-unsuitable.wire.log).

One retrievable population representative from KOSCOM confirms the same
identifier issue. `POST /get-account-list` parses the declared response property
`accountType` as `종합-00`, and serializing the result preserves both that alias
and value. Its enum member `_00` adds a leading underscore. The package imports
but reports **2 mypy errors** under its own configuration. The representative's
immutable locator is recorded in its generation log; the source is the cached
Jentic copy, with no SwaggerHub request.

Population digest: `0fecc098ba9097c085e2bcbb46fbf55e51b4032d5d23719ce49dff4197e8c610`.
[generation](evidence/0fecc098ba9097c085e2bcbb46fbf55e51b4032d5d23719ce49dff4197e8c610.generate.log),
[import](evidence/0fecc098ba9097c085e2bcbb46fbf55e51b4032d5d23719ce49dff4197e8c610.import.log),
[mypy](evidence/0fecc098ba9097c085e2bcbb46fbf55e51b4032d5d23719ce49dff4197e8c610.mypy.log),
[wire](evidence/0fecc098ba9097c085e2bcbb46fbf55e51b4032d5d23719ce49dff4197e8c610.wire.log).

Supplemental measurements use the pinned Fern CLI, without reading its source:
[`+1`](evidence/plus.fern-check.log) and [`_1`](evidence/underscore.fern-check.log)
are unsuitable names, while [`1st`](evidence/letter-digit.fern-check.log) is
accepted. Invalid explicit overrides
([digit-led](evidence/named-digit.fern-check.log),
[hyphenated](evidence/named-hyphen.fern-check.log),
[underscore-led](evidence/named-underscore.fern-check.log)) warn and fall back to
the original value. These controls prevent refusing an accepted digit-led enum
or treating an invalid override as a rescue.

ASCII [punctuation](evidence/punctuation.fern-check.log) and
[whitespace](evidence/space.fern-check.log) produce an empty unsuitable enum
name. The real registry gate was observed
[failing before the detector](evidence/pre-detector-gate-failure.log):
both modes generated the probe and wrote 38 files instead of refusing.

Strict population: **368/368** retrievable documents refuse with exit 1 and
no files written ([population log](evidence/population-strict.log)). The log
labels its two measurement phases: 307 documents already refused through the
enum-value detector at `e95eefa21`; the remaining 61 were measured through the
enum-name detector. Adding this detector preserves those earlier refusal
outcomes. Each corresponding `crozier_strict_exit` is 1.
