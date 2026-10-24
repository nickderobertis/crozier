

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentCheckResponseRole(enum.StrEnum):
    LEAD = "lead"
    GUEST = "guest"

    def visit(self, lead: typing.Callable[[], T_Result], guest: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentCheckResponseRole.LEAD:
            return lead()
        if self is AgentCheckResponseRole.GUEST:
            return guest()
