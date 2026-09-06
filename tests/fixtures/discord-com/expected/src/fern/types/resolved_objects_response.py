

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_member_response import GuildMemberResponse
from .guild_role_response import GuildRoleResponse
from .resolved_objects_response_channels_value import ResolvedObjectsResponseChannelsValue
from .user_response import UserResponse


class ResolvedObjectsResponse(UniversalBaseModel):
    users: typing.Dict[str, UserResponse]
    members: typing.Dict[str, GuildMemberResponse]
    channels: typing.Dict[str, ResolvedObjectsResponseChannelsValue]
    roles: typing.Dict[str, GuildRoleResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
