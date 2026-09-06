

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interaction_types import InteractionTypes
from .snowflake_type import SnowflakeType


class InteractionResponse(UniversalBaseModel):
    id: SnowflakeType
    type: InteractionTypes
    response_message_id: typing.Optional[SnowflakeType] = None
    response_message_loading: typing.Optional[bool] = None
    response_message_ephemeral: typing.Optional[bool] = None
    channel_id: typing.Optional[SnowflakeType] = None
    guild_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
