# titled-alias-body-collapses

A body component that is only allOf one $ref with empty properties is an alias, kept beside the method, and with no parameters collapses to a bare type name that sends no content-type whatever its title.

Verdict: `parity-gap-repaired`. Witnessed on the handed-off documents `698ea54a`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_titled_alias_body_with_no_parameters_collapses_and_sends_no_content_type`.
