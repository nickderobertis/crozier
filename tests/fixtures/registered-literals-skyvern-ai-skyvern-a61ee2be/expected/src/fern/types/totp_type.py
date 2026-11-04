

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TotpType(enum.StrEnum):
    """
    Type of 2FA/TOTP method used.
    """

    AUTHENTICATOR = "authenticator"
    EMAIL = "email"
    TEXT = "text"
    PASSKEY = "passkey"
    NONE = "none"

    def visit(
        self,
        authenticator: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        passkey: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TotpType.AUTHENTICATOR:
            return authenticator()
        if self is TotpType.EMAIL:
            return email()
        if self is TotpType.TEXT:
            return text()
        if self is TotpType.PASSKEY:
            return passkey()
        if self is TotpType.NONE:
            return none()
