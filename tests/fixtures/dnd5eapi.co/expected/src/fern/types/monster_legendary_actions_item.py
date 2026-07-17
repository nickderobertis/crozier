

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .dc import Dc
from .monster_legendary_actions_item_actions_item import MonsterLegendaryActionsItemActionsItem
from .monster_legendary_actions_item_attacks_item import MonsterLegendaryActionsItemAttacksItem
from .monster_legendary_actions_item_damage_item import MonsterLegendaryActionsItemDamageItem


class MonsterLegendaryActionsItem(UniversalBaseModel):
    """
    Action available to a `Monster` in addition to the standard creature actions.
    """

    action_options: typing.Optional["Choice"] = None
    actions: typing.Optional[typing.List[MonsterLegendaryActionsItemActionsItem]] = None
    attack_bonus: typing.Optional[float] = None
    attacks: typing.Optional[typing.List[MonsterLegendaryActionsItemAttacksItem]] = None
    damage: typing.Optional[typing.List[MonsterLegendaryActionsItemDamageItem]] = None
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
from .option import Option
from .option_choice import OptionChoice
from .option_items import OptionItems
from .option_set import OptionSet
from .option_set_options_array import OptionSetOptionsArray

update_forward_refs(
    MonsterLegendaryActionsItem,
    Choice=Choice,
    Option=Option,
    OptionChoice=OptionChoice,
    OptionItems=OptionItems,
    OptionSet=OptionSet,
    OptionSetOptionsArray=OptionSetOptionsArray,
)
