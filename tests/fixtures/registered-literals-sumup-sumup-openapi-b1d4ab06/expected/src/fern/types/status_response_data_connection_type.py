

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusResponseDataConnectionType(enum.StrEnum):
    """
    Type of connection used by the device
    """

    BTLE = "btle"
    EDGE = "edge"
    GPRS = "gprs"
    LTE = "lte"
    UMTS = "umts"
    USB = "usb"
    WI_FI = "Wi-Fi"

    def visit(
        self,
        btle: typing.Callable[[], T_Result],
        edge: typing.Callable[[], T_Result],
        gprs: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        umts: typing.Callable[[], T_Result],
        usb: typing.Callable[[], T_Result],
        wi_fi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusResponseDataConnectionType.BTLE:
            return btle()
        if self is StatusResponseDataConnectionType.EDGE:
            return edge()
        if self is StatusResponseDataConnectionType.GPRS:
            return gprs()
        if self is StatusResponseDataConnectionType.LTE:
            return lte()
        if self is StatusResponseDataConnectionType.UMTS:
            return umts()
        if self is StatusResponseDataConnectionType.USB:
            return usb()
        if self is StatusResponseDataConnectionType.WI_FI:
            return wi_fi()
