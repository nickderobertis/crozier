# extension-reference-cycle: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. Its 11 probe and 12 control shapes are measured at this pair too ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): a `-probe` is a shape Fern refuses, a `-control` one it generates from, and each `evaluation-logs/fern-<shape>.log` holds that measurement. The population carries the class on 2 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses both under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

What moved: The shapes the older naming filed as controls but Fern refuses are probes; none changed verdict. An extension reaching its reference through an array (`x-link: {oneOf: [...]}`, Stripe's `x-expansionResources`) generates on a field or a schema root (`field-oneof-link`, `root-oneof-link` and `expandable-field` controls); through an object member it is still refused, on a union field too (`union-field-link` probe). crozier now follows an extension's references through object members only, so the twelve Stripe documents it refused with this class are refused with `example-type-mismatch`, the class Fern reports for them ([`dispositions.tsv`](../dispositions.tsv)).

**Ruling `empty-sdk-refused` (the user's design review, 2026-11-01).** crozier
refuses, in default and `fern-strict` modes, every document the certified pair
turns into an empty SDK, because an empty SDK is useless and crozier refuses
rather than writes one. This is an intended departure from the pair's exit 0,
recorded under [Intended departures](../README.md#intended-departures). Both
of this class's documents are Stripe's SDK descriptions, and crozier refuses
both in both modes, as the bodies-and-paths record's
[false successes](../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md#the-certified-pairs-false-successes)
list.

**The valid-OpenAPI exception: lolesports.** The pair prints this class's
phrase, `Maximum call stack size exceeded`, over a document that has no
extension cycle: `vickz84259/lolesports-api-docs`'s `openapi.yaml` at
`74027a7950c7e4629d3cab01ddd3990457a9956d` (SHA-256
`5737ba80e2e41e0bdf0f3e9079dcd757c16553d3f120b3f6d8bba6f3dc782d9c`). Its stack
is the pair's example builder (`buildExampleHelper`) recursing through
`navItem.parentNavItem`. That property is required, and it is an `allOf` of
`navItem` itself and a nullable object. The document is valid OpenAPI, so the
empty SDK is only a Fern limitation. crozier's SDK for it passes evaluation:
`fern-refusals.py evaluate-sdk` ran validation, default and strict generation,
a wheel build, a fresh installation and an import of every generated module
([receipt](../../fern-measurements/handed-off/empty-sdk-documents/R1/lolesports-sdk-evaluation.json)).
By the refusal rule's exception and the ruling, lolesports keeps generating in
both modes.

crozier's `extension-reference-cycle` detector does not fire on it: no
extension is involved. The from-scratch probe of the shape and its measurements
are [`R1`](../../fern-measurements/handed-off/empty-sdk-documents/R1/README.md).
The pair writes the empty SDK for the probe and generates its control, where
the property is optional.

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), and mypy
reports zero errors. `Node.x-link.target` refers back to `Node`; this is
extension metadata, while the declared wire object has only `id`. The
[public model journey](evaluation-logs/probe.wire.log) serializes `{id: A}`
and parses its unchanged `id`. The document declares no HTTP endpoint, so
this model boundary is the available sending/parsing interface.

One representative, [Stripe's SDK description,
`92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a`](evaluation-logs/population.log),
cannot import its root client: a generated `application_fee_fee_source` module
is missing. Mypy reports **60 errors in 11 files**. The offending
`POST /v2/core/account_links` request's `account` string carries
`x-stripeProperty.referenced_resource`, referring to `v2.core.account` and
participating in a metadata-reference cycle. The [public client boundary](evaluation-logs/population.wire.log)
fails on import, so no client can send or parse that account field; no request
is sent and no response returned. This class is `refuse` because the population
package fails, although the small probe's crozier output works. Both population
documents come from this same Stripe publisher.

Fern's [probe record](fern-refusal.txt) is a false success: check and generation
exit 0 despite `Maximum call stack size exceeded`, and its 35-file output comes
from a document it never parsed. Pinned runs reproduce this for
[another extension key](evaluation-logs/fern-other-extension.log) and
[a two-schema metadata cycle](evaluation-logs/fern-two-schema-cycle.log).
They accept [ordinary schema recursion](evaluation-logs/fern-ordinary-recursion.log),
[an acyclic extension reference](evaluation-logs/fern-acyclic-extension.log),
and [a metadata edge with an ordinary property return edge](evaluation-logs/fern-ordinary-return-edge.log).
The detector follows extension references between their targets, leaving
ordinary Schema Object references to the normal loader. The CLI recovery
journey preserves the accepted cases, compares output bytes in both modes,
and covers an ignored source schema.

The [population refusal log](evaluation-logs/population-refusals.jsonl)
covers both retrievable documents in both modes: exit 1, no files, one line
identifying the class and `x-stripeProperty`, with `fern-strict` as the
strict-mode cause. A preserved detector build makes the measurement independent
of assertion-witness rebuilds.

The [CLI assertion fails with only the cycle check disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 37 files for the probe instead of refusing. This deliberately records
an induced earlier state; the finished source restores the check.

The corpus comparison exposed an overbroad cycle refusal on Bungie's field
metadata. Its [pinned full-document check](evaluation-logs/fern-bungie-full.check.log)
passes without a parser failure. Pinned reduced controls distinguish direct
references on Property Object extensions: Fern accepts
[integer mapped fields](evaluation-logs/fern-field-mapped.log),
[another extension key on an integer field](evaluation-logs/fern-field-direct-link.log),
[object fields](evaluation-logs/fern-field-object-mapped.log),
[string fields](evaluation-logs/fern-field-string-mapped.log),
[qualified schema names](evaluation-logs/fern-qualified-field.log), and
[unsigned fields](evaluation-logs/fern-unsigned-field.log).
It still reports parser stack failures for direct extensions on a
[schema root](evaluation-logs/fern-direct-link.log),
[a mapped schema root](evaluation-logs/fern-direct-mapped.log),
[a Stripe extension on a root](evaluation-logs/fern-direct-stripe.log),
[a qualified root](evaluation-logs/fern-qualified-root.log),
and nested references on [integer](evaluation-logs/fern-field-integer.log),
[string](evaluation-logs/fern-field-string.log) or
[boolean](evaluation-logs/fern-field-boolean.log) fields.
The corrected detector exempts direct extension Reference Objects on schema
properties; it keeps nested references and schema-root extensions in the cycle
check. The CLI controls preserve each accepted SDK's bytes between modes.
Remeasured with the corrected detector, both population documents still
refuse in both modes with the unchanged lines in the population refusal log:
Stripe's `x-stripeProperty` nests its reference under `referenced_resource`.

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evaluation-logs/fern-bungie-full.check.log`](evaluation-logs/fern-bungie-full.check.log)
