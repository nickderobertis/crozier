# Candidate ledger

`candidates.tsv` contains only documents confirmed to declare a key by that
key's census selector. It has no `securityscheme-ref` row: the branch-point
`securityScheme:$ref` selector is [unsupported by the census](../witness-search-keys.tsv),
so none of the four registry sources was evaluated for that key. The four
outstanding source segments are in [security.md](../security.md#witness-search-exhaustive).
Adding a candidate here requires a selector output over the parsed document;
an earlier keyword hit or another key's census output does not qualify.
