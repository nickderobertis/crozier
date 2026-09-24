

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCalendarEventsCalendarEventIdRequestRepeatEndType(enum.StrEnum):
    NEVER = "NEVER"
    ON_DATE = "ON_DATE"
    AFTER = "AFTER"

    def visit(
        self,
        never: typing.Callable[[], T_Result],
        on_date: typing.Callable[[], T_Result],
        after: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostCalendarEventsCalendarEventIdRequestRepeatEndType.NEVER:
            return never()
        if self is PostCalendarEventsCalendarEventIdRequestRepeatEndType.ON_DATE:
            return on_date()
        if self is PostCalendarEventsCalendarEventIdRequestRepeatEndType.AFTER:
            return after()
