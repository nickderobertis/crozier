

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_historical_stats_destiny_aggregate_activity_stats import (
    DestinyHistoricalStatsDestinyAggregateActivityStats,
)


class DestinyHistoricalStatsDestinyAggregateActivityResults(UniversalBaseModel):
    activities: typing.Optional[typing.List[DestinyHistoricalStatsDestinyAggregateActivityStats]] = pydantic.Field(
        default=None
    )
    """
    List of all activities the player has participated in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
