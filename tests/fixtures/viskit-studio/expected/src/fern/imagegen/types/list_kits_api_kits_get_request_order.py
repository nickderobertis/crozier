

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKitsApiKitsGetRequestOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListKitsApiKitsGetRequestOrder.ASC:
            return asc()
        if self is ListKitsApiKitsGetRequestOrder.DESC:
            return desc()
