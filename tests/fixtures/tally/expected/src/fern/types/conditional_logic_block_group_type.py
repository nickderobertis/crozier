

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionalLogicBlockGroupType(enum.StrEnum):
    CONDITIONAL_LOGIC = "CONDITIONAL_LOGIC"

    def visit(self, conditional_logic: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConditionalLogicBlockGroupType.CONDITIONAL_LOGIC:
            return conditional_logic()
