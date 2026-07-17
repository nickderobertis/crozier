

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GroupsV2GroupEditAction(UniversalBaseModel):
    about: typing.Optional[str] = None
    allow_chat: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowChat"), pydantic.Field(alias="allowChat")
    ] = None
    avatar_image_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="avatarImageIndex"), pydantic.Field(alias="avatarImageIndex")
    ] = None
    callsign: typing.Optional[str] = None
    chat_security: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="chatSecurity"), pydantic.Field(alias="chatSecurity")
    ] = None
    default_publicity: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="defaultPublicity"), pydantic.Field(alias="defaultPublicity")
    ] = None
    enable_invitation_messaging_for_admins: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="enableInvitationMessagingForAdmins"),
        pydantic.Field(alias="enableInvitationMessagingForAdmins"),
    ] = None
    homepage: typing.Optional[int] = None
    is_public: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPublic"), pydantic.Field(alias="isPublic")
    ] = None
    is_public_topic_admin_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPublicTopicAdminOnly"),
        pydantic.Field(alias="isPublicTopicAdminOnly"),
    ] = None
    locale: typing.Optional[str] = None
    membership_option: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membershipOption"), pydantic.Field(alias="membershipOption")
    ] = None
    motto: typing.Optional[str] = None
    name: typing.Optional[str] = None
    tags: typing.Optional[str] = None
    theme: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
