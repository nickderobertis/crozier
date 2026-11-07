

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupConditionDtoOperator(enum.StrEnum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"

    def visit(
        self,
        and_: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        not_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GroupConditionDtoOperator.AND:
            return and_()
        if self is GroupConditionDtoOperator.OR:
            return or_()
        if self is GroupConditionDtoOperator.NOT:
            return not_()
