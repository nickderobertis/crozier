

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_retrieve_scheduled_message_response_message import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessage,
)
from .scheduled_messages_retrieve_scheduled_message_response_schedule import (
    ScheduledMessagesRetrieveScheduledMessageResponseSchedule,
)


class ScheduledMessagesRetrieveScheduledMessageResponse(UniversalBaseModel):
    id: str
    agent_id: str
    message: ScheduledMessagesRetrieveScheduledMessageResponseMessage
    schedule: ScheduledMessagesRetrieveScheduledMessageResponseSchedule
    next_scheduled_time: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
