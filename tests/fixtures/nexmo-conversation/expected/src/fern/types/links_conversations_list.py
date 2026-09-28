

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links_conversations_list_self import LinksConversationsListSelf


class LinksConversationsList(UniversalBaseModel):
    """
    A series of links between resources in this API in the http://stateless.co/hal_specification.html.
    """

    self_: typing_extensions.Annotated[
        LinksConversationsListSelf, FieldMetadata(alias="self"), pydantic.Field(alias="self")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
