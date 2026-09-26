

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class QueryTableRowsRequestSortItemDirection(enum.StrEnum):
    """
    Sort direction for this column.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryTableRowsRequestSortItemDirection.ASC:
            return asc()
        if self is QueryTableRowsRequestSortItemDirection.DESC:
            return desc()
