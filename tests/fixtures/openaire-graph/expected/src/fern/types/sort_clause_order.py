

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortClauseOrder(enum.StrEnum):
    DESC = "desc"
    ASC = "asc"

    def visit(self, desc: typing.Callable[[], T_Result], asc: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortClauseOrder.DESC:
            return desc()
        if self is SortClauseOrder.ASC:
            return asc()
