

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SignatureRequestNotificationMethod(enum.StrEnum):
    EMAIL = "email"
    SMS = "sms"
    APP = "app"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        app: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignatureRequestNotificationMethod.EMAIL:
            return email()
        if self is SignatureRequestNotificationMethod.SMS:
            return sms()
        if self is SignatureRequestNotificationMethod.APP:
            return app()
