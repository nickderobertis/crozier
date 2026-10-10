

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BookYardRequestSlot(enum.StrEnum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    NIGHT = "night"

    def visit(
        self,
        morning: typing.Callable[[], T_Result],
        afternoon: typing.Callable[[], T_Result],
        night: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BookYardRequestSlot.MORNING:
            return morning()
        if self is BookYardRequestSlot.AFTERNOON:
            return afternoon()
        if self is BookYardRequestSlot.NIGHT:
            return night()
