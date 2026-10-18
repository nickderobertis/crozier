

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NormalizedCallTelephonyProvider(enum.StrEnum):
    VONAGE = "vonage"
    TWILIO = "twilio"

    def visit(self, vonage: typing.Callable[[], T_Result], twilio: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormalizedCallTelephonyProvider.VONAGE:
            return vonage()
        if self is NormalizedCallTelephonyProvider.TWILIO:
            return twilio()
