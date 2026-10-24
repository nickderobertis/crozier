

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BriefingMetricFormat(enum.StrEnum):
    AMOUNT = "amount"
    INTEGER = "integer"
    PERCENT = "percent"

    def visit(
        self,
        amount: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        percent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BriefingMetricFormat.AMOUNT:
            return amount()
        if self is BriefingMetricFormat.INTEGER:
            return integer()
        if self is BriefingMetricFormat.PERCENT:
            return percent()
