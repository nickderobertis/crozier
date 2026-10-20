# type-name-not-letter-led

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. The population carries the class on 6 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses 6 of the 6 retrievable ones under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under its own generated pyproject configuration. Its id field parses and serializes exactly, but the schema 123456 becomes One23456, adding a prefix absent from the document and making the public identifier misleading.
[generate](evidence/type-name-not-letter-led.generate.log), [import](evidence/type-name-not-letter-led.import.log), [mypy](evidence/type-name-not-letter-led.mypy.log), [wire](evidence/type-name-not-letter-led.wire.log)

Retrievable population representative `2708ffbb889404d788cffc6da58c1b283f7e1a301931136806c432b40afab6ab` (source locator in generation log):
The representative fails import and reports 12 mypy errors under its own generated pyproject configuration. A valid typed send/parse journey is unavailable; this independently fails the required bar.
[generate](evidence/2708ffbb889404d788cffc6da58c1b283f7e1a301931136806c432b40afab6ab.generate.log), [import](evidence/2708ffbb889404d788cffc6da58c1b283f7e1a301931136806c432b40afab6ab.import.log), [mypy](evidence/2708ffbb889404d788cffc6da58c1b283f7e1a301931136806c432b40afab6ab.mypy.log)

All 6 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: [type-led-digit-word.pinned-fern](evidence/type-led-digit-word.pinned-fern.log), [type-led-name-override.pinned-fern](evidence/type-led-name-override.pinned-fern.log), [type-led-punctuation.pinned-fern](evidence/type-led-punctuation.pinned-fern.log), [type-led-type-override.pinned-fern](evidence/type-led-type-override.pinned-fern.log), [type-led-underscore.pinned-fern](evidence/type-led-underscore.pinned-fern.log).

The numeric boundary is measured: [9999 is accepted](evidence/type-numeric-9999.pinned-fern.log), [10000 is refused](evidence/type-numeric-10000.pinned-fern.log), and [leading zeroes alone do not trigger it](evidence/type-numeric-00001.pinned-fern.log). The empty-name population uses [object references to legacy definitions](evidence/object-type-ref-definitions.pinned-fern.log), [webhook-local object references](evidence/object-type-ref-webhook.pinned-fern.log), or [unavailable relative component aliases](evidence/component-type-ref-relative.pinned-fern.log). Direct response relative references and component-local definitions are accepted controls. Available relative files continue through the existing loader.

A declared type name (`x-fern-type-name` or `x-crozier-type-name`) replaces the
key Fern checks, so a hinted `123456` generates as its declared name (the
authored probe
[`376-350-declared-type-name`](../../openapi-surface/authored-probes/376-350-declared-type-name/)).
A blank declaration declares nothing: Fern falls back to the key and refuses it
([probe](evidence/376-350-declared-type-name-blank-digit-led.yml),
[pinned Fern](evidence/376-350-declared-type-name-blank-digit-led.pinned-fern.log)),
and crozier refuses it in both modes, naming `123456`.

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/component-type-ref-defs.pinned-fern.log`](evidence/component-type-ref-defs.pinned-fern.log)
- [`evidence/component-type-ref-local.pinned-fern.log`](evidence/component-type-ref-local.pinned-fern.log)
- [`evidence/component-type-ref-relative.pinned-fern.log`](evidence/component-type-ref-relative.pinned-fern.log)
- [`evidence/object-type-ref-definitions.pinned-fern.log`](evidence/object-type-ref-definitions.pinned-fern.log)
- [`evidence/object-type-ref-defs.pinned-fern.log`](evidence/object-type-ref-defs.pinned-fern.log)
- [`evidence/object-type-ref-ordinary.pinned-fern.log`](evidence/object-type-ref-ordinary.pinned-fern.log)
- [`evidence/object-type-ref-relative-definitions.pinned-fern.log`](evidence/object-type-ref-relative-definitions.pinned-fern.log)
- [`evidence/object-type-ref-relative-defs.pinned-fern.log`](evidence/object-type-ref-relative-defs.pinned-fern.log)
- [`evidence/object-type-ref-relative.pinned-fern.log`](evidence/object-type-ref-relative.pinned-fern.log)
- [`evidence/object-type-ref-response-short.pinned-fern.log`](evidence/object-type-ref-response-short.pinned-fern.log)
- [`evidence/object-type-ref-response.pinned-fern.log`](evidence/object-type-ref-response.pinned-fern.log)
- [`evidence/object-type-ref-unknown.pinned-fern.log`](evidence/object-type-ref-unknown.pinned-fern.log)
- [`evidence/object-type-ref-webhook.pinned-fern.log`](evidence/object-type-ref-webhook.pinned-fern.log)
- [`evidence/type-led-digit-word.pinned-fern.log`](evidence/type-led-digit-word.pinned-fern.log)
- [`evidence/type-led-name-override.pinned-fern.log`](evidence/type-led-name-override.pinned-fern.log)
- [`evidence/type-led-punctuation.pinned-fern.log`](evidence/type-led-punctuation.pinned-fern.log)
- [`evidence/type-led-type-override.pinned-fern.log`](evidence/type-led-type-override.pinned-fern.log)
- [`evidence/type-led-underscore.pinned-fern.log`](evidence/type-led-underscore.pinned-fern.log)
- [`evidence/type-numeric-0.pinned-fern.log`](evidence/type-numeric-0.pinned-fern.log)
- [`evidence/type-numeric-00001.pinned-fern.log`](evidence/type-numeric-00001.pinned-fern.log)
- [`evidence/type-numeric-1.pinned-fern.log`](evidence/type-numeric-1.pinned-fern.log)
- [`evidence/type-numeric-10000.pinned-fern.log`](evidence/type-numeric-10000.pinned-fern.log)
- [`evidence/type-numeric-10001.pinned-fern.log`](evidence/type-numeric-10001.pinned-fern.log)
- [`evidence/type-numeric-12345.pinned-fern.log`](evidence/type-numeric-12345.pinned-fern.log)
- [`evidence/type-numeric-9999.pinned-fern.log`](evidence/type-numeric-9999.pinned-fern.log)
- [`evidence/type-ref-definitions.pinned-fern.log`](evidence/type-ref-definitions.pinned-fern.log)
- [`evidence/type-ref-defs.pinned-fern.log`](evidence/type-ref-defs.pinned-fern.log)
- [`evidence/type-ref-ordinary.pinned-fern.log`](evidence/type-ref-ordinary.pinned-fern.log)
- [`evidence/type-ref-response.pinned-fern.log`](evidence/type-ref-response.pinned-fern.log)
