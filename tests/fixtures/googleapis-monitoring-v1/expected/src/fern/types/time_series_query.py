

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ops_analytics_query import OpsAnalyticsQuery
from .time_series_filter import TimeSeriesFilter
from .time_series_filter_ratio import TimeSeriesFilterRatio


class TimeSeriesQuery(UniversalBaseModel):
    """
    TimeSeriesQuery collects the set of supported methods for querying time series data from the Stackdriver metrics API.
    """

    ops_analytics_query: typing_extensions.Annotated[
        typing.Optional[OpsAnalyticsQuery],
        FieldMetadata(alias="opsAnalyticsQuery"),
        pydantic.Field(
            alias="opsAnalyticsQuery",
            description="Preview: A query used to fetch a time series, category series, or numeric series with SQL. This is a preview feature and may be subject to change before final release.",
        ),
    ] = None
    """
    Preview: A query used to fetch a time series, category series, or numeric series with SQL. This is a preview feature and may be subject to change before final release.
    """

    output_full_duration: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="outputFullDuration"),
        pydantic.Field(
            alias="outputFullDuration",
            description="Optional. If set, Cloud Monitoring will treat the full query duration as the alignment period so that there will be only 1 output value.*Note: This could override the configured alignment period except for the cases where a series of data points are expected, like - XyChart - Scorecard's spark chart",
        ),
    ] = None
    """
    Optional. If set, Cloud Monitoring will treat the full query duration as the alignment period so that there will be only 1 output value.*Note: This could override the configured alignment period except for the cases where a series of data points are expected, like - XyChart - Scorecard's spark chart
    """

    prometheus_query: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prometheusQuery"),
        pydantic.Field(alias="prometheusQuery", description="A query used to fetch time series with PromQL."),
    ] = None
    """
    A query used to fetch time series with PromQL.
    """

    time_series_filter: typing_extensions.Annotated[
        typing.Optional[TimeSeriesFilter],
        FieldMetadata(alias="timeSeriesFilter"),
        pydantic.Field(alias="timeSeriesFilter", description="Filter parameters to fetch time series."),
    ] = None
    """
    Filter parameters to fetch time series.
    """

    time_series_filter_ratio: typing_extensions.Annotated[
        typing.Optional[TimeSeriesFilterRatio],
        FieldMetadata(alias="timeSeriesFilterRatio"),
        pydantic.Field(
            alias="timeSeriesFilterRatio", description="Parameters to fetch a ratio between two time series filters."
        ),
    ] = None
    """
    Parameters to fetch a ratio between two time series filters.
    """

    time_series_query_language: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeSeriesQueryLanguage"),
        pydantic.Field(alias="timeSeriesQueryLanguage", description="A query used to fetch time series with MQL."),
    ] = None
    """
    A query used to fetch time series with MQL.
    """

    unit_override: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitOverride"),
        pydantic.Field(
            alias="unitOverride",
            description="The unit of data contained in fetched time series. If non-empty, this unit will override any unit that accompanies fetched data. The format is the same as the unit (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors) field in MetricDescriptor.",
        ),
    ] = None
    """
    The unit of data contained in fetched time series. If non-empty, this unit will override any unit that accompanies fetched data. The format is the same as the unit (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors) field in MetricDescriptor.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
