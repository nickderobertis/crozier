

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delta import Delta
from .done import Done
from .problem import Problem
from .usage import Usage


class StreamEvent_Delta(UniversalBaseModel):
    """
    One Server-Sent Event of the answer stream. `event` is the SSE event name.
    """

    event: typing.Literal["delta"] = "delta"
    data: Delta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamEvent_Usage(UniversalBaseModel):
    """
    One Server-Sent Event of the answer stream. `event` is the SSE event name.
    """

    event: typing.Literal["usage"] = "usage"
    data: Usage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamEvent_Done(UniversalBaseModel):
    """
    One Server-Sent Event of the answer stream. `event` is the SSE event name.
    """

    event: typing.Literal["done"] = "done"
    data: Done

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamEvent_Error(UniversalBaseModel):
    """
    One Server-Sent Event of the answer stream. `event` is the SSE event name.
    """

    event: typing.Literal["error"] = "error"
    data: Problem

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamEvent = typing_extensions.Annotated[
    typing.Union[StreamEvent_Delta, StreamEvent_Usage, StreamEvent_Done, StreamEvent_Error],
    pydantic.Field(discriminator="event"),
]
