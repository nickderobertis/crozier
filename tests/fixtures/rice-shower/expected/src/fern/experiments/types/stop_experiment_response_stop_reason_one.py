

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StopExperimentResponseStopReasonOne(enum.StrEnum):
    OVERHEAT = "overheat"

    def visit(self, overheat: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopExperimentResponseStopReasonOne.OVERHEAT:
            return overheat()
