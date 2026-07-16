

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_activity import (
    DestinyHistoricalStatsDestinyHistoricalStatsActivity,
)
from .destiny_historical_stats_destiny_post_game_carnage_report_entry import (
    DestinyHistoricalStatsDestinyPostGameCarnageReportEntry,
)
from .destiny_historical_stats_destiny_post_game_carnage_report_team_entry import (
    DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry,
)


class DestinyHistoricalStatsDestinyPostGameCarnageReportData(UniversalBaseModel):
    activity_details: typing_extensions.Annotated[
        typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsActivity],
        FieldMetadata(alias="activityDetails"),
        pydantic.Field(alias="activityDetails", description="Details about the activity."),
    ] = None
    """
    Details about the activity.
    """

    activity_was_started_from_beginning: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="activityWasStartedFromBeginning"),
        pydantic.Field(
            alias="activityWasStartedFromBeginning",
            description="True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release.",
        ),
    ] = None
    """
    True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release.
    """

    entries: typing.Optional[typing.List[DestinyHistoricalStatsDestinyPostGameCarnageReportEntry]] = pydantic.Field(
        default=None
    )
    """
    Collection of players and their data for this activity.
    """

    period: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date and time for the activity.
    """

    starting_phase_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="startingPhaseIndex"),
        pydantic.Field(
            alias="startingPhaseIndex",
            description='If this activity has "phases", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here.',
        ),
    ] = None
    """
    If this activity has "phases", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here.
    """

    teams: typing.Optional[typing.List[DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry]] = pydantic.Field(
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
