

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_table_column import DataTableColumn
from .data_table_source_type import DataTableSourceType
from .data_table_type import DataTableType
from .variable_name import VariableName


class DataTable(UniversalBaseModel):
    """
    Represents a data table.

    Attributes:
        source_type (DataTableSource): Type of data source ('local', 'duckdb', 'connection').
        source (str): Can be dialect, or source db name.
        name (str): Name of the data table.
        num_rows (Optional[int]): Total number of rows in the table, if known.
        num_columns (Optional[int]): Total number of columns in the table, if known.
        variable_name (Optional[VariableName]): Variable name referencing this table in code.
        columns (List[DataTableColumn]): List of column definitions and metadata.
        engine (Optional[VariableName]): Database engine or connection handler, if any.
        type (DataTableType): Table type, either 'table' or 'view'. Defaults to 'table'.
        primary_keys (Optional[List[str]]): Column names used as primary keys, if any.
        indexes (Optional[List[str]]): Column names used as indexes, if any.
    """

    columns: typing.List[DataTableColumn]
    engine: typing.Optional[VariableName] = None
    indexes: typing.Optional[typing.List[str]] = None
    name: str
    num_columns: typing.Optional[int] = None
    num_rows: typing.Optional[int] = None
    primary_keys: typing.Optional[typing.List[str]] = None
    source: str
    source_type: DataTableSourceType
    type: typing.Optional[DataTableType] = None
    variable_name: typing.Optional[VariableName] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
