

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackSetOperationResultStatus(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetOperationResultStatus.PENDING:
            return pending()
        if self is StackSetOperationResultStatus.RUNNING:
            return running()
        if self is StackSetOperationResultStatus.SUCCEEDED:
            return succeeded()
        if self is StackSetOperationResultStatus.FAILED:
            return failed()
        if self is StackSetOperationResultStatus.CANCELLED:
            return cancelled()
