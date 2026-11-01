

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetPlayerCmdSwitchModeRequestMode(enum.StrEnum):
    LINE_IN = "line-in"
    BLUETOOTH = "bluetooth"
    OPTICAL = "optical"
    UDISK = "udisk"
    WIFI = "wifi"
    HDMI = "HDMI"

    def visit(
        self,
        line_in: typing.Callable[[], T_Result],
        bluetooth: typing.Callable[[], T_Result],
        optical: typing.Callable[[], T_Result],
        udisk: typing.Callable[[], T_Result],
        wifi: typing.Callable[[], T_Result],
        hdmi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SetPlayerCmdSwitchModeRequestMode.LINE_IN:
            return line_in()
        if self is SetPlayerCmdSwitchModeRequestMode.BLUETOOTH:
            return bluetooth()
        if self is SetPlayerCmdSwitchModeRequestMode.OPTICAL:
            return optical()
        if self is SetPlayerCmdSwitchModeRequestMode.UDISK:
            return udisk()
        if self is SetPlayerCmdSwitchModeRequestMode.WIFI:
            return wifi()
        if self is SetPlayerCmdSwitchModeRequestMode.HDMI:
            return hdmi()
