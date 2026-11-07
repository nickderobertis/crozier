

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListOrder(enum.StrEnum):
    """
    Order to list prerecordings.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListOrder.ASC:
            return asc()
        if self is ListOrder.DESC:
            return desc()
