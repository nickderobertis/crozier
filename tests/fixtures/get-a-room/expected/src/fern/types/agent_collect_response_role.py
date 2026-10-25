

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentCollectResponseRole(enum.StrEnum):
    LEAD = "lead"

    def visit(self, lead: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentCollectResponseRole.LEAD:
            return lead()
