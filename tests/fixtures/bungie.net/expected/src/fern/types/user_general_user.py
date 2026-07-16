

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_to_user_context import UserUserToUserContext


class UserGeneralUser(UniversalBaseModel):
    about: typing.Optional[str] = None
    blizzard_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blizzardDisplayName"), pydantic.Field(alias="blizzardDisplayName")
    ] = None
    cached_bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cachedBungieGlobalDisplayName"),
        pydantic.Field(alias="cachedBungieGlobalDisplayName"),
    ] = None
    cached_bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="cachedBungieGlobalDisplayNameCode"),
        pydantic.Field(alias="cachedBungieGlobalDisplayNameCode"),
    ] = None
    context: typing.Optional[UserUserToUserContext] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    egs_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="egsDisplayName"), pydantic.Field(alias="egsDisplayName")
    ] = None
    fb_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fbDisplayName"), pydantic.Field(alias="fbDisplayName")
    ] = None
    first_access: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="firstAccess"), pydantic.Field(alias="firstAccess")
    ] = None
    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")
    ] = None
    last_ban_report_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastBanReportId"), pydantic.Field(alias="lastBanReportId")
    ] = None
    last_update: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdate"), pydantic.Field(alias="lastUpdate")
    ] = None
    legacy_portal_uid: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="legacyPortalUID"), pydantic.Field(alias="legacyPortalUID")
    ] = None
    locale: typing.Optional[str] = None
    locale_inherit_default: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="localeInheritDefault"), pydantic.Field(alias="localeInheritDefault")
    ] = None
    membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membershipId"), pydantic.Field(alias="membershipId")
    ] = None
    normalized_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="normalizedName"), pydantic.Field(alias="normalizedName")
    ] = None
    profile_ban_expire: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="profileBanExpire"), pydantic.Field(alias="profileBanExpire")
    ] = None
    profile_picture: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="profilePicture"), pydantic.Field(alias="profilePicture")
    ] = None
    profile_picture_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="profilePicturePath"), pydantic.Field(alias="profilePicturePath")
    ] = None
    profile_picture_wide_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="profilePictureWidePath"),
        pydantic.Field(alias="profilePictureWidePath"),
    ] = None
    profile_theme: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="profileTheme"), pydantic.Field(alias="profileTheme")
    ] = None
    profile_theme_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="profileThemeName"), pydantic.Field(alias="profileThemeName")
    ] = None
    psn_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="psnDisplayName"), pydantic.Field(alias="psnDisplayName")
    ] = None
    show_activity: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showActivity"), pydantic.Field(alias="showActivity")
    ] = None
    show_group_messaging: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showGroupMessaging"), pydantic.Field(alias="showGroupMessaging")
    ] = None
    stadia_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stadiaDisplayName"), pydantic.Field(alias="stadiaDisplayName")
    ] = None
    status_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="statusDate"), pydantic.Field(alias="statusDate")
    ] = None
    status_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusText"), pydantic.Field(alias="statusText")
    ] = None
    steam_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="steamDisplayName"), pydantic.Field(alias="steamDisplayName")
    ] = None
    success_message_flags: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="successMessageFlags"), pydantic.Field(alias="successMessageFlags")
    ] = None
    twitch_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="twitchDisplayName"), pydantic.Field(alias="twitchDisplayName")
    ] = None
    unique_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uniqueName"), pydantic.Field(alias="uniqueName")
    ] = None
    user_title: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="userTitle"), pydantic.Field(alias="userTitle")
    ] = None
    user_title_display: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userTitleDisplay"), pydantic.Field(alias="userTitleDisplay")
    ] = None
    xbox_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xboxDisplayName"), pydantic.Field(alias="xboxDisplayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
