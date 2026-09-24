

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsUnit(enum.StrEnum):
    COUNT = "count"
    USD = "$"
    MS = "ms"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricsUnit.COUNT:
            return count()
        if self is MetricsUnit.USD:
            return usd()
        if self is MetricsUnit.MS:
            return ms()
