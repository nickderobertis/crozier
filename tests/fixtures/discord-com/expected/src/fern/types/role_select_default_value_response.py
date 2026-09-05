

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role_select_default_value_response_type import RoleSelectDefaultValueResponseType
from .snowflake_type import SnowflakeType


class RoleSelectDefaultValueResponse(UniversalBaseModel):
    type: RoleSelectDefaultValueResponseType
    id: SnowflakeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
