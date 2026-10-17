

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StopExperimentResponseStopReasonTwo(enum.StrEnum):
    SENSOR_TIMEOUT = "sensor_timeout"

    def visit(self, sensor_timeout: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopExperimentResponseStopReasonTwo.SENSOR_TIMEOUT:
            return sensor_timeout()
