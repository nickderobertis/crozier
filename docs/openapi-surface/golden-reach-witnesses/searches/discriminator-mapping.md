# Arm search: `discriminator-mapping`

The unreached handling site(s) searched for: `src/openapi.rs::collect_schema_refs[if let Some\(disc\) = &schema\.discriminator \{]`.
Read with: `schema.discriminator.mapping`.

No Contract B search ran for this arm, and none could find a witness for it.
The arm runs only under a generation setting, and the probe Contract B runs
every declarer through never sets one. So this record states the setting,
measures it, and says for each declared source why the source owes nothing. It
does not read `exhausted`, which would claim a search that did not happen. The
form is the manager's ruling to `cover-new-unreached-arm`, and `RankedBacklogTests`
checks each of its three parts against the tree.

### Configuration gate

| key | setting | gate | verdict |
|---|---|---|---|
| `discriminator-mapping` | `audiences` | `src/openapi.rs::filter_by_audience` | `config-gated` |

`collect_schema_refs` has two callers, `operation_schema_seed` and
`expand_schema_closure`. Both are called only from `filter_by_audience`, which
returns before either when no audience is configured. `src/lib.rs` passes it
the generator's `audiences` setting (`--audience`, `CROZIER_AUDIENCES` or
`crozier.yml`). With an audience set, the arm runs on any document whose kept
operations reach a schema carrying a `discriminator`, whether or not the
document labels its operations. Until commit `63c6be587`, `filter_ignored`'s
schema-closure prune called the closure walk too, on any document with an
ignore marker. That incidental reach is why this arm was counted reached before
the repair.

#### Measured gate

The hand-written fixture
[`discriminator-mapping-audience`](../../handwritten/discriminator-mapping-audience/)
is a minimal document with a `Pet` base schema whose `mapping` names the
subtypes `Cat` and `Dog`. The mapping is the only path to those subtypes, and
Fern 5.20.0 keeps them when generating for `public`. `just handwritten-reach`
measured an instrumented crozier run over it with its declared audience and
without one, into
[`handwritten-config-gates.tsv`](../../handwritten-config-gates.tsv):

| fixture | setting | regions executed | regions |
|---|---|---:|---:|
| `discriminator-mapping-audience` | `audiences=public` | 9 | 9 |
| `discriminator-mapping-audience` | — | 0 | 9 |

#### Each declared source

`tools/surface-census/golden-reach-search.py probe` runs every declarer through
`crozier generate` with no `--audience`, as 217 of the 220 golden tests are
run. So no document in any source can execute the arm under it, and each
source's candidate set is empty by construction. The selector was never walked
or queried for this key either. No committed census counts its declarers or any
document's audience labels. The files each line cites show that: no
`records.tsv` row names the key, no `enumeration.tsv.gz` document lists it among
its `matched_keys`, and `queries.tsv` holds no phrasing for it.

| source | probe setting | evidence the key was never walked or queried |
|---|---|---|
| `apis.guru` | none | `apis.guru/records.tsv`, `apis.guru/enumeration.tsv.gz` |
| `jentic` | none | `jentic/records.tsv`, `jentic/enumeration.tsv.gz` |
| `github-code-search` | none | `github-code-search/records.tsv`, `queries.tsv` |
| `github-publisher-trees` | none | `github-publisher-trees/records.tsv`, `github-publisher-trees/enumeration.tsv.gz` |
| `sourcegraph` | none | `sourcegraph/records.tsv`, `queries.tsv` |
| `vendor-portals` | none | `vendor-portals/records.tsv`, `vendor-portals/enumeration.tsv.gz` |

The three goldens generated with an audience, `audience-filter`,
`audience-filter-strict` and `ziptax-node`, declare no `discriminator`. The one
audience-labelled document among the query sources' locally cached results is
An excluded synthetic input, `screened-nonpublic-input:v2:2a9e147687d94da191ed78449f6ed061:1` at
`screened-nonpublic-input:v2:2a9e147687d94da191ed78449f6ed061:2`, declares no
`discriminator`. That cache is not committed, so this is supporting detail only.

**The real-specification route stays open.** A corpus row registered with an
audience over a document that declares a `discriminator` reaches this arm. No
row is registered that way yet, so the arm stays unreached by real
specifications. The fixture above covers it at the lower level of proof.

### Successor arms

`src/ir.rs::Builder::discriminated_union[if union_target \{]` and
`src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.wrapped => \{]`,
the union repair for the shape `nested-oneof-mapping-target-wrapped-as-value`,
joined this key after the gate above was recorded. Neither is behind a
generation setting: both run on any document whose `discriminator.mapping`
names a schema that is itself a `oneOf` or `anyOf` of references, and
`just handwritten-reach` measures the hand-written fixture below, which
declares no setting, executing 20 of 20 and 18 of 20 of their regions
([`handwritten-reach.tsv`](../../handwritten-reach.tsv)). So the
`config-gated` verdict above is the earlier site's alone, and these two arms
read `search-incomplete`. No Contract B search
has run for these two either. The bounded
[union witness search](../../witness-search-union-scenarios/README.md#witness-search) read the APIs.guru archive at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` and the already-acquired GitHub
code-search and Sourcegraph pools for the shape and screened its three
declarers, none registrable, so their search is `search-incomplete`; the
hand-written fixture
[`kitchen-nested-mapping-target`](../../handwritten/kitchen-nested-mapping-target/)
covers them at the lower level of proof.

