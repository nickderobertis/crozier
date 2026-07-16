

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .interpolation_interpolation_point_float import InterpolationInterpolationPointFloat


class DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition(UniversalBaseModel):
    """
    These are pre-constructed collections of data that can be used to determine the Level Requirement for an item given a Progression to be tested (such as the Character's level).
    For instance, say a character receives a new Auto Rifle, and that Auto Rifle's DestinyInventoryItemDefinition.quality.progressionLevelRequirementHash property is pointing at one of these DestinyProgressionLevelRequirementDefinitions. Let's pretend also that the progressionHash it is pointing at is the Character Level progression. In that situation, the character's level will be used to interpolate a value in the requirementCurve property. The value picked up from that interpolation will be the required level for the item.
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

    progression_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressionHash"),
        pydantic.Field(
            alias="progressionHash",
            description="The progression whose level should be used to determine the level requirement.\r\nLook up the DestinyProgressionDefinition with this hash for more information about the progression in question.",
        ),
    ] = None
    """
    The progression whose level should be used to determine the level requirement.
    Look up the DestinyProgressionDefinition with this hash for more information about the progression in question.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    requirement_curve: typing_extensions.Annotated[
        typing.Optional[typing.List[InterpolationInterpolationPointFloat]],
        FieldMetadata(alias="requirementCurve"),
        pydantic.Field(
            alias="requirementCurve",
            description="A curve of level requirements, weighted by the related progressions' level.\r\nInterpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.",
        ),
    ] = None
    """
    A curve of level requirements, weighted by the related progressions' level.
    Interpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
