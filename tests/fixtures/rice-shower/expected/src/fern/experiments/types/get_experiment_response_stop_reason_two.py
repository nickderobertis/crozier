

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetExperimentResponseStopReasonTwo(enum.StrEnum):
    SENSOR_TIMEOUT = "sensor_timeout"

    def visit(self, sensor_timeout: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetExperimentResponseStopReasonTwo.SENSOR_TIMEOUT:
            return sensor_timeout()
