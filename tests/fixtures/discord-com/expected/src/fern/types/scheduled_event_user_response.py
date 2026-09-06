

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_member_response import GuildMemberResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class ScheduledEventUserResponse(UniversalBaseModel):
    guild_scheduled_event_id: SnowflakeType
    user_id: SnowflakeType
    user: typing.Optional[UserResponse] = None
    member: typing.Optional[GuildMemberResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
