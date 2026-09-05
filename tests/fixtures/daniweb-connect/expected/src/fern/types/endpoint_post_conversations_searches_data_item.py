

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_post_conversations_searches_data_item_relevance import EndpointPostConversationsSearchesDataItemRelevance


class EndpointPostConversationsSearchesDataItem(UniversalBaseModel):
    message: typing.Optional["Message"] = None
    relevance: typing.Optional[EndpointPostConversationsSearchesDataItemRelevance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointPostConversationsSearchesDataItem, Conversation=Conversation, Message=Message)
