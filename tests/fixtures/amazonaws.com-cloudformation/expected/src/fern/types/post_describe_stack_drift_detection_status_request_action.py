

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackDriftDetectionStatusRequestAction(str, enum.Enum):
    DESCRIBE_STACK_DRIFT_DETECTION_STATUS = "DescribeStackDriftDetectionStatus"

    def visit(self, describe_stack_drift_detection_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackDriftDetectionStatusRequestAction.DESCRIBE_STACK_DRIFT_DETECTION_STATUS:
            return describe_stack_drift_detection_status()
