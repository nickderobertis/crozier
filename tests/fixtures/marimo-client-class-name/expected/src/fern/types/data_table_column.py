

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_table_column_type import DataTableColumnType


class DataTableColumn(UniversalBaseModel):
    """
    Represents a column in a data table.

    Attributes:
        name (str): The name of the column.
        type (DataType): The data type of the column.
        external_type (ExternalDataType): The raw data type of the column.
        sample_values (List[Any]): The sample values of the column.
    """

    external_type: str
    name: str
    sample_values: typing.List[typing.Any]
    type: DataTableColumnType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
