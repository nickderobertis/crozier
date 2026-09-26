

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aggregation import Aggregation
from .pick_time_series_filter import PickTimeSeriesFilter
from .statistical_time_series_filter import StatisticalTimeSeriesFilter


class TimeSeriesFilter(UniversalBaseModel):
    """
    A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the ListTimeSeries (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.
    """

    aggregation: typing.Optional[Aggregation] = pydantic.Field(default=None)
    """
    By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.
    """

    filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.
    """

    pick_time_series_filter: typing_extensions.Annotated[
        typing.Optional[PickTimeSeriesFilter],
        FieldMetadata(alias="pickTimeSeriesFilter"),
        pydantic.Field(alias="pickTimeSeriesFilter", description="Ranking based time series filter."),
    ] = None
    """
    Ranking based time series filter.
    """

    secondary_aggregation: typing_extensions.Annotated[
        typing.Optional[Aggregation],
        FieldMetadata(alias="secondaryAggregation"),
        pydantic.Field(
            alias="secondaryAggregation", description="Apply a second aggregation after aggregation is applied."
        ),
    ] = None
    """
    Apply a second aggregation after aggregation is applied.
    """

    statistical_time_series_filter: typing_extensions.Annotated[
        typing.Optional[StatisticalTimeSeriesFilter],
        FieldMetadata(alias="statisticalTimeSeriesFilter"),
        pydantic.Field(
            alias="statisticalTimeSeriesFilter",
            description="Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.",
        ),
    ] = None
    """
    Statistics based time series filter. Note: This field is deprecated and completely ignored by the API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
