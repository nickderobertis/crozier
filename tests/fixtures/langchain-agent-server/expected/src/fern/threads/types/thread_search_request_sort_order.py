

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadSearchRequestSortOrder(enum.StrEnum):
    """
    Sort order.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadSearchRequestSortOrder.ASC:
            return asc()
        if self is ThreadSearchRequestSortOrder.DESC:
            return desc()
