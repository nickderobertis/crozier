

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContent,
)
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_role import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemRole,
)
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_type import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemType,
)


class ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem(UniversalBaseModel):
    content: ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContent
    role: ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemRole
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    type: typing.Optional[ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
