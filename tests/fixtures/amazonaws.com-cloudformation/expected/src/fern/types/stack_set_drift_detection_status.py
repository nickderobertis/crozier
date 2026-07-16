

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackSetDriftDetectionStatus(str, enum.Enum):
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
        if self is StackSetDriftDetectionStatus.COMPLETED:
            return completed()
        if self is StackSetDriftDetectionStatus.FAILED:
            return failed()
        if self is StackSetDriftDetectionStatus.PARTIAL_SUCCESS:
            return partial_success()
        if self is StackSetDriftDetectionStatus.IN_PROGRESS:
            return in_progress()
        if self is StackSetDriftDetectionStatus.STOPPED:
            return stopped()
