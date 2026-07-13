

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity(UniversalBaseModel):
    """
    If you are playing in an activity, this is some information about it.
    Note that we cannot guarantee any of this resembles what ends up in the PGCR in any way. They are sourced by two entirely separate systems with their own logic, and the one we source this data from should be considered non-authoritative in comparison.
    """

    end_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="endTime")] = (
        pydantic.Field(default=None)
    )
    """
    If you're still in it but it "ended" (like when folks are dancing around the loot after they beat a boss), this is when the activity ended.
    """

    highest_opposing_faction_score: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="highestOpposingFactionScore")
    ] = pydantic.Field(default=None)
    """
    If you have human opponents, this is the highest opposing team's score.
    """

    number_of_opponents: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="numberOfOpponents")] = (
        pydantic.Field(default=None)
    )
    """
    This is how many human or poorly crafted aimbot opponents you have.
    """

    number_of_players: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="numberOfPlayers")] = (
        pydantic.Field(default=None)
    )
    """
    This is how many human or poorly crafted aimbots are on your team.
    """

    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is what our non-authoritative source thought the score was.
    """

    start_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="startTime")] = (
        pydantic.Field(default=None)
    )
    """
    When the activity started.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
