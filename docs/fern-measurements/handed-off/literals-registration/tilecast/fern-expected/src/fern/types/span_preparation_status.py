

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpanPreparationStatus(enum.StrEnum):
    QUEUED = "queued"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SpanPreparationStatus.QUEUED:
            return queued()
        if self is SpanPreparationStatus.PROCESSING:
            return processing()
        if self is SpanPreparationStatus.READY:
            return ready()
        if self is SpanPreparationStatus.FAILED:
            return failed()
