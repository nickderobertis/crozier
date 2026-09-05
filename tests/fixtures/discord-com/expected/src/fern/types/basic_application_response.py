

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_types import ApplicationTypes
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class BasicApplicationResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    icon: typing.Optional[str] = None
    description: str
    type: typing.Optional[ApplicationTypes] = None
    cover_image: typing.Optional[str] = None
    primary_sku_id: typing.Optional[SnowflakeType] = None
    bot: typing.Optional[UserResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
