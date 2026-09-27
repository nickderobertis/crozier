

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aggregation import Aggregation
from .pick_time_series_filter import PickTimeSeriesFilter
from .ratio_part import RatioPart
from .statistical_time_series_filter import StatisticalTimeSeriesFilter


class TimeSeriesFilterRatio(UniversalBaseModel):
    """
    A pair of time series filters that define a ratio computation. The output time series is the pair-wise division of each aligned element from the numerator and denominator time series.
    """

    denominator: typing.Optional[RatioPart] = pydantic.Field(default=None)
    """
    The denominator of the ratio.
    """

    numerator: typing.Optional[RatioPart] = pydantic.Field(default=None)
    """
    The numerator of the ratio.
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
            alias="secondaryAggregation", description="Apply a second aggregation after the ratio is computed."
        ),
    ] = None
    """
    Apply a second aggregation after the ratio is computed.
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
