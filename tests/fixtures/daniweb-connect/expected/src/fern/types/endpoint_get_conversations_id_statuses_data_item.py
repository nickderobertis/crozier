

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_get_conversations_id_statuses_data_item_bubbled import EndpointGetConversationsIdStatusesDataItemBubbled


class EndpointGetConversationsIdStatusesDataItem(UniversalBaseModel):
    archived_status: typing.Optional[bool] = None
    bubbled: typing.Optional[EndpointGetConversationsIdStatusesDataItemBubbled] = None
    conversation: typing.Optional["Conversation"] = None
    earliest_unseen_message: typing.Optional["Message"] = None
    new_message_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointGetConversationsIdStatusesDataItem, Conversation=Conversation, Message=Message)
