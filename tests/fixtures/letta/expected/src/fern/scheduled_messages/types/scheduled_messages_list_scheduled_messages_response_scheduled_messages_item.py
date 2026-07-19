

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessage,
)
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule,
)


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem(UniversalBaseModel):
    id: str
    agent_id: str
    message: ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessage
    schedule: ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule
    next_scheduled_time: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
