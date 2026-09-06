

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .view_options_chart_annotations_chart_annotations_item import ViewOptionsChartAnnotationsChartAnnotationsItem
from .view_options_chart_annotations_excluded_measures_item import ViewOptionsChartAnnotationsExcludedMeasuresItem
from .view_options_chart_annotations_query_shape import ViewOptionsChartAnnotationsQueryShape
from .view_options_chart_annotations_symbol_grouping import ViewOptionsChartAnnotationsSymbolGrouping
from .view_options_chart_annotations_time_range_filter import ViewOptionsChartAnnotationsTimeRangeFilter
from .view_options_chart_annotations_x_axis import ViewOptionsChartAnnotationsXAxis
from .view_options_chart_annotations_y_metric import ViewOptionsChartAnnotationsYMetric


class ViewOptionsChartAnnotations(UniversalBaseModel):
    column_visibility: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[bool]]],
        FieldMetadata(alias="columnVisibility"),
        pydantic.Field(alias="columnVisibility"),
    ] = None
    column_order: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="columnOrder"), pydantic.Field(alias="columnOrder")
    ] = None
    column_sizing: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[float]]],
        FieldMetadata(alias="columnSizing"),
        pydantic.Field(alias="columnSizing"),
    ] = None
    grouping: typing.Optional[str] = None
    row_height: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rowHeight"), pydantic.Field(alias="rowHeight")
    ] = None
    tall_group_rows: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tallGroupRows"), pydantic.Field(alias="tallGroupRows")
    ] = None
    layout: typing.Optional[str] = None
    chart_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="chartHeight"), pydantic.Field(alias="chartHeight")
    ] = None
    excluded_measures: typing_extensions.Annotated[
        typing.Optional[typing.List[ViewOptionsChartAnnotationsExcludedMeasuresItem]],
        FieldMetadata(alias="excludedMeasures"),
        pydantic.Field(alias="excludedMeasures"),
    ] = None
    y_metric: typing_extensions.Annotated[
        typing.Optional[ViewOptionsChartAnnotationsYMetric],
        FieldMetadata(alias="yMetric"),
        pydantic.Field(alias="yMetric"),
    ] = None
    x_axis: typing_extensions.Annotated[
        typing.Optional[ViewOptionsChartAnnotationsXAxis], FieldMetadata(alias="xAxis"), pydantic.Field(alias="xAxis")
    ] = None
    symbol_grouping: typing_extensions.Annotated[
        typing.Optional[ViewOptionsChartAnnotationsSymbolGrouping],
        FieldMetadata(alias="symbolGrouping"),
        pydantic.Field(alias="symbolGrouping"),
    ] = None
    x_axis_aggregation: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="xAxisAggregation"),
        pydantic.Field(alias="xAxisAggregation", description="One of 'avg', 'sum', 'min', 'max', 'median', 'all'"),
    ] = None
    """
    One of 'avg', 'sum', 'min', 'max', 'median', 'all'
    """

    chart_annotations: typing_extensions.Annotated[
        typing.Optional[typing.List[ViewOptionsChartAnnotationsChartAnnotationsItem]],
        FieldMetadata(alias="chartAnnotations"),
        pydantic.Field(alias="chartAnnotations"),
    ] = None
    time_range_filter: typing_extensions.Annotated[
        typing.Optional[ViewOptionsChartAnnotationsTimeRangeFilter],
        FieldMetadata(alias="timeRangeFilter"),
        pydantic.Field(alias="timeRangeFilter"),
    ] = None
    query_shape: typing_extensions.Annotated[
        typing.Optional[ViewOptionsChartAnnotationsQueryShape],
        FieldMetadata(alias="queryShape"),
        pydantic.Field(alias="queryShape"),
    ] = None
    freeze_columns: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="freezeColumns"), pydantic.Field(alias="freezeColumns")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
