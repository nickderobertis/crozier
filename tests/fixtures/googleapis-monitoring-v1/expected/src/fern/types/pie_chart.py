

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pie_chart_chart_type import PieChartChartType
from .pie_chart_data_set import PieChartDataSet


class PieChart(UniversalBaseModel):
    """
    A widget that displays timeseries data as a pie or a donut.
    """

    chart_type: typing_extensions.Annotated[
        typing.Optional[PieChartChartType],
        FieldMetadata(alias="chartType"),
        pydantic.Field(alias="chartType", description="Required. Indicates the visualization type for the PieChart."),
    ] = None
    """
    Required. Indicates the visualization type for the PieChart.
    """

    data_sets: typing_extensions.Annotated[
        typing.Optional[typing.List[PieChartDataSet]],
        FieldMetadata(alias="dataSets"),
        pydantic.Field(alias="dataSets", description="Required. The queries for the chart's data."),
    ] = None
    """
    Required. The queries for the chart's data.
    """

    show_labels: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showLabels"),
        pydantic.Field(
            alias="showLabels",
            description="Optional. Indicates whether or not the pie chart should show slices' labels",
        ),
    ] = None
    """
    Optional. Indicates whether or not the pie chart should show slices' labels
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
