# Enum values that cannot be named

Evaluated on baseline `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`, before
adding detectors. Decision: **refuse**. No generator repair is made.

The probe generates, imports, and reports zero mypy errors under its generated
`pyproject.toml` (mypy 1.13.0, including the declared optional dependencies).
Its response parses `10080` and serialization preserves `10080`, but its
identifiers `_10080` and `_20160` add leading underscores absent from the
values. That fails the identifier criterion, despite correct wire values.
See the committed [generation](evidence/enum-value-unnameable.generate.log),
[import](evidence/enum-value-unnameable.import.log),
[mypy](evidence/enum-value-unnameable.mypy.log), and
[wire](evidence/enum-value-unnameable.wire.log) logs.

Three retrievable population documents, selected from different publishers,
confirm a further failure. Their generated packages cannot import the offending
enum types: distinct declared values collapse to `_`. Consequently no request or
response at that element can run; the declarations are neither independently
sendable nor parseable. The import logs enumerate the actual duplicate member
and its original wire value. The mypy runs use each generated project's own
configuration, without additional flags or suppressions.

| Population digest | Import | Mypy errors | Evidence |
| --- | --- | --- | --- |
| `6cfc658fe510e051684d34217dfa4fc0745e19097440a3337cd08fea5b10a90e` (PSO2 API) | fails: duplicate `_` | 3 | [generation](evidence/6cfc658fe510e051684d34217dfa4fc0745e19097440a3337cd08fea5b10a90e.generate.log), [import](evidence/6cfc658fe510e051684d34217dfa4fc0745e19097440a3337cd08fea5b10a90e.import.log), [mypy](evidence/6cfc658fe510e051684d34217dfa4fc0745e19097440a3337cd08fea5b10a90e.mypy.log) |
| `4df76002aa2b8542828b72e27c60edd1133800d391c92721cdad90f5e49175cf` (Body Sheet) | fails: duplicate `_` | 8 | [generation](evidence/4df76002aa2b8542828b72e27c60edd1133800d391c92721cdad90f5e49175cf.generate.log), [import](evidence/4df76002aa2b8542828b72e27c60edd1133800d391c92721cdad90f5e49175cf.import.log), [mypy](evidence/4df76002aa2b8542828b72e27c60edd1133800d391c92721cdad90f5e49175cf.mypy.log) |
| `f57ffad87f0ea2e4a14ba030f7d24c5c5dbcd285805400c3d01433e26927e35f` (KOSCOM) | fails: duplicate `_` | 16 | [generation](evidence/f57ffad87f0ea2e4a14ba030f7d24c5c5dbcd285805400c3d01433e26927e35f.generate.log), [import](evidence/f57ffad87f0ea2e4a14ba030f7d24c5c5dbcd285805400c3d01433e26927e35f.import.log), [mypy](evidence/f57ffad87f0ea2e4a14ba030f7d24c5c5dbcd285805400c3d01433e26927e35f.mypy.log) |

The generation logs record immutable source locators; `documents.tsv` supplies
their revisions and measured Fern diagnostics. These copies were available in
the host's digest-indexed cache; no Postman or SwaggerHub request was made.

The enum-value detector, measured before the other names detectors were added,
refuses all **331/331** retrievable population documents
under `fern-strict`, exits 1, writes no files, and names the class, offending
element and strict mode in each diagnostic: [population log](evidence/population-strict.log).
Integer enums and mixed-kind enums remain scalar aliases, as Fern's accepted
Bungie golden requires. A single `UNDEFINED` member remains accepted, as Fern's
People Data Labs golden requires. Invalid name overrides cannot rescue a refused
value: Fern warns and falls back to the wire value, measured with the pinned CLI
([override log](evidence/override-fallback.fern.log)).

Pinned controls distinguish non-ASCII unnameable values
([CJK](evidence/cjk.fern-check.log), [emoji](evidence/emoji.fern-check.log))
from punctuation, which is classified as `enum-name-unsuitable`.
