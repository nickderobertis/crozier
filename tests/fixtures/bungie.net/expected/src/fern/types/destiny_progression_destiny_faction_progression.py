

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_progression_reset_entry import DestinyDestinyProgressionResetEntry


class DestinyProgressionDestinyFactionProgression(UniversalBaseModel):
    """
    Mostly for historical purposes, we segregate Faction progressions from other progressions. This is just a DestinyProgression with a shortcut for finding the DestinyFactionDefinition of the faction related to the progression.
    """

    current_progress: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentProgress"),
        pydantic.Field(
            alias="currentProgress",
            description="This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)",
        ),
    ] = None
    """
    This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)
    """

    current_reset_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentResetCount"),
        pydantic.Field(
            alias="currentResetCount",
            description="The number of resets of this progression you've executed this season, if applicable to this progression.",
        ),
    ] = None
    """
    The number of resets of this progression you've executed this season, if applicable to this progression.
    """

    daily_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="dailyLimit"),
        pydantic.Field(alias="dailyLimit", description="If this progression has a daily limit, this is that limit."),
    ] = None
    """
    If this progression has a daily limit, this is that limit.
    """

    daily_progress: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="dailyProgress"),
        pydantic.Field(alias="dailyProgress", description="The amount of progress earned today for this progression."),
    ] = None
    """
    The amount of progress earned today for this progression.
    """

    faction_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="factionHash"),
        pydantic.Field(
            alias="factionHash",
            description="The hash identifier of the Faction related to this progression. Use it to look up the DestinyFactionDefinition for more rendering info.",
        ),
    ] = None
    """
    The hash identifier of the Faction related to this progression. Use it to look up the DestinyFactionDefinition for more rendering info.
    """

    faction_vendor_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="factionVendorIndex"),
        pydantic.Field(
            alias="factionVendorIndex",
            description="The index of the Faction vendor that is currently available. Will be set to -1 if no vendors are available.",
        ),
    ] = None
    """
    The index of the Faction vendor that is currently available. Will be set to -1 if no vendors are available.
    """

    level: typing.Optional[int] = pydantic.Field(default=None)
    """
    This is the level of the progression (for instance, the Character Level).
    """

    level_cap: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="levelCap"),
        pydantic.Field(
            alias="levelCap",
            description="This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)",
        ),
    ] = None
    """
    This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)
    """

    next_level_at: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nextLevelAt"),
        pydantic.Field(
            alias="nextLevelAt",
            description='The total amount of progression (i.e. "Experience") needed in order to reach the next level.',
        ),
    ] = None
    """
    The total amount of progression (i.e. "Experience") needed in order to reach the next level.
    """

    progress_to_next_level: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressToNextLevel"),
        pydantic.Field(
            alias="progressToNextLevel",
            description='The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.',
        ),
    ] = None
    """
    The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.
    """

    progression_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressionHash"),
        pydantic.Field(
            alias="progressionHash",
            description="The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.",
        ),
    ] = None
    """
    The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.
    """

    reward_item_states: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="rewardItemStates"),
        pydantic.Field(
            alias="rewardItemStates",
            description="Information about historical rewards for this progression, if there is any data for it.",
        ),
    ] = None
    """
    Information about historical rewards for this progression, if there is any data for it.
    """

    season_resets: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyProgressionResetEntry]],
        FieldMetadata(alias="seasonResets"),
        pydantic.Field(
            alias="seasonResets",
            description="Information about historical resets of this progression, if there is any data for it.",
        ),
    ] = None
    """
    Information about historical resets of this progression, if there is any data for it.
    """

    step_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stepIndex"),
        pydantic.Field(
            alias="stepIndex",
            description='Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)',
        ),
    ] = None
    """
    Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)
    """

    weekly_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="weeklyLimit"),
        pydantic.Field(alias="weeklyLimit", description="If this progression has a weekly limit, this is that limit."),
    ] = None
    """
    If this progression has a weekly limit, this is that limit.
    """

    weekly_progress: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="weeklyProgress"),
        pydantic.Field(
            alias="weeklyProgress",
            description="The amount of progress earned toward this progression in the current week.",
        ),
    ] = None
    """
    The amount of progress earned toward this progression in the current week.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
