

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyMessage(enum.StrEnum):
    AGENT_NOT_FOUND = "Agent not found"

    def visit(self, agent_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyMessage.AGENT_NOT_FOUND:
            return agent_not_found()
