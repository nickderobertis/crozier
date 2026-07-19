

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAgentsForArchiveRequestOrder(enum.StrEnum):
    """
    Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListAgentsForArchiveRequestOrder.ASC:
            return asc()
        if self is ListAgentsForArchiveRequestOrder.DESC:
            return desc()
