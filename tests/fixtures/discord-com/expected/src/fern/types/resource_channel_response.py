

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .settings_emoji_response import SettingsEmojiResponse
from .snowflake_type import SnowflakeType


class ResourceChannelResponse(UniversalBaseModel):
    channel_id: SnowflakeType
    title: str
    emoji: typing.Optional[SettingsEmojiResponse] = None
    icon: typing.Optional[str] = None
    description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
