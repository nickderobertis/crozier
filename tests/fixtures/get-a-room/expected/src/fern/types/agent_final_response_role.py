

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentFinalResponseRole(enum.StrEnum):
    LEAD = "lead"

    def visit(self, lead: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentFinalResponseRole.LEAD:
            return lead()
