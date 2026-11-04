# Group placement carries synthetic descendants

The document-acceptance area exposed this residual on the four AssemblyAI
handed-off documents: a component's SDK group places the component in that
package but left its hoisted inline objects and enums at the root in crozier.
The certified pair keeps those synthetic descendants beside the component.
References to other named components retain their own placements.

The independent Garden Depot Ledger document covers a grouped component, an
inline array-item object, two inline enums, and a reference to a separate root
component. Its complete certified tree was freshly generated under the shared
lock through `just fern-references measurements
handed-off/remeasure/group-placed-nested-type-placement`. Its literals overlay
is regenerated through the same case's `expected-literals` item.

The e2e journey compares the whole tree, asserts both the moved descendants and
the root component control, and checks that an extra root copy still fails the
comparison. No named ruling covers the placement gap: it is `default-matched`,
recorded in [`../../remeasure.tsv`](../../remeasure.tsv).
