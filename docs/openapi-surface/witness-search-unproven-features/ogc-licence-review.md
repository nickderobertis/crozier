# OGC licence review

The census recognizer reads `OGC License` as naming no grant it admits. That
is a recognizer outcome, not a reading of the grant, so the grant was read by
hand before any OGC-licensed candidate was excluded from this search.

The documents declare `http://www.opengeospatial.org/legal/` or
`https://www.ogc.org/legal/`, which resolves to
`https://www.ogc.org/about/legal-notices-term-and-conditions/` and links the
[document licence agreement](https://www.ogc.org/about/policies/document-license-agreement/)
(fetched once through `tools/witness-search/rate_limit_guard.py` into the shared
cache; response body SHA-256
`3b92b64f83ba21945b1e939a205358ef1261688bdd2f2e9a179ca86a34f3cdef`).
`opengeospatial/ogcapi-records` carries the same agreement as its pinned
`LICENSE`.

The agreement grants the rights to "copy, modify, merge, publish, distribute,
and/or sublicense", but on termination the licensee must "destroy or cause to
be destroyed" every copy, "whether held by you or by any third party". A public
repository cannot recall the clones and package downloads of everyone who has
fetched it, so it cannot meet that condition. Under
[the corpus rule](../../corpus-licensing.md), a grant conditioned on terms the
repository cannot meet is not admissible, so every OGC-licensed candidate in
[`remaining-bounds.tsv`](remaining-bounds.tsv) is excluded. The recognizer and
the corpus rule are unchanged.
