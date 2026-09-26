

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTableRowsRequestSortItemDirection(enum.StrEnum):
    """
    Sort direction for this column.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTableRowsRequestSortItemDirection.ASC:
            return asc()
        if self is SearchTableRowsRequestSortItemDirection.DESC:
            return desc()
