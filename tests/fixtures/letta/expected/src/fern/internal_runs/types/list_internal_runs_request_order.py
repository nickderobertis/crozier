

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListInternalRunsRequestOrder(enum.StrEnum):
    """
    Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListInternalRunsRequestOrder.ASC:
            return asc()
        if self is ListInternalRunsRequestOrder.DESC:
            return desc()
