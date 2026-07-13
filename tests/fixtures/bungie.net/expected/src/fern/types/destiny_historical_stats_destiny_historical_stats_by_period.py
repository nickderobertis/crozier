

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_period_group import (
    DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup,
)
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue


class DestinyHistoricalStatsDestinyHistoricalStatsByPeriod(UniversalBaseModel):
    all_time: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]],
        FieldMetadata(alias="allTime"),
    ] = None
    all_time_tier1: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]],
        FieldMetadata(alias="allTimeTier1"),
    ] = None
    all_time_tier2: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]],
        FieldMetadata(alias="allTimeTier2"),
    ] = None
    all_time_tier3: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]],
        FieldMetadata(alias="allTimeTier3"),
    ] = None
    daily: typing.Optional[typing.List[DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup]] = None
    monthly: typing.Optional[typing.List[DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
