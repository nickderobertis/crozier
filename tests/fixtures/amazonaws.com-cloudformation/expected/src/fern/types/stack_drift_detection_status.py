

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackDriftDetectionStatus(enum.StrEnum):
    DETECTION_IN_PROGRESS = "DETECTION_IN_PROGRESS"
    DETECTION_FAILED = "DETECTION_FAILED"
    DETECTION_COMPLETE = "DETECTION_COMPLETE"

    def visit(
        self,
        detection_in_progress: typing.Callable[[], T_Result],
        detection_failed: typing.Callable[[], T_Result],
        detection_complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackDriftDetectionStatus.DETECTION_IN_PROGRESS:
            return detection_in_progress()
        if self is StackDriftDetectionStatus.DETECTION_FAILED:
            return detection_failed()
        if self is StackDriftDetectionStatus.DETECTION_COMPLETE:
            return detection_complete()
