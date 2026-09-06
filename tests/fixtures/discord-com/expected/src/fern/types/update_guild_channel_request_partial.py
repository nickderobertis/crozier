

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_overwrite_request import ChannelPermissionOverwriteRequest
from .forum_layout import ForumLayout
from .snowflake_type import SnowflakeType
from .thread_auto_archive_duration import ThreadAutoArchiveDuration
from .thread_sort_order import ThreadSortOrder
from .update_default_reaction_emoji_request import UpdateDefaultReactionEmojiRequest
from .update_thread_tag_request import UpdateThreadTagRequest
from .video_quality_modes import VideoQualityModes


class UpdateGuildChannelRequestPartial(UniversalBaseModel):
    type: typing.Optional[int] = None
    name: typing.Optional[str] = None
    position: typing.Optional[int] = None
    topic: typing.Optional[str] = None
    bitrate: typing.Optional[int] = None
    user_limit: typing.Optional[int] = None
    nsfw: typing.Optional[bool] = None
    rate_limit_per_user: typing.Optional[int] = None
    parent_id: typing.Optional[SnowflakeType] = None
    permission_overwrites: typing.Optional[typing.List[ChannelPermissionOverwriteRequest]] = None
    rtc_region: typing.Optional[str] = None
    video_quality_mode: typing.Optional[VideoQualityModes] = None
    default_auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    default_reaction_emoji: typing.Optional[UpdateDefaultReactionEmojiRequest] = None
    default_thread_rate_limit_per_user: typing.Optional[int] = None
    default_sort_order: typing.Optional[ThreadSortOrder] = None
    default_forum_layout: typing.Optional[ForumLayout] = None
    flags: typing.Optional[int] = None
    available_tags: typing.Optional[typing.List[UpdateThreadTagRequest]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
