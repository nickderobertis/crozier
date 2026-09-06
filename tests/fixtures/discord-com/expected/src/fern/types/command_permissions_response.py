

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command_permission_response import CommandPermissionResponse
from .snowflake_type import SnowflakeType


class CommandPermissionsResponse(UniversalBaseModel):
    id: SnowflakeType
    application_id: SnowflakeType
    guild_id: SnowflakeType
    permissions: typing.List[CommandPermissionResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
