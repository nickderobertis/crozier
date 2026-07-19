

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource,
)


class ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem = typing_extensions.Annotated[
    typing.Union[
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text,
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Image,
    ],
    pydantic.Field(discriminator="type"),
]
