

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links_conversation_self import LinksConversationSelf


class LinksConversation(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        typing.Optional[LinksConversationSelf], FieldMetadata(alias="self"), pydantic.Field(alias="self")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
