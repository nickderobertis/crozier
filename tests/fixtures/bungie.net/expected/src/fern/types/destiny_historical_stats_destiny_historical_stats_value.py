

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value_pair import (
    DestinyHistoricalStatsDestinyHistoricalStatsValuePair,
)


class DestinyHistoricalStatsDestinyHistoricalStatsValue(UniversalBaseModel):
    activity_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityId")] = pydantic.Field(
        default=None
    )
    """
    When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property.
    """

    basic: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValuePair] = pydantic.Field(default=None)
    """
    Basic stat value.
    """

    pga: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValuePair] = pydantic.Field(default=None)
    """
    Per game average for the statistic, if applicable
    """

    stat_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="statId")] = pydantic.Field(
        default=None
    )
    """
    Unique ID for this stat
    """

    weighted: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValuePair] = pydantic.Field(default=None)
    """
    Weighted value of the stat if a weight greater than 1 has been assigned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
