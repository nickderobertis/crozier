

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInteractionKind(enum.StrEnum):
    """
    `connection` is a deprecated compatibility alias until the runtime migration ships.
    """

    AUTHENTICATION = "authentication"
    CONNECTION = "connection"

    def visit(
        self, authentication: typing.Callable[[], T_Result], connection: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AuthenticationInteractionKind.AUTHENTICATION:
            return authentication()
        if self is AuthenticationInteractionKind.CONNECTION:
            return connection()
