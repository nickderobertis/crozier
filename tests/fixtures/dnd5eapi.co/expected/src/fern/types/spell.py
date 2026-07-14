

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .area_of_effect import AreaOfEffect
from .resource_description import ResourceDescription
from .spell_components_item import SpellComponentsItem
from .spell_damage import SpellDamage


class Spell(ApiReference, ResourceDescription):
    """
    `Spell`
    """

    area_of_effect: typing.Optional[AreaOfEffect] = None
    attack_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Attack type of the spell.
    """

    casting_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    How long it takes for the spell to activate.
    """

    classes: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of classes that are able to learn the spell.
    """

    components: typing.Optional[typing.List[SpellComponentsItem]] = pydantic.Field(default=None)
    """
    List of shorthand for required components of the spell.
    V: verbal
    S: somatic
    M: material
    """

    concentration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines if a spell needs concentration to persist.
    """

    damage: typing.Optional[SpellDamage] = None
    duration: typing.Optional[str] = pydantic.Field(default=None)
    """
    How long the spell effect lasts.
    """

    higher_level: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of descriptions for casting the spell at higher levels.
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Level of the spell.
    """

    material: typing.Optional[str] = pydantic.Field(default=None)
    """
    Material component for the spell to be cast.
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    Range of the spell, usually expressed in feet.
    """

    ritual: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines if a spell can be cast in a 10-min(in-game) ritual.
    """

    school: typing.Optional[ApiReference] = pydantic.Field(default=None)
    """
    Magic school this spell belongs to.
    """

    subclasses: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of subclasses that have access to the spell.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
