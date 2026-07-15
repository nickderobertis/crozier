

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .area_of_effect import AreaOfEffect
from .dc import Dc
from .trait_trait_specific_breath_weapon_breath_weapon_damage import TraitTraitSpecificBreathWeaponBreathWeaponDamage
from .trait_trait_specific_breath_weapon_breath_weapon_usage import TraitTraitSpecificBreathWeaponBreathWeaponUsage


class TraitTraitSpecificBreathWeaponBreathWeapon(UniversalBaseModel):
    """
    The breath weapon action associated with a draconic ancestry.
    """

    area_of_effect: typing.Optional[AreaOfEffect] = None
    damage: typing.Optional[TraitTraitSpecificBreathWeaponBreathWeaponDamage] = None
    dc: typing.Optional[Dc] = None
    desc: typing.Optional[str] = None
    name: typing.Optional[str] = None
    usage: typing.Optional[TraitTraitSpecificBreathWeaponBreathWeaponUsage] = pydantic.Field(default=None)
    """
    Description of the usage constraints of this action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
