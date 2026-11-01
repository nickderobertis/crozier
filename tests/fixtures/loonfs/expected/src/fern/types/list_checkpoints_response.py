

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkpoint import Checkpoint
from .namespace_id import NamespaceId


class ListCheckpointsResponse(UniversalBaseModel):
    """
    One page of checkpoint records, including expired records that garbage collection hasn't deleted
    yet.
    """

    checkpoints: typing.List[Checkpoint] = pydantic.Field()
    """
    The records, in ascending checkpoint ID order.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the records belong to.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    An opaque cursor for the next page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
