# request-property-name-collision

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe generates, imports, and reports zero mypy errors under its generated pyproject configuration. It sends PATCH /repos/original with body {"name":"new"} and parses the 204 response as None. However, the path parameter is emitted as name_, adding a suffix absent from the document. The required identifier bar fails.
[generate](evidence/request-property-name-collision.generate.log), [import](evidence/request-property-name-collision.import.log), [mypy](evidence/request-property-name-collision.mypy.log), [wire](evidence/request-property-name-collision.wire.log)

Retrievable population representative `b647ad473786da2dc733e115a1066da8c0485e2f6be78e85f54bf615a6140f90` (source locator in generation log):
The Irrigator representative exits 1 before producing a package. Import, mypy and a send/parse journey are unavailable; that independently fails the required bar.
[generate](evidence/b647ad473786da2dc733e115a1066da8c0485e2f6be78e85f54bf615a6140f90.generate.log)

Pinned Fern refuses a name shared by a [path parameter and body property](evidence/request-path.pinned-fern.log),
including a [referenced body](evidence/request-reference.pinned-fern.log),
but accepts the tested [query/body](evidence/request-query.pinned-fern.log) and
[header/body](evidence/request-header.pinned-fern.log) pairs.
It accepts [duplicate query declarations](evidence/same-parameter-query-query.pinned-fern.log)
and refuses parameters in [different locations](evidence/same-parameter-query-header.pinned-fern.log).
Cross-location pairs with the same wire spelling belong to the normalization
class; differently spelled names such as X-Namespace and namespace belong to
this exact-name class. Repeated
properties within an expanded request body also belong to this exact-name class.

All 296 retrievable population documents refuse under strict mode with no
output: [population measurements](evidence/population-strict.log). The log
combines the initial population pass with fresh checks of its two misses after
handling X-prefixed headers and a name collision hidden by a malformed nullable
flag. The malformed flag is not repaired; source validation retains the measured
name refusal before returning to the typed parser's other errors.
