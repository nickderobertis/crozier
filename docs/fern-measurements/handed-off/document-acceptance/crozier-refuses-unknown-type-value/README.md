# crozier-refuses-unknown-type-value

Root cause `crozier-refuses-unknown-type-value` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A `type` list holding an entry that is not a string (`type: [string, false]`), beside `type` names crozier does not know (`int`, `list`, `positive number or null`).

## The measurement

`openapi.yml` declares a battery whose `relayState` is `type: [string, false]`. It was authored from scratch for this measurement (SHA-256 `70dda9dfe9c71c4dce32c7b1d047633bcb30b63ca2994bc9b6b93a7f31f3c038`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `9e46a634c19f032beddc0fb5ea56de835581b296348a24158beb21949705aee6`. `fern.log` and `exit-code` (`0`) are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-refuses-unknown-type-value` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `could not parse OpenAPI document: `data did not match any variant of untagged enum TypeField``.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/openapi.rs`'s `TypeField` deserializer keeps a non-string entry as its JSON spelling (`"false"`), an unknown type name, so the list stays the two-member union the certified pair hoists: `BatteryRelayState = typing.Union[str, typing.Any]`. Unknown single names were already `typing.Any`, as the certified pair types them. The record's document (OLeier's VRM API) is the certified pair's own refusal at this node's base: its parse fails on a `#/paths/…` parameter reference (`Failed to resolve #/paths/~1users~1me/get/parameters/0`, exit 0 over the empty scaffold), which crozier refuses as `unresolved-reference` too.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `openapi::document_acceptance_tests::a_non_string_type_entry_is_kept_as_an_unknown_type_name`.
