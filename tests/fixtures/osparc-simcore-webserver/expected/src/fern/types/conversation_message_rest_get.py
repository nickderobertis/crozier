

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conversation_id import ConversationId
from .conversation_message_id import ConversationMessageId
from .conversation_message_type import ConversationMessageType
from .group_id_int import GroupIdInt


class ConversationMessageRestGet(UniversalBaseModel):
    message_id: typing_extensions.Annotated[
        ConversationMessageId, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ]
    conversation_id: typing_extensions.Annotated[
        ConversationId, FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ]
    user_group_id: typing_extensions.Annotated[
        GroupIdInt, FieldMetadata(alias="userGroupId"), pydantic.Field(alias="userGroupId")
    ]
    content: str
    type: ConversationMessageType
    created: dt.datetime
    modified: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
