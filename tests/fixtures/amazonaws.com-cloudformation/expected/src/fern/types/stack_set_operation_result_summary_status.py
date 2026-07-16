

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationResultSummaryStatus(enum.StrEnum):
    """
    <p>The result status of the stack set operation for the given account in the given Region.</p> <ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed.</p> <p>If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>
    """

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
        if self is StackSetOperationResultSummaryStatus.PENDING:
            return pending()
        if self is StackSetOperationResultSummaryStatus.RUNNING:
            return running()
        if self is StackSetOperationResultSummaryStatus.SUCCEEDED:
            return succeeded()
        if self is StackSetOperationResultSummaryStatus.FAILED:
            return failed()
        if self is StackSetOperationResultSummaryStatus.CANCELLED:
            return cancelled()
