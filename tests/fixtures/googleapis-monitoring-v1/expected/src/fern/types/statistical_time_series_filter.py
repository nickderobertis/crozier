

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .statistical_time_series_filter_ranking_method import StatisticalTimeSeriesFilterRankingMethod


class StatisticalTimeSeriesFilter(UniversalBaseModel):
    """
    A filter that ranks streams based on their statistical relation to other streams in a request. Note: This field is deprecated and completely ignored by the API.
    """

    num_time_series: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numTimeSeries"),
        pydantic.Field(alias="numTimeSeries", description="How many time series to output."),
    ] = None
    """
    How many time series to output.
    """

    ranking_method: typing_extensions.Annotated[
        typing.Optional[StatisticalTimeSeriesFilterRankingMethod],
        FieldMetadata(alias="rankingMethod"),
        pydantic.Field(
            alias="rankingMethod",
            description="rankingMethod is applied to a set of time series, and then the produced value for each individual time series is used to compare a given time series to others. These are methods that cannot be applied stream-by-stream, but rather require the full context of a request to evaluate time series.",
        ),
    ] = None
    """
    rankingMethod is applied to a set of time series, and then the produced value for each individual time series is used to compare a given time series to others. These are methods that cannot be applied stream-by-stream, but rather require the full context of a request to evaluate time series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
