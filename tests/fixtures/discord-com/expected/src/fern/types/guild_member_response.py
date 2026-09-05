

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .user_avatar_decoration_response import UserAvatarDecorationResponse
from .user_response import UserResponse


class GuildMemberResponse(UniversalBaseModel):
    avatar: typing.Optional[str] = None
    avatar_decoration_data: typing.Optional[UserAvatarDecorationResponse] = None
    banner: typing.Optional[str] = None
    communication_disabled_until: typing.Optional[dt.datetime] = None
    flags: int
    joined_at: dt.datetime
    nick: typing.Optional[str] = None
    pending: bool
    premium_since: typing.Optional[dt.datetime] = None
    roles: typing.List[SnowflakeType]
    user: UserResponse
    mute: bool
    deaf: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
