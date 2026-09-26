

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .empty import Empty
from .gauge_view import GaugeView
from .spark_chart_view import SparkChartView
from .threshold import Threshold
from .time_series_query import TimeSeriesQuery


class Scorecard(UniversalBaseModel):
    """
    A widget showing the latest value of a metric, and how this value relates to one or more thresholds.
    """

    blank_view: typing_extensions.Annotated[
        typing.Optional[Empty],
        FieldMetadata(alias="blankView"),
        pydantic.Field(
            alias="blankView",
            description="Will cause the Scorecard to show only the value, with no indicator to its value relative to its thresholds.",
        ),
    ] = None
    """
    Will cause the Scorecard to show only the value, with no indicator to its value relative to its thresholds.
    """

    gauge_view: typing_extensions.Annotated[
        typing.Optional[GaugeView],
        FieldMetadata(alias="gaugeView"),
        pydantic.Field(alias="gaugeView", description="Will cause the scorecard to show a gauge chart."),
    ] = None
    """
    Will cause the scorecard to show a gauge chart.
    """

    spark_chart_view: typing_extensions.Annotated[
        typing.Optional[SparkChartView],
        FieldMetadata(alias="sparkChartView"),
        pydantic.Field(alias="sparkChartView", description="Will cause the scorecard to show a spark chart."),
    ] = None
    """
    Will cause the scorecard to show a spark chart.
    """

    thresholds: typing.Optional[typing.List[Threshold]] = pydantic.Field(default=None)
    """
    The thresholds used to determine the state of the scorecard given the time series' current value. For an actual value x, the scorecard is in a danger state if x is less than or equal to a danger threshold that triggers below, or greater than or equal to a danger threshold that triggers above. Similarly, if x is above/below a warning threshold that triggers above/below, then the scorecard is in a warning state - unless x also puts it in a danger state. (Danger trumps warning.)As an example, consider a scorecard with the following four thresholds: { value: 90, category: 'DANGER', trigger: 'ABOVE', }, { value: 70, category: 'WARNING', trigger: 'ABOVE', }, { value: 10, category: 'DANGER', trigger: 'BELOW', }, { value: 20, category: 'WARNING', trigger: 'BELOW', } Then: values less than or equal to 10 would put the scorecard in a DANGER state, values greater than 10 but less than or equal to 20 a WARNING state, values strictly between 20 and 70 an OK state, values greater than or equal to 70 but less than 90 a WARNING state, and values greater than or equal to 90 a DANGER state.
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
