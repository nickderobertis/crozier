

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_milestone_activity_variant import DestinyMilestonesDestinyMilestoneActivityVariant


class DestinyMilestonesDestinyMilestoneActivity(UniversalBaseModel):
    """
    Sometimes, we know the specific activity that the Milestone wants you to play. This entity provides additional information about that Activity and all of its variants. (sometimes there's only one variant, but I think you get the point)
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash of an arbitrarily chosen variant of this activity. We'll go ahead and call that the "canonical" activity, because if you're using this value you should only use it for properties that are common across the variants: things like the name of the activity, it's location, etc... Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.
    """

    activity_mode_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityModeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
    """

    activity_mode_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityModeType")] = (
        pydantic.Field(default=None)
    )
    """
    The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    modifier_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="modifierHashes")
    ] = pydantic.Field(default=None)
    """
    If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
    """

    variants: typing.Optional[typing.List[DestinyMilestonesDestinyMilestoneActivityVariant]] = pydantic.Field(
        default=None
    )
    """
    If you want more than just name/location/etc... you're going to have to dig into and show the variants of the conceptual activity. These will differ in seemingly arbitrary ways, like difficulty level and modifiers applied. Show it in whatever way tickles your fancy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
