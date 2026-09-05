

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class PrivateGroupChannelResponse(UniversalBaseModel):
    id: SnowflakeType
    type: int
    last_message_id: typing.Optional[SnowflakeType] = None
    flags: int
    last_pin_timestamp: typing.Optional[dt.datetime] = None
    recipients: typing.List[UserResponse]
    name: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    owner_id: typing.Optional[SnowflakeType] = None
    managed: typing.Optional[bool] = None
    application_id: typing.Optional[SnowflakeType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
