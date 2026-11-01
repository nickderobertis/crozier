# `R1`

Root cause `R1` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md),
triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv).

**Rule.** The certified pair's importer throws while it reads the document. It
logs `Failed to parse openapi document`, still exits 0, and writes the 35-file
empty SDK. By the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, with the refusal rule's exception for valid OpenAPI
whose empty SDK is only a Fern limitation. R1 names two documents, which
therefore part:

- **lolesports keeps generating.** It is valid OpenAPI, and the pair's
  `RangeError: Maximum call stack size exceeded` comes from its example builder
  (`buildExampleHelper`). The builder recurses without end through a required
  property that is an `allOf` of its own schema and a nullable object
  (`navItem.parentNavItem`).
- **tacd is refused.** Its importer error is
  `Cannot read properties of null (reading 'schema')`, from a Media Type Object
  written as `null`. That is invalid OpenAPI, measured in
  [`../refusal-null-media-type/`](../refusal-null-media-type/README.md), and now
  refused as the class `null-media-type`.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: a `Shelf`
whose required `parentShelf` is `allOf: [$ref Shelf, {type: object, nullable:
true}]`. [`control.yml`](control.yml) is the same document with `parentShelf`
optional.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. On `openapi.yml` the pair exits 0 and writes the 35-file empty SDK
(`fern-expected/`). [`fern.log`](fern.log) reads:

    [api]: Failed to parse openapi document Reading Room
           RangeError: Maximum call stack size exceeded
               at e.buildExampleHelper (…/fern-api/cli.cjs:207:9133)

On `control.yml` the pair generates 41 files, and
[`control.fern.log`](control.fern.log) carries no error. So the required
self-reference alone empties the SDK.

**The real documents.** Each was run through the pair on its exact bytes, SHA-256
verified against the record:

| document | SHA-256 | the pair | crozier on the finished tree |
|---|---|---|---|
| `vickz84259/lolesports-api-docs:openapi.yaml@74027a7950c7e4629d3cab01ddd3990457a9956d` | `5737ba80e2e41e0bdf0f3e9079dcd757c16553d3f120b3f6d8bba6f3dc782d9c` | exit 0, 35 files, `Maximum call stack size exceeded` | generates 243 files, by default and under `--fern-strict` |
| `linux-automation/tacd:openapi.yaml@df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` | `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c` | exit 0, 35 files, `Cannot read properties of null (reading 'schema')` | refused in both modes, `null-media-type` |

**Evaluation (the exception).**
[`lolesports-sdk-evaluation.json`](lolesports-sdk-evaluation.json) is
`fern-refusals.py evaluate-sdk`'s receipt over lolesports' exact bytes. The
chain is OpenAPI validation, default and strict generation (equal trees), a
wheel build, a fresh installation, and an import of every generated module, and
every stage passed. The receipt was taken with the release binary built at this
node's base, `6b4509ab9`. On the finished tree crozier's SDK for lolesports is
byte-identical to that build's, file for file. The exception is recorded in
[`extension-reference-cycle`'s evaluation](../../../../fern-refusals/extension-reference-cycle/evaluation.md),
the class whose phrase the pair prints.

**crozier.** crozier generates `openapi.yml` in both enum modes and both refusal
modes. [`crozier-tree.tsv`](crozier-tree.tsv) records each file's SHA-256, with
`python_enums`; the literals tree is the same without `src/fern/core/enum.py`.
`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` holds the tree to that manifest, the pair's empty SDK to its log and file
count, and the control to its generation.

**Verdict.** `user-ruling` (`empty-sdk-refused`): lolesports generates under the
valid-OpenAPI exception, and tacd is refused.
