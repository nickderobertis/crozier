

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_features import GroupsV2GroupFeatures
from .groups_v2group_v2clan_info_and_investment import GroupsV2GroupV2ClanInfoAndInvestment


class GroupsV2GroupV2(UniversalBaseModel):
    about: typing.Optional[str] = None
    allow_chat: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="allowChat")] = None
    avatar_image_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="avatarImageIndex")] = (
        None
    )
    avatar_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="avatarPath")] = None
    ban_expire_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="banExpireDate")] = (
        None
    )
    banner_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="bannerPath")] = None
    chat_security: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="chatSecurity")] = None
    clan_info: typing_extensions.Annotated[
        typing.Optional[GroupsV2GroupV2ClanInfoAndInvestment], FieldMetadata(alias="clanInfo")
    ] = None
    conversation_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="conversationId")] = None
    creation_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="creationDate")] = None
    default_publicity: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="defaultPublicity")] = None
    enable_invitation_messaging_for_admins: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableInvitationMessagingForAdmins")
    ] = None
    features: typing.Optional[GroupsV2GroupFeatures] = None
    group_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupId")] = None
    group_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupType")] = None
    homepage: typing.Optional[int] = None
    is_default_post_public: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDefaultPostPublic")
    ] = None
    is_public: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPublic")] = None
    is_public_topic_admin_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPublicTopicAdminOnly")
    ] = None
    locale: typing.Optional[str] = None
    member_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="memberCount")] = None
    membership_id_created: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membershipIdCreated")
    ] = None
    membership_option: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipOption")] = None
    modification_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modificationDate")
    ] = None
    motto: typing.Optional[str] = None
    name: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None
    theme: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
