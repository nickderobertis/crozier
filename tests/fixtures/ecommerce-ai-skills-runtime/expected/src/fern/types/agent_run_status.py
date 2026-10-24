

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunStatus(enum.StrEnum):
    REQUESTED = "requested"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentRunStatus.REQUESTED:
            return requested()
        if self is AgentRunStatus.RUNNING:
            return running()
        if self is AgentRunStatus.COMPLETED:
            return completed()
        if self is AgentRunStatus.FAILED:
            return failed()
