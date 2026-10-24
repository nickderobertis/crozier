

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentSayResponseRole(enum.StrEnum):
    LEAD = "lead"
    GUEST = "guest"

    def visit(self, lead: typing.Callable[[], T_Result], guest: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentSayResponseRole.LEAD:
            return lead()
        if self is AgentSayResponseRole.GUEST:
            return guest()
