

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BriefingAgentStatus(enum.StrEnum):
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
        if self is BriefingAgentStatus.PENDING:
            return pending()
        if self is BriefingAgentStatus.RUNNING:
            return running()
        if self is BriefingAgentStatus.COMPLETED:
            return completed()
        if self is BriefingAgentStatus.FAILED:
            return failed()
