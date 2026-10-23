

from __future__ import annotations

import typing

from .condition_group_conditions_item_zero import ConditionGroupConditionsItemZero

if typing.TYPE_CHECKING:
    from .condition_group import ConditionGroup
ConditionGroupConditionsItem = typing.Union[ConditionGroupConditionsItemZero, "ConditionGroup"]
