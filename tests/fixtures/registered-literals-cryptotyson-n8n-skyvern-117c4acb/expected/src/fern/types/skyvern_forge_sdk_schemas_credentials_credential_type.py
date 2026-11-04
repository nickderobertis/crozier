

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkyvernForgeSdkSchemasCredentialsCredentialType(enum.StrEnum):
    """
    Type of credential stored in the system.
    """

    PASSWORD = "password"
    CREDIT_CARD = "credit_card"

    def visit(self, password: typing.Callable[[], T_Result], credit_card: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkyvernForgeSdkSchemasCredentialsCredentialType.PASSWORD:
            return password()
        if self is SkyvernForgeSdkSchemasCredentialsCredentialType.CREDIT_CARD:
            return credit_card()
