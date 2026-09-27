

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEnrollmentsV3RequestGroupBy(enum.StrEnum):
    MONTH = "month"
    PERIOD = "period"

    def visit(self, month: typing.Callable[[], T_Result], period: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEnrollmentsV3RequestGroupBy.MONTH:
            return month()
        if self is GetEnrollmentsV3RequestGroupBy.PERIOD:
            return period()
