

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunWorkflow(enum.StrEnum):
    WEEKLY_OPS = "weekly_ops"

    def visit(self, weekly_ops: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentRunWorkflow.WEEKLY_OPS:
            return weekly_ops()
