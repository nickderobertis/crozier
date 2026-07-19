

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListStepsForRunRequestOrder(enum.StrEnum):
    """
    Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListStepsForRunRequestOrder.ASC:
            return asc()
        if self is ListStepsForRunRequestOrder.DESC:
            return desc()
