

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Order(enum.StrEnum):
    """
    Used to specify the order in sorting results.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is Order.ASC:
            return asc()
        if self is Order.DESC:
            return desc()
