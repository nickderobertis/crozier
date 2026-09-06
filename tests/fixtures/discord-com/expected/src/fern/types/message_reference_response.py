

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_reference_type import MessageReferenceType
from .snowflake_type import SnowflakeType


class MessageReferenceResponse(UniversalBaseModel):
    type: typing.Optional[MessageReferenceType] = None
    channel_id: SnowflakeType
    message_id: typing.Optional[SnowflakeType] = None
    guild_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
