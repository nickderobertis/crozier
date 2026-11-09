

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Platform(enum.StrEnum):
    APNS = "apns"
    FCM = "fcm"

    def visit(self, apns: typing.Callable[[], T_Result], fcm: typing.Callable[[], T_Result]) -> T_Result:
        if self is Platform.APNS:
            return apns()
        if self is Platform.FCM:
            return fcm()
