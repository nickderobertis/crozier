

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType


class CreateGuildInviteRequest(UniversalBaseModel):
    max_age: typing.Optional[int] = None
    temporary: typing.Optional[bool] = None
    max_uses: typing.Optional[int] = None
    unique: typing.Optional[bool] = None
    target_user_id: typing.Optional[SnowflakeType] = None
    target_application_id: typing.Optional[SnowflakeType] = None
    target_type: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
