

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_constants_destiny_environment_location_mapping import DestinyConstantsDestinyEnvironmentLocationMapping
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_activity_challenge_definition import (
    DestinyDefinitionsDestinyActivityChallengeDefinition,
)
from .destiny_definitions_destiny_activity_graph_list_entry_definition import (
    DestinyDefinitionsDestinyActivityGraphListEntryDefinition,
)
from .destiny_definitions_destiny_activity_guided_block_definition import (
    DestinyDefinitionsDestinyActivityGuidedBlockDefinition,
)
from .destiny_definitions_destiny_activity_insertion_point_definition import (
    DestinyDefinitionsDestinyActivityInsertionPointDefinition,
)
from .destiny_definitions_destiny_activity_loadout_requirement_set import (
    DestinyDefinitionsDestinyActivityLoadoutRequirementSet,
)
from .destiny_definitions_destiny_activity_matchmaking_block_definition import (
    DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition,
)
from .destiny_definitions_destiny_activity_modifier_reference_definition import (
    DestinyDefinitionsDestinyActivityModifierReferenceDefinition,
)
from .destiny_definitions_destiny_activity_playlist_item_definition import (
    DestinyDefinitionsDestinyActivityPlaylistItemDefinition,
)
from .destiny_definitions_destiny_activity_reward_definition import DestinyDefinitionsDestinyActivityRewardDefinition
from .destiny_definitions_destiny_activity_unlock_string_definition import (
    DestinyDefinitionsDestinyActivityUnlockStringDefinition,
)


