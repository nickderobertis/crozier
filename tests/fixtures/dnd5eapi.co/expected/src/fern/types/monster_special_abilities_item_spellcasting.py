

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference
from .monster_special_abilities_item_spellcasting_spells_item import MonsterSpecialAbilitiesItemSpellcastingSpellsItem


class MonsterSpecialAbilitiesItemSpellcasting(UniversalBaseModel):
    ability: typing.Optional[ApiReference] = None
    components_required: typing.Optional[typing.List[str]] = None
    dc: typing.Optional[float] = None
    modifier: typing.Optional[float] = None
    school: typing.Optional[str] = None
    slots: typing.Optional[typing.Dict[str, float]] = None
    spells: typing.Optional[typing.List[MonsterSpecialAbilitiesItemSpellcastingSpellsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
