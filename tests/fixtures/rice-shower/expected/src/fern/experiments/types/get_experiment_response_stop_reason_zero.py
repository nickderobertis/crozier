

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetExperimentResponseStopReasonZero(enum.StrEnum):
    MANUAL = "manual"

    def visit(self, manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetExperimentResponseStopReasonZero.MANUAL:
            return manual()
