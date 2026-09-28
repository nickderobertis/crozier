

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ContactChannelVerifyResponseChannel(UniversalBaseModel):
    id: str
    contact_id: typing_extensions.Annotated[str, FieldMetadata(alias="contactId"), pydantic.Field(alias="contactId")]
    type: str
    address: str
    is_primary: typing_extensions.Annotated[bool, FieldMetadata(alias="isPrimary"), pydantic.Field(alias="isPrimary")]
    external_chat_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalChatId"), pydantic.Field(alias="externalChatId")
    ] = None
    status: typing.Optional[str] = None
    policy: typing.Optional[str] = None
    verified_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="verifiedAt"), pydantic.Field(alias="verifiedAt")
    ] = None
    verified_via: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verifiedVia"), pydantic.Field(alias="verifiedVia")
    ] = None
    invite_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inviteId"), pydantic.Field(alias="inviteId")
    ] = None
    revoked_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="revokedReason"), pydantic.Field(alias="revokedReason")
    ] = None
    blocked_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockedReason"), pydantic.Field(alias="blockedReason")
    ] = None
    last_seen_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastSeenAt"), pydantic.Field(alias="lastSeenAt")
    ] = None
    interaction_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="interactionCount"), pydantic.Field(alias="interactionCount")
    ]
    last_interaction: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastInteraction"), pydantic.Field(alias="lastInteraction")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
