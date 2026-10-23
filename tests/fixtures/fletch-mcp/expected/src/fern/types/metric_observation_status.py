

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationStatus(enum.StrEnum):
    """
    Timestamp validity and freshness, separate from read success and coverage.
    """

    CURRENT = "current"
    STALE = "stale"
    MISSING = "missing"
    INVALID = "invalid"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationStatus.CURRENT:
            return current()
        if self is MetricObservationStatus.STALE:
            return stale()
        if self is MetricObservationStatus.MISSING:
            return missing()
        if self is MetricObservationStatus.INVALID:
            return invalid()
