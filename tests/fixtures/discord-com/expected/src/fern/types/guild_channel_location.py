

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_channel_location_kind import GuildChannelLocationKind
from .snowflake_type import SnowflakeType


class GuildChannelLocation(UniversalBaseModel):
    id: str
    kind: GuildChannelLocationKind
    channel_id: SnowflakeType
    guild_id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
