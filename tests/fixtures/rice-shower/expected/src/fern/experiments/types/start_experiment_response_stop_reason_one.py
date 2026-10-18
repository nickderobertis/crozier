

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StartExperimentResponseStopReasonOne(enum.StrEnum):
    OVERHEAT = "overheat"

    def visit(self, overheat: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartExperimentResponseStopReasonOne.OVERHEAT:
            return overheat()
