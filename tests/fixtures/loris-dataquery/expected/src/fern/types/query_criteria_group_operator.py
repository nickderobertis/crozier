

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryCriteriaGroupOperator(enum.StrEnum):
    """
    The operator to connect the items in group
    """

    AND = "and"
    OR = "or"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryCriteriaGroupOperator.AND:
            return and_()
        if self is QueryCriteriaGroupOperator.OR:
            return or_()
