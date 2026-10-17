

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateInlineStreamRequestModeZeroItem(enum.StrEnum):
    TEMPERATURE = "temperature"
    POWER = "power"

    def visit(self, temperature: typing.Callable[[], T_Result], power: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateInlineStreamRequestModeZeroItem.TEMPERATURE:
            return temperature()
        if self is CreateInlineStreamRequestModeZeroItem.POWER:
            return power()
