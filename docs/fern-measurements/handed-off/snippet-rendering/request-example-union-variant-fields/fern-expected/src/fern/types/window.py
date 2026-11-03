

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Window(enum.StrEnum):
    HOURLY = "hourly"
    DAILY = "daily"

    def visit(self, hourly: typing.Callable[[], T_Result], daily: typing.Callable[[], T_Result]) -> T_Result:
        if self is Window.HOURLY:
            return hourly()
        if self is Window.DAILY:
            return daily()
