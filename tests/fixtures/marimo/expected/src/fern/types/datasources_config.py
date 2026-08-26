

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .datasources_config_auto_discover_columns import DatasourcesConfigAutoDiscoverColumns
from .datasources_config_auto_discover_schemas import DatasourcesConfigAutoDiscoverSchemas
from .datasources_config_auto_discover_tables import DatasourcesConfigAutoDiscoverTables


class DatasourcesConfig(UniversalBaseModel):
    """
    Configuration for datasources panel.

        **Keys.**

        - `auto_discover_schemas`: if `True`, include schemas in the datasource
        - `auto_discover_tables`: if `True`, include tables in the datasource
        - `auto_discover_columns`: if `True`, include columns & table metadata in the datasource
    """

    auto_discover_columns: typing.Optional[DatasourcesConfigAutoDiscoverColumns] = None
    auto_discover_schemas: typing.Optional[DatasourcesConfigAutoDiscoverSchemas] = None
    auto_discover_tables: typing.Optional[DatasourcesConfigAutoDiscoverTables] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
