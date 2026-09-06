

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .afk_timeouts import AfkTimeouts
from .available_locales_enum import AvailableLocalesEnum
from .emoji_response import EmojiResponse
from .guild_explicit_content_filter_types import GuildExplicitContentFilterTypes
from .guild_features import GuildFeatures
from .guild_mfa_level import GuildMfaLevel
from .guild_nsfw_content_level import GuildNsfwContentLevel
from .guild_role_response import GuildRoleResponse
from .guild_sticker_response import GuildStickerResponse
from .premium_guild_tiers import PremiumGuildTiers
from .snowflake_type import SnowflakeType
from .user_notification_settings import UserNotificationSettings
from .verification_levels import VerificationLevels


class GuildResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    icon: typing.Optional[str] = None
    description: typing.Optional[str] = None
    home_header: typing.Optional[str] = None
    splash: typing.Optional[str] = None
    discovery_splash: typing.Optional[str] = None
    features: typing.List[GuildFeatures]
    banner: typing.Optional[str] = None
    owner_id: SnowflakeType
    application_id: typing.Optional[SnowflakeType] = None
    region: str
    afk_channel_id: typing.Optional[SnowflakeType] = None
    afk_timeout: AfkTimeouts
    system_channel_id: typing.Optional[SnowflakeType] = None
    system_channel_flags: int
    widget_enabled: bool
    widget_channel_id: typing.Optional[SnowflakeType] = None
    verification_level: VerificationLevels
    roles: typing.List[GuildRoleResponse]
    default_message_notifications: UserNotificationSettings
    mfa_level: GuildMfaLevel
    explicit_content_filter: GuildExplicitContentFilterTypes
    max_presences: typing.Optional[int] = None
    max_members: typing.Optional[int] = None
    max_stage_video_channel_users: typing.Optional[int] = None
    max_video_channel_users: typing.Optional[int] = None
    vanity_url_code: typing.Optional[str] = None
    premium_tier: PremiumGuildTiers
    premium_subscription_count: int
    preferred_locale: AvailableLocalesEnum
    rules_channel_id: typing.Optional[SnowflakeType] = None
    safety_alerts_channel_id: typing.Optional[SnowflakeType] = None
    public_updates_channel_id: typing.Optional[SnowflakeType] = None
    premium_progress_bar_enabled: bool
    nsfw: bool
    nsfw_level: GuildNsfwContentLevel
    emojis: typing.List[EmojiResponse]
    stickers: typing.List[GuildStickerResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
