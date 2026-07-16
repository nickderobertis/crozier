

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeStackDriftDetectionStatusOutputDetectionStatus(enum.StrEnum):
    """
    <p>The status of the stack drift detection operation.</p> <ul> <li> <p> <code>DETECTION_COMPLETE</code>: The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that don't currently support stack detection remain unchecked.)</p> <p>If you specified logical resource IDs for CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift.</p> </li> <li> <p> <code>DETECTION_FAILED</code>: The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which CloudFormation successfully completed drift detection.</p> </li> <li> <p> <code>DETECTION_IN_PROGRESS</code>: The stack drift detection operation is currently in progress.</p> </li> </ul>
    """

    DETECTION_IN_PROGRESS = "DETECTION_IN_PROGRESS"
    DETECTION_FAILED = "DETECTION_FAILED"
    DETECTION_COMPLETE = "DETECTION_COMPLETE"

    def visit(
        self,
        detection_in_progress: typing.Callable[[], T_Result],
        detection_failed: typing.Callable[[], T_Result],
        detection_complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeStackDriftDetectionStatusOutputDetectionStatus.DETECTION_IN_PROGRESS:
            return detection_in_progress()
        if self is DescribeStackDriftDetectionStatusOutputDetectionStatus.DETECTION_FAILED:
            return detection_failed()
        if self is DescribeStackDriftDetectionStatusOutputDetectionStatus.DETECTION_COMPLETE:
            return detection_complete()
