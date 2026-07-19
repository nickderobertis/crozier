

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_schedule_agent_message_request_messages_item_content import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItemContent,
)
from .scheduled_messages_schedule_agent_message_request_messages_item_role import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole,
)
from .scheduled_messages_schedule_agent_message_request_messages_item_type import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItemType,
)


class ScheduledMessagesScheduleAgentMessageRequestMessagesItem(UniversalBaseModel):
    content: ScheduledMessagesScheduleAgentMessageRequestMessagesItemContent
    role: ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    type: typing.Optional[ScheduledMessagesScheduleAgentMessageRequestMessagesItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
