

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadingMode(enum.StrEnum):
    IDLE = "idle"
    LIVE = "live"

    def visit(self, idle: typing.Callable[[], T_Result], live: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadingMode.IDLE:
            return idle()
        if self is ReadingMode.LIVE:
            return live()
