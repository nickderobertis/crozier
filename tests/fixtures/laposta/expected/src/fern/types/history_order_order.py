

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HistoryOrderOrder(enum.StrEnum):
    DESC = "desc"
    ASC = "asc"

    def visit(self, desc: typing.Callable[[], T_Result], asc: typing.Callable[[], T_Result]) -> T_Result:
        if self is HistoryOrderOrder.DESC:
            return desc()
        if self is HistoryOrderOrder.ASC:
            return asc()
