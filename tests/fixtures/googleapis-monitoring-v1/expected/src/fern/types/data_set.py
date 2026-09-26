

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .breakdown import Breakdown
from .data_set_plot_type import DataSetPlotType
from .data_set_target_axis import DataSetTargetAxis
from .dimension import Dimension
from .measure import Measure
from .time_series_query import TimeSeriesQuery


class DataSet(UniversalBaseModel):
    """
    Groups a time series query definition with charting options.
    """

    breakdowns: typing.Optional[typing.List[Breakdown]] = pydantic.Field(default=None)
    """
    Optional. The collection of breakdowns to be applied to the dataset.
    """

    dimensions: typing.Optional[typing.List[Dimension]] = pydantic.Field(default=None)
    """
    Optional. A collection of dimension columns.
    """

    legend_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="legendTemplate"),
        pydantic.Field(
            alias="legendTemplate",
            description="A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label's value.",
        ),
    ] = None
    """
    A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label's value.
    """

    measures: typing.Optional[typing.List[Measure]] = pydantic.Field(default=None)
    """
    Optional. A collection of measures.
    """

    min_alignment_period: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minAlignmentPeriod"),
        pydantic.Field(
            alias="minAlignmentPeriod",
            description="Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.",
        ),
    ] = None
    """
    Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.
    """

    plot_type: typing_extensions.Annotated[
        typing.Optional[DataSetPlotType],
        FieldMetadata(alias="plotType"),
        pydantic.Field(alias="plotType", description="How this data should be plotted on the chart."),
    ] = None
    """
    How this data should be plotted on the chart.
    """

    target_axis: typing_extensions.Annotated[
        typing.Optional[DataSetTargetAxis],
        FieldMetadata(alias="targetAxis"),
        pydantic.Field(alias="targetAxis", description="Optional. The target axis to use for plotting the metric."),
    ] = None
    """
    Optional. The target axis to use for plotting the metric.
    """

    time_series_query: typing_extensions.Annotated[
        typing.Optional[TimeSeriesQuery],
        FieldMetadata(alias="timeSeriesQuery"),
        pydantic.Field(
            alias="timeSeriesQuery",
            description="Required. Fields for querying time series data from the Stackdriver metrics API.",
        ),
    ] = None
    """
    Required. Fields for querying time series data from the Stackdriver metrics API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
