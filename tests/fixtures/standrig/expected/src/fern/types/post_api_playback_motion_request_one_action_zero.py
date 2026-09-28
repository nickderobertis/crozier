

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestOneActionZero(enum.StrEnum):
    PLAY = "play"

    def visit(self, play: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestOneActionZero.PLAY:
            return play()
