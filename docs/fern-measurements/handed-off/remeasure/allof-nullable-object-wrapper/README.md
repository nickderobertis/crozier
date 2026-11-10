# allof-nullable-object-wrapper

A 3.0 {nullable: true, type: object} member beside a $ref extends the parent; only 3.1 type: [object, null] flattens it.

Verdict: `parity-gap-repaired`. Witnessed on the handed-off documents `79291d99`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_nullable_object_member_extends_the_parent_while_a_type_array_flattens_it`.
