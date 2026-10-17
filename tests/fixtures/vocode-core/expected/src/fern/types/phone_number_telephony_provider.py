

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhoneNumberTelephonyProvider(enum.StrEnum):
    VONAGE = "vonage"
    TWILIO = "twilio"

    def visit(self, vonage: typing.Callable[[], T_Result], twilio: typing.Callable[[], T_Result]) -> T_Result:
        if self is PhoneNumberTelephonyProvider.VONAGE:
            return vonage()
        if self is PhoneNumberTelephonyProvider.TWILIO:
            return twilio()
