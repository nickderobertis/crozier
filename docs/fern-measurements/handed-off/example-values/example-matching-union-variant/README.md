# `example-matching-union-variant`

The handed-off root cause `example-matching-union-variant` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /seals/verify` posts `seal: oneOf [WaxSeal, StampSeal]`, discriminated by single-member `format` enums, exampled as a stamp; `POST /logbooks/verify` posts `entry: oneOf [EntryV1, EntryV2]`, undiscriminated, whose example's nested `page` fits only `EntryV2` (dcp-ai's `signed_bundle`). The same tagged-member rule is measured where the union is a map's value (`POST /shelves/stock`), where each member's tag is a `$ref` to a one-member enum component (`POST /badges/verify`) and where the body is a `$ref` component exampled through a named `examples` entry (`POST /seals/register`). `POST /charms/verify` and `POST /charms/inspect` example a `charm` member, `CharmSeal`, which requires an unknown (`{}`) field `charm`, the first with that field given and the second without it (nussknacker's `TypedObjectWithValue`, requiring `value: {}`).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/example-matching-union-variant` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the same document generated with `enum_type` unset (the `literals` mode), reduced to an overlay of `fern-expected/` (the files that differ, and `.crozier-overlay.json` naming the files Fern omits); its `cases.tsv` row is `handed-off/example-values/example-matching-union-variant/expected-literals`.

## The comparison

The certified pair builds the variant the example fits: `…Seal_Stamp(stamp_id="stamp_id")` (placeholders, as a discriminated example is built) and `EntryV2(page=PageV2(…keeper="Morwenna"…))`; crozier built the first variant of each. It builds the tagged member in the map value, `$ref`-tag and named-`examples` shapes too (`StockShelfRequestShelfValue_Stamp`, `VerifyBadgeRequestBadge_Copper`, `SealRegistrationSeal_Stamp`). For the `charm` examples it builds the union's first member instead (`VerifyCharmRequestToken_Wax(colour="colour")`, `InspectCharmRequestToken_Wax(…)`), which crozier then got wrong, writing `…_Charm(charm={"key": "value"}, motto="motto")`.

**Verdict: `parity-gap-repaired`.** `emit::ExampleCtx::union_value_from_example` builds the tagged member, unless that member requires an unknown field, where it builds the union's first member as a synthesized example does; an object's example check now recurses into its fields; crozier byte-matches `fern-expected/` and the `expected-literals/` overlay.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/` and its literals tree with `expected-literals/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`, `handed_off_example_value_literals_overlays_match_fern`); the `emit` unit tests `a_discriminated_example_builds_the_member_its_tag_names` and `a_tagged_member_requiring_an_unknown_field_is_worked_as_the_first` assert the lines.
