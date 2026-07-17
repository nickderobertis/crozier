

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackInstanceComprehensiveStatusDetailedStatus(enum.StrEnum):
    """
    <ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed. If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.</p> </li> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to <code>true</code>, to delete the stack instance, and then delete the stack manually.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>
    """

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
        if self is StackInstanceComprehensiveStatusDetailedStatus.PENDING:
            return pending()
        if self is StackInstanceComprehensiveStatusDetailedStatus.RUNNING:
            return running()
        if self is StackInstanceComprehensiveStatusDetailedStatus.SUCCEEDED:
            return succeeded()
        if self is StackInstanceComprehensiveStatusDetailedStatus.FAILED:
            return failed()
        if self is StackInstanceComprehensiveStatusDetailedStatus.CANCELLED:
            return cancelled()
        if self is StackInstanceComprehensiveStatusDetailedStatus.INOPERABLE:
            return inoperable()
