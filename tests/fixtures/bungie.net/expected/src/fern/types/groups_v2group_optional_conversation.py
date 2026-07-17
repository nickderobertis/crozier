

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GroupsV2GroupOptionalConversation(UniversalBaseModel):
    chat_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="chatEnabled"), pydantic.Field(alias="chatEnabled")
    ] = None
    chat_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="chatName"), pydantic.Field(alias="chatName")
    ] = None
    chat_security: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="chatSecurity"), pydantic.Field(alias="chatSecurity")
    ] = None
    conversation_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
