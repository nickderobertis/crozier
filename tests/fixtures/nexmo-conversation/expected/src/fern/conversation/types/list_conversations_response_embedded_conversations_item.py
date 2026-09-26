

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.conversation_id import ConversationId
from ...types.name_conversation import NameConversation
from .list_conversations_response_embedded_conversations_item_links import (
    ListConversationsResponseEmbeddedConversationsItemLinks,
)


class ListConversationsResponseEmbeddedConversationsItem(UniversalBaseModel):
    links: typing_extensions.Annotated[
        typing.Optional[ListConversationsResponseEmbeddedConversationsItemLinks],
        FieldMetadata(alias="_links"),
        pydantic.Field(alias="_links"),
    ] = None
    name: NameConversation
    uuid_: typing_extensions.Annotated[ConversationId, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
