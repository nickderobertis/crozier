# Unsuitable discriminant names

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. The population carries the class on 13 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses 13 of the 13 retrievable ones under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

**Narrowed at this pair to mappings of references.** A discriminator whose
`mapping` names a target by bare schema name is `typing.Any` to Fern, which
never reads its discriminant: the class's bare-name controls generate, and so do
three real documents whose `$_type` or `@odata.type` crozier used to refuse.
crozier no longer refuses that shape. Every shape a mapping of references
spells, the probes `shapes.tsv` measures, is refused as before, and all 13
retrievable population documents still exit 1 in both modes. The root cause,
the repair and each document's outcome are recorded in
[`../../fern-measurements/refusal-parity/README.md`](../../fern-measurements/refusal-parity/README.md).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**;
no generator repair is made.

The probe generates and imports. It preserves the declared `_t` wire alias,
parses an `ImageAsset` with its width, and serializes that same selector value.
The Python field is `t`. However, mypy 1.13.0 under the generated project's own
configuration reports **2 errors** at the response union's `parse_obj_as` calls.
The zero-error requirement fails. Logs:
[generation](evidence/discriminant-value-unsuitable.generate.log),
[import](evidence/discriminant-value-unsuitable.import.log),
[mypy](evidence/discriminant-value-unsuitable.mypy.log),
[wire](evidence/discriminant-value-unsuitable.wire.log).

One retrievable population representative from Rapidata,
`6940ddab47fc670434d92fbc949ad63a25438530e502f66f732d829fc89858fd`,
generates but fails to import all SDK modules, and reports **48 mypy errors**
under its own configuration. Its offending discriminant cannot be driven through
an importable, type-correct SDK; no successful send/parse claim is made for that
package. The immutable source locator is in its generation log:
[generation](evidence/6940ddab47fc670434d92fbc949ad63a25438530e502f66f732d829fc89858fd.generate.log),
[import](evidence/6940ddab47fc670434d92fbc949ad63a25438530e502f66f732d829fc89858fd.import.log),
[mypy](evidence/6940ddab47fc670434d92fbc949ad63a25438530e502f66f732d829fc89858fd.mypy.log).

Pinned Fern controls refuse an
[underscore-led](evidence/underscore.fern-check.log),
[hyphenated](evidence/hyphen.fern-check.log), or
[digit-led](evidence/digit.fern-check.log) discriminant, and accept
[`kind_name`](evidence/valid.fern-check.log). The detector uses that measured
identifier grammar on the document's discriminant property name.

The same check covers inferred selectors and explicit mapping-only selectors,
using the generator's existing selector inference without changing it.
All 13 retrievable population documents refuse in strict mode before any file
is written: [population run](evidence/population-strict.log).

An accepted neighboring shape is retained: [pinned Fern control](evidence/discriminant-anyof.pinned-fern.log).

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/digit.fern-check.log`](evidence/digit.fern-check.log)
- [`evidence/discriminant-anyof.pinned-fern.log`](evidence/discriminant-anyof.pinned-fern.log)
- [`evidence/hyphen.fern-check.log`](evidence/hyphen.fern-check.log)
- [`evidence/underscore.fern-check.log`](evidence/underscore.fern-check.log)
- [`evidence/valid.fern-check.log`](evidence/valid.fern-check.log)
