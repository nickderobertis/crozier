

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceTeamsRequestOrder(enum.StrEnum):
    """
    Sort order
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWorkspaceTeamsRequestOrder.ASC:
            return asc()
        if self is GetWorkspaceTeamsRequestOrder.DESC:
            return desc()
