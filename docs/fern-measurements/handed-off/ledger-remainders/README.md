# Ledger remainders: Webflow collections exports

No row here is `default-matched` or `ruling-applied:*`. No new departure or
repair is needed: this node verifies the collections initializer as
**`already-matching`** at its base. The authoritative cause is already recorded
once, as [#694](https://github.com/nickderobertis/crozier/issues/694), in
[`follow-up-tickets.tsv`](../follow-up-tickets.tsv); the area TSV has no duplicate
cause. No ticket was moved.

## Document and certified generation

`webflow-v2`, corpus row 132, is Webflow's own `openapi/v2.yml` at
`webflow/openapi-spec@f6db607359a412dd6aa6cd304674731d7f2dbe10`, SHA-256
`a765cfec420d5f9c3dc4fe5af81396594a27547a591ba6c25ac1248e64a967f7`.
Its source is committed at `tests/fixtures/corpus-sources/webflow-v2/openapi.yml`.

A fresh generation through `generate-fern-fixture.sh webflow-v2 5.41.3
<committed-source>`, under the shared generation lock, wrote the complete
1,501-file `tests/fixtures/webflow-v2/expected/` tree with Fern CLI 5.163.1 and
Python SDK 5.41.3. The generated files were not edited. The initial
`just fern-goldens-generate --version 5.41.3 --fixture webflow-v2` had reported
that tree current; the subsequent direct generation is the fresh measurement.

## Collections initializer

The certified tree exports a union variant owned by both the collections'
`.types` and `.fields` packages through `.fields` once. Crozier does the same;
there is no duplicate lazy-map key or `__all__` entry. This is exactly the
shared-export cause #694 repaired at the base in
`emit::tag_pkg_init_file`. Its existing unit regression is
`a_parent_exports_a_shared_type_from_its_child_once`.

`src/fern/collections/__init__.py` is absent from the measured `unmatched`
list and from all three difference lists in the full
[`crozier compare` measurement](694/comparison.json), whose normalized
[diff](694/comparison.diff) is retained unchanged. The real corpus test
`webflow_v2_matches_fern_output` compares this file. Thus the collections file
of `boolean-schema-true` is proven whole; no default or design-review ruling
needs to decide a remaining difference in it.

## Whole-document status

**Webflow v2 does not byte-match whole.** The fresh complete comparison reports
11 differing files, 34 files only in the certified tree and none only in
crozier. Every remaining file is named and attributed in
[`remaining.tsv`](remaining.tsv), to its visible example-selection,
description-propagation or audit-log-union cause. These attributions describe
the measured hunks; they do not claim a repair or decide output outside this
subtask. The corpus registration's broader pinned unmatched set is unchanged.

It therefore remains a blocked whole-document witness for
`combo-inline-body-read-only-property`, even though the collections-export
remainder itself is closed.
