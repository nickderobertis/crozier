

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStagesStageStatus(enum.StrEnum):
    """
    Status of the job stage.
    """

    NONE = "None"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"
    SUCCEEDED_WITH_ERRORS = "SucceededWithErrors"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        cancelling: typing.Callable[[], T_Result],
        succeeded_with_errors: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStagesStageStatus.NONE:
            return none()
        if self is JobStagesStageStatus.IN_PROGRESS:
            return in_progress()
        if self is JobStagesStageStatus.SUCCEEDED:
            return succeeded()
        if self is JobStagesStageStatus.FAILED:
            return failed()
        if self is JobStagesStageStatus.CANCELLED:
            return cancelled()
        if self is JobStagesStageStatus.CANCELLING:
            return cancelling()
        if self is JobStagesStageStatus.SUCCEEDED_WITH_ERRORS:
            return succeeded_with_errors()
