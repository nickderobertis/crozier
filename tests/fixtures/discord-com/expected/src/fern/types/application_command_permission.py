

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_permission_type import ApplicationCommandPermissionType
from .snowflake_type import SnowflakeType


class ApplicationCommandPermission(UniversalBaseModel):
    id: SnowflakeType
    type: ApplicationCommandPermissionType
    permission: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
