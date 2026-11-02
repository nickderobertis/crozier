# R14

Root cause `R14` of the [operations-and-extensions record](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A response `links` entry that is a `$ref` to a `components/links` entry the document does not declare.

## The measurement

`openapi.yml` creates a parcel whose `200` response carries `links: {ReadParcel: {$ref: '#/components/links/ReadParcel'}}`, and declares no `components/links` at all. It shares its rule with [`crozier-refuses-component-link-ref`](../crozier-refuses-component-link-ref/README.md), whose document declares the link; the two certified-pair trees are byte-identical (same digest), because the certified pair ignores response links either way. It was authored from scratch for this measurement (SHA-256 `68a66b5edf38b080068b25e0db4b9e26731da597109349115648eb91663cfd89`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `b614ae8b9a1c37c820329dfbb9ec5d4cd3263b852d9d9d9a01ec1b421556c677`. `fern.log` and `exit-code` (`0`) are that run's.

`cases.tsv` admits only lower-case case names, so this tree is regenerated in the same workspace by hand, as `docs/openapi-surface/probes/AGENTS.md` describes, or by copying `crozier-refuses-component-link-ref/fern-expected/`, which the certified pair writes byte for byte the same.

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `unresolved-reference: paths//parcels/post/responses/200/links/ReadParcel: #/components/links/ReadParcel`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/document_refusals.rs`'s reference walk no longer descends into a Response Object's `links` (`response_object_element`), so no Link Object `$ref` refuses the document; crozier writes nothing from links, as the certified pair writes nothing.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `document_refusals::tests::response_links_refuse_nothing_but_a_response_ref_still_does`.
