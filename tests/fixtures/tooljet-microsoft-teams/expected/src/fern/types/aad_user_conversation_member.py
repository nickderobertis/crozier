

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aad_user_conversation_member_user import AadUserConversationMemberUser


class AadUserConversationMember(UniversalBaseModel):
    email: typing.Optional[str] = None
    tenant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    user: typing.Optional[AadUserConversationMemberUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
