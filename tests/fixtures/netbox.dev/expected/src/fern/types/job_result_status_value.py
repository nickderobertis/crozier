

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobResultStatusValue(str, enum.Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    ERRORED = "errored"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobResultStatusValue.PENDING:
            return pending()
        if self is JobResultStatusValue.SCHEDULED:
            return scheduled()
        if self is JobResultStatusValue.RUNNING:
            return running()
        if self is JobResultStatusValue.COMPLETED:
            return completed()
        if self is JobResultStatusValue.ERRORED:
            return errored()
        if self is JobResultStatusValue.FAILED:
            return failed()
