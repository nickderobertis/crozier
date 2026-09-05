

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_types import ChannelTypes
from .snowflake_type import SnowflakeType


class MessageMentionChannelResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    type: ChannelTypes
    guild_id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
