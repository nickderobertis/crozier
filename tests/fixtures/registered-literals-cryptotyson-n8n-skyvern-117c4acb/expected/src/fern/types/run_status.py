

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    CREATED = "created"
    QUEUED = "queued"
    RUNNING = "running"
    TIMED_OUT = "timed_out"
    FAILED = "failed"
    TERMINATED = "terminated"
    COMPLETED = "completed"
    CANCELED = "canceled"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        terminated: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.CREATED:
            return created()
        if self is RunStatus.QUEUED:
            return queued()
        if self is RunStatus.RUNNING:
            return running()
        if self is RunStatus.TIMED_OUT:
            return timed_out()
        if self is RunStatus.FAILED:
            return failed()
        if self is RunStatus.TERMINATED:
            return terminated()
        if self is RunStatus.COMPLETED:
            return completed()
        if self is RunStatus.CANCELED:
            return canceled()
