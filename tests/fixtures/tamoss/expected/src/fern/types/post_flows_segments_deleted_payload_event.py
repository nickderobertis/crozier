

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timerange import Timerange
from .uuid_ import Uuid


class PostFlowsSegmentsDeletedPayloadEvent(UniversalBaseModel):
    flow_id: Uuid
    timerange: Timerange = pydantic.Field()
    """
    The timerange of Segments that have been deleted. The timerange MUST intersect with a Segment which has been deleted at both start and end (e.g. it cannot start or end in empty space).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
