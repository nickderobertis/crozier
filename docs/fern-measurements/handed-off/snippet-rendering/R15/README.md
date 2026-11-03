# `R15`

The handed-off root cause `R15` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A members' gallery downloads a portrait (`*/*`, `format: binary`) and a sepia one (`image/png`) through two path parameters, neither declaring an error, and a thumbnail (`application/octet-stream`) through one path parameter, declaring a JSON `404`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py`'s own `generated_tree` (the same function its `measurements` family runs), under the shared Fern lock. The directory name is the record's cause name, which `cases.tsv`'s lower-case case names cannot spell, so it has no `cases.tsv` row.

## The comparison

The certified pair's `reference.md` gives both error-less downloads the bare `client.portraits.<method>(...)` line and works the thumbnail's call (`member_id="memberId"`). crozier writes the same at this node's base.

**Verdict: `already-matching`, cleared by `630240929` (#722, the bodies-media landing).** Built at `6b4509ab9` (its parent), crozier still wrote a worked call for nextcloud's `core_avatar.get_avatar_dark`; built at `630240929` it writes the bare line, and the nextcloud document's `reference.md` and avatar clients match (its remaining files are `R16`'s, another area's). crozier's tree for this document byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`).
