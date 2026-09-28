

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTablesRequestSortOrder(enum.StrEnum):
    """
    Sort direction.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTablesRequestSortOrder.ASC:
            return asc()
        if self is ListTablesRequestSortOrder.DESC:
            return desc()
