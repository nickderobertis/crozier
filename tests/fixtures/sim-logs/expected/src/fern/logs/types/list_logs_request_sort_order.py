

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListLogsRequestSortOrder(enum.StrEnum):
    """
    Sort direction.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListLogsRequestSortOrder.ASC:
            return asc()
        if self is ListLogsRequestSortOrder.DESC:
            return desc()
