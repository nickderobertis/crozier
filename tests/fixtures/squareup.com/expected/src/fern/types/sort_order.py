

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortOrder(enum.StrEnum):
    """
    The order (e.g., chronological or alphabetical) in which results from a request are returned.
    """

    DESC = "DESC"
    ASC = "ASC"

    def visit(self, desc: typing.Callable[[], T_Result], asc: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortOrder.DESC:
            return desc()
        if self is SortOrder.ASC:
            return asc()
