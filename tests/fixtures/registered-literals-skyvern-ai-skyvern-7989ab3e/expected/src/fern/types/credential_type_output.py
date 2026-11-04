

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CredentialTypeOutput(enum.StrEnum):
    """
    Type of credential stored in the system.
    """

    PASSWORD = "password"
    CREDIT_CARD = "credit_card"
    SECRET = "secret"

    def visit(
        self,
        password: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        secret: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CredentialTypeOutput.PASSWORD:
            return password()
        if self is CredentialTypeOutput.CREDIT_CARD:
            return credit_card()
        if self is CredentialTypeOutput.SECRET:
            return secret()
