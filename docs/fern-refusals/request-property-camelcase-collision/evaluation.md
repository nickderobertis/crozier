# request-property-camelcase-collision

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
