# Withdrawal remainder search

## Bound and inputs

This search reads the four source shapes left by the
[Nexmo withdrawal](../withdrawn-witnesses/nexmo-conversation.md#the-reach-row-223-alone-carried).
The census selectors describe declarations, not a claim that an emitted line
has executed. The controls in `WithdrawnWitnessSelectorTests` read the actual
`ref-pointer-walk/openapi.yml`, distinguish copied references from ordinary
ones, and distinguish plain timestamps from quoted, temporal, required and
header examples.

[census.tsv](census.tsv) records the offline walk of all 336 acquired source
identities in the current registry, including the original authored fixtures;
none failed to parse. Authored fixtures are controls, not real candidates.
Seven additional handed-off documents were recovered from the preflight cache
by matching their exact SHA-256 against `handed-off/documents.tsv`. The eighth
is Cyoda, fetched through `witness-acquire-github.py` and its rate-limit guard:
`Cyoda/cyoda-go:docs/cyoda/openapi.yml` at
`0021e97806811b369a13d87701fe4a6454ac99fa`, SHA-256
`5ce9d61397d9e296c2de0644bfe07bb90bf500e81f5472a8773f5fddcb9432b9`.
Its bytes match the handoff. The other 139 handoff hashes were not recovered
from that cache; some overlap registered sources, but this walk does not claim
complete coverage of the handoff population.

The planner confirmed that neither the retained APIs.guru archive extraction
at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` nor the acquired GitHub and
Sourcegraph `candidate-documents.json` pools exists on this host, and directed
that these populations not be reacquired. The committed
`witness-search-clients-extensions/apis-guru-census.tsv.gz`,
`apis-guru-gap-witnesses.tsv` and `apis-guru-publisher-provenance.tsv` retain
older selectors and provenance, not the bytes or the four new readings. They
cannot be used to infer a zero for a new selector. These missing inputs leave
each bound incomplete. No live code search was run and no new corpus row is
registered here.

## Verdicts

| key | selector | verdict | reason |
|---|---|---|---|
| `withdrawn-properties-reference-copy` | `schema.$ref:properties-copy` | `search-incomplete` | Three registered sources declare the broader copying predicate; their pointers end on properties or items, not the withdrawn plain component or composition-member forms. The retained archive and acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-properties-copy-variant-name` | `schema.oneOf:properties-copy-type-variant` | `search-incomplete` | No declarer in the inputs read. The retained archive and acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-properties-copy-inferred-type` | `schema.oneOf:properties-copy-inferred-type` | `search-incomplete` | No declarer in the inputs read. The retained archive and acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-optional-nontemporal-timestamp` | `parameter.example:optional-nontemporal-yaml-timestamp` | `search-incomplete` | No real witness found. No declarer in the inputs read, including the pinned Cyoda document. The retained archive and acquired pools are unavailable, and the handoff walk is partial. |

The broader reference-copy selector counts `dnd5eapi.co` (2),
`openbanking-brasil-directory` (1), and `embedpdf-cloudpdf` (1160).
The handed-off `ogcincubator/developer-website-v3` document contributes one
more declaration. A broader pointer-copy declaration does not establish the
withdrawn union naming and inferred-tag behaviours.

**No real specification is known here to witness the optional non-temporal
YAML-timestamp drop.** Cyoda's unquoted parameter timestamps have
`format: date-time`, as the
[certified example-value measurement](../../fern-measurements/handed-off/example-values/yaml-timestamp-parameter-example/README.md)
already records. They are temporal and do not satisfy the selector. This
search does not override the timestamp ruling or that measurement.
