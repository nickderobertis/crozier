

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateInlineStreamRequestModeOne(enum.StrEnum):
    TEMPERATURE = "temperature"
    POWER = "power"

    def visit(self, temperature: typing.Callable[[], T_Result], power: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateInlineStreamRequestModeOne.TEMPERATURE:
            return temperature()
        if self is CreateInlineStreamRequestModeOne.POWER:
            return power()
