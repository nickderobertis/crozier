# union-discriminant-base-strip

The discriminant declared beside a discriminated union's members is no shared field and its type is never written; a union declaring nothing else has no Base.

Verdict: `parity-gap-repaired`. Witnessed on the handed-off documents `aa02af8d`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_shared_field_beside_a_discriminated_union_excludes_the_discriminant`.
