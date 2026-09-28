

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dimension import Dimension
from .measure import Measure
from .time_series_query import TimeSeriesQuery


class PieChartDataSet(UniversalBaseModel):
    """
    Groups a time series query definition.
    """

    dimensions: typing.Optional[typing.List[Dimension]] = pydantic.Field(default=None)
    """
    A dimension is a structured label, class, or category for a set of measurements in your data.
    """

    measures: typing.Optional[typing.List[Measure]] = pydantic.Field(default=None)
    """
    A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.
    """

    min_alignment_period: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minAlignmentPeriod"),
        pydantic.Field(
            alias="minAlignmentPeriod",
            description="Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.",
        ),
    ] = None
    """
    Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.
    """

    slice_name_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sliceNameTemplate"),
        pydantic.Field(
            alias="sliceNameTemplate",
            description="Optional. A template for the name of the slice. This name will be displayed in the legend and the tooltip of the pie chart. It replaces the auto-generated names for the slices. For example, if the template is set to ${resource.labels.zone}, the zone's value will be used for the name instead of the default name.",
        ),
    ] = None
    """
    Optional. A template for the name of the slice. This name will be displayed in the legend and the tooltip of the pie chart. It replaces the auto-generated names for the slices. For example, if the template is set to ${resource.labels.zone}, the zone's value will be used for the name instead of the default name.
    """

    time_series_query: typing_extensions.Annotated[
        typing.Optional[TimeSeriesQuery],
        FieldMetadata(alias="timeSeriesQuery"),
        pydantic.Field(
            alias="timeSeriesQuery",
            description="Required. The query for the PieChart. See, google.monitoring.dashboard.v1.TimeSeriesQuery.",
        ),
    ] = None
    """
    Required. The query for the PieChart. See, google.monitoring.dashboard.v1.TimeSeriesQuery.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
