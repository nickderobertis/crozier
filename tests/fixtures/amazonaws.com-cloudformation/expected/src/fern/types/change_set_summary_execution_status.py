

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetSummaryExecutionStatus(enum.StrEnum):
    """
    If the change set execution status is <code>AVAILABLE</code>, you can execute the change set. If you can't execute the change set, the status indicates why. For example, a change set might be in an <code>UNAVAILABLE</code> state because CloudFormation is still creating it or in an <code>OBSOLETE</code> state because the stack was already updated.
    """

    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    OBSOLETE = "OBSOLETE"

    def visit(
        self,
        unavailable: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        execute_in_progress: typing.Callable[[], T_Result],
        execute_complete: typing.Callable[[], T_Result],
        execute_failed: typing.Callable[[], T_Result],
        obsolete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetSummaryExecutionStatus.UNAVAILABLE:
            return unavailable()
        if self is ChangeSetSummaryExecutionStatus.AVAILABLE:
            return available()
        if self is ChangeSetSummaryExecutionStatus.EXECUTE_IN_PROGRESS:
            return execute_in_progress()
        if self is ChangeSetSummaryExecutionStatus.EXECUTE_COMPLETE:
            return execute_complete()
        if self is ChangeSetSummaryExecutionStatus.EXECUTE_FAILED:
            return execute_failed()
        if self is ChangeSetSummaryExecutionStatus.OBSOLETE:
            return obsolete()
