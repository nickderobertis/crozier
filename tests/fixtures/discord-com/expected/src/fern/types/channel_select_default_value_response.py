

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_select_default_value_response_type import ChannelSelectDefaultValueResponseType
from .snowflake_type import SnowflakeType


class ChannelSelectDefaultValueResponse(UniversalBaseModel):
    type: ChannelSelectDefaultValueResponseType
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