class DestinyDefinitionsDestinyActivityDefinition(UniversalBaseModel):
    """
    The static data about Activities in Destiny 2.
    Note that an Activity must be combined with an ActivityMode to know - from a Gameplay perspective - what the user is "Playing".
    In most PvE activities, this is fairly straightforward. A Story Activity can only be played in the Story Activity Mode.
    However, in PvP activities, the Activity alone only tells you the map being played, or the Playlist that the user chose to enter. You'll need to know the Activity Mode they're playing to know that they're playing Mode X on Map Y.
    Activity Definitions tell a great deal of information about what *could* be relevant to a user: what rewards they can earn, what challenges could be performed, what modifiers could be applied. To figure out which of these properties is actually live, you'll need to combine the definition with "Live" data from one of the Destiny endpoints.
    Activities also have Activity Types, but unfortunately in Destiny 2 these are even less reliable of a source of information than they were in Destiny 1. I will be looking into ways to provide more reliable sources for type information as time goes on, but for now we're going to have to deal with the limitations. See DestinyActivityTypeDefinition for more information.
    """

    activity_graph_list: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]],
        FieldMetadata(alias="activityGraphList"),
        pydantic.Field(
            alias="activityGraphList",
            description="Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity.",
        ),
    ] = None
    """
    Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity.
    """

    activity_light_level: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityLightLevel"),
        pydantic.Field(alias="activityLightLevel", description="The recommended light level for this activity."),
    ] = None
    """
    The recommended light level for this activity.
    """

    activity_location_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyConstantsDestinyEnvironmentLocationMapping]],
        FieldMetadata(alias="activityLocationMappings"),
        pydantic.Field(
            alias="activityLocationMappings",
            description="A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience.",
        ),
    ] = None
    """
    A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience.
    """

    activity_mode_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="activityModeHashes"),
        pydantic.Field(
            alias="activityModeHashes",
            description="The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant.",
        ),
    ] = None
    """
    The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant.
    """

    activity_mode_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="activityModeTypes"),
        pydantic.Field(
            alias="activityModeTypes",
            description="The activity modes - if any - in enum form. Because we can't seem to escape the enums.",
        ),
    ] = None
    """
    The activity modes - if any - in enum form. Because we can't seem to escape the enums.
    """

    activity_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityTypeHash"),
        pydantic.Field(
            alias="activityTypeHash",
            description="The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You'll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing.",
        ),
    ] = None
    """
    The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You'll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing.
    """

    challenges: typing.Optional[typing.List[DestinyDefinitionsDestinyActivityChallengeDefinition]] = pydantic.Field(
        default=None
    )
    """
    An activity can have many Challenges, of which any subset of them may be active for play at any given period of time. This gives the information about the challenges and data that we use to understand when they're active and what rewards they provide. Sadly, at the moment there's no central definition for challenges: much like "Skulls" were in Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicates across the Destiny 2 ecosystem. I have it in mind to centralize these in a future revision of the API, but we are out of time.
    """

    destination_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="destinationHash"),
        pydantic.Field(
            alias="destinationHash",
            description='The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a "Place". For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.',
        ),
    ] = None
    """
    The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a "Place". For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.
    """

    direct_activity_mode_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="directActivityModeHash"),
        pydantic.Field(
            alias="directActivityModeHash",
            description="If this activity had an activity mode directly defined on it, this will be the hash of that mode.",
        ),
    ] = None
    """
    If this activity had an activity mode directly defined on it, this will be the hash of that mode.
    """

    direct_activity_mode_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="directActivityModeType"),
        pydantic.Field(
            alias="directActivityModeType",
            description="If the activity had an activity mode directly defined on it, this will be the enum value of that mode.",
        ),
    ] = None
    """
    If the activity had an activity mode directly defined on it, this will be the enum value of that mode.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties",
            description="The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played.",
        ),
    ] = None
    """
    The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played.
    """

    guided_game: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyActivityGuidedBlockDefinition],
        FieldMetadata(alias="guidedGame"),
        pydantic.Field(
            alias="guidedGame",
            description="This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn't exist, the game is not able to be played as a guided game.",
        ),
    ] = None
    """
    This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn't exist, the game is not able to be played as a guided game.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    insertion_points: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyActivityInsertionPointDefinition]],
        FieldMetadata(alias="insertionPoints"),
        pydantic.Field(
            alias="insertionPoints",
            description="The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability.",
        ),
    ] = None
    """
    The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability.
    """

    is_playlist: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPlaylist"),
        pydantic.Field(
            alias="isPlaylist",
            description="If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist.",
        ),
    ] = None
    """
    If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist.
    """

    is_pv_p: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPvP"),
        pydantic.Field(alias="isPvP", description="If true, this activity is a PVP activity or playlist."),
    ] = None
    """
    If true, this activity is a PVP activity or playlist.
    """

    loadouts: typing.Optional[typing.List[DestinyDefinitionsDestinyActivityLoadoutRequirementSet]] = pydantic.Field(
        default=None
    )
    """
    The set of all possible loadout requirements that could be active for this activity. Only one will be active at any given time, and you can discover which one through activity-associated data such as Milestones that have activity info on them.
    """

    matchmaking: typing.Optional[DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition] = pydantic.Field(
        default=None
    )
    """
    This block of data provides information about the Activity's matchmaking attributes: how many people can join and such.
    """

    modifiers: typing.Optional[typing.List[DestinyDefinitionsDestinyActivityModifierReferenceDefinition]] = (
        pydantic.Field(default=None)
    )
    """
    Activities can have Modifiers, as defined in DestinyActivityModifierDefinition. These are references to the modifiers that *can* be applied to that activity, along with data that we use to determine if that modifier is actually active at any given point in time.
    """

    optional_unlock_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyActivityUnlockStringDefinition]],
        FieldMetadata(alias="optionalUnlockStrings"),
        pydantic.Field(
            alias="optionalUnlockStrings",
            description="If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown.",
        ),
    ] = None
    """
    If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown.
    """

    original_display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="originalDisplayProperties"),
        pydantic.Field(
            alias="originalDisplayProperties",
            description="The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director).",
        ),
    ] = None
    """
    The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director).
    """

    pgcr_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pgcrImage"),
        pydantic.Field(
            alias="pgcrImage",
            description='When Activities are completed, we generate a "Post-Game Carnage Report", or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general.',
        ),
    ] = None
    """
    When Activities are completed, we generate a "Post-Game Carnage Report", or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general.
    """

    place_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="placeHash"),
        pydantic.Field(
            alias="placeHash",
            description='The hash identifier for the "Place" on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.',
        ),
    ] = None
    """
    The hash identifier for the "Place" on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.
    """

    playlist_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyActivityPlaylistItemDefinition]],
        FieldMetadata(alias="playlistItems"),
        pydantic.Field(
            alias="playlistItems",
            description="Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time.",
        ),
    ] = None
    """
    Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    release_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="releaseIcon"),
        pydantic.Field(
            alias="releaseIcon",
            description="If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release's icon.",
        ),
    ] = None
    """
    If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release's icon.
    """

    release_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="releaseTime"),
        pydantic.Field(
            alias="releaseTime",
            description="If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible.",
        ),
    ] = None
    """
    If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible.
    """

    rewards: typing.Optional[typing.List[DestinyDefinitionsDestinyActivityRewardDefinition]] = pydantic.Field(
        default=None
    )
    """
    The expected possible rewards for the activity. These rewards may or may not be accessible for an individual player based on their character state, the account state, and even the game's state overall. But it is a useful reference for possible rewards you can earn in the activity. These match up to rewards displayed when you hover over the Activity in the in-game Director, and often refer to Placeholder or "Dummy" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the game doesn't even know what you'll earn specifically until you roll for it at the end)
    """

    selection_screen_display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="selectionScreenDisplayProperties"),
        pydantic.Field(
            alias="selectionScreenDisplayProperties",
            description="The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won't be data in this field if the activity is never shown in a selection/options screen.",
        ),
    ] = None
    """
    The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won't be data in this field if the activity is never shown in a selection/options screen.
    """

    tier: typing.Optional[int] = pydantic.Field(default=None)
    """
    The difficulty tier of the activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
