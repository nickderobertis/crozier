

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .class_level_class_specific_creating_spell_slots_creating_spell_slots_item import (
    ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem,
)


class ClassLevelClassSpecificCreatingSpellSlots(UniversalBaseModel):
    """
    Bard Sorcerer Specific Features
    """

    creating_spell_slots: typing.Optional[
        typing.List[ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem]
    ] = None
    metamagic_known: typing.Optional[float] = None
    sorcery_points: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
