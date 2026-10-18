

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StartExperimentResponseStopReasonZero(enum.StrEnum):
    MANUAL = "manual"

    def visit(self, manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartExperimentResponseStopReasonZero.MANUAL:
            return manual()
