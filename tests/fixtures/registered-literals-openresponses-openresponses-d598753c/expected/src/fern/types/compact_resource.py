

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compact_resource_object import CompactResourceObject
from .compact_resource_usage import CompactResourceUsage
from .item_field import ItemField


class CompactResource(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier for the compacted response.
    """

    object: CompactResourceObject = pydantic.Field()
    """
    The object type. Always `response.compaction`.
    """

    output: typing.List[ItemField] = pydantic.Field()
    """
    The compacted list of output items.
    """

    created_at: int = pydantic.Field()
    """
    Unix timestamp (in seconds) when the compacted conversation was created.
    """

    usage: CompactResourceUsage = pydantic.Field()
    """
    Token accounting for the compaction pass, including cached, reasoning, and total tokens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
