

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationUnit(enum.StrEnum):
    COUNT = "count"
    CURRENCY = "currency"
    RATIO = "ratio"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        currency: typing.Callable[[], T_Result],
        ratio: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationUnit.COUNT:
            return count()
        if self is MetricObservationUnit.CURRENCY:
            return currency()
        if self is MetricObservationUnit.RATIO:
            return ratio()
