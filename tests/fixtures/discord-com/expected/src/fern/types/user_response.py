

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .int53type import Int53Type
from .snowflake_type import SnowflakeType
from .user_avatar_decoration_response import UserAvatarDecorationResponse
from .user_collectibles_response import UserCollectiblesResponse
from .user_primary_guild_response import UserPrimaryGuildResponse


class UserResponse(UniversalBaseModel):
    id: SnowflakeType
    username: str
    avatar: typing.Optional[str] = None
    discriminator: str
    public_flags: int
    flags: Int53Type
    bot: typing.Optional[bool] = None
    system: typing.Optional[bool] = None
    banner: typing.Optional[str] = None
    accent_color: typing.Optional[int] = None
    global_name: typing.Optional[str] = None
    avatar_decoration_data: typing.Optional[UserAvatarDecorationResponse] = None
    collectibles: typing.Optional[UserCollectiblesResponse] = None
    clan: typing.Optional[UserPrimaryGuildResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
