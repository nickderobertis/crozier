

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_post_conversations_id_searches_data_item_relevance import (
    EndpointPostConversationsIdSearchesDataItemRelevance,
)


class EndpointPostConversationsIdSearchesDataItem(UniversalBaseModel):
    message: typing.Optional["Message"] = None
    relevance: typing.Optional[EndpointPostConversationsIdSearchesDataItemRelevance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointPostConversationsIdSearchesDataItem, Conversation=Conversation, Message=Message)
