

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_overwrite_response import ChannelPermissionOverwriteResponse
from .default_reaction_emoji_response import DefaultReactionEmojiResponse
from .forum_layout import ForumLayout
from .guild_template_channel_tags import GuildTemplateChannelTags
from .icon_emoji_response import IconEmojiResponse
from .snowflake_type import SnowflakeType
from .thread_auto_archive_duration import ThreadAutoArchiveDuration
from .thread_sort_order import ThreadSortOrder


class GuildTemplateChannelResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    type: int
    name: typing.Optional[str] = None
    position: typing.Optional[int] = None
    topic: typing.Optional[str] = None
    bitrate: int
    user_limit: int
    nsfw: bool
    rate_limit_per_user: int
    parent_id: typing.Optional[SnowflakeType] = None
    default_auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    permission_overwrites: typing.List[typing.Optional[ChannelPermissionOverwriteResponse]]
    available_tags: typing.Optional[typing.List[GuildTemplateChannelTags]] = None
    template: str
    default_reaction_emoji: typing.Optional[DefaultReactionEmojiResponse] = None
    default_thread_rate_limit_per_user: typing.Optional[int] = None
    default_sort_order: typing.Optional[ThreadSortOrder] = None
    default_forum_layout: typing.Optional[ForumLayout] = None
    icon_emoji: typing.Optional[IconEmojiResponse] = None
    theme_color: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
