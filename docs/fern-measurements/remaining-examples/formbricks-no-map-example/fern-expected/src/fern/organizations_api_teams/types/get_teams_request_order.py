

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTeamsRequestOrder(enum.StrEnum):
    """
    Sort order
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTeamsRequestOrder.ASC:
            return asc()
        if self is GetTeamsRequestOrder.DESC:
            return desc()
