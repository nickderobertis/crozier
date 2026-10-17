# `emoji-tag-reference-identifiers`

**Kind:** `fern-defect`. A tag whose name holds a character no Python
identifier admits: Fern's `README.md` and `reference.md` spell its client
accessor, source link and imports with the raw character, although its own
package names the module by an identifier.

## The input

[`marina-emoji-tag/openapi.yml`](../../fern-measurements/examples-docs/marina-emoji-tag/openapi.yml),
a crozier-authored document declaring the tags `Moorings` and
`🚧 Legacy endpoints` at its top level, and two operations tagged with the
second. The real dystore API tags its unsupported operations
`⚠️ Not supported yet` the same way.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds, exits 0; the
comment-stripped tree is the case's `fern-expected/`. The package's module is
`src/fern/legacy_endpoints/`, and its client exposes `legacy_endpoints`. Yet
`README.md` calls `client.🚧_legacy_endpoints.list_legacy_moorings(...)`, and
`reference.md` writes `client.🚧_legacy_endpoints.` with the link
`src/fern/🚧_legacy_endpoints/client.py` for both operations.

## Why it is a defect

Running each tree's first `README.md` usage block with its own package on
`PYTHONPATH` (Python 3.12, `httpx`, `pydantic` 2.14.1; the base URL pointed at
a closed local port):

```text
fern     client.🚧_legacy_endpoints.list_legacy_moorings(
         SyntaxError: invalid character '🚧' (U+1F6A7)                     exit 1
crozier  client.legacy_endpoints.list_legacy_moorings(
         httpx.ConnectError: [Errno 111] Connection refused               exit 1
```

Fern's documented call does not compile, so it cannot reach the method; the
same call through crozier's documented accessor is valid Python, resolves the
method and sends the request (`inspect.signature(...).bind(include="buoys")`
binds). Of the links each `reference.md` writes:

```text
fern     src/fern/🚧_legacy_endpoints/client.py   missing
crozier  src/fern/legacy_endpoints/client.py      exists
```

The docs contradict the generated code, a defect under the defect rule. The
same execution against the certified tree generated from a document tagged
`⚠️ Not supported yet` fails with `SyntaxError: invalid character '⚠'
(U+26A0)`.

## crozier's output

crozier writes the same tree but for those lines: every occurrence of the raw
spelling in `README.md` and `reference.md` is the module identifier its package
defines, `legacy_endpoints`.

## The parity rule

The rule accepts one aligned line pair of `README.md` or `reference.md` when
the parsed source document has an operation tag whose words, lowered and joined
by `_`, hold a character no Python identifier admits, the identifier left once
those characters and the surrounding `_` are removed names a module crozier's
package holds (`src/<package>/<module>/client.py`), and Fern's line is
crozier's with every occurrence of that identifier replaced by the raw
spelling. `examples_docs_measurements_match_fern` and
`examples_docs_cases_fail_on_an_adjacent_unexplained_byte` in
`crates/crozier-e2e/tests/e2e/examples_docs.rs` hold the case; the line ledger
is recorded from `src/parity.rs`, never hand-edited.
