

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_member_response import GuildMemberResponse
from .snowflake_type import SnowflakeType


class ThreadMemberResponse(UniversalBaseModel):
    id: SnowflakeType
    user_id: SnowflakeType
    join_timestamp: dt.datetime
    flags: int
    member: typing.Optional[GuildMemberResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
