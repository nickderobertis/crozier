

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAgentsForIdentityRequestOrder(enum.StrEnum):
    """
    Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListAgentsForIdentityRequestOrder.ASC:
            return asc()
        if self is ListAgentsForIdentityRequestOrder.DESC:
            return desc()
