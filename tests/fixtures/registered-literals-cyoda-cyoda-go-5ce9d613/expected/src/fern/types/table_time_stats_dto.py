

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .table_operation_stats_dto import TableOperationStatsDto
from .time_stat_data_dto import TimeStatDataDto


class TableTimeStatsDto(UniversalBaseModel):
    """
    Detailed execution statistics for a Cassandra table, including timing distributions and operation breakdowns
    """

    table: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Cassandra table
    """

    table_stats: typing_extensions.Annotated[
        typing.Optional[TimeStatDataDto],
        FieldMetadata(alias="tableStats"),
        pydantic.Field(alias="tableStats", description="Detailed timing statistics for all operations on this table"),
    ] = None
    """
    Detailed timing statistics for all operations on this table
    """

    operation_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[TableOperationStatsDto]],
        FieldMetadata(alias="operationStats"),
        pydantic.Field(
            alias="operationStats",
            description="Per-operation timing statistics breakdown (SELECT, INSERT, UPDATE, DELETE, etc.)",
        ),
    ] = None
    """
    Per-operation timing statistics breakdown (SELECT, INSERT, UPDATE, DELETE, etc.)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
