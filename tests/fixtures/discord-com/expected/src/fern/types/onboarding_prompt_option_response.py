

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .settings_emoji_response import SettingsEmojiResponse
from .snowflake_type import SnowflakeType


class OnboardingPromptOptionResponse(UniversalBaseModel):
    id: SnowflakeType
    title: str
    description: str
    emoji: SettingsEmojiResponse
    role_ids: typing.List[SnowflakeType]
    channel_ids: typing.List[SnowflakeType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
