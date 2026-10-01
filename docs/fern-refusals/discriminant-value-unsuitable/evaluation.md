# Unsuitable discriminant names

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
