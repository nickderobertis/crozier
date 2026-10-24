

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentTaskStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentTaskStatus.PENDING:
            return pending()
        if self is AgentTaskStatus.RUNNING:
            return running()
        if self is AgentTaskStatus.COMPLETED:
            return completed()
        if self is AgentTaskStatus.FAILED:
            return failed()
