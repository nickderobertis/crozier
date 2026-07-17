

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_activity import DestinyDestinyActivity


class DestinyEntitiesCharactersDestinyCharacterActivitiesComponent(UniversalBaseModel):
    """
    This component holds activity data for a character. It will tell you about the character's current activity status, as well as activities that are available to the user.
    """

    available_activities: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyActivity]],
        FieldMetadata(alias="availableActivities"),
        pydantic.Field(alias="availableActivities", description="The list of activities that the user can play."),
    ] = None
    """
    The list of activities that the user can play.
    """

    current_activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentActivityHash"),
        pydantic.Field(
            alias="currentActivityHash",
            description="If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP \"Activities\" are just maps: it's the ActivityMode that determines what type of PVP game they're playing.",
        ),
    ] = None
    """
    If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP "Activities" are just maps: it's the ActivityMode that determines what type of PVP game they're playing.
    """

    current_activity_mode_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentActivityModeHash"),
        pydantic.Field(
            alias="currentActivityModeHash",
            description="If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.",
        ),
    ] = None
    """
    If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
    """

    current_activity_mode_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="currentActivityModeHashes"),
        pydantic.Field(
            alias="currentActivityModeHashes",
            description="If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.",
        ),
    ] = None
    """
    If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
    """

    current_activity_mode_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentActivityModeType"),
        pydantic.Field(
            alias="currentActivityModeType",
            description="And the current activity's most specific mode type, if it can be found.",
        ),
    ] = None
    """
    And the current activity's most specific mode type, if it can be found.
    """

    current_activity_mode_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="currentActivityModeTypes"),
        pydantic.Field(
            alias="currentActivityModeTypes",
            description="All Activity Modes that apply to the current activity being played, in enum form.",
        ),
    ] = None
    """
    All Activity Modes that apply to the current activity being played, in enum form.
    """

    current_playlist_activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentPlaylistActivityHash"),
        pydantic.Field(
            alias="currentPlaylistActivityHash",
            description="If the user is in a playlist, this is the hash identifier for the playlist that they chose.",
        ),
    ] = None
    """
    If the user is in a playlist, this is the hash identifier for the playlist that they chose.
    """

    date_activity_started: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateActivityStarted"),
        pydantic.Field(
            alias="dateActivityStarted", description="The last date that the user started playing an activity."
        ),
    ] = None
    """
    The last date that the user started playing an activity.
    """

    last_completed_story_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastCompletedStoryHash"),
        pydantic.Field(
            alias="lastCompletedStoryHash",
            description="This will have the activity hash of the last completed story/campaign mission, in case you care about that.",
        ),
    ] = None
    """
    This will have the activity hash of the last completed story/campaign mission, in case you care about that.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
