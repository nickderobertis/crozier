

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Search5RequestLogicalOperator(enum.StrEnum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"

    def visit(
        self,
        and_: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        not_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Search5RequestLogicalOperator.AND:
            return and_()
        if self is Search5RequestLogicalOperator.OR:
            return or_()
        if self is Search5RequestLogicalOperator.NOT:
            return not_()
