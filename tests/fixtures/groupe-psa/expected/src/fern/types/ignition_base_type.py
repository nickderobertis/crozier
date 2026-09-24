

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IgnitionBaseType(enum.StrEnum):
    STOP = "Stop"
    START_UP = "StartUp"
    START = "Start"

    def visit(
        self,
        stop: typing.Callable[[], T_Result],
        start_up: typing.Callable[[], T_Result],
        start: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IgnitionBaseType.STOP:
            return stop()
        if self is IgnitionBaseType.START_UP:
            return start_up()
        if self is IgnitionBaseType.START:
            return start()
