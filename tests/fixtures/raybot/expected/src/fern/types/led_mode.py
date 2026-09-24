

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LedMode(enum.StrEnum):
    """
    The mode of the led
    """

    OFF = "OFF"
    ON = "ON"
    BLINK = "BLINK"

    def visit(
        self,
        off: typing.Callable[[], T_Result],
        on: typing.Callable[[], T_Result],
        blink: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LedMode.OFF:
            return off()
        if self is LedMode.ON:
            return on()
        if self is LedMode.BLINK:
            return blink()
