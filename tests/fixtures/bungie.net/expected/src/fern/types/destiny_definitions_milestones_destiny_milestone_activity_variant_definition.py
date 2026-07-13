

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition(UniversalBaseModel):
    """
    Represents a variant on an activity for a Milestone: a specific difficulty tier, or a specific activity variant for example.
    These will often have more specific details, such as an associated Guided Game, progression steps, tier-specific rewards, and custom values.
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash to use for looking up the variant Activity's definition (DestinyActivityDefinition), where you can find its distinguishing characteristics such as difficulty level and recommended light level. 
    Frequently, that will be the only distinguishing characteristics in practice, which is somewhat of a bummer.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    If you care to do so, render the variants in the order prescribed by this value.
    When you combine live Milestone data with the definition, the order becomes more useful because you'll be cross-referencing between the definition and live data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
