

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dc import Dc
from .monster_special_abilities_item_spellcasting import MonsterSpecialAbilitiesItemSpellcasting
from .monster_special_abilities_item_usage import MonsterSpecialAbilitiesItemUsage


class MonsterSpecialAbilitiesItem(UniversalBaseModel):
    attack_bonus: typing.Optional[float] = None
    damage: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    dc: typing.Optional[Dc] = None
    desc: typing.Optional[str] = None
    name: typing.Optional[str] = None
    spellcasting: typing.Optional[MonsterSpecialAbilitiesItemSpellcasting] = None
    usage: typing.Optional[MonsterSpecialAbilitiesItemUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
