

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_segment import FlowSegment
from .uuid_ import Uuid


class PostFlowsSegmentsAddedPayloadEvent(UniversalBaseModel):
    flow_id: Uuid
    segments: typing.List[FlowSegment]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
