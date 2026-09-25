

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilterReportsRequestScope(enum.StrEnum):
    TOTALS = "totals"
    EVENTS = "events"

    def visit(self, totals: typing.Callable[[], T_Result], events: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterReportsRequestScope.TOTALS:
            return totals()
        if self is FilterReportsRequestScope.EVENTS:
            return events()
