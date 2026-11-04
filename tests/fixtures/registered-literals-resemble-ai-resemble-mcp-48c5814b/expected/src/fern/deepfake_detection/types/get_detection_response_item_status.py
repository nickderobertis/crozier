

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDetectionResponseItemStatus(enum.StrEnum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDetectionResponseItemStatus.PROCESSING:
            return processing()
        if self is GetDetectionResponseItemStatus.COMPLETED:
            return completed()
        if self is GetDetectionResponseItemStatus.FAILED:
            return failed()
