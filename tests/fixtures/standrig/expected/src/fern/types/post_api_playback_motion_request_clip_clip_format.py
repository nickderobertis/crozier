

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestClipClipFormat(enum.StrEnum):
    STANDRIG_MOTION = "standrig-motion"

    def visit(self, standrig_motion: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestClipClipFormat.STANDRIG_MOTION:
            return standrig_motion()
