# example-summary-not-string: refuse

## At Fern CLI 5.216.0 / fern-python-sdk 5.42.0

Decision: **refuse**, unchanged. The Fern goldens run 44880783817
re-took the [probe record](fern-refusal.txt) at this pair, and Fern still refuses
the probe as recorded. Every shape, confirmation and reduction the registry
carries for the class was retaken at this pair (`fern-refusals.py shapes`,
`confirm` and `reduce`, one Fern run at a time), each keeping its role's
verdict (`shapes.tsv` is unchanged), and `fern-refusals.py check` holds them
there. crozier's behaviour is unchanged: the e2e gate still runs its probe in
both modes. The sections below are history at the pairs they name.

## At Fern CLI 5.200.0 / fern-python-sdk 5.41.25

Decision: **refuse**, unchanged. The Fern goldens run 43423270787
re-took the [probe record](fern-refusal.txt) at this pair, and Fern still refuses
the probe as recorded. Every shape, confirmation and reduction the registry
carries for the class was retaken at this pair (`fern-refusals.py shapes`,
`confirm` and `reduce`, serially), each with its role's verdict, and
`fern-refusals.py check` holds them there. crozier's behaviour is unchanged: the
e2e gate still runs its probe in both modes. The sections below are history at
the pairs they name.

Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3. Decision: **refuse**, in
both modes.

The [probe](probe.yml) names its one request example with `summary: 1`, a YAML
integer. `fern check` passes, then the generator crashes with `Cannot use 'in'
operator to search for 'wireValue' in 1` and writes nothing
([record](fern-refusal.txt),
[check](../../openapi-surface/fern-refusals/probe-logs/example-summary-not-string.check.log),
[generate](../../openapi-surface/fern-refusals/probe-logs/example-summary-not-string.generate.log)).
The same summary as a string generates ([control](string-summary-control.yml)),
and so does every shape of [`duplicate-example-name`](../duplicate-example-name/evaluation.md)
whose summaries are strings; its `number-vs-string-summary` probe, a numeric and a
string summary that do not collide, fails the same way
([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)).

The OpenAPI Specification declares an Example Object's `summary` a string, so
the document is at fault rather than Fern: there is no valid input whose
intent a generated SDK could reproduce, and the class is `refuse` in both modes.
crozier refuses it after the duplicate-name check, as Fern's check reports
duplicates before the generator runs: two equal numeric summaries remain
`duplicate-example-name`. Only request examples are measured; a numeric summary
on a response example is not refused.

No document in the refused population carries the class.
