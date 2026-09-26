

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_conversations_response_embedded_conversations_item import ListConversationsResponseEmbeddedConversationsItem


class ListConversationsResponseEmbedded(UniversalBaseModel):
    """
    A list of conversation objects. See the [get details of a specific conversation](#retrieveConversation) response fields for a description of the nested objects
    """

    conversations: typing.List[ListConversationsResponseEmbeddedConversationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
