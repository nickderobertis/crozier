

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_historical_stats_destiny_historical_stats_by_period import (
    DestinyHistoricalStatsDestinyHistoricalStatsByPeriod,
)


class DestinyHistoricalStatsDestinyHistoricalStatsWithMerged(UniversalBaseModel):
    merged: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsByPeriod] = None
    results: typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsByPeriod]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
