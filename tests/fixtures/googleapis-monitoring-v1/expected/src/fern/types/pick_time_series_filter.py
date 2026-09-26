

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .interval import Interval
from .pick_time_series_filter_direction import PickTimeSeriesFilterDirection
from .pick_time_series_filter_ranking_method import PickTimeSeriesFilterRankingMethod


class PickTimeSeriesFilter(UniversalBaseModel):
    """
    Describes a ranking-based time series filter. Each input time series is ranked with an aligner. The filter will allow up to num_time_series time series to pass through it, selecting them based on the relative ranking.For example, if ranking_method is METHOD_MEAN,direction is BOTTOM, and num_time_series is 3, then the 3 times series with the lowest mean values will pass through the filter.
    """

    direction: typing.Optional[PickTimeSeriesFilterDirection] = pydantic.Field(default=None)
    """
    How to use the ranking to select time series that pass through the filter.
    """

    interval: typing.Optional[Interval] = pydantic.Field(default=None)
    """
    Select the top N streams/time series within this time interval
    """

    num_time_series: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numTimeSeries"),
        pydantic.Field(alias="numTimeSeries", description="How many time series to allow to pass through the filter."),
    ] = None
    """
    How many time series to allow to pass through the filter.
    """

    ranking_method: typing_extensions.Annotated[
        typing.Optional[PickTimeSeriesFilterRankingMethod],
        FieldMetadata(alias="rankingMethod"),
        pydantic.Field(
            alias="rankingMethod",
            description="ranking_method is applied to each time series independently to produce the value which will be used to compare the time series to other time series.",
        ),
    ] = None
    """
    ranking_method is applied to each time series independently to produce the value which will be used to compare the time series to other time series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
