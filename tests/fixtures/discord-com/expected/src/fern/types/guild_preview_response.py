

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .emoji_response import EmojiResponse
from .guild_features import GuildFeatures
from .guild_sticker_response import GuildStickerResponse
from .snowflake_type import SnowflakeType


class GuildPreviewResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    icon: typing.Optional[str] = None
    description: typing.Optional[str] = None
    home_header: typing.Optional[str] = None
    splash: typing.Optional[str] = None
    discovery_splash: typing.Optional[str] = None
    features: typing.List[GuildFeatures]
    approximate_member_count: int
    approximate_presence_count: int
    emojis: typing.List[EmojiResponse]
    stickers: typing.List[GuildStickerResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
