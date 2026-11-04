# Enum member digit separator

Explicit enum casing preserves publisher-declared digit separators in member and visitor names; ordinary enum values keep the existing derived spelling. This residual was exposed by AssemblyAI.

The independent measurement document is authored from scratch. Its complete
certified tree was generated through `just fern-references measurements
handed-off/remeasure/enum-member-digit-separator` under the shared lock. The real-binary e2e
compares the complete SDK, exercises the controlling shape, and changes adjacent
output to show that an unexplained mismatch remains a failure. Where present,
the `expected-literals/` overlay holds the same comparison in literals mode.

No named ruling covers this behavior: the decision is `default-matched`, recorded
in [`../../remeasure.tsv`](../../remeasure.tsv).
