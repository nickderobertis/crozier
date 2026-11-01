# `missing-relative-file`: section E of the refusal-parity record

The document of [`refusal-parity-ten-documents.md`](../../../../refusal-parity-ten-documents.md),
section E (`outstack/enveloper`), triaged in
[`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv). crozier
refused it with a resolve error, not a registry class, so the row is named for
its shape.

**Measured: no empty SDK.** `outstack/enveloper:docs/api/openapi.yaml@cd8150d6d78c64ff48acdfb886c833a4600515df`
(SHA-256 `95595ff60c5a51617e5bd497fb94eeba13e6b3566c271b5bf59403a5789145bf`),
run through the certified pair on its exact bytes, exits 0 with no error and
writes 44 files. Those are the `messages` client's four operations, with every
schema `$ref` to a missing relative file read as `typing.Any`. The record's
account of that output is current. Ruling `empty-sdk-refused` does not cover it,
and no ruling names it. The no-ruling default applies, and the planner confirmed
it: crozier matches the certified pair.

**Rule.** Two shapes, both in enveloper:

- A Schema Object `$ref` naming a relative file that does not exist is
  `typing.Any`. crozier writes one `crozier: warning:` line per such reference
  to stderr, naming the referring document, the JSON pointer of each `$ref`
  writing it, and the missing file, and still exits 0 in both modes.
- An inline body whose `discriminator.mapping` names local pointers outside
  `#/components/schemas/` (enveloper's `#/Components/schemas/…`, under a
  capital-C key neither tool reads) is `typing.Any`, as a mapping to a bare
  schema name already was.

**What stays an error.**

- A missing file a security scheme, a response or a parameter names stays
  refused as `unresolved-reference`.
- A file that exists but cannot be read keeps its read error.
- A remote document that cannot be fetched keeps its fetch error.
- A component that is itself a `$ref` to a missing file cannot form a type name.
  The pair refuses it (`Type name must begin with a letter`;
  [`missing-relative-component.fern.log`](missing-relative-component.fern.log)
  for the whole-file form,
  [`missing-relative-component-pointer.fern.log`](missing-relative-component-pointer.fern.log)
  for the pointer form), and crozier refuses both as `type-name-not-letter-led`.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch in
enveloper's shape. A post room's `sendParcel` request and `202` response are
`$ref`s to absent `./generated/*.schema.yaml` files, and its `400` is an inline
object discriminated by `title`, mapped to `#/Components/schemas/…`. A
`Components` block names two more absent files.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. The pair generates 40 files (`fern-expected/`) and its log carries no
error. `request` and the response are `typing.Any`, and `BadRequestError` takes
`body: typing.Any`.

**Change.**

- `src/refs.rs`: `Resolver::missing_local_file` generalizes the
  `#/components/schemas/`-only case NDW's golden pinned to every relative file
  that does not exist. `Resolver::missing_file_warnings` and
  `reference_pointers` write the warnings.
- `src/ir.rs`: `unresolvable_mapped_error_body` is true of a body mapped to a
  bare name or to a local pointer outside `#/components/schemas/`.
  `error_body_type` and `hoist_error_body_types` type such a body as unknown
  and hoist no model for it. Only the error-body form is measured, so the
  named-union, request and success-response paths keep `bare_name_mapped_union`
  unchanged.

**Comparison on the finished tree.**

- `openapi.yml`: crozier's output byte-matches `fern-expected/`, apart from the
  departures the ledger records, by default and under `--fern-strict`, with the
  two warnings, one per operation `$ref`. The `Components` entries sit under
  no key OpenAPI reads, so nothing resolves or warns of them. The document declares no enum, so `python_enums` is the only
  tree.
- Enveloper's exact bytes: crozier writes the same 44 paths as the pair's tree.
  Stripped of comments, every file outside `core/`, `tests/` and
  `_default_clients.py` is identical, and those three hold the catalogued
  departures. That holds by default and under `--fern-strict`, with eight
  warnings, one per missing file. Enveloper is not committed, since the corpus
  rules were not screened for it; the probe stands in for it.

`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` holds the probe's tree and warnings, both component refusals, and each
of the errors above. Unit tests of the touched functions are in `src/refs.rs`
and `src/ir.rs`.

**Verdict.** `default-matched`: no ruling covers the difference, so crozier
matches the certified pair. The warning is the planner's addition, and no
generated byte depends on it.
