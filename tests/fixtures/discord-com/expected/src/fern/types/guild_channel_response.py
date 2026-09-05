

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_overwrite_response import ChannelPermissionOverwriteResponse
from .default_reaction_emoji_response import DefaultReactionEmojiResponse
from .forum_layout import ForumLayout
from .forum_tag_response import ForumTagResponse
from .snowflake_type import SnowflakeType
from .thread_auto_archive_duration import ThreadAutoArchiveDuration
from .thread_sort_order import ThreadSortOrder
from .video_quality_modes import VideoQualityModes


class GuildChannelResponse(UniversalBaseModel):
    id: SnowflakeType
    type: int
    last_message_id: typing.Optional[SnowflakeType] = None
    flags: int
    last_pin_timestamp: typing.Optional[dt.datetime] = None
    guild_id: SnowflakeType
    name: str
    parent_id: typing.Optional[SnowflakeType] = None
    rate_limit_per_user: typing.Optional[int] = None
    bitrate: typing.Optional[int] = None
    user_limit: typing.Optional[int] = None
    rtc_region: typing.Optional[str] = None
    video_quality_mode: typing.Optional[VideoQualityModes] = None
    permissions: typing.Optional[str] = None
    topic: typing.Optional[str] = None
    default_auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    default_thread_rate_limit_per_user: typing.Optional[int] = None
    position: int
    permission_overwrites: typing.Optional[typing.List[ChannelPermissionOverwriteResponse]] = None
    nsfw: typing.Optional[bool] = None
    available_tags: typing.Optional[typing.List[ForumTagResponse]] = None
    default_reaction_emoji: typing.Optional[DefaultReactionEmojiResponse] = None
    default_sort_order: typing.Optional[ThreadSortOrder] = None
    default_forum_layout: typing.Optional[ForumLayout] = None
    hd_streaming_until: typing.Optional[dt.datetime] = None
    hd_streaming_buyer_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
