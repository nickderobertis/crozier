

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conversation_title_status import ConversationTitleStatus


class Conversation(UniversalBaseModel):
    id: str
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    project_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")
    ] = None
    title: str = pydantic.Field()
    """
    Empty with titleStatus auto marks a settled fallback; localize from createdAt at display time.
    """

    preview: typing.Optional[str] = pydantic.Field(default=None)
    """
    Computed on conversation list responses from the latest nonblank user or assistant message, ordered by createdAt then message ID descending. Unicode whitespace is collapsed before truncation to 160 code points plus an ellipsis. Empty for chats without readable messages. Other conversation endpoints do not populate this field.
    """

    title_status: typing_extensions.Annotated[
        ConversationTitleStatus, FieldMetadata(alias="titleStatus"), pydantic.Field(alias="titleStatus")
    ]
    pinned_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="pinnedAt"), pydantic.Field(alias="pinnedAt")
    ] = None
    last_message_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastMessageAt"), pydantic.Field(alias="lastMessageAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
