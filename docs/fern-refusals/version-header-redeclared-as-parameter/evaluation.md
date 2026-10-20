# Version header also declared as a parameter: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. No document in the population carries the class, at this pair or at Fern CLI 5.67.1.

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

The [independently authored probe](probe.yml) has a document version extension
whose `header` is `X-Calibration-Revision`. The operation declares the same
header as a required ordinary parameter. The certified pair rejects it during
generation with `Unexpected header "X-Calibration-Revision"`; the complete
[pinned log](evidence/pinned-fern.log) and [versioned outcome](fern-refusal.txt)
record exit 1 and no SDK tree.

Two declarations claim the same header with different ownership. This is a
version-extension conflict, so it is `refuse` in both default and fern-strict
modes. There is no generated SDK to evaluate for import, type checking or wire
behaviour. The real-binary registry gate verifies exit 1, no output and the
header diagnostic; `parameter_header_refusals_keep_adjacent_controls_generating`
removes the conflicting version declaration and proves both modes generate.
Canonical version spelling takes precedence on the document node.

Settings: CLI 5.67.1, Python SDK 5.20.0, packaged layout, organization `fern`,
client `FernApi`, `python_enums`, extra fields `allow`, default retries 2, no
audience filter. There is no known real-document population for this class.

The [optional-header control](evidence/optional-control.yml) changes only the
parameter’s `required` flag to `false`. The same certified pair accepts it
([generation log](evidence/optional-control-fern.log),
[generator metadata](evidence/optional-control-metadata.json)); its source
SHA-256 is `9edc12026e0458d89c70752f643ed4496e7c14202c228be79332ce7dffddad75`.
The compiled-CLI recovery journey generates this adjacent control in both
default and fern-strict modes. It does not alter the required-header conflict
or this class’s `refuse` status.

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/optional-control-fern.log`](evidence/optional-control-fern.log)
- [`evidence/optional-control-metadata.json`](evidence/optional-control-metadata.json)
