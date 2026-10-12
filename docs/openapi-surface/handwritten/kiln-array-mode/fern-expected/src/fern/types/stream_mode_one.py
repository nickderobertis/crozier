

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamModeOne(enum.StrEnum):
    TEMPERATURE = "temperature"
    POWER = "power"

    def visit(self, temperature: typing.Callable[[], T_Result], power: typing.Callable[[], T_Result]) -> T_Result:
        if self is StreamModeOne.TEMPERATURE:
            return temperature()
        if self is StreamModeOne.POWER:
            return power()
