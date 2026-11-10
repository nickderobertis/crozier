# allof-oneof-member-field-order

A $ref oneOf branch of an allOf member lends its properties in branch order, and a docstring passes a flattened parent's fields in declaration order.

Verdict: `parity-gap-repaired`. Witnessed on the handed-off documents `4ff65943`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_referenced_one_of_branch_orders_the_fields_it_lends`.
