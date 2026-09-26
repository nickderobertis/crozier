

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCalendarEventsRequestFilterCalendarRange(enum.StrEnum):
    DAY = "DAY"
    THREE_DAY = "THREE_DAY"
    WEEK = "WEEK"
    FORTNIGHT = "FORTNIGHT"
    MONTH = "MONTH"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        three_day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        fortnight: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCalendarEventsRequestFilterCalendarRange.DAY:
            return day()
        if self is GetCalendarEventsRequestFilterCalendarRange.THREE_DAY:
            return three_day()
        if self is GetCalendarEventsRequestFilterCalendarRange.WEEK:
            return week()
        if self is GetCalendarEventsRequestFilterCalendarRange.FORTNIGHT:
            return fortnight()
        if self is GetCalendarEventsRequestFilterCalendarRange.MONTH:
            return month()
