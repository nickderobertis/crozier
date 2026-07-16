

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortDirection(enum.StrEnum):
    """
    The direction in which to sort the results
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortDirection.ASC:
            return asc()
        if self is SortDirection.DESC:
            return desc()
