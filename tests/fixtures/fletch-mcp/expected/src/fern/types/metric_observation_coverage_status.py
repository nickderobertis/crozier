

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationCoverageStatus(enum.StrEnum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    UNKNOWN = "unknown"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationCoverageStatus.COMPLETE:
            return complete()
        if self is MetricObservationCoverageStatus.PARTIAL:
            return partial()
        if self is MetricObservationCoverageStatus.UNKNOWN:
            return unknown()
