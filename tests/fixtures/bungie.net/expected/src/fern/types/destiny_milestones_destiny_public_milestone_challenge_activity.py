

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyPublicMilestoneChallengeActivity(UniversalBaseModel):
    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = None
    boolean_activity_options: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, bool]], FieldMetadata(alias="booleanActivityOptions")
    ] = pydantic.Field(default=None)
    """
    The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).
    As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode".
    We have no human readable information for this data, so it's up to you if you want to associate it with such info to show it.
    """

    challenge_objective_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="challengeObjectiveHashes")
    ] = None
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

    phase_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="phaseHashes")] = (
        pydantic.Field(default=None)
    )
    """
    The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
