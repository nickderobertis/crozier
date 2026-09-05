

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_role_tags_response import GuildRoleTagsResponse
from .snowflake_type import SnowflakeType


class GuildRoleResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    description: typing.Optional[str] = None
    permissions: str
    position: int
    color: int
    hoist: bool
    managed: bool
    mentionable: bool
    icon: typing.Optional[str] = None
    unicode_emoji: typing.Optional[str] = None
    tags: typing.Optional[GuildRoleTagsResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
