

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_historical_stats_destiny_historical_stats_period_group import (
    DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup,
)


class DestinyHistoricalStatsDestinyActivityHistoryResults(UniversalBaseModel):
    activities: typing.Optional[typing.List[DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup]] = pydantic.Field(
        default=None
    )
    """
    List of activities, the most recent activity first.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
