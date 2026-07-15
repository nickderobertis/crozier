

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_reference import ApiReference
from .trait_trait_specific_breath_weapon_breath_weapon import TraitTraitSpecificBreathWeaponBreathWeapon


class TraitTraitSpecificBreathWeapon(UniversalBaseModel):
    breath_weapon: typing_extensions.Annotated[
        typing.Optional[TraitTraitSpecificBreathWeaponBreathWeapon], FieldMetadata(alias="breath-weapon")
    ] = pydantic.Field(default=None)
    """
    The breath weapon action associated with a draconic ancestry.
    """

    damage_type: typing_extensions.Annotated[typing.Optional[ApiReference], FieldMetadata(alias="damage-type")] = (
        pydantic.Field(default=None)
    )
    """
    A damage type associated with this trait.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
