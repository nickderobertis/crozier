

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped(enum.StrEnum):
    TRUE = "TRUE"
    FALSE = "FALSE"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped.TRUE:
            return true()
        if self is DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped.FALSE:
            return false()
