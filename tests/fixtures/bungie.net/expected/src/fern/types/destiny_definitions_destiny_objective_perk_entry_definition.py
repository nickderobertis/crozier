

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyObjectivePerkEntryDefinition(UniversalBaseModel):
    """
    Defines the conditions under which an intrinsic perk is applied while participating in an Objective.
    These perks will generally not be benefit-granting perks, but rather a perk that modifies gameplay in some interesting way.
    """

    perk_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="perkHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character.
    """

    style: typing.Optional[int] = pydantic.Field(default=None)
    """
    An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
