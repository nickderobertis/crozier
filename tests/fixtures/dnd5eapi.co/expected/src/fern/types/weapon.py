

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .cost import Cost
from .damage import Damage
from .resource_description import ResourceDescription
from .weapon_range import WeaponRange


class Weapon(ApiReference, ResourceDescription):
    """
    `Weapon`
    """

    category_range: typing.Optional[str] = pydantic.Field(default=None)
    """
    A combination of weapon_category and weapon_range.
    """

    cost: typing.Optional[Cost] = None
    damage: typing.Optional[Damage] = None
    equipment_category: typing.Optional[ApiReference] = None
    properties: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    A list of the properties this weapon has.
    """

    range: typing.Optional[WeaponRange] = None
    two_handed_damage: typing.Optional[Damage] = None
    weapon_category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category of weapon this falls into.
    """

    weapon_range: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether this is a Melee or Ranged weapon.
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    How much the equipment weighs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
