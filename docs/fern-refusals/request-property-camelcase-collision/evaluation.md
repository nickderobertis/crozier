# request-property-camelcase-collision

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. Its 1 probe and 1 control shapes are measured at this pair too ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): a `-probe` is a shape Fern refuses, a `-control` one it generates from, and each `evaluation-logs/fern-<shape>.log` holds that measurement. The population carries the class on 30 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses 30 of the 30 retrievable ones under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe exits 1 because ruff rejects duplicate account_id keyword arguments, and writes nothing. There is no generated package to import, type-check, send or parse. That fails the required bar.
[generate](evidence/request-property-camelcase-collision.generate.log)

Retrievable population representative `3e6a7110aa83d452089845e0ae696723318e3030308cdaae80acf4c7548b3f0c` (source locator in generation log):
The Eclipse Foundation representative generates and imports, but its own pyproject configuration reports 160 mypy errors. A type-correct send/parse journey cannot be established.
[generate](evidence/3e6a7110aa83d452089845e0ae696723318e3030308cdaae80acf4c7548b3f0c.generate.log), [import](evidence/3e6a7110aa83d452089845e0ae696723318e3030308cdaae80acf4c7548b3f0c.import.log), [mypy](evidence/3e6a7110aa83d452089845e0ae696723318e3030308cdaae80acf4c7548b3f0c.mypy.log)

All 29 retrievable population documents refuse under strict mode with no output: [run](evidence/population-strict.log). Validation includes implicit path placeholders and body properties as well as declared parameters.

Pinned Fern accepts deconflicting declared names on
[parameters](evidence/name-override-parameter.pinned-fern.log) and
[body properties](evidence/name-override-property.pinned-fern.log).
The detector respects those hints and canonical crozier precedence, including
hints behind local references. This makes no repair to baseline emitted code.

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/name-override-parameter.pinned-fern.log`](evidence/name-override-parameter.pinned-fern.log)
- [`evidence/name-override-property.pinned-fern.log`](evidence/name-override-property.pinned-fern.log)
