

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_retrieve_scheduled_message_response_message_include_return_message_types_item import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageIncludeReturnMessageTypesItem,
)
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem,
)


class ScheduledMessagesRetrieveScheduledMessageResponseMessage(UniversalBaseModel):
    messages: typing.List[ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem]
    max_steps: typing.Optional[float] = None
    callback_url: typing.Optional[str] = None
    include_return_message_types: typing.Optional[
        typing.List[ScheduledMessagesRetrieveScheduledMessageResponseMessageIncludeReturnMessageTypesItem]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
