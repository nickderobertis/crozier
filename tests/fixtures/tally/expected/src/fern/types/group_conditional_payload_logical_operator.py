

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupConditionalPayloadLogicalOperator(enum.StrEnum):
    """
    How to combine child conditions (AND/OR).
    """

    AND = "AND"
    OR = "OR"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is GroupConditionalPayloadLogicalOperator.AND:
            return and_()
        if self is GroupConditionalPayloadLogicalOperator.OR:
            return or_()
