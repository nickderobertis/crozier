

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_object import MessageDeltaObject
from .message_object import MessageObject


class MessageStreamEvent_ThreadMessageCreated(UniversalBaseModel):
    event: typing.Literal["thread.message.created"] = "thread.message.created"
    data: MessageObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageStreamEvent_ThreadMessageInProgress(UniversalBaseModel):
    event: typing.Literal["thread.message.in_progress"] = "thread.message.in_progress"
    data: MessageObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageStreamEvent_ThreadMessageDelta(UniversalBaseModel):
    event: typing.Literal["thread.message.delta"] = "thread.message.delta"
    data: MessageDeltaObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageStreamEvent_ThreadMessageCompleted(UniversalBaseModel):
    event: typing.Literal["thread.message.completed"] = "thread.message.completed"
    data: MessageObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageStreamEvent_ThreadMessageIncomplete(UniversalBaseModel):
    event: typing.Literal["thread.message.incomplete"] = "thread.message.incomplete"
    data: MessageObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MessageStreamEvent = typing_extensions.Annotated[
    typing.Union[
        MessageStreamEvent_ThreadMessageCreated,
        MessageStreamEvent_ThreadMessageInProgress,
        MessageStreamEvent_ThreadMessageDelta,
        MessageStreamEvent_ThreadMessageCompleted,
        MessageStreamEvent_ThreadMessageIncomplete,
    ],
    pydantic.Field(discriminator="event"),
]
