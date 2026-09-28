

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .axis import Axis
from .chart_options import ChartOptions
from .data_set import DataSet
from .threshold import Threshold


class XyChart(UniversalBaseModel):
    """
    A chart that displays data on a 2D (X and Y axes) plane.
    """

    chart_options: typing_extensions.Annotated[
        typing.Optional[ChartOptions],
        FieldMetadata(alias="chartOptions"),
        pydantic.Field(alias="chartOptions", description="Display options for the chart."),
    ] = None
    """
    Display options for the chart.
    """

    data_sets: typing_extensions.Annotated[
        typing.Optional[typing.List[DataSet]],
        FieldMetadata(alias="dataSets"),
        pydantic.Field(alias="dataSets", description="Required. The data displayed in this chart."),
    ] = None
    """
    Required. The data displayed in this chart.
    """

    thresholds: typing.Optional[typing.List[Threshold]] = pydantic.Field(default=None)
    """
    Threshold lines drawn horizontally across the chart.
    """

    timeshift_duration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeshiftDuration"),
        pydantic.Field(
            alias="timeshiftDuration",
            description="The duration used to display a comparison chart. A comparison chart simultaneously shows values from two similar-length time periods (e.g., week-over-week metrics). The duration must be positive, and it can only be applied to charts with data sets of LINE plot type.",
        ),
    ] = None
    """
    The duration used to display a comparison chart. A comparison chart simultaneously shows values from two similar-length time periods (e.g., week-over-week metrics). The duration must be positive, and it can only be applied to charts with data sets of LINE plot type.
    """

    x_axis: typing_extensions.Annotated[
        typing.Optional[Axis],
        FieldMetadata(alias="xAxis"),
        pydantic.Field(alias="xAxis", description="The properties applied to the x-axis."),
    ] = None
    """
    The properties applied to the x-axis.
    """

    y2axis: typing_extensions.Annotated[
        typing.Optional[Axis],
        FieldMetadata(alias="y2Axis"),
        pydantic.Field(alias="y2Axis", description="The properties applied to the y2-axis."),
    ] = None
    """
    The properties applied to the y2-axis.
    """

    y_axis: typing_extensions.Annotated[
        typing.Optional[Axis],
        FieldMetadata(alias="yAxis"),
        pydantic.Field(alias="yAxis", description="The properties applied to the y-axis."),
    ] = None
    """
    The properties applied to the y-axis.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
