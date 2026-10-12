

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamModeZeroItem(enum.StrEnum):
    TEMPERATURE = "temperature"
    POWER = "power"

    def visit(self, temperature: typing.Callable[[], T_Result], power: typing.Callable[[], T_Result]) -> T_Result:
        if self is StreamModeZeroItem.TEMPERATURE:
            return temperature()
        if self is StreamModeZeroItem.POWER:
            return power()
