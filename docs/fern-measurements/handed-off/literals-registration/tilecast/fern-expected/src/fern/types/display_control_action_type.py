

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisplayControlActionType(enum.StrEnum):
    DISPLAY_POWER_ON = "display_power_on"
    DISPLAY_POWER_OFF = "display_power_off"
    DISPLAY_SET_INPUT = "display_set_input"
    DISPLAY_SET_VOLUME = "display_set_volume"
    DISPLAY_MUTE = "display_mute"
    DISPLAY_UNMUTE = "display_unmute"
    DISPLAY_SET_BRIGHTNESS = "display_set_brightness"

    def visit(
        self,
        display_power_on: typing.Callable[[], T_Result],
        display_power_off: typing.Callable[[], T_Result],
        display_set_input: typing.Callable[[], T_Result],
        display_set_volume: typing.Callable[[], T_Result],
        display_mute: typing.Callable[[], T_Result],
        display_unmute: typing.Callable[[], T_Result],
        display_set_brightness: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisplayControlActionType.DISPLAY_POWER_ON:
            return display_power_on()
        if self is DisplayControlActionType.DISPLAY_POWER_OFF:
            return display_power_off()
        if self is DisplayControlActionType.DISPLAY_SET_INPUT:
            return display_set_input()
        if self is DisplayControlActionType.DISPLAY_SET_VOLUME:
            return display_set_volume()
        if self is DisplayControlActionType.DISPLAY_MUTE:
            return display_mute()
        if self is DisplayControlActionType.DISPLAY_UNMUTE:
            return display_unmute()
        if self is DisplayControlActionType.DISPLAY_SET_BRIGHTNESS:
            return display_set_brightness()
