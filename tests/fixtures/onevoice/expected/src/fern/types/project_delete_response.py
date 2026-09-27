

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProjectDeleteResponse(UniversalBaseModel):
    deleted_conversations: typing_extensions.Annotated[
        int, FieldMetadata(alias="deletedConversations"), pydantic.Field(alias="deletedConversations")
    ]
    deleted_messages: typing_extensions.Annotated[
        int, FieldMetadata(alias="deletedMessages"), pydantic.Field(alias="deletedMessages")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
