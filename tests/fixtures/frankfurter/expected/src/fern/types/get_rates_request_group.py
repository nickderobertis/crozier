

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRatesRequestGroup(enum.StrEnum):
    WEEK = "week"
    MONTH = "month"

    def visit(self, week: typing.Callable[[], T_Result], month: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRatesRequestGroup.WEEK:
            return week()
        if self is GetRatesRequestGroup.MONTH:
            return month()
