# Witness search: annotated `$ref` to an inheritance-spelled union

The real-specification search for `annotated-ref-target-inheritance-union`, the
key of `prop_type_ref`'s case 3c: a property that annotates a `$ref` through
`allOf` whose target is the base of an inheritance-style discriminated union
(a `discriminator` whose `mapping` names the subtypes that `allOf` it, and no
`oneOf` or `anyOf` of its own). The arm was added by the
[#617](https://github.com/nickderobertis/crozier/issues/617) repair, measured in
[`617-annotated-inherited-union`](../../fern-measurements/output-defects/617-annotated-inherited-union/README.md).

## The search

The selector is the census's own,
`schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.discriminator:inheritance-union`,
and the search was bounded by the manager's ruling for this key to two
document sets already on the host, with no new GitHub query:

- **Every registered corpus source** (270: 31 original fixtures, 239 corpus
  sources), by `just surface-census --selector <selector>`: declared by no
  registered source.
- **The APIs.guru `openapi-directory` snapshot at `f04b8d0`** already acquired
  by the discriminator search: its 19 documents, censused with `--fixtures-root`.
  Seven declare the target shape on its own (`schema.discriminator:inheritance-union`:
  `apple.com/sirikit-cloud-media` 8, `just-eat.co.uk` 1, `microsoft.com/graph-beta`
  340, `microsoft.com/graph` 136, `rebilly.com` 43, `twitter.com/current` 2,
  `viator.com` 1) and one declares annotated `$ref` properties
  (`digitalocean.com` 13), but none declares the conjunction: no annotated
  `$ref` in any of them names an inheritance-union base.

No candidate was found, so none is outstanding, and the row is `handwritten`
on [`glaze-ledger-coats`](../handwritten/glaze-ledger-coats/), the from-scratch
document of the #617 measurement.

| key | outcome | search | note |
|---|---|---|---|
| `annotated-ref-target-inheritance-union` | `exhausted` | registered corpus: 0 of 270 sources declare it; APIs.guru `f04b8d0` snapshot: 0 of 19 documents declare it | bounded to the host's document sets; no GitHub query was made |
