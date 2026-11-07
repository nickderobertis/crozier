

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.v2ground_metadata import V2GroundMetadata


class V2GroundRunSyncResponse(UniversalBaseModel):
    """
    Result returned by V2GroundOperationWorkflow — the ``/v2/ground``
    response body.

    ``grounding`` MIRRORS the ``extraction_metadata`` tree: nested objects and
    arrays keep their shape, and each ``{value, ranges}`` leaf is replaced by
    the list of structure blocks its ranges overlap (the block-hit shape
    documented on the field). It is NOT a flat map — a nested schema field like
    ``issuer.name`` resolves to ``grounding["issuer"]["name"]``.
    """

    grounding: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    A tree mirroring ``extraction_metadata``: nested objects and arrays keep their shape, and each ``{value, ranges}`` leaf is replaced by the list of blocks its ranges overlap, in reading order. Each entry carries ``block_id`` and ``type`` identifying the matched ``structure`` block, ``parent_id`` naming the enclosing block for nested blocks (table cells), and the block's own ``grounding`` object (``{page, range, box}``) verbatim. When the block itself carries ``atomic_grounding``, the entry also lists the overlapping subset as ``{index, page, range, box}`` objects, where ``index`` is the position in the block's own ``atomic_grounding`` array; ``[]`` means the block matched but no individual entry did, and the key is omitted for blocks that carry no ``atomic_grounding``. A leaf is ``null`` when its ``ranges`` was ``null`` (a synthesised value, with no supporting passage to look up) and ``[]`` when valid ranges overlapped no block (which usually indicates a mismatched extraction/structure pair).
    """

    metadata: V2GroundMetadata = pydantic.Field()
    """
    Request metadata (job_id, duration_ms, credit_usage).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
