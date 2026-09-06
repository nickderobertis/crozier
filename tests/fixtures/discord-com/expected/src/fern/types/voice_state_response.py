

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_member_response import GuildMemberResponse
from .snowflake_type import SnowflakeType


class VoiceStateResponse(UniversalBaseModel):
    channel_id: typing.Optional[SnowflakeType] = None
    deaf: bool
    guild_id: typing.Optional[SnowflakeType] = None
    member: typing.Optional[GuildMemberResponse] = None
    mute: bool
    request_to_speak_timestamp: typing.Optional[dt.datetime] = None
    suppress: bool
    self_stream: typing.Optional[bool] = None
    self_deaf: bool
    self_mute: bool
    self_video: bool
    session_id: str
    user_id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
