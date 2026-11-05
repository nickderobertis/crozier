

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewDisplayGroupControlRequestCommandType(enum.StrEnum):
    DISPLAY_POWER_ON = "display_power_on"
    DISPLAY_POWER_OFF = "display_power_off"
    DISPLAY_MUTE = "display_mute"
    DISPLAY_UNMUTE = "display_unmute"

    def visit(
        self,
        display_power_on: typing.Callable[[], T_Result],
        display_power_off: typing.Callable[[], T_Result],
        display_mute: typing.Callable[[], T_Result],
        display_unmute: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreviewDisplayGroupControlRequestCommandType.DISPLAY_POWER_ON:
            return display_power_on()
        if self is PreviewDisplayGroupControlRequestCommandType.DISPLAY_POWER_OFF:
            return display_power_off()
        if self is PreviewDisplayGroupControlRequestCommandType.DISPLAY_MUTE:
            return display_mute()
        if self is PreviewDisplayGroupControlRequestCommandType.DISPLAY_UNMUTE:
            return display_unmute()
