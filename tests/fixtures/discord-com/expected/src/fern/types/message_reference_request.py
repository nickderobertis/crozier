

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_reference_type import MessageReferenceType
from .snowflake_type import SnowflakeType


class MessageReferenceRequest(UniversalBaseModel):
    guild_id: typing.Optional[SnowflakeType] = None
    channel_id: typing.Optional[SnowflakeType] = None
    message_id: SnowflakeType
    fail_if_not_exists: typing.Optional[bool] = None
    type: typing.Optional[MessageReferenceType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
