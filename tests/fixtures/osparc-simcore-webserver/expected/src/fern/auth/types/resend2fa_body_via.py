

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Resend2FaBodyVia(enum.StrEnum):
    SMS = "SMS"
    EMAIL = "Email"

    def visit(self, sms: typing.Callable[[], T_Result], email: typing.Callable[[], T_Result]) -> T_Result:
        if self is Resend2FaBodyVia.SMS:
            return sms()
        if self is Resend2FaBodyVia.EMAIL:
            return email()
