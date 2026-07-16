

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsoleServerPortTypeValue(enum.StrEnum):
    DE9 = "de-9"
    DB25 = "db-25"
    RJ11 = "rj-11"
    RJ12 = "rj-12"
    RJ45 = "rj-45"
    MINI_DIN8 = "mini-din-8"
    USB_A = "usb-a"
    USB_B = "usb-b"
    USB_C = "usb-c"
    USB_MINI_A = "usb-mini-a"
    USB_MINI_B = "usb-mini-b"
    USB_MICRO_A = "usb-micro-a"
    USB_MICRO_B = "usb-micro-b"
    USB_MICRO_AB = "usb-micro-ab"
    OTHER = "other"

    def visit(
        self,
        de9: typing.Callable[[], T_Result],
        db25: typing.Callable[[], T_Result],
        rj11: typing.Callable[[], T_Result],
        rj12: typing.Callable[[], T_Result],
        rj45: typing.Callable[[], T_Result],
        mini_din8: typing.Callable[[], T_Result],
        usb_a: typing.Callable[[], T_Result],
        usb_b: typing.Callable[[], T_Result],
        usb_c: typing.Callable[[], T_Result],
        usb_mini_a: typing.Callable[[], T_Result],
        usb_mini_b: typing.Callable[[], T_Result],
        usb_micro_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_micro_ab: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsoleServerPortTypeValue.DE9:
            return de9()
        if self is ConsoleServerPortTypeValue.DB25:
            return db25()
        if self is ConsoleServerPortTypeValue.RJ11:
            return rj11()
        if self is ConsoleServerPortTypeValue.RJ12:
            return rj12()
        if self is ConsoleServerPortTypeValue.RJ45:
            return rj45()
        if self is ConsoleServerPortTypeValue.MINI_DIN8:
            return mini_din8()
        if self is ConsoleServerPortTypeValue.USB_A:
            return usb_a()
        if self is ConsoleServerPortTypeValue.USB_B:
            return usb_b()
        if self is ConsoleServerPortTypeValue.USB_C:
            return usb_c()
        if self is ConsoleServerPortTypeValue.USB_MINI_A:
            return usb_mini_a()
        if self is ConsoleServerPortTypeValue.USB_MINI_B:
            return usb_mini_b()
        if self is ConsoleServerPortTypeValue.USB_MICRO_A:
            return usb_micro_a()
        if self is ConsoleServerPortTypeValue.USB_MICRO_B:
            return usb_micro_b()
        if self is ConsoleServerPortTypeValue.USB_MICRO_AB:
            return usb_micro_ab()
        if self is ConsoleServerPortTypeValue.OTHER:
            return other()
