

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_status_message_stream_status_range_complete_range_complete import (
    StreamStatusMessageStreamStatusRangeCompleteRangeComplete,
)
from .stream_status_message_stream_status_start_time_range import StreamStatusMessageStreamStatusStartTimeRange


class StreamStatusMessageStreamStatus_Start(UniversalBaseModel):
    """
    Stream lifecycle event. Sources emit these; the engine tracks stream progress from them.
    """

    status: typing.Literal["start"] = "start"
    stream: str
    time_range: typing.Optional[StreamStatusMessageStreamStatusStartTimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamStatusMessageStreamStatus_RangeComplete(UniversalBaseModel):
    """
    Stream lifecycle event. Sources emit these; the engine tracks stream progress from them.
    """

    status: typing.Literal["range_complete"] = "range_complete"
    stream: str
    range_complete: StreamStatusMessageStreamStatusRangeCompleteRangeComplete

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamStatusMessageStreamStatus_Complete(UniversalBaseModel):
    """
    Stream lifecycle event. Sources emit these; the engine tracks stream progress from them.
    """

    status: typing.Literal["complete"] = "complete"
    stream: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamStatusMessageStreamStatus_Error(UniversalBaseModel):
    """
    Stream lifecycle event. Sources emit these; the engine tracks stream progress from them.
    """

    status: typing.Literal["error"] = "error"
    stream: str
    error: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamStatusMessageStreamStatus_Skip(UniversalBaseModel):
    """
    Stream lifecycle event. Sources emit these; the engine tracks stream progress from them.
    """

    status: typing.Literal["skip"] = "skip"
    stream: str
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamStatusMessageStreamStatus = typing_extensions.Annotated[
    typing.Union[
        StreamStatusMessageStreamStatus_Start,
        StreamStatusMessageStreamStatus_RangeComplete,
        StreamStatusMessageStreamStatus_Complete,
        StreamStatusMessageStreamStatus_Error,
        StreamStatusMessageStreamStatus_Skip,
    ],
    pydantic.Field(discriminator="status"),
]
