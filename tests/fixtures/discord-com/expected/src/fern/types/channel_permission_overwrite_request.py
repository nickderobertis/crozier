

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_overwrites import ChannelPermissionOverwrites
from .snowflake_type import SnowflakeType


class ChannelPermissionOverwriteRequest(UniversalBaseModel):
    id: SnowflakeType
    type: typing.Optional[ChannelPermissionOverwrites] = None
    allow: typing.Optional[int] = None
    deny: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
