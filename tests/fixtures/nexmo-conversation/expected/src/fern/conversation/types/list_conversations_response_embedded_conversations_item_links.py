

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_conversations_response_embedded_conversations_item_links_self import (
    ListConversationsResponseEmbeddedConversationsItemLinksSelf,
)


class ListConversationsResponseEmbeddedConversationsItemLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        typing.Optional[ListConversationsResponseEmbeddedConversationsItemLinksSelf],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
