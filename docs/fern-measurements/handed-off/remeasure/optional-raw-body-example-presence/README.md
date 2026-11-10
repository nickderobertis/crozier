# optional-raw-body-example-presence

An optional raw body works a call only where the operation declares x-codeSamples, and README anchors on it; the pair's empty call fails to bind the required request keyword, so crozier passes request=b"string".

Verdict: `fern-defect-departed`. Witnessed on the handed-off documents `215ec23d`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `an_optional_raw_body_with_code_samples_is_worked_and_without_them_is_not` and `an_empty_raw_upload_call_is_explained_only_for_a_sampled_optional_body`.
