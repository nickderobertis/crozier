# request-alias-inherited-sequence-fields

The request-alias rule read only a model's own fields and compared typing.Sequence to the reference's typing.List; it now reads inherited fields and the documented spelling.

Verdict: `fern-defect-departed`. Witnessed on the handed-off documents `698ea54a`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `alias_reference_correction_requires_the_actual_alias_signature_json_and_descriptions`.
