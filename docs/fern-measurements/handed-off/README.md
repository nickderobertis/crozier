# Handed-off measurements

The source records define the root causes:
[bodies and paths](../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md),
[operations and extensions](../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md),
and [schemas](../../openapi-surface/witness-search-fixture-only-schemas/README.md).

Each area is a tab-separated file with a header and exactly these columns,
in order: `source`, `root_cause`, `verdict`, `measurement`, `departure`, `note`.
`source` names the source record or follow-up ticket; `root_cause` preserves
its spelling (including numbered `R7`-style causes). `measurement` names the
repository-relative measurement directory; `departure` names its catalog entry,
or `-`; `note` states the measured rule on one line.

The closed verdict set is `parity-gap-repaired`, `already-matching`,
`fern-defect-departed`, `user-ruling`, `default-matched`,
`ruling-applied:<ruling id>`, and `refusal-kept`. A `user-ruling` note names
the ruling; `ruling-applied:<ruling id>` applies that ruling's principle to
a different cause. Every verdict is decided.

The area records are [bodies and media](bodies-media.tsv),
[client structure](client-structure.tsv),
[document acceptance](document-acceptance.tsv),
[empty SDK documents](empty-sdk-documents.tsv),
[example values](example-values.tsv),
[snippet rendering](snippet-rendering.tsv),
[type declarations](type-declarations.tsv), and
[union modelling](union-modelling.tsv).

## Newly admitted documents

No documents have been registered by this reconciliation yet.
