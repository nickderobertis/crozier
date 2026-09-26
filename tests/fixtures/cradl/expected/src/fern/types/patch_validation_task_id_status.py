

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchValidationTaskIdStatus(enum.StrEnum):
    READY = "ready"
    IN_PROGRESS = "in-progress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchValidationTaskIdStatus.READY:
            return ready()
        if self is PatchValidationTaskIdStatus.IN_PROGRESS:
            return in_progress()
        if self is PatchValidationTaskIdStatus.SUCCEEDED:
            return succeeded()
        if self is PatchValidationTaskIdStatus.FAILED:
            return failed()
        if self is PatchValidationTaskIdStatus.CANCELLED:
            return cancelled()
