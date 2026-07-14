

from __future__ import annotations

import typing

from .option_action_name import OptionActionName
from .option_alignments import OptionAlignments
from .option_bonus import OptionBonus
from .option_damage import OptionDamage
from .option_damage_dice import OptionDamageDice
from .option_item import OptionItem
from .option_minimum_score import OptionMinimumScore
from .option_of import OptionOf
from .option_string import OptionString

if typing.TYPE_CHECKING:
    from .option_choice import OptionChoice
    from .option_items import OptionItems
Option = typing.Union[
    OptionItem,
    OptionActionName,
    "OptionItems",
    "OptionChoice",
    OptionString,
    OptionAlignments,
    OptionOf,
    OptionMinimumScore,
    OptionBonus,
    OptionDamage,
    OptionDamageDice,
]
