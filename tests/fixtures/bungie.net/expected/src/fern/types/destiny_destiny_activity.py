

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_challenges_destiny_challenge_status import DestinyChallengesDestinyChallengeStatus


class DestinyDestinyActivity(UniversalBaseModel):
    """
    Represents the "Live" data that we can obtain about a Character's status with a specific Activity. This will tell you whether the character can participate in the activity, as well as some other basic mutable information.
    Meant to be combined with static DestinyActivityDefinition data for a full picture of the Activity.
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the Activity. Use this to look up the DestinyActivityDefinition of the activity.
    """

    boolean_activity_options: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, bool]], FieldMetadata(alias="booleanActivityOptions")
    ] = pydantic.Field(default=None)
    """
    The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).
    As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode".
    We don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the "option" that is enabled/disabled) and the value (whether it's enabled or disabled presently)
    On our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation.
    """

    can_join: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canJoin")] = pydantic.Field(
        default=None
    )
    """
    If true, the user is allowed to join with another Fireteam in this activity.
    """

    can_lead: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canLead")] = pydantic.Field(
        default=None
    )
    """
    If true, the user is allowed to lead a Fireteam into this activity.
    """

    challenges: typing.Optional[typing.List[DestinyChallengesDestinyChallengeStatus]] = None
    difficulty_tier: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="difficultyTier")] = (
        pydantic.Field(default=None)
    )
    """
    A DestinyActivityDifficultyTier enum value indicating the difficulty of the activity.
    """

    display_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="displayLevel")] = (
        pydantic.Field(default=None)
    )
    """
    The difficulty level of the activity, if applicable.
    """

    is_completed: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isCompleted")] = (
        pydantic.Field(default=None)
    )
    """
    If true, we both have the ability to know that the user has completed this activity and they have completed it. Unfortunately, we can't necessarily know this for all activities. As such, this should probably only be used if you already know in advance which specific activities you wish to check.
    """

    is_new: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isNew")] = pydantic.Field(
        default=None
    )
    """
    If true, then the activity should have a "new" indicator in the Director UI.
    """

    is_visible: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isVisible")] = pydantic.Field(
        default=None
    )
    """
    If true, the user should be able to see this activity.
    """

    loadout_requirement_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="loadoutRequirementIndex")
    ] = pydantic.Field(default=None)
    """
    If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements.
    """

    modifier_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="modifierHashes")
    ] = pydantic.Field(default=None)
    """
    If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.
    Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
    """

    recommended_light: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="recommendedLight")] = (
        pydantic.Field(default=None)
    )
    """
    The recommended light level for the activity, if applicable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
