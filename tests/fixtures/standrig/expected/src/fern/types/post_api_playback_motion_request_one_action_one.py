

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestOneActionOne(enum.StrEnum):
    PAUSE = "pause"

    def visit(self, pause: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestOneActionOne.PAUSE:
            return pause()
