

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApplyWatermarkRequestPrefer(enum.StrEnum):
    WAIT = "wait"

    def visit(self, wait: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApplyWatermarkRequestPrefer.WAIT:
            return wait()
