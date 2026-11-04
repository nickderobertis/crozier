

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_status_message_stream_status_start_time_range import StreamStatusMessageStreamStatusStartTimeRange


class StreamStatusMessageStreamStatusStart(UniversalBaseModel):
    stream: str = pydantic.Field()
    """
    Stream being reported on.
    """

    time_range: typing.Optional[StreamStatusMessageStreamStatusStartTimeRange] = pydantic.Field(default=None)
    """
    Full backfill time span for this stream.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
