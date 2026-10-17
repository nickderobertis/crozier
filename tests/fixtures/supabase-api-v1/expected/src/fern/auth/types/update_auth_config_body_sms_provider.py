

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateAuthConfigBodySmsProvider(enum.StrEnum):
    MESSAGEBIRD = "messagebird"
    TEXTLOCAL = "textlocal"
    TWILIO = "twilio"
    TWILIO_VERIFY = "twilio_verify"
    VONAGE = "vonage"

    def visit(
        self,
        messagebird: typing.Callable[[], T_Result],
        textlocal: typing.Callable[[], T_Result],
        twilio: typing.Callable[[], T_Result],
        twilio_verify: typing.Callable[[], T_Result],
        vonage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateAuthConfigBodySmsProvider.MESSAGEBIRD:
            return messagebird()
        if self is UpdateAuthConfigBodySmsProvider.TEXTLOCAL:
            return textlocal()
        if self is UpdateAuthConfigBodySmsProvider.TWILIO:
            return twilio()
        if self is UpdateAuthConfigBodySmsProvider.TWILIO_VERIFY:
            return twilio_verify()
        if self is UpdateAuthConfigBodySmsProvider.VONAGE:
            return vonage()
