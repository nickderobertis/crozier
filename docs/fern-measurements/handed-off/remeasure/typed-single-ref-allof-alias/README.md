# Typed single ref allof alias

A single-reference allOf without own fields is an alias even with explicit object type or additionalProperties false; own properties still produce an inherited model. This residual was exposed by AssemblyAI.

The independent measurement document is authored from scratch. Its complete
certified tree was generated through `just fern-references measurements
handed-off/remeasure/typed-single-ref-allof-alias` under the shared lock. The real-binary e2e
compares the complete SDK, exercises the controlling shape, and changes adjacent
output to show that an unexplained mismatch remains a failure. Where present,
the `expected-literals/` overlay holds the same comparison in literals mode.

No named ruling covers this behavior: the decision is `default-matched`, recorded
in [`../../remeasure.tsv`](../../remeasure.tsv).
