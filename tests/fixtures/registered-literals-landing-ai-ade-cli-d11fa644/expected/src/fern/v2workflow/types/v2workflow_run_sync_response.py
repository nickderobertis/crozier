

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.v2workflow_metadata import V2WorkflowMetadata


class V2WorkflowRunSyncResponse(UniversalBaseModel):
    """
    Result returned by V2WorkflowOperationWorkflow.

    ``output`` is keyed by step name (or by caller-chosen projection keys when
    ``output`` was provided in the request). For the ``"parse-extract"`` pipeline
    with no projection, the keys are ``"parse-extract"`` → ``{parse, extract, ground}``:

    * ``output["parse-extract"]["parse"]`` — full parse response (markdown,
      structure with per-node grounding inline, metadata).
    * ``output["parse-extract"]["extract"]`` — extraction + ``extraction_metadata``
      with ``{value, ranges}`` leaves.
    * ``output["parse-extract"]["ground"]`` — a tree MIRRORING
      ``extraction_metadata``: each ``{value, ranges}`` leaf is replaced by its
      resolved block-hit list (``[{block_id, type, parent_id?, grounding,
      atomic_grounding?}]`` — the same shape ``/v2/ground`` returns; see
      ``V2GroundResult.grounding`` for the full field-level contract), or
      ``null`` for a synthesised value. Nested objects and arrays keep their
      shape, so ``ground.issuer.name`` parallels
      ``extraction_metadata.issuer.name``. Resolved server-side — no
      client-side span lookup needed.

    References into the results use the ``$output.<step>.<field>...`` grammar
    (see ``output`` field of the request).
    """

    output: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Step results keyed by step name, or a caller-defined projection. For ``parse-extract`` with no projection: ``{"parse-extract": {parse, extract, ground}}``.
    """

    metadata: V2WorkflowMetadata = pydantic.Field()
    """
    Request metadata (job_id, duration_ms, billing).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
