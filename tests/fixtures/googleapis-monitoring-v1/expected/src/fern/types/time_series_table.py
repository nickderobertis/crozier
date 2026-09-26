

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_settings import ColumnSettings
from .table_data_set import TableDataSet
from .time_series_table_metric_visualization import TimeSeriesTableMetricVisualization


class TimeSeriesTable(UniversalBaseModel):
    """
    A table that displays time series data.
    """

    column_settings: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnSettings]],
        FieldMetadata(alias="columnSettings"),
        pydantic.Field(
            alias="columnSettings", description="Optional. The list of the persistent column settings for the table."
        ),
    ] = None
    """
    Optional. The list of the persistent column settings for the table.
    """

    data_sets: typing_extensions.Annotated[
        typing.Optional[typing.List[TableDataSet]],
        FieldMetadata(alias="dataSets"),
        pydantic.Field(alias="dataSets", description="Required. The data displayed in this table."),
    ] = None
    """
    Required. The data displayed in this table.
    """

    metric_visualization: typing_extensions.Annotated[
        typing.Optional[TimeSeriesTableMetricVisualization],
        FieldMetadata(alias="metricVisualization"),
        pydantic.Field(alias="metricVisualization", description="Optional. Store rendering strategy"),
    ] = None
    """
    Optional. Store rendering strategy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
