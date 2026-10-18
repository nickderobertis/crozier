

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhraseTriggerConditionsItem(enum.StrEnum):
    PHRASE_CONDITION_TYPE_CONTAINS = "phrase_condition_type_contains"

    def visit(self, phrase_condition_type_contains: typing.Callable[[], T_Result]) -> T_Result:
        if self is PhraseTriggerConditionsItem.PHRASE_CONDITION_TYPE_CONTAINS:
            return phrase_condition_type_contains()
