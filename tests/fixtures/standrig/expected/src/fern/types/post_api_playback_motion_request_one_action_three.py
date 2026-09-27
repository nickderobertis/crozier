

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestOneActionThree(enum.StrEnum):
    CLEAR = "clear"

    def visit(self, clear: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestOneActionThree.CLEAR:
            return clear()
