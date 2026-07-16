

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskState(enum.StrEnum):
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    TIMEDOUT = "timedout"
    COMPLETED = "completed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        timedout: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskState.PENDING:
            return pending()
        if self is TaskState.QUEUED:
            return queued()
        if self is TaskState.RUNNING:
            return running()
        if self is TaskState.TIMEDOUT:
            return timedout()
        if self is TaskState.COMPLETED:
            return completed()
