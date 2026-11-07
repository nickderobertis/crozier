

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_status_message_stream_status_range_complete_range_complete import (
    StreamStatusMessageStreamStatusRangeCompleteRangeComplete,
)


class StreamStatusMessageStreamStatusRangeComplete(UniversalBaseModel):
    stream: str = pydantic.Field()
    """
    Stream being reported on.
    """

    range_complete: StreamStatusMessageStreamStatusRangeCompleteRangeComplete = pydantic.Field()
    """
    The sub-range that finished.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
