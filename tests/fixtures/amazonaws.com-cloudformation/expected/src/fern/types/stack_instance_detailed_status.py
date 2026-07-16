

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackInstanceDetailedStatus(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    INOPERABLE = "INOPERABLE"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        inoperable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackInstanceDetailedStatus.PENDING:
            return pending()
        if self is StackInstanceDetailedStatus.RUNNING:
            return running()
        if self is StackInstanceDetailedStatus.SUCCEEDED:
            return succeeded()
        if self is StackInstanceDetailedStatus.FAILED:
            return failed()
        if self is StackInstanceDetailedStatus.CANCELLED:
            return cancelled()
        if self is StackInstanceDetailedStatus.INOPERABLE:
            return inoperable()
