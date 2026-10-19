# `stream-reference-return-type`

**Kind:** `fern-defect`, as the manager ruled. Fern heads every streaming method
in `reference.md` with `-> typing.Iterator[bytes]`. The method it documents
returns an iterator of parsed chunks.

## The input

[`streaming-extension-terminator/openapi.yml`](../../openapi-surface/handwritten/streaming-extension-terminator/openapi.yml),
a crozier-authored document. Its `GET /builds/{buildId}/log` streams
Server-Sent Events of a `StepResult` model, ended by a `[DONE]` terminator.
Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 exits 0 on it. The
comment-stripped tree is the fixture's `fern-expected/`, whose `reference.md`
line 2 heads the method `follow_build_log(...) -> typing.Iterator[bytes]`.

Every stream does the same, whatever its framing or chunk type. The registered
SSE goldens and the newline-delimited JSON halves of corpus row 1600
(`zylon-private-gpt`) all carry the heading at the new pair: the comparison
applies this departure in 32 goldens: eleven hand-written fixtures, one
measurement case and twenty corpus goldens and overlays. A binary download is the one case where the heading is true: its
method does return `typing.Iterator[bytes]`, and this departure never touches
it.

## Why it is a defect

The [journey](../../../crates/crozier-e2e/tests/e2e/stream_reference_heading.py)
imports the generated package and reads the method's declared return annotation.
It then iterates a real stream: two `StepResult` events and the terminator,
served by a local HTTP server. It compares both with the method's
`reference.md` heading. `just test-sdk-env` runs it as
`sdk_env_stream_reference_heading_states_the_returned_iterator` in
`crates/crozier-e2e/tests/e2e.rs`, three ways.

Re-run at the new pair, over Fern's tree, expecting the heading to contradict
the method, it exits 0:

```text
reference.md heads follow_build_log `-> typing.Iterator[bytes]`; the method declares `-> typing.Iterator[StepResult]`; iterating yields ['StepResult']
```

Over Fern's tree, expecting agreement, it exits 1 (`expected the heading to
agree with the method, and it does not`). That is the induced failure
showing the assertion detects the defect. `reference.md` documents a return
type the method does not have, which the defect rule names.

## crozier's output

crozier heads the method with the iterator its sync signature declares. Over
crozier's SDK, generated from the same document with package `fern` and project
`default_package_name` and expecting agreement, the journey exits 0:

```text
reference.md heads follow_build_log `-> typing.Iterator[StepResult]`; the method declares `-> typing.Iterator[StepResult]`; iterating yields ['StepResult']
```

The rule in [`src/departures.rs`](../../../src/departures.rs) accepts only a
heading line whose two sides differ in that annotation alone. Fern's must be
`typing.Iterator[bytes]`. crozier's must be the annotation the linked module's
method declares. `tests/fixtures/departures-ledger.tsv` pins each application
by golden, file and line.
