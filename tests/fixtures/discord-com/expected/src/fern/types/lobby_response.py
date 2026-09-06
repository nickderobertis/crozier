

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_channel_response import GuildChannelResponse
from .lobby_member_response import LobbyMemberResponse
from .snowflake_type import SnowflakeType


class LobbyResponse(UniversalBaseModel):
    id: SnowflakeType
    application_id: SnowflakeType
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    members: typing.Optional[typing.List[LobbyMemberResponse]] = None
    linked_channel: typing.Optional[GuildChannelResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
