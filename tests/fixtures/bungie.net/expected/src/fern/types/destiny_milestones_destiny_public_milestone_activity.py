

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_public_milestone_activity_variant import (
    DestinyMilestonesDestinyPublicMilestoneActivityVariant,
)


class DestinyMilestonesDestinyPublicMilestoneActivity(UniversalBaseModel):
    """
    A milestone may have one or more conceptual Activities associated with it, and each of those conceptual activities could have a variety of variants, modes, tiers, what-have-you. Our attempts to determine what qualifies as a conceptual activity are, unfortunately, janky. So if you see missing modes or modes that don't seem appropriate to you, let us know and I'll buy you a beer if we ever meet up in person.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description='The hash identifier of the activity that\'s been chosen to be considered the canonical "conceptual" activity definition. This may have many variants, defined herein.',
        ),
    ] = None
    """
    The hash identifier of the activity that's been chosen to be considered the canonical "conceptual" activity definition. This may have many variants, defined herein.
    """

    activity_mode_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityModeHash"),
        pydantic.Field(
            alias="activityModeHash",
            description="The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.",
        ),
    ] = None
    """
    The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
    """

    activity_mode_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityModeType"),
        pydantic.Field(
            alias="activityModeType",
            description="The enumeration equivalent of the most specific Activity Mode under which this activity is played.",
        ),
    ] = None
    """
    The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    modifier_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="modifierHashes"),
        pydantic.Field(
            alias="modifierHashes",
            description="The activity may have 0-to-many modifiers: if it does, this will contain the hashes to the DestinyActivityModifierDefinition that defines the modifier being applied.",
        ),
    ] = None
    """
    The activity may have 0-to-many modifiers: if it does, this will contain the hashes to the DestinyActivityModifierDefinition that defines the modifier being applied.
    """

    variants: typing.Optional[typing.List[DestinyMilestonesDestinyPublicMilestoneActivityVariant]] = pydantic.Field(
        default=None
    )
    """
    Every relevant variation of this conceptual activity, including the conceptual activity itself, have variants defined here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
