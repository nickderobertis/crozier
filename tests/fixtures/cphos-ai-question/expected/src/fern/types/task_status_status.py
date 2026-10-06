

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskStatusStatus(enum.StrEnum):
    """
    任务生命周期状态。
    """

    QUEUED = "queued"
    RUNNING = "running"
    ABORTING = "aborting"
    DONE = "done"
    ERROR = "error"
    ABORTED = "aborted"
    INTERRUPTED = "interrupted"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        aborting: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskStatusStatus.QUEUED:
            return queued()
        if self is TaskStatusStatus.RUNNING:
            return running()
        if self is TaskStatusStatus.ABORTING:
            return aborting()
        if self is TaskStatusStatus.DONE:
            return done()
        if self is TaskStatusStatus.ERROR:
            return error()
        if self is TaskStatusStatus.ABORTED:
            return aborted()
        if self is TaskStatusStatus.INTERRUPTED:
            return interrupted()
