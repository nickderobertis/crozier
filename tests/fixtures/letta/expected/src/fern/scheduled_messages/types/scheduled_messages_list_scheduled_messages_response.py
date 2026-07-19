

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item import (
    ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem,
)


class ScheduledMessagesListScheduledMessagesResponse(UniversalBaseModel):
    scheduled_messages: typing.List[ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem]
    has_next_page: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
