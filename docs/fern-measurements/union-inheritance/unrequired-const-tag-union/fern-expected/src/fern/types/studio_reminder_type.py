

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudioReminderType(enum.StrEnum):
    REMINDER = "reminder"

    def visit(self, reminder: typing.Callable[[], T_Result]) -> T_Result:
        if self is StudioReminderType.REMINDER:
            return reminder()
