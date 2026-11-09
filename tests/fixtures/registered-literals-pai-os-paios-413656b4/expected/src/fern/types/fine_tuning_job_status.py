

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningJobStatus(enum.StrEnum):
    """
    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
    """

    VALIDATING_FILES = "validating_files"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        validating_files: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FineTuningJobStatus.VALIDATING_FILES:
            return validating_files()
        if self is FineTuningJobStatus.QUEUED:
            return queued()
        if self is FineTuningJobStatus.RUNNING:
            return running()
        if self is FineTuningJobStatus.SUCCEEDED:
            return succeeded()
        if self is FineTuningJobStatus.FAILED:
            return failed()
        if self is FineTuningJobStatus.CANCELLED:
            return cancelled()
