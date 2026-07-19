

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource,
)


class ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImage(UniversalBaseModel):
    source: ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
