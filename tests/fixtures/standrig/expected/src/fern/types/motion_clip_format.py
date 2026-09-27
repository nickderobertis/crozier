

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionClipFormat(enum.StrEnum):
    STANDRIG_MOTION = "standrig-motion"

    def visit(self, standrig_motion: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionClipFormat.STANDRIG_MOTION:
            return standrig_motion()
