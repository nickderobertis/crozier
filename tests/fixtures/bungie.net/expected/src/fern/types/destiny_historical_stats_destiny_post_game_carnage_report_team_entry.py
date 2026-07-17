

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue


class DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry(UniversalBaseModel):
    score: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValue] = pydantic.Field(default=None)
    """
    Score earned by the team
    """

    standing: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValue] = pydantic.Field(default=None)
    """
    Team's standing relative to other teams.
    """

    team_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="teamId"),
        pydantic.Field(alias="teamId", description="Integer ID for the team."),
    ] = None
    """
    Integer ID for the team.
    """

    team_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="teamName"),
        pydantic.Field(alias="teamName", description="Alpha or Bravo"),
    ] = None
    """
    Alpha or Bravo
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
