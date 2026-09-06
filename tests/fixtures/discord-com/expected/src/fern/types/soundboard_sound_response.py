

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class SoundboardSoundResponse(UniversalBaseModel):
    name: str
    sound_id: SnowflakeType
    volume: float
    emoji_id: typing.Optional[SnowflakeType] = None
    emoji_name: typing.Optional[str] = None
    guild_id: typing.Optional[SnowflakeType] = None
    available: bool
    user: typing.Optional[UserResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
