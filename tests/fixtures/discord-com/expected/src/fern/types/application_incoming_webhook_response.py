

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class ApplicationIncomingWebhookResponse(UniversalBaseModel):
    application_id: typing.Optional[SnowflakeType] = None
    avatar: typing.Optional[str] = None
    channel_id: typing.Optional[SnowflakeType] = None
    guild_id: typing.Optional[SnowflakeType] = None
    id: SnowflakeType
    name: str
    type: int
    user: typing.Optional[UserResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
