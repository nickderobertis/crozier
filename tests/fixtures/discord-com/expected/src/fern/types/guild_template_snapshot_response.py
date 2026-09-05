

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .afk_timeouts import AfkTimeouts
from .available_locales_enum import AvailableLocalesEnum
from .guild_explicit_content_filter_types import GuildExplicitContentFilterTypes
from .guild_template_channel_response import GuildTemplateChannelResponse
from .guild_template_role_response import GuildTemplateRoleResponse
from .snowflake_type import SnowflakeType
from .user_notification_settings import UserNotificationSettings
from .verification_levels import VerificationLevels


class GuildTemplateSnapshotResponse(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    region: typing.Optional[str] = None
    verification_level: VerificationLevels
    default_message_notifications: UserNotificationSettings
    explicit_content_filter: GuildExplicitContentFilterTypes
    preferred_locale: AvailableLocalesEnum
    afk_channel_id: typing.Optional[SnowflakeType] = None
    afk_timeout: AfkTimeouts
    system_channel_id: typing.Optional[SnowflakeType] = None
    system_channel_flags: int
    roles: typing.List[GuildTemplateRoleResponse]
    channels: typing.List[GuildTemplateChannelResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
