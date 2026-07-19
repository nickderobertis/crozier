

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContent,
)
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_role import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole,
)
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_type import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemType,
)


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItem(UniversalBaseModel):
    content: ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContent
    role: ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    type: typing.Optional[
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemType
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
