

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_progression import DestinyDestinyProgression
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyEntitiesCharactersDestinyCharacterComponent(UniversalBaseModel):
    """
    This component contains base properties of the character. You'll probably want to always request this component, but hey you do you.
    """

    base_character_level: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="baseCharacterLevel")
    ] = pydantic.Field(default=None)
    """
    The "base" level of your character, not accounting for any light level.
    """

    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = (
        pydantic.Field(default=None)
    )
    """
    The unique identifier for the character.
    """

    class_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="classHash")] = pydantic.Field(
        default=None
    )
    """
    Use this hash to look up the character's DestinyClassDefinition.
    """

    class_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="classType")] = pydantic.Field(
        default=None
    )
    """
    Mostly for historical purposes at this point, this is an enumeration for the character's class.
    It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
    """

    date_last_played: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateLastPlayed")
    ] = pydantic.Field(default=None)
    """
    The last date that the user played Destiny.
    """

    emblem_background_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="emblemBackgroundPath")
    ] = pydantic.Field(default=None)
    """
    A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
    """

    emblem_color: typing_extensions.Annotated[
        typing.Optional[DestinyMiscDestinyColor], FieldMetadata(alias="emblemColor")
    ] = pydantic.Field(default=None)
    """
    A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup.
    """

    emblem_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="emblemHash")] = pydantic.Field(
        default=None
    )
    """
    The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition.
    """

    emblem_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="emblemPath")] = pydantic.Field(
        default=None
    )
    """
    A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
    """

    gender_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="genderHash")] = pydantic.Field(
        default=None
    )
    """
    Use this hash to look up the character's DestinyGenderDefinition.
    """

    gender_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="genderType")] = pydantic.Field(
        default=None
    )
    """
    Mostly for historical purposes at this point, this is an enumeration for the character's Gender.
    It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me.
    """

    level_progression: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyProgression], FieldMetadata(alias="levelProgression")
    ] = pydantic.Field(default=None)
    """
    The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level.
    """

    light: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user's calculated "Light Level". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items.
    """

    membership_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipId")] = (
        pydantic.Field(default=None)
    )
    """
    Every Destiny Profile has a membershipId. This is provided on the character as well for convenience.
    """

    membership_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipType")] = (
        pydantic.Field(default=None)
    )
    """
    membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values.
    """

    minutes_played_this_session: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minutesPlayedThisSession")
    ] = pydantic.Field(default=None)
    """
    If the user is currently playing, this is how long they've been playing.
    """

    minutes_played_total: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minutesPlayedTotal")
    ] = pydantic.Field(default=None)
    """
    If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things.
    """

    percent_to_next_level: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="percentToNextLevel")
    ] = pydantic.Field(default=None)
    """
    A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level.
    """

    race_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="raceHash")] = pydantic.Field(
        default=None
    )
    """
    Use this hash to look up the character's DestinyRaceDefinition.
    """

    race_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="raceType")] = pydantic.Field(
        default=None
    )
    """
    Mostly for historical purposes at this point, this is an enumeration for the character's race.
    It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
    """

    stats: typing.Optional[typing.Dict[str, int]] = pydantic.Field(default=None)
    """
    Your character's stats, such as Agility, Resilience, etc... *not* historical stats.
    You'll have to call a different endpoint for those.
    """

    title_record_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="titleRecordHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
