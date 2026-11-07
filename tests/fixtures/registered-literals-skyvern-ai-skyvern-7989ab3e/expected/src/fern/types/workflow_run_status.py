

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRunStatus(enum.StrEnum):
    CREATED = "created"
    QUEUED = "queued"
    RUNNING = "running"
    FAILED = "failed"
    TERMINATED = "terminated"
    CANCELED = "canceled"
    TIMED_OUT = "timed_out"
    COMPLETED = "completed"
    PAUSED = "paused"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        terminated: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowRunStatus.CREATED:
            return created()
        if self is WorkflowRunStatus.QUEUED:
            return queued()
        if self is WorkflowRunStatus.RUNNING:
            return running()
        if self is WorkflowRunStatus.FAILED:
            return failed()
        if self is WorkflowRunStatus.TERMINATED:
            return terminated()
        if self is WorkflowRunStatus.CANCELED:
            return canceled()
        if self is WorkflowRunStatus.TIMED_OUT:
            return timed_out()
        if self is WorkflowRunStatus.COMPLETED:
            return completed()
        if self is WorkflowRunStatus.PAUSED:
            return paused()
