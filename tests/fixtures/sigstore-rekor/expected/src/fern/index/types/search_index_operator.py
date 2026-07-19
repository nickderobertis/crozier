

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchIndexOperator(enum.StrEnum):
    AND = "and"
    OR = "or"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchIndexOperator.AND:
            return and_()
        if self is SearchIndexOperator.OR:
            return or_()
