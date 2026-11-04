# Ignored multipart query collision

An unsplit octet-stream request wins over unused multipart alternatives; unused multipart properties cannot collide with actual query arguments. A split or selected multipart body still receives collision validation. This residual was exposed by Inferna.

The independent measurement document is authored from scratch. Its complete
certified tree was generated through `just fern-references measurements
handed-off/remeasure/ignored-multipart-query-collision` under the shared lock. The real-binary e2e
compares the complete SDK, exercises the controlling shape, and changes adjacent
output to show that an unexplained mismatch remains a failure. Where present,
the `expected-literals/` overlay holds the same comparison in literals mode.

No named ruling covers this behavior: the decision is `default-matched`, recorded
in [`../../remeasure.tsv`](../../remeasure.tsv).
