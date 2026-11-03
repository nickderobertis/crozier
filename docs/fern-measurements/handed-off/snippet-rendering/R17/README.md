# `R17`

The handed-off root cause `R17` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A market's `GET /stalls/availability` declares an optional `market` (string, `example: riverside`), a required `row`, an optional `week` (integer, `example: 14`) and a required `stall`, in that order.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py`'s own `generated_tree` (the same function its `measurements` family runs), under the shared Fern lock. The directory name is the record's cause name, which `cases.tsv`'s lower-case case names cannot spell, so it has no `cases.tsv` row.

## The comparison

The certified pair's worked call keeps declaration order (`market`, `row`, `stall`; the optional integer leaves the call); crozier writes the same at this node's base.

**Verdict: `already-matching`, cleared by `de440bc03` (#669, "match the certified pair on worked-example order …").** Built at its parent the vtex Marketplace-Protocol document still differed; built at `de440bc03` it byte-matches, as it does on the finished tree, where it is registered as corpus row 3479 (`vtex-marketplace-protocol`) and its golden test passes. crozier's tree for this document byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`).
