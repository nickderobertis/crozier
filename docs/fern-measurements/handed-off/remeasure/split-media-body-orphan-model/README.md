# Split media body does not leave an orphan JSON model

A JSON request component offered beside a binary media type, with one SDK
method name per media type. The certified pair spreads the JSON fields and
writes no standalone `RecordingUrl` model. crozier already does the same on
this node's base; this is a regression guard for the `orphan-type-emission`
cause and the Deepgram amendment.

The complete `fern-expected/` tree was freshly generated from this independent
Garden Recording Archive document through `just fern-references measurements
handed-off/remeasure/split-media-body-orphan-model`, at the certified pair under
the shared generation lock. `remeasure_split_media_body_writes_no_unreferenced_json_model`
drives crozier and compares the whole tree; resurrecting that unused model
makes the comparison fail.
