

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestClipAction(enum.StrEnum):
    LOAD = "load"

    def visit(self, load: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestClipAction.LOAD:
            return load()
