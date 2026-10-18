

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StartExperimentResponseStopReasonThree(enum.StrEnum):
    EXTERNAL_STOP = "external_stop"

    def visit(self, external_stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartExperimentResponseStopReasonThree.EXTERNAL_STOP:
            return external_stop()
