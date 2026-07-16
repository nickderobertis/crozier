

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus(enum.StrEnum):
    """
    <p>The status of the stack set drift detection operation.</p> <ul> <li> <p> <code>COMPLETED</code>: The drift detection operation completed without failing on any stack instances.</p> </li> <li> <p> <code>FAILED</code>: The drift detection operation exceeded the specified failure tolerance.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: The drift detection operation completed without exceeding the failure tolerance for the operation.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The drift detection operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the drift detection operation.</p> </li> </ul>
    """

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        partial_success: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus.COMPLETED
        ):
            return completed()
        if (
            self
            is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus.FAILED
        ):
            return failed()
        if (
            self
            is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus.PARTIAL_SUCCESS
        ):
            return partial_success()
        if (
            self
            is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus.IN_PROGRESS
        ):
            return in_progress()
        if (
            self
            is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus.STOPPED
        ):
            return stopped()
