

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationQualityStatus(enum.StrEnum):
    ACCEPTED = "accepted"

    def visit(self, accepted: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricObservationQualityStatus.ACCEPTED:
            return accepted()
