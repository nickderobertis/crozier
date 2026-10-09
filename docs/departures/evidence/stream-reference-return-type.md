# `stream-reference-return-type`

**Kind:** `fern-defect`, as the manager ruled. Fern heads every streaming method
in `reference.md` with `-> typing.Iterator[bytes]`. The method it documents
returns an iterator of parsed chunks.

## The input

[`streaming-extension-terminator/openapi.yml`](../../openapi-surface/handwritten/streaming-extension-terminator/openapi.yml),
a crozier-authored document. Its `GET /builds/{buildId}/log` streams
Server-Sent Events of a `StepResult` model, ended by a `[DONE]` terminator.
Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0 exits 0 on it. The
comment-stripped tree is the fixture's `fern-expected/`.

Every stream does the same, whatever its framing or chunk type. The registered
SSE goldens and the newline-delimited JSON halves of corpus row 1600 all carry
the heading. A binary download is the one case where the heading is true: its
method does return `typing.Iterator[bytes]`, and this departure never touches
it.

## Why it is a defect

The [journey](stream-reference-return-type.py) imports the generated package and
reads the method's declared return annotation. It then iterates a real stream:
two `StepResult` events and the terminator, served through httpx's transport
boundary. It compares both with the method's `reference.md` heading. Run from
the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 uv run -q --no-project --python 3.12 --with httpx --with pydantic \
  python docs/departures/evidence/stream-reference-return-type.py \
  docs/openapi-surface/handwritten/streaming-extension-terminator/fern-expected contradicts
```

Result, exit 0:

```text
reference.md heads follow_build_log `-> typing.Iterator[bytes]`; the method declares `-> typing.Iterator[StepResult]`; iterating yields ['StepResult']
```

The same run expecting `agrees` exits 1 against Fern's tree. That is the
induced failure showing the assertion detects the defect. `reference.md`
documents a return type the method does not have, which the defect rule names.

## crozier's output

crozier heads the method with the iterator its sync signature declares. Generate
crozier's SDK from the same document with package `fern` and project
`default_package_name`, and run the journey on that SDK's root expecting
`agrees`. Result, exit 0:

```text
reference.md heads follow_build_log `-> typing.Iterator[StepResult]`; the method declares `-> typing.Iterator[StepResult]`; iterating yields ['StepResult']
```

The rule in [`src/departures.rs`](../../../src/departures.rs) accepts only a
heading line whose two sides differ in that annotation alone. Fern's must be
`typing.Iterator[bytes]`. crozier's must be the annotation the linked module's
method declares. `tests/fixtures/departures-ledger.tsv` pins each application
by golden, file and line.
