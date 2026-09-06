# Which licences the corpus admits

**This file is the only statement of the rule.** Every other document that needs
it links here rather than repeating it; a second enumeration of the admissible
licences anywhere else in the tree fails `just lint-corpus-licensing`, which is
part of `just check`. Prose that *refers* to the rule ("outside the admissible
set", "under a redistribution-compatible licence") is fine — a second **list of
licence names** is what drifts.

The rule governs which real-world OpenAPI documents may be registered in
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md), and so which
publishers' generated SDK output this repository redistributes as a committed
golden. `NOTICE` retains each registered document's own licence name beside its
source URL; the source documents themselves are fetched at generation time
rather than vendored (`decision` = `link-ok`).

## The rule

<!-- corpus-licence-set: the canonical enumeration. Do not copy it elsewhere. -->

**Admissible — any licence that grants redistribution**, permissive or copyleft:
Apache-2.0, MIT, the BSD family, CC0, GPL, AGPL, LGPL, MPL, EPL, CC-BY, CC-BY-SA,
CC-BY-ND, and other grants of that kind.

**Not admissible — a document that grants nothing.** One carrying neither an
`info.license` nor a repository `LICENSE`, and one whose licence is proprietary
or reported as `NOASSERTION`.

**Not admissible — a licence conditioning redistribution on terms this
repository cannot meet**, whatever else it grants.

## Why each half was decided that way

**Copyleft is in, deliberately.** A copyleft licence attaches conditions to
redistribution rather than withholding permission for it, and a repository that
vendors generated output alongside the document's own provenance can satisfy
them: the manifest row records the source URL, the pinned immutable ref, and the
licence name, and `NOTICE` carries the attribution. The earlier rule admitted
only permissive grants, which cost the corpus real, publisher-owned API
descriptions that Fern accepts — the shapes they alone declare were unanswerable
for no reason the licences themselves supplied. Widening is a decision about
what this project ships, so it is recorded here rather than inferred from which
documents happen to be registered.

**No-grant documents are out, deliberately** — it is a boundary, not an
oversight. With no `info.license` and no repository `LICENSE`, with a
proprietary licence, or with the licence reported as `NOASSERTION`, there is no
condition to satisfy: the default is all rights reserved, so redistributing the
generated output is not something the repository can make lawful by recording
provenance. Documents blocked on exactly this stay blocked after the widening.

**A grant this repository cannot honour is out too.** A licence may permit
redistribution only on terms a public, unpaid, single-maintainer repository
cannot meet — a revenue ceiling, a per-seat fee, a field-of-use restriction.
`CORPUS.md`'s `assemblyai-autosdk` row is the recorded instance.

## Rows screened before the widening

The narrower set is what the recorded screening outcomes under
[`openapi-surface/`](openapi-surface/) and in
[`fern-limitations.md`](fern-limitations.md) were measured against, and this
change moved the rule without reclassifying any of them. So a `witness-blocked`
row naming a copyleft licence was blocked by a rule that no longer says that,
and its settlement stands only until the row is rescreened. A row blocked on a
document that grants nothing is blocked by the rule as it now stands and stays
blocked — `dollar-anchor`'s `inkeep/chat-api-openapi-schema` (no licence
anywhere), `format-idn-email`'s `wttw/aboutmyemail` (no licence) and
`format-relative-json-pointer`'s `geo-engine/BioIS` (`NOASSERTION`) are the
worked examples.

Every candidate those records block on a licence has since been rescreened
against the rule as it now stands, one line each, in
[`licence-rescreening.md`](licence-rescreening.md) — which the widening admits,
what Fern does with it, and which coverage rows it would settle.

## Screening a candidate against it

Read the document's own `info.license` **and** the licence of the repository or
aggregation redistributing it; record both in the `CORPUS.md` row when they
differ (a `jentic/jentic-public-apis` redistribution is CC0-1.0 by the
aggregation even where the document declares its own). Where GitHub's API
reports `NOASSERTION` for a repository with no `info.license` in the document,
that is the no-grant case above.

The licence screen is one of three a candidate must clear; the other two —
Fern must accept the document, and the reference must be immutable — are in
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md).

## The drift gate

`scripts/corpus-licensing-drift.py` reads every tracked Markdown document in the
repository (the vendored Fern goldens and the generated `CHANGELOG.md` aside)
and fails when one outside this file enumerates the admissible licences again.
`just lint-corpus-licensing` runs it; `just test-corpus-licensing` proves it
still discriminates by planting such an enumeration and requiring the failure to
name it. Both are in `just check`.
