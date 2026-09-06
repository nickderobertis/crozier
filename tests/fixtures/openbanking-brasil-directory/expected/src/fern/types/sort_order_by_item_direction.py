

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortOrderByItemDirection(enum.StrEnum):
    """
    Direction of sort, i.e. ascending or descending
    """

    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortOrderByItemDirection.ASC:
            return asc()
        if self is SortOrderByItemDirection.DESC:
            return desc()
