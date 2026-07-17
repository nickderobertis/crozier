

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobResultStatusLabel(enum.StrEnum):
    PENDING = "Pending"
    SCHEDULED = "Scheduled"
    RUNNING = "Running"
    COMPLETED = "Completed"
    ERRORED = "Errored"
    FAILED = "Failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobResultStatusLabel.PENDING:
            return pending()
        if self is JobResultStatusLabel.SCHEDULED:
            return scheduled()
        if self is JobResultStatusLabel.RUNNING:
            return running()
        if self is JobResultStatusLabel.COMPLETED:
            return completed()
        if self is JobResultStatusLabel.ERRORED:
            return errored()
        if self is JobResultStatusLabel.FAILED:
            return failed()
