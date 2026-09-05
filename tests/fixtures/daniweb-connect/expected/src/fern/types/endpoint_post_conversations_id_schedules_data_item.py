

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_post_conversations_id_schedules_data_item_navigation import (
    EndpointPostConversationsIdSchedulesDataItemNavigation,
)


class EndpointPostConversationsIdSchedulesDataItem(UniversalBaseModel):
    author_count: typing.Optional[int] = None
    conversation_count: typing.Optional[int] = None
    conversation_id: typing.Optional[int] = None
    date: typing.Optional[dt.date] = None
    first_message: typing.Optional["Message"] = None
    last_message: typing.Optional["Message"] = None
    message_count: typing.Optional[int] = None
    my_message_count: typing.Optional[int] = None
    navigation: typing.Optional[EndpointPostConversationsIdSchedulesDataItemNavigation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointPostConversationsIdSchedulesDataItem, Conversation=Conversation, Message=Message)
