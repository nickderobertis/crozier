# `text-response-optional-query-examples`

**Kind:** `richer-documentation`. An operation whose successful responses
answer only `text/*`: Fern's worked calls pass only the required arguments,
crozier's also pass each optional query parameter's declared example.

## The input

[`marina-dock-log/openapi.yml`](../../fern-measurements/examples-docs/marina-dock-log/openapi.yml),
a crozier-authored document whose `GET /docks/{dock_id}/log` answers `200`
with `text/plain` only, beside a required `dock_id` path parameter and two
optional query parameters whose schemas declare examples: `columns`
(`vessel,arrival`) and `compact` (`'true'`). The real Supabase management API's
`v1-diff-a-branch` is the same shape (`included_schemas: public,auth`,
`pgdelta: 'true'`).

## Fern's output

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds, exits 0; the
comment-stripped tree is the case's `fern-expected/`. Fern builds no example
from the document for a `text/*` success body, so `README.md`, `reference.md`
and both `export_dock_log` docstrings pass `dock_id="dock_id"` alone; for a JSON
success body both Fern and crozier pass the same optional examples. crozier's
tree adds `columns="vessel,arrival",` and `compact="true",` after it: lines
45–46 and 67–68 of `README.md`, 24–25 of `reference.md`, and 59–60 and 123–124
of `src/fern/docks/client.py`. The supabase-api-v1 golden shows the same at
the new pair (`reference.md` lines 647–648 and two docstrings of
`src/fern/environments/client.py`).

## Both sides are valid; crozier's documents the declared examples

Binding every worked call of `export_dock_log` in each tree's client docstrings
and `reference.md` (three per tree) to the package's own method, re-run at the
new pair:

```text
fern     {"dock_id": "'dock_id'"}                                                  binds
crozier  {"dock_id": "'dock_id'", "columns": "'vessel,arrival'", "compact": "'true'"}  binds
```

Validating the declared examples with `jsonschema` 4.26.0:

```text
columns optional example 'vessel,arrival' valid against {"type": "string"}
compact optional example 'true' valid against {"type": "string"}
responses 2xx media: ['text/plain']
```

## The parity rule

The rule accepts a worked-example line only crozier writes in `README.md`,
`reference.md` or a high-level `client.py`, `<name>=<value>,`, when the parsed
source document has an operation whose successful responses are all `text/*`
with an optional query parameter passed as `<name>` that declares that value.
A required parameter, a value no parameter declares, a JSON-answering
operation, or a missing source document leaves the line a difference.
`examples_docs_measurements_match_fern` and
`examples_docs_cases_fail_on_an_adjacent_unexplained_byte` in
`crates/crozier-e2e/tests/e2e/examples_docs.rs` hold the case; the line ledger
is recorded from `src/parity.rs`, never hand-edited.
