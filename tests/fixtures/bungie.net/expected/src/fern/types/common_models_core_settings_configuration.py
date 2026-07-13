

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .common_models_core_system import CommonModelsCoreSystem
from .common_models_destiny2core_settings import CommonModelsDestiny2CoreSettings
from .user_email_settings import UserEmailSettings


class CommonModelsCoreSettingsConfiguration(UniversalBaseModel):
    clan_banner_decal_colors: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerDecalColors")
    ] = None
    clan_banner_decals: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerDecals")
    ] = None
    clan_banner_gonfalon_colors: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerGonfalonColors")
    ] = None
    clan_banner_gonfalon_detail_colors: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerGonfalonDetailColors")
    ] = None
    clan_banner_gonfalon_details: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerGonfalonDetails")
    ] = None
    clan_banner_gonfalons: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerGonfalons")
    ] = None
    clan_banner_standards: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="clanBannerStandards")
    ] = None
    default_group_theme: typing_extensions.Annotated[
        typing.Optional["CommonModelsCoreSetting"], FieldMetadata(alias="defaultGroupTheme")
    ] = None
    destiny2core_settings: typing_extensions.Annotated[
        typing.Optional[CommonModelsDestiny2CoreSettings], FieldMetadata(alias="destiny2CoreSettings")
    ] = None
    destiny_membership_types: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="destinyMembershipTypes")
    ] = None
    email_settings: typing_extensions.Annotated[
        typing.Optional[UserEmailSettings], FieldMetadata(alias="emailSettings")
    ] = None
    environment: typing.Optional[str] = None
    fireteam_activities: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="fireteamActivities")
    ] = None
    forum_categories: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="forumCategories")
    ] = None
    group_avatars: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="groupAvatars")
    ] = None
    ignore_reasons: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="ignoreReasons")
    ] = None
    recruitment_activities: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="recruitmentActivities")
    ] = None
    recruitment_misc_tags: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="recruitmentMiscTags")
    ] = None
    recruitment_platform_tags: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="recruitmentPlatformTags")
    ] = None
    system_content_locales: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="systemContentLocales")
    ] = None
    systems: typing.Optional[typing.Dict[str, CommonModelsCoreSystem]] = None
    user_content_locales: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]], FieldMetadata(alias="userContentLocales")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .common_models_core_setting import CommonModelsCoreSetting

update_forward_refs(CommonModelsCoreSettingsConfiguration)
