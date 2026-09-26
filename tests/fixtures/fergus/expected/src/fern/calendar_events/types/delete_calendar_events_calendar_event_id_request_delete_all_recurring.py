

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring(enum.StrEnum):
    TRUE = "TRUE"
    FALSE = "FALSE"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring.TRUE:
            return true()
        if self is DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring.FALSE:
            return false()
