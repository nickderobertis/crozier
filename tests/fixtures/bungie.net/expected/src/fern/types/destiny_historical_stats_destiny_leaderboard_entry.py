

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue
from .destiny_historical_stats_destiny_player import DestinyHistoricalStatsDestinyPlayer


class DestinyHistoricalStatsDestinyLeaderboardEntry(UniversalBaseModel):
    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = (
        pydantic.Field(default=None)
    )
    """
    ID of the player's best character for the reported stat.
    """

    player: typing.Optional[DestinyHistoricalStatsDestinyPlayer] = pydantic.Field(default=None)
    """
    Identity details of the player
    """

    rank: typing.Optional[int] = pydantic.Field(default=None)
    """
    Where this player ranks on the leaderboard. A value of 1 is the top rank.
    """

    value: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValue] = pydantic.Field(default=None)
    """
    Value of the stat for this player
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
