

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conversation_id import ConversationId
from .conversation_name import ConversationName
from .conversation_status import ConversationStatus
from .conversation_type import ConversationType
from .group_id_int import GroupIdInt


class ConversationRestGet(UniversalBaseModel):
    conversation_id: typing_extensions.Annotated[
        ConversationId, FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ]
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    name: typing.Optional[ConversationName] = None
    project_uuid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectUuid"), pydantic.Field(alias="projectUuid")
    ] = None
    user_group_id: typing_extensions.Annotated[
        GroupIdInt, FieldMetadata(alias="userGroupId"), pydantic.Field(alias="userGroupId")
    ]
    type: ConversationType
    fogbugz_case_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fogbugzCaseId"), pydantic.Field(alias="fogbugzCaseId")
    ] = None
    created: dt.datetime
    modified: dt.datetime
    extra_context: typing_extensions.Annotated[
        typing.Dict[str, str], FieldMetadata(alias="extraContext"), pydantic.Field(alias="extraContext")
    ]
    is_read_by_user: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isReadByUser"), pydantic.Field(alias="isReadByUser")
    ]
    is_read_by_support: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isReadBySupport"), pydantic.Field(alias="isReadBySupport")
    ]
    status: ConversationStatus
    last_message_created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastMessageCreatedAt"), pydantic.Field(alias="lastMessageCreatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
