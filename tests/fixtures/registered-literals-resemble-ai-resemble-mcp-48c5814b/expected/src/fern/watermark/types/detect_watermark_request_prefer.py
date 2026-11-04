

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DetectWatermarkRequestPrefer(enum.StrEnum):
    WAIT = "wait"

    def visit(self, wait: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetectWatermarkRequestPrefer.WAIT:
            return wait()
