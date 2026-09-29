

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_connection_info import MssqlConnectionInfo


class MssqlConnConfiguration(UniversalBaseModel):
    connection_info: MssqlConnectionInfo
    read_replicas: typing.Optional[typing.List[MssqlConnectionInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
