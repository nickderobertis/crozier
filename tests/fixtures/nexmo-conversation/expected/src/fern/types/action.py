

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Action(enum.StrEnum):
    """
    Recording Action
    """

    START = "start"
    STOP = "stop"

    def visit(self, start: typing.Callable[[], T_Result], stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is Action.START:
            return start()
        if self is Action.STOP:
            return stop()
