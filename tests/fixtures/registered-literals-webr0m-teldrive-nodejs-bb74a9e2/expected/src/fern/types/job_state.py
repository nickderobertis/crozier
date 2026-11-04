

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobState(enum.StrEnum):
    AVAILABLE = "available"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DISCARDED = "discarded"
    PENDING = "pending"
    RETRYABLE = "retryable"
    RUNNING = "running"
    SCHEDULED = "scheduled"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        discarded: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        retryable: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobState.AVAILABLE:
            return available()
        if self is JobState.CANCELLED:
            return cancelled()
        if self is JobState.COMPLETED:
            return completed()
        if self is JobState.DISCARDED:
            return discarded()
        if self is JobState.PENDING:
            return pending()
        if self is JobState.RETRYABLE:
            return retryable()
        if self is JobState.RUNNING:
            return running()
        if self is JobState.SCHEDULED:
            return scheduled()
