# streaming-core-api-error-alias

Streaming and binary-download methods raised a bare ApiError where the import was aliased beside a component of that name, a NameError at runtime; they now raise the alias.

Verdict: `parity-gap-repaired`. Witnessed on the handed-off documents `75888823`, each compared against its certified-pair tree in both enum modes (`../../comparisons/`). Guarded by `a_streamed_download_raises_the_aliased_core_api_error`.
