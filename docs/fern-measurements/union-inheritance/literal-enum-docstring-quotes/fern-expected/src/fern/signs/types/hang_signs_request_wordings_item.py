

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class HangSignsRequestWordingsItem(enum.StrEnum):
    SAY_CHEESE = 'say "cheese"'
    OPEN_LATE = "open late"

    def visit(self, say_cheese: typing.Callable[[], T_Result], open_late: typing.Callable[[], T_Result]) -> T_Result:
        if self is HangSignsRequestWordingsItem.SAY_CHEESE:
            return say_cheese()
        if self is HangSignsRequestWordingsItem.OPEN_LATE:
            return open_late()
