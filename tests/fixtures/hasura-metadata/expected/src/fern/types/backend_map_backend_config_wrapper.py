

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_connector_options import DataConnectorOptions


class BackendMapBackendConfigWrapper(UniversalBaseModel):
    bigquery: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    citus: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    cockroach: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    dataconnector: typing.Optional[typing.Dict[str, DataConnectorOptions]] = None
    mssql: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    postgres: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
