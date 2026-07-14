

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .dc import Dc
from .monster_reactions_item_actions_item import MonsterReactionsItemActionsItem
from .monster_reactions_item_attacks_item import MonsterReactionsItemAttacksItem
from .monster_reactions_item_damage_item import MonsterReactionsItemDamageItem


class MonsterReactionsItem(UniversalBaseModel):
    """
    Action available to a `Monster` in addition to the standard creature actions.
    """

    action_options: typing.Optional["Choice"] = None
    actions: typing.Optional[typing.List[MonsterReactionsItemActionsItem]] = None
    attack_bonus: typing.Optional[float] = None
    attacks: typing.Optional[typing.List[MonsterReactionsItemAttacksItem]] = None
    damage: typing.Optional[typing.List[MonsterReactionsItemDamageItem]] = None
    dc: typing.Optional[Dc] = None
    desc: typing.Optional[str] = None
    multiattack_type: typing.Optional[str] = None
    name: typing.Optional[str] = None
    options: typing.Optional["Choice"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice

update_forward_refs(MonsterReactionsItem)
