

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationReadStatus(enum.StrEnum):
    """
    A retained current observation may coexist with a failed latest refresh.
    """

    OK = "ok"
    PARTIAL = "partial"
    FAILED = "failed"
    UNREAD = "unread"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unread: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationReadStatus.OK:
            return ok()
        if self is MetricObservationReadStatus.PARTIAL:
            return partial()
        if self is MetricObservationReadStatus.FAILED:
            return failed()
        if self is MetricObservationReadStatus.UNREAD:
            return unread()
