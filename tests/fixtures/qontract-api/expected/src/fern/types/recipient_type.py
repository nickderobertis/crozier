

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecipientType(enum.StrEnum):
    """
    Type of alert recipient.
    """

    EMAIL = "email"
    WEBHOOK = "webhook"

    def visit(self, email: typing.Callable[[], T_Result], webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is RecipientType.EMAIL:
            return email()
        if self is RecipientType.WEBHOOK:
            return webhook()
