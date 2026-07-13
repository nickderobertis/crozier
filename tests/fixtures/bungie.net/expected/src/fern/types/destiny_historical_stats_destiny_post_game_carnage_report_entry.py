

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue
from .destiny_historical_stats_destiny_player import DestinyHistoricalStatsDestinyPlayer
from .destiny_historical_stats_destiny_post_game_carnage_report_extended_data import (
    DestinyHistoricalStatsDestinyPostGameCarnageReportExtendedData,
)


class DestinyHistoricalStatsDestinyPostGameCarnageReportEntry(UniversalBaseModel):
    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = (
        pydantic.Field(default=None)
    )
    """
    ID of the player's character used in the activity.
    """

    extended: typing.Optional[DestinyHistoricalStatsDestinyPostGameCarnageReportExtendedData] = pydantic.Field(
        default=None
    )
    """
    Extended data extracted from the activity blob.
    """

    player: typing.Optional[DestinyHistoricalStatsDestinyPlayer] = pydantic.Field(default=None)
    """
    Identity details of the player
    """

    score: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValue] = pydantic.Field(default=None)
    """
    Score of the player if available
    """

    standing: typing.Optional[int] = pydantic.Field(default=None)
    """
    Standing of the player
    """

    values: typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]] = pydantic.Field(
        default=None
    )
    """
    Collection of stats for the player in this activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
