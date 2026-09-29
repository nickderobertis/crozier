

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_connection_info_connection_string import MssqlConnectionInfoConnectionString


class MssqlConnectionInfo(UniversalBaseModel):
    connection_string: MssqlConnectionInfoConnectionString
    isolation_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction isolation level in which the queries made to the source will be run with (default: read-committed).
    Isolation level
    """

    pool_settings: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
