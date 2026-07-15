

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .api_reference import ApiReference
from .class_starting_equipment_item import ClassStartingEquipmentItem
from .multiclassing import Multiclassing
from .spellcasting import Spellcasting


class Class(ApiReference):
    """
    `Class`
    """

    class_levels: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the level resource for the class.
    """

    hit_die: typing.Optional[float] = pydantic.Field(default=None)
    """
    Hit die of the class. (ex: 12 == 1d12).
    """

    multi_classing: typing.Optional[Multiclassing] = None
    proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of starting proficiencies for all new characters of this class.
    """

    proficiency_choices: typing.Optional[typing.List["Choice"]] = pydantic.Field(default=None)
    """
    List of choices of starting proficiencies.
    """

    saving_throws: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Saving throws the class is proficient in.
    """

    spellcasting: typing.Optional[Spellcasting] = None
    spells: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the spell resource list for the class.
    """

    starting_equipment: typing.Optional[typing.List[ClassStartingEquipmentItem]] = pydantic.Field(default=None)
    """
    List of equipment and their quantities all players of the class start with.
    """

    starting_equipment_options: typing.Optional[typing.List["Choice"]] = pydantic.Field(default=None)
    """
    List of choices of starting equipment.
    """

    subclasses: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of all possible subclasses this class can specialize in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice

update_forward_refs(Class)
