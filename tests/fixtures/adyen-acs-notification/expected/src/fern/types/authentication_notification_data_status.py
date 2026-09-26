

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationNotificationDataStatus(enum.StrEnum):
    """
    Outcome of the authentication.
    Allowed values:
    * authenticated
    * rejected
    * error
    """

    AUTHENTICATED = "authenticated"
    REJECTED = "rejected"
    ERROR = "error"

    def visit(
        self,
        authenticated: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationNotificationDataStatus.AUTHENTICATED:
            return authenticated()
        if self is AuthenticationNotificationDataStatus.REJECTED:
            return rejected()
        if self is AuthenticationNotificationDataStatus.ERROR:
            return error()
