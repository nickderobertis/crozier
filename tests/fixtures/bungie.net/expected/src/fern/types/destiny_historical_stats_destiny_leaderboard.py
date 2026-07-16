

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_leaderboard_entry import DestinyHistoricalStatsDestinyLeaderboardEntry


class DestinyHistoricalStatsDestinyLeaderboard(UniversalBaseModel):
    entries: typing.Optional[typing.List[DestinyHistoricalStatsDestinyLeaderboardEntry]] = None
    stat_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statId"), pydantic.Field(alias="statId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
