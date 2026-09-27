

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestOneActionTwo(enum.StrEnum):
    STOP = "stop"

    def visit(self, stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestOneActionTwo.STOP:
            return stop()
