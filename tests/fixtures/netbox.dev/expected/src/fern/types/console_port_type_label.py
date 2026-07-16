

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConsolePortTypeLabel(str, enum.Enum):
    DE9 = "DE-9"
    DB25 = "DB-25"
    RJ11 = "RJ-11"
    RJ12 = "RJ-12"
    RJ45 = "RJ-45"
    MINI_DIN8 = "Mini-DIN 8"
    USB_TYPE_A = "USB Type A"
    USB_TYPE_B = "USB Type B"
    USB_TYPE_C = "USB Type C"
    USB_MINI_A = "USB Mini A"
    USB_MINI_B = "USB Mini B"
    USB_MICRO_A = "USB Micro A"
    USB_MICRO_B = "USB Micro B"
    USB_MICRO_AB = "USB Micro AB"
    OTHER = "Other"

    def visit(
        self,
        de9: typing.Callable[[], T_Result],
        db25: typing.Callable[[], T_Result],
        rj11: typing.Callable[[], T_Result],
        rj12: typing.Callable[[], T_Result],
        rj45: typing.Callable[[], T_Result],
        mini_din8: typing.Callable[[], T_Result],
        usb_type_a: typing.Callable[[], T_Result],
        usb_type_b: typing.Callable[[], T_Result],
        usb_type_c: typing.Callable[[], T_Result],
        usb_mini_a: typing.Callable[[], T_Result],
        usb_mini_b: typing.Callable[[], T_Result],
        usb_micro_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_micro_ab: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsolePortTypeLabel.DE9:
            return de9()
        if self is ConsolePortTypeLabel.DB25:
            return db25()
        if self is ConsolePortTypeLabel.RJ11:
            return rj11()
        if self is ConsolePortTypeLabel.RJ12:
            return rj12()
        if self is ConsolePortTypeLabel.RJ45:
            return rj45()
        if self is ConsolePortTypeLabel.MINI_DIN8:
            return mini_din8()
        if self is ConsolePortTypeLabel.USB_TYPE_A:
            return usb_type_a()
        if self is ConsolePortTypeLabel.USB_TYPE_B:
            return usb_type_b()
        if self is ConsolePortTypeLabel.USB_TYPE_C:
            return usb_type_c()
        if self is ConsolePortTypeLabel.USB_MINI_A:
            return usb_mini_a()
        if self is ConsolePortTypeLabel.USB_MINI_B:
            return usb_mini_b()
        if self is ConsolePortTypeLabel.USB_MICRO_A:
            return usb_micro_a()
        if self is ConsolePortTypeLabel.USB_MICRO_B:
            return usb_micro_b()
        if self is ConsolePortTypeLabel.USB_MICRO_AB:
            return usb_micro_ab()
        if self is ConsolePortTypeLabel.OTHER:
            return other()
