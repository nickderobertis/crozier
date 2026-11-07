# multipart-sibling-oneof

A multipart object whose oneOf sits beside its properties loses them: the method takes no part and sends data={} and files={}, as the certified pair does.

Verdict: `default-matched`. Witnessed on the handed-off documents `7da1db69`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_multipart_object_with_a_sibling_one_of_takes_no_parts`.
