

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionalLogicPayloadLogicalOperator(enum.StrEnum):
    """
    How to combine top-level conditions (AND/OR).
    """

    AND = "AND"
    OR = "OR"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConditionalLogicPayloadLogicalOperator.AND:
            return and_()
        if self is ConditionalLogicPayloadLogicalOperator.OR:
            return or_()
