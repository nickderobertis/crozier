# crozier-refuses-component-link-ref

Root cause `crozier-refuses-component-link-ref` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A response `links` entry that is a `$ref` to a declared `components/links` entry.

## The measurement

`openapi.yml` is [`R14`](../R14/README.md)'s parcel document with `components.links.ReadParcel` declared. The rule is R14's (the certified pair ignores response links), settled here from the schemas record. It was authored from scratch for this measurement (SHA-256 `4754ada26fadf2cf4f95a7905ee588db02e03089961df0b5f031d6d14b3dda75`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `b614ae8b9a1c37c820329dfbb9ec5d4cd3263b852d9d9d9a01ec1b421556c677`. `fern.log` and `exit-code` (`0`) are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-refuses-component-link-ref` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `unresolved-reference: paths//parcels/post/responses/200/links/ReadParcel: #/components/links/ReadParcel`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

As R14: `src/document_refusals.rs` no longer walks a Response Object's `links`.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `document_refusals::tests::response_links_refuse_nothing_but_a_response_ref_still_does`.
