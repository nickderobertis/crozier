

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_milestones_destiny_milestone_activity_variant_definition import (
    DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition,
)


class DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition(UniversalBaseModel):
    """
    Milestones can have associated activities which provide additional information about the context, challenges, modifiers, state etc... related to this Milestone.
    Information we need to be able to return that data is defined here, along with Tier data to establish a relationship between a conceptual Activity and its difficulty levels and variants.
    """

    conceptual_activity_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="conceptualActivityHash")
    ] = pydantic.Field(default=None)
    """
    The "Conceptual" activity hash. Basically, we picked the lowest level activity and are treating it as the canonical definition of the activity for rendering purposes.
    If you care about the specific difficulty modes and variations, use the activities under "Variants".
    """

    variants: typing.Optional[
        typing.Dict[str, DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition]
    ] = pydantic.Field(default=None)
    """
    A milestone-referenced activity can have many variants, such as Tiers or alternative modes of play.
    Even if there is only a single variant, the details for these are represented within as a variant definition.
    It is assumed that, if this DestinyMilestoneActivityDefinition is active, then all variants should be active.
    If a Milestone could ever split the variants' active status conditionally, they should all have their own DestinyMilestoneActivityDefinition instead! The potential duplication will be worth it for the obviousness of processing and use.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
